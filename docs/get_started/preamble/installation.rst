=============
Installation
=============

.. admonition:: YouTube
    :class: dropdown admonition-youtube

    ..  youtube:: e8ajS3FVMUI

.. admonition:: A sidebar admonition!
    :class: sidebar note

    Some sidebar content.

.. admonition:: Custom title!

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.



#. `DQ Robotics <https://dqrobotics.github.io/>`_

.. tab-set::

    .. tab-item:: Matlab


        #. Using `git <https://git-scm.com/>`_ commands:

         .. code-block:: python

               cd ~
               git clone https://github.com/dqrobotics/matlab.git

         .. image:: /_static/basics/install_matlab_using_powershell.gif
            :align: center

        #. Set the path in Matlab

         .. image:: /_static/basics/set_path.gif
            :align: center    

        |
        
        Alternatively, you can download the zip file: 

        Go to the `repository <https://github.com/dqrobotics/matlab.git>`_ clik on :bdg-success:`<> Code`, and clik on :bdg-primary-line:`Download ZIP`.

         .. image:: /_static/basics/install_matlab_zip.png
           :align: center       

        Unzip the :bdg-secondary:`matlab-master.zip` file and add it to the Path in Matlab.








    .. tab-item:: Python

         .. code-block:: python

            from dqrobotics import *
            from dqrobotics.interfaces.vrep  import DQ_VrepInterface
            from dqrobotics.robot_control import ControlObjective
            from dqrobotics.robot_control import DQ_PseudoinverseController
            from dqrobotics.robots import FrankaEmikaPandaRobot
            import time

            vi = DQ_VrepInterface()

            try:
                vi.connect(19997, 100, 10)
                vi.set_synchronous(True)
                vi.start_simulation()
                time.sleep(0.1)

                jointnames = ("Franka_joint1", "Franka_joint2",
                              "Franka_joint3", "Franka_joint4",
                              "Franka_joint5", "Franka_joint6",
                              "Franka_joint7")

                robot = FrankaEmikaPandaRobot.kinematics()
                controller = DQ_PseudoinverseController(robot)
                controller.set_gain(0.5)
                controller.set_damping(0.01)
                controller.set_control_objective(ControlObjective.Translation)
                controller.set_stability_threshold(0.00001)
                pd = vec4(0.2 * i_ + 0.3 * j_ + 0.3 * k_)

                while not controller.system_reached_stable_region():
                    q = vi.get_joint_positions(jointnames)
                    u = controller.compute_setpoint_control_signal(q, pd)
                    vi.set_joint_target_velocities(jointnames, u)
                    vi.trigger_next_simulation_step()

                vi.stop_simulation()
                vi.disconnect()

            except Exception as exp:
                print(exp)
                vi.disconnect_all()

    .. tab-item:: C++

       C++

       

