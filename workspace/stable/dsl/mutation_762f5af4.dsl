[METHOD: mutation_762f5af4 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UL
add_edge UB
add_edge UF
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[STEP: Step_DBL_DFR | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DFR
[STEP: Step_BD_LD | cache_alg=true | free_layer=D]
add_edge LD
add_edge BD
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
add_corner UBR
add_edge BR
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
[END METHOD]