import json
import pandas as pd

# Direct Google Sheet URL details
SPREADSHEET_ID = "1Zx3xxASAdaQ8dEJTq4dOa419hDqu5Czq00AU06MUx4Y"
GID = "1619855414"

csv_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&gid={GID}"

try:
    print("Kumokonekta sa Google Sheet...")
    df = pd.read_csv(csv_url)
    df = df.dropna(how="all").fillna("")

    json_data = df.to_dict(orient="records")

    # >>> DITO PAPALITAN: gawing 'rawdata.json' <<<
    output_filename = "rawdata.json"
    
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print(f"\n[SUCCESS] Na-download at na-convert na ang {len(json_data)} rows!")
    print(f"Na-save ang file bilang: {output_filename}")

except Exception as e:
    print(f"\n[ERROR] May naganap na mali: {e}")

input("\nPindutin ang ENTER para isara...")