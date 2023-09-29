Enabling ports
**************

CoppeliaSim has the port :file:`19997` enabled by default to start the remote API server. However, you can enable
more ports according to your requirements. The ports are defined in :file:`remoteApiConnections.txt`, which is located
in your CoppeliaSim installation.

This is the default content of file :file:`remoteApiConnections.txt`:

.. code-block:: python
    :emphasize-lines: 12,13,14
    :linenos:

    // This file defines all the continuous remote API server services (started at remote API plugin initialization, i.e. CoppeliaSim start-up)
    //
    // Each remote API server service requires following 3 entries:
    //
    // portIndex@_port = xxxx               // where xxxx is the desired port number (below 19997 are preferred for server services starting at CoppeliaSim start-up)
    // portIndex@_debug = xxxx              // where xxxx is true or false
    // portIndex@_syncSimTrigger = xxxx     // where xxxx is true or false. When true, then the service will be pre-enabled for synchronous operation.
    //
    // In above strings, @ can be any number starting with 1. If more than one server service is required, then numbers need to be consecutive and starting with 1

    // Let's start a continuous remote API server service on port 19997:
    portIndex1_port             = 19997
    portIndex1_debug            = false
    portIndex1_syncSimTrigger   = true

The definition of a new port requires three entries, namely :file:`portIndex1_port`, :file:`portIndex1_debug`,
and :file:`portIndex1_syncSimTrigger`. (Check the definition of the port :file:`19997` in lines :file:`12-14`).

For instance, to enable another port, let says, port :file:`19998`, we need to add the following entries in

:file:`remoteApiConnections.txt`:

.. code-block:: python

    portIndex2_port             = 19998
    portIndex2_debug            = false
    portIndex2_syncSimTrigger   = true

The final :file:`remoteApiConnections.txt`:

.. code-block:: python
    :emphasize-lines: 15,16,17

    // This file defines all the continuous remote API server services (started at remote API plugin initialization, i.e. CoppeliaSim start-up)
    //
    // Each remote API server service requires following 3 entries:
    //
    // portIndex@_port = xxxx               // where xxxx is the desired port number (below 19997 are preferred for server services starting at CoppeliaSim start-up)
    // portIndex@_debug = xxxx              // where xxxx is true or false
    // portIndex@_syncSimTrigger = xxxx     // where xxxx is true or false. When true, then the service will be pre-enabled for synchronous operation.
    //
    // In above strings, @ can be any number starting with 1. If more than one server service is required, then numbers need to be consecutive and starting with 1

    // Let's start a continuous remote API server service on port 19997:
    portIndex1_port             = 19997
    portIndex1_debug            = false
    portIndex1_syncSimTrigger   = true
    portIndex2_port             = 19998
    portIndex2_debug            = false
    portIndex2_syncSimTrigger   = true


.. admonition:: See also
    :class: admonition-git

    Enabling ports 20010, 20011, 20012, 20013, and 20020. https://github.com/AISciencePlatform/aisp_coppeliasim_scenes





