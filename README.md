# Genocode
[![Build Status](https://travis-ci.org/Genes-N-Risks/genocode.svg?branch=master)](https://travis-ci.org/Genes-N-Risks/genocode)
[![Documentation Status](https://readthedocs.org/projects/genocode/badge/?version=latest)](https://genocode.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/Genes-N-Risks/genocode/badge.svg?branch=master)](https://coveralls.io/github/Genes-N-Risks/genocode?branch=master)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![HitCount](http://hits.dwyl.com/Genes-N-Risks/genocode.svg)](http://hits.dwyl.com/Genes-N-Risks/genocode)
## Webtool with synthetic datasets to better understand health risks associated with common genetic polymorphisms
* This webtool will extract data from DTC genetic test outputs (e.g. 23andMe) and generate personalized data visualizations for a given individual.



#### Repository Structure
```
  |- README.md
  |- genocode/
      |- __init__.py
      |- tests/
        |- __init__.py
      |- data/
        |- SNP.csv
  |- app/
      |- dash_setup.sh
      |- norm_visual_webtool.py
      |- load_file.py
      |- popup_window.py
  |- docs/
      |- README.md
      |- Gantt Chart.ipynb
      |- conf.py
      |- modules.rst
      |- genocode.rst
      |- User Story.pdf
      |- index.rst
  |- examples/
      |- README.md
      |- DataOperation.ipynb
      |- DataOperation.example.ipynb
      |- NormalDistribution.ipynb
      |- NormalDistribution.example.ipynb
  |- images/
      |- README.md
  |- setup.py
  |- .travis.yml
  |- environment.yml
  |- .gitignore
  |- LICENSE
  |- .coveragerc
  |- requirements.txt

```

#### Activating the virtual environment
* Included within the root of the repository is a virtual environment
pre-suited to run `genocode`
  * The virtual environment is located within environment.yml
  * To create the virtual environment from the .yml file:
  `conda env create -f environment.yml`
  * To activate the virtual environment:
  `conda activate genocode_env`
  * The environment contains:
    * Python 3.8 from miniconda3
    * numpy
    * pandas
    * matplotlib

`pip install git+https://github.com/Genes-N-Risks/genocode.git`

### Using genocode
* Before using
* Access to our jupyter notebook examples

### Example Output
* Example data and graphs will be updated here

### Miscellaneous Notes

