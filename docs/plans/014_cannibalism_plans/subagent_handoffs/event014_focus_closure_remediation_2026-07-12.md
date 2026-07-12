# Event 014 Focus-Closure Remediation Handoff

Date: 2026-07-12

Owner: `event014_focus_closure_planner`

Source addendum: `docs/plans/014_cannibalism_plans/improvement_loop/2026-07-12_event014_focus_closure_addendum.md`

## Status

The H-01 scoring/MTTH implementation, H-02 four-surface terminal hunt, M-01 Wendigo progression, H-03 normalization, focus/pulse/lifecycle wiring, six sprite registrations, and late English localisation are implemented and ready for parent-led focus, country-package, localisation, and event-completion re-audits.

The six registered focus-closure DDS files are explicitly pending from the separately owned `event014_closure_assets` package. No fallback, shared icon, placeholder, or transform-only substitute was introduced. This handoff therefore does not claim binary-asset completion.

No commit was created.

## H-01: reusable target scoring and AI consumers

Implemented exact scorer IDs:

- `cannibalism_unified_target_scorer`
- `cannibalism_wendigo_target_scorer`

Implemented exact MTTH IDs in `common/mtth/014_cannibalism_mtth.txt`:

- `cannibalism_unified_target_decision_weight`
- `cannibalism_wendigo_target_decision_weight`

The scorer contract is explicit: scorer target/default scope is the candidate and scorer `FROM` is the initiating actor. Targeted decisions and their MTTH weights use mirrored `_from_decision` hard-validity and relationship wrappers because their default/`ROOT` scope is the actor and `FROM` is the candidate. Final review caught and corrected an earlier reversal of this contract before handoff.

Hard eligibility rejects self, allies/faction members/subjects, capitulated or nonexistent countries, Event 014 cannibals, actual nonhumans, unusable population, per-operation target locks, a second hunt target, and countries without a proved war/adjacency/cell/corridor/post-lock route. Wasteland and unusable larder states cannot prove population, port, rail, prison, cell, or supply factors.

The exact score constants are in `common/script_constants/014_cannibalism_target_score_constants.txt`. Very-high population replaces the high-population factor; the other independent physical/logistical factors may stack. Score arrays are temporary, cleared before and after each consumer, and never stored as a global cache.

Exactly six unified targeted decisions now start AI weighting at zero and add `mtth:cannibalism_unified_target_decision_weight`, while preserving their narrower existing pools:

1. `cannibalism_unified_seed_major_enemy_army`
2. `cannibalism_unified_prepare_global_campaign`
3. `cannibalism_unified_issue_terror_ultimatum`
4. `cannibalism_unified_provoke_border_incident`
5. `cannibalism_unified_destroy_coalition_hub`
6. `cannibalism_unified_collapse_enemy_front`

`CBL_read_the_continental_weakness` applies the scored campaign priorities. The Wendigo focus consumer uses score-banded pre-lock priorities. The parent-owned patch to `cannibalism_activate_terminal_global_war` calls `cannibalism_wendigo_apply_scored_terminal_priorities` only for the Wendigo branch after leaving its faction; the ordinary global-war loop remains unchanged.

## H-02: terminal hunt

Implemented exactly four terminal-hunt surfaces:

- `cannibalism_wendigo_launch_terminal_hunt`
- `cannibalism_wendigo_terminal_hunt_mission`
- `cannibalism_wendigo_press_terminal_hunt`
- `cannibalism_break_wendigo_terminal_hunt`

The launch stores the single persistent `cannibalism_wendigo_terminal_hunt_target`, pays the authored Larder/Command Power/equipment costs, seeds 25 pressure, applies the target/defender state, and activates the 120-day mission. Pressing pays Larder, Command Power, infantry equipment, support equipment, and fuel for 25 pressure with a 30-day cooldown. Defender break pays manpower, Command Power, infantry equipment, and support equipment for 25 counterpressure with re-enable timing and contributor recording.

Success is target capitulation or target-capital control with 100 pressure. It grants exactly five transformation progress, records completion, and does not call world-end or mint a casualty receipt. Failure covers 100 counterpressure, broken route/no anchors, invalid actor/target, ended war, cancellation, and timeout; it subtracts exactly ten transformation progress and records failure. Ordinary success/failure preserves the original timed target lock until expiry; route break, terminal lock, actor removal, and global cleanup remove all pre-lock runtime.

