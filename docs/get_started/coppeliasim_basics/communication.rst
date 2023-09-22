Communication test
******************



.. image:: /_static/basics/frame_x_sc.png
    :align: center

.. tab-set::

    .. tab-item:: Matlab


         .. code-block:: python
                :emphasize-lines: 13

                clear all;
                close all;
                clc;


                include_namespace_dq;
                vi = DQ_VrepInterface();

                try
                    vi.connect('127.0.0.1', 19997);
                    vi.start_simulation();
                    pause(0.1);
                    x = vi.get_object_pose('Frame_x');
                    vi.stop_simulation();
                    vi.disconnect();
                    disp('Position: ')
                    translation(x)
                    disp('The test was succesful!')
                catch ME
                    vi.stop_simulation();
                    vi.disconnect();
                    rethrow(ME)
                end


    .. tab-item:: Python

         .. code-block:: python
                :emphasize-lines: 13

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

    .. tab-item:: C++

            .. code-block:: cpp
                :emphasize-lines: 12

                #include <iostream>
                #include <dqrobotics/interfaces/vrep/DQ_VrepInterface.h>
                #include <thread>

                int main()
                {
                    auto vi = DQ_VrepInterface();
                    try {
                        vi.connect("10.198.113.136", 19997,100,10);
                        vi.start_simulation();
                        std::this_thread::sleep_for(std::chrono::milliseconds(100));
                        DQ x = vi.get_object_pose("Frame_x");
                        vi.stop_simulation();
                        vi.disconnect();
                        std::cout<<"Position: "<<x.translation()<<std::endl;
                        std::cout<<"the test was successful!"<<std::endl;
                    } catch (std::exception& e) {
                        std::cout<<e.what()<<std::endl;
                        vi.stop_simulation();
                        vi.disconnect();
                    }
                    return 0;
                }


