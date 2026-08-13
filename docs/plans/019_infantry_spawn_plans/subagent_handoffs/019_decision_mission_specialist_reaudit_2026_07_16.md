# Event 019 decision and mission specialist re-audit — 2026-07-16

## Outcome

This was a read-only audit of the live Event 019 decision, mission, scripted-GUI,
AI, scenario-transaction, claimant, registry, localisation, icon, and cleanup
source.

The surface is not clean:

| Severity | Count | Result |
| --- | ---: | --- |
| P0 | 0 | No game-breaking decision or mission defect found. |
| P1 | 1 | Ordinary-country paid selected-family reinforcement can refund without proving whole-request rollback. |
| P2 | 1 | Appoint Family Liaison has no AI non-GUI execution route. |

Two separately approval-gated engine contracts remain blocked:

1. exact ownership transfer of the recorded loyal Event 19 formations during a
   natural claimant or anomalous-family revolt;
2. exact same-battle proof for four division-specific achievements.

No fallback was implemented or recommended as complete. No gameplay source,
localisation, registry source, asset, spreadsheet, staging area, or Git history
was changed by this audit.

## Findings

### P1 — paid ordinary selected-family reinforcement can refund before whole-request rollback is proved

The ordinary-country Anomalous Registry action is not enclosed by the full
management-request transaction used by ordinary paid random requests and
derivative paid reinforcement.

Evidence:

- common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:922-983
  pays the selected provider and the political/command overhead before it calls
  the training or spawn materializer.
- The failure branch at the same file's lines 967-973 refunds both the overhead
  and provider payment solely because infantry_spawn_family_management_result
  is false.
- infantry_spawn_prepare_request_generation_context in
  common/scripted_effects/019_infantry_spawn_core_effects.txt:321-391 can append
  a new generation row before materialization.
- infantry_spawn_create_or_load_selected_family_lot in
  common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:839-856
  can append a registered lot, template, and selected-state row.
- A provider spawn reaches infantry_spawn_spawn_current_template_unit in
  common/scripted_effects/019_infantry_spawn_generation_effects.txt:2212-2318.
  Its failure handling calls infantry_spawn_rollback_current_unit_transaction
  at lines 2161-2210 and then quarantines the ledger, but that local rollback
  owns only the provisional unit and obligation surfaces. It does not remove a
  newly appended generation, selected-state row, lot, or template.
- infantry_spawn_family_lot_created is set when a fresh family lot is appended
  but has no rollback consumer.
- The full transaction helpers already exist at
  common/scripted_effects/019_infantry_spawn_management_effects.txt:4472-4590
  and 4591-4836. They are used by the ordinary paid random request at lines
  4952 and 4994, but the selected-family action does not call them.

Impact:

- A provider or engine materialization failure after publication begins can
  leave an open generation, selected-state row, anomalous lot, and locked
  template behind while refunding the provider and overhead costs.
- The invariant quarantine prevents a normal repeatable free-formation exploit,
  so this is not P0. It is still a P1 transaction-integrity defect: the paid
  action is not atomic, the country's Event 19 management can be frozen, and
  the refund is not conditioned on exact restoration.

Required remediation:

1. After provider and overhead payment succeeds, snapshot the post-payment
   management-request state before preparing the generation.
2. On either training or spawn materialization failure, call the full request
   rollback and prove infantry_spawn_request_rollback_valid.
3. Refund provider and overhead payment only after that proof succeeds.
4. If rollback cannot be proved, keep the invariant quarantine, grant no
   cooldown or request credit, and do not refund.
5. Apply the same boundary to the trainable-zombie branch because it can publish
   a new generation, lot, template, and selected-state row even though it does
   not spawn a unit.

The derivative implementation is the correct precedent:
common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:992-1066
snapshots before publication, performs exact rollback on failure, and exposes a
separate rollback-proved result. Zombie, ghost, and golem callers at lines
1275-1332 refund only when that result is true and grant cooldown only on
materialization success.

### P2 — Appoint Family Liaison has no AI non-GUI path

The player decision and scripted-GUI button share the correct trigger and
effect, but the AI cannot execute this seventh family-management action.

Evidence:

- The decision at common/decisions/019_infantry_spawn_decisions.txt:686-696
  calls infantry_spawn_appoint_selected_family_liaison and deliberately has a
  disabled ordinary decision AI weight.
