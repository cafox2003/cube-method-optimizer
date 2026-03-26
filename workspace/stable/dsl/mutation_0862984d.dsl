[METHOD: mutation_0862984d | rotation=x2]
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DBR
add_corner DFR
[STEP: Step_BD_LD | cache_alg=true | free_layer=D]
add_edge LD
add_edge BD
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
add_edges_orientation
add_corners_orientation
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UB
add_edge UL
add_edge UF
add_edge UR
[END METHOD]