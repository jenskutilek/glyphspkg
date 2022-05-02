from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="glyphspkg",
    description="Converter from .glyphspackage to .glyphs files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jens Kutilek",
    url="https://github.com/jenskutilek/glyphspkg",
    packages=[
        "glyphspkg",
    ],
    package_dir={"": "Lib"},
    entry_points={
        "console_scripts": [
            "glyphspkg = glyphspkg.cmdline:main",
        ]
    },
    install_requires=[
        "openstep-plist >= 0.3.0",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
    ],
)
