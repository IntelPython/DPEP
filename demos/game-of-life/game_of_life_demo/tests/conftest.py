def pytest_addoption(parser):
    parser.addoption("--variant", action="store", help="Implementation variant")
    parser.addoption(
        "--parallel", action="store_true", help="@njit(parallel=True/False) setting"
    )
    parser.addoption(
        "--no-parallel", action="store_false", help="@njit(parallel=True/False) setting"
    )
