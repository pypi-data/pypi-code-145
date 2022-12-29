###############################################################################
#####   Setup.py - installs all the required packages and dependancies    #####
###############################################################################

import pathlib
from setuptools import setup, find_packages
import sys
# import iso3166_updates

#software metadata
__author__ = 'AJ McKenna, https://github.com/amckenna41'
__authorEmail__ = 'amckenna41@qub.ac.uk'
__url__ = 'https://github.com/amckenna41/iso3166-updates'
__credits__ = ['AJ McKenna']
__version__ = "0.0.5"
__license__ = 'MIT'
__name__ = 'iso3166-updates'
__status__ = 'Development'
__maintainer__ = "AJ McKenna"

#ensure python version is greater than 3
if (sys.version_info[0] < 3):
    sys.exit('Python 3 is the minimum version requirement.')

#get path to README file
HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(name='iso3166-updates',
      version=__version__,
      description='A Python package that pulls the latest updates & changes to all ISO3166 listed countries.',
      long_description = README,
      long_description_content_type = "text/markdown",
      author=__license__,
      author_email=__authorEmail__,
      maintainer=__maintainer__,
      license=__license__,
      url=__url__,
      keywords=["iso", "iso3166", "beautifulsoup", "python", "pypi", "countries", "country codes", "csv" \
            "iso3166-2", "iso3166-1", "alpha2", "alpha3"],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'License :: Free For Educational Use',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',	
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
      install_requires=[
          'beautifulsoup4>=4.11.1',
          'pandas',
          'numpy',
          'requests>=2.28.1',
          'iso3166'
      ],
     test_suite='tests',
     packages=find_packages(),
     include_package_data=True,
     zip_safe=False)
