all: cnll-bullet-points.pdf

cnll-bullet-points.pdf:
	./builder.py make

#cnll-bullet-points.typ: cnll-bullet-points.md
#	pandoc -o $@ $<
#
#cnll-bullet-points.pdf: cnll-bullet-points.typ
#	typst compile $<

clean:
	rm -rf dist
	rm -rf *.md.tmp
