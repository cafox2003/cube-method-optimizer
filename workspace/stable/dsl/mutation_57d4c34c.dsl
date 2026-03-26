[METHOD: mutation_57d4c34c | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UL
add_edge UF
add_edge UR
add_edge UB
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
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
add_edges_orientation
add_corners_orientation
add_edge RD
add_edge FD
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DBL
add_edge LD
add_corner DFR
add_edge BD
[END METHOD]