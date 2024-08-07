========
Topic B2
========

.. raw:: html

    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Consider these important definitions that apply to all following explanations.

The quaternion set is given by

:math:`\mathbb{H}\triangleq\left\{ h_{1}+\imi h_{2}+\imj h_{3}+\imk h_{4}\,:\,h_{1},h_{2},h_{3},h_{4}\in\mathbb{R}\right\}`

in which the imaginary units :math:`\imi`, :math:`\imj`, and :math:`\imk` have the following properties:

:math:`\hat{\imath}^{2}=\hat{\jmath}^{2}=\hat{k}^{2}=\hat{\imath}\hat{\jmath}\hat{k}=-1`

The dual quaternion set is given by

:math:`\mathcal{H}\triangleq\left\{ \quat h+\dual\quat h'\,:\,\quat h,\quat h'\in\mathbb{H},\,\dual^{2}=0,\,\dual\neq0\right\}`

where :math:`\dual^2=0` but :math:`\dual\neq0`.


.. math::

    \begin{aligned}
    V_{source} &= i\times R_{source} \\
    V_{output} &= -i\times R_{feedback} \\
    \frac{V_{source}}{V_{output}} &= -\frac{R_{source}}{R_{feedback}}\\
    V_{output} &= -V_{source}\frac{R_{feedback}}{R_{source}}
    \end{aligned}
