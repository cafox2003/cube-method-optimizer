[METHOD: mutation_dc7cce4a | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_GEN | cache_alg=false]
add_edges_orientation
add_corners_orientation
add_corners_orientation
add_edges_orientation
[END GROUP]
[STEP: Step_DBL | cache_alg=false]
add_corner DBL
add_edges_orientation
add_corners_orientation
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UL
add_edge UB
add_edge UR
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[END METHOD]