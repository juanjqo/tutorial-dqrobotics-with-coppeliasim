=============
Installation
=============

.. _more-info: https://dqroboticsgithubio.readthedocs.io/en/latest/installation/python.html
.. |more-info| replace:: **DQ Robotics documentation**

.. _tutorial: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python.html
.. |tutorial| replace:: **tutorial**

.. _environment: https://ros2-tutorial.readthedocs.io/en/latest/preamble/python/installing_python.html#isolate-your-environment-with-a-venv
.. |environment| replace:: **environment**


.. _sudo: https://ros2-tutorial.readthedocs.io/en/latest/preamble/ubuntu.html
.. |sudo| replace:: **Ubuntu Terminal Basics**

.. _repository: https://github.com/dqrobotics/matlab.git
.. |repository| replace:: **repository**


.. _pycharm: https://www.jetbrains.com/pycharm/
.. |pycharm| replace:: **PyCharm**


.. |ubuntu| image:: https://img.shields.io/badge/official%20support-Ubuntu%20LTS-orange

.. |windows| image:: https://img.shields.io/badge/partial%20support-Windows%20&%20macOS-blue

.. |python| image:: https://img.shields.io/pypi/pyversions/dqrobotics/21.4.0a75



.. _link: https://www.coppeliarobotics.com/
.. |link| replace:: **link**


CoppeliaSim
-----------

Download and install CoppeliaSim EDU from this |link|_.


On Ubuntu, you only need to extract the downloaded file. For instance, if you use Ubuntu 22.04,
the file would seem to something like :file:`CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu22_04.tar.xz`. To extract it, you
can use the graphic interface or the terminal. The latter can be done as follows:

.. admonition:: Learn more about the terminal in Ubuntu
    :class: admonition-example

    https://ros2-tutorial.readthedocs.io/en/latest/preamble/ubuntu.html

Open a new terminal (:kbd:`CTRL+ALT+T`) and type

.. code-block:: python

    cd ~/Downloads/
    tar -xf CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu22_04.tar.xz

Finally, you can open CoppeliaSim:

.. code-block:: python

    ~/Downloads/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu20_04/coppeliaSim.sh


.. hint::
   You can create an alias to CoppeliaSim. For instance:

   Run this (**Do this only once**):

   .. code-block:: python

        echo "alias coppeliasim='~/Downloads/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu20_04/coppeliaSim.sh &'" >> ~/.bashrc
        source ~/.bashrc


   Now, you can type :file:`coppeliasim` in your terminal to open CoppeliaSim!



.. note::
   The DQ Robotics library uses the legacy remote API, which is available for Windows 64bits,
   Ubuntu 64bits :file:`{` 16.04, 18.04, 20.04, 22.04 :file:`}` and MacOS 12 64bits (intel processors).

.. warning::
   For MacOS and Matlab users: Apple Silicon macs have the option to download CoppeliaSim :file:`x86_64` and :file:`arm64`.
   However, the latter does not work with the legacy remote API.

.. warning::
   MacOS users could require additional steps to run a simulation.

   #. Add :file:`simRemoteApi.start(19997)` to the main script of the scene.
   #. Start the simulation.
   #. Run your script.

   Check the |more-info|_ for more details.

.. raw:: html

    <video width="100%" height="auto" autoplay muted loop playsInline> <source
     src="../../_static/videos/coppeliaSim.mp4"
     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
     Your browser does not support the video tag.  </video>



DQ Robotics
-----------

