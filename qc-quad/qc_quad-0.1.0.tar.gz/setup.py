# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qc_quad', 'qc_quad.lebedev', 'qc_quad.lebedev.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.0,<2.0.0']

setup_kwargs = {
    'name': 'qc-quad',
    'version': '0.1.0',
    'description': 'Quantum-chemistry quadrature package',
    'long_description': '# qc-quad\n\nQuantum-chemistry quadrature package.\n\nThis package makes easy to set up so-called Lebedev-Laikov and Gaussian-Legendre grids.\nThese grids are suitable for numerical integration in quantum chemistry applications.\n\nLebedev-Laikov grids provide coordinates and weights for an optimal integration over a surface\nof unit sphere. These grids are Golden standard in quantum chemistry because of the accuracy\nthey provide at the minimal number of the integrand-function evaluations.\nThe implementation of the grids is derived from a Matlab implementation by John Burkardt\nhttps://people.sc.fsu.edu/~jburkardt/m_src/sphere_lebedev_rule/sphere_lebedev_rule.html\n\nGauss-Legendre grids provide coordinates and weights for an optimal integration in one dimension,\nover a finite segment. The Gauss-Legendre grids are suitable for generic functions. This is in\ncontrast to the behavior of wave-functions along radial distance. However, I provide these\ngrids here in order to organize an integration of generic functions over spherical volumes. \n\nNote, that to become truly quantum-chemical quadrature this software needs a smooth separation\nof space which depends on the geometry of the molecule and, perhaps, a one-dimensional grid\nsuitable for integrating radial functions together with a pruning scheme for Lebedev-Laikov\ngrids. This should be easy to bolt in later for somebody who needs it.\n\nA motivation for composing this package instead of using several packages out there in the\nopen-source community would be "doing things" right, in a testable, malleable and parsimonious way.\n\nThe major difficulty in setting up of the Lebedev-Laikov grids is the absence of their\ndefinition for a given number of points. The grids are provided for minimum of 6 and maximum \nof 5810 points: 6, 14, 26, 38, 50, 74, 86, 110, 146, 170, 194, 230, 266, 302, 350, 434, 590,\n770, 974, 1202, 1454, 1730, 2030, 2354, 2702, 3074, 3470, 3890, 4334, 4802, 5294 and 5810,\n32 grids in total. Each of the 32 grids, is composed of a set of 6 kinds of grids composed \nof 6, 12, 8, 24, 24 and 48 points. To the best of my knowledge, no implementation out in\nthe open-source offers any generalizations. For example, a construction of grids with more \npoints by attaching the 48-point grids together or construction of a 36-point grid by using \nthree of the 12-point grids is not implemented although this should be feasible.\n\nThere are several open-source implementations of Lebedev-Laikov grids.\nThe quantum-chemistry package Horton is using a Python binding to a C++\nmodule implementing the grids https://github.com/theochem/horton.\nA sub-repository `grid` of `theochem` repositories offers the Lebedev-Laikov grids stored\nin `.npy` files. There is an exhaustive set of quadratures in repository\nhttps://github.com/sigma-py/quadpy . However, the code of `quadpy` is obfuscated.\nThe repository https://github.com/Rufflewind/lebedev_laikov provides the grids via a Python\nbinding to a source code in C language. Similarly, https://github.com/dftlibs/numgrid\nprovides the grids through a binding to a Fortran source.\nThere is a pure Python implementation of Lebedev-Laikov grids\nhttps://github.com/gabrielelanaro/pyquante/ . However, it provides the grids for the first \n11 (6, 14, 26, 38, 50, 74, 86, 110, 146, 170, 194) out of 32 grids implemented by Dmitri Laikov.\nFinally, there is an issue in SciPy with a feature request of Lebedev grids\nhttps://github.com/scipy/scipy/issues/11929\n\nCurrent package `qc-quad` is open source. It provides Lebedev-Laikov grids for 32 grids published by\nDmitri Laikov. It is a pure Python package. This makes this implementation easily testable (pytest), \nextendable and usable. \n\n\n## References:\n    Axel Becke, "A multicenter numerical integration scheme for polyatomic molecules",\n    Journal of Chemical Physics,\n    Volume 88, Number 4, 15 February 1988, pages 2547-2553. \n\n    Vyacheslav Lebedev, Dmitri Laikov, "A quadrature formula for the sphere of the 131st\n    algebraic order of accuracy", Russian Academy of Sciences Doklady Mathematics,\n    Volume 59, Number 3, 1999, pages 477-481.\n\n## Installation\n\n    pip install qc-quad\n\n## Developer installation\n\nInstallation could be done with poetry = "^1.3.1"\n\n    poetry install\n\n## Usage\n\nThis is a part of some quantum-chemistry software. Some use cases can be seen in the tests.\n\n## Roadmap\n\nLet\'s see what does the community thinks.\n\n## Contributing\n\n  - PEP8 code formatting is mandatory.\n  - The bug fixes are welcome.\n  - Small improvements are welcome.\n  - Definition of the hard-coded coefficients is especially welcome.\n\n## Authors and acknowledgment\nJames Talman drew my attention to Lebedev-Laikov grids.\n\n## License\n\nMIT license: no guarantee, free to use anywhere.\n\n## Project status\n\nInitial release is done.',
    'author': 'Peter Koval',
    'author_email': 'koval.peter@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