- The scripted-GUI action at
  common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:98 and
  its enabled gate at line 194 call the same effect and trigger.
- The effect is defined at
  common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1109-1116.
- A repository-wide exact-call search finds no AI call to that effect.
- infantry_spawn_run_anomalous_family_ai at the same file's lines 1251-1329
  dispatches containment, dispersal, sustainment, cantonment, restricted
  deployment, and reinforcement. It does not evaluate
  infantry_spawn_can_appoint_selected_family_liaison and has no liaison weight.
- The scripted GUI itself correctly has AI disabled at
  common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:229, so
  it cannot compensate for the missing dispatcher route.

This conflicts with:

- docs/specs/019_infantry_spawn_specs/prompts/019_infantry_spawn_decision_mission_prompt.md:142,
  which requires an equivalent non-GUI AI path for every interactive button;
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_5_evolution_iv.md:369-377,
  where Field Prophets aggressively seek liaison authority.

Required remediation:

- Add a liaison candidate to the bounded anomalous-family AI dispatcher using
  infantry_spawn_can_appoint_selected_family_liaison and
  infantry_spawn_appoint_selected_family_liaison.
- Centralize its weight in script constants and make the positive preference
  claimant/archetype-aware, especially for Field Prophets.
- Keep the ordinary decision AI weight disabled; the dedicated dispatcher owns
  family selection and prevents an invalid GUI-cursor execution path.

## Verified live-source inventory

The parser treated every one-tab object inside each category as either a
decision or a mission based on days_mission_timeout:

| Source | Decisions | Missions | Total objects |
| --- | ---: | ---: | ---: |
| common/decisions/019_infantry_spawn_decisions.txt | 35 | 10 | 45 |
| common/decisions/019_infantry_spawn_claimant_decisions.txt | 6 | 0 | 6 |
| common/decisions/019_infantry_spawn_derivative_decisions.txt | 23 | 3 | 26 |
| Total | 64 | 13 | 77 |

The three registered categories are:

1. infantry_spawn_formation_management_category in
   common/decisions/categories/019_infantry_spawn_decision_categories.txt:11;
2. infantry_spawn_claimant_category in
   common/decisions/categories/019_infantry_spawn_claimant_categories.txt:10;
3. infantry_spawn_derivative_operations_category in
   common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10.

Every category is always allowed and places
infantry_spawn_scenario_transaction_is_idle in its runtime visibility gate.
The ordinary category excludes derivative countries, the claimant category
requires Evolution III plus an active claimant system, and the derivative
category requires an active derivative package or one of its active missions.

All 64 decisions have:

- an icon;
- visible and available gates;
- an AI weight block;
- a complete effect;
- a player-facing custom effect tooltip.

The live documentation matrix agrees with the source:
docs/specs/019_infantry_spawn_specs/matrices/019_decision_mission_map.md:3-5,
88-93, and 95-109 records 64 decisions and the same 13 missions.

## Mission lifecycle

The ten ordinary-country missions are:

1. infantry_spawn_formation_roll_call_mission
2. infantry_spawn_standardization_cycle_mission
3. infantry_spawn_supervised_demobilization_mission
4. infantry_spawn_training_cycle_mission
5. infantry_spawn_muster_districts_mission
6. infantry_spawn_officer_search_mission
7. infantry_spawn_specialist_preservation_mission
8. infantry_spawn_prototype_maintenance_trial_mission
9. infantry_spawn_rail_corridor_mission
10. infantry_spawn_request_cooldown_mission

They are effect-activated, not player-selectable, use dynamic timeout values,
and route timeout through dedicated completion/defer helpers. Their activation
sites are in common/scripted_effects/019_infantry_spawn_management_effects.txt:
503, 607, 687, 3180, 3249, 3394, 3441, 3538, and 3885, plus the request
cooldown activation in the management or selected-family request path. System
cleanup removes all ten at lines 7333-7342.

The three derivative missions are:

1. infantry_spawn_derivative_integrate_conquered_district_mission
2. infantry_spawn_derivative_submission_warning_mission
3. infantry_spawn_derivative_survive_former_parent_front

They are effect-activated and unavailable for manual selection. Integration
keeps an exact state variable and cancels when package, ownership, or control is
lost. Submission keeps an exact target-country variable and cancels if that
country disappears or war begins. Former-parent survival is bound to the exact
opening-crisis flag. Their activation sites are
common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:540,
2056, and 2223; both derivative cleanup paths remove all three at lines
2425-2427 and 2645-2647.

