clear all;
close all;
clc;


include_namespace_dq;
vi = DQ_VrepInterface();

try
    vi.connect('127.0.0.1', 19997);
    vi.start_simulation();
    pause(0.1);
    x = vi.get_object_pose('/Frame_x');
    disp('Position: ')
    translation(x)
    disp('The test was succesful!')
    vi.stop_simulation();
    vi.disconnect();
catch ME
    vi.stop_simulation();
    vi.disconnect();
    rethrow(ME)
end