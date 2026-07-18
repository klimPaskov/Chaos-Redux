# Event 015 Localisation Final Audit

Status: **PASS after a narrow case-collision and prose-style patch**

Audit date: 2026-07-18  
Scope: current English localisation, Event 15 scripted localisation, and the linked event, focus, decision, mission, category, idea, character, achievement, country identity, Ledger UI, event-log, evolution, and super-event consumers.  
Workbook source used for alignment: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/spreadsheet_final_audit_2026_07_18.md`. The workbook was not edited.

## Final verdict

The final source has complete Event 15 English key coverage and no remaining P0-P2 localisation defect found by this audit. The nine Event 15-owned English files contain exactly **2,480 quoted definitions**, **2,480 exact unique keys**, and **2,480 case-folded unique keys**. The two shared Event 15 display keys bring the directly audited player-facing set to 2,482 definitions without changing the Event-owned 2,480 count.

The audit found two case-only localisation collisions. Uppercase cosmetic country keys were colliding with lowercase founding national-spirit IDs. The cosmetic keys remain stable and the two idea IDs now use explicit `_idea` suffixes. The patch changes no modifiers or gameplay outcome. Six player-facing definitions were also normalized to remove prohibited em-dash or semicolon constructions without changing requirements, costs, or results.

## Authoritative live inventory

| Surface | Current count | Coverage result |
| --- | ---: | --- |
| Events | 106 | 106 unique IDs; every public title, triggered/static description, option name, and Event 15 tooltip reference resolves |
| Hidden events | 12 | All 12 omit public title and description text by design |
| Focuses | 124 | All 124 title/description pairs and linked availability/effect tooltips resolve |
| Decisions | 121 | All title/description pairs and direct cost/requirement/result references resolve |
| Missions | 44 | All title/description pairs and direct result/failure references resolve |
| Decision categories | 9 | All category title/description pairs resolve |
| Ideas | 50 | All 50 title/description pairs resolve after the two founding-ID renames |
| Characters | 24 | All 24 character names and descriptions resolve |
| Advisor traits | 16 | All 16 trait title/description pairs resolve |
| Achievements | 14 | All 14 `_NAME`, `_DESC`, and custom achievement tooltip triplets resolve |
| Route identities | 5 | All cosmetic-name matrices, party identities, route labels, and formation outcomes resolve |
| Ledger GUI references | 25 | Every `text`, `buttonText`, and `pdx_tooltip` key in the Ledger GUI resolves |
| Scripted localisation | 35 defined texts | 35 unique names; all 246 `localization_key` references resolve |
| Super-events | 5 slots | Slots 96-100 each resolve title, quote, remark, and description: 20/20 keys |
| Paid military formations | 8 | All eight dynamic formation-name keys resolve and reach template/unit creation |

The hidden event IDs are `chaosx.nr15.205`, `.207`, `.214`, `.212`, `.216`, `.218`, `.220`, `.116`, `.150`, `.163`, `.164`, and `.165`.

## Definition, duplicate, missing, and orphan report

| English file | Quoted definitions | UTF-8 BOM | Final SHA-256 |
| --- | ---: | --- | --- |
| `015_utopia_manifesto_country_package_l_english.yml` | 218 | Yes | `f4e6ce0be0b37a44a56133141b9c8aed3cd30a38dfbcbf853c5a78f8040f2e09` |
| `015_utopia_manifesto_decision_completion_l_english.yml` | 676 | Yes | `070b00d6243c7e10c11d6709258a0cba54da9477599fdb73dbc803c5feb8e78f` |
| `015_utopia_manifesto_events_l_english.yml` | 503 | Yes | `fd1ddda9a374ac5a3bbce30bd6d61d8fe46eadba87473e32d6f560eae3f7a446` |
| `015_utopia_manifesto_evolution_consumption_l_english.yml` | 84 | Yes | `8205917030d34a204b95fb6fd198859b1e7c8b77acc1b8d242fcd46ebf8a92dc` |
| `015_utopia_manifesto_evolutions_l_english.yml` | 18 | Yes | `508786fb2a6d8b0b1efa51dca67467a8241c25d9aa141528c9e44b590b1d1c01` |
| `015_utopia_manifesto_focus_l_english.yml` | 349 | Yes | `cb27494bad4e6c0817cd4d80a0164f73086bdcaa9450428a9aefda902f357057` |
| `015_utopia_manifesto_ideas_l_english.yml` | 136 | Yes | `a19cbd8592e7c09c0e09fa75b01bd4238f632f055d29909ae7b8cfa25e1b548d` |
| `015_utopia_manifesto_l_english.yml` | 476 | Yes | `d8cbb572a479619a266289a509f3f5e2fd2304522d19058b57a4b5c2041423ec` |
| `015_utopia_manifesto_super_event_l_english.yml` | 20 | Yes | `8f14e4fb22578e942ba5019e1022032b12a794c464e61fcef8d7d01bb5527e32` |
| **Total** | **2,480** | **All nine** | |

- Missing key list: **none** across the audited Event 15 surfaces.
- Duplicate key list after patch: **none**, both exact-case and case-folded.
- Duplicate key list before patch:
  - `UTOPIA_MANIFESTO_CLOSED_ISLAND` collided with `utopia_manifesto_closed_island`.
  - `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` collided with `utopia_manifesto_practical_commonwealth`.
- Orphan localisation list: **none unaccounted**. Event keys have direct consumers. Focus, decision, mission, category, idea, character, cosmetic-tag, achievement, and modifier descriptions use their documented implicit engine suffixes. Blocked-cost and cost-tooltip variants are paired with their live custom-cost bases. Scripted-localisation branches and super-event slots are explicitly mapped.
- Malformed quoted-definition lines: **none**.
- Versioned `:0` definitions: **none**.

The shared files remain aligned and BOM-safe:

- `chaosx_gui_l_english.yml`: `6810c1c888a171926e2841de0b4366773b9e6490ddc6e01a7faca90dc86b691f`
- `chaosx_event_names_l_english.yml`: `ba57396a4e1b939f4e589ea38639694d6e9ab4c48f39df0b41c603be9d62421e`

## Case-collision correction

Before: 2,480 definitions, 2,478 case-folded unique keys, two collision groups.  
After: 2,480 definitions, 2,480 case-folded unique keys, zero collision groups.

The stable cosmetic display keys remain:

- `UTOPIA_MANIFESTO_CLOSED_ISLAND`
- `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH`

The founding national-spirit identifiers and implicit localisation pairs changed as follows:

- `utopia_manifesto_closed_island` -> `utopia_manifesto_closed_island_idea`
- `utopia_manifesto_closed_island_desc` -> `utopia_manifesto_closed_island_idea_desc`
- `utopia_manifesto_practical_commonwealth` -> `utopia_manifesto_practical_commonwealth_idea`
- `utopia_manifesto_practical_commonwealth_desc` -> `utopia_manifesto_practical_commonwealth_idea_desc`

Each new idea ID is present in the idea definition, route-institution clear list, route founding `add_ideas` branch, and matching title/description pair. Exact old founding-ID references no longer remain. Mitigated, failure, and final stages were already unique and were not renamed.

## Five route identities

| Public interpretation | Final country identity | Party identity |
| --- | --- | --- |
| Consent of Households | Voluntary Commonwealth | Household Cooperatives |
| Common Table | Union of Common Tables | Congress of Common Tables |
| Guardians of Measure | Commonwealth of Measure | Planning Movement |
| Closed Island | Closed Island | Service and Unity Movement |
| The Joke Understood | Practical Commonwealth | Humanist Reform Coalition |

Each cosmetic identity has base, definite, adjective, and four-ideology name/definite/adjective coverage: 75/75 keys. Hidden achievement wording does not expose the two hidden achievements before their conditions are met. No route wording was found that collapses the five political identities into one generic result.

## Ledger and dynamic text

The visible Ledger presents all four live constitutional values:

- Need: numeric value, last delta, and five scripted bands plus unread fallback.
- Plenty: numeric value, last delta, and five scripted bands plus unread fallback.
- Concord: numeric value, last delta, and five scripted bands plus unread fallback.
- Choice / Assignment: numeric Assignment value, last delta, and five scripted bands plus unread fallback.

The overview gives current component breakdowns for 10 Need inputs, 5 Plenty inputs, 9 Concord inputs, and 3 Assignment inputs. It also resolves current route, political organization, geography, current problem, next proof, and formation status. The remaining tabs use dynamic calling severities and policy adjustments, reserve score/band, district state and role, named case partner/state, case stage/method/integrity/support/expiry, League counts, and current state names.

Dynamic text opportunities: **no unresolved P0-P2 opportunity**. Existing variables, actor scopes, state names, cost values, timers, route names, and status enums are already used where a static value would become misleading. The event-log default actor maps Event 15 through `utopia_manifesto_latest_actor`, and the shared details/evolution mappings resolve Event 15 through `constant:utopia_manifesto_event.id`.

## Eight military formation names

`GetUtopiaManifestoMilitaryFormationName` maps all eight paid formation constants:

| Constant branch | Localisation key | Display name |
| --- | --- | --- |
| `citizen_watch` | `utopia_manifesto_military_formation_citizen_watch` | Citizen Watch |
| `worker_defense` | `utopia_manifesto_military_formation_worker_defense` | Workers' Defense Column |
| `engineer_corps` | `utopia_manifesto_military_formation_engineer_corps` | Commonwealth Engineer Corps |
| `service_formation` | `utopia_manifesto_military_formation_service_formation` | Household Service Formation |
| `professional_guard` | `utopia_manifesto_military_formation_professional_guard` | Small Professional Guard |
| `league_defense` | `utopia_manifesto_military_formation_league_defense` | League Defense Group |
| `auxiliary_column` | `utopia_manifesto_military_formation_auxiliary_column` | Auxiliary Service Column |
| `commonwealth_guard` | `utopia_manifesto_military_formation_commonwealth_guard` | Commonwealth Field Guard |

The scripted value is injected as `FORMATION_NAME` into all eight template-creation branches and all eight paid unit-creation branches. The citizen-watch fallback is also localised.

## Event Details and workbook alignment

Workbook SHA-256 remains `729e48a3135094d210b70e74ce3694ff0b66dbd5d2bc448051db931a41f4bd80`, exactly the audited workbook hash. Current source values match the authoritative row `Events!A16:M16` hashes from the spreadsheet handoff:

| Cell | Current source | Expected hash | Result |
| --- | --- | --- | --- |
| `B16` | `chaosx.event_name.15` | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` | Exact |
| `C16` | `chaosx.events_log.window.event_details.utopia_manifesto` | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` | Exact after decoding localisation `\\n` escapes to workbook LF characters |
| `D16` | Evolution 1 title + two LF + body | `c62381e7a169616993fc62127d7e720089dfb621aed36944fb6979cd1f021b9a` | Exact |
| `E16` | Evolution 2 title + two LF + body | `4dcb2f732af67a2e4730e62d3a65f189c80f9d480612d9c4bd8c6dfb78a47da7` | Exact |
| `F16` | Evolution 3 title + two LF + body | `c055f5f4025553464ee396e9a197298c1042a2938b1b1f5693b8f464b2a3bdd6` | Exact |
| `G16` | Evolution 4 title + two LF + body | `a359ce4d6c882d7a513bebeca6d710a2d96592b6b0c850d00a2d3e35fd0719c5` | Exact |
| `H16` | Evolution 5 title + two LF + body | `b14a3d96f6507efadd4490af9dd6737b05e5ab3b0e4c749320a8c1daa926c541` | Exact |

No workbook change or CSV export was required.

## Leakage and player-facing wording

No live Event 15 player-facing localisation, scripted localisation, Ledger GUI text key, or super-event surface contains:

- `World Tension Subsides`
- `world_tension_subsides`
- an `Event 015` placeholder
- visible `ID15` / `ID 15`
- a contradiction-meter widget, key, tooltip, or label
- a stale 43-mission count
- implementation-history wording such as newly added, reworked, hardcoded, previous version, or this update

`Event 015` remains only in source comments. Narrative uses of the ordinary word “contradiction” and the `GFX_report_event_utopia_manifesto_contradiction` report image are intentional story content, not a contradiction meter.

The player-facing punctuation/style scan is clean after the six-definition prose patch. No Event 15-owned English value retains an em dash, semicolon, TODO/TBD, placeholder, debug label, or dummy text.

## Scripted localisation issues

Scripted-localisation issue list: **none remaining**.

- 35 `GetUtopiaManifesto...` definitions, all unique.
- 246 localisation-key branches, all resolved.
- No direct `§` or `£` formatting characters in the scripted-localisation source.
- No broken nested `$KEY$` reference found. The only non-nested `$...$` placeholders are the expected `$ORDER$`, `$FIRST$`, and `$STATE$` parameters in the Necessary Ground war name.
- `015_utopia_manifesto_scripted_localisation.txt` is a script `.txt`, not a localisation `.yml`; its lack of BOM is not an encoding defect.

## Cross-surface mismatch notes

Cross-surface mismatch list after patch: **none**.

- Event name, Event Details, and all five evolutions agree with the workbook handoff.
- Five route interpretations agree with focus wording, Ledger route labels, party names, cosmetic identities, formation effects, and five super-event bodies.
- Decision/mission names, cost/requirement/result tooltips, and category names resolve against the current 121/44/9 inventory.
- Country character/advisor names and descriptions agree with the 24-character and 16-trait packages.
- Achievement display triplets agree with all 14 achievement IDs.

## Files and keys changed by this audit

Gameplay identifier/reference correction:

- `common/ideas/015_utopia_manifesto_ideas.txt`
  - `utopia_manifesto_closed_island` -> `utopia_manifesto_closed_island_idea`
  - `utopia_manifesto_practical_commonwealth` -> `utopia_manifesto_practical_commonwealth_idea`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`
  - Updated the two founding entries in `utopia_manifesto_clear_route_institution_idea_stages`.
  - Updated the Closed Island and Joke Understood founding `add_ideas` branches.