Mission removal does not silently run completion effects. Each cancellation or
cleanup path owns the relevant flags, target variables, and exact resolution
effect.

## Selected-lot identity and deferred replay

Selected-lot management is UID-bound rather than cursor-bound:

- audit captures infantry_spawn_audit_target_lot_uid at
  common/scripted_effects/019_infantry_spawn_management_effects.txt:479;
- training captures infantry_spawn_training_target_lot_uid at line 602;
- standardization captures infantry_spawn_standardization_target_lot_uid at
  line 669;
- demobilization captures infantry_spawn_demobilization_target_lot_uid at line
  3172;
- specialist preservation captures infantry_spawn_specialist_target_lot_uid at
  line 3241;
- prototype maintenance captures infantry_spawn_prototype_target_lot_uid at
  line 3860.

Each timeout resolves the recorded UID through the ledger instead of reusing
the mutable selected-lot index. The same six UIDs are copied into independent
deferred variables before a same-tag scenario transaction. The muster-district,
officer-search, rail-corridor, and request-cooldown missions retain their own
independent flags or exact state target.

The 53 routed outcomes reconcile exactly:

- 39 incident choices in
  common/script_constants/019_infantry_spawn_constants.txt:61-107;
- 2 prefire choices at lines 109-118;
- 2 claimant-demand choices at lines 120-129;
- 10 ordinary mission completions.

The resumers at
common/scripted_effects/019_infantry_spawn_management_effects.txt:5158-5429 and
6471-6759 run only while the scenario transaction is idle, validate the frozen
choice and target identity, clear only their own evidence, and quarantine an
invalid immutable target rather than switching to the current selection.

Both same-tag commit and proved rollback converge through
infantry_spawn_scenario_finish_same_tag_transaction at
common/scripted_effects/019_infantry_spawn_scenario_effects.txt:1802-1817 and
2206-2237. That finisher clears transaction state, rebuilds the GUI view,
resumes all deferred Event 19 actions, rebuilds again, and reschedules the
country pulse.

## SCN-013 4-by-4 contract

All sixteen type/intensity combinations are represented in each public input
contract:

- infantry_spawn_scenario_launch_inputs_are_valid at
  common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:30-75;
- infantry_spawn_scenario_pending_inputs_are_valid at lines 77-122;
- infantry_spawn_scenario_can_launch_from_triggerable_scenarios at lines
  147-195.

The four types are conventional flood, arsenal lottery, general mutiny, and
anomalous rising. The four intensities are low, medium, high, and maximum. No
fifth fallback or default branch accepts an out-of-range input.

infantry_spawn_scenario_transaction_is_idle at the same file's lines 13-21
blocks the active transaction, same-tag cleanup-pending state, and rollback
cleanup-pending state. Unlock requires aligned ordinary and claimant ledgers
and no invariant failure.

## Claimant profile geography

infantry_spawn_current_claimant_profile_is_regionally_compatible in
common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-109 is one
explicit twenty-profile OR. It has no global catch-all.

The required boundary cases are correct:

- profile 9, Lucien Vautrin, is limited to Europe or North America at lines
  61-64;
- profile 13, Matteo Vellani, is limited to Europe or South America at lines
  77-80;
- profile 20, Mara Voss, is limited to Australia at lines 105-108.

Their stable numeric mappings are in
common/script_constants/019_infantry_spawn_claimant_constants.txt:40, 44, and
51. Claimant payment, recognition, counter-command, discredit, arrest, and
refusal gates all include the same-tag scenario transaction idle contract.

## Payment and transaction checks that passed

Apart from the P1 ordinary selected-family exception:

- Ordinary paid random formation requests snapshot every touched ledger,
  auxiliary array, aggregate, template, unit, and debited resource surface at
  common/scripted_effects/019_infantry_spawn_management_effects.txt:4472-4836.
  The request at lines 4946-5001 commits cooldown, history, and control changes
  only after materialization proof; failure uses the exact rollback.
- Standardization resolves an immutable lot UID, preflights the exact resource
  loss, debits the frozen totals, proves conversion, rolls conversion back on
  failure, and refunds only the exact debit.
- Supervised demobilization resolves the frozen lot UID, proves exact teardown,
  and grants salvage only after that proof.
