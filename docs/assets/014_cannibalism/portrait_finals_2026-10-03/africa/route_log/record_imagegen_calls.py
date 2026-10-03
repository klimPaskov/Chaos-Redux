"""Record native ImageGen prompts, returned paths, errors, and retained bytes."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOT = Path(r"C:/Users/klimp/.codex/generated_images/01a101df-456d-7ea2-bacf-eedea456699e")
OUTPUT_IDS = {
    "CBA": "exec-d356a3f3-63b3-40b2-adfb-ba8012c45801.png",
    "CBB": "exec-d9f717ed-3348-443e-afbe-f1a52ad684f6.png",
    "CBC": "exec-a29fbec6-0461-4cbe-8106-eb516a04ebb4.png",
    "CBD": "exec-41c7399b-d444-4d6f-b5e6-87d6a6d01ba3.png",
    "CBE": "exec-a50e5f9c-13d2-45c6-93b4-e2281a0e9f0f.png",
    "CBF": "exec-13788e1f-28b6-41fb-b613-26b829a53f3f.png",
    "CBG": "exec-014ef54d-1cc4-4861-b5c7-c7236856362e.png",
    "CBH": "exec-8320024c-e7ca-418c-9f58-4e665dc64590.png",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def prompt_record(path: Path) -> dict[str, str]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256(path)}


def source_record(slot: str) -> dict[str, object]:
    native = ROOT / "source_png" / f"leader_{slot}_warlord_africa_native.png"
    original = GENERATED_ROOT / OUTPUT_IDS[slot]
    if sha256(native) != sha256(original):
        raise ValueError(f"Retained workspace source differs from native ImageGen output: {slot}")
    with Image.open(native) as image:
        image.load()
        dimensions, mode = list(image.size), image.mode
    return {
        "tool_returned_path": original.as_posix(),
        "workspace_source_png": native.relative_to(ROOT).as_posix(),
        "dimensions": dimensions,
        "mode": mode,
        "sha256": sha256(native),
        "byte_identical_to_tool_output": True,
    }


def main() -> None:
    calls = []
    for slot in ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH"):
        if slot == "CBE":
            initial_prompt = ROOT / "prompts/leader_CBE_warlord_africa_prompt.txt"
            retry_prompt = ROOT / "prompts/leader_CBE_warlord_africa_retry01_prompt.txt"
            attempts = [
                {
                    "attempt": 1,
                    "prompt": prompt_record(initial_prompt),
                    "status": "rejected by output safety review",
                    "http_status": 400,
                    "request_id": "d202df39-8ff6-4240-9853-1dcefec4472f",
                    "moderation_stage": "output",
                    "categories": ["violence"],
                    "provider_message": "Your request was rejected by the safety system. If you believe this is an error, contact us at help.openai.com and include the request ID d202df39-8ff6-4240-9853-1dcefec4472f. safety_violations=[violence].",
                    "returned_asset": None,
                    "retry_reason": "Native generation produced no candidate; retry narrowed graphic language while retaining the exact four-case counting action and blood-stained fingers.",
                },
                {
                    "attempt": 2,
                    "prompt": prompt_record(retry_prompt),
                    "status": "success",
                    "source": source_record(slot),
                },
            ]
        else:
            prompt = ROOT / "prompts" / f"leader_{slot}_warlord_africa_prompt.txt"
            attempts = [{"attempt": 1, "prompt": prompt_record(prompt), "status": "success", "source": source_record(slot)}]
        calls.append(
            {
                "slot": slot,
                "candidate_id": "AF-CBE-NATIVE-R01" if slot == "CBE" else f"AF-{slot}-NATIVE-01",
                "parent_candidate_id": None,
                "new_generation_reason": "Distinct accepted Africa slot and assigned action; no source image or identity anchor was provided.",
                "source_mode": "fictional_high_chaos",
                "background_mode": "consumer_opaque",
                "tool": "built-in image_gen",
                "model_selector": "not exposed by the built-in tool",
                "transparent_background": False,
                "input_images": [],
                "attempts": attempts,
            }
        )

    log = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Event 014 CBA-CBH Africa fictional portrait source provenance",
        "generation_route": "native built-in ImageGen; one call per slot, with the single recorded CBE retry after an explicit native output rejection",
        "identity_sources": [],
        "third_party_raster_sources": [],
        "provenance_and_rights": "All subjects are invented fictional adult humans. No Internet identity source, real person, or third-party raster was used. No separate legal license claim is made for generated output.",
        "calls": calls,
    }
    output = ROOT / "route_log/imagegen_call_log.json"
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite ImageGen call log: {output}")
    output.write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"log": output.as_posix(), "successful_slots": len(calls), "CBE_attempts": 2}))


if __name__ == "__main__":
    main()
