[METHOD: mutation_094eeaf4 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UL
add_edge UR
add_edge UF
add_edge UB
[STEP: Step_BD_FD_RD | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
add_edge RD
add_edge FD
add_edge BD
[STEP: Step_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DBR
add_edge LD
add_corner DFR
add_corner DBL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
add_corners_orientation
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
add_edge FR
add_corner UFR
[END GROUP]
[END METHOD]