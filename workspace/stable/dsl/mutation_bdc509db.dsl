[METHOD: mutation_bdc509db | rotation=x2]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_edge BL
add_corner UBL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_BD_FD_LD_RD | cache_alg=true | free_layer=D]
add_edge BD
add_edge LD
add_edge FD
add_edge RD
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UB
add_edge UR
add_edge UL
[STEP: Step_DBL_DFR | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBL
[END METHOD]