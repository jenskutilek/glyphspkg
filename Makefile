.PHONY: all
all:
	wheel

.PHONY: build
build:
	python setup.py build_ext --inplace

.PHONY: wheel
wheel:
	MYPYPATH=~/Code/glyphspkg/stubs python3 setup.py bdist_wheel

.PHONY: clean
clean:
	rm -f Lib/*.so
	rm -f Lib/glyphspkg/*.so
	rm -rf build/*
	rm -rf dist/*