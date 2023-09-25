Communication test
******************

.. _more-info: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |more-info| replace:: **DQ Robotics documentation**

The goal is to get the position of the object :file:`Frame_x`, which is located in the position :file:`[-1,0,0]`
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

Run the example in you favorite language

.. tab-set::

    .. tab-item:: Matlab


        :download:`communication_test.m </_static/codes/get_started/coppeliasim_basics/communication/communication_test.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.m
            :linenos:
            :language: python
            :lines: 1-


    .. tab-item:: Python


        :download:`communication_test.py </_static/codes/get_started/coppeliasim_basics/communication/communication_test.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.py
            :linenos:
            :language: python
            :lines: 1-

    .. tab-item:: C++

        :download:`communication_test.cpp </_static/codes/get_started/coppeliasim_basics/communication/communication_test.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/communication_test.cpp
            :linenos:
            :language: cpp
            :lines: 1-


You will have the following output:

.. grid::

    .. grid-item-card::

        | Position:   - 1i
        | The test was successful!
