[METHOD: mutation_fd584942 | rotation=x2]
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DBR
add_corner DFR
add_edge BD
add_edge LD
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UL
add_edge UF
add_edge UB
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_GEN | cache_alg=false]
add_edges_orientation
add_edges_orientation
add_corners_orientation
add_corners_orientation
add_corners_orientation
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_RD | cache_alg=true | free_layer=D]
add_edge RD
add_corners_orientation
add_edges_orientation
add_edges_orientation
add_corners_orientation
[END METHOD]