images := $(patsubst %,board-%.svg,blank numbers easy hard)
pngs := $(patsubst %,board-%.jpg,blank numbers easy hard)

all: slides.html

images: $(images)
#	$(pngs)

clean:
	rm -f slides.html
	rm -f board-*.svg
	rm -f board-*.png

slides.html: slides.asc custom.css $(images)
	cdk --theme=twitter --custom-css=custom.css slides.asc

board-%.svg: svg.py
	python3 svg.py $* > $@
	convert $@ board-$*.png
