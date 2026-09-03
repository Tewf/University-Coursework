# Python TP2: Image processing with Numpy

Images as Numpy arrays: loading, greyscale, padding, convolution, blurring and edge detection.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Write a Python function that takes as input the path to an image file, loads the image using Image module from Pillow and returns a Numpy array |
| 2 | Write a Python function that takes as input a Numpy array Programming You can use the function Image.fromarray to convert a Numpy array to a Pillow image |
| 3 | Implement a function that takes as input a Numpy array repre- senting a colored image and returns a Numpy array representing the grayscale version of the image |
| 4 | For a kernel of size (m, n), what is the size of the padding that needs to be added to the input image to apply a convolution |
| 5 | Implement a function that applies a convolution filter to an image represented as a Numpy array |
| 6 | Apply your convolution function to the images in the folder sample_images using the 3x3 box blur kernel defined as follows: |
| 7 | Implement a function that applies a Gaussian blur by applying the one-dimensional Gaussian kernel in the horizontal and vertical directions |
| 8 | Implement a function that performs edge detection by applying       successively grayscale conversion, gaussian blur and the Sobel operator |

## What the handout provides

Unpacked and set up in place, so this folder reads as a working project
rather than an archive next to a drop zone. The archive itself stays for
reference; the `provided-files/` wrapper it unpacked into does not.

From `sample_images.zip`:

- `060811_131006_GM6A0103.jpg`
- `060814_073026__M6A0169.jpg`
- `1022.jpg`
- `1062.jpg`
- `1104.jpg`
- `1192.jpg`
- `1320.jpg`
- `1473.jpg`
- `README.txt`
- `bmp_24.bmp`
- `small_image.bmp`

## Running it

```bash
conda activate m1ai-programming
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - Python/TP2 - Image Processing with Numpy.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
