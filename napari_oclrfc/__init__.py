try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.3.1"




from ._function import napari_experimental_provide_function
