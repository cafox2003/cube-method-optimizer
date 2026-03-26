[METHOD: mutation_348fee23 | rotation=x2]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_DBL_DBR | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DBL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_DFL_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UB
add_edge UF
add_edge UL
add_corner DFL
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[END METHOD]