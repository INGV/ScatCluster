Welcome to ScatCluster's documentation!
=======================================

**ScatCluster** A workflow for clustering continuous time series with a deep scattering network.

.. image:: _static/scatcluster_text.png
   :width: 0
   :align: center

.. raw:: html

   <p align="center">
      <img src="_images/scatcluster_text.png" width=250px
      style="background-color: transparent;"/>
   </p>

|


Contents
--------

.. toctree::
   :maxdepth: 2

   usage
   getting_started

About
-----

.. important::

   This project is still in development. The API is not stable and may change
   without notice. Once a stable version is released, the API will be
   considered stable and will not change without a major version bump.

License
-------

**Copyright ©️ 2024 Christopher Zerafa and Carlo Giunchi**

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Please use the following dropdown menu to see the full terms of use, or directly have a look at the LICENSE file in the root directory of the repository.

.. dropdown:: Full terms of use

   .. include:: ../../LICENSE
      :literal:

Installation
------------

The package is available from the PyPI repository. To install using pip, execute the following line:


.. code-block:: bash
   :caption: CPU-only installation

   pip install scatcluster

If you want to use a GPU, you need to install the package with the package CuPy. The code will try to find it and use it if it is installed. You can install it with the following command.

.. code-block:: bash
   :caption: GPU usage

   pip install scatcluster[gpu]


Contributing and Releases
-------------------------
Check out the :doc:`contributing` section for further information on how to contribute to the project and make releases.


References
----------


Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.
