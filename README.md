# Genocode
[![Build Status](https://travis-ci.org/Genes-N-Risks/genocode.svg?branch=master)](https://travis-ci.org/Genes-N-Risks/genocode)
[![Documentation Status](https://readthedocs.org/projects/genocode/badge/?version=latest)](https://genocode.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/Genes-N-Risks/genocode/badge.svg?branch=master)](https://coveralls.io/github/Genes-N-Risks/genocode?branch=master)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![HitCount](http://hits.dwyl.com/Genes-N-Risks/genocode.svg)](http://hits.dwyl.com/Genes-N-Risks/genocode)
## Webtool with synthetic datasets to better understand health risks associated with common genetic polymorphisms
* Our webtool allows users to privately upload their genetic test data, identify risk genes that they are concerned about, and be shown outputs of normally-distributed synthetic data that describes the full possible range of phenotypes for a given genotype. Hundreds of common single nucleotide polymorphisms (SNPs) are associated with altered risk of common diseases and health risks; however, these are based on average health data that incompletely describes the variability of the population and the true risk of a SNP being associated with an outcome in a given individual. We designed a user-friendly web-tool GenoCode using synthetic datasets that we collected from published literature to help users better understand their health risks associated with common genetic polymorphisms from their direct-to-consumer genetic test.




#### Repository Structure
```
  |- README.md
  |- genocode/
      |- __init__.py
      |- tests/
        |- __init__.py
        |- test_data_extract.py
        |- test_datavis.py
        |- test_vectorized_datavis.py
      |- data/
        |- 23andMe_data.csv 
        |- 'Genetic Statistical Data.xlsx - Initial data.csv' 
        |- 23andMe_data.txt 
        |- 'Obesity OR-Effect.csv'
        |- 'Genetic Data T2DB.xlsx'
        |- 'Polygenic Risk Scores Data.csv'
        |- 'Genetic Data.csv'
      |- bmistat.py
      |- data_extract.py
      |- type2diabetes.py
      |- datavis.py
      |- vectorized_datavis.py
      |- match_snps.ipynb	
  |- app/
      |- multi_page/
        |- apps/
          |- __init__.py
          |- consent.py
          |- main.py
          |- statistic.py
          |- load.py
          |- README.txt
        |- app.py
        |- index.py
        |- requirements.txt
        |- runtime.txt
        |- README.txt
        |- 'Polygenic Risk Scores Data.csv'
        |- 'Genetic Data.csv'
        |- uwlogo.png
        |- .Procfile
      |- dash_setup.sh
      |- norm_visual_webtool.py
      |- load_file.py
      |- popup_window.py
  |- docs/
      |- _build/
        |- doctrees/
          |- environment.pickle
          |- genocode.doctree
          |- index.doctree
          |- modules.doctree
        |- html/
          |- _sources/
          |- _static/
          |- genindex.html
          |- index.html    
          |- objects.inv
          |- search.html
          |- genocode.html  
          |- modules.html  
          |- py-modindex.html 
          |- searchindex.js
      |- README.md
      |- Gantt Chart.ipynb
      |- conf.py
      |- modules.rst
      |- genocode.rst
      |- User Story.pdf
      |- index.rst
      |- Makefile
      |- make.bat
  |- examples/
      |- README.md
      |- DataOperation.ipynb
      |- DataOperation.example.ipynb
      |- NormalDistribution.ipynb
      |- NormalDistribution.example.ipynb
      |- 'Data Visualization Tool.ipynb'
      |- 'Unit Tests.ipynb'
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
    * python == 3.8 
    * plotly
    * dash
    * dash-core-components
    * dash-html-components
    * dash-renderer
    * numpy
    * pandas
    * matplotlib
    * scipy
    * statistics
   

### Using genocode
* Before using
* Access to our jupyter notebook examples

### Example Output
* Homepage
![Homepage](https://github.com/Genes-N-Risks/genocode/blob/master/images/main_demo.gif)
* Data page
![Homepage](https://github.com/Genes-N-Risks/genocode/blob/master/images/statistic_demo.gif)
* Agreement page
![Homepage](https://github.com/Genes-N-Risks/genocode/blob/master/images/agreement_demo.gif)
* Users analysis page
![Homepage](https://github.com/Genes-N-Risks/genocode/blob/master/images/load_demo.gif)

### Miscellaneous Notes

