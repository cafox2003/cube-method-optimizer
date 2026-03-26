[METHOD: mutation_f1b43b11 | rotation=x2]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[GROUP: F2L | order=best_1]
[STEP: Step_BR_LD_UBR | cache_alg=false]
add_corner UBR
add_edge BR
add_edge LD
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
add_edges_orientation
add_corners_orientation
[END GROUP]
[STEP: Step_DBL_UB_UF | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
add_corner DBL
add_edge UB
add_edge UF
[END METHOD]