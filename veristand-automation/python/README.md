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
├── README.md              (this file)
├── requirements.txt       (Python deps)
├── conftest.py            (shared fixtures: system def path, deployment lifecycle)
├── test_veristand_smoke.py  (one minimal end-to-end test)
└── system-definition/     (placeholder for the example .nivssdf)
```

The actual sample files will land here as the session approaches.

## Running it

Once the sample is in place:

```bash
pip install -r requirements.txt
pytest -v
```
