[METHOD: mutation_cd870389 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_DBL | cache_alg=true | free_layer=D]
add_corner DBL
[STEP: Step_RD_UL_UR | cache_alg=true | free_layer=D]
add_edge UR
add_edge UL
add_edge RD
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_FD | cache_alg=true | free_layer=D]
add_edge FD
[END METHOD]