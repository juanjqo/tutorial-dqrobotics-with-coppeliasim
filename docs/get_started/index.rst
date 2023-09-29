.. _get-started:

Get started
***********

.. _juanjqo: https://juanjqo.github.io/
.. |juanjqo| replace:: **Juan José Quiroz Omaña**

.. _dqrobotics: https://dqrobotics.github.io/
.. |dqrobotics| replace:: **DQ Robotics**

.. _book: https://hal.science/hal-01478225v1
.. |book| replace:: **book**

.. _dq: https://hal.science/hal-01478225v1
.. |dq| replace:: **Dual Quaternions**

.. note::
   This tutorial is focused on |dqrobotics|_ for Matlab (master branch). However, some hints for Python and C++ are also included.


**About this tutorial**

This tutorial is brought to you by |juanjqo|_. The examples are implemented mainly on Ubuntu 20.04 64bits and
Windows 11 using Matlab 2023a, and CoppeliaSim 4.5.1.

The capybara's  drawings were designed by Camila Quiroz.

.. warning::
    This tutorial assumes that you know the basic concepts about dual quaternions and the basic operations in Matlab.
    If this is not your case, we recommend checking this |book|_ and taking this **course**:
    https://github.com/dqrobotics/learning-dqrobotics-in-matlab before this tutorial.

.. admonition:: Disclaimer
   :class: admonition-disclaimer

   The videos shown in this tutorial (and **this tutorial itself**) must be used as a **reference**. You could see different behaviors in your
   implementations due to software updates, versions, operating systems, etc.


**About** |dq|_

Dual quaternions can be seen as an extension of complex numbers.

.. raw:: html

    <video width="100%" height="auto" autoplay muted loop playsInline> <source
     src="../_static/videos/dqrobotics_animation.mp4"
     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
     Your browser does not support the video tag.  </video>


**About** |dqrobotics|_

DQ Robotics is a standalone open-source and multiplatform library for robot modelling and control based on
dual quaternion algebra.

.. admonition:: YouTube: DQ Robotics
    :class: admonition-youtube

    ..  youtube:: e8ajS3FVMUI




Contents
--------

#. :doc:`Preamble <preamble/index>`
    Install DQ Robotics and CoppeliaSim.

    * :doc:`Installation <preamble/installation>`
    * :doc:`One scene to rule them all <preamble/example_scene>`

#. :doc:`Fundamentals on CoppeliaSim <coppeliasim_basics/index>`
    Some basic topics about CoppeliaSim

#. :doc:`Static world <kinematic_world/index>`
    Some topics on non-dynamic scenes

#. :doc:`Dynamic world <dynamic_world/index>`
    Some topics on dynamic scenes





.. toctree::
   :hidden:

   preamble/index
   coppeliasim_basics/index
   kinematic_world/index
   dynamic_world/index