- Derivative zombie, ghost, and golem reinforcement uses the post-payment
  snapshot and exact rollback contract at
  common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:
  992-1066 and 1275-1332. Refund requires the distinct rollback-proved result;
  cooldown and reinforcement count require materialization success.
- Claimant guard rally snapshots before mutation and commits its experience
  debit, cooldown, and count only after the exact generated formation is
  proved.
- Claimant demand effects recheck the same can-pay trigger immediately before
  manual resource debit. The demand for another formation materializes first
  and charges only on success.

No audited failure path grants request credit or cooldown on an unproved
materialization.

## Muster Board and AI equivalence

The board availability trigger at
common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:10-17
requires an idle scenario transaction, active Event 19 participation,
Evolution III, and a non-derivative country.

Source parity is otherwise sound:

- the nine selected-lot and prototype GUI buttons call the same execution
  wrappers as their decisions;
- the request-mode buttons call the same can-pay triggers and paid random
  request dispatcher;
- all six claimant buttons call the same response effects as their decisions;
- all seven family buttons call the same family effects as their decisions;
- GUI enabled blocks reuse the decision-side can-action triggers;
- lot-sensitive actions load exact stable UIDs;
- scripted-GUI AI is disabled, leaving one intentional AI execution surface.

Every one of the 64 decisions has an AI block. Human-only selection, board-open,
and selected-family decisions correctly use disabled ordinary weights because
their dedicated dispatcher owns selection. The P2 liaison omission is the sole
failed AI-equivalence check found.

The country pulse at
common/scripted_effects/019_infantry_spawn_pulse_effects.txt:9-70 is country
scoped and first checks the scenario transaction lock. It resumes deferred
actions before management closeout, claimant work, and family AI. Event 19 has
no daily, weekly, or monthly all-country on-action. The every-country effects
found in Event 19 source are one-time manifestation, evolution, or SCN-013
setup/cleanup passes, not recurring decision AI scans.

## Localisation, icons, tooltips, and GUI source

A live source cross-check found:

- 160 expected implicit title and description keys for 77 decision/mission
  objects plus three categories, with zero missing;
- 221 unique explicit Event 19 localisation references across decisions,
  categories, the scripted GUI, and the interface layout, with zero missing;
- 51 unique decision/category icon references, with zero missing sprite
  definitions;
- 202 texture references in interface/019_infantry_spawn.gfx, representing 154
  unique texture paths, with zero missing files;
- UTF-8 BOM present in
  localisation/english/019_infrantry_spawn_l_english.yml;
- zero decisions missing complete-effect tooltips.

The static GUI source defines infantry_spawn_muster_board_window and its
overview, lot, command, anomalous-family, and history panels. Control bindings,
enabled gates, localisation, sprites, and texture files are linked. A rendered
layout claim is not made: the optional corrected hoi4.gui_inspect request hit
SCAN_BYTE_LIMIT before producing an artifact.

## Cleanup and exploit protection

The ordinary cleanup effect removes all ten ordinary missions and clears their
running flags, target UIDs, deferred copies, selected indices, claimant/family
state, scenario transaction flags, and GUI arrays. Derivative cleanup removes
all three derivative missions, family cooldowns, exact target variables, and
package flags.

The following protections are present:

- exact lot and unit UIDs instead of mutable cursor identity;
- exact delete cohorts with disband disabled;
- post-materialization proof before normal request success;
- success-only cooldown and request credit;
- invariant quarantine on ledger or rollback proof failure;
- no manual decision availability while a same-tag transaction is active;
- bounded country scheduling rather than a recurring world scan.

The P1 finding is the one transaction boundary that does not meet this standard.

## Registry implementation-file boundary

A live filename scan under common found exactly one Event 19 registry-named
implementation file:

- common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt

The worktree already records the former registry-specific constants and trigger
files as deleted. Shared constants and trigger contracts are present in the
general Event 19 constants and trigger files. This audit did not restore,
create, rename, or edit any additional registry file.

## Approval-gated blockers, separate from severity findings

### B-019-001 — exact natural recorded-formation ownership transfer

common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:171-176 keeps
infantry_spawn_natural_recorded_formation_transfer_is_available explicitly
false. Natural claimant revolt eligibility calls that capability gate.

The derivative package has exact preflight work for selecting a coherent
region and freezing recorded family/claimant unit evidence, but no
ownership-changing caller is wired. HOI4 exposes whole-army or ratio transfer,
not an exact division-subset ownership transfer. The documented
recreate/prove/delete substitute would lose live organisation, veterancy,
medals, officer history, army assignment, and orders. It remains a fallback
requiring explicit owner approval. No blanket transfer or fresh-unrecorded-unit
substitute is present.

