# ScatCluster
A workflow for clustering continuous time series with a deep scattering network.

<div align=center>

<img src=docs/source/_static/scatcluster_text.png width=250px/>

[![Python Version](https://img.shields.io/pypi/pyversions/scatcluster)](https://pypi.org/project/scatcluster/)
[![PyPI version](https://badge.fury.io/py/scatcluster.svg)](https://badge.fury.io/py/scatcluster)
![GitHub last commit](https://img.shields.io/github/last-commit/INGV/scatcluster)
[![Documentation Status](https://readthedocs.org/projects/scatcluster/badge/?version=latest)](https://scatcluster.readthedocs.io/en/latest/?badge=latest)

</div>

## Installation
Installation is achieved by following these instructions:

`pip install scatcluster`

## Getting Started
This code contains a *quick_start* section with notebooks that can be used to execute the workflow on Sardinia Data. The workflow contains 3 sections:
1. **Processing**: This section contains 2 notebooks that will prepare the data to be used in the next stages.
    - *01_processing_01_set_config.ipynb*: This notebook is used to set the parameterization for the experimentation and set the location for where to store the results.
    - *01_processing_02_processing_workflow.ipynb*: This notebook is used to run the processing of the scatseis transform. The duration of this notebook is dependent on the dataset parameters set in the previous notebook.
2. **Visualisation**: This section contains the notebook *02_visualisation_01_dendrograms_waveforms.ipynb* used to build the hierarchical clustering diagram and appropriate clusters
3. **Analysis**: *03_analysis_01_timewindow_cluster_comparison.ipynb* offers a notebook to analyse the different clusters identified in the previous stages.

## Dependencies
This package can be executed on CPU or GPU respectively. The main dependencies are:
- obspy>=1.4.0
- scatseisnet>=0.2.1
- fastcluster

If GPU is required, ensure that cupy>=11.3.0 is available.

Additional dependencies are available within `requirements.txt`.

## Documentation

Please check the [documentation](https://scatcluster.readthedocs.io/en/latest/). You can find tutorials in the form of notebooks.

## Question and Issues
Should you have any issues with this code, you can reach out on christopher.zerafa@ingv.it or carlo.giunchi@ingv.it

## Contribution guidelines

Thank you for your interest in contributing to this project! Here are some guidelines to help ensure a smooth and successful contribution process. Please read them carefully before contributing. We are happy to answer any questions you may have, and to welcome you as a contributor.

1. __Fork__ the project to your own GitHub account by clicking the "Fork" button in the top right corner of the repository page. This will allow you to make changes to the project without affecting the main project.

2. Create a __new branch__ for your contribution. This will keep your changes separate from the main branch and make it easier to review and merge your changes. The name of your branch should be concise and descriptive. For example, if you are adding a new feature, you might call your branch "add-feature".

3. Write concise __commit messages__ that describe the changes you made. Use the present tense and avoid redundant information. We try to follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

4. Make sure your changes work as intended and do not introduce new bugs or problems. Write __tests__ if applicable.

5. __Document__ your changes with following the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format. This step is important to ensure that the package documentation is up to date and complete. If you are not sure about this step, we can help you.

6. When you are ready to submit your changes, create a __pull request__ from your branch to the main branch of the original repository. Provide a clear description of your changes and why they are necessary, and we will review your contribution.

Thank you again for your interest in contributing to this project!