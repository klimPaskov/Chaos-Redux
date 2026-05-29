# Soviet Collapse Focus Reward Idea-Spam Audit Handoff

Date: 2026-05-29
Subagent scope: Soviet Collapse focus trees only, with small-patch permission.

## Files Audited

| File | Focus blocks | Notes |
| --- | ---: | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | 501 | Includes Ukraine, Belarus, Moldova, Kazakhstan, regional republic packages. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 1005 | Includes high-chaos splinters and tag-specific trees. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 128 | Includes Construction Directorate and factory successor packages. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 64 | Ancient restoration successor packages. |

Related files inspected: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, `common/ideas/005_soviet_collapse_ideas.txt`, `common/script_constants/005_soviet_collapse_constants.txt`, and `localisation/english/005_soviet_collapse*.yml`.

## High-Priority Fixes Made

| Priority | Issue | Patch |
| --- | --- | --- |
| High | Repeatable CFR decisions re-added static ideas every reuse through helper effects. | Guarded `cfr_construction_mandates` in `soviet_collapse_apply_cfr_survey_unfinished_sites` and `cfr_housing_ration_boards` in `soviet_collapse_apply_cfr_reconstruction_contracts`. |
| High | Nineteen custom-splinter doctrine focuses could re-add each tag's starting/internal-faction idea even when the setup helper already added it. | Added `NOT = { has_idea = ... }` guards around each identity idea inside `soviet_collapse_apply_custom_splinter_doctrine_identity`. |

Changed file: `common/scripted_effects/005_soviet_collapse_effects.txt`.

## Changed Helper Effects and Affected Identifiers

