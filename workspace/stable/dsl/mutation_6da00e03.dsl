[METHOD: mutation_6da00e03 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UF
add_edge UB
add_edge UL
[STEP: Step_RD | cache_alg=true | free_layer=D]
add_edge RD
[STEP: Step_DBL_DBR_DFR_FD | cache_alg=true | free_layer=D]
add_edge FD
add_corner DFR
add_corner DBL
add_corner DBR
[STEP: Step_BD_LD | cache_alg=true | free_layer=D]
add_edge LD
add_edge BD
[GROUP: F2L | order=best_1]
[STEP: Step_BR | cache_alg=false]
add_edge BR
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
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[END METHOD]