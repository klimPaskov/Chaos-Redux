# Event 019 independent decision and mission specialist audit — 2026-07-16

## Audit report block

| Field | Result |
| --- | --- |
| Specialist role | `chaosx_decision_mission_auditor` |
| Audit mode | Independent live-source review with bounded corrective patches |
| P0 found / open | 0 / 0 |
| P1 found / open | 2 / 0 |
| P2 found / open | 3 / 0 |
| Exact live inventory | 68 decisions and 14 timed missions |
| MCP result | Event lint blocked by `ARTIFACT_STORAGE_LIMIT`; GUI inspection blocked by `SCAN_BYTE_LIMIT` |
| Overall Event 19 completion claim | Not made; this handoff covers only the decision, mission, shared-GUI, AI, claimant-demand, controlled-trial, scenario-lock, cost-localisation, and linked documentation surfaces |

The bounded surface is clean after the patches recorded below. No fallback or
simplification was introduced. The active release-mode transaction tranche,
visual asset production, and the broader Event 19 completion claim remained
outside this audit's ownership.

## Required references consulted

The audit used the offline Paradox wiki snapshot for Data structures, Triggers,
Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision
modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.
It also used the installed vanilla decision, effect, trigger, script-concept,
and script-constant documentation. Vanilla `WTT_border_conflicts.txt` supplied
the concrete controlled-border-war and timed-mission precedent. No online
Paradox wiki page was used.

The repository skills used were `chaos-redux-decisions-missions`,
`chaos-redux-events`, and `chaos-redux-subagents`. No skill was created or
modified because the reviewed cost-localisation, mission-lifecycle, GUI, and
handoff rules are already covered by those workflows.

## Exact decision and mission inventory

The live source parses as follows:

| File | Decisions | Missions | Total objects |
| --- | ---: | ---: | ---: |
| `common/decisions/019_infantry_spawn_decisions.txt` | 39 | 11 | 50 |
| `common/decisions/019_infantry_spawn_claimant_decisions.txt` | 6 | 0 | 6 |
| `common/decisions/019_infantry_spawn_derivative_decisions.txt` | 23 | 3 | 26 |
| **Total** | **68** | **14** | **82** |

Every one of the 68 decisions has an icon, visibility gate, availability gate,
complete effect, and `ai_will_do`. Every one of the 14 missions has an icon,
availability contract, duration, and timeout effect. The controlled combat
mission and all three derivative missions also have paired cancellation
triggers and cancellation effects. The ten ordinary management/request
missions deliberately use their independent exact deferred-timeout wrappers
instead of generic cancellation.

The 14 mission identifiers are:

- `infantry_spawn_achievement_combat_trial_mission`
- `infantry_spawn_formation_roll_call_mission`
- `infantry_spawn_standardization_cycle_mission`
- `infantry_spawn_supervised_demobilization_mission`
- `infantry_spawn_training_cycle_mission`
- `infantry_spawn_muster_districts_mission`
- `infantry_spawn_officer_search_mission`
- `infantry_spawn_specialist_preservation_mission`
- `infantry_spawn_prototype_maintenance_trial_mission`
- `infantry_spawn_rail_corridor_mission`
- `infantry_spawn_request_cooldown_mission`
- `infantry_spawn_derivative_integrate_conquered_district_mission`
- `infantry_spawn_derivative_submission_warning_mission`
- `infantry_spawn_derivative_survive_former_parent_front`

The four controlled-trial decisions accounting for the live increase from the
historical 64/13 inventory are:

- `infantry_spawn_achievement_one_battalion_combat_trial`
- `infantry_spawn_achievement_combined_arms_combat_trial`
- `infantry_spawn_achievement_borrowed_future_combat_trial`
- `infantry_spawn_achievement_barracks_of_babel_combat_trial`

## Closed P1 — pending claimant demand could resolve against a different row

### Defect

`infantry_spawn_claimant_demand_pending` previously identified only that some
demand existed. The selected claimant index remained a movable player/AI GUI
cursor. Cycling or rebuilding the claimant view could therefore make an
acceptance, refusal, timeout, or deferred replay operate against a different
claimant row.

### Correction

The pending demand now stores
`infantry_spawn_claimant_demand_owner_uid` at issuance. The centralized trigger
`infantry_spawn_selected_claimant_owns_pending_demand` requires all of the
following before a response is exposed or executed:

