import json
import os
from pathlib import Path

def add_name_to_hero_files():
    # Define the directory path
    heroes_dir = Path("table-data/heroes")
    
    # Check if directory exists
    if not heroes_dir.exists():
        print(f"Directory {heroes_dir} does not exist!")
        return
    
    # Loop through all JSON files in the directory
    for json_file in heroes_dir.glob("*.json"):
        try:
            # Get the filename without extension as the name
            hero_name = json_file.stem
            
            # Read the JSON file
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Check if 'infos' key exists
            if 'infos' in data:
                # Create a new ordered dictionary with 'name' first
                new_infos = {"name": hero_name}
                # Add all existing infos data
                new_infos.update(data['infos'])
                # Replace the infos section
                data['infos'] = new_infos
                
                # Write back to the file with proper formatting
                with open(json_file, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                
                print(f"✓ Updated {json_file.name}")
            else:
                print(f"⚠ Skipped {json_file.name} - no 'infos' section found")
                
        except json.JSONDecodeError as e:
            print(f"✗ Error parsing {json_file.name}: {e}")
        except Exception as e:
            print(f"✗ Error processing {json_file.name}: {e}")
    
    print("Processing complete!")

if __name__ == "__main__":
    add_name_to_hero_files()