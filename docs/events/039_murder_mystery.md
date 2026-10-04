# Event 039 Murder Mystery

Event 039 opens a national investigation after the sitting leader is murdered.
The investigation can uncover a cult, foreign cells, an armed territorial movement, and a campaign against ordinary governments.
The Assassin movement is fictional and has no connection to the Nizari Ismailis, any real religion or ethnicity, historical societies, or anarchism as a whole.

## Design authority and implementation status

The active user goal explicitly authorizes implementation from the accepted Event 039 package under `docs/specs/039_murder_mystery_specs/`.
This is the acceptance basis for the package requirements, including Part 8's real objectives, bounded target management, and lifecycle cleanup.
Current implementation is incomplete and this document does not certify the package or the Part 18 acceptance matrix.
Character validation checks exact membership in the recorded owner's recruited roster, unused target disposition and a frozen row generation.
Consumed rows retain their identity as tombstones during the active lifecycle, so reconciliation cannot reauthorize a second removal.
The validator returns its ownership proof to the actual calling country through a regular event target, including calls made inside a chain rooted in another country.
The First Knife pointer is resolved from the sitting leader through a synchronous modifier-free native trait anchor after its generated package name is verified.
The anchor is removed before the helper returns and never supplies a death authorization by itself.
Founder capture installs and verifies the current route's successor before removal and records a persistent core-capture receipt.
Baseline offender identity is allocated once for the original host and cannot replace a missing, invalid or previously captured territorial founder.
A surviving Assassin State loses bounded Cohesion and Reach after capture and keeps its country, forces, route and foreign network active.
Capture alone does not certify worldwide dismantling or territorial inheritance.
The implementation and evidence limits for the current objective repair are recorded in `docs/plans/039_murder_mystery_plans/validation/mission_repair_2026_10_03/repair_evidence.md`.

## Objective lifecycle

Ordinary phase actions start event-owned missions through `murder_mystery_decision_start_bound_objective`.
The actor retains its mission type, recipient country, original capital, objective state, selected country when relevant, starting public values, and terminal sector snapshot in country variables and arrays.
The binder captures its actual recipient in the regular `murder_mystery_objective_actor` event target, so a setup chain rooted in the original host can still bind an Assassin State objective to the Assassin State.
The regular target is needed only during setup and does not become a persistent shared selector.

The capital and quarter objectives retain the original capital's state identity.
Automatic capital relocation after a loss cannot satisfy those objectives.
Evidence transport and restored capital connections use `has_railway_connection` between the stored endpoints and require full control of both endpoint states.
Force and depot objectives require actual divisions, a supply hub, and the rail connection at the named state.
These checks establish logistical prerequisites but do not measure individual divisions' live supply percentages.
That remaining validation and implementation question stays unresolved.

The terminal mission copies only the countries already assigned to its selected sector from the bounded government registry.
Changing or losing the presentation selector cannot alter that snapshot.
Full mission success requires every snapshot country to capitulate, cease to exist, or become the actor's subject.
Partial success requires at least one such country outcome.
An empty snapshot provides neither full nor partial success.
Sector mission completion does not by itself resolve the entire World of Anarchy campaign.

Every objective checks `murder_mystery_objective_owner_is_valid` in cancellation and reward delivery.
Country loss, runtime resolution, or cleanup retires its receipt and prevents later mission rewards.
The country cleanup helper explicitly removes all sixteen named objective missions without firing their complete or timeout effects.
Global cleanup visits the original host, the central movement, and the existing bounded cell and derivative registries.
It adds no periodic whole-world scan.

Government partial results improve Case Progress and reduce Network Reach while allowing enemy adaptation.
Assassin partial results expand Reach at a Cohesion cost.
Assassin failures reduce Reach and Cohesion, rather than increasing the movement's strength.
These objective outcomes do not add Chaos.

## Runtime ownership and presentation

| Surface | Source |
| --- | --- |
| Phase actions and sixteen objective missions | `common/decisions/039_murder_mystery_decisions.txt` |
| Recipient binding, snapshots, outcomes and removal | `common/scripted_effects/039_murder_mystery_decision_effects.txt` |
| Objective receipt, full control, rail and sector predicates | `common/scripted_triggers/039_murder_mystery_objective_triggers.txt` |
| Country loss and split integration | `common/scripted_effects/039_murder_mystery_integration_effects.txt` |
| Shared Event 039 cleanup | `common/scripted_effects/039_murder_mystery_runtime_effects.txt` |
| Objective types, durations and tuning | `common/script_constants/039_murder_mystery_constants.txt` |
| Mission titles, named states and requirements | `localisation/english/039_murder_mystery_l_english.yml` |
| Mission sprites | `interface/039_murder_mystery_icons.gfx` |

The sixteen objective sprites use `GFX_mission_039_murder_mystery_<objective>` and runtime textures under `gfx/interface/decisions/039_murder_mystery/`.
The objective names are `protect_witness_transfer`, `hold_government_quarter`, `secure_evidence_convoy`, `guard_named_route`, `place_supplied_divisions`, `keep_capital_connected`, `capture_safehouse_chain`, `preserve_target_attack_window`, `prevent_revolt_preparation`, `secure_depots_rail_hubs`, `dismantle_local_recruitment`, `protect_local_government`, `intercept_support_shipment`, `hold_parent_capital_revolt_border`, `survive_opening_war`, and `complete_terminal_sector`.
The current repair reuses their existing bespoke textures and does not create or replace image files.
The asset audit remains governed by the full per-asset review and consumer crosswalk in `docs/assets/039_murder_mystery/visual_asset_audit.md`.

## Remaining acceptance work

The mission family count is not proof of complete objective coverage.
The agency operation, foreign shipment receipts, witness state-to-state transfer, recruitment network outcomes, protected-character survival, derivative support, subject obedience, and all six terminal mandate families still require comparison against their accepted gameplay requirements.
Route rewards, country viability, native technology and focus evidence, probability comparisons, both Meshy model packages and actions, licensed audio, workbook reconciliation, and the full Part 18 matrix remain separate completion gates.
No runtime or persistence claim in this document substitutes for observed game state.

## Further development

Complete the accepted objective families using operation-specific receipts, named evidence locations, guarded transport, and actual cell or administration transactions.
Any proposal beyond the accepted package should receive its own recorded acceptance basis before implementation.
