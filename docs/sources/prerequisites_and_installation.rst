.. _prerequisites_and_installation:
.. include:: ./ext_links.txt

.. |copy| unicode:: U+000A9

.. |trade| unicode:: U+2122

Prerequisites and Installation
==============================

1. Device Drivers
******************

To start programming data parallel devices beyond CPU, you need an appropriate hardware.
For example, Data Parallel Extensions for Python work fine on Intel(R) laptops with integrated graphics.
In majority of cases, your laptop already has all necessary device drivers installed. But if you want the most
up-to-date driver, you can 
`update it to the latest one <https://www.intel.com/content/www/us/en/download-center/home.html>`_.
Follow device driver installation instructions
to complete this step.

All other necessary components are be installed with
Data Parallel Extensions for Python.

2. Python Interpreter
**********************

Install Python 3.8, 3.9, or 3.10 to your system. 

If you do not have one yet, the easiest way to do
that is to install `Intel Distribution for Python*`_.
It installs all essential Python numerical and machine
learning packages optimized for the Intel(R) hardware, including Data Parallel Extensions for Python*.


If you have Python installation from another vendor, you need is to install Data Parallel
Extensions for Python manually.

3. Data Parallel Extensions for Python
***************************************

Skip this step if you already have Intel |copy| Distribution for Python or Intel |copy| AI Analytics Toolkit on your system.

.. WARNING:: Update ``conda`` and ``pip`` to the latest version, before installing ``numba-dpex``. 

The easiest way to install Data Parallel Extensions for Python is to install ``numba-dpex``:

* Conda: ``conda install numba-dpex``
* Pip: ``pip install numba-dpex``

These commands install  along with its dependencies, including ``dpnp``, ``dpctl``,
and required compiler runtimes and drivers.

