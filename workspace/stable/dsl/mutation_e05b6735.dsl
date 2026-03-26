[METHOD: mutation_e05b6735 | rotation=x2]
[STEP: Step_BD | cache_alg=true | free_layer=D]
add_edge BD
[STEP: Step_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DBR
add_edge LD
add_corner DFR
add_corner DBL
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
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
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
add_edge FR
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_UF | cache_alg=false]
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[END METHOD]