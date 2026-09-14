#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 --version
if ! command -v uv >/dev/null 2>&1; then
  python3 -m pip install uv==0.12.11
fi
uv --version
python3 scripts/check_project.py
uv run _bmad/scripts/resolve_config.py --project-root . >/dev/null
printf '%s\n' 'Workstead development baseline ready. Product runtime not installed.'
