Usage
=====

.. _installation:

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
