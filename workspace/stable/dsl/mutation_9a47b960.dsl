[METHOD: mutation_9a47b960 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FL_UFL | cache_alg=false]
add_edge FL
add_corner UFL
[STEP: Step_FR_UFR | cache_alg=false]
add_edge FR
add_corner UFR
[END GROUP]
[STEP: Step_BD_DBL_DBR_DFR_LD | cache_alg=true | free_layer=D]
add_corner DFR
add_corner DBR
add_corner DBL
add_edge LD
add_edge BD
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge RD
add_edges_orientation
add_corners_orientation
add_edge FD
[STEP: Step_UB_UR | cache_alg=false]
add_edge UB
add_edge UR
[END METHOD]