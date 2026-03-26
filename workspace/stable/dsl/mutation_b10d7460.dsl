[METHOD: mutation_b10d7460 | rotation=x2]
[STEP: Step_UF_UR | cache_alg=false]
add_edge UR
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_DBL_DBR | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DBL
[GROUP: F2L | order=best_1]
[STEP: Step_BR | cache_alg=false]
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[END METHOD]