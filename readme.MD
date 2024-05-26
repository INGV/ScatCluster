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
Installation is achieved via pip. To install using pip, execute the
```bash
# CPU-only installation
pip install scatcluster
```

If you want to use a GPU, you need to install the package with the package CuPy. The code will try to find it and use it if it is installed. You can install it with the following command.
```bash
# GPU usage
pip install scatcluster[gpu]
```


## Getting Started
To help you get started with ScatCluster, we have created a set of notebooks located in the [`./docs/source/getting_started`](https://github.com/INGV/ScatCluster/tree/main/docs/source/getting_started) directory. These notebooks guide you through the entire workflow, which is divided into three main sections: Processing, Visualisation, and Analysis. Below is a detailed description of each section and its corresponding notebooks.

### 1. Processing

The Processing section includes two notebooks that prepare your data for subsequent stages:

- **01_processing_01_set_config.ipynb**: In this notebook, you will set the parameters for your experiment and specify the location where results will be stored. This step is crucial for ensuring that your data processing and analysis are properly configured.

- **01_processing_02_processing_workflow.ipynb**: This notebook executes the processing of the scatseis transform. The duration of this step depends on the dataset parameters you set in the previous notebook. It is designed to handle the heavy lifting of data transformation, preparing your time series data for clustering.

### 2. Visualisation

The Visualisation section contains a notebook that helps you visualize the clustering results:

- **02_visualisation_01_dendrograms_waveforms.ipynb**: Use this notebook to build hierarchical clustering diagrams and generate appropriate clusters. Visualization is key to understanding the structure and relationships within your time series data.

### 3. Analysis

The Analysis section offers a notebook to dive deeper into the clustering results:

- **03_analysis_01_timewindow_cluster_comparison.ipynb**: This notebook allows you to analyze the different clusters identified in the previous stages. By comparing clusters across different time windows, you can gain insights into the dynamics and patterns within your time series data.

By following these notebooks, you will be able to execute the full workflow of ScatCluster, from data preparation and transformation to visualization and in-depth analysis. This structured approach ensures a comprehensive understanding and effective clustering of your time series data. Happy clustering!


## Dependencies
This package can be executed on CPU or GPU respectively. The main dependencies are:
- obspy>=1.4.0
- scatseisnet>=0.2.1
- fastcluster

If GPU is required, ensure that cupy>=11.3.0 is available.

Additional dependencies are available within `requirements.txt`.

## Documentation

Please check the [documentation](https://scatcluster.readthedocs.io/en/latest/).

## Question and Issues
Should you have any issues with this code, you can reach out on christopher.zerafa@ingv.it or carlo.giunchi@ingv.it

## Contribution guidelines

Thank you for your interest in contributing to this project! Here are some guidelines to help ensure a smooth and successful contribution process. Please read them carefully before contributing. We are happy to answer any questions you may have, and to welcome you as a contributor.

1. __Fork__ the project to your own GitHub account by clicking the "Fork" button in the top right corner of the repository page. This will allow you to make changes to the project without affecting the main project.

2. Create a __new branch__ for your contribution. This will keep your changes separate from the main branch and make it easier to review and merge your changes. The name of your branch should be concise and descriptive. For example, if you are adding a new feature, you might call your branch "add-feature".

3. Write concise __commit messages__ that describe the changes you made. Use the present tense and avoid redundant information. We try to follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

4. Make sure your changes work as intended and do not introduce new bugs or problems. Write __tests__ if applicable.

5. __Document__ your changes with following the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format. This step is important to ensure that the package documentation is up-to-date and complete. If you are not sure about this step, we can help you.

6. When you are ready to submit your changes, create a __pull request__ from your branch to the main branch of the original repository. Provide a clear description of your changes and why they are necessary, and we will review your contribution.

Thank you again for your interest in contributing to this project!

## Making a Release

To make a release, please follow these steps:

1. Stage all your changes with:
   ```bash
   git stage .
   ```

2. Commit the code to the master branch. Make sure to use a proper commit message. Use the following command:
   ```bash
   git commit -s -m "this is a proper commit message"
   ```

3. Tag the code with the next version number x.x.x. Please note that version numbering needs to follow proper major, minor, micro increments. Use the following command:
   ```bash
   git tag x.x.x
   ```

4. Push to origin with:
   ```bash
   git push origin --tags
   ```

   This will trigger [GitHub Actions](https://github.com/INGV/ScatCluster/actions) which will:

   1. Automatically push to PyPI and PyPI test:
      [GitHub Actions PyPI release workflow](https://github.com/INGV/ScatCluster/actions/workflows/pypi_release.yml)

   2. Run pre-commit changes to check code quality:
      [GitHub Actions pre-commit workflow](https://github.com/INGV/ScatCluster/actions/workflows/pre-commit.yml)

   3. Build documentation:
      [GitHub Actions documentation build workflow](https://github.com/INGV/ScatCluster/actions/workflows/docs.yml)
