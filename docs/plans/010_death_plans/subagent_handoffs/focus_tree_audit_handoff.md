# Event 010 Death Focus Tree Audit Handoff

## Summary

Audited `common/national_focus/010_death_focus_tree.txt` against the Event 010 Death specs and current implementation surfaces. I applied three tiny wiring fixes:

- `common/scripted_effects/010_death_effects.txt`: `death_setup_country` now explicitly loads `death_focus_tree` when DTH is first set up.
- `interface/010_death.gfx`: added `_shine` sprites for all seven Death focus icons.
- `localisation/english/010_death_l_english.yml`: added `death_focus_tree: "Death"` for the runtime load-tree tooltip.

The broader result is still an audit finding: the implemented tree is a compact seven-focus mechanic ladder, not the multi-lane compact custom tree described by the source spec. I wrote the follow-up plan at `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md`.

## Route Coverage

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Quiet origin / opening trunk | `death_shroud_whispers` | Simplified | Spec expects `The First Silence` and `A Country on the Island`; current focus only adds spread pressure and records origin evolution. See `common/national_focus/010_death_focus_tree.txt:28` and spec lines `184-191`. |
| Shroud lane | Partly `death_shroud_whispers` | Missing as a lane | No focuses for report delay, investigation chance, or report variants. Spec lines `193-212`. |
| Island spread / Hunger lane | `death_hunger_shore`, `death_wasteland_roads` | Simplified | Current rewards increase spread pressure and can trigger one coastal jump after reveal; no low-pop target preference or report-risk tradeoff. See focus lines `43-57`, `91-108`; spec lines `214-233`. |
| Weak/strong host thresholds | `death_mourning_host`, `death_black_census_focus` | Partial | Focuses check 600/800 chaos thresholds and spawn one host if possible, but the tree does not expose a full Host lane or template/AI progression. See focus lines `59-89`, `110-139`; constants at `common/script_constants/010_death_constants.txt:71`. |
| Black census counters | `death_black_census_focus` | Simplified/mismatch | Focus title/desc promise a register, but reward only adds pressure and conditionally spawns a stronger host. It does not add or upgrade `death_black_census` idea despite the idea existing at `common/ideas/chaosx_ideas.txt:150`. |
| Public Death convergence | Scripted reveal, no focus | Missing from tree | Spec requires a reveal convergence focus after mainland reveal. Current tree jumps from two early branches directly to Last Shores. Spec lines `255-257`. |
| Wasteland road pressure | `death_wasteland_roads` | Simplified/mismatch | Focus text says Death learns to move through wasteland, but reward does not change wither progress, wasteland modifiers, road/supply pressure, or recaptured wasteland behavior. See focus lines `91-108`; spec lines `280-299`. |
| Coastal lane | `death_wasteland_roads`, `death_last_shores_focus` | Simplified | No `Another Shoreline` / `No Ferry Returns` style lane, cooldown change, target pool change, or counter-decision interaction. Spec lines `259-278`. |
| Host lane | `death_mourning_host`, `death_black_census_focus` | Simplified | No `Ruin Host` / `Orders Without Breath` route payoff; Death aggression mainly comes from ideas and scripted world-end behavior. Spec lines `301-319`. |
| Last Shores | `death_last_shores_focus` | Present but thin | Correctly AND-gated behind `death_wasteland_roads` and `death_black_census_focus`; availability requires world-end active or startable. See focus lines `141-172`. |
| Whole-world-consumed | `death_world_consumed_focus` | Present | Correctly gated by `death_whole_world_consumed` and fires the final helper. See focus lines `174-188`; trigger lines `common/scripted_triggers/010_death_triggers.txt:201`. |
| Hidden/queued Dark Methods | Not exposed in focus tree | Queued/hidden | This matches `docs/events/010_death.md:35` and `:53`; no half-visible Death focus branch found. |
| Hidden/queued Black Oath / Herald | Not exposed in focus tree | Queued/hidden | `GFX_decision_death_black_oath` is registered but no visible decision/focus route uses it; docs explicitly queue it. See `interface/010_death.gfx:10`, `docs/events/010_death.md:35`, `:54`. |

## Icon Coverage

| Focus id | Icon id | Base sprite | Shine sprite | DDS file | Status |
| --- | --- | --- | --- | --- | --- |
| `death_shroud_whispers` | `GFX_focus_death_shroud_whispers` | Present | Added | Present | Fixed |
| `death_hunger_shore` | `GFX_focus_death_hunger_shore` | Present | Added | Present | Fixed |
| `death_mourning_host` | `GFX_focus_death_mourning_host` | Present | Added | Present | Fixed |
| `death_wasteland_roads` | `GFX_focus_death_wasteland_roads` | Present | Added | Present | Fixed |
| `death_black_census_focus` | `GFX_focus_death_black_census` | Present | Added | Present | Fixed |
| `death_last_shores_focus` | `GFX_focus_death_last_shores` | Present | Added | Present | Fixed |
| `death_world_consumed_focus` | `GFX_focus_death_world_consumed` | Present | Added | Present | Fixed |

Sprite definitions are in `interface/010_death.gfx:12-25`. DDS files exist under `gfx/interface/goals/death/`.

