import json, os, re

data = json.load(open("/home/claude/dashboard/extracted.json"))
OUT = "/home/claude/jb"

FIELD_LABELS = {
    "education": "Neuroscience × Education",
    "economics": "Neuroscience × Economics",
    "policy-diplomacy-advocacy": "Neuroscience × Policy, Diplomacy & Advocacy",
    "physics": "Neuroscience × Physics",
    "mathematics": "Neuroscience × Mathematics",
    "biology-chemistry": "Neuroscience × Biology & Chemistry",
    "computer-science": "Neuroscience × Computer Science",
    "entrepreneurship": "Neuroscience × Entrepreneurship",
}

UNIT_ORDER = ["UNIT I", "UNIT II", "UNIT III", "UNIT IV", "UNIT V", "UNIT VI"]
UNIT_META = {
    "UNIT I":   ("Unit I — Learning Innovation Challenge", "Weeks 1–4",  "Innovation Proposal I", "Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter)."),
    "UNIT II":  ("Unit II — Research Investigation", "Weeks 5–8",  "Research Investigation / Prospectus", "Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory."),
    "UNIT III": ("Unit III — Public Communication & Social Impact", "Weeks 9–12", "Communication Product + Dissemination Plan", "Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory."),
    "UNIT IV":  ("Unit IV — Memory/Decision Systems Simulation", "Weeks 13–16", "Simulation Model IV", "Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory."),
    "UNIT V":   ("Unit V — Policy Formation Simulation", "Weeks 17–20", "Policy Draft Document", "Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory."),
    "UNIT VI":  ("Unit VI — Integration & Summit", "Weeks 21–24", "Capstone Project", "Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit."),
}

def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def steps_from_text(text):
    text = text.strip()
    chunks = re.split(r'(?=\*[A-Z][a-zA-Z /]+:\*)', text)
    steps = []
    for c in chunks:
        c = c.strip()
        if not c:
            continue
        label_m = re.match(r'\*([A-Z][a-zA-Z /]+):\*\s*(.*)', c, re.DOTALL)
        if label_m:
            label, rest = label_m.group(1), label_m.group(2).strip()
            steps.append(f"**{label}:** {rest}")
        else:
            steps.append(c)
    return steps

def project_page(field_key, p):
    label = FIELD_LABELS[field_key]
    L = []
    L.append(f"# {p['num']}. {p['title']}")
    L.append("")
    L.append(f"*{p['subtitle']}*")
    L.append("")
    L.append(f"**Field:** {label} &nbsp;·&nbsp; **Project ID:** `{field_key}/{p['slug']}`")
    L.append("")
    L.append("```{admonition} Big Question")
    L.append(":class: tip")
    L.append(p['big_question'])
    L.append("```")
    L.append("")
    L.append("```{admonition} Why This Matters")
    L.append(":class: note")
    L.append(p['why_matters'])
    L.append("```")
    L.append("")
    L.append("## Core Literature — Read This Before Starting Unit II")
    L.append("")
    L.append(p["literature"] if p["literature"] else "No specific literature block was detected — use the field's shared Core Concept Library.")
    L.append("")
    L.append("## Exact Steps, Unit by Unit")
    L.append("")
    L.append("Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.")
    L.append("")
    for uk in UNIT_ORDER:
        if uk not in p["units"]:
            continue
        meta_title, weeks, artifact, process_note = UNIT_META[uk]
        L.append(f"### {meta_title}")
        L.append(f"*{weeks} · Required artifact: **{artifact}***")
        L.append("")
        L.append(f"**Process for this unit (same for every project in the chapter):** {process_note}")
        L.append("")
        L.append("**Steps specific to this project:**")
        L.append("")
        for step in steps_from_text(p["units"][uk]):
            L.append(f"- [ ] {step}")
        L.append("")
    L.append("## Skills This Project Builds")
    L.append("")
    if p["skills_block"]:
        L.append("*Technical skills:*" + p["skills_block"])
    L.append("")
    L.append("## Why This Project Impresses")
    L.append("")
    L.append(p["why_impresses"])
    L.append("")
    L.append("## How the Six Outputs Link Into One Portfolio")
    L.append("")
    L.append(p["portfolio_note"])
    L.append("")
    return "\n".join(L)

def field_index(field_key, projects):
    label = FIELD_LABELS[field_key]
    L = [f"# {label}", "", "Ten complete project pathways for this field. Every pathway runs on the exact same six-unit process — only the topic and literature change.", ""]
    L.append("```{list-table}")
    L.append(":header-rows: 1")
    L.append("")
    L.append("* - #")
    L.append("  - Project")
    L.append("  - Big Question")
    for p in projects:
        bq = p["big_question"]
        if len(bq) > 110:
            bq = bq[:107] + "..."
        L.append(f"* - {p['num']}")
        L.append(f"  - {{doc}}`{p['slug']}`")
        L.append(f"  - {bq}")
    L.append("```")
    L.append("")
    return "\n".join(L)

toc_chapters = []
for field_key, projects in data.items():
    fdir = os.path.join(OUT, "fields", field_key)
    os.makedirs(fdir, exist_ok=True)
    with open(os.path.join(fdir, "index.md"), "w", encoding="utf-8") as f:
        f.write(field_index(field_key, projects))
    sections = []
    for p in projects:
        with open(os.path.join(fdir, f"{p['slug']}.md"), "w", encoding="utf-8") as f:
            f.write(project_page(field_key, p))
        sections.append(f"fields/{field_key}/{p['slug']}")
    toc_chapters.append((f"fields/{field_key}/index", sections))

with open(os.path.join(OUT, "toc_chapters.json"), "w") as f:
    json.dump(toc_chapters, f, indent=2)

print("done", len(toc_chapters))
