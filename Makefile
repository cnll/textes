all: cnll-bullet-points.pdf

cnll-bullet-points.pdf:
	./builder.py make

#cnll-bullet-points.typ: cnll-bullet-points.md
#	pandoc -o $@ $<
#
#cnll-bullet-points.pdf: cnll-bullet-points.typ
#	typst compile $<

clean:
	rm -f dist/*.typ
	rm -f src/*.tmp.md
	rm -f styles/*.pdf
