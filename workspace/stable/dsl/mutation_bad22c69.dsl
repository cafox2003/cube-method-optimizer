[METHOD: mutation_bad22c69 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_FR_UFL_UFR | cache_alg=false]
add_edge FL
add_corner UFL
add_edge FR
add_corner UFR
[STEP: Step_RD | cache_alg=false]
add_corners_orientation
add_edges_orientation
add_edges_orientation
add_corners_orientation
add_edge RD
[END GROUP]
[STEP: Step_UB_UF_UL | cache_alg=false]
add_edge UL
add_edge UF
add_edge UB
[STEP: Step_BD | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
add_edge BD
[STEP: Step_DFR | cache_alg=true | free_layer=D]
add_corner DFR
[END METHOD]