# glyphspkg

Converter for GlyphsApp package to monolithic files and vice versa.

[Glyphs](https://glyphsapp.com) supports two different file formats, both of
which are based on plist. One, using the suffix `.glyphs`, is a monolithic
file, the other, using the suffix `.glyphspackage`, is a special folder that
appears as one file on macOS.

The _package_ variant has advantages when used in SCM systems, but some
external tools only support the monolithic file format. That’s where this
converter tool comes in. It can be integrated into font build workflows to
convert package files before further processing.


## Installation

`glyphspkg` is listed on PyPi, so you can install it via pip.


## Usage

```
usage: glyphspkg [-h] [-o OUTPUT_PATH] glyphsfile [glyphsfile ...]

positional arguments:
  glyphsfile            Path to the glyphs file or package to be converted.

options:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output OUTPUT_PATH
                        Output path for converted files. If omitted, the file is saved next to the original.
```