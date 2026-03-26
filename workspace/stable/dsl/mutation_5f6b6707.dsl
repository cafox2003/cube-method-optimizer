[METHOD: mutation_5f6b6707 | rotation=x2]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[STEP: Step_DBL_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UL
add_corner DBL
add_edge UF
add_edge UB
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corners_orientation
add_edges_orientation
add_edge FR
add_corner UFR
[END GROUP]
[END METHOD]