### B-019-002 — exact same-battle proof for four achievements

The following achievements remain hidden and unawarded:

- 019_infantry_spawn_one_battalion_wonder
- 019_infantry_spawn_combined_arms_accident
- 019_infantry_spawn_borrowed_future
- 019_infantry_spawn_barracks_of_babel

They are the four hidden Event 19 entries in
common/achievements/chaos_redux_achievements.txt:3131-3210. The exact recorder
at common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1142-1194
has no public caller and requires the exact generated division, opponent
strength ratio, battle duration, and casualties from one battle. Installed
callbacks do not expose that tuple atomically. No country-level proxy or
controlled combat-trial fallback was added.

## Reference and tool record

Skills used:

- chaos-redux-subagents for the bounded audit and handoff contract;
- chaos-redux-events for Event 19 integration, writing, and completion rules;
- chaos-redux-decisions-missions for decision, mission, cost, AI, and scripted-GUI
  review.

No skill was created or updated.

Required offline Paradox wiki pages were consulted before live-source review:
Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On
actions, Event modding, Decision modding, Idea modding, AI modding, Interface
Modding, Scripted GUI Modding, and the relevant division/unit material.

Installed vanilla documentation consulted included effects_documentation.md,
triggers_documentation.md, script_concept_documentation.md,
script_collection_operator.md, script_collection_input.md, dynamic variable
and localisation documentation, and common/script_constants/documentation.md.
Relevant vanilla precedents included:

- common/decisions/CHI_warlord_decisions.txt:557-597 for an effect-activated
  mission;
- common/decisions/POL.txt:2891-3005 for custom-cost display plus explicit
  resource debit;
- common/decisions/categories/AST_decision_categories.txt:130-150 and
  common/scripted_guis/AST_cabinet_trust_scripted_gui.txt for linked
  decision-category and scripted-GUI structure.

The optional narrow hoi4.event_inspect trace for chaosx.nr19.1 reached
ARTIFACT_STORAGE_LIMIT. The optional corrected Muster Board hoi4.gui_inspect
request reached SCAN_BYTE_LIMIT. Neither call changed source or produced
evidence used for a completion claim; the findings and clean checks above come
from the authoritative live files.

## Handoff status

This audit is complete as a review artifact, but Event 19 decision/mission
implementation is not specialist-clean until the P1 and P2 findings are
remediated and rechecked. The two engine-dependent contracts remain approval
blockers even after those source findings are fixed.

Files changed by this audit:

- docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_decision_mission_specialist_reaudit_2026_07_16.md

No simplification or fallback was introduced by this audit.

## Remediation closure re-audit - 2026-07-16

This dated closure pass rechecked the live remediation without changing
gameplay source. The historical P1 and P2 findings above are closed by the
current implementation.

| Severity | Open count | Closure result |
| --- | ---: | --- |
| P0 | 0 | No game-breaking decision, mission, AI, or transaction defect found. |
| P1 | 0 | The paid selected-family request is enclosed by exact commit and fail-closed rollback proof. |
| P2 | 0 | Appoint Family Liaison has a bounded non-GUI AI execution route. |

### P1 closure - selected-family request transaction

The ordinary-country selected-family request now follows this transaction
order in
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1036-1124`:

1. The selected provider payment is attempted first at lines 1048-1051.
2. The political-power and command-power request overhead is paid at lines
   1054-1056.
3. All ordinary-request paid-cost temporary variables and the ordinary
   payment-success temporary variable are set to zero at lines 1057-1066.
   This prevents the shared rollback from treating provider or overhead costs
   as ordinary random-request costs.
4. The post-payment transaction snapshot is taken at line 1067 before any
   generation, lot, template, selected-state, unit, or obligation publication.
5. Training and spawn paths run their dedicated commit verifiers at lines
   1068-1076.
6. Cooldown, request credit, history, control, and success telemetry are
   granted only after `infantry_spawn_request_transaction_committed` is proved
   at lines 1077-1095.
7. A failed commit runs the shared rollback. Provider and overhead refunds are
   reachable only when `infantry_spawn_request_rollback_valid` is greater than
   zero at lines 1096-1106.

The provider refund at lines 1109-1113 is a separate pre-publication case. It
is used only when the provider debit succeeded but the overhead debit did not.
No transaction snapshot or Event 19 publication has begun at that point, so no
whole-request rollback is required.

Both materialization branches create a fresh registered family lot through
`infantry_spawn_create_selected_family_request_lot` at lines 828-839. The
training branch no longer mutates a previously authorized template or an
established family lot.

The training verifier at lines 910-970 proves exact lot, template, component,
selected-state, locked-template, trainable-family, and active-lot deltas. It
also proves the new lot and template identities, family ID, registered-family
profile, integrated recruitment state, zero unit tail, engine template
existence, trainable-family membership, and training telemetry flag.

The spawn verifier at lines 972-1027 builds on the shared live-unit and
obligation materialization proof in
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4887-4929`.
It then proves the exact selected-family lot, template, component,
selected-state, unit, locked-template, spawn-only-template,
transfer-eligible-unit, trainable-family, active-lot, and active-division
deltas together with the family, lot, template, unit, and telemetry identity
checks.

