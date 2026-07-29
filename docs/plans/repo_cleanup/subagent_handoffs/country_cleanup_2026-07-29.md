# Country package cleanup handoff (Events 1-20) — 2026-07-29

Status: bounded audit complete with three local cleanup patches. No commit was created because the parent requested a shared-worktree handoff without committing.

## Scope and references

This handoff covers country-package surfaces for Events 1-20 and shared country/AI references in `common/country_tags/`, `common/countries/`, `history/countries/`, `common/ai_strategy/`, `common/ai_templates/`, and country-package localisation/docs. `common/national_focus/` and `common/decisions/` were not changed.

I followed `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/hoi4-focus-trees/SKILL.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-improvement-loop/SKILL.md`.

I consulted the required offline Paradox wiki pages in `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, and National focus modding, plus the relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` and vanilla country/history precedents.

## Changed files and behavior

- `common/ai_strategy/ZZZ.txt`: removed a contradictory duplicate `ai_strategy = { type = template_prio id = zombies value = -1000 }` from `ZZZ_unit_production`, leaving the intended positive `zombies` template priority of `2500`; also removed the second identical `role_ratio` suppression for `infantry` in the minimization block. Before the patch the duplicate entries could override or negate the intended zombie production weighting; after the patch each `(type,id)` pair is declared once.
- `history/countries/ZIN - ZIN.txt`: removed the second `elections_allowed = no` entry inside the `set_politics` block. Before the patch the same key appeared twice; after the patch the intended non-elective politics setup is represented once.
- `localisation/english/chaosx_countries_l_english.yml`: corrected `REV_ADJ: "Revolutinary"` to `REV_ADJ: "Revolutionary"`. No tag, state, leader, party, focus, decision, or formable identifier was added or removed.

## Country package coverage checklist

- Event 001 (`REV`): registered in `common/country_tags/chaosx_countries.txt`, with `common/countries/REV - The Revolution.txt`, `history/countries/REV - The Revolution.txt`, OOB/character references, base flag, and base name/adjective localisation. Active party-name keys remain a deferred identity decision because no authoritative party naming source was found.
- Event 002 (`ZZZ`, `ZIN`): registered country files, histories, OOB/character references, flags, ideas, and base name/adjective localisation are present. `ZZZ` AI duplicate weighting was fixed and `ZIN` duplicate politics syntax was fixed.
- Events 003-004, 007-009, 011-013, 015, 017, and 019: no standalone custom country-tag package was found in the owned country surfaces; these events use shared or existing carriers and require broader event/system review outside this bounded country cleanup.
- Event 005: the current Soviet-collapse registry contains `CFR MFR IJX INX SOG ANX ABX AOX FTH BBH AEX IKX DSC UWR KMB NRF TNC AAX UDC SDZ GAC DHC KHC FEV SZA UWD IMX IUL ADX PRA ILX ICD ARD NLC` in `common/country_tags/chaosx_countries.txt`. Their common country definitions, histories, capitals, OOB references, portrait references, flags, and base country localisation resolve in static checks. Existing event documentation still marks broader successor/reconsolidation playability, presentation parity, and final package audits as open work.
- Event 006: `common/country_tags/006_independence_wave_countries.txt` contains 102 reserved rows; 17 intentionally inert reservations use `common/countries/006_independence_wave_unresearched_reservations.txt`, while 85 researched rows have country histories and base name/adjective localisation. Only 15 of the 85 researched rows have a base flag; the missing-flag list is recorded below. Event documentation explicitly keeps this package `HOLD / PARTIAL` pending identity, asset, leader, focus, decision, idea, force, technology, AI, formable, and localisation work.
- Event 010 (`DTH`): `common/countries/Death.txt`, `history/countries/DTH - Death.txt`, OOB, leader, flag, and localisation surfaces resolve; the intentionally passive world-end role is documented.
- Event 014 (`CBA`-`CBH`, `CBL`): reusable cannibalism-warlord and unified-host country surfaces resolve with histories, capitals, runtime-owned warlord setup, flags, and localisation as documented.
- Event 016 (`KRG`): dormant `KRG` package files and runtime release hooks resolve; no country-file defect was found.
- Event 018 (`DHO`): `DHO` history, institutional leader/portrait references, custom-unit OOB, flag, AI, and localisation surfaces resolve. The `DHO_vhorruk` recruitment before neutral politics is intentional and documented.
- Event 020 (`RTA`, `RTX`): current two-tag package has histories, flags, leaders, parties, AI, focus/decision links, custom unit templates, and localisation; the current handoff reports no package issue to patch.

