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
        time_simulation_step = 0.05
        y_0 = vi.get_object_pose("/Sphere").translation().vec3()[2]
        print("---------------------------")
        print("Initial height: ", y_0)
        print("---------------------------")
        for i in range(0, 6):
            t = i * time_simulation_step
            y_sim = vi.get_object_pose("/Sphere").translation().vec3()[2]
            y_est = y_0 - 0.5 * 9.81 * pow(t, 2)
            vi.trigger_next_simulation_step()
            vi.wait_for_simulation_step_to_end()
        print("Elapsed time: ", t)
        print("Estimated height: ", y_est, "Measured height: ", y_sim)

    except (Exception, KeyboardInterrupt) as e:
        print(e)
        pass

    finally:
        vi.stop_simulation()
        vi.disconnect()


if __name__ == "__main__":
    main()



