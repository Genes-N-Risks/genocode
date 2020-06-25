# Genocode
[![Build Status](https://travis-ci.org/Genes-N-Risks/genocode.svg?branch=master)](https://travis-ci.org/Genes-N-Risks/genocode)
[![Documentation Status](https://readthedocs.org/projects/genocode/badge/?version=latest)](https://genocode.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/Genes-N-Risks/genocode/badge.svg?branch=master)](https://coveralls.io/github/Genes-N-Risks/genocode?branch=master)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![HitCount](http://hits.dwyl.com/Genes-N-Risks/genocode.svg)](http://hits.dwyl.com/Genes-N-Risks/genocode)
## Webtool with synthetic datasets to better understand health risks associated with common genetic polymorphisms

**Problem:** Direct-to-consumer (DTC) genetic tests are increasingly popular, with a market worth of around $1B that is expected to double over the next decade. Hundreds of common single nucleotide polymorphisms (SNPs) are associated with altered risk of common diseases and health risks; however, these are based on average health data that incompletely describes the variability or the heterogeneity of the population and the true risk of a SNP being associated with an outcome in a given individual. This reduces the ability of an individual to determine how they themselves or their patients might truly be affected. Healthcare practitioners must therefore be able to navigate between the promise and reality of these tools, including being able to interpret the literature that is associated with a given risk or suggested intervention.

**Solution:** Our webtool allows users to privately upload their genetic test data, identify risk genes that they are concerned about, and be shown outputs of normally-distributed synthetic data that describes the full possible range of phenotypes for a given genotype. We are looking to design a user-friendly web-tool GenoCode using synthetic datasets that we collected from published literature to help users better understand their health risks associated with common genetic polymorphisms from their direct-to-consumer genetic test.

**Beneficiary:** The user is anyone who has taken a DTC genetic test offered by companies such as 23andme, Ancestry.com, and MyHeritage, and would like to understand their test results with much more clarity.

**Site:** https://genocode.herokuapp.com.

**Disclaimer:** The current app is a prototype only. It only supports 23andMe test results. The output generated does not correspond to your actual risk. The heterogeneity factors will soon be added. Any decision you take after consulting the app is not our  responsibility.

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
Please upload the text file containing the SNPs provided by 23andMe.
![Homepage](https://github.com/Genes-N-Risks/genocode/blob/master/images/load_demo.gif)

### Acknowledgements
* We thank Dr. Thomas Wood, UW Medicine for his guidance and sponsorship of the project. This app would not have been possible without his help. 
* This app is a result of Data Intensive Research Enabling Clean Technologies (DIRECT) Program offered by the E-Science Institute. 
* We would also like to thank Dr David Beck, Dr Dan Schwartz, and Dr Ting Cao for their support and guidance throughout the program.
