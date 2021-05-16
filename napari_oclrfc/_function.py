from typing import TYPE_CHECKING

from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation

if TYPE_CHECKING:
    import napari


@napari_hook_implementation
def napari_experimental_provide_function():
    return [train, predict]

import oclrfc


class FeatureSets(Enum):
    small = "original gaussian_blur=1 sobel_of_gaussian_blur=1 top_hat_box=5"
    medium = "gaussian_blur=5 sobel_of_gaussian_blur=5 top_hat_box=25"
    large = "gaussian_blur=25 sobel_of_gaussian_blur=25 top_hat_box=50"

def train(
        image: "napari.types.ImageData",
        annotation : "napari.types.LabelsData",
        model_filename : str = "temp.cl",
        featureset : FeatureSets = FeatureSets.small,
        max_depth : int = 2,
        num_ensembles : int = 10
) -> "napari.types.LabelsData":
    feature_stack = featureset.value

    clf = oclrfc.OCLRandomForestClassifier(opencl_filename=model_filename, num_ensembles=num_ensembles, max_depth=max_depth)
    clf.train(feature_stack, annotation, image)

    result = clf.predict(feature_stack, image)
    return result

def predict(image: "napari.types.ImageData",
        model_filename : str = "temp.cl") -> "napari.types.LabelsData":

    clf = oclrfc.OCLRandomForestClassifier(opencl_filename=model_filename)
    result = clf.predict(image=image)
    return result
