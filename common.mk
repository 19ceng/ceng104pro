.DEFAULT: build

BUILT := text.pdf
build: $(BUILT)
clean: ; rm -f $(BUILT)

%.pdf: %.rst
	@drug -d slide --render rest --append-store ../src $<

.PHONY: build clean
