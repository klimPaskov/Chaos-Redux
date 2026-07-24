from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
GFX = ROOT / "interface/012_africa_priority_member_assets.gfx"
OUT = ROOT / "docs/assets/012_africa_priority_member_idea_icons/validation/path_resolution.json"
text = GFX.read_text(encoding="utf-8-sig")
paths = re.findall(r'texturefile = "(gfx/interface/ideas/012_africa/priority_members/idea_africa_priority_[^"]+\.dds)"', text)
rows = [{"texture_path": path, "exists": (ROOT / path).exists()} for path in paths]
payload = {"registered_idea_paths": len(rows), "all_resolve": all(row["exists"] for row in rows), "rows": rows}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"registered_idea_paths": len(rows), "all_resolve": payload["all_resolve"]}))
