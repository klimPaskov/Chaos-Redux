# Event 016 tracked Kruger holder and KRG history loader repair

Date: 2026-08-02

Status: parent-owned repair complete; live save validation remains user-owned.

## Scope

The opening appointment used the reserved `DJX` country as the origin of the fixed `KRG_warren_kruger` character, but the Event 006 tag map points `DJX` at a missing shared history filename and the per-tag holder files are untracked outside Event 016.

## Changes

- `history/countries/KRG - Kruger State.txt` now recruits `KRG_warren_kruger` in the tracked dormant country history alongside the institutional roster.
- `common/country_tags/016_brilliant_scientist_country.txt` now points `KRG` at the tracked `history/countries/KRG - Kruger State.txt` filename.
- `brilliant_scientist_appoint_kruger_from_opening` now uses the documented `every_possible_country` plus character-scope `set_nationality` pattern, so the opening finds the one recruited Kruger token without a hard-coded cross-event holder tag.
- The duplicate guard now checks every active country for the fixed character and no longer exempts `DJX`.
- A trailing history comment keeps the final KRG recruitment call from being the last parsed history line.

## Validation

- The KRG tag path resolves to an existing tracked history file.
- The tracked KRG history contains exactly one `recruit_character = KRG_warren_kruger` call.
- Event 016 scripted-effect scans contain no remaining `DJX` holder reference.
- Focused Event Inspector lint for `chaosx.nr16.2` returned `status = ok` with zero blocking diagnostics; workspace-wide helper analysis remains deferred by the tool's large-workspace limit.
- No model, entity, animation, or new visual asset was created.

## Remaining risk

The unrelated Event 006 reserved-country mappings still point several tags at their existing missing shared placeholder path; this repair leaves those out of scope and does not stage the pre-existing untracked reservation files.

Live opening, transfer, and formation scenarios remain user-owned acceptance work.
