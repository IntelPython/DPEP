import argparse


def int_tuple(tuple_str):
    return tuple(map(int, tuple_str.split(",")))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Mandelbrot Set")
    parser.add_argument(
        "--variant",
        help="Implementation variant",
        type=str.casefold,
        choices=["numpy", "numba", "dpnp", "numba-dpex"],
        default="numpy",
    )
    parser.add_argument(
        "--max-frames",
        help="Stop game after specified amount of frames "
        "(default 0 - no stop frame)",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--gui",
        help="Render the evolution of the grid or do computation only and "
        "print statistics in the end. Default --no-gui",
        action="store_true",
        default=False,
    )
    w = 1024
    h = 800
    parser.add_argument(
        "--task-size",
        help=f"Window size. E.g. 800,600. Default {w},{h}",
        type=int_tuple,
        default=int_tuple(f"{w},{h}"),
    )

    args, _ = parser.parse_known_args(argv)
    return args
