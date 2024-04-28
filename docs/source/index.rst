Welcome to ScatCluster's documentation!
===================================

**ScatCluster** A workflow for clustering continuous time series with a deep scattering network.

Contents
--------

.. toctree::
   :maxdepth: 2

   guide
   tutorials

About
-----

.. important::

   This project is still in development. The API is not stable and may change
   without notice. Once a stable version is released, the API will be
   considered stable and will not change without a major version bump.
   A target release date will be around April 2023.

License
-------

**Copyright ©️ 2024 Christopher Zerafa and Carlo Giunchi**

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Please use the following dropdown menu to see the full terms of use, or directrly have a look at the LICENCE file in the root directory of the repository.

.. dropdown:: Full terms of use

   .. include:: ../../LICENCE
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


References
----------


Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.
