[METHOD: mutation_cf3a1482 | rotation=x2]
[STEP: Step_UB_UL_UR | cache_alg=false]
add_edge UR
add_edge UL
add_edge UB
add_edge UB
add_edge UL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edges_orientation
add_corners_orientation
add_edge RD
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_edge BD
add_corner DBL
add_edge LD
add_corner DBR
add_corner DFR
[END METHOD]