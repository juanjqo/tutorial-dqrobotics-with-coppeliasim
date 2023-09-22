=============
Installation
=============
.. _tutorial: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |tutorial| replace:: **tutorial**

.. _environment: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python/installing_python.html#isolate-your-environment-with-a-venv
.. |environment| replace:: **environment**

.. admonition:: YouTube
    :class: dropdown admonition-youtube

    ..  youtube:: e8ajS3FVMUI

.. admonition:: A sidebar admonition!
    :class: sidebar note

    Some sidebar content.

.. admonition:: Custom title!

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.



`DQ Robotics <https://dqrobotics.github.io/>`_

.. tab-set::

    .. tab-item:: Matlab

        Using `git <https://git-scm.com/>`_ commands:

         .. code-block:: python

               cd ~
               git clone https://github.com/dqrobotics/matlab.git

         .. image:: /_static/basics/install_matlab_using_powershell.gif
            :align: center

        Set the path in Matlab

         .. image:: /_static/basics/set_path.gif
            :align: center    

        |
        
        Alternatively, you can download the zip file: 

        Go to the `repository <https://github.com/dqrobotics/matlab.git>`_ clik on :bdg-success:`<> Code`, and clik on :bdg-primary-line:`Download ZIP`.

         .. image:: /_static/basics/install_matlab_zip.png
           :align: center       

        Unzip the :bdg-secondary:`matlab-master.zip` file and add it to the Path in Matlab.

        Add the following folders to the path









    .. tab-item:: Python



            Open a terminal and run:

            .. code-block:: python

                python3 -m pip install --user --pre dqrobotics




    .. tab-item:: C++

            Open a terminal and run:

            .. code-block:: python

                sudo add-apt-repository ppa:dqrobotics-dev/development
                sudo apt-get update
                sudo apt-get install libdqrobotics libdqrobotics-interface-vrep


