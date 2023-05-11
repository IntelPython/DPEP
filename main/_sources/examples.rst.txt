.. _examples:
.. include:: ./ext_links.txt

List of examples
================
All examples are located in the `GitHub repository<https://github.com/IntelPython/DPEP/tree/main/examples>`_.
Their names start with the 2-digit number followed by a descriptive name.
You can run examples in any order, however, if
you are new to the Data Parallel Extensions for Python, it is recommended to go in the order examples are enumerated.

The following command will run the very first example of using Data Parallel Extensions for Python

.. code-block:: console

    python ./examples/01-hello_dpnp.py

These are listings of these examples:

.. literalinclude:: ../../examples/01-hello_dpnp.py
   :language: python
   :lines: 27-
   :caption: **EXAMPLE 01:** Your first NumPy code running on GPU
   :name: examples_01_hello_dpnp

.. literalinclude:: ../../examples/02-dpnp_device.py
   :language: python
   :lines: 27-
   :caption: **EXAMPLE 02:** Select device type while creating array
   :name: examples_02_dpnp_device

.. literalinclude:: ../../examples/03-dpnp2numba-dpex.py
   :language: python
   :lines: 27-
   :caption: **EXAMPLE 03:** Compile dpnp code with numba-dpex
   :name: examples_03_dpnp2numba_dpex

.. literalinclude:: ../../examples/04-dpctl_device_query.py
   :language: python
   :lines: 27-
   :caption: **EXAMPLE 04:** Get information about devices
   :name: examples_04_dpctl_device_query