- the pending flag exists;
- the immutable owner UID exists;
- the selected claimant index is a live aligned row;
- that row's claimant UID equals the owner UID;
- that row still carries a nonempty demand.

`infantry_spawn_can_accept_selected_claimant_demand` combines that ownership
proof with the existing exact affordability gate.
`infantry_spawn_can_refuse_selected_claimant_demand` combines the same ownership
proof with the scenario-transaction idle gate.

The binding is enforced across all execution surfaces:

- the accept/refuse decisions and their AI weights;
- the Muster Board accept/refuse visibility and enabled checks;
- the claimant-cycle button and its underlying effect, both disabled while a
  demand is pending;
- Event `chaosx.nr19.201`, whose immediate block restores the owner row and whose
  acceptance option uses the centralized acceptance trigger;
- immediate AI demand response;
- timeout refusal;
- deferred choice capture and replay.

Deferred replay freezes the owner UID and demand enum. Replay requires the live
owner UID to equal the deferred UID, re-resolves the exact row, proves the live
row UID and demand enum, temporarily selects only that row, and then calls the
same acceptance/refusal effects. A missing owner, missing row, retired row,
mismatched UID, empty demand, changed demand enum, or malformed response enum
calls `infantry_spawn_quarantine_pending_claimant_demand`, marks the existing
ledger/deferred invariant, and clears the malformed pending context without
substituting another claimant.

Cleanup was audited as an invariant, not as a best-effort convention. There is
exactly one pending-demand setter, and it assigns the owner UID before setting
the flag. All six live pending-demand clear sites clear the owner UID with the
flag. Ordinary-country cleanup also clears the variable independently, and the
claimant-crisis and derivative-conversion paths carry the same pair.

## Closed P1 — scenario setup could take custody of a controlled-trial country

### Defect

`infantry_spawn_scenario_country_is_valid_host` admitted an active controlled
trial attacker, the temporary trial opponent, and an opponent retained after a
failed teardown. It also did not prove that the candidate country's same-tag
scenario transaction was idle. Because scenario setup iterates the shared host
trigger, it could select a country while a one-versus-one trial or rollback
owned its state and army identity.

### Correction

`infantry_spawn_achievement_combat_trial_scenario_host_is_safe` centralizes the
trial exclusion. It rejects:

- `infantry_spawn_achievement_combat_trial_active` on the attacker;
- `infantry_spawn_achievement_combat_trial_opponent` on the temporary defender;
- `infantry_spawn_achievement_combat_trial_cleanup_quarantined` on an opponent
  whose exact teardown could not be proved.

`infantry_spawn_scenario_country_is_valid_host` now requires that trigger plus
`infantry_spawn_scenario_transaction_is_idle`. Both the direct/unregistered
launch checks and the shared triggerable-scenario checks already use the host
trigger, and the country iteration in scenario setup uses it for every
additional host.

The cleanup proof supports the exclusion: the opponent flag is cleared only
after zero nonce-marked defenders and no `Event 19 Controlled Trial Detachment`
template remain. A missing, duplicate, or residual identity keeps the opponent
flag and sets cleanup quarantine, so failed teardown cannot silently make the
temporary country eligible. The attacker active flag is cleared only through
the common cleanup path after mission removal, opponent cleanup, and attacker
marker cleanup.

## Closed P2 — custom decision costs lacked engine companion localisation

The three decision files contain 54 custom-cost decision references backed by
52 unique `custom_cost_text` identifiers. All 52 base keys existed, but none had
the engine-derived `_blocked` or `_tooltip` companion, leaving 104 missing
localisation surfaces.

The main Event 19 localisation now contains the exact 156-key cost contract:

- 52 base cost keys;
- 52 `_blocked` keys using the same live values with the cost highlights changed
  from yellow to red;
- 52 `_tooltip` keys preserving the same values under a `Cost:` hover label.

All 54 custom-cost decisions have a `custom_cost_trigger` and a completion
effect. The gameplay debit audit confirmed the ordinary transaction helpers,
claimant response helpers, family-provider payment/refund routes, derivative
government/diplomacy/integration costs, and controlled-trial delayed debit.
The controlled trial charges Army Experience and Command Power only after both
states prove a live border war; failed launch performs cleanup without payment.

