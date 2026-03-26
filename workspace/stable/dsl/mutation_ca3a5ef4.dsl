[METHOD: mutation_ca3a5ef4 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UB
add_edge UL
add_edge UR
add_edge UR
add_edge UF
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
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_RD | cache_alg=true | free_layer=D]
add_edge RD
[STEP: Step_FD | cache_alg=true | free_layer=D]
add_edge FD
add_corners_orientation
add_edges_orientation
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DBR
add_corner DFR
[END METHOD]