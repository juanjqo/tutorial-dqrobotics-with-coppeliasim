.. _synchronous mode:

Minimal example: synchronous mode
*********************************


.. _synch: https://www.coppeliarobotics.com/helpFiles/en/remoteApiModusOperandi.htm
.. |synch| replace:: **synchronous mode**


.. admonition:: Goals
    :class: admonition-goal

    #. Understand the synchronous mode.
    #. Know the methods:

       * :file:`set_synchronous()`.
       * :file:`trigger_next_simulation_step()`.
       * :file:`wait_for_simulation_step_to_end()`.

Learn more in |synch|_.



Templates:
----------

The templates show how to establish communication with a CoppeliaSim scene in :file:`synchronous mode` (default mode) using the default :file:`port`. It's assumed that both the script and
the scene are running in the same computer (default :file:`IP`).

.. tab-set::

    .. tab-item:: Matlab


        :download:`template_synchronous.m </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.m>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.m
            :linenos:
            :language: python
            :lines: 1-
            :emphasize-lines: 11, 16,18


    .. tab-item:: Python


        :download:`template_synchronous.py </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.py>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.py
            :linenos:
            :language: python
            :lines: 1-
            :emphasize-lines: 11,15,17

    .. tab-item:: C++

        :download:`template_synchronous.cpp </_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.cpp>`

        .. literalinclude:: /_static/codes/get_started/coppeliasim_basics/communication/template_synchronous.cpp
            :linenos:
            :language: cpp
            :lines: 1-
            :emphasize-lines: 10,14,16



Free fall experiment
____________________

.. sidebar:: Hint

    .. image:: /_static/newton.png

    Use **try/catch** statements to handle different types of errors. If an exception is thrown, stop and close the communication
    in the catch statements.
