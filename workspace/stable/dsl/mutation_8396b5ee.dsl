[METHOD: mutation_8396b5ee | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
add_edge BR
add_corner UBR
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
[STEP: Step_BD_DFR | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
add_edge BD
add_corner DFR
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UR
add_edge UL
add_edge UB
add_edge UF
[END METHOD]