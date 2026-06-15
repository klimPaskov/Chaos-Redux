# Event 010 Death Focus Tree Audit Handoff

Supersession note: this handoff predates the 26-node focus-tree expansion and the remaining-route implementation. Its seven-focus tree findings and Dark Methods/Black Oath conclusions are superseded by `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md`, `docs/plans/010_death_plans/improvement_loop_remaining_routes_addendum.md`, and the current Event 010 files.

## Summary

Audited `common/national_focus/010_death_focus_tree.txt` against the Event 010 Death specs and current implementation surfaces. I applied three tiny wiring fixes:

- `common/scripted_effects/010_death_effects.txt`: `death_setup_country` now explicitly loads `death_focus_tree` when DTH is first set up.
- `interface/010_death.gfx`: added `_shine` sprites for all seven Death focus icons.
- `localisation/english/010_death_l_english.yml`: added `death_focus_tree: "Death"` for the runtime load-tree tooltip.

Audit-time finding, now resolved: the then-implemented tree was a compact seven-focus mechanic ladder, not the multi-lane compact custom tree described by the source spec. The follow-up plan at `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md` was later implemented and supersedes the gap table below.

## Route Coverage

| Required route | Audit-time route or focus branch | Audit-time status | Notes |
| --- | --- | --- | --- |
| Quiet origin / opening trunk | `death_shroud_whispers` | Superseded simplification | Spec expected `The First Silence` and `A Country on the Island`; the audit-time focus only added spread pressure and recorded origin evolution. |
| Shroud lane | Partly `death_shroud_whispers` | Superseded gap | No audit-time focuses existed for report delay, investigation chance, or report variants. |
| Island spread / Hunger lane | `death_hunger_shore`, `death_wasteland_roads` | Superseded simplification | Audit-time rewards increased spread pressure and could trigger one coastal jump after reveal; low-pop target preference and report-risk tradeoff were added later. |
| Weak/strong host thresholds | `death_mourning_host`, `death_black_census_focus` | Superseded partial | Audit-time focuses checked 600/800 chaos thresholds and spawned one host if possible, but the fuller Host lane was added later. |
| Black census counters | `death_black_census_focus` | Superseded mismatch | Audit-time reward did not add or upgrade `death_black_census`; the implemented tree now gives this surface a lifecycle. |
| Public Death convergence | Scripted reveal, no focus | Superseded gap | The audit-time tree had no reveal convergence focus; the implemented tree now includes `death_public_death_focus`. |
| Wasteland road pressure | `death_wasteland_roads` | Superseded mismatch | Audit-time reward did not change wither progress, wasteland modifiers, road/supply pressure, or recaptured wasteland behavior; later helpers cover the lane. |
| Coastal lane | `death_wasteland_roads`, `death_last_shores_focus` | Superseded simplification | Audit-time tree lacked `Another Shoreline` / `No Ferry Returns` style lane behavior; later implementation added coastal cooldown and target handling. |
| Host lane | `death_mourning_host`, `death_black_census_focus` | Superseded simplification | Audit-time tree lacked `Ruin Host` / `Orders Without Breath` payoff; later implementation added host progression with tier gates. |
| Last Shores | `death_last_shores_focus` | Superseded thin implementation | Audit-time focus existed but had fewer prerequisite lanes; the implemented tree now proves the post-reveal lane capstones. |
| Whole-world-consumed | `death_world_consumed_focus` | Retained | Correctly gated by `death_whole_world_consumed` and fires the final helper. |
| Dark Methods | Not exposed in focus tree | Correct boundary | The route remains outside the DTH focus tree and is implemented as living-country decisions. |
| Black Oath / Herald | Not exposed in focus tree | Correct boundary | The route remains outside the DTH focus tree and is implemented as living-country decisions, cosmetic identities, ideas, and achievements. |

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

## Superseded High-Priority Fixes

1. The focus tree was expanded into the compact lane architecture from the spec.
2. `Public Death` exists as a real convergence focus.
3. Black Census, Wasteland Roads, and Host progression rewards modify their named mechanics through helpers/constants.
4. DTH focus AI is stage-aware through per-focus availability and modifiers tied to hidden, revealed, and world-end state.
5. Dark Methods and Black Oath remain outside the DTH focus tree and are implemented as their own full living-country routes.

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
- Syntax-risk check on touched Event 010 focus/effect/trigger/GFX files: balanced braces and no unsupported comparison operators.
- Localisation file still has UTF-8 BOM after the added `death_focus_tree` key.

Skipped full game boot/load validation because this audit environment only performed static repo checks.

## Remaining Route Risks

- The tree remains materially shallower than the accepted focus architecture in `docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md`.
- The current focus rewards mostly push existing scripted variables or one-off spawns; they do not yet create distinct replayable Death lanes.
- AI behavior is not route-aware enough for a debug-playable or scenario-playable DTH.
- Superseded by later implementation: Black Oath and Dark Methods now have completed living-country route coverage, and their assets are active behind route prerequisites.

## Plan Handoff

Follow-up plan written: `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md`.
