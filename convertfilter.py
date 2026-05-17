import pandas as pd
import json

# Đọc Excel
df = pd.read_excel(r"D:\SOFTWARE\GIT HUB\pdf-dashboard\NXTIII.xlsx")

# Lấy nguyên cột TYPE (giữ nguyên dữ liệu)
types = df["TYPE"].tolist()

# Xuất JSON
with open("quickFilters.json", "w", encoding="utf-8") as f:
    json.dump(types, f, indent=4, ensure_ascii=False)

print("DONE")