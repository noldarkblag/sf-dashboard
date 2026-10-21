import json
import urllib.request
import pandas as pd
import io

SPREADSHEET_ID = "1Zx3xxASAdaQ8dEJTq4dOa419hDqu5Czq00AU06MUx4Y"
GID = "1619855414"

# Standard GViz CSV URL
csv_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&gid={GID}"

try:
    print("Kumokonekta sa Google Sheet...")
    
    # Nagdaragdag ng User-Agent para hindi i-block ng Google ang GitHub Runner
    req = urllib.request.Request(
        csv_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    with urllib.request.urlopen(req) as response:
        csv_data = response.read()

    # Basahin ang CSV data
    df = pd.read_csv(io.BytesIO(csv_data))
    df = df.dropna(how="all").fillna("")

    json_data = df.to_dict(orient="records")

    # I-save bilang rawdata.json
    output_filename = "rawdata.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print(f"\n[SUCCESS] Na-download at na-convert na ang {len(json_data)} rows!")

except Exception as e:
    print(f"\n[ERROR] May naganap na mali: {e}")
    raise e  # Sisiguraduhin nitong makikita sa logs ang eksaktong error kung mag-fail
