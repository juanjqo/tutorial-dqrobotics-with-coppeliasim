Communication test
******************


.. tab-set::

    .. tab-item:: Matlab


         .. code-block:: python

                clear all;
                close all;
                clc;

                include_namespace_dq;
                vi = DQ_VrepInterface();

                try
                    vi.connect('127.0.0.1', 19997);
                    vi.start_simulation();
                    pause(0.1);
                    vi.stop_simulation();
                    vi.disconnect();
                    disp('The test was successful!')
                catch ME
                    vi.stop_simulation();
                    vi.disconnect();
                    rethrow(ME)
                end


    .. tab-item:: Python

         .. code-block:: python

                from dqrobotics.interfaces.vrep import DQ_VrepInterface
                import time

                vi = DQ_VrepInterface()

                try:
                    vi.connect('127.0.0.1', 19997, 100, 10)
                    vi.start_simulation()
                    time.sleep(0.1)
                    vi.stop_simulation()
                    vi.disconnect()
                    print('The test was successful!')

                except Exception as exp:
                    print(exp)
                    vi.stop_simulation()
                    vi.disconnect()

    .. tab-item:: C++

            .. code-block:: cpp

                #include <iostream>
                #include <dqrobotics/interfaces/vrep/DQ_VrepInterface.h>
                #include <thread>

                int main()
                {
                    auto vi = DQ_VrepInterface();
                    try {
                        vi.connect(19997,100,10);
                        vi.start_simulation();
                        std::this_thread::sleep_for(std::chrono::milliseconds(100));
                        vi.stop_simulation();
                        vi.disconnect();
                        std::cout<<"the test was successful!"<<std::endl;
                    } catch (std::exception& e) {
                        std::cout<<e.what()<<std::endl;
                        vi.stop_simulation();
                        vi.disconnect();
                    }
                    return 0;

