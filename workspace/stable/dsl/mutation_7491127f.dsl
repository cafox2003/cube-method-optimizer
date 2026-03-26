[METHOD: mutation_7491127f | rotation=x2]
[STEP: Step_UL_UR | cache_alg=false]
add_edge UL
add_edge UR
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBR
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
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
[END METHOD]