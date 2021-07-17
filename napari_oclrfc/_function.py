from oclrfc import PredefinedFeatureSet
from typing import TYPE_CHECKING

import numpy as np
from napari_plugin_engine import napari_hook_implementation

if TYPE_CHECKING:
    import napari


@napari_hook_implementation
def napari_experimental_provide_function():
    return [train_pixel_classifier, predict_pixel_classifier, connected_component_labeling, train_label_classifier, predict_label_classifier]

import oclrfc

def train_pixel_classifier(
        image: "napari.types.ImageData",
        annotation : "napari.types.LabelsData",
        model_filename : str = "pixel_classifier.cl",
        featureset : PredefinedFeatureSet = PredefinedFeatureSet.small_quick,
        custom_features : str = "original gaussian_blur=1 sobel_of_gaussian_blur=1",
        max_depth : int = 2,
        num_ensembles : int = 10
) -> "napari.types.LabelsData":
    feature_stack = featureset.value
    if feature_stack == "":
        feature_stack = custom_features

    clf = oclrfc.OCLRandomForestClassifier(opencl_filename=model_filename, num_ensembles=num_ensembles, max_depth=max_depth)
    clf.train(feature_stack, annotation, image)

    result = clf.predict(feature_stack, image)
    return result

def predict_pixel_classifier(image: "napari.types.ImageData",
                             model_filename : str = "pixel_classifier.cl") -> "napari.types.LabelsData":

    clf = oclrfc.OCLRandomForestClassifier(opencl_filename=model_filename)
    result = clf.predict(image=image)
    return result

def connected_component_labeling(labels: "napari.types.LabelsData", object_class_identifier : int = 2, fill_gaps_between_labels:bool = True) -> "napari.types.LabelsData":
    import pyclesperanto_prototype as cle
    binary = cle.equal_constant(labels, constant=object_class_identifier)
    if fill_gaps_between_labels:
        instances = cle.voronoi_labeling(binary)
    else:
        instances = cle.connected_components_labeling_box(binary)
    return instances


def train_label_classifier(image: "napari.types.ImageData",
        labels : "napari.types.LabelsData",
        annotation : "napari.types.LabelsData",
        model_filename : str = "label_classifier.cl",
        max_depth : int = 2,
        num_ensembles : int = 10,
        area : bool = True,
        min_intensity: bool = False,
        mean_intensity: bool = False,
        max_intensity: bool = False,
        sum_intensity: bool = False,
        standard_deviation_intensity: bool = False,
        shape: bool = False,
        position:bool = False,
        touching_neighbor_count:bool = False,
        average_distance_of_touching_neighbors:bool = False,
        distance_to_nearest_neighbor:bool = False,
        average_distance_to_6_nearest_neighbors:bool = False,
        average_distance_to_10_nearest_neighbors:bool = False,
    ) -> "napari.types.LabelsData":

    features = ","
    if area:
        features = features + "area,"
    if min_intensity:
        features = features + "min_intensity,"
    if mean_intensity:
        features = features + "mean_intensity,"
    if max_intensity:
        features = features + "max_intensity,"
    if sum_intensity:
        features = features + "sum_intensity,"
    if standard_deviation_intensity:
        features = features + "standard_deviation_intensity,"
    if shape:
        features = features + "mean_max_distance_to_centroid_ratio,"
    if position:
        features = features + "centroid_x,centroid_y,centroid_z,"
    if touching_neighbor_count:
        features = features + "touching_neighbor_count,"
    if average_distance_of_touching_neighbors:
        features = features + "average_distance_of_touching_neighbors,"
    if distance_to_nearest_neighbor:
        features = features + "average_distance_of_n_nearest_neighbors=1,"
    if average_distance_to_6_nearest_neighbors:
        features = features + "average_distance_of_n_nearest_neighbors=6,"
    if average_distance_to_10_nearest_neighbors:
        features = features + "average_distance_of_n_nearest_neighbors=10,"

    features = features[1:-1]

    clf = oclrfc.OCLRandomForestLabelClassifier(opencl_filename=model_filename, num_ensembles=num_ensembles,
                                           max_depth=max_depth)

    clf.train(features, labels, annotation, image)
    result = clf.predict(labels, image)
    return result

def predict_label_classifier(image: "napari.types.ImageData",
                             labels: "napari.types.LabelsData",

                             model_filename : str = "label_classifier.cl") -> "napari.types.LabelsData":

    clf = oclrfc.OCLRandomForestLabelClassifier(opencl_filename=model_filename)
    result = clf.predict(labels, image)
    return result
