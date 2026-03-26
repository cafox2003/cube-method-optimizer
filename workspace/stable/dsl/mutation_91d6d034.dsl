[METHOD: mutation_91d6d034 | rotation=x2]
[STEP: Step_FD | cache_alg=false]
add_edge FD
add_corners_orientation
[STEP: Step_RD_UF | cache_alg=false]
add_edge UF
add_edge RD
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_edge BD
add_corner DBL
add_edge LD
add_corner DBR
add_corner DFR
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR | cache_alg=false]
add_edge FR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[END METHOD]