The final localisation parse contains 2,874 keys, zero duplicate-key groups,
52 blocked companions, 52 hover companions, and zero semantic mismatches from
their base cost strings. UTF-8 BOM remains present.

## Closed P2 — live inventory and achievement documentation were stale

The decision/mission map still reported 64 decisions and 13 missions. It now
records 68/14, the 39/6/23 decision split, the 11/0/3 mission split, all 14
mission identifiers, all four controlled-trial decisions, and the controlled
mission's 14-day minimum, 45-day timeout, 90-day cooldown, cancellation, and
quarantine contract.

The Event 19 document, achievement matrix, and achievement document now agree
on the same 14/45/90 lifecycle and the scenario-host isolation. The Event 19
document also records the claimant demand-owner UID invariant. The live
near-completion addendum marks these current source-of-truth documents as
reconciled while preserving older audit handoffs as dated historical evidence.

## Closed P2 — live scenario visual documentation lagged the final selector

The finalized generic actor government no longer uses
`GFX_portrait_communist_rebels`. The source already correctly defines and
consumes `GetInfantrySpawnScenarioActorArmyScene`:

- three exact anomalous-family branches return the zombie, ghost, or golem host
  council scene;
- Arsenal Lottery and General Mutiny return registered Event 19 claimant
  army/muster scenes;
- Anomalous Rising and the unconditional default return registered massed-host
  or army scenes;
- both generic `create_country_leader` paths inject the scripted-localisation
  result into `picture = [ARMY_SCENE]` through a meta effect.

The selector exposes six unique sprite tokens. All six are registered in
`interface/019_infantry_spawn.gfx`, and both technical leader names have English
localisation. Event 19 scenario source contains zero references to
`GFX_portrait_communist_rebels`. The live scenario-system document was the only
stale surface and now describes the selector/meta-effect contract. Historical
handoffs were not rewritten.

## Broader decision, GUI, AI, and mission audit

### Category and transaction locks

All three dynamic categories require
`infantry_spawn_scenario_transaction_is_idle`: ordinary formation management,
Evolution III claimant command, and derivative operations. The player Muster
Board is human-only, and its state-changing click gates share the same
transaction-safe triggers as the decisions. Event `chaosx.nr19.201` is the
intentional exception that can record a claimant response for deferred replay;
it performs no locked transaction mutation itself.

### Selected lot and AI parity

Lot-specific actions capture an immutable lot UID before starting their
mission. Their completion paths re-resolve that UID rather than trusting the
current board row. AI start effects choose a qualifying lot through dedicated
selectors and then call the same shared action effects as player decisions and
scripted-GUI buttons. Same-tag replay stores each mission's UID or exact state
identity in its own independent record, so simultaneous expirations cannot
overwrite one another.

The Muster Board defines 41 click effects and 41 exact `_click_enabled`
partners with no missing or orphan partner. Its 54 tooltip references all have
localisation. The Command tab is visible only with an active claimant. The
Anomalous Registry tab is visible only after Evolution IV and only when the
rebuilt country view contains a locally eligible family. Invalid current tabs
return to the overview during rebuild.

The board is explicitly disabled for AI. AI countries use the bounded Event 19
country pulse, dedicated lot selectors, claimant response selector, and family
action dispatcher. No daily, weekly, or monthly all-country on-action was added.

### Controlled combat trials

The four state-targeted decisions use the same shared launch effect and the
same Army Experience/Command Power checks for players and AI. The attacker state
must contain exactly one qualifying Event 19 division and no allied or foreign
formation. The adjacent defender state must be empty and owned by a peaceful
independent AI country. The launch freezes the unit, generation, lot, template,
trial type, nonce, attacker state, defender state, and defender country.

The callback mapping is exact:

- attacker win/loss/cancel: `chaosx.nr19.920/.921/.922`;
- defender win routes to attacker loss through `.923`;
- defender loss routes to attacker win through `.924`;
- defender cancel routes to attacker cancel through `.925`.

Only the attacker-win path can set a ready flag, and it revalidates the frozen
pair and full trial-specific composition/technology evidence first. Loss,
cancel, invalidation, and timeout converge on the same idempotent cleanup. The
mission cancels when the frozen pair is no longer live, times out after 45 days,
and applies the 90-day cooldown to every started trial.

