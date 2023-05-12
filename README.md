[![Build-test-upload mcpi package](https://github.com/IntelPython/DPEP/actions/workflows/mcpi_build_test_upload.yml/badge.svg)](https://github.com/IntelPython/DPEP/actions/workflows/mcpi_build_test_upload.yml)

# Data Parallel Extensions for Python*

Data Parallel Extensions for Python* extend numerical Python capabilities beyond CPU and allow even higher performance
gains on data parallel devices such as GPUs. It consists of three related projects:
* [**dpnp** – Data Parallel Extensions for Numpy*](https://github.com/IntelPython/dpnp) - a library that implements a subset
             of Numpy that can be executed on any data parallel device. The subset is a drop-in replacement of core
             Numpy functions and numerical data types.
* [**numba-dpex** – Data Parallel Extensions for Numba*](https://github.com/IntelPython/numba-dpex) - extension for Numba
             compiler that enables programming data parallel devices the same way you program CPU with Numba.
* [**dpctl** – Data Parallel Control library](https://github.com/IntelPython/dpctl) that provides utilities for device
              selection, allocation of data on devices, tensor data structure along with Python Array API standard
              implementation, and support for creation of user-defined data-parallel extensions.

## Learn more
Read more about [Data Parallel Extensions for Python](https://intelpython.github.io/DPEP/main/)

## Examples
Examples are located in `./examples`. Their names start with the 2-digit number followed by a descriptive name. You can run examples in any order, however, if
you are new to **Data Parallel Extensions for Python**, it is recommended to go in the order examples enumerated.

The following command will run the very first example of using **Data Parallel Extensions for Python**
```
python ./examples/01-hello_dpnp.py
```
## Tutorials
Jupyter Notebook-based Getting Started tutorials are located in `./notebooks` directory.

To run the tutorial, in the command line prompt type:
```
jupyter notebook
```
This will print some information about the notebook server in your terminal, including the URL of the web application (by default, `http://localhost:8888`):

```

$ jupyter notebook
[I 08:58:24.417 NotebookApp] Serving notebooks from local directory: /Users/catherine
[I 08:58:24.417 NotebookApp] 0 active kernels
[I 08:58:24.417 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
[I 08:58:24.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

It will then open your default web browser to this URL.

When the notebook opens in your browser, you will see the **Notebook Dashboard**, which will show a list of the notebooks, files, and subdirectories in the directory where the notebook server was started. Navigate to the notebook of your interest and open it in the dashboard.

For more information please refer to [Jupyter documentation](https://docs.jupyter.org/en/latest/running.html)

## Benchmarks
Data Parallel Extensions for Python provide a set of [benchmarks](https://github.com/IntelPython/dpbench) illustrating different aspects of implementing the performant code with Data Parallel Extensions for Python.
Benchmarks represent some real life numerical problem or some important part (kernel) of real life application. Each application/kernel is implemented in several variants (not necessarily all variants):
- Pure Python: Typically the slowest and used just as a reference implementation
- `numpy`: Same application/kernel implemented using NumPy library
- `dpnp`: Modified `numpy` implementation to run on a specific device. You can use `numpy` as a baseline while evaluating the `dpnp` implementation and its performance
- `numba @njit` array-style: application/kernel implemented using NumPy and compiled with Numba. You can use `numpy` as a baseline when evaluate `numba @njit` array-style implementat and its performance
- `numba @njit` direct loops (`prange`): Same application/kernel implemented using Numba compiler using direct loops. Sometimes array-style programming is cumbersome and performance inefficient. Using direct loop programming may lead to more readable and performance code. Thus, while evaluating the performance of direct loop implementation it is useful to compare array-style Numba implementation as a baseline
- `numba-dpex @dpjit` array-style: Modified `numba @njit` array-style implementation to compile and run on a specific device. You can use vanilla Numba implementation as a baseline while comparing `numba-dpex` implementation details and performance. You can also compare it against `dpnp` implementation to see how much extra performance `numba-dpex` can bring when you compile NumPy code for a given device
- `numba-dpex @dpjit` direct loops (`prange`): Modified `numba @njit` direct loop implementation to compile and run on a specific device. You can use vanilla Numba implementation as a baseline while comparing `numba-dpex` implementation details and performance. You can also compare it against `dpnp` implementation to see how much extra performance `numba-dpex` can bring when you compile NumPy code for a given device
- `numba-dpex @dpjit` kernel: Kernel-style programming, which is close to `@cuda.jit` programming model used in vanilla Numba
- `numba-mlir`: Array-style, direct loops and kernel-style implementations for experimental MLIR-based backend for Numba
- `cupy`: NumPy-like implementation using CuPy to run on CUDA-compatible devices
- `@cuda.jit`: Kernel-style Numba implementation to run on CUDA-compatible devices
- Native SYCL: Most applications/kernels also have DPC++ implementation, which can be used to compare performance of above implementations to DPC++ compiled code.

For more details please refer to `dpbench` [documentation](https://github.com/IntelPython/dpbench/blob/main/README.md).

## Demos
There are several demo applications illustrating the power of the **Data Parallel Extensions for Python**. They are:

- [Monte Carlo Pi](https://github.com/IntelPython/DPEP/tree/main/demos/mcpi>) -
The Monte Carlo method to estimate the value of $\pi$.

- [Mandelbrot Set](https://github.com/IntelPython/DPEP/tree/main/demos/mandelbrot) -
Visualization of the breathtaking process of diving in the famous Mandelbrot fractal

- [Game of Life](https://github.com/IntelPython/DPEP/tree/main/demos/game-of-life>) -
Visualization of the life evolution using famous Conway's model

For more details please refer to the documentation located in the individual demo directory.
