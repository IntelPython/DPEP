.. _benchmarks:
.. include:: ./ext_links.txt

Benchmarks
==========

**Data Parallel Extensions for Python** provide a set of
`benchmarks<https://github.com/IntelPython/dpbench>`_ illustrating different aspects of
implementing the performant code with Data Parallel Extensions for Python.
Benchmarks represent some real life numerical problem or some important part (kernel) of real life application.
Each application/kernel is implemented in several variants (not necessarily all variants):

- Pure Python: Typically the slowest and used just as a reference implementation

- ``numpy``: Same application/kernel implemented using NumPy library

- ``dpnp``: Modified numpy implementation to run on a specific device. You can use numpy as a
baseline while evaluating the dpnp implementation and its performance

- ``numba @njit`` array-style: application/kernel implemented using NumPy and compiled with Numba.
You can use numpy as a baseline when evaluate numba @njit array-style implementat and its performance

- ``numba @njit`` direct loops (prange): Same application/kernel implemented using Numba
compiler using direct loops. Sometimes array-style programming is cumbersome and
performance inefficient. Using direct loop programming may lead to more
readable and performance code. Thus, while evaluating the performance of direct loop
implementation it is useful to compare array-style Numba implementation as a baseline

- ``numba-dpex @dpjit`` array-style: Modified numba @njit array-style implementation to
compile and run on a specific device. You can use vanilla Numba implementation as
a baseline while comparing numba-dpex implementation details and performance.
You can also compare it against dpnp implementation to see how much extra performance
numba-dpex can bring when you compile NumPy code for a given device

- ``numba-dpex @dpjit`` direct loops (prange): Modified numba @njit direct loop implementation
to compile and run on a specific device. You can use vanilla Numba implementation
as a baseline while comparing numba-dpex implementation details and performance.
You can also compare it against dpnp implementation to see how much extra performance
numba-dpex can bring when you compile NumPy code for a given device

- ``numba-dpex @dpjit`` kernel: Kernel-style programming, which is close to @cuda.jit
programming model used in vanilla Numba

- ``numba-mlir``: Array-style, direct loops and kernel-style implementations
for experimental MLIR-based backend for Numba

- ``cupy``: NumPy-like implementation using CuPy to run on CUDA-compatible devices

- ``@cuda.jit``: Kernel-style Numba implementation to run on CUDA-compatible devices

- Native SYCL: Most applications/kernels also have DPC++ implementation, which
can be used to compare performance of above implementations to DPC++ compiled code.

These benchmarks are implemented in ``dpbench`` framework, which allows you to run
all or select benchmarks and variants to evaluate their performance on different hardware.

For more details please refer to ``dpbench``
`documentation<https://github.com/IntelPython/dpbench/blob/main/README.md>`_.