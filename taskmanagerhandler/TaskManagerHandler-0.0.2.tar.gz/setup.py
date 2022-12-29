from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name='TaskManagerHandler',
    version='0.0.02',
    packages=find_packages(),
    author="Shivam Sharma",
    author_email="shivamsharma1913@gmail.com",
    description="This package will take care of interacting with speech interactions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
)

install_requires = ['setuptools', 'wheel']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
