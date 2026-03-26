[METHOD: mutation_4fa59121 | rotation=x2]
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
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_GEN | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
[STEP: Step_DBL_DBR_DFR | cache_alg=true | free_layer=D]
add_corner DBL
add_corner DFR
add_corner DBR
[STEP: Step_BD_LD | cache_alg=true | free_layer=D]
add_edge LD
add_edge BD
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_edge FD
add_edge RD
[STEP: Step_UF_UR | cache_alg=false]
add_edge UF
add_edge UR
[END METHOD]