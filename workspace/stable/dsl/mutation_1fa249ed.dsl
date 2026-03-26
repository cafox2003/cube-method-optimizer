[METHOD: mutation_1fa249ed | rotation=x2]
[STEP: Step_UF | cache_alg=false]
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
add_corners_orientation
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBL
add_corner DBR
[STEP: Step_BD_LD | cache_alg=true | free_layer=D]
add_edge BD
add_edge LD
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR | cache_alg=false]
add_edge FR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[END METHOD]