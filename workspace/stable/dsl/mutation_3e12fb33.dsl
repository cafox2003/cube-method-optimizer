[METHOD: mutation_3e12fb33 | rotation=x2]
[STEP: Step_UF | cache_alg=false]
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBR
add_corner DBL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_UBL | cache_alg=false]
add_corner UBL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[END METHOD]