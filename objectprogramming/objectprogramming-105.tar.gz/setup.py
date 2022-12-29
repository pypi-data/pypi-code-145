# This file is placed in the Public Domain.


"object programming"


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl


setup(
    name="objectprogramming",
    version="105",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/objectprogramming",
    description="functional programming with objects",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["op"],
    scripts=["bin/op"],
    include_package_data=True,
    data_files=[
                ("op/mod", uploadlist("mod")),
                ("share/doc/op", ("README.rst",))
               ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