The shared snapshot at
`common/scripted_effects/019_infantry_spawn_management_effects.txt:4431-4514`
now includes the trainable-family tail, political power, command power,
coal-golem equipment stock, and both selected-family telemetry flags. The
rollback at lines 4558-4821 removes every post-snapshot ledger tail, including
the trainable-family tail, restores the reusable generation tail and family
telemetry flags, and proves exact array counts, aggregates, divisions,
resources, coal-golem stock, flags, and ledger alignment. A failed proof sets
`infantry_spawn_request_rollback_valid` to zero and marks the invariant
failure. The caller then withholds both provider and overhead refunds.

Provider-specific debit and refund review also closed cleanly:

- provider 501 pays and refunds zombie training army experience, infantry
  equipment, and manpower.
- provider 502 pays and refunds ghost manifestation political power and
  command power.
- provider 503 pays and refunds golem binding political power, command power,
  and `coal_golem_equipment_1` stock.

Because the selected-family snapshot is post-payment, rollback first proves
those resource values still match the paid state. The external refunds then
return the country to its pre-payment state only after that proof succeeds.

### P2 closure - Family Liaison AI parity

`infantry_spawn_run_anomalous_family_ai` at
`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1384-1473`
now evaluates `infantry_spawn_can_appoint_selected_family_liaison`, assigns the
centralized ordinary liaison weight, adds the centralized Field Prophet bonus
when `infantry_spawn_claimant_field_prophet` is active, includes the liaison
weight in the total, and dispatches the shared
`infantry_spawn_appoint_selected_family_liaison` effect from the weighted
list.

The dispatcher remains bounded to an AI country with an idle scenario
transaction, Evolution IV, an active anomalous registry, and no request
cooldown. The player decision, scripted-GUI button, and AI dispatcher all call
the same effect and therefore share the same availability and payment checks.
The ordinary decision AI weight remains disabled because the country-pulse
dispatcher owns non-GUI selection.

### Re-run checks

The live decision parser still finds 77 objects across the three Event 19
decision files: 64 decisions and 13 missions. All 64 decisions retain an icon,
visibility gate, availability gate, AI block, complete effect, and effect
tooltip. All 13 missions retain an icon, timeout effect, an explicit
`activate_mission` caller, and cleanup through `remove_mission`.

The exact liaison-effect call search now finds all three required execution
surfaces: the player decision, the scripted-GUI button, and the country-pulse
AI dispatcher. No Event 19 daily, weekly, or monthly all-country on-action was
introduced.

A live filename scan under `common/` still finds exactly one Event 19
registry-named implementation file:

- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

No registry file was created, restored, renamed, or edited by this closure
audit.

### Residual risk and unchanged blockers

This is a static source re-audit. Engine execution of dynamic division-template
creation, unit creation and deletion, and exact stockpile values cannot be
simulated by the source review. The implementation handles an unproved engine
rollback by quarantining the invariant and withholding refunds, cooldown, and
request credit. That fail-closed outcome can cost the attempted action, but it
does not expose the prior free-refund or partial-publication exploit.

The two approval-gated engine contracts recorded above remain unchanged:

- B-019-001, exact natural ownership transfer of recorded formations.
- B-019-002, exact same-battle proof for four division-specific achievements.

They are separate from the closed P1 and P2 remediation findings. No fallback
or simplification was introduced. The only file changed by this closure pass
is this existing handoff.
