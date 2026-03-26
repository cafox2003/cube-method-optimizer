[METHOD: mutation_4601fca7 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UB
add_edge UF
add_edge UR
add_edge UL
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
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_edges_orientation
add_corners_orientation
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DBL
add_edge LD
add_edge BD
add_corner DFR
add_corner DBR
[END METHOD]