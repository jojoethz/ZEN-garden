from zen_garden import Results, compare_model_values, compare_configs

r1 = Results(path=r'C:\Users\joell\Documents\ETH\Master\master_thesis\ZEN-garden\outputs\Europe_but_better')
r2 = Results(path=r'C:\Users\joell\Documents\ETH\Master\master_thesis\ZEN-garden\outputs\Europe_but_better_joel')

compare_parameters = compare_model_values([r1, r2], component_type = 'parameter')
compare_variables = compare_model_values([r1, r2], component_type = 'variable')
compare_config = compare_configs([r1, r2])