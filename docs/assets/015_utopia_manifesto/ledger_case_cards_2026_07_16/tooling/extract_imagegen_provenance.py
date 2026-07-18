#!/usr/bin/env python3
"""Freeze exact built-in ImageGen prompts and handles for this asset package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


SESSION_ID = "019f67b0-daff-7143-b03e-2b584ae8d3f7"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = next(
	candidate
	for candidate in (PACKAGE_ROOT, *PACKAGE_ROOT.parents)
	if (candidate / "AGENTS.md").is_file()
)
METADATA_DIR = PACKAGE_ROOT / "metadata"
PROMPTS_DIR = PACKAGE_ROOT / "prompts"
LEDGER_STYLE_REFERENCE = (
	"docs/assets/015_utopia_manifesto/processed_png/"
	"utopia_ledger_background_panel.png"
)
NO_TARGET_REFERENCE = (
	"docs/assets/015_utopia_manifesto/ledger_case_cards_2026_07_16/"
	"sources/utopia_ledger_case_no_target_source.png"
)

RECORDS = (
	{
		"state": "no_target",
		"handle": "exec-26d6909d-5171-4281-ac32-5da2501c366e",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_no_target_source.png",
		"references": [
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette and interface-family style"},
		],
	},
	{
		"state": "target_eligible",
		"handle": "exec-e5773e1b-bfe9-49a7-ab1e-10a219d8df98",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_target_eligible_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "target_selected",
		"handle": "exec-0a0e1d07-5b36-48c2-927b-ea7daa6f79b4",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_target_selected_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family style and proportions"},
		],
	},
	{
		"state": "offer_pending",
		"handle": "exec-cbb341f0-5f7d-424f-abaf-622f61d70556",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_offer_pending_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "counteroffer",
		"handle": "exec-de9b4b7c-f0ba-4498-81ad-2b2c3f3625e6",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_counteroffer_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "refusal",
		"handle": "exec-b8e5bfbd-cd59-4864-8408-fc007d5e8aad",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_refusal_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "ultimatum_available",
		"handle": "exec-6cf17e9c-5573-4ac2-a94c-c6f0e4ab358b",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_ultimatum_available_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family style and proportions"},
		],
	},
	{
		"state": "expired",
		"handle": "exec-9033b6dc-24fa-4a61-86c4-aaa15ada3227",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_expired_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "stewardship_active",
		"handle": "exec-5ba30e1c-4fc2-4426-b922-72dc57ed2776",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_stewardship_active_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "associate_established",
		"handle": "exec-e0ca3e48-125b-4f1c-b673-46dd18f2e50b",
		"status": "accepted",
		"workspace_source": "sources/utopia_ledger_case_associate_established_source.png",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "target_selected",
		"handle": "exec-eda0034a-0e35-4ee9-bab3-f7e7ec617d52",
		"status": "rejected",
		"workspace_source": "sources/rejected/utopia_ledger_case_target_selected_rejected_2_5197_source.png",
		"rejection_reason": "2.5197:1 post-matte aspect required a material vertical crop at 300x96",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "ultimatum_available",
		"handle": "exec-92568123-7993-4044-b10c-a9d8a4564078",
		"status": "rejected",
		"workspace_source": "sources/rejected/utopia_ledger_case_ultimatum_available_rejected_2_5006_source.png",
		"rejection_reason": "2.5006:1 post-matte aspect required a material vertical crop at 300x96",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family composition"},
			{"path": LEDGER_STYLE_REFERENCE, "role": "palette reference"},
		],
	},
	{
		"state": "target_selected",
		"handle": "exec-30745e31-dd3f-4eaf-a3ce-e00154a1dd83",
		"status": "rejected",
		"workspace_source": "sources/rejected/utopia_ledger_case_target_selected_retry_rejected_2_5006_source.png",
		"rejection_reason": "2.5006:1 retry still required a material vertical crop at 300x96",
		"references": [
			{"path": NO_TARGET_REFERENCE, "role": "accepted case-card family style and proportions"},
		],
	},
)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as stream:
		for chunk in iter(lambda: stream.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def find_session() -> Path:
	matches = list((Path.home() / ".codex" / "sessions").rglob(f"*{SESSION_ID}.jsonl"))
	if len(matches) != 1:
		raise RuntimeError(f"Expected one ImageGen session transcript, found {len(matches)}")
	return matches[0]


def load_prompts(session_path: Path) -> dict[str, dict[str, str]]:
	prompts: dict[str, dict[str, str]] = {}
	with session_path.open("r", encoding="utf-8") as stream:
		for line in stream:
			entry = json.loads(line)
			payload = entry.get("payload", {})
			if payload.get("type") != "image_generation_end":
				continue
			handle = payload.get("call_id")
			prompt = payload.get("revised_prompt")
			if handle and prompt:
				prompts[handle] = {
					"timestamp": entry.get("timestamp", ""),
					"prompt": prompt,
				}
	return prompts


def main() -> int:
	session_path = find_session()
	prompts = load_prompts(session_path)
	output_records: list[dict[str, object]] = []
	for record in RECORDS:
		handle = str(record["handle"])
		if handle not in prompts:
			raise RuntimeError(f"No exact ImageGen prompt found for {handle}")
		workspace_source = PACKAGE_ROOT / str(record["workspace_source"])
		if not workspace_source.is_file():
			raise FileNotFoundError(workspace_source)
		output_records.append(
			{
				**record,
				"provider": "OpenAI built-in ImageGen (gpt-image 2.0 provenance assertion)",
				"session_id": SESSION_ID,
				"generated_original": (
					f"C:/Users/klimp/.codex/generated_images/{SESSION_ID}/{handle}.png"
				),
				"generation_timestamp": prompts[handle]["timestamp"],
				"exact_revised_prompt": prompts[handle]["prompt"],
				"workspace_source_sha256": sha256(workspace_source),
			}
		)

	METADATA_DIR.mkdir(parents=True, exist_ok=True)
	PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
	output_path = METADATA_DIR / "source_handles.json"
	output_path.write_text(
		json.dumps(
			{
				"package": "Event 015 Necessary Ground case cards",
				"accepted_count": 10,
				"rejected_count": 3,
				"prompt_field": "exact_revised_prompt is copied from image_generation_end",
				"session_transcript": str(session_path),
				"records": output_records,
			},
			indent=2,
			ensure_ascii=False,
		),
		encoding="utf-8",
	)

	markdown_lines = [
		"# Exact built-in ImageGen prompts",
		"",
		(
			"This catalog is generated from the session transcript's "
			"`image_generation_end.revised_prompt` field. The ten accepted "
			"masters and three aspect-ratio rejections are preserved below."
		),
		"",
	]
	for record in output_records:
		markdown_lines.extend(
			[
				f"## {record['state']} — {record['status']}",
				"",
				f"- Handle: `{record['handle']}`",
				f"- Workspace source: `{record['workspace_source']}`",
				f"- SHA-256: `{record['workspace_source_sha256']}`",
			]
		)
		if "rejection_reason" in record:
			markdown_lines.append(f"- Rejection: {record['rejection_reason']}")
		markdown_lines.extend(
			[
				"",
				"```text",
				str(record["exact_revised_prompt"]),
				"```",
				"",
			]
		)
	(PROMPTS_DIR / "exact_imagegen_prompts.md").write_text(
		"\n".join(markdown_lines),
		encoding="utf-8",
	)
	print(output_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
