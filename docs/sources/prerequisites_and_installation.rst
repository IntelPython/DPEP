.. _prerequisites_and_installation:
.. include:: ./ext_links.txt

.. |copy| unicode:: U+000A9

.. |trade| unicode:: U+2122

Prerequisites and installation
==============================

1. Device drivers and runtimes
******************

We ask you to install the `Intel® oneAPI DPC++/C++ Compiler Runtime for Windows* <https://www.intel.com/content/www/us/en/developer/articles/tool/compilers-redistributable-libraries-by-version.html>`_ for correct work of Data Parallel Extensions for Python with CPU.
..Note:: If you installed Intel® oneAPI Base Toolkit on your laptop, you may ignore the step above.

All other necessary components for programming data parallel devices will be installed with
Data Parallel Extensions for Python.

2. Python interpreter
**********************

You will need Python 3.8, 3.9, or 3.10 installed on your system. If you do not have one yet the easiest way to do
that is to install `Intel Distribution for Python*`_.
It will install all essential Python numerical and machine
learning packages optimized for Intel hardware, including Data Parallel Extensions for Python*.
If you have Python installation from another vendor, it is fine too. All you need is to install Data Parallel
Extensions for Python manually.

3. Windows
**********************

Data Parallel Extensions for Python* can be installed and used on various Windows distributions. 
But preferable Windows platforms is Windows 10 and Windows 11.


4. Data Parallel Extensions for Python
***************************************

You can skip this step if you already installed Intel |copy| Distribution for Python or Intel |copy| AI Analytics Toolkit.

The easiest way to install Data Parallel Extensions for Python is to install numba-dpex:

Conda: ``conda install numba-dpex``

Pip: ``pip install numba-dpex``

The above commands will install ``numba-dpex`` along with its dependencies, including ``dpnp``, ``dpctl``,
and required compiler runtimes and drivers.

.. WARNING::
   Before installing with conda or pip it is strongly advised to update ``conda`` and ``pip`` to latest versions
   
5. Quick start and installation test
***************************************

You can run the following peaces of code to test the installation: 
1. The ``numba-dpex`` extension allows to compile and offload data parallel regions to any data parallel device.
To test installation please execute the following example:

.. literalinclude:: https://github.com/IntelPython/numba-dpex/blob/main/numba_dpex/examples/kernel/vector_sum.py
   :language: python
   :lines: 47-
   :caption: **EXAMPLE:** Test installation of ``numba-dpex`` on the example of vector sum 
   :name: ex_05_vector_sum_numba_dpex

2. To test the installation of ``dpctl`` you may use several options:
You may run the command:
``pytest –pyargs dpctl``
or run
``python -m dpctl -l``

3. To test the installation of ``dpnp`` please run the example:

.. literalinclude:: ../../examples/06-dpctl_dpnp_test.py
   :language: python
   :lines: 41-
   :caption: **EXAMPLE:** Test installation of ``dpnp``
   :name: ex_06_dpnp_test

The output should be looks like to
    ``Name            Intel(R) Iris(R) Xe Graphics``
    ``Driver version  1.3.23904``
    ``Vendor          Intel(R) Corporation``
    ``Profile         FULL_PROFILE``
    ``Filter string   level_zero:gpu:0``

``None``
``Array x is located on the device: Device(level_zero:gpu:0)``
``Array x is: [1 2 3]``
``Result y is located on the device: Device(level_zero:gpu:0)``
``y =  6``

``Dpctl`` provides API to manage specific SYCL resources for SYCL-based Python packages. ``Dpnp`` uses ``dpctl`` as a global SYCL queue manager. 
Above code illustrates simple usage of ``dpnp`` in combination with ``dpctl``.