- `localisation/english/015_utopia_manifesto_ideas_l_english.yml`
  - `utopia_manifesto_closed_island` -> `utopia_manifesto_closed_island_idea`
  - `utopia_manifesto_closed_island_desc` -> `utopia_manifesto_closed_island_idea_desc`
  - `utopia_manifesto_practical_commonwealth` -> `utopia_manifesto_practical_commonwealth_idea`
  - `utopia_manifesto_practical_commonwealth_desc` -> `utopia_manifesto_practical_commonwealth_idea_desc`

Player-facing prose normalization:

- `localisation/english/015_utopia_manifesto_events_l_english.yml`
  - `chaosx.nr15.54.d`
  - `chaosx.nr15.54.c.tt`
  - `chaosx.nr15.63.a.tt`
- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
  - `mission_utopia_need_case_expiry_failure_tt`
  - `decision_utopia_offer_stewardship_autonomy_desc`
  - `decision_utopia_offer_stewardship_autonomy_effect_tt`

Display before and after:

- Before, case-insensitive lookup could make “Closed Island” / “Practical Commonwealth” cosmetic names compete with “The Closed Island” / “The Practical Commonwealth” national-spirit names.
- After, cosmetic country identities retain their stable uppercase keys while the founding national spirits have unambiguous `_idea` keys.
- Before, six definitions used prohibited em-dash or semicolon sentence joins.
- After, the same facts are split into direct sentences. Costs, requirements, actors, targets, timers, and effects are unchanged.

