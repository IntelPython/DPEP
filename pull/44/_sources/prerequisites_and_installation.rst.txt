.. _prerequisites_and_installation:
.. include:: ./ext_links.txt

.. |copy| unicode:: U+000A9

.. |trade| unicode:: U+2122

Prerequisites and Installation
==============================

1. Device Drivers
******************

To start programming data parallel devices beyond CPU, you will need an appropriate hardware.
For example, Data Parallel Extensions for Python work fine on Intel |copy| laptops with integrated graphics.
In majority of cases, your Windows*-based laptop already has all necessary device drivers installed. But if you want the most
up-to-date driver, you can always
`update it to the latest one <https://www.intel.com/content/www/us/en/download-center/home.html>`_.
Follow device driver installation instructions
to complete this step.

All other necessary components for programming data parallel devices will be installed with
Data Parallel Extensions for Python.

2. Python Interpreter
**********************

You will need Python 3.8, 3.9, or 3.10 installed on your system. If you do not have one yet the easiest way to do
that is to install `Intel Distribution for Python*`_.
It installs all essential Python numerical and machine
learning packages optimized for the Intel hardware, including Data Parallel Extensions for Python*.
If you have Python installation from another vendor, it is fine too. All you need is to install Data Parallel
Extensions for Python manually as shown in the next section.

3. Data Parallel Extensions for Python
***************************************

Skip this step if you already installed Intel |copy| Distribution for Python.

The easiest way to install Data Parallel Extensions for Python is to install numba-dpex:

* Conda: ``conda install numba-dpex``

* Pip: ``pip install numba-dpex``

These commands install ``numba-dpex`` along with its dependencies, including ``dpnp``, ``dpctl``,
and required compiler runtimes.

.. WARNING::
   Before installing with conda or pip it is strongly advised to update ``conda`` and ``pip`` to latest versions
