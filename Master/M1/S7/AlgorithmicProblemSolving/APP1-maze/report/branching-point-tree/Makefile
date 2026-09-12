MAIN = branching-point-tree

.PHONY: all clean

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex ../preamble.tex $(wildcard figure-*.tex)
	latexmk -pdf -halt-on-error -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -C
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz
