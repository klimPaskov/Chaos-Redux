"""Bounded source assertions for the 2026-10-09 dated scientist-trait repair."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = Path(__file__).resolve().parent
BEFORE = EVIDENCE / "before"
CHARACTER_PATH = ROOT / "common/characters/cbrn_historical_scientists.txt"
EFFECT_PATH = ROOT / "common/scripted_effects/chaosx_startup_history_effects.txt"
SPECIALIST_PATH = ROOT / "common/characters/cbrn_historical_specialists.txt"
HISTORY_PATH = ROOT / "history/general/chaosx_startup_character_recruitment.txt"
ON_ACTION_PATH = ROOT / "common/on_actions/cbrn_historical_startup_on_actions.txt"


def read(path: Path) -> str:
    # Current Git candidates may use LF while exact archived snapshots retain CRLF.
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


def brace_end(text: str, start: int) -> int:
    open_at = text.index("{", start)
    depth = 0
    in_string = False
    escaped = False
    in_comment = False
    for pos in range(open_at, len(text)):
        char = text[pos]
        if in_comment:
            if char == "\n":
                in_comment = False
            continue
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == "#":
            in_comment = True
        elif char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return pos + 1
    raise AssertionError(f"unclosed block at character offset {start}")


def named_block(text: str, token: str) -> str:
    pattern = re.compile(r"(?m)^[\t ]*" + re.escape(token) + r"\s*=\s*\{")
    matches = list(pattern.finditer(text))
    assert len(matches) == 1, f"expected one definition for {token}, found {len(matches)}"
    match = matches[0]
    return text[match.start() : brace_end(text, match.start())]


def direct_if_blocks(text: str) -> list[tuple[int, int, str]]:
    blocks = []
    for match in re.finditer(r"(?m)^\tif = \{", text):
        end = brace_end(text, match.start())
        blocks.append((match.start(), end, text[match.start() : end]))
    return blocks


def report(results: list[dict[str, object]]) -> None:
    payload = {
        "task": "2026-10-09_scientist_conduct_traits",
        "kind": "source-only acceptance checks",
        "native_runtime_executed": False,
        "results": results,
        "passed": all(item["passed"] for item in results),
    }
    (EVIDENCE / "source_test_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


def main() -> None:
    before_manifest = json.loads((EVIDENCE / "before_manifest.json").read_text(encoding="utf-8"))
    before_hashes = {row["source"]: row["source_sha256"] for row in before_manifest}
    old_chars = read(BEFORE / "cbrn_historical_scientists.txt")
    old_effects = read(BEFORE / "chaosx_startup_history_effects.txt")
    chars = read(CHARACTER_PATH)
    effects = read(EFFECT_PATH)
    results: list[dict[str, object]] = []

    def check(name: str, passed: bool, details: str) -> None:
        results.append({"name": name, "passed": bool(passed), "details": details})

    for relative, path in (
        ("common/characters/cbrn_historical_scientists.txt", CHARACTER_PATH),
        ("common/scripted_effects/chaosx_startup_history_effects.txt", EFFECT_PATH),
    ):
        snapshot = BEFORE / Path(relative).name
        actual = hashlib.sha256(snapshot.read_bytes()).hexdigest()
        check(
            f"byte-exact-before-snapshot:{relative}",
            actual == before_hashes[relative],
            f"manifest={before_hashes[relative]} snapshot={actual}",
        )

    targets = {
        "GER_sigmund_rascher": "scientist_trait_inhumane",
        "GER_josef_mengele": "scientist_trait_inhumane",
    }
    character_edits: list[tuple[int, int, str]] = []
    for person, trait in targets.items():
        match = re.search(r"(?m)^[\t ]*" + re.escape(person) + r"\s*=\s*\{", old_chars)
        assert match, f"missing before character definition {person}"
        old_block = old_chars[match.start() : brace_end(old_chars, match.start())]
        new_block = named_block(chars, person)
        removal = re.compile(r"(?m)^[\t ]*traits\s*=\s*\{\s*" + re.escape(trait) + r"\s*\}[\t ]*(?:\r?\n)?")
        old_without_trait, removed = removal.subn("", old_block, count=1)
        check(f"static-trait-removed:{person}", removed == 1 and trait not in new_block, f"removed={removed}; current static trait present={trait in new_block}")
        check(f"character-id-portrait-skill-preserved:{person}", old_without_trait == new_block, "character definition matches the raw before block after removing only the dated trait line")
        character_edits.append((match.start(), match.start() + len(old_block), old_without_trait))
    expected_chars = old_chars
    for start, end, updated_block in sorted(character_edits, reverse=True):
        expected_chars = expected_chars[:start] + updated_block + expected_chars[end:]
    check("character-file-text-preservation", expected_chars == chars, "after checkout newline normalization, the full character file differs only by the two scoped trait-line removals")

    def_ids = re.compile(r"(?m)^[\t ]*([A-Z]{3}_[A-Za-z0-9_]+)\s*=\s*\{")
    old_character_ids = def_ids.findall(old_chars)
    new_character_ids = def_ids.findall(chars)
    specialist_ids = def_ids.findall(read(SPECIALIST_PATH))
    current_ids = new_character_ids + specialist_ids
    check("character-identity-set-preserved", len(old_character_ids) == len(new_character_ids) and set(old_character_ids) == set(new_character_ids), f"before={len(old_character_ids)} current={len(new_character_ids)}")
    check("67-roster-identities-present", len(current_ids) == 67 and len(set(current_ids)) == 67, f"scientists={len(new_character_ids)} specialists={len(specialist_ids)} total={len(current_ids)} unique={len(set(current_ids))}")

    helper_name = "chaosx_startup_recruit_dated_ger_cbrn_characters"
    old_helper = named_block(old_effects, helper_name)
    new_helper = named_block(effects, helper_name)
    award_flags = {
        "rascher_inhumane_trait_awarded": ("GER_sigmund_rascher", "1941.05.14"),
        "mengele_inhumane_trait_awarded": ("GER_josef_mengele", "1943.05.29"),
    }
    award_spans = []
    blocks = direct_if_blocks(new_helper)
    for flag, (person, previous_day) in award_flags.items():
        matches = [(start, end, block) for start, end, block in blocks if flag in block]
        check(f"one-date-award-block:{person}", len(matches) == 1, f"matching top-level blocks={len(matches)}")
        if len(matches) != 1:
            continue
        start, end, block = matches[0]
        award_spans.append((start, end))
        required = [
            f"date > {previous_day}",
            f"has_character = {person}",
            f"NOT = {{ has_country_flag = {flag} }}",
            f"{person} = {{ add_scientist_trait = scientist_trait_inhumane }}",
            f"set_country_flag = {flag}",
        ]
        missing = [token for token in required if token not in block]
        check(f"date-and-idempotency-guards:{person}", not missing, f"missing={missing}")
        check(f"no-runtime-recruit-in-award:{person}", "recruit_character" not in block, "award block contains only a dated character-trait effect and its one-time flag")

    reduced_helper = new_helper
    for start, end in reversed(award_spans):
        reduced_helper = reduced_helper[:start] + reduced_helper[end:]
    hirt_anchor = "\tif = {\n\t\tlimit = {\n\t\t\t# Hirt's first documented"
    reduced_helper = re.sub(r"(?:\n){2,}(?=" + re.escape(hirt_anchor) + r")", "\n", reduced_helper, count=1)
    check("all-other-GER-helper-content-unchanged", reduced_helper == old_helper, "removing the two new top-level award blocks reproduces the exact before helper, including CSH transfer gates and the other five trait dates")
    check("all-other-startup-effects-unchanged", effects.replace(new_helper, reduced_helper, 1) == old_effects, "the complete startup effects file is preserved outside the two new award blocks after checkout newline normalization")

    for person, year, month, day in (
        ("GER_sigmund_rascher", 1941, 5, 15),
        ("GER_josef_mengele", 1943, 5, 30),
    ):
        award_flag = next(flag for flag, values in award_flags.items() if values[0] == person)
        threshold_year, threshold_month, threshold_day = map(int, award_flags[award_flag][1].split("."))
        threshold = dt.date(threshold_year, threshold_month, threshold_day)
        first_date = dt.date(year, month, day)
        before_date = first_date - dt.timedelta(days=1)
        after_date = first_date + dt.timedelta(days=1)
        def eligible(date: dt.date, has_character: bool, flag_set: bool) -> bool:
            return date > threshold and has_character and not flag_set
        cases = {
            "before": not eligible(before_date, True, False),
            "effective_date": eligible(first_date, True, False),
            "after_unawarded_start": eligible(after_date, True, False),
            "duplicate_guard": not eligible(first_date, True, True),
            "unrecruited_guard": not eligible(first_date, False, False),
        }
        check(f"dated-guard-scenarios:{person}", all(cases.values()), json.dumps(cases, sort_keys=True))

    startup = read(ROOT / "common/scripted_effects/chaosx_startup_history_effects.txt")
    on_actions = read(ON_ACTION_PATH)
    all_gameplay_txt = "\n".join(
        path.read_text(encoding="utf-8")
        for folder in (ROOT / "common", ROOT / "events", ROOT / "history")
        for path in folder.rglob("*.txt")
    )
    total_calls = all_gameplay_txt.count(helper_name)
    daily_ger = re.search(r"on_daily_GER\s*=\s*\{[\s\S]*?GER\s*=\s*\{\s*" + re.escape(helper_name) + r"\s*=\s*yes\s*\}", on_actions)
    startup_ger = re.search(r"GER\s*=\s*\{\s*" + re.escape(helper_name) + r"\s*=\s*yes\s*\}", startup)
    check("only-existing-GER-startup-and-daily-callers", total_calls == 3 and daily_ger is not None and startup_ger is not None, f"definition-plus-calls={total_calls}; on_daily_GER={daily_ger is not None}; startup_GER={startup_ger is not None}")

    event_texts = [*(ROOT / "events").glob("016*.txt"), ROOT / "events/germany_mengele.txt"]
    direct_consumers = []
    for path in event_texts:
        event_text = read(path)
        for token in ("GER_josef_mengele", "GER_sigmund_rascher", "scientist_trait_inhumane"):
            if token in event_text:
                direct_consumers.append(f"{path.relative_to(ROOT)}:{token}")
    check("no-direct-event-character-or-trait-consumer", not direct_consumers, f"direct consumers={direct_consumers}; Event 016 and Germany chain use their own event/country flags")

    portrait_only_files = (
        ROOT / "common/scripted_effects/chaosx_triggerable_scenarios_effects.txt",
        ROOT / "common/scripted_effects/germany_mengele_effects.txt",
    )
    character_token = re.compile(r"(?<![A-Za-z0-9_])(?:GER_josef_mengele|GER_sigmund_rascher)(?![A-Za-z0-9_])")
    portrait_only_results = []
    for path in portrait_only_files:
        source = read(path)
        direct_ids = character_token.findall(source)
        direct_traits = source.count("scientist_trait_inhumane")
        reused_portraits = source.count("GFX_portrait_GER_josef_mengele")
        portrait_only_results.append({"file": str(path.relative_to(ROOT)), "direct_character_ids": direct_ids, "direct_trait_refs": direct_traits, "portrait_refs": reused_portraits})
    check("separate-Mengele-leader-routes-use-portrait-only", all(not row["direct_character_ids"] and row["direct_trait_refs"] == 0 and row["portrait_refs"] == 1 for row in portrait_only_results), json.dumps(portrait_only_results, sort_keys=True))

    report(results)


if __name__ == "__main__":
    main()
