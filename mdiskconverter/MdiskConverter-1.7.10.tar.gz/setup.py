import re
import os
import setuptools

ver = '1.7.10'

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

desc = "Package containing basic functions to build telegram bots."
GPL = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
git = "https://github.com/vasusen-code/ethon"
classify = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]
requirements = [
    "pyrogram",
    "aiofiles",
    "aiohttp",
    "requests",
]


setuptools.setup(
    name="MdiskConverter",
    version=ver,
    author="MDISK",
    description=desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=git,
    license=GPL,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classify,
    python_requires=">=3.6",
)
