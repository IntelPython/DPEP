from mandelbrot_demo.impl.arg_parser import parse_args

RUN_VERSION = parse_args().variant

if RUN_VERSION == "Numba".casefold():
    from mandelbrot_demo.impl.impl_numba import asnumpy
    from mandelbrot_demo.impl.impl_numba import init_values
    from mandelbrot_demo.impl.impl_numba import mandelbrot
elif RUN_VERSION == "NumPy".casefold():
    from mandelbrot_demo.impl.impl_numpy import asnumpy
    from mandelbrot_demo.impl.impl_numpy import init_values
    from mandelbrot_demo.impl.impl_numpy import mandelbrot
elif RUN_VERSION == "DPNP".casefold():
    from mandelbrot_demo.impl.impl_dpnp import asnumpy
    from mandelbrot_demo.impl.impl_dpnp import init_values
    from mandelbrot_demo.impl.impl_dpnp import mandelbrot
elif RUN_VERSION == "Numba-DPEX".casefold():
    from mandelbrot_demo.impl.impl_numba_dpex import asnumpy
    from mandelbrot_demo.impl.impl_numba_dpex import init_values
    from mandelbrot_demo.impl.impl_numba_dpex import mandelbrot
