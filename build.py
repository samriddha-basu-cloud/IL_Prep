"""Bundle notes/*.md into assets/notes.js so the site works on Vercel and when index.html is opened directly.

Run after editing any note:  python3 build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
NOTES = ROOT / "notes"

# Sidebar order and short labels. Any new .md file not listed here is appended at the end.
ORDER = [
    # (slug, sidebar label, tag, group)
    ("README", "About these notes & syllabus", "", "start"),
    ("rapid-revision", "Rapid Revision", "★", "start"),
    ("p1-outsourcing-contract-problems", "Outsourcing & Contract Problems", "P1", "focus"),
    ("p2-incoterms-problems", "Incoterms Problems", "P2", "focus"),
    ("p3-container-imbalance-problems", "Container Imbalance Problems", "P3", "focus"),
    ("p4-insurance-general-average-problems", "Insurance & GA Problems", "P4", "focus"),
    ("p5-freight-costing-numericals", "Freight Costing Numericals", "P5", "focus"),
    ("p6-kpi-book-cases", "KPI Book Cases", "P6", "focus"),
    ("ch01-outsourcing-contracts", "Outsourcing & Contracts", "01", "chapters"),
    ("ch02-incoterms", "Incoterms® 2020", "02", "chapters"),
    ("ch03-containerization-container-imbalance", "Containerization & Imbalance", "03", "chapters"),
    ("ch04-maritime-logistics-costing", "Maritime & Logistics Costing", "04", "chapters"),
    ("ch05-air-freight-pricing-security", "Air Security & Cost", "05", "chapters"),
    ("ch06-marine-insurance-general-average", "Insurance & General Average", "06", "chapters"),
    ("ch07-air-transportation", "Air Transportation", "07", "chapters"),
    ("ch08-transportation-kpis-scorecards", "KPIs & Carrier Scorecards", "08", "chapters"),
    ("exam-questions-qna", "Exam Q&A Bank", "Q&A", "practice"),
    ("mcq-bank", "MCQ Bank", "MCQ", "practice"),
    ("glossary", "Glossary A–Z", "A–Z", "practice"),
]


def first_heading(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


def main() -> None:
    files = {p.stem: p for p in NOTES.glob("*.md")}
    entries = []
    for slug, label, tag, group in ORDER:
        if slug in files:
            md = files.pop(slug).read_text(encoding="utf-8")
            entries.append({"slug": slug, "label": label, "tag": tag, "group": group, "title": first_heading(md, label), "md": md})
    for slug, path in sorted(files.items()):
        md = path.read_text(encoding="utf-8")
        title = first_heading(md, slug)
        entries.append({"slug": slug, "label": title, "tag": "", "group": "practice", "title": title, "md": md})

    out = ROOT / "assets" / "notes.js"
    out.write_text("window.NOTES = " + json.dumps(entries, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {len(entries)} notes")


if __name__ == "__main__":
    main()
