[METHOD: mutation_60b4094f | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UL
add_edge UB
add_edge UR
[STEP: Step_DBR_DFR_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
add_corner DBR
add_corner DFR
[STEP: Step_BD | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
add_edges_orientation
add_corners_orientation
add_edge BD
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
add_edges_orientation
add_corners_orientation
[END GROUP]
[END METHOD]