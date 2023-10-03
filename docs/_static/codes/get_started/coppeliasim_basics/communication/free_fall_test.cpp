#include <iostream>
#include <dqrobotics/interfaces/vrep/DQ_VrepInterface.h>
#include <thread>

int main()
{
    auto vi = DQ_VrepInterface();
    try {
        if (!vi.connect("127.0.0.1", 19997,100,10))
            throw std::runtime_error("Unable to connect to CoppeliaSim.");
        vi.set_synchronous(true);
        vi.start_simulation();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        //---------------Your code here----------------------------

        double time_simulation_step = 0.05;
        double y_0 = vi.get_object_pose("/Sphere").translation().vec3()[2];
        double y_sim;
        double y_est;
        double t;
        std::cout<<"-----------------"<<std::endl;
        std::cout<<"Initial height: "<<y_0<<std::endl;
        std::cout<<"-----------------"<<std::endl;

        for (int i=0; i<=5; i++)
        {
            t = i*time_simulation_step;
            y_sim = vi.get_object_pose("/Sphere").translation().vec3()[2];
            y_est = y_0 - 0.5 * 9.81 * std::pow(t, 2);
            vi.trigger_next_simulation_step();
            vi.wait_for_simulation_step_to_end();
        }
        std::cout<<"Elapsed time: "<<t<<std::endl;
        std::cout<<"Estimated height: "<<y_est<<", Measured height: "<<y_sim<<std::endl;
        vi.stop_simulation();
        vi.disconnect();
    } catch (std::exception& e) {
        std::cout<<e.what()<<std::endl;
        vi.stop_simulation();
        vi.disconnect();
    }
    return 0;
}