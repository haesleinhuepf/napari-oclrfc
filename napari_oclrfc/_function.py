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

def train(
        image: "napari.types.ImageData",
        annotation : "napari.types.LabelsData",
        model_filename : str = "temp.cl",
        max_depth : int = 2,
        num_trees : int = 100
) -> "napari.types.LabelsData":
    feature_stack = oclrfc.generate_feature_stack(image)

    num_features = len(feature_stack)
    num_classes = np.max(annotation)

    clf = oclrfc.OCLRandomForestClassifier(num_features, num_classes, opencl_filename=model_filename, num_trees=num_trees, max_depth=max_depth)
    clf.train(feature_stack, annotation)

    result = clf.predict_gpu(feature_stack)
    return result

def predict(image: "napari.types.ImageData",
        model_filename : str = "temp.cl") -> "napari.types.LabelsData":

    feature_stack = oclrfc.generate_feature_stack(image)

    clf = oclrfc.OCLRandomForestClassifier(0, 0, opencl_filename=model_filename)
    result = clf.predict_gpu(feature_stack)
    return result
