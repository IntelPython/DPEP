.. _parallelism:
.. include:: ./ext_links.txt

Parallelism in modern data parallel architectures
=================================================

Python is loved for its productivity and interactivity. But when it comes to dealing with
computationally heavy codes Python performance cannot be compromised. Intel and Python numerical
computing communities, such as `NumFOCUS <https://numfocus.org/>`_, dedicated attention to
optimizing core numerical and data science packages for leveraging parallelism available in modern CPUs:

* **Multiple computational cores:** Several computational cores allow processing data concurrently.
  Compared to a single core CPU, *N* cores can process either *N* times bigger data in a fixed time, or
  reduce a computation time *N* times for a fixed amount of data.

.. image:: ./_images/dpep-cores.png
    :width: 600px
    :align: center
    :alt: Multiple CPU Cores

* **SIMD parallelism:** SIMD (Single Instruction Multiple Data) is a special type of instructions
  that perform operations on vectors of data elements at the same time. The size of vectors is called SIMD width.
  If SIMD width is *K* then a SIMD instruction can process *K* data elements in parallel.

  In the following diagram the SIMD width is 2, which means that a single instruction processes two elements simultaneously.
  Compared to regular instructions that process one element at a time, 2-wide SIMD instruction performs
  2 times more data in fixed time, or, respectively, process a fixed amount of data 2 times faster.

.. image:: ./_images/dpep-simd.png
    :width: 150px
    :align: center
    :alt: SIMD

* **Instruction-Level Parallelism:** Modern CISC architectures, such as x86, allow performing data independent
  instructions in parallel. In the following example, we compute :math:`a * b + (c - d)`.
  Operations :math:`*` and :math:`-` can be executed in parallel, the last instruction
  :math:`+` depends on availability of :math:`a * b` and :math:`c - d` and hence cannot be executed in parallel
  with :math:`*` and :math:`-`.

.. image:: ./_images/dpep-ilp.png
    :width: 150px
    :align: center
    :alt: SIMD

