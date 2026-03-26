[METHOD: mutation_713453b0 | rotation=x2]
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_edge LD
add_corner DBR
add_corner DBL
add_corner DFR
add_edge BD
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UB
add_edge UR
add_edge UL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_GEN | cache_alg=false]
add_edges_orientation
add_edges_orientation
add_corners_orientation
add_corners_orientation
add_corners_orientation
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_RD | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
add_edges_orientation
add_corners_orientation
add_edge RD
[END METHOD]