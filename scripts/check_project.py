"""Baseline validation only: does not test the agent platform."""
from pathlib import Path
import re
r = Path(__file__).resolve().parents[1]
required = ["AGENTS.md", "README.md", "docs/STATUS.md", "docs/START-HERE.md",
    "_bmad-output/planning-artifacts/prd.md", "docs/validation/qualification.md",
    "_bmad/_config/manifest.yaml", ".agents/skills/bmad-help/SKILL.md"]
errors = [f"Missing: {p}" for p in required if not (r / p).is_file()]
prd = (r / "_bmad-output/planning-artifacts/prd.md").read_text()
ids = re.findall(r"\| (REQ-\d{3}) \|", prd)
if len(ids) != len(set(ids)):
    errors.append("Duplicate requirement IDs")
qualification = (r / "docs/validation/qualification.md").read_text()
for ref in set(re.findall(r"REQ-\d{3}", qualification)):
    if ref not in ids:
        errors.append(f"Unknown requirement: {ref}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: baseline files, {len(ids)} unique requirements, qualification references. Product tests: NOT RUN.")
