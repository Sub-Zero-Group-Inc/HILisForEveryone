import pytest
import sys


def main():
    # Define which folders, files, or functions to test
    # You can specify folders, files, or indidual test functions here
    # If left blank, pytest will run all tests in the root directory
    files_to_test = [
        "test_veristand_smoke.py",
        # "test_veristand_smoke.py::test_engine_temperature_alert",
    ]

    # Arguments to pass to PyTest. You can modify these as needed.
    # fmt: off
    flags = [
        "--capture", "no",
        "--verbosity", "2",
    ]
    # fmt: on

    # Pass extra arguments to PyTest dynamically. Unused in this demo.
    cli_flags = []
    if len(sys.argv) > 1:
        cli_flags = [x for x in sys.argv[1:]]

    return pytest.main(files_to_test + flags + cli_flags)


if __name__ == "__main__":
    retcode = main()
    sys.exit(retcode)
