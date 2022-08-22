"""
Command line interface for compilation/decompilation
"""

import argparse
from glyphspkg.package_to_single import package_to_single
from glyphspkg.single_to_package import single_to_package
from pathlib import Path


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

    if arguments.output_path is None:
        output_path = None
    else:
        output_path = Path(arguments.output_path)
        if not output_path.is_dir() and len(arguments.glyphsfile) > 1:
            print(
                "ERROR: If you specify a full output file path, you must only "
                "supply one input file path, or else the output file will be "
                "overwritten with each input file."
            )
            return

    for inp in arguments.glyphsfile:
        input_path = Path(inp)
        print("Reading:", input_path)
        if input_path.is_dir():
            # The file is a package, convert to single
            output_file_path = package_to_single(input_path, output_path)
            print(f"Saved <{output_file_path}>.")
        else:
            # The file is a single file, convert to package
            output_file_path = single_to_package(input_path, output_path)
            print(f"Saved <{output_file_path}>.")