| Helper effect | File/line after patch | Direct callers | Before | After |
| --- | --- | --- | --- | --- |
| `soviet_collapse_apply_cfr_survey_unfinished_sites` | `common/scripted_effects/005_soviet_collapse_effects.txt:9370` | Repeatable decision at `common/decisions/005_soviet_collapse_decisions.txt:4608` | Re-applied `cfr_construction_mandates` on every use. | Adds the idea only if absent, while still advancing CFR site depth and construction payoff. |
| `soviet_collapse_apply_cfr_reconstruction_contracts` | `common/scripted_effects/005_soviet_collapse_effects.txt:9383` | Repeatable decision at `common/decisions/005_soviet_collapse_decisions.txt:4669` | Re-applied `cfr_housing_ration_boards` on every use. | Adds the idea only if absent, while still advancing CFR contract depth and construction payoff. |
| `soviet_collapse_apply_custom_splinter_doctrine_identity` | `common/scripted_effects/005_soviet_collapse_effects.txt:12943` | 19 `*_doctrine` focuses in `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Re-added setup/internal identity ideas for all handled tags. | Keeps doctrine rewards but avoids duplicate idea application. |

Changed focus ids, via helper behavior only: `FTH_doctrine`, `BSC_doctrine`, `TNC_doctrine`, `ALA_doctrine`, `BBH_doctrine`, `KRS_doctrine`, `UDC_doctrine`, `SDZ_doctrine`, `GAC_doctrine`, `DHC_doctrine`, `KHC_doctrine`, `FEV_doctrine`, `SZA_doctrine`, `UWD_doctrine`, `MRC_doctrine`, `IUL_doctrine`, `BAC_doctrine`, `ARD_doctrine`, `NLC_doctrine`.

Guarded idea ids: `fth_internal_factions`, `bsc_internal_factions`, `tnc_oasis_bureau_rivalries`, `ala_steppe_congress_rivalries`, `bbh_commune_war_councils`, `krs_sailors_assembly`, `udc_internal_factions`, `sdz_internal_factions`, `gac_internal_factions`, `dhc_internal_factions`, `khc_stanitsa_committee_rivalries`, `fev_liaison_office_tensions`, `sza_city_guard_compromises`, `uwd_manager_officer_rivalries`, `mrc_pass_confederation_rivalries`, `iul_tatar_bashkir_committees`, `bac_refugee_archive_tensions`, `ard_convoy_officer_tensions`, `nlc_scientific_refuge_council`.

Localisation keys changed: none.

Icon ids changed: none.

## Deep Reward Audit Findings

| Surface | Finding | Risk | Recommendation |
| --- | --- | --- | --- |
| `soviet_collapse_update_consolidated_republic_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5215` | Clears staged idea families before applying the current stage. It appears in many helper reward chains. | Scanner-noisy but structurally safe; not duplicate idea spam by itself. | Keep as consolidated updater. Avoid replacing with direct focus idea adds. |
| `soviet_collapse_check_republic_recovery` around `common/scripted_effects/005_soviet_collapse_effects.txt:4117` | Adds `soviet_collapse_emergency_administration_stabilized` after removing startup disorder. | Gated by startup/mitigated idea state, so not a repeatable focus stack issue. | No patch. |
| CFR repeatable helpers at `common/scripted_effects/005_soviet_collapse_effects.txt:9370` and `:9383` | Reusable decisions could repeatedly apply the same idea ids. | Real idea-spam surface. | Patched with `has_idea` guards. |
| Custom splinter doctrine helper at `common/scripted_effects/005_soviet_collapse_effects.txt:12943` | Duplicated many setup/internal faction idea ids already added by setup helpers around `common/scripted_effects/005_soviet_collapse_effects.txt:14564-15102`. | Real duplicate focus reward surface. | Patched with per-idea `has_idea` guards. |
| Endgame generic reward trio | 10 focuses call all of `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_depot_and_supply_control`, and `soviet_collapse_apply_focus_military_consolidation`. | Cadence is broad and generic for high-chaos endpoint lore. | Needs route-specific endpoint rewards in the parent rework rather than a small helper guard. |

Endgame generic-trio focus ids: `FTH_endgame` (`custom_splinters.txt:1186`), `KRS_endgame` (`:10045`), `FEV_endgame` (`:17236`), `SZA_endgame` (`:18416`), `IUL_volga_ural_endurance` (`:21717`), `IUL_endgame` (`:21971`), `BAC_amur_commune_endurance` (`:23016`), `BAC_endgame` (`:23105`), `ARD_arctic_port_endurance` (`:24194`), `ARD_endgame` (`:24290`).

## Route Coverage Table

| Required route area | Current coverage | Audit result |
| --- | --- | --- |
| Construction Directorate major civilian construction payoff | CFR tree has crane/site committee/contract/cities/rails/factories/protectorate/endgame branches in `005_soviet_collapse_factory_successors.txt:33-1094`; repeatable construction decisions call CFR helpers. | Strongest match to requested direction. Patched repeatable idea spam; civilian payoff depth remains present. |
| Dead Soldiers Congress war goals, cores, and zombie-like expansion | DSC tree exists at `005_soviet_collapse_custom_splinters.txt:2725-3246` with roll-call, revenant staff, grave ordnance, lost armies, soldier road, and end-state branches. | Thematic coverage exists. Needs parent-level review of actual cores/war goals versus lore promises; no safe small patch made. |
| Pale Railway rails and supply | PRA tree exists at `005_soviet_collapse_custom_splinters.txt:1220-1749` with timetable law, station guard, mobile workshops, armored train schools, corridors, junction claims, and rail endpoints. | Coverage matches requested rails/supply identity. No duplicate idea issue found in this route. |
| Naval/directorate tags naval/logistics | KRS, FEV, ARD, NRF, and related custom-splinter helpers award navy/logistics resources; KRS/FEV/ARD doctrine helper branches now guard identity ideas while preserving convoy/navy rewards. | Coverage exists but some endpoints still use generic reward trio. |
| Chaos countries tag-specific expansion, decisions, templates, cores/claims/war goals, factories, aggressive AI | 19 custom-splinter doctrine route hooks are tag-specific and there are many tag-specific trees. | Breadth exists, but reward cadence still leans on shared helpers. Parent rework should prioritize endpoint war-goal/core/template review per tag. |
| Ukraine geometry and depth | 83 Ukraine focuses, x range 4-34, y range 0-18, no duplicate coordinates, no missing reciprocal mutual exclusions. | Geometry is broad and busy but mechanically clean in this audit. Pathlines may still look crossed due wide political/military/industrial interleaving. |
| Belarus geometry and depth | 53 Belarus focuses, x range 3-28, y range 0-16, no duplicate coordinates, no missing reciprocal mutual exclusions. | Mechanically clean in this audit. Several long OR-gated links can still make pathlines visually busy. |

## Missing or Simplified Content List

| Area | Missing or simplified content | File/id references |
| --- | --- | --- |
| High-chaos endpoint payoff | Several endgames still use the same generic recognition/depot/military helper trio instead of tag-specific final mechanics. | Listed in Deep Reward Audit Findings. |
| Expansion verification | The requested "not OP/aggressive enough" goal needs a tag-by-tag check of decisions, cores, claims, war goals, and AI weights, not only focus reward parsing. | Start with DSC (`custom_splinters.txt:2725`), PRA (`:1220`), KRS (`:8842` approx route block), CFR (`factory_successors.txt:33`). |
| Ukraine/Belarus visual layout polish | No coordinate duplicates or reciprocal mutex defects found, but both trees remain wide enough that in-game pathline readability should be visually checked. | Ukraine focus ids prefix `ukr_soviet_collapse_`; Belarus focus ids prefix `blr_soviet_collapse_`. |

## Icon Coverage Table

| Check | Result |
| --- | --- |
| Focuses without `icon` in audited focus files | 0 |
| Referenced focus icon ids without interface definitions | 0 |
| Top repeated icons | Reuse exists, max observed count 4 for individual icon ids such as `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, and `GFX_focus_IUL_supply`. |
| Patch impact | No icon ids changed. |

