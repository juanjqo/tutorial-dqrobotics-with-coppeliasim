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