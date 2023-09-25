Hello world
***********
.. _more-info: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |more-info| replace:: **DQ Robotics documentation**


.. _more-info2: https://www.coppeliarobotics.com/helpFiles/en/accessingSceneObjects.htm
.. |more-info2| replace:: **Accessing scene objects programmatically**

It is time to run your first example! The goal is to get the position of the object :file:`Frame_x`, which is located in the position :file:`[-1,0,0]`
in the DQ_Robotics_lab.ttt scene.

.. warning::
   MacOS users could require additional steps to run a simulation.

   #. add :file:`simRemoteApi.start(19997)` to the main script of the scene
   #. start the simulation.
   #. run your script.

   Check the |more-info|_ for more details.


Open the DQ_Robotics_lab.ttt scene (see :ref:`download-scene`).

.. image:: /_static/basics/frame_x_sc.png
    :align: center

|



.. sidebar:: Hint

    .. image:: /_static/Tips.png

    Use try/catch statements to handle different types of errors. If an exception is thrown, stop and close the communication
    in the catch statements.

To get the pose (position and orientation) of an object we need to use the method :file:`get_object_pose("OBJECT_PATH")` of the class
:file:`DQ_VrepInterface()`.

Roughly speaking, you need to do the following steps:

#. define an object of the :file:`DQ_VrepInterface()` class.
#. establish the connection to an specific IP and port. If you are running both the script and the simulation
   in the same computer, the default IP is :file:`127.0.0.1`. The default port is :file:`19997`.
#. start the simulation.
#. get the object pose.
#. stop the simulation.
#. disconnect.

|

Templates
---------

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
    In case you use the object name, you are required to use de :file:`deprecated name`.
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