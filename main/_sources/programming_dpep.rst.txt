.. _programming_dpep:
.. include:: ./ext_links.txt

Programming with Data Parallel Extensions for Python
====================================================

As we briefly outlined, **Data Parallel Extensions for Python** consist of three foundational packages:

* the `Numpy*`_-like library, ``dpnp``;
* the compiler extension for `Numba*`_, ``numba-dpex``
* the library for managing devices, queues, and heterogeneous data, ``dpctl``.

Their underlying implementation is based on `SYCL*`_ standard, which is a cross-platform abstraction layer
for heterogeneous computing on data parallel devices, such as CPU, GPU, or domain specific accelerators.

Scalars vs. 0-dimensional arrays
********************************

Primitive types such as Python’s and Numpy’s ``float``, ``int``, or ``complex``, used to represent scalars,
have the host storage. In contrast, ``dpctl.tensor.usm_ndarray`` and ``dpnp.ndarray`` have USM storage
and carry associated allocation queue. For the :ref:`Compute-Follows-Data` consistent behavior
all ``dpnp`` operations that produce scalars will instead produce respective 0-dimensional arrays.

That implies, that some code changes may be needed to replace scalar math operations with respective
``dpnp`` array operations. See `Data Parallel Extension for Numpy*`_ - **API Reference** section for details.

Data Parallel Extension for Numpy - dpnp
****************************************

The ``dpnp`` library is a bare minimum to start programming numerical codes for data parallel devices.
You may already have a Python script written in `Numpy*`_. Being a drop-in replacement of (a subset of) `Numpy*`_,
to execute your `Numpy*`_ script on GPU usually requires changing just a few lines of the code:

.. literalinclude:: ../../examples/01-hello_dpnp.py
   :language: python
   :lines: 27-
   :caption: Your first NumPy code running on GPU
   :name: ex_01_hello_dpnp

In this example ``np.asarray()`` creates an array on the default `SYCL*`_ device, which is ``"gpu"`` on systems
with integrated or discrete GPU (it is ``"cpu"`` on systems that do not have GPU).
The queue associated with this array is now carried with ``x``, and ``np.sum(x)`` will derive it from ``x``,
and respective pre-compiled kernel implementing ``np.sum()`` will be submitted to that queue.
The result ``y`` will be allocated on the device 0-dimensional array associated with that queue too.

All ``dpnp`` array creation routines as well as random number generators have additional optional keyword arguments
``device``, ``queue``, and ``usm_type``, using which you can explicitly specify on which device or queue you want
the tensor data to be created along with USM memory type to be used (``"host"``, ``"device"``, or ``"shared"``).
In the following example we create the array ``x`` on the GPU device, and perform a reduction sum on it:

.. literalinclude:: ../../examples/02-dpnp_device.py
   :language: python
   :lines: 27-
   :caption: Select device type while creating array
   :name: ex_02_dpnp_device

Data Parallel Extension for Numba - numba-dpex
**********************************************

`Numba*`_ is a powerful Just-In-Time (JIT) compiler that works best on `Numpy*`_ arrays, `Numpy*`_ functions, and loops.
Data parallel loops is where the data parallelism resides. It allows leveraging all available CPU cores,
SIMD instructions, and schedules those in a way that exploits maximum instruction-level parallelism.
The ``numba-dpex`` extension allows to compile and offload data parallel regions to any data parallel device.
It takes just a few lines to modify your CPU `Numba*`_ script to run on GPU.

