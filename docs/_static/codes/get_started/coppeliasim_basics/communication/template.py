#!/bin/python3
from dqrobotics.interfaces.vrep import DQ_VrepInterface
import time

vi = DQ_VrepInterface()


def main() -> None:
    try:
        vi.connect('127.0.0.1', 19997, 100, 10)
        vi.start_simulation()
        time.sleep(0.1)
        #---------------------------------------------------------
        # Your code here
        #---------------------------------------------------------
        vi.stop_simulation()
        vi.disconnect()

    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(e)
        vi.stop_simulation()
        vi.disconnect()


if __name__ == "__main__":
    main()