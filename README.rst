CellBender Downstream Analysis
==============================
This repository contains standalone Python code for downstream analysis of CellBender output—without requiring the full CellBender environment.

The official CellBender downstream module (cellbender.remove_background.downstream) has strict dependency requirements (e.g., nbconvert < 7.0), which can conflict with some Python environments.
To avoid this issue, the key downstream functions have been extracted and packaged here for easier use.

Original CellBender Project

Full pipeline, documentation, and development can be found here:
https://github.com/broadinstitute/CellBender