`cannibalism_clear_wendigo_prelock_operation_runtime` clears the hunt, receipt, inherited-cell, recruitment-operation, and temporary cooldown state while retaining the original ZZZ country, live units, template structure, paid population history, Larder history, origin upgrades, commander traits, and lifetime outcome counters.

## M-01: Wendigo progression

### Enemy-death receipts and paid Pack muster

Receipt collection is initialized non-retroactively by `ZZZ_wendigo_count_the_winter_victories`. The existing Event 014 pulse samples only current enemies of the one live pre-lock Wendigo actor through `every_enemy_country`; no daily/weekly/monthly hook or whole-world country iteration was added. Each enemy keeps a casualty snapshot, remainder, and issued count. The threshold is 50,000 new military casualties, with a per-enemy cap of two and a held-pool cap of five. Counter resets discard stale remainder and never create a receipt. Receipt logic reads `casualties` only and never records Deaths or grants resources.

`cannibalism_muster_wendigo_pack_from_enemy_death_receipt` is a controlled-state decision. It requests exactly 100K population through the canonical recruitment consumption context, requires exact applied loss, records that loss once, pays one receipt, 200 Larder, 500 infantry equipment, and 100 support equipment, transfers 50K to manpower, and spawns one empty `Wendigo Pack`. The refactored `cannibalism_spawn_empty_wendigo_pack_batch` accepts a temporary batch: the existing paid trainer passes two and the receipt muster passes one. Neither caller unlocks ordinary queue recruitment.

### Structural progression

- Pack stage 1 adds recon support to the existing `Wendigo Pack`.
- Pack stage 2 adds engineer support.
- Pack stage 3 adds logistics support.
- Stage flags make every addition idempotent; no battalion or template reconstruction was introduced.
- Island Reavers gain recon only with inherited island knowledge and the live template.
- Siege Eaters gain artillery only with inherited siege knowledge and the live template.
- March Predation Column gains logistics only with inherited march knowledge and the live template.
- Lockhouse Column gains engineer only with inherited prison knowledge and the live template.
- `cannibalism_wendigo_bound_captain` and `cannibalism_wendigo_winter_hunt_captain` apply only to existing inherited host commanders/bound servants, exclude `ZZZ_hannibal_wendigo`, create no leader, and never coexist on one commander.
- `ZZZ_wendigo_all_inheritances_intact` opens/refreshes the second commander stage; the existing pulse also refreshes it so focus order cannot strand the promotion.

### Inherited winter cell

`cannibalism_activate_inherited_winter_cell` targets an ordinary current enemy with a live inherited Event 014 cell, usable population, and valid Wendigo score route. It pays all authored costs, applies `cannibalism_wendigo_inherited_cell_pressure` for 60 days, registers the target in the actor-owned active-cell array, and applies a 90-day target lock. If the target is the active hunt target, it adds the one-time 20 hunt pressure interaction and clamps it. It creates no cell, population loss, Larder, stockpile, unit, or war goal. Cleanup loops only the registered array.

### Focus and lifecycle wiring

The accepted existing-focus rows are wired without adding a focus:

- winter victories: receipt initialization/opening;
- original Pack drill: stage 1;
- Pack musters: receipt muster opening alongside paid training;
- hunting Packs: stage 2;
- frozen Larder army: stage 3;
- retained captains: commander stage 1;
- foreign cells: inherited-cell operation opening;
- all inheritances: origin upgrades and commander stage 2;
- hunt/world-beneath-winter: terminal hunt opening and scored priorities.

Capitulation and annex lifecycle hooks resolve an active hunt as failure before clearing pre-lock runtime. Route break does the same. Terminal transformation lock remains pulse-only, clears the pre-lock runtime first, then applies the lock and scored terminal-war consumer.

## H-03: exact normalization

`common/script_constants/014_cannibalism_warlord_focus_constants.txt` and `common/script_constants/014_cannibalism_wendigo_focus_constants.txt` implement the addendum normalization tables. The explicit semantic/formula/engine exceptions remain documented inline: one-shot counters, fort/building levels, Pack capacity multiples of the existing paid two-Pack batch, research-use count, and encoded AI factors.

