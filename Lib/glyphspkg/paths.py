from pathlib import Path
from typing import Optional


def build_output_file_path(
    input_path: Path, output_path: Optional[Path] = None, target_suffix: str = ".glyphs"
) -> Path:
    file_name = input_path.with_suffix(target_suffix).name
    if output_path is None:
        # No path was specified, save next to original file
        output_file_path = input_path.parent / file_name
    elif output_path.is_dir():
        # Output directory was specified, save to original file name with
        # changed suffix in new dir
        output_file_path = output_path / file_name
    else:
        # Full path with file name was specified, save there
        output_file_path = output_path

    return output_file_path


def rmdir(directory: Path):
    """Recursively remove files and directories from a directory, then remove the
    directory itself.

    Args:
        directory (Path): The directory to remove.
    """
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()