.. tab-set::

    .. tab-item:: Matlab

        .. warning::
           DQ Robotics for Matlab is distributed as a LGPLV3 licensed package. Matlab, however, is not free software and other third-party toolboxes may also not be free.

        .. note::
           The installation for Matlab has four steps:
            #. Download the DQ Robotics.
            #. Add the DQ Robotics to the path in Matlab.
            #. Add the :file:`matlab folder` located in your CoppeliaSim to the path in Matlab.
            #. Add the :file:`remoteApi` located in CoppeliaSim to the path in Matlab. The :file:`remoteApi`

        Clone the repository (you can use `Github Desktop <https://desktop.github.com/>`_ or `git commands <https://git-scm.com/>`_ ). Alternatively,
        you can download the zip file.

        .. tab-set::

            .. tab-item:: git

                .. code-block:: python

                       cd ~
                       git clone https://github.com/dqrobotics/matlab.git

                Set the path in Matlab. Example:

                .. raw:: html

                    <video width="100%" height="auto" autoplay muted loop playsInline> <source
                     src="../../_static/videos/add_path_windows.mp4"
                     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
                     Your browser does not support the video tag.  </video>

            .. tab-item:: zip file

                    Download the zip file (Only if you did not clone the repository)


                    Go to the |repository|_ clik on :bdg-success:`<> Code`, and clik on :bdg-primary-line:`Download ZIP`.

                    .. image:: /_static/basics/install_matlab_zip.png
                       :align: center


                    Unzip the :bdg-secondary:`matlab-master.zip` file and add it to the Path in Matlab.



        |


        Add to the path both the :file:`matlab folder` and the :file:`remoteApi`. Usually, they are located in



        .. tab-set::

            .. tab-item:: Ubuntu x64

                .. code-block:: python

                    YOUR_COPPELIASIM_PATH/programming/legacyRemoteApi/remoteApiBindings/lib/lib/YOUR_UBUNTU_VERSION

                .. code-block:: python

                    YOUR_COPPELIASIM_PATH/programming/legacyRemoteApi/remoteApiBindings/matlab/matlab

                .. raw:: html

                    <video width="100%" height="auto" autoplay muted loop playsInline> <source
                     src="../../_static/videos/add_path_remote_api_ubuntu.mp4"
                     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
                     Your browser does not support the video tag.  </video>

            .. tab-item:: Windows x64

                .. code-block:: python

                    C:/Program Files/CoppeliaRobotics/CoppeliaSimEdu/programming/legacyRemoteApi/remoteApiBindings/lib/lib/Windows

                .. code-block:: python

                    C:/Program Files/CoppeliaRobotics/CoppeliaSimEdu/programming/legacyRemoteApi/remoteApiBindings/matlab/matlab

                .. raw:: html

                    <video width="100%" height="auto" autoplay muted loop playsInline> <source
                     src="../../_static/videos/add_path_remote_api.mp4"
                     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
                     Your browser does not support the video tag.  </video>



    .. tab-item:: Python

            |ubuntu| |windows| |python|

            .. tip::
               If you are unfamiliar with Python, check this |tutorial|_
               before installing the library.

            .. danger::
               You could break your system or create annoying conflicts by using :file:`sudo` to install Python packages.
               Check |sudo|_ to learn more.

            .. tip::
               It is a good practice to isolate your Python |environment|_ (i.e., using :file:`venv` to create virtual environments).


            Open a terminal and run (using a virtual environment hopefully):

            .. code-block:: python

                python3 -m pip install --user --pre dqrobotics


            .. hint::

                |pycharm| is an excellent multiplatform software to manage your Python scripts and your Python |environment|_.
                The Community Edition is free and open source.

            Check this video using Pycharm to install DQ Robotics in a virtual environment:


            .. raw:: html

                    <video width="100%" height="auto" autoplay muted loop playsInline> <source
                     src="../../_static/videos/pycharm.mp4"
                     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
                     Your browser does not support the video tag.  </video>


    .. tab-item:: C++

            |ubuntu|

            .. warning::
                The C++ version is recommended only for experienced users.

            Open a terminal and run:

            .. code-block:: python

                sudo add-apt-repository ppa:dqrobotics-dev/development
                sudo apt-get update
                sudo apt-get install libdqrobotics libdqrobotics-interface-vrep
       

