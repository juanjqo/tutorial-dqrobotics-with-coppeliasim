Hello world
***********
.. _more-info: https://dqroboticsgithubio.readthedocs.io/en/latest/installation/python.html
.. |more-info| replace:: **DQ Robotics documentation**


.. _more-info2: https://www.coppeliarobotics.com/helpFiles/en/accessingSceneObjects.htm
.. |more-info2| replace:: **Accessing scene objects programmatically**


.. _synch: https://www.coppeliarobotics.com/helpFiles/en/remoteApiModusOperandi.htm
.. |synch| replace:: **synchronous mode**


.. _tutorial: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |tutorial| replace:: **tutorial**


It is time to run your first example! The goal is to get the position of the object :file:`Frame_x`, which is located in the position :file:`[-1,0,0]`
in the DQ_Robotics_lab.ttt scene.

.. warning::
   MacOS users could require additional steps to run a simulation.

   #. Add :file:`simRemoteApi.start(19997)` to the main script of the scene.
   #. Start the simulation.
   #. Run your script.

   Check the |more-info|_ for more details.


Open the DQ_Robotics_lab.ttt scene (see :ref:`download-scene`).

.. image:: /_static/basics/frame_x_sc.png
    :align: center

|



.. sidebar:: Hint

    .. image:: /_static/Tips.png

    Use **try/catch** statements to handle different types of errors. If an exception is thrown, stop and close the communication
    in the catch statements.

To get the pose (position and orientation) of an object we need to use the method :file:`get_object_pose()` of the class
:file:`DQ_VrepInterface()`.

Roughly speaking, you need to do the following steps:

#. Define an object of the :file:`DQ_VrepInterface()` class.
#. Establish the connection to an specific IP and port. If you are running both the script and the simulation
   in the same computer, the default IP is :file:`127.0.0.1`. The default port is :file:`19997`.
#. Start the simulation.
#. Get the object pose.
#. Stop the simulation.
#. Disconnect.

|

Templates: asynchronous mode
----------------------------

The following templates are minimal scripts containing good practices for Matlab, Python, and C++. Those are based
on hundreds of feedbacks provided by the Maintainers of the DQ Robotics.

The templates show how to establish communication with a CoppeliaSim scene using the default :file:`port`. It's assumed that both the script and
the scene are running in the same computer (default :file:`IP`). Furthermore, the :file:`asynchronous mode` (default mode) is used.
This latter means that the simulation on CoppeliaSim will advance without taking into account the progress of your script. Learn more in |synch|_.

.. image:: /_static/basics/default_mode.png


.. tab-set::

    .. tab-item:: Matlab


        :download:`template.m </_static/codes/get_started/coppeliasim_basics/communication/template.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template.m
            :linenos:
            :language: python
            :lines: 1-


    .. tab-item:: Python


        :download:`template.py </_static/codes/get_started/coppeliasim_basics/communication/template.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template.py
            :linenos:
            :language: python
            :lines: 1-

    .. tab-item:: C++

        :download:`template.cpp </_static/codes/get_started/coppeliasim_basics/communication/template.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template.cpp
            :emphasize-lines: 12
            :linenos:
            :language: cpp
            :lines: 1-



.. hint::
    From CoppeliaSim V4.3.0 and up, objects can be accessed with object names (deprecated) and
    object paths (recommended). See more in |more-info2|_.

    |

    For instance: the deprecated name of the object :file:`Frame_x`
    is :file:`Frame_x` and its path corresponds to :file:`/Frame_x`.



.. warning::
    In case you use the object name, you are required to use the :file:`deprecated name`.
    The deprecated name does not always coincide with the object name displayed in the scene hierarchy.

    .. image:: /_static/basics/deprecated_name.png
        :align: center

Example
-------

.. tab-set::

    .. tab-item:: Matlab


        :download:`communication_test.m </_static/codes/get_started/coppeliasim_basics/communication/communication_test.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.m
            :emphasize-lines: 13
            :linenos:
            :language: python
            :lines: 1-


    .. tab-item:: Python


        :download:`communication_test.py </_static/codes/get_started/coppeliasim_basics/communication/communication_test.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.py
            :emphasize-lines: 13
            :linenos:
            :language: python
            :lines: 1-

    .. tab-item:: C++

        :download:`communication_test.cpp </_static/codes/get_started/coppeliasim_basics/communication/communication_test.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.cpp
            :emphasize-lines: 12
            :linenos:
            :language: cpp
            :lines: 1-


You will have the following output:

.. grid::

    .. grid-item-card::

        | Position:   - 1i
        | The test was successful!


|

.. raw:: html

    <video width="100%" height="auto" autoplay muted loop playsInline> <source
     src="../../_static/videos/hello_world_test.mp4"
     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
     Your browser does not support the video tag.  </video>

.. seealso::
    You can run the script and the simulation on different computers that are on the same local network.
    To do so, in :file:`connect()` use the IP of the computer that is running the simulation. For instance, lets say
    that your simulation is running on a PC with the IP address :file:`10.198.113.159`. Then,
    in the example, you must replace :file:`127.0.0.1` by :file:`10.198.113.159`.

    .. tab-set::

        .. tab-item:: Matlab

            .. code-block:: python

                vi.connect('10.198.113.159', 19997);

        .. tab-item:: Python

            .. code-block:: python

                vi.connect("10.198.113.159", 19997, 100, 10)

        .. tab-item:: C++

           .. code-block:: python

                vi.connect("10.198.113.159", 19997,100,10);




    .. image:: /_static/basics/requirements.png
        :align: left