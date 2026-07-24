from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[4]
PROCESSED = ROOT / "docs/assets/012_africa_priority_member_post_settlement_decision_icons/processed_png"
RUNTIME = ROOT / "gfx/interface/decisions/012_africa/priority_members"
DECODED = ROOT / "docs/assets/012_africa_priority_member_post_settlement_decision_icons/validation/dds_decoded"
REPORT = ROOT / "docs/assets/012_africa_priority_member_post_settlement_decision_icons/validation/dds_validation.json"
DECODED.mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(path: Path) -> tuple[Image.Image, dict[str, object]]:
	data = path.read_bytes()
	if len(data) < 128 or data[:4] != b"DDS ":
		raise ValueError(f"{path}: invalid DDS magic or short header")
	words = struct.unpack_from("<31I", data, 4)
	header_size, flags, height, width, pitch, depth, mipmaps = words[:7]
	pf_size, pf_flags, fourcc, bits, r_mask, g_mask, b_mask, a_mask = words[18:26]
	caps = words[26]
	expected = 128 + width * height * 4
	checks = {
		"magic": data[:4].decode("ascii"),
		"header_size": header_size,
		"width": width,
		"height": height,
		"pitch": pitch,
		"mipmap_count": mipmaps,
		"pixel_format_size": pf_size,
		"pixel_format_flags": pf_flags,
		"fourcc": fourcc,
		"bits": bits,
		"masks": [r_mask, g_mask, b_mask, a_mask],
		"caps": caps,
		"file_length": len(data),
		"expected_length": expected,
	}
	checks["header_ok"] = header_size == 124 and pf_size == 32 and pf_flags == 65 and fourcc == 0 and bits == 32 and [r_mask, g_mask, b_mask, a_mask] == [0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000] and caps == 0x1000 and len(data) == expected and width == 32 and height == 32
	if not checks["header_ok"]:
		raise ValueError(f"{path}: malformed 32x32 legacy BGRA header: {checks}")
	pixels = bytearray(data[128:])
	for i in range(0, len(pixels), 4):
		pixels[i], pixels[i + 2] = pixels[i + 2], pixels[i]
	image = Image.frombytes("RGBA", (width, height), bytes(pixels))
	checks["alpha_min"], checks["alpha_max"] = image.getchannel("A").getextrema()
	return image, checks


records: list[dict[str, object]] = []
for dds in sorted(RUNTIME.glob("decision_012_africa_priority_member_post_settlement_*.dds")):
	processed = PROCESSED / f"{dds.stem}.png"
	image, checks = decode(dds)
	decoded_path = DECODED / f"{dds.stem}_decoded.png"
	image.save(decoded_path)
	processed_image = Image.open(processed).convert("RGBA")
	checks["decoded_pixel_equal_processed"] = image.tobytes() == processed_image.tobytes()
	checks["processed_sha256"] = sha256(processed)
	checks["dds_sha256"] = sha256(dds)
	checks["decoded_sha256"] = sha256(decoded_path)
	checks["final_path"] = str(dds.relative_to(ROOT)).replace("\\", "/")
	records.append(checks)

REPORT.write_text(json.dumps({"count": len(records), "assets": records}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"count": len(records), "all_header_ok": all(r["header_ok"] for r in records), "all_pixel_equal": all(r["decoded_pixel_equal_processed"] for r in records)}))
