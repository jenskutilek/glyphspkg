from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="glyphspkg",
    version="0.1.1",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
