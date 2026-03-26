[METHOD: mutation_1f4b5589 | rotation=x2]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_DFL_UB_UF_UL_UR | cache_alg=false]
add_corner DFL
add_edge UB
add_edge UL
add_edge UF
add_edge UR
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_edge LD
add_corner DBL
add_corner DFR
add_corner DBR
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
[STEP: Step_GEN | cache_alg=false]
add_corners_orientation
add_edges_orientation
add_corners_orientation
add_corners_orientation
add_edges_orientation
[END GROUP]
[END METHOD]