# napari-oclrfc

[![License](https://img.shields.io/pypi/l/napari-oclrfc.svg?color=green)](https://github.com/haesleinhuepf/napari-oclrfc/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-oclrfc.svg?color=green)](https://pypi.org/project/napari-oclrfc)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-oclrfc.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-oclrfc/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-oclrfc/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-oclrfc/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-oclrfc)

[cle](https://github.com/clEsperanto/pyclesperanto_prototype) meets [sklearn](https://scikit-learn.org/stable/)

OpenCL-based Random Forest Classifiers for pixel classification in [napari].

![](https://github.com/haesleinhuepf/napari-oclrfc/raw/master/images/screenshot.png)

For using OpenCL-based Random Forest Classifiers for pixel classification in python, check out [oclrfc](https://github.com/haesleinhuepf/oclrfc).


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `napari-oclrfc` via [pip]. Note: you also need [pyopencl](https://documen.tician.de/pyopencl/).

    conda install pyopencl
    pip install napari-oclrfc
    
In case of issues in napari, make sure these dependencies are installed properly:
    
    pip install pyclesperanto_prototype==0.9.0
    pip install oclrfc==0.1.1

## Contributing
 
Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-oclrfc" is free and open source software

## Issues

If you encounter any problems, please [open a thread on image.sc](https://image.sc) along with a detailed description and tag [@haesleinhuepf](https://github.com/haesleinhuepf).

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/haesleinhuepf/napari-oclrfc/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
