[METHOD: mutation_c90ed9c4 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UB
add_edge UL
add_edge UF
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_LD | cache_alg=true | free_layer=D]
add_edge LD
[STEP: Step_BD_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DBR
add_corner DBL
add_corner DFR
add_edge BD
[END METHOD]