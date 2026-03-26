[METHOD: mutation_d0180789 | rotation=x2]
[GROUP: F2L | order=best_1]
[STEP: Step_BR_UBR | cache_alg=false]
add_corner UBR
add_edge BR
add_corner UBR
add_edge BR
[STEP: Step_BL_UBL | cache_alg=false]
add_corner UBL
add_edge BL
[STEP: Step_FD_FL_RD_UFL | cache_alg=false]
add_corner UFL
add_edge FL
add_edge RD
add_edge FD
[STEP: Step_FR_UFR | cache_alg=false]
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_BD | cache_alg=true | free_layer=D]
add_edge BD
add_corners_orientation
add_edges_orientation
[STEP: Step_DFR | cache_alg=true | free_layer=D]
add_corner DFR
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UB
add_edge UL
add_edge UR
[END METHOD]