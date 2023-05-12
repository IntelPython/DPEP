# Mandelbrot Set

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Join the chat at https://matrix.to/#/#Data-Parallel-Python_community:gitter.im](https://badges.gitter.im/Join%20Chat.svg)](https://app.gitter.im/#/room/#Data-Parallel-Python_community:gitter.im)

Mandelbrot set demo implemented using NumPy, Numba, DPNP, and Numba-DPEx.

## What it is

The Mandelbrot set is the set of complex numbers $c$ for which the function
$f_{c}(z)=z^{2}+c$ does not diverge to infinity when iterated from  $z=0$, i.e.,
for which the sequence $f_{c}(0)$, $f_{c}(f_{c}(0))$, etc., remains bounded in absolute value.

Images of the Mandelbrot set exhibit an elaborate and infinitely complicated boundary
that reveals progressively ever-finer recursive detail at increasing magnifications

For further details please visit respective [Wikipedia article](https://en.wikipedia.org/wiki/Mandelbrot_set).

## How to run demo

### Running from installed conda package

Install the demo as follows:
`conda install -c pycoddiy/label/dev mandelbrot-demo`

From command line type:
`mandelbrot  [command line options]`

* `--variant [numba, numpy, dpnp, numba-dpex]` (default `numpy`) - implementation variant
* `--frames-count` - stop rendering after a specified amount of frames. Default 0 meaning that the demo
  does not stop until user action, e.g. close window
* `--gui` (default) or `--no-gui` - render the evolution of the grid or do the computation only and
  print performance statistics in the end.
* `--task-size` - window size WIDTH, HEIGHT. Example: 1024,800

### Running from GitHub sources
Clone repository to a local project directory:
```
git clone https://github.com/samaid/Mandelbrot.git
cd ./Mandelbrot
```

From the command line type:
`python mandelbrot_demo.py [command line options]`

* `--variant [numba, numpy, dpnp, numba-dpex]` (default `numpy`) - implementation variant
* `--frames-count` - stop rendering after a specified amount of frames. Default 0 meaning that the demo
  does not stop until user action, e.g. close window
* `--gui` (default) or `--no-gui` - render the evolution of the grid or do the computation only and
  print performance statistics in the end.
* `--task-size` - window size WIDTH, HEIGHT. Example: 1024,800
