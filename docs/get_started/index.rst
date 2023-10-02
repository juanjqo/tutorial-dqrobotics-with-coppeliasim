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

.. warning::
    This tutorial assumes that you know the basic concepts about dual quaternions and the basic operations in Matlab.
    If this is not your case, we recommend checking this |book|_ and taking this **course**:
    https://github.com/dqrobotics/learning-dqrobotics-in-matlab before this tutorial.

.. admonition:: Disclaimer
   :class: admonition-disclaimer

   The videos shown in this tutorial (and **this tutorial itself**) must be used as a **reference**. You could see different behaviors in your
   implementations due to software updates, versions, operating systems, etc.

.. admonition:: Issues
   :class: admonition-bug

   If you find bugs/typos or have any issues, please let us know.
   https://github.com/juanjqo/tutorial-dqrobotics-with-coppeliasim/issues

**About this tutorial**

This tutorial is brought to you by |juanjqo|_. The examples are implemented mainly on Ubuntu 20.04 64bits and
Windows 11 using Matlab 2023a, and CoppeliaSim 4.5.1.

**Contributors**

|

**Acknowledgments**

* Camila Andrea Quiroz Omaña for the capybara's drawings.

|

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


|
|

.. rubric:: Recommended References

* **About** |dq|_


.. raw:: html

    <video width="100%" height="auto" autoplay muted loop playsInline> <source
     src="../_static/videos/dqrobotics_animation.mp4"
     type="video/mp4" style="margin-left: -220px; margin-right: -10.5%">
     Your browser does not support the video tag.  </video>


.. admonition:: YouTube: DQ Robotics
    :class: admonition-youtube

    ..  youtube:: e8ajS3FVMUI

.. [#] Adorno, B.V., 2017. Robot Kinematic Modeling and Control Based on Dual Quaternion Algebra---Part I: Fundamentals `(link) <https://hal.science/hal-01478225/>`_.
.. [#] Adorno, B.V., 2011. Two-arm manipulation: From manipulators to enhanced human-robot collaboration (Doctoral dissertation) `(link) <https://theses.hal.science/tel-00641678/>`_.
.. [#] Marinho, M.M., Adorno, B.V., Harada, K. and Mitsuishi, M., 2019. Dynamic active constraints for surgical robots using vector-field inequalities. IEEE Transactions on Robotics, 35(5), pp.1166-1185 `(link) <https://arxiv.org/pdf/1804.11270>`_.
.. [#] Adorno, B.V and Marinho, M.M., "DQ Robotics: A Library for Robot Modeling and Control," in IEEE Robotics & Automation Magazine, vol. 28, no. 3, pp. 102-116 `(link) <https://arxiv.org/abs/1910.11612>`_.



.. toctree::
   :hidden:

   preamble/index
   coppeliasim_basics/index
   kinematic_world/index
   dynamic_world/index





