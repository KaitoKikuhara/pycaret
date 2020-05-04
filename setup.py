# Copyright (C) 2019-2020 Moez Ali <moez.ali@queensu.ca>
# License: MIT, moez.ali@queensu.ca

"""

PyCaret - An end-to-end open source machine learning library

Module Author:
--------------
pycaret.anomaly, Moez Ali <moez.ali@queensu.ca>
pycaret.classification, Moez Ali <moez.ali@queensu.ca>
pycaret.clustering, Moez Ali <moez.ali@queensu.ca>
pycaret.datasets, Moez Ali <moez.ali@queensu.ca>
pycaret.nlp, Moez Ali <moez.ali@queensu.ca>
pycaret.preprocess, Fahad Akbar <M.akbar@queensu.ca>
pycaret.regression, Moez Ali <moez.ali@queensu.ca>

"""

from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pycaret",
    version="1.0.0",
    description="An open source, low-code machine learning library in Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pycaret/pycaret",
    author="Moez Ali",
    author_email="moez.ali@queensu.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas", "numpy", "seaborn", "matplotlib", "IPython", "joblib",
                     "scikit-learn", "shap", "ipywidgets", "yellowbrick", "xgboost",
                     "wordcloud", "textblob", "plotly", "cufflinks", "umap-learn",
                     "lightgbm", "pyLDAvis",
                     "gensim", "spacy", "nltk", "mlxtend",
                     "pyod", "catboost", "pandas-profiling", "kmodes",
                     "datefinder", "datetime", "DateTime", "awscli"]
)
