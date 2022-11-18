.. _index:
.. include:: ./ext_links.txt

.. image:: ./_images/DPEP-large.png
    :width: 400px
    :align: center
    :alt: Data Parallel Extensions for Python

Data Parallel Extensions for Python
===================================

Data Parallel Extensions for Python* extend numerical Python capabilities beyond CPU and allow even higher performance
gains on data parallel devices such as GPUs. It consists of three foundational packages:

* **dpnp** - Data Parallel Extensions for `Numpy*`_ - a library that implements a subset of
  Numpy that can be executed on any data parallel device. The subset is a drop-in replacement
  of core Numpy functions and numerical data types.
* **numba_dpex** - Data Parallel Extensions for `Numba*`_ - extension for Numba compiler
  that enables programming data parallel devices the same way you program CPU with Numba.
* **dpctl - Data Parallel Control library** that provides utilities for device selection,
  allocation of data on devices, tensor data structure along with `Python* Array API Standard`_ implementation, and support for creation of user-defined data-parallel extensions.

Table of Contents
*****************
.. toctree::
    :maxdepth: 2

    prerequisites_and_installation
    parallelism
    heterogeneous_computing
    programming_dpep
    examples
    useful_links
