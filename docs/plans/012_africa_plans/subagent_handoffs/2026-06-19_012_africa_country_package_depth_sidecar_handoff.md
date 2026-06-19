# Event 012 Africa Country Package Depth Sidecar Handoff

Date: 2026-06-19
Agent role: Chaos Redux country-package auditor subagent
Scope: Event 012 Africa created-country package audit and small patch pass for `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`, `BON`, `HYR`, `BIR`, and `SAO`.

## Changed Files

Intentional country-package changes:

- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `history/countries/BON - Bonobo Kinship Congress.txt`
- `history/countries/BIR - Bird of the Walls.txt`
- `history/units/BON_1936.txt`
- `history/units/BIR_1936.txt`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-19_012_africa_country_package_depth_sidecar_handoff.md`

Important worktree note: `common/scripted_effects/012_africa_effects.txt` and `common/scripted_triggers/012_africa_triggers.txt` also contain unrelated existing/concurrent forgery-museum diffs. I did not author or revert those. My intentional edits in those two files are only the Event 012 seat constants listed below.

No Event 010 files were edited by this pass. No commit was made.

## Fixes Made

### Shared classification

Before:

- `BON`, `HYR`, `BIR`, and `SAO` existed as Event 012 high-chaos actors and receive `africa_high_chaos_actor` / `africa_high_chaos_nonhuman` during setup, but the shared `is_special_chaos_country` and `is_actual_nonhuman_country` static tag lists still ended at `GHC`.

After:

- Added `BON`, `HYR`, `BIR`, and `SAO` to `is_special_chaos_country`.
- Added `BON`, `HYR`, `BIR`, and `SAO` to `is_actual_nonhuman_country`.
- Updated `common/scripted_triggers/chaosx_dynamic_triggers.md` coverage notes for both classifiers.

Changed identifiers:

- Tags: `BON`, `HYR`, `BIR`, `SAO`.
- Scripted triggers: `is_special_chaos_country`, `is_actual_nonhuman_country`.

### Duplicate seat-state cleanup

Before:

- `BON` used `@africa_bon_seat_state = 295`, overlapping `CBC` / Congo Basin Charter state `295`.
- `BIR` used `@africa_bir_seat_state = 771`, overlapping `ZSC` / Zambezi-Stone Cities state `771`.
- Their standalone history capitals and OOB locations matched those duplicate seats.

After:

- `BON` moved to Lusambo state `888`, with history capital `888`, OOB province `2024`, and unit name `Lusambo Kinship Envoys`.
- `BIR` moved to Malawi state `770`, with history capital `770`, OOB province `12986`, and unit name `Malawi Wall Watch`.
- `docs/events/012_africa_foundation.md` now records `BON` Lusambo `888` and `BIR` Malawi `770`.

Changed state ids and identifiers:

- `@africa_bon_seat_state`: `295` -> `888`.
- `@africa_bir_seat_state`: `771` -> `770`.
- `BON` history capital: `295` -> `888`.
- `BIR` history capital: `771` -> `770`.
- `BON_1936` OOB location: `5117` -> `2024`.
- `BIR_1936` OOB location: `5199` -> `12986`.

## Country Package Coverage Checklist

- Tag registration: all 25 target tags are registered in `common/country_tags/chaosx_countries.txt`.
- Country files: all 25 target tags resolve to existing `common/countries/*.txt` files.
- History files: all 25 target tags have `history/countries/TAG - *.txt`.
- Static land OOBs: all 25 target tags have `history/units/TAG_1936.txt`.
- Localisation: all 25 target tags have base, DEF, ADJ, and ideology-specific country keys in `localisation/english/chaosx_countries_l_english.yml`.
- Flags: all 25 target tags have root, ideology, medium, and small `.tga` flag families.
- Portraits/leaders: all 25 histories use institutional or nonhuman/supernatural leader names; no personal generated name pool mismatch was found.
- AI: all 25 tags have at least grouped AI posture coverage in `common/ai_strategy/012_africa.txt`; each tag appears in the strategy file.
- Focus loading: regional authorities load `africa_regional_authority_focus_tree`; high-chaos actors load `africa_high_chaos_actor_focus_tree`.

## File Surface Checklist

Checked surfaces:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/*.txt` for all 25 tags
- `history/countries/*.txt` for all 25 tags
- `history/units/*_1936.txt` for all 25 tags
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/ai_strategy/012_africa.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `interface/012_africa.gfx`
- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/012_african_union_l_english.yml`
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`
- `docs/events/012_africa_foundation.md`

## Missing Or Stale Country Package Surfaces

- `BON`, `HYR`, `BIR`, and `SAO` do not have tag-specific high-chaos capstone focuses in `common/national_focus/012_africa_authority_focus.txt`. The first 11 high-chaos actors do. This is a country-package depth gap, but adding four capstones would require focus rewards, localisation, AI, balance, and route review, so I did not patch it as a sidecar fix.
- The 25 created tags still use shared regional-authority and high-chaos companion trees rather than fully bespoke country focus trees.
- Expanded historical authority matrix tags remain dossier/office content rather than complete country packages.
- I did not create new country packages or route systems.

## Map And State Setup Issues

- Fixed duplicate one-state seats for `BON` and `BIR`.
- Current 25 seat constants in both `012_africa_effects.txt` and `012_africa_triggers.txt` are unique after the patch.
- `BON` now uses state `888` / Lusambo and province `2024`.
- `BIR` now uses state `770` / Malawi and province `12986`.
- Remaining map risk: I did not run a full state-by-state balance pass for supply hubs, railways, resources, ports, airbases, or victory-point quality beyond validating the moved OOB provinces belong to the moved states.

## Politics, Leaders, Portraits, Flags, Advisors, And Parties

- No opposite-gender portrait/name-pool issue found. These actors use institutional names, council names, or explicit nonhuman/supernatural names rather than random personal leader pools.
- `BON`, `HYR`, `BIR`, and `SAO` now classify statically as special chaos and actual nonhuman/supernatural actors even before setup flags are applied.
- Party localisation exists for all 25 target tags.
- Advisor/staff generation was spot-checked through setup helper references, not deeply rebalanced.

## Focus, Decision, Idea, And Asset Issues

- Focus loading is present and appropriate by role flag.
- The missing capstone gap for `BON`, `HYR`, `BIR`, and `SAO` remains.
- Role ideas `africa_regional_authority_spirit` and `africa_high_chaos_actor_spirit` are used through setup helpers.
- Portrait sprite references for the Event 012 leader portraits resolve in `interface/012_africa.gfx`; `GHP` continues using `GFX_portrait_independence_wave_gorilla_chair`.
- No asset files were created or converted.

## Starting Military, Technology, Industry, Supply, And Production

- All 25 tags have static land OOB starts.
- The two moved actors have OOB locations inside their new states:
  - `BON`: state `888`, province `2024`.
  - `BIR`: state `770`, province `12986`.
- Naval/air OOB coverage was not expanded; existing coastal/air-capable actors keep their current split OOBs.
- Production-line depth remains shared setup/focus/AI driven rather than bespoke per-country production histories.

## AI And Playability Issues

- `common/ai_strategy/012_africa.txt` includes grouped and tag-specific AI coverage for all 25 target tags.
- `BON`, `HYR`, `BIR`, and `SAO` have AI posture entries but not tag-specific focus capstones, so their playable identity is thinner than the first 11 high-chaos actors.
- Targeted scenario validation remains open for the parent goal.

## Meaningful Validation Run

- Verified all 25 target tags have tag registration, country files, history files, static land OOBs, and country localisation keys.
- Verified all 25 target tags have root/ideology/medium/small `.tga` flag families.
- Verified both Event 012 seat-constant tables have 25 entries and no duplicate state ids.
- Verified `BON` and `BIR` moved OOB province ids belong to their new vanilla state files.
- Verified `BON`, `HYR`, `BIR`, and `SAO` now appear in both shared classifier trigger lists.
- Verified `BON`, `HYR`, `BIR`, and `SAO` have zero tag-specific focus capstone hits, which is recorded as a remaining depth issue rather than patched.
- Ran `git diff --check` on the files touched by this pass.

## Skipped Meaningful Validation

- No game launch or in-game scenario run.
- No full focus-tree, decision, achievement, or scripted GUI audit.
- No visual QA for flags/portraits.
- No full map-supply balance pass.

## Remaining Risks And Blockers

- Four later high-chaos actors still need tag-specific companion-tree capstones if the parent wants parity with the first 11 Bestiary actors.
- Country packages remain shared-tree packages, not fully bespoke country routes.
- Route-specific consequences beyond current dossier slot families remain an Event 012 blocker.
- Targeted scenario validation remains an Event 012 blocker.
- The worktree contains unrelated dirty files, including Event 010 and concurrent Event 012 surfaces. I did not revert or modify Event 010 files.
