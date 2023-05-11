# MCPI - Monte Carlo estimation of Pi using numpy, numba, dpnp, numba-dpex

This is a "Hello, World" application in Monte Carlo methods. It stresses random number generation 
along with some other math required for implementation of the Acceptance-Rejection technique.

For details please refer to [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)

## How to run

`python -m mcpi_demo [options]`

Demo can be invoked in several ways:

1. Cloning Github repo and running `python mcpi.py [options]`
2. Cloning Github repo and running `python -m mcpi_demo [options]`
3. Installing conda package and invoking executable
   * `conda install -c pycoddiy/label/dev mcpi-demo`
   * `mcpi [options]`

### Options

The following options are allowed:
* `--variant [numpy, numba, dpnp, numba-dpex]` (default `numpy`): Implementation variant
* `--batch-size`: Number of trial points in the batch
* `--n-batches`:  Number of batches

## Jupyter Notebook
The Monte Carlo Pi demo is also supplemented with the [Juoyter Notebook](https://github.com/samaid/mcpi/blob/main/mcpi.ipynb),
where step by step we illustrate the idea of the algorithm.
