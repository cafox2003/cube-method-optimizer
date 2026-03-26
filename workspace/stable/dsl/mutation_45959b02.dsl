[METHOD: mutation_45959b02 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UB
add_edge UR
add_edge UF
add_edge UL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
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
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_DBL_DBR_DFL_DFR_RD | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DFL
add_corner DBR
add_edge RD
add_corner DBL
[END METHOD]