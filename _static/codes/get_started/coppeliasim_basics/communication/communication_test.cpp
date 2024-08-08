#include <iostream>
#include <dqrobotics/interfaces/vrep/DQ_VrepInterface.h>
#include <thread>

int main()
{
    auto vi = DQ_VrepInterface();
    try {
        if (!vi.connect("127.0.0.1", 19997,100,10))
            throw std::runtime_error("Unable to connect to CoppeliaSim.");
        vi.start_simulation();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        DQ x = vi.get_object_pose("/Frame_x");
        std::cout<<"Position: "<<x.translation()<<std::endl;
        std::cout<<"the test was successful!"<<std::endl;
        vi.stop_simulation();
        vi.disconnect();

    } catch (std::exception& e) {
        std::cout<<e.what()<<std::endl;
        vi.stop_simulation();
        vi.disconnect();
    }
    return 0;
}