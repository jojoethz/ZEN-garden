from zen_garden import Results, compare_model_values, compare_configs

r1 = Results(path=r'C:\Users\joell\Documents\ETH\Master\master_thesis\ZEN-garden\outputs\Europe_calibrated')
r2 = Results(path=r'C:\Users\joell\Documents\ETH\Master\master_thesis\ZEN-garden\outputs\Europe_calibrated_with_Updated_EVs')

compare_parameters = compare_model_values([r1, r2], component_type = 'parameter')
compare_variables = compare_model_values([r1, r2], component_type = 'variable')
compare_config = compare_configs([r1, r2])

import os
import json

def print_capex_specific_conversion(dataset_path):
    """
    Scans the dataset directory to find all technologies with 
    capex_specific_conversion defined in their attributes.
    """
    tech_base_dir = os.path.join(dataset_path, "set_technologies")
    
    if not os.path.exists(tech_base_dir):
        print(f"[Error] Directory not found: {tech_base_dir}")
        return

    print(f"\n{'Technology Name':<35} | {'Raw CAPEX Definition'}")
    print("-" * 100)
    
    found_any = False

    # Walk through all subdirectories in set_technologies
    for root, dirs, files in os.walk(tech_base_dir):
        if "attributes.json" in files:
            file_path = os.path.join(root, "attributes.json")
            tech_name = os.path.basename(root)
            
            try:
                with open(file_path, 'r') as f:
                    attrs = json.load(f)
                    
                # Look specifically for the CAPEX parameter
                if "capex_specific_conversion" in attrs:
                    raw_val = attrs["capex_specific_conversion"]
                    
                    # Strictly filter out genuine emptiness
                    if raw_val in [None, "", {}, "null"]:
                        continue
                        
                    # Print the absolute raw JSON representation to catch CSVs or dicts
                    print(f"{tech_name:<35} | {json.dumps(raw_val)}")
                    found_any = True
                    
            except (json.JSONDecodeError, IOError) as e:
                print(f"[Warning] Could not read file for {tech_name}: {e}")
                continue

    if not found_any:
        print("Confirmed: No CAPEX data defined in any attributes.json file.")
    print("-" * 100 + "\n")


# # --- Example Usage ---
# DATASET_PATH = r'C:\Users\joell\Documents\ETH\Master\master_thesis\ZEN-garden\Europe_calibrated_with_Updated_EVs' 
# print_capex_specific_conversion(DATASET_PATH)