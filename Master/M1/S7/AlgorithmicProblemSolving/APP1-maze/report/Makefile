MAIN = main

.PHONY: all clean

all: $(MAIN).pdf

# latexmk reruns pdflatex until the table of contents and every cross-reference
# between sections has settled; -halt-on-error stops on the first real failure
# instead of burying it under three more passes.
$(MAIN).pdf: $(MAIN).tex preamble.tex $(wildcard sections/*/*.tex)
	latexmk -pdf -halt-on-error -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -C
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz
