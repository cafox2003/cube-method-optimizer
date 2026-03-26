[METHOD: mutation_66209a82 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
add_edges_orientation
add_corners_orientation
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_DBR_DFR_FD_RD | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DFR
add_edge FD
add_edge RD
[STEP: Step_UB_UF_UL | cache_alg=false]
add_edge UB
add_edge UL
add_edge UF
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[END METHOD]