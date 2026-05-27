# Event 005 Leader Portrait/Name Gender Recheck

Date: 2026-05-27

Scope: bounded country-package sidecar for the latest user correction that leader portraits and names must match by apparent gender. No balance, decision, focus, flag, or asset files were edited.

## Coverage Checklist

- Event 005 custom history leader files checked: `ALA`, `ALN`, `ARD`, `BAC`, `BBH`, `BSC`, `CFR`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `MFR`, `MRC`, `NLC`, `NRF`, `OGB`, `PRA`, `RMC`, `SDZ`, `SOG`, `SZA`, `TNC`, `TSC`, `UDC`, `UWD`.
- Scripted release-council leader branches checked: `MOL`, `UZB`, `TAJ`, `TMS`, `FER` in `soviet_collapse_apply_event_created_republic_council_leader`.
- Randomized single-person leader name pools checked in `soviet_collapse_randomize_single_person_leader_name`.
- Related portrait wiring checked in `interface/005_soviet_collapse_custom_icons.gfx` and `interface/005_soviet_collapse_factory_ancient_icons.gfx`.
- Related localisation checked for leader-description surfaces in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.

## File Surface Checklist

- `history/countries/<TAG> - *.txt`: read only for the 32 active Event 005 custom country leaders.
- `common/scripted_effects/005_soviet_collapse_effects.txt`: read only for random leader-name pools and release-council leader creation.
- `interface/005_soviet_collapse_custom_icons.gfx`: read only for active portrait sprite-to-DDS references.
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`: read only for factory/ancient portrait sprite-to-DDS references.
- `gfx/leaders/005_soviet_collapse/*_leader.dds`: reviewed through `/tmp/event005_leader_recheck/live_leaders_contact.png`.

## Findings

No small proven gender/name mismatch was found in the active wired surface.

- Female-presenting active portraits with explicit `female = yes` remain matched to female pools: `BAC`, `NLC`, `TSC`, `UDC`, `UWD`.
- Male-presenting active release-council portraits remain matched to male pools after the previous correction: `MOL`, `UZB`, `TAJ`, `TMS`, `FER`.
- Remaining active custom history leaders either use male-presenting portraits with male pools or institutional/council names before the randomizer runs.
- No live Event 005 leader DDS hash matched vanilla leader DDS files in the direct hash check, so no actual real-person portrait/name replacement was identified from the live file surface.

## Required Audit Categories

- Missing or stale country package surfaces: the previously noted unwired promoted portrait DDS files for `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` remain outside active leader creation in this pass; no gender/name fix was applied to them because they are not currently wired by `.gfx` plus `create_country_leader`.
- Map and state setup issues: not audited beyond confirming no leader-name change was needed.
- Politics, leader, portrait, flag, advisor, and party issues: no active leader portrait/name gender mismatch found; no advisor, party, or flag edits made.
- Focus, decision, idea, and asset issues: no focus, decision, idea, or asset edits made.
- Starting military, technology, industry, supply, and production issues: not in scope; no edits made.
- AI and playability issues: not in scope; no edits made.

## Files Changed

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_27_event005_leader_portrait_name_gender_recheck.md`

Changed tags, state ids, leaders, parties, focus tree ids, localisation keys, or formable ids: none.

Before and after behavior: no gameplay behavior changed.

## Validation

- Read `AGENTS.md`, `chaos-redux-subagents`, and `chaos-redux-events`.
- Consulted offline wiki pages required by the prompt, including country creation, localisation, effects, triggers, scopes, portraits, events, decisions, ideas, modifiers, on actions, and AI.
- Consulted vanilla documentation and examples: `/home/klim/projects/Hearts of Iron IV/common/characters/_documentation.md`, vanilla `SOV` character/history precedent, and core script documentation under `/home/klim/projects/Hearts of Iron IV/documentation/`.
- Built and reviewed `/tmp/event005_leader_recheck/live_leaders_contact.png` from live `gfx/leaders/005_soviet_collapse/*_leader.dds`.
- `identify` found no non-`156x210` live Event 005 leader DDS files.
- Direct SHA-256 check found `0` vanilla hash matches among live Event 005 leader DDS files.
- `rg` checks confirmed current `MOL` and `TAJ` male replacement pools are present and old mismatched female pools are absent from the scripted-effect surface.

Skipped validation: no in-game parser/load validation was run from this sidecar.

## Uncertainty

The portrait gender assessment is visual and source-level only. Several portraits are generated institutional/council concepts centered on one person; this pass treated already-wired random pools as the governing name surface and did not redesign institutional versus one-person leader identity.
