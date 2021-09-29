PYTHON=python3

notes.pdf: notes.tex
	latexmk -pdf $<

notes.tex: notes.py | template.tex
	./$< > $@

clean:
	latexmk -C
	$(RM) notes.tex

.PHONY: clean
