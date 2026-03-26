[METHOD: mutation_e178cddf | rotation=x2]
[STEP: Step_GEN | cache_alg=false]
add_corners_orientation
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UR
add_edge UL
add_edge UB
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
add_corner UBL
add_edge BL
add_corners_orientation
[STEP: Step_FL_UFL | cache_alg=false]
add_corner UFL
add_edge FL
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_DBR | cache_alg=true | free_layer=D]
add_corner DBR
[END METHOD]