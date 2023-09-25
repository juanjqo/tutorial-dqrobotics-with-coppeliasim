=============
Installation
=============

.. _tutorial: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |tutorial| replace:: **tutorial**

.. _environment: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python/installing_python.html#isolate-your-environment-with-a-venv
.. |environment| replace:: **environment**

.. _repository: https://github.com/dqrobotics/matlab.git
.. |repository| replace:: **repository**

.. tab-set::

    .. tab-item:: Matlab

        .. warning::
           DQ Robotics for Matlab is distributed as a LGPLV3 licensed package. Matlab, however, is not free software and other third-party toolboxes may also not be free.


        Clone the repository (you can use `Github Desktop <https://desktop.github.com/>`_ or `git commands <https://git-scm.com/>`_ ). If you do not want to clone
        the repository you can ignore this step and download the Zip file, as explained below.

        .. code-block:: python

               cd ~
               git clone https://github.com/dqrobotics/matlab.git

        .. image:: /_static/basics/install_matlab_using_powershell.gif
            :align: center

        Set the path in Matlab

        .. image:: /_static/basics/set_path.gif
            :align: center    

        |
        
        Download the zip file (Only if you did not clone the repository)


        Go to the |repository|_ clik on :bdg-success:`<> Code`, and clik on :bdg-primary-line:`Download ZIP`.

        .. image:: /_static/basics/install_matlab_zip.png
           :align: center

        |

        Unzip the :bdg-secondary:`matlab-master.zip` file and add it to the Path in Matlab.

        |

        Add to the path both the library and the remoteApi. Usually they are located in

        .. code-block:: python

            YOUR_INSTALLATION_PATH/CoppeliaRobotics/CoppeliaSimEdu/programming/legacyRemoteApi/remoteApiBindings/lib/lib/YOUR_PLATFORM

        .. code-block:: python

            YOUR_INSTALLATION_PATH/CoppeliaRobotics/CoppeliaSimEdu/programming/legacyRemoteApi/remoteApiBindings/matlab/matlab


        .. raw:: html

         <video width="100%" height="auto" autoplay muted loop playsInline> <source
           src="_static/videos/add_path_remote_api.mp4"
           type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
           Your browser does not support the video tag.  </video>



    .. tab-item:: Python

            .. tip::
               If you are unfamiliar with Python, check this |tutorial|_
               before installing the library.

            .. warning::
               It is a good practice to isolate your Python |environment|_.


            Open a terminal and run:

            .. code-block:: python

                python3 -m pip install --user --pre dqrobotics


    .. tab-item:: C++

            Open a terminal and run:

            .. code-block:: python

                sudo add-apt-repository ppa:dqrobotics-dev/development
                sudo apt-get update
                sudo apt-get install libdqrobotics libdqrobotics-interface-vrep
       