### Derivative missions

The conquered-district mission cancels and clears its state transaction if the
package disappears or ownership/control is lost. The submission-warning
mission cancels and clears its target if the package or target disappears or an
intervening war begins. The former-parent-front mission removes itself when the
package or opening crisis ends. Their timeout effects revalidate the stored
state/country identity before applying the family-specific result or bounded war
goal.

## Required stable-source reread

After the release-mode/first-family transaction agent finalized its tranche,
the audit re-read `chaosx.nr19.105`, `chaosx.nr19.206`, their English
localisation, and the `infantry_spawn.history.first_family_*` payloads.

- `.105` remains the three-option, one-time first-family reception. All options
  call `infantry_spawn_execute_first_family_reception_choice`, and the AI weights
  remain distinct and centrally tuned.
- `.206` remains a report-only acknowledgement for contained claimant-free
  family breach failure; its gameplay consequence is applied before the report.
- All 19 `.105`/`.206` and first-family history localisation keys remain exactly
  once.

No `.105`, `.206`, first-family transaction helper, or
`infantry_spawn.history.first_family_*` key was edited by this audit.

## Validation evidence

- Parsed source: 68 decisions, 14 missions, and 82 total objects.
- Decision surfaces: 0 missing icon, visibility, availability, completion, or AI
  blocks.
- Mission surfaces: 0 missing icon, availability, duration, or timeout blocks;
  4 paired cancellation contracts.
- Object localisation: 82/82 names and 82/82 descriptions present.
- Explicit tooltip localisation: 108/108 decision tooltip keys and 54/54 GUI
  tooltip keys present.
- Custom costs: 54 decision uses, 52 unique IDs, 156/156 base/blocked/hover keys,
  and 0 semantic companion mismatches.
- Claimant ownership lifecycle: 1/1 pending setter assigns owner first; 6/6
  pending clear sites clear the owner UID.
- Scripted GUI: 41/41 click effects have exact enabled partners; no orphan.
- Scenario visual selector: 6 unique returned sprite tokens, 6/6 registered,
  2/2 leader-name localisation keys present, and 0 Event 19 scenario-source uses
  of the former rebel portrait.
- Combined localisation: UTF-8 BOM, 2,874 keys, and 0 duplicate-key groups.
- Targeted script brace review covered the eleven edited gameplay/script files
  with no imbalance.

The required HOI4 MCP calls were attempted after source stabilization. A narrow
event-lint request for `chaosx.nr19.201` and the combat-trial callback family was
rejected with `ARTIFACT_STORAGE_LIMIT` before scanning any file. A Muster Board
GUI inspection was rejected with `SCAN_BYTE_LIMIT`, also before returning source
diagnostics. These are tool-retention/scan blockers, not passing or failing HOI4
source evidence; the local exact-source checks above remain the available audit
evidence.

## Files patched by this audit

Gameplay and interface patches:

- `common/decisions/019_infantry_spawn_claimant_decisions.txt`
- `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
- `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt`
- `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt`
- `events/019_infantry_spawn.txt` (`chaosx.nr19.201` only)
- `localisation/english/019_infrantry_spawn_l_english.yml`

Current documentation patches:

- `docs/specs/019_infantry_spawn_specs/matrices/019_decision_mission_map.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_achievement_matrix.md`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/achievements/019_infantry_spawn/achievements.md`
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`
- `docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`
- this dated specialist handoff

These paths contain concurrent parent and specialist work. This list identifies
the files in which this audit placed bounded patches; it does not claim ownership
of every working-tree difference in those files.

## Simplifications, omissions, blockers, and residual risk

- Simplifications: none.
- Fallbacks: none.
- Open P0/P1/P2 findings inside the audited surface: none.
- MCP blockers: `ARTIFACT_STORAGE_LIMIT` and `SCAN_BYTE_LIMIT`, as described
  above.
- Residual risk: this is a static source audit. It cannot execute the engine's
  border-war callbacks, scripted-GUI renderer, dynamic country creation, or
  exact division/template deletion. The implementation responds to unproved
  runtime identity or cleanup with invariant quarantine rather than a substitute
  row, unit, country, or refund.
- Overall Event 19 completion: not assessed or claimed by this specialist.
