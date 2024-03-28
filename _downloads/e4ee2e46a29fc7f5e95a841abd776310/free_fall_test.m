clear all;
close all;
clc;



include_namespace_dq;
vi = DQ_VrepInterface();


try

    vi.connect('127.0.0.1', 19997);
    vi.set_synchronous(true);
    vi.start_simulation();
    pause(0.1);
    p0 = vec3(translation(vi.get_object_pose('/Sphere')));
    y0 = p0(3);
    time_simulation_step = 0.05;
    disp('---------------------------------')
    disp(['Initial height: ',num2str(y0)])
    disp('---------------------------------')

    for i=0:5
        t = i*time_simulation_step;
        p = vec3(translation(vi.get_object_pose('/Sphere')));
        y_sim = p(3);
        y_est = y0 - 0.5*9.81*t^2;
        vi.trigger_next_simulation_step();
        vi.wait_for_simulation_step_to_end();
    end
    disp(['Elapsed time: ',num2str(t)])
    disp(['Estimated height: ',num2str(y_est),' Measured height: ', num2str(y_sim)])
    vi.stop_simulation();
    vi.disconnect();

catch ME

    vi.stop_simulation();
    vi.disconnect();
    rethrow(ME)

end