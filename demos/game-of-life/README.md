# Conway's Game Of Life
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Join the chat at https://matrix.to/#/#Data-Parallel-Python_community:gitter.im](https://badges.gitter.im/Join%20Chat.svg)](https://app.gitter.im/#/room/#Data-Parallel-Python_community:gitter.im)

The Game of Life is a cellular automaton devised by John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state.
One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

![Game Of Life Demo](https://github.com/samaid/GameOfLife/blob/main/images/game-of-life-lowres.gif)

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states,
live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally,
vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:

* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system.
The first generation is created by applying the above rules simultaneously to every cell in the seed,
live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is
sometimes called a tick.
Each generation is a pure function of the preceding one.
The rules continue to be applied repeatedly to create further generations.

For further details please address [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

Installation
------------
`conda install -c "pycoddiy/label/dev" game-of-life-demo`

Also, if you are using GUI, you will need to add
`opencv-python` to the environment:

`pip install opencv-python`

Running demo
------------

From command line type:
`game_of_life  [command line options]`

* `--variant [numba, numpy, dpnp, numba-dpex]` (default `numpy`) - implementation variant
* `--threading-layer [omp, tbb, workqueue]` (default `omp`) - threading layer for `numba` implementation
* `--parallel` (default) or `--no-parallel` - keyword argument `parallel=` for `@njit`.
  Used along with `--variant numba`
* `--frames-count` - stop rendering after a specified amount of frames. Default 0 meaning that the demo
  does not stop until user action, e.g. close window
* `--gui` (default) or `--no-gui` - render the evolution of the grid or do the computation only and
  print performance statistics in the end.
* `--stats` (default) or `--no-stats` - Display statistics in gui while running or not
* `--task-size` - size of the grid WIDTH, HEIGHT. Example: `960,540` (default)