## File surface checklist

- `common/country_tags/`: custom package tags are registered once and map to existing country-definition files; no duplicate tag rows or external country-definition/identity collisions were found.
- `common/countries/`: package files contain the expected graphical culture and colour surfaces; the comment-only Event 006 inert reservation file is an intentional parser-safe fail-closed placeholder.
- `history/countries/`: package histories have valid capital IDs, OOB references, politics blocks, and recruited character IDs; Event 006 inert reservations intentionally have no histories.
- `history/units/` and `common/characters/`: every custom package `oob`/`set_oob` and recruited character reference resolved in static checks.
- `common/ai_strategy/` and `common/ai_templates/`: custom tag context references are registered; exact duplicate `(type,id)` pairs were removed from `ZZZ` AI strategy. No unused package file was deleted because deadness could not be proven.
- `interface/`, `gfx/`, flags, portraits, and localisation: non-Event-006 package base flags and literal portrait references resolve; Event 006 broad asset readiness remains deferred.

## Missing or stale package surfaces

Event 006 researched tags missing base flags are: `AKX ATX AXX BAX BBX BFX BHX BJX BKX BWX CIX CJX CKX CLX COX CPX CQX CUX CVX CWX CXX CYX DAX DBX DFX DHX HYX DKX DLX DPX DVX EBX EEX EHX ELX ERX ESX HZX EUX EWX FAX FBX FDX FLX FNX FOX FSX FUX FVX FXX GBX GCX IAX IBX GIX GMX GRX GTX GYX GZX HAX HCX HDX HEX HFX HGX HKX HPX HSX HUX`.

This is the canonical 70-tag set from the audited rows in `common/country_tags/006_independence_wave_countries.txt` and should be regenerated before any future asset work.

Event 006 also lacks many country-specific leaders/portraits, parties, focus trees, decisions, ideas, forces, technology, AI, formables, and final localisation surfaces. The 17 inert reservations intentionally lack history, localisation, and flags until their research package is approved.

`ZZZ`, `ZIN`, and `REV` have base country name/adjective localisation but no active ideology party-name keys in `localisation/english/chaosx_countries_l_english.yml`. No design-authoritative party names were found, so this remains a deferred identity decision rather than invented cleanup text. Dynamic active-neutrality party localisation for `CBA`-`CBL` and `RTA`/`RTX` is present.

