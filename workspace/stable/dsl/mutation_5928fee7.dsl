[METHOD: mutation_5928fee7 | rotation=x2]
[STEP: Step_DBL | cache_alg=false]
add_corner DBL
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_edge BR
add_corner UBR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_GEN | cache_alg=false]
add_corners_orientation
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edge FD
[STEP: Step_LD_UB_UF_UL_UR | cache_alg=false]
add_edge LD
add_edge UF
add_edge UB
add_edge UR
add_edge UL
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[END METHOD]