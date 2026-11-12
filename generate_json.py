import json
import pandas as pd

# Ilagay dito ang eksaktong filename o path ng Excel file mo
EXCEL_FILE = "data.xlsx" 

# Kung maraming tabs/sheets ang Excel mo, ilagay ang pangalan ng sheet. 
# Kung ang pinakaunang sheet lang ang babasahin, iwanang 0
SHEET_NAME = 0  # Halimbawa: "Sheet1" o 0 para sa first tab

try:
    print(f"Binabasa ang Excel file: {EXCEL_FILE}...")
    
    # Basahin ang Excel file
    df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    
    # Linisin ang mga blankong rows at cells
    df = df.dropna(how="all").fillna("")

    # I-convert sa list of dictionaries para maging valid JSON
    json_data = df.to_dict(orient="records")

    # I-save bilang rawdata.json
    output_filename = "rawdata.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False, default=str)

    print(f"\n[SUCCESS] Na-convert na ang {len(json_data)} rows papuntang {output_filename}!")

except FileNotFoundError:
    print(f"\n[ERROR] Hindi mahanap ang file na '{EXCEL_FILE}'. Siguraduhing nasa parehong folder ito ng script.")
except Exception as e:
    print(f"\n[ERROR] May naganap na mali: {e}")
    raise e
