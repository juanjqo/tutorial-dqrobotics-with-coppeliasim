.. _synchronous mode:

Minimal example: synchronous mode
*********************************


.. _synch: https://www.coppeliarobotics.com/helpFiles/en/remoteApiModusOperandi.htm
.. |synch| replace:: **Legacy remote API modus operandi**


.. admonition:: Goals
    :class: admonition-goal

    #. Understand the synchronous mode.
    #. Know the methods:

       * :file:`set_synchronous()`.
       * :file:`trigger_next_simulation_step()`.
       * :file:`wait_for_simulation_step_to_end()`.


We learned previously the asynchronous mode, the default operation mode. In this section we are going to see the
synchronous mode (now called stepped mode).  In this mode, the simulation will take into account the progress of your script.
To enable it, you need to use :file:`set_synchronous(true)`.

Once enabled, the simulation will wait for a trigger to start computing the next simulation step. Such a trigger is sent by the
method :file:`trigger_next_simulation_step()`. To keep the synchrony, we need to ensure that the simulation step is finished before sending the next trigger.
This can be done by using the method :file:`wait_for_simulation_step_to_end()`.


.. admonition:: Recommendation
    :class: admonition-example

    Check |synch|_ to learn more about the synchronous mode.



Templates:
----------

The templates show how to establish communication with a CoppeliaSim scene in :file:`synchronous mode` using the default :file:`port`. It's assumed that both the script and
the scene are running in the same computer (default :file:`IP`).

.. tab-set::

    .. tab-item:: Matlab


        :download:`template_synchronous.m </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.m
            :linenos:
            :language: python
            :lines: 1-
            :emphasize-lines: 11, 15,16


    .. tab-item:: Python


        :download:`template_synchronous.py </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.py
            :linenos:
            :language: python
            :lines: 1-
            :emphasize-lines: 12,16,17

    .. tab-item:: C++

        :download:`template_synchronous.cpp </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.cpp
            :linenos:
            :language: cpp
            :lines: 1-
            :emphasize-lines: 11,15,16


    .. tab-item:: CMake

        .. admonition:: See also
            :class: admonition-git

            CMake examples for Ubuntu, Windows and MacOS https://github.com/dqrobotics/cpp-examples/blob/master/cmake/dqrobotics_dependencies.cmake

        .. code-block:: cmake
            :linenos:

            # Example CMAKE project for Ubuntu
            make_minimum_required(VERSION 3.5)

            project(template_synchronous)

            set(CMAKE_CXX_STANDARD 11)

            FIND_PACKAGE(Threads REQUIRED)
            FIND_PACKAGE(Eigen3 REQUIRED)
            INCLUDE_DIRECTORIES(${EIGEN3_INCLUDE_DIR})
            ADD_COMPILE_OPTIONS(-Werror=return-type
                                -Wall -Wextra -Wmissing-declarations
                                -Wredundant-decls -Woverloaded-virtual)

            add_executable(${PROJECT_NAME}
                           ${PROJECT_NAME}.cpp)

            target_link_libraries(${PROJECT_NAME}
                                  dqrobotics
                                  dqrobotics-interface-vrep
                                  Threads::Threads)





Free fall experiment
____________________

|

.. sidebar:: Hint

    .. image:: /_static/newton.png

    The expected height :math:`y(t)` of the red ball is computed as :math:`y(t) = y_{0} + v_{0}t + (1/2)gt^2`, where
    :math:`y_{0}`, :math:`v_{0}`, :math:`g`, :math:`t` are the initial height, the initial velocity, the gravity,
    and the elapsed simulation time, respectively.

It's time to test the synchronous mode! To do so, we are going to compare the height of the red ball (:file:`/Sphere`)
that is in free fall with the expected height after 0.25 s in the simulation time. The dynamics of the red ball is
handled by the engine and its behavior is affected by the simulation time step and the gravity.

In the DQ_Robotics_lab.ttt scene (see :ref:`example-scene`), the engine is Newton, the simulation time step is :file:`50ms` and the gravity
is :file:`-9,81`.  You can modify those parameters, but you'll need to update the examples as well.

.. note::

   As reported in https://github.com/dqrobotics/python/pull/51 the synchronous mode is working properly on Ubuntu
   (Matlab, Python and C++) and on Windows (Matlab). Other combinations of OS and languages could not ensure the synchrony.

|


.. tab-set::

    .. tab-item:: Matlab


        :download:`free_fall_test.m </_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.m
            :linenos:
            :language: python
            :lines: 1-


    .. tab-item:: Python


        :download:`free_fall_test.py </_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.py
            :linenos:
            :language: python
            :lines: 1-

    .. tab-item:: C++

        :download:`free_fall_test.cpp </_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/free_fall_test.cpp
            :linenos:
            :language: cpp
            :lines: 1-


|

You will have the following output:

.. grid::

    .. grid-item-card::

        | ---------------------------------
        | Initial height: 1
        | ---------------------------------
        | Elapsed time: 0.25
        | Estimated height: 0.69344 Measured height: 0.68731


.. admonition:: See also
    :class: admonition-git

    Synchronous test https://github.com/dqrobotics/python-examples/tree/master/vrep_interface_tests/synchronous_test