## Files added

- `common/script_constants/014_cannibalism_target_score_constants.txt`
- `common/script_constants/014_cannibalism_focus_closure_constants.txt`
- `common/scripted_triggers/014_cannibalism_target_scoring_triggers.txt`
- `common/scorers/country/014_cannibalism_target_scorers.txt`
- `common/scripted_effects/014_cannibalism_target_scoring_effects.txt`
- `common/scripted_triggers/014_cannibalism_focus_closure_triggers.txt`
- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt`
- `common/dynamic_modifiers/014_cannibalism_focus_closure_modifiers.txt`
- `interface/014_cannibalism_focus_closure.gfx`
- `localisation/english/zz_014_cannibalism_focus_closure_l_english.yml`
- this handoff

## Existing files updated

- `common/mtth/014_cannibalism_mtth.txt`
- `common/country_leader/014_cannibalism_traits.txt`
- `common/decisions/014_cannibalism_unified_decisions.txt`
- `common/decisions/014_cannibalism_wendigo_decisions.txt`
- `common/decisions/categories/014_cannibalism_categories.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `common/script_constants/014_cannibalism_warlord_focus_constants.txt`
- `common/script_constants/014_cannibalism_wendigo_constants.txt`
- `common/script_constants/014_cannibalism_wendigo_focus_constants.txt`
- `common/scripted_effects/014_cannibalism_core_effects.txt`
- `common/scripted_effects/014_cannibalism_unified_focus_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt`
- `common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt`
- parent-owned call-site patch: `common/scripted_effects/014_cannibalism_super_event_effects.txt`

No specs, event source docs, spreadsheet, presentation, or Event Details files were edited by this tranche, per parent ownership boundaries.

## Audit evidence and review scenarios

- Exact definition audit found one definition each for both scorers, both MTTH entries, all four terminal-hunt decisions, receipt muster, and inherited cell.
- The six unified AI consumers contain exactly six references to `mtth:cannibalism_unified_target_decision_weight`.
- Independent decision audit found the new blocks brace-balanced and consistent with the repository's targeted-decision `FROM` pattern; a follow-up reference pass was requested after the final scorer-scope repair.
- The ordinary terminal global-war branch was diff-reviewed as unchanged; the Wendigo branch calls the scored terminal helper once.
- No unit-history, country-history, technology, template-definition, or OOB file was changed. The existing `Wendigo Pack` spawn refactor preserves zero starting manpower/equipment and the original template.
- The new pulse work iterates current enemies only. Receipt/cell cleanup uses registered arrays. No recurring world-country on action was introduced.
- The late localisation file contains 82 unique keys, has its required BOM, covers all six decisions/surfaces and new traits/modifier/flags/tooltips, and contains no implementation-history wording.
- Exactly six sprite definitions and six frozen texture paths are registered; none points to a fallback texture.

Parent/gameplay re-audits should exercise the addendum's target matrix, overextension, pre/post-lock score bands, all hunt exits, casualty initialization/caps/reset, exact 100K receipt muster transaction, Pack-stage idempotence, four origin combinations, both commander focus orders, inherited-cell/hunt interaction, and lifecycle cleanup. These runtime scenarios were not represented as having been executed in-game by this subagent.

## Pending asset-owned files

The following six DDS files are registered but not yet present at this handoff checkpoint:

1. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_launch_terminal_hunt.dds`
2. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_terminal_hunt_mission.dds`
3. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_press_terminal_hunt.dds`
4. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_wendigo_terminal_hunt.dds`
5. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_muster_wendigo_pack_from_enemy_death_receipt.dds`
6. `gfx/interface/decisions/014_cannibalism/decision_cannibalism_activate_inherited_winter_cell.dds`

Asset owner: `event014_closure_assets`

Planned package: `docs/assets/014_cannibalism/static_icons_imagegen/closure_2026-07-12/`

Planned asset handoff: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_closure_assets_15_2026-07-12.md`

## Simplifications, omissions, and blockers

No gameplay, AI, focus, lifecycle, localisation, or sprite-registration simplification was made. The only incomplete surface is the six final DDS binaries listed above, which remain under the separate asset agent's ownership. This implementation handoff intentionally does not claim the addendum fully complete until those files and their asset manifest are delivered and reviewed.