## Localisation And Reward Mismatches

| Focus id / key | Status | Finding |
| --- | --- | --- |
| `death_focus_tree` | Fixed | Added missing tree-id localisation at `localisation/english/010_death_l_english.yml:15` for explicit `load_focus_tree`. |
| All seven focus ids | Covered | Name and `_desc` keys exist at `localisation/english/010_death_l_english.yml:92-105`. |
| `death_black_census_focus` | Mismatch | Text promises a register of consumed places; reward does not add/upgrade `death_black_census` or present counters. |
| `death_wasteland_roads` | Mismatch | Text promises wasteland movement/road identity; reward only adds pressure and attempts a coastal jump if revealed. |
| `death_hunger_shore` | Thin | Text implies island/shore target learning; reward only adds pressure and records island-report evolution. |
| `death_last_shores_focus` | Acceptable but thin | It starts or reinforces world-end footholds, but is a single focus for the whole Last Shores branch. |

## AI Behavior Gaps

- Every focus has an `ai_will_do`, but the weights are mostly flat (`common/national_focus/010_death_focus_tree.txt:40`, `:56`, `:107`, `:187`).
- There is no Death-specific `common/ai_strategy` entry found for DTH route behavior.
- Current focus AI does not implement spec priority for hidden-stage Shroud/Hunger/Census, post-reveal Wasteland/Coastal/Host selection, or pushed-back coastal recovery. Spec lines `340-356`.
- Last Shores and World Consumed are availability-gated, so the AI should not take terminal focuses early; that part is safe.

## Prerequisites, Availability, Loading, And Syntax

- `death_last_shores_focus` uses two separate prerequisite blocks, so it is an AND gate as intended (`common/national_focus/010_death_focus_tree.txt:148-149`).
- No OR-prerequisite ambiguity found in the current tree.
- No duplicate focus coordinates found.
- DTH history defines templates but no deployed divisions, matching the no-starting-army requirement (`history/units/DTH_1936.txt:1-36`).
- DTH history itself does not load a focus tree (`history/countries/DTH - Death.txt:1-25`); this is now covered by `death_setup_country` at `common/scripted_effects/010_death_effects.txt:95`.

## High-Priority Fixes

1. Expand the focus tree from the current seven-focus ladder into the compact lane architecture from the spec, or explicitly supersede that spec if the seven-focus version is now accepted.
2. Add a real `Public Death` convergence focus or document why reveal remains purely scripted.
3. Give Black Census, Wasteland Roads, and Host progression rewards that actually modify their named mechanics, preferably through existing helpers/constants.
4. Add route-aware DTH AI strategy or stronger per-focus AI modifiers tied to hidden/revealed/world-end state.
5. Keep Dark Methods and Black Oath hidden until their full route mechanics are implemented.

## Changed Files

- `common/scripted_effects/010_death_effects.txt`
- `interface/010_death.gfx`
- `localisation/english/010_death_l_english.yml`
- `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md`
- `docs/plans/010_death_plans/subagent_handoffs/focus_tree_audit_handoff.md`

## Changed Focus IDs

No focus ids were renamed or added.

## Route Behavior Before And After

- Before: DTH relied on the focus-tree `country` score and history/state timing; no explicit runtime `load_focus_tree` path existed for the event setup.
- After: first-time `death_setup_country` explicitly loads `death_focus_tree` with `keep_completed = no`.
- Before: focus base icons were registered, but available-focus shine sprites were missing.
- After: every implemented Death focus has a matching `_shine` sprite using the same DDS and `gfx/FX/buttonstate.lua`.

## Localisation Keys And Icon IDs Changed

- Added localisation key: `death_focus_tree`.
- Added icon ids: `GFX_focus_death_shroud_whispers_shine`, `GFX_focus_death_hunger_shore_shine`, `GFX_focus_death_mourning_host_shine`, `GFX_focus_death_wasteland_roads_shine`, `GFX_focus_death_black_census_shine`, `GFX_focus_death_last_shores_shine`, `GFX_focus_death_world_consumed_shine`.

## Validation

- Focus/localisation/GFX cross-check: 7 focus ids, no duplicate ids, no missing focus name/desc keys, `death_focus_tree` loc present, no missing base or shine sprites, and all focus DDS paths exist.
- Route prerequisite check: no OR-prerequisite blocks in current tree; `death_last_shores_focus` uses separate prerequisites for AND gating.
- Syntax-risk check on touched Event 010 focus/effect/trigger/GFX files: balanced braces and no `<=` / `>=` operators.
- Localisation file still has UTF-8 BOM after the added `death_focus_tree` key.

Skipped full game boot/load validation because this audit environment only performed static repo checks.

## Remaining Route Risks

- The tree remains materially shallower than the accepted focus architecture in `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md`.
- The current focus rewards mostly push existing scripted variables or one-off spawns; they do not yet create distinct replayable Death lanes.
- AI behavior is not route-aware enough for a debug-playable or scenario-playable DTH.
- Black Oath/Dark Methods are correctly hidden/queued, but the registered `decision_death_black_oath` asset may look like implemented coverage unless docs stay clear.

## Plan Handoff

Follow-up plan written: `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md`.
