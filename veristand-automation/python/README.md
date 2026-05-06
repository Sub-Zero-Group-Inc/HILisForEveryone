# Python `pytest` + VeriStand

A minimal `pytest` example that automates VeriStand test execution.

## What it demonstrates

- Connecting to a VeriStand system definition from Python.
- Deploying and running a real-time model.
- Driving stimulus channels (the inputs your DUT responds to).
- Reading response channels (what the DUT does in return).
- Writing assertions that turn channel values into pass/fail outcomes.
- Cleaning up the deployment regardless of test outcome (fixtures + teardown).

## Prerequisites

- Python 3.10+
- A VeriStand installation reachable from the host running pytest.
- A VeriStand system definition (`.nivssdf`) appropriate for your DUT.
- The Python packages listed in `requirements.txt` (added with the sample).

## Layout (planned)

```
python-pytest-veristand/
├── core/                           Folder of helper functions for writing tests
├── conftest.py                     (shared fixtures: system def path, deployment lifecycle)
├── engine_demo.py                  Python object for organizing VeriStand channels
├── pytest_runner.py                A script to easily run the tests
├── README.md                       (this file)
├── requirements.txt                (Python deps)
└── test_veristand_smoke.py         (one minimal end-to-end test)
```

The actual sample files will land here as the session approaches.

## Running it

Once the sample is in place:

```powershell
python -m pip install -r requirements.txt
python pytest_runner.py
```

or

```powershell
python -m pip install -r requirements.txt
pytest -v
```

## Reccomended Reading

- [PyTest Documentation](https://docs.pytest.org/en/stable/index.html)
- [Veristand User Manual](https://www.ni.com/docs/en-US/bundle/veristand/page/user-manual-welcome.html)
- [Automate the Boring Stuff -- Python Tutorial](https://automatetheboringstuff.com/)