`common/ai_strategy/020_black_plague_rat_ai_strategy.txt` uses semantic IDs `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, and `rat_tunnelers`, while `history/units/020_black_plague_rat_1936.txt` names the visible templates `Rat Brood`, `Rat Shock Brood`, `Rat Burrow Column`, `Rat Carrion Guard`, and `Rat Dock Stowaways`. Prior Event 020 handoffs treat these custom identifiers as resolved, but the relationship to AI-template role IDs is not independently proven by this bounded pass; a broader AI-template reconciliation would require design authority and is deferred.

## Map and state setup

All package `capital` values, including dormant `capital = 1` setups, resolve against the vanilla state set of 1081 IDs. No state history or map rewrite was required. Event 006 runtime transfer/capital behavior remains owned by its event system and was not altered.

All custom `oob` and `set_oob` references resolve to files in `history/units/`; dormant countries use intentionally empty or locked setup where documented. No map write or map MCP operation was performed.

## Politics, leaders, portraits, flags, advisors, and parties

Event 005 random-leader histories have consistent gender metadata: every female-presenting leader has `female = yes`, and male-presenting leaders do not set the female field. Literal package portrait references resolve to a repository GFX definition, and institutional portraits use institutional names rather than personal random-name pools.

Event 006 base-flag coverage is the broad gap listed above; adding flags, portraits, or party identities would be an asset/source-research task rather than a safe cleanup. No advisor icon or portrait package was invented.

## Focus, decision, idea, and asset surfaces

This subtask deliberately excluded `common/national_focus/` and `common/decisions/`. Existing Event 005 and Event 006 documentation records focus/decision gaps for broader implementation; Event 020 current two-tag focus/decision coverage is documented as present. No focus tree, decision system, idea family, or asset package was redesigned.

Non-Event-006 package idea/flag surfaces resolve in the static package scan. Event 006 asset and identity gaps remain `HOLD / PARTIAL`.

## Starting military, technology, industry, supply, and production

Every custom package history OOB reference and recruited character ID resolves. Dormant countries intentionally use zero or runtime-owned conventional setup where documented. Event 005 dynamic release setup, Event 006 runtime releases, Event 014 warlord slots, Event 018 DHO custom units, and Event 020 rat forces were not expanded or rebalanced in this cleanup.

## AI and playability

Custom AI strategy context tags resolve to registered or vanilla tags. The `ZZZ` template file `common/ai_templates/ZZZ.txt` and OOB `history/units/ZZZ_1936.txt` support the `zombies` priority ID; duplicate/conflicting `ZZZ` strategy entries were removed. The rat AI identifier uncertainty is retained above because resolving it safely may require coordinated template/effect changes.

## Event 21+ and shared references

No Event 21+ gameplay file, event target, scripted GUI, map, or shared runtime hook was changed. Shared country/tag and AI files were inspected only where Event 1-20 packages referenced them.

## Rejected or deferred candidates

- Do not add the 70 Event 006 flags, portraits, party names, or other identity surfaces without approved country-specific source/design packages; the event remains documented `HOLD / PARTIAL`.
- Do not add a new rat AI-template file or rewrite rat scripted effects without reconciling the existing Event 020 design and prior handoff evidence.
- Do not invent active party names for `ZZZ`, `ZIN`, or `REV` without an identity decision.
- Do not delete any country or AI package file because no file was proven unused or dead.

## Validation evidence

- `.tools/audit_chaosx_country_tags.py --surface-scan` completed with `Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1`.
- The corrected combined static package audit reported `package tags=153 inert_006=17 histories=136` and `errors= 0` for tag mappings, histories, capitals, OOBs, recruited characters, targeted `set_politics` duplicate keys, exact duplicate AI strategy `(type,id)` pairs, and legacy-ID gameplay references.
- Event 006 package counts were `rows 102 inert 17 resolved with history 85 expected researched 85 missing history []`.
- All package capitals resolved against vanilla state IDs; all package OOB and recruited-character references resolved; package portrait `GFX_*` references had repository definitions; no Event 005 leader gender mismatch was found.
- Edited script/history files retain the repository line-ending style; the localisation file retains UTF-8 BOM and CRLF encoding.
- No game launch or live save validation was performed, as required by repository instructions; no map write was performed.

## Remaining risks

The Event 006 country package is still `HOLD / PARTIAL`, with 70 researched tags missing base flags and broader identity/focus/decision/idea/force/technology/AI/formable/localisation work outstanding. Active party localisation for `ZZZ`, `ZIN`, and `REV` remains an unapproved identity decision. Rat AI semantic IDs remain a deferred reconciliation risk. Live in-game behavior was not tested.

No simplification was silently substituted for requested country cleanup; the three narrow defects were corrected, and broad design/asset gaps are explicitly retained for parent planning.
