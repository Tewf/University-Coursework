# The maths

Twelve thermometers, 460 000 pixels. This page is the one idea that bridges them.

## The problem

We know the temperature in Lyon and in Brest. What is it in Dijon, where nobody
measured? Any answer is a guess, but some guesses are much better than others,
and the good ones all share one rule: **near things count more than far things.**

## Weighted average

The plain average of Lyon (29.3) and Brest (19.8) is 24.6 — the same answer
everywhere in France, which is useless. A *weighted* average lets each city
count a different amount:

```
                w_Lyon * 29.3  +  w_Brest * 19.8
temperature =  ----------------------------------
                     w_Lyon  +  w_Brest
```

Dividing by the total weight is what makes it an average rather than a sum. It
also guarantees the answer sits between 19.8 and 29.3 — which is why the colour
scale can be pinned to the coldest and hottest cities and be exactly right, with
no colour wasted at either end.

## Choosing the weights

We want a weight that is large at the city and fades with distance. The Gaussian
— the bell curve — does exactly that:

```
w = exp( -d² / (2 · spread²) )
```

At the city itself `d = 0`, so `w = exp(0) = 1`, the largest it ever gets. One
`spread` away it has fallen to about 0.61, two spreads to 0.14, three to 0.011.
Nothing is ever exactly zero, which is convenient: every pixel always has *some*
total weight to divide by, so the formula never breaks.

`INFLUENCE_SPREAD_DEGREES` is that `spread`, set to 2.0 — roughly 200 km. Turn
it down to 0.5 and each city becomes an isolated blob with cold gaps between
them; turn it up to 10 and the whole country flattens towards one average
colour. Try both, it is one number in `configuration.py`.

This method has a name worth knowing — **Nadaraya–Watson kernel regression** —
and searching for it will show you the same formula written more formally.

## Why the loop runs over cities, not pixels

The obvious way to write it is two nested loops over the 460 000 pixels, doing
twelve small calculations in each. In Python that takes minutes.

`interpolate` instead loops **twelve times**, once per city, and each line
inside works on the entire grid at once:

```python
squared_distance = (longitudes - longitude) ** 2 + (latitudes - latitude) ** 2
```

`longitudes` is a whole 2-D array, so that one line does 460 000 subtractions in
compiled code. The whole interpolation takes 0.07 s. This is the single most
useful habit numpy teaches: **loop over the few, not over the many.**

---

← [reusing the code](reusing-the-code.md)  ·  [guide](README.md)
