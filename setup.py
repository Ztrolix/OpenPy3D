from setuptools import setup; setup()
import setuptools
from setuptools import *

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "OpenPy3D",
    version = "0.0.1",
    author = "Ztrolix",
    author_email = "xdpxigamer@gmail.com",
    description = "OpenPy3D Is a Python PIP package that you can create 3D objects in Python really easy with.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Ztrolix/OpenPy3D",
    project_urls = {
        "Bug Tracker": "https://github.com/Ztrolix/OpenPy3D/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 license",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.11"
)