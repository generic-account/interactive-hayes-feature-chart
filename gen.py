from pathlib import Path

TITLE = "Hayes Features"

FEATURES = [
    "consonantal",
    "sonorant",
    "continuant",
    "delayed release",
    "approximant",
    "tap",
    "trill",
    "nasal",
    "voice",
    "spread glottis",
    "constricted glottis",
    "labial",
    "round",
    "labiodental",
    "coronal",
    "anterior",
    "distributed",
    "strident",
    "lateral",
    "dorsal",
    "high",
    "low",
    "front",
    "back",
    "tense",
]

# First column in each major section
SECTION_STARTS = {0, 8, 11}  # manner, laryngeal, place
# First column in place subsections after labial
SUBSECTION_STARTS = {14, 19}  # coronal, dorsal

GROUP_HEADERS = [
    ("Manner features", 8),
    ("Laryngeal features", 3),
    ("Place features", 14),
]

ROWS = [
    {
        "label": "bilabial",
        "rows": [
            {
                "symbol": "p",
                "audio": "001",
                "values": ["+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "b",
                "audio": "002",
                "values": ["+", "-", "-", "-", "-", "-", "-", "-", "+", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "ɸ",
                "audio": "003",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "-", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "β",
                "audio": "004",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "+", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "m",
                "audio": "005",
                "values": ["+", "+", "-", "0", "-", "-", "-", "+", "+", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "ʙ",
                "audio": "006",
                "values": ["+", "+", "+", "0", "+", "-", "+", "-", "+", "-", "-", "+", "-", "-", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
        ],
    },
    {
        "label": "labiodental",
        "rows": [
            {
                "symbol": "pf",
                "audio": "007",
                "values": ["+", "-", "-", "+", "-", "-", "-", "-", "-", "-", "-", "+", "-", "+", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "f",
                "audio": "008",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "-", "-", "-", "+", "-", "+", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "v",
                "audio": "009",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "+", "-", "-", "+", "-", "+", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "ɱ",
                "audio": "010",
                "values": ["+", "+", "-", "0", "-", "-", "-", "+", "+", "-", "-", "+", "-", "+", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "ʋ",
                "audio": "011",
                "values": ["-", "+", "+", "0", "+", "-", "-", "-", "+", "-", "-", "+", "-", "+", "-", "0", "0", "0", "-", "-", "0", "0", "0", "0", "0"],
            },
        ],
    },
    {
        "label": "dental",
        "rows": [
            {
                "symbol": "t̪",
                "audio": "012",
                "values": ["+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "-", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "d̪",
                "audio": "013",
                "values": ["+", "-", "-", "-", "-", "-", "-", "-", "+", "-", "-", "-", "-", "-", "+", "+", "+", "-", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "θ",
                "audio": "014",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "-", "-", "-", "0", "0", "0", "0", "0"],
            },
            {
                "symbol": "ð",
                "audio": "015",
                "values": ["+", "-", "+", "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "-", "+", "+", "+", "-", "-", "-", "0", "0", "0", "0", "0"],
            },
        ],
    },
]

def feature_header_cell(name: str, i: int) -> str:
    classes = ["vertical"]
    if i in SECTION_STARTS:
        classes.append("section-start")
    elif i in SUBSECTION_STARTS:
        classes.append("subsection-start")
    cls = " ".join(classes)
    return f'      <th class="{cls}"><span>{name}</span></th>'

def value_cell(value: str, i: int) -> str:
    classes = []
    if i in SECTION_STARTS:
        classes.append("section-start")
    elif i in SUBSECTION_STARTS:
        classes.append("subsection-start")
    class_attr = f' class="{" ".join(classes)}"' if classes else ""
    return f"<td{class_attr}>{value}</td>"

def render_thead() -> str:
    top = [
        "    <tr>",
        '      <th colspan="2" class="corner"></th>',
    ]
    for label, span in GROUP_HEADERS:
        top.append(f'      <th colspan="{span}" class="group">{label}</th>')
    top.append("    </tr>")

    second = [
        "    <tr>",
        '      <th colspan="2" class="lefthead">Segment</th>',
    ]
    second.extend(feature_header_cell(name, i) for i, name in enumerate(FEATURES))
    second.append("    </tr>")

    return "\n".join(top + [""] + second)

def render_group(group: dict, start_index: int) -> tuple[str, int]:
    out = []
    rows = group["rows"]
    label = group["label"]

    for row_i, row in enumerate(rows):
        tr_class = ' class="group-start"' if row_i == 0 else ""
        out.append(f"    <tr{tr_class}>")

        if row_i == 0:
            out.append(f'      <th rowspan="{len(rows)}" class="row-group"><span>{label}</span></th>')

        out.append('      <th scope="row" class="segment">')
        out.append(
            f'        <button class="sound" data-audio="{{{{ \'/assets/audio/stub/{row["audio"]}.mp3\' | relative_url }}}}">{row["symbol"]}</button>'
        )
        out.append("      </th>")

        cells = [value_cell(v, i) for i, v in enumerate(row["values"])]
        out.append("      " + "".join(cells))
        out.append("    </tr>")

    return "\n".join(out), start_index + len(rows)

def validate() -> None:
    expected = len(FEATURES)
    for group in ROWS:
        for row in group["rows"]:
            actual = len(row["values"])
            if actual != expected:
                raise ValueError(
                    f'{group["label"]} / {row["symbol"]}: expected {expected} values, got {actual}'
                )

def render_page() -> str:
    validate()

    body_chunks = []
    idx = 1
    for group in ROWS:
        chunk, idx = render_group(group, idx)
        body_chunks.append(chunk)

    return f"""---
layout: default
title: {TITLE}
---

<h1>Hayes Consonant Features</h1>
<p>Prototype chart. Click a segment to play a stub audio file.</p>

<table class="hayes-chart">
  <thead>
{render_thead()}
  </thead>

  <tbody>
{chr(10).join(body_chunks)}
  </tbody>
</table>

<audio id="player"></audio>
<script src="{{{{ '/assets/js/hayes-features.js' | relative_url }}}}"></script>
"""

def main() -> None:
    html = render_page()
    Path("index.html").write_text(html, encoding="utf-8")
    print("Wrote index.html")

if __name__ == "__main__":
    main()