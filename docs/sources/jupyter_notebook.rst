.. _jupyter_notebook:
.. include:: ./ext_links.txt

Tutorials
*********

Getting started Jupyter* Notebooks illustrating the usage of **Data Parallel Extensions for Python** are located
in the `GitHub repository <https://github.com/IntelPython/DPEP/tree/main/notebooks>`_

To run the tutorial, in the command line prompt type:

.. code-block:: console

    jupyter notebook

This will print some information about the notebook server in your terminal, including the URL of
the web application (by default, ``http://localhost:8888``):


.. code-block:: console

    $ jupyter notebook
    [I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
    [I 08:58:24.417 NotebookApp] 0 active kernels
    [I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
    [I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    It will then open your default web browser to this URL.

When the notebook opens in your browser, you will see the Notebook Dashboard,
which will show a list of the notebooks, files, and subdirectories
in the directory where the notebook server was started.
Navigate to the notebook of your interest and open it in the dashboard.

For more information please refer to `Jupyter documentation <https://docs.jupyter.org/en/latest/running.html>`_

.. toctree::
   :maxdepth: 1

   Getting Started <notebooks/01-get_started.ipynb>
   Controlling `dpnp` fallback to `numpy` <notebooks/02-dpnp_numpy_fallback.ipynb>
