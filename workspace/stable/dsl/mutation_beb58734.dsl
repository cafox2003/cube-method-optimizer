[METHOD: mutation_beb58734 | rotation=x2]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
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
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_UB_UL | cache_alg=false]
add_edge UL
add_edge UB
[STEP: Step_LD | cache_alg=true | free_layer=D]
add_edge LD
[STEP: Step_DBL_DBR | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DBL
add_corner DBL
add_corners_orientation
add_edges_orientation
[END METHOD]