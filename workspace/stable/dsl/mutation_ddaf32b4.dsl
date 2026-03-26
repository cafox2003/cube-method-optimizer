[METHOD: mutation_ddaf32b4 | rotation=x2]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_UB_UBL_UF_UL_UR | cache_alg=false]
add_edge UL
add_edge UF
add_corner UBL
add_edge UB
add_edge UR
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_GEN | cache_alg=false]
add_corners_orientation
add_edges_orientation
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_edge BD
add_corner DBR
add_corner DFR
add_corner DBL
add_edge LD
[END METHOD]