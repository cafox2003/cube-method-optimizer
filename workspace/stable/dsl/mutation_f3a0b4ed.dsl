[METHOD: mutation_f3a0b4ed | rotation=x2]
[STEP: Step_UF | cache_alg=false]
add_edge UF
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_UFR | cache_alg=false]
add_corner UFR
add_corner UFR
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_DBL_DBR | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DBR
[END METHOD]