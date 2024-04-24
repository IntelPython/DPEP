import pytest
from game_of_life_demo import int_tuple
from game_of_life_demo.impl.arg_parser import parse_args


@pytest.mark.parametrize("variant_str", ["numpy", "numba", "dpnp", "numba-dpex"])
def test_variant(variant_str):
    args = parse_args(["--variant", variant_str])
    assert args.variant == variant_str


@pytest.mark.parametrize("threading_str", ["omp", "tbb", "workqueue"])
def test_threading(threading_str):
    args = parse_args(["--threading-layer", threading_str])
    assert args.threading_layer == threading_str


@pytest.mark.parametrize("frames_count", [0, 100])
def _test_frames_count(frames_count):
    args = parse_args(["--frames-count", frames_count])
    assert args.frames_count == frames_count


@pytest.mark.parametrize("task_size", ["3, 3", "100, 100"])
def test_task_size(task_size):
    args = parse_args(["--task-size", task_size])
    assert args.task_size == int_tuple(task_size)


def test_parallel_true():
    args = parse_args(["--parallel"])
    assert args.parallel


def test_parallel_false():
    args = parse_args(["--no-parallel"])
    assert not args.parallel


def test_gui_true():
    args = parse_args(["--gui"])
    assert args.gui


def test_gui_false():
    args = parse_args(["--no-gui"])
    assert not args.gui


def test_stats_true():
    args = parse_args(["--stats"])
    assert args.stats


def test_stats_false():
    args = parse_args(["--no-stats"])
    assert not args.stats
