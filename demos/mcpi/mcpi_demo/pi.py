import time

from mcpi_demo.impl.arg_parser import parse_args
from mcpi_demo.impl.impl_versioner import monte_carlo_pi


def main():
    args = parse_args()
    batch_size = args.batch_size
    n_batches = args.n_batches
    print(
        f"Estimating Pi with {args.variant} for {n_batches} "
        f"Sbatches of size {batch_size}..."
    )
    t1 = time.time()
    pi, pi_std = monte_carlo_pi(batch_size, n_batches)
    t2 = time.time()
    print(f"Pi={pi}, std={pi_std}")
    print("Done in ", t2 - t1, "seconds...")


if __name__ == "__main__":
    main()
