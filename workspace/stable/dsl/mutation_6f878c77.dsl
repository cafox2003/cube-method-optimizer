[METHOD: mutation_6f878c77 | rotation=x2]
[STEP: Step_UR | cache_alg=false]
add_edge UR
[GROUP: F2L | order=best_1]
[STEP: Step_BR_FD_RD_UBR | cache_alg=false]
add_edge BR
add_corner UBR
add_edge FD
add_edge RD
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
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBR
add_corner DBL
add_corner DFR
[END METHOD]