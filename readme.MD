# INGV ScatCluster
A workflow for clustering continuous time series with a deep scattering network.

<div align=center>

<!-- <img src=docs/source/_static/logo_scatseisnet.png width=250px/> -->

[![Python Version](https://img.shields.io/pypi/pyversions/scatcluster)](https://pypi.org/project/scatcluster/)
[![PyPI Version](https://img.shields.io/pypi/v/scatcluster.svg)](https://pypi.org/project/scatcluster/)\
![GitHub last commit](https://img.shields.io/github/last-commit/INGV/scatcluster)
[![Documentation Status](https://readthedocs.org/projects/scatcluster/badge/?version=latest)](https://scatcluster.readthedocs.io/en/latest/?badge=latest)


</div>

## Installation
Installation is achieved by following these instructions:

1. Run the following command to build and install the INGV ScatCluster package `pip install scatcluster`

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

## Question and Issues
Should you have any issues with this code, you can reach out on christopher.zerafa@ingv.it or carlo.giunchi@ingv.it
