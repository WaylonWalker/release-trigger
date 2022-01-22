from pathlib import Path

from setuptools import setup

NAME = "markata"

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

with open("requirements_dev.txt", "r", encoding="utf-8") as f:
    dev_requires = [x.strip() for x in f if x.strip()]

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="",
    version="0.0.0",
    py_modules=[
        "releaseme",
    ],
    install_requires=requires,
    extras_require={"dev": dev_requires},
)
