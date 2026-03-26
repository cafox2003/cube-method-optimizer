[METHOD: mutation_580e5473 | rotation=x2]
[STEP: Step_UB_UF_UL_UR | cache_alg=false]
add_edge UF
add_edge UB
add_edge UR
add_edge UR
add_edge UL
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
add_corner UFR
add_edge FR
[END GROUP]
[STEP: Step_FD_RD | cache_alg=true | free_layer=D]
add_corners_orientation
add_edges_orientation
add_edge FD
add_edge RD
[STEP: Step_DBR | cache_alg=true | free_layer=D]
add_corner DBR
[END METHOD]