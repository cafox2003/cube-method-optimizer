[METHOD: mutation_c5ff72b9 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_BD_DFR | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
add_corner DFR
add_edge BD
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UL
add_edge UB
add_edge UF
add_edge UR
[END METHOD]