"""
Command line interface for compilation/decompilation
"""

import argparse
from os.path import isdir
from glyphspkg.package_to_single import package_to_single
from glyphspkg.single_to_package import single_to_package


def main() -> None:
    parser = argparse.ArgumentParser()

    # parser.add_argument(
    #     "-i",
    #     "--in-place",
    #     action="store_true",
    #     default=False,
    #     help="Convert the file in place, i.e. remove the input file.",
    # )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_path",
        type=str,
        help=(
            "Output path for converted files. If omitted, the file is saved "
            "next to the input file."
        ),
    )
    parser.add_argument(
        "glyphsfile",
        type=str,
        nargs="+",
        help="Path to the .glyphs file or .glyphspackage dir to be converted.",
    )

    arguments = parser.parse_args()

    if not arguments:
        parser.print_help()
        return

    for input_path in arguments.glyphsfile:
        print("Reading:", input_path)
        if isdir(input_path):
            # The file is a package, convert to single
            package_to_single(input_path, arguments.output_path)
        else:
            # The file is a single file, convert to package
            single_to_package(input_path, arguments.output_path)