Dynamic localisation added or fixed: no new dynamic branch was required. The existing dynamic formation-name and Ledger/state/actor mappings were validated. The fix was identifier disambiguation plus prose normalization.

## Frozen source anchors

Relevant final source hashes after the identity-effect `.none` -> `.unset` correction and this localisation patch:

- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`: `aef6d312c246b11af26ab126ca372f0bb9d654303573e254a1548f7e5fce5e48`
- `common/ideas/015_utopia_manifesto_ideas.txt`: `0f29203805f9ba9902f3615690cb019f0517dcd7761447745e7182472bfa20e3`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`: `6fb28ba9a2eb20b3f1c8cfc0e11f7b850446796d19e4414196f632045c5df1d9`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`: `36cd2cc4c245f19a2a8f6bb7660ccaa77e630a681504cd50a1184180a8083c63`
- `events/015_utopia_manifesto.txt`: `32c7993f1ad23f74fcddedc81f119e367b038bc631b6ae48558360a940ece29f`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`: `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05`
- Main decision file: `e58b33608294970dc0f383c88c4660f36119800990bd90c5b08b7ec0c5556f28`
- Evolution-consumption decision file: `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4`
- Prefire decision file: `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347`

## Meaningful validation and limits

Meaningful validation run:

- Independent block-aware inventory parse for 106 events / 12 hidden, 124 focuses, 121 decisions, 44 missions, 9 categories, 50 ideas, 24 characters, 16 traits, and 14 achievements.
- Surface-specific implicit and explicit key-resolution checks. Missing lists were empty for events, focuses, decisions/missions, categories, ideas, characters, traits, achievements, cosmetic matrices, Ledger UI, scripted localisation, super-events, and formation names.
- Case-insensitive duplicate audit before and after the identifier patch.
- Exact old/new idea-ID consumer trace through definition, clear, and add effects.
- Exact workbook/value SHA comparison for Event name, Event Details, and five evolution cells.
- Hidden-event title/description exposure and prohibited-runtime-string scans.
- GUI source review for all 25 Ledger text/button/tooltip keys and their declared dimensions.

Skipped meaningful validation:

- No rendered Ledger overflow/click-region validation was available in this subagent tool surface. Source dimensions and all text bindings were inspected, and no confirmed overflow defect was found, but this is not pixel-render proof.
- No in-game runtime was run. The parent workflow owns integrated runtime review.
- The shared Thomas More quotation was retained unchanged and was not independently re-researched in this localisation pass. Its exact quotation/source wording therefore remains dependent on the existing super-event text-research handoff.

File encoding concerns: **none**. All nine Event 15-owned English files and both shared English files audited here retain UTF-8 BOM.

Recommended fixes: **none remaining at P0-P2**.

Unresolved wording decisions: none introduced by this audit. The quotation-source limitation above is evidence scope, not a requested wording change.

Plan handoff path: this file. No separate missing-mechanic plan was required.

Simplifications, omissions, and blockers: no localisation fallback or gameplay simplification was used. The two validation limitations above are explicit; neither concealed a known defect.

Skills applied: `chaos-redux-events`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `chaos-redux-super-events`, and `chaos-redux-subagents`, with the required offline Paradox wiki and vanilla documentation references.
