import sys
import os
from setuptools import setup, find_packages

setup(  name = "genocode",
        version = "1.0",
        keywords = ("genetic", "risk", "prediction"),
        description = "genocode genetic disease risk prediction",
        long_description = "eds sdk for python",
        license = "MIT Licence",

        url = "https://github.com/Genes-N-Risks/genocode",
        author = "Yousef Baioumy, Saransh Jain, Jinrong Ma, July Zhou ",
        author_email = "baioumyy@uw.edu, saranshj@uw.edu, majorn@uw.edu, qiongz@uw.edu"
        maintainer = "Yousef Baioumy",
        maintainer_email = "baioumyy@uw.edu",


        classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        ],
        packages = find_packages('genocode',exclude=['tests']),
        include_package_data = True,
        platforms = "any",
        install_requires = [ 'numpy',
                             'pandas',
                             'math',
                             'matplotlib',
                             'seaborn'
                             'statistics'
                            ],
        entry_points = {
             'console_scripts': [
                  'genocode_run = genocode.genocode_run:main',
        ]
     }
 )
