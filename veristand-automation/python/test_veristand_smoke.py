import pytest
from niveristand.legacy.NIVeriStand import Workspace2

from core.utils import wait_for_channel
from engine_demo import EngineDemo


def test_veristand_connection(engine_demo: EngineDemo):
    print("If this test passes, Veristand successfully deployed")
    assert True


def test_engine_on_off(engine_demo: EngineDemo):
    engine_demo.engine_on()
    assert wait_for_channel(
        engine_demo.engine_power, True, timeout=5
    ), "Engine did not turn on in time"

    engine_demo.engine_off()
    assert wait_for_channel(
        engine_demo.engine_power, False, timeout=5
    ), "Engine did not turn off in time"


def test_engine_idle_speed(engine_demo: EngineDemo):
    engine_demo.engine_on()
    assert wait_for_channel(
        engine_demo.engine_power, True, timeout=5
    ), "Engine did not turn on in time"

    assert wait_for_channel(
        engine_demo.actual_rpm,
        engine_demo.idle_speed.read(),
        timeout=5,
        abs_tolerance=10,
    ), "Engine did not reach idle speed in time"
    
    engine_demo.engine_off()
    assert wait_for_channel(
        engine_demo.engine_power, False, timeout=5
    ), "Engine did not turn off in time"


@pytest.mark.parametrize("rpm", [5000, 10000])
def test_engine_set_speed(engine_demo: EngineDemo, rpm):
    engine_demo.engine_on()
    engine_demo.desired_rpm.write(rpm)
    assert wait_for_channel(
        engine_demo.actual_rpm, rpm, timeout=6, abs_tolerance=10
    ), f"Engine did not reach set RPM {rpm} in time"


@pytest.mark.parametrize("rpm", [5000, 10000])
def test_engine_ramp_down(engine_demo: EngineDemo, rpm):
    engine_demo.engine_on()

    engine_demo.desired_rpm.write(rpm)
    assert wait_for_channel(
        engine_demo.actual_rpm, rpm, timeout=6, abs_tolerance=10
    ), f"Engine did not reach set RPM {rpm} in time"

    engine_demo.engine_off()
    assert wait_for_channel(
        engine_demo.actual_rpm, 0, timeout=6, abs_tolerance=10
    ), "Engine did not ramp down to 0 RPM in time"


def test_engine_temperature_alert(engine_demo: EngineDemo):
    engine_demo.engine_on()

    # Engine won't oveheat unless we change environment temp or alert temp
    # We unfortunately can't control model parameters channels unless an alias is made for them in VeriStand
    engine_demo.engine_temperature_alert.write(124)

    engine_demo.desired_rpm.write(10000)
    assert wait_for_channel(
        engine_demo.actual_rpm, 10000, timeout=6, abs_tolerance=10
    ), "Engine did not reach set RPM 10000 in time"
    print("Engine at 10000 RPM")

    assert wait_for_channel(
        engine_demo.engine_temp, 124, timeout=60, abs_tolerance=1
    ), "Engine did not reach alert temperature in time"
    print("Engine reached alert temperature")

    assert wait_for_channel(
        engine_demo.engine_power, False, timeout=45
    ), "Engine did not turn off after reaching alert temperature"
