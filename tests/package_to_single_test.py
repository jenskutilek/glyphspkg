import pytest
import unittest

from glyphspkg.package_to_single import package_to_single
from glyphspkg.paths import rmdir
from pathlib import Path


def get_mono_path():
    return (
        Path(__file__).parent / "data" / "JetBrainsMono-Italic.glyphspackage"
    )


def get_tmp_path():
    return Path(__file__).parent / "data" / "tmp"


class PackageToSingleText(unittest.TestCase):
    def test_same_dir(self):
        package_to_single(get_mono_path())
        out_file = get_mono_path().with_suffix(".glyphs")
        assert out_file.is_file()
        # TODO: Check against original file?
        out_file.unlink()

    def test_with_output_dir(self):
        out_dir = get_tmp_path()
        out_dir.mkdir(exist_ok=True)
        package_to_single(get_mono_path(), out_dir)
        out_file = out_dir / "JetBrainsMono-Italic.glyphs"
        assert out_file.is_file()

    def test_with_output_file(self):
        out_dir = get_tmp_path()
        out_dir.mkdir(exist_ok=True)
        out_file = out_dir / "custom.glyphs"
        package_to_single(get_mono_path(), out_file)
        assert out_file.is_file()

    @classmethod
    def tearDownClass(cls):
        rmdir(get_tmp_path())
