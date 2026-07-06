import pandas as pd
import json

# Đọc Excel
df = pd.read_excel(
    r"D:\SOFTWARE\GIT HUB\pdf-dashboard\FILTER.xlsx"
)

# ===== NXTII =====

nxt2 = (
    df["NXT II"]
    .dropna()
    .tolist()
)

with open(
    "NXT II.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nxt2,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== GPX-CSII =====

gpxcs2 = (
    df["GPX-CSII"]
    .dropna()
    .tolist()
)

with open(
    "GPX-CSII.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        gpxcs2,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== GPX-CS =====

gpxcs = (
    df["GPX-CS"]
    .dropna()
    .tolist()
)

with open(
    "GPX-CS.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        gpxcs,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== GPX-CL =====

gpxcl = (
    df["GPX-CL"]
    .dropna()
    .tolist()
)

with open(
    "GPX-CL.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        gpxcl,
        f,
        indent=4,
        ensure_ascii=False
    )
    
# ===== GPX-CII =====

gpxc2 = (
    df["GPX-CII"]
    .dropna()
    .tolist()
)

with open(
    "GPX-CII.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        gpxc2,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== Flexa =====

flexa = (
    df["Flexa"]
    .dropna()
    .tolist()
)

with open(
    "Flexa.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        flexa,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== Fujitrax =====

fujitrax = (
    df["Fujitrax"]
    .dropna()
    .tolist()
)

with open(
    "Fujitrax.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        fujitrax,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== Unit =====

unit = (
    df["Unit"]
    .dropna()
    .tolist()
)

with open(
    "Unit.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        unit,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== NXTR =====

nxtr = (
    df["NXTR"]
    .dropna()
    .tolist()
)

with open(
    "NXTR.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nxtr,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== GPX =====

gpx = (
    df["GPX"]
    .dropna()
    .tolist()
)

with open(
    "GPX.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        gpx,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== Feeder =====

feeder = (
    df["Feeder"]
    .dropna()
    .tolist()
)

with open(
    "Feeder.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        feeder,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== AIMEXIII =====

aimex3 = (
    df["AIMEXIII"]
    .dropna()
    .tolist()
)

with open(
    "AIMEXIII.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        aimex3,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== Nexim =====

nexim = (
    df["Nexim"]
    .dropna()
    .tolist()
)

with open(
    "Nexim.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nexim,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== NXTIII =====

nxt3 = (
    df["NXTIII"]
    .dropna()
    .tolist()
)

with open(
    "NXTIII.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nxt3,
        f,
        indent=4,
        ensure_ascii=False
    )

# ===== KNOWLEDGE =====

nxt3 = (
    df["KNOWLEDGE"]
    .dropna()
    .tolist()
)

with open(
    "KNOWLEDGE.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        nxt3,
        f,
        indent=4,
        ensure_ascii=False
    )

print("DONE")