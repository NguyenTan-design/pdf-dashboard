import pandas as pd
import json

# Đọc Excel
df = pd.read_excel(r"C:\Users\quoct\OneDrive - Fuji Machine Asia Pte Ltd\DOCUMENT CONTROL.xlsx")

# Chỉ lấy các cột cần
df = df[["Category", "TYPE", "Release date", "Title", "LINK", "Document No"]]

# Format ngày
df["Release date"] = df["Release date"].dt.strftime("%m-%d-%Y")

# Convert JSON
data = json.loads(df.to_json(orient="records", force_ascii=False))
# Xuất JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("DONE")