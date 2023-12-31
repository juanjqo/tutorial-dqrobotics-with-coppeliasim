Knowing the user interface
**************************


.. admonition:: Goals
    :class: admonition-goal

    #. Get familiar with CoppeliaSim.
    #. Know the elements that compose the user interface.

.. image:: /_static/basics/GUI_edited.png
    :align: center



.. note::
    If you are using a high-resolution display and the user interface looks too small, you
    could fix it by setting the parameter :file:`highResDisplay=2` in the configuration file :file:`usrset.txt`.

    To know where the :file:`usrset.txt` is, you can type in the Lua commander the following:

    .. code-block:: python

        sim.getStringParam(sim.stringparam_usersettingsdir)