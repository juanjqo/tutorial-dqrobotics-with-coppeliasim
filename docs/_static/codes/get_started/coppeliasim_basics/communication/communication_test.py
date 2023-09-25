from dqrobotics.interfaces.vrep import DQ_VrepInterface
import time


vi = DQ_VrepInterface()


try:

    vi.connect('127.0.0.1', 19997, 100, 10)
    vi.start_simulation()
    time.sleep(0.1)
    x = vi.get_object_pose('Frame_x')
    vi.stop_simulation()
    vi.disconnect()
    print("Position: ", x.translation())
    print('The test was successful!')


except Exception as exp:
    print(exp)
    vi.stop_simulation()
    vi.disconnect()