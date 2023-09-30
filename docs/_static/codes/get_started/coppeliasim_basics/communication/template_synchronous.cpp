#include <iostream>
#include <dqrobotics/interfaces/vrep/DQ_VrepInterface.h>
#include <thread>

int main()
{
    auto vi = DQ_VrepInterface();
    try {
        vi.connect("127.0.0.1", 19997,100,10);
        vi.set_synchronous(true);
        vi.start_simulation();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        //---------------Your code here----------------------------
        vi.trigger_next_simulation_step();
        //---------------------------------------------------------
        vi.wait_for_simulation_step_to_end();
        vi.stop_simulation();
        vi.disconnect();
    } catch (std::exception& e) {
        std::cout<<e.what()<<std::endl;
        vi.stop_simulation();
        vi.disconnect();
    }
    return 0;
}