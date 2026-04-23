"""
features.py — Feature engineering on top of method_vector.

Any transforms, normalization, or derived features needed before
feeding method vectors into a model live here.

"""

import numpy as np

# Must stay in sync with METHOD_FIELDNAMES in data_generation.py.
# Drop 'method_name' (identifier) and 'score' (label), everything else is a feature
# FEATURE_COLS = [
#     "num_steps",
#     "num_groups",
#     "num_removes",
#    # "total_constraints", getting rid of for now as its just a sum of num edge corner and orientation constraints
#     "avg_constraints_per_step",
#     "max_constraints_per_step",
#     "num_cache_alg_steps",
#     "num_free_layer_steps",
#     "symmetry_depth",
#     "num_symmetry_orientations",
#     "num_edge_constraints",
#     "num_corner_constraints",
#     "num_orientation_constraints",
#     "constraint_type_diversity",
# ]
FEATURE_COLS = [
    "num_steps",
    "num_groups",
    "num_removes",
    "total_constraints",
    "avg_constraints_per_step",
    "min_constraints_per_step",
    "max_constraints_per_step",
    "constraints_per_step_range",
    "constraints_per_step_std",
    "step_entropy",
    "num_cache_alg_steps",
    "num_free_layer_steps",
    "symmetry_depth",
    "num_symmetry_orientations",
    "total_step_face_overlap_score",
    "avg_step_face_overlap_score",
    "min_step_face_overlap_score",
    "max_step_face_overlap_score",
    "step_face_overlap_score_range",
    "step_face_overlap_score_std",
    "num_zero_face_overlap_steps",
    "fraction_zero_face_overlap_steps",
    "avg_distinct_faces_per_step",
    "min_distinct_faces_per_step",
    "max_distinct_faces_per_step",
    "num_edge_only_steps",
    "num_corner_only_steps",
    "num_mixed_piece_type_steps",
    "fraction_mixed_piece_type_steps",
    "avg_adjacent_step_face_overlap",
    "max_adjacent_step_face_overlap",
]


 # extract a feature vector from methods.csv dict row
def extract_from_row(row: dict) -> np.ndarray:
    feature_values = []

    # Loop over each feature column defined above
    for col in FEATURE_COLS:
        # Get the value from the row dictionary
        value = row[col]
    
        # Convert the value to a float
        numeric_value = float(value)
    
        # Add the value to feature list
        feature_values.append(numeric_value)

    # Convert the list of numeric values into a numpy array
    feature_vector = np.array(feature_values, dtype=np.float64)

    # Return the resulting feature vector
    return feature_vector

# extract a feature vector directly from a method object
def extract_from_method(method) -> np.ndarray:
    # Import here to avoid circular imports at module load time
    from generation.data_generation import method_vector
 
    vec = method_vector(method)
    return np.array([float(vec[col]) for col in FEATURE_COLS], dtype=np.float64)
