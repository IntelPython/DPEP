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
Read more about [Data Parallel Extensions for Python[(https://intelpython.github.io/DPEP/main/)

## Examples
Examples are located in `./examples`. Their names start with the 2-digit number followed by a descriptive name. You can run examples in any order, however, if  
you are new to **Data Parallel Extensions for Python**, it is recommended to go in the order examples enumerated.
```
> python ./examples/01_hello-dpnp.py
```
