#!/bin/python3
from dqrobotics.interfaces.vrep import DQ_VrepInterface
import time


def main() -> None:
    vi = DQ_VrepInterface()
    try:
        if not vi.connect("127.0.0.1", 19997, 100, 10):
            raise RuntimeError("Unable to connect to CoppeliaSim.")

        vi.set_synchronous(True)
        vi.start_simulation()
        time.sleep(0.1)
        # --------------Your code here----------------------------
        vi.trigger_next_simulation_step()
        vi.wait_for_simulation_step_to_end()
        # ---------------------------------------------------------

    except (Exception, KeyboardInterrupt) as e:
        print(e)
        pass

    finally:
        vi.stop_simulation()
        vi.disconnect()


if __name__ == "__main__":
    main()