## Localisation and Reward Mismatch List

| Check | Result |
| --- | --- |
| Missing focus name localisation among 1698 audited focuses | 0 |
| Missing focus desc localisation among 1698 audited focuses | 0 |
| Reward/name mismatch found in patched helpers | No localisation mismatch introduced; patched helpers only prevent repeated identical idea application. |
| Potential mismatch to review manually | Endgame focus descriptions should be checked against route-specific rewards where generic trio helpers remain. |

## AI Behavior Gaps

| Gap | Evidence | Recommendation |
| --- | --- | --- |
| All audited focuses have `ai_will_do`, but aggression may still be weak. | Mechanical audit found 0 focuses without `ai_will_do`; user goal says chaos countries are not aggressive enough. | Parent rework should inspect AI factors and decision AI for expansion, especially DSC/PRA/KRS/FEV/ARD and CFR protectorate routes. |
| Generic endpoint reward helpers can make AI route outcomes feel similar. | 10 endgame/endpoint focuses use the same recognition/depot/military trio. | Replace with route-aware endpoint AI and effects in a broader pass. |

## Validation Run

Commands run:

```bash
python3 - <<'PY'
from pathlib import Path
p=Path('common/scripted_effects/005_soviet_collapse_effects.txt')
depth=0
for n,line in enumerate(p.read_text(errors='ignore').splitlines(),1):
    depth += line.count('{') - line.count('}')
    if depth < 0:
        print('negative depth', n)
        break
else:
    print('final depth', depth)
PY
rg -n '<=|>=' common/scripted_effects/005_soviet_collapse_effects.txt
git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_soviet_collapse_focus_reward_idea_spam_audit_handoff.md
```

Results:

| Check | Result |
| --- | --- |
| Brace depth | `final_depth=0`, `min_depth=0`, no negative depth lines in the four audited focus files and `common/scripted_effects/005_soviet_collapse_effects.txt`. |
| Unsupported comparison operator search | No matches in the audited focus files or related Soviet Collapse effects/triggers/decisions/ideas/constants files. |
| `git diff --check` | Passed for `common/scripted_effects/005_soviet_collapse_effects.txt` and this handoff. |

## Skipped Validation and Why

No in-game validation was run. This subagent task was a static focus/helper audit and small patch; the parent remains responsible for loading the mod and route-play validation.

## Remaining Route Risks

1. Tag-specific depth is broad but not consistently endpoint-distinct; the 10 generic-trio endpoints should be the first parent rework target.
2. Requested chaos-country aggression needs decision AI and war-goal/core/claim behavior validation beyond focus parsing.
3. Ukraine and Belarus are mechanically clean for duplicate coordinates and reciprocal mutual exclusions, but in-game visual pathline readability still needs a screenshot/layout pass.
4. No separate broad redesign patch was attempted because the task explicitly limited this subagent to audit plus small high-confidence fixes.

Plan handoff path: this file. No separate broad rewrite plan was created.
