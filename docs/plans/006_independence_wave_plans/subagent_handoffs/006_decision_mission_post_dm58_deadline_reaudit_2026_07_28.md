# Event 006 decision and mission post-repair re-audit

Date: 2026-07-28.

Scope: static re-audit of Event 006 decision categories and decision or mission files after the DM-58 participant-invalidation repair and the four manual deadline-mission availability repairs.

No gameplay, localisation, scripted-GUI, or helper source was changed by this audit.

## Result

The five repaired surfaces are present in current source and no additional concrete local defect was found that is safe to patch inside this audit scope.

The four manually activated non-selectable deadlines now use `available = { always = no }`, so they cannot immediately complete through the engine's default-true mission availability behavior.

DM-58 now cancels its frozen shared operation when the currently unregistering country is one of its recorded participants, not only when the post-unregister league count falls below the formation minimum.

## Issue list, sorted by severity

### P3: runtime lifecycle evidence remains open

The source is internally consistent for the repaired paths, but static review cannot prove the exact live behavior of mission activation, timeout, cancellation, save/load, or a country leaving a live DM-58 operation.

The required runtime matrix remains the one recorded by the prior repair handoff: non-coordinator participant exit with sufficient unrelated league members, coordinator exit, member-count collapse, natural expiry, finite war-goal expiry after early operation cleanup, save/load during the active window, and AI selection.

### P3: DM-58 AI evidence is incomplete

`hoi4.probability_inspect` found one `mission_ai_will_do` candidate for `independence_wave_coordinate_reclamation_fronts`, but the candidate pool was incomplete.

The named empty-state analysis `probability-968a9859e53e56870b4e8203` correctly returned partial rather than inventing campaign state, with nine unresolved inputs.

No numerical willingness, click probability, or balance conclusion is justified from that partial artifact.

### P4: no new source-level issue

No missing mission `available`, timeout, cancellation trigger, selectable-mission AI block, raw gameplay cost or duration, free-unit effect, or repeatable claim or core issue was found in the current Event 006 decision surface.

## Decision category lifecycle notes

`independence_wave_founding_category`, `independence_wave_government_category`, and `independence_wave_security_category` are gated to active Independence Wave countries.

Recognition, network, league, borders, formables, and high-chaos categories have progressive legitimacy, route, or unlock-flag visibility gates instead of exposing a permanent debug-menu list.

`independence_wave_form01_congress_category`, `independence_wave_form02_union_category`, and `independence_wave_form04_league_category` remain visible only while their corresponding formable progression is active.

`independence_wave_rival_bloc_category` remains visible only to current members or pending invitees, so invitation recipients can answer without exposing the contract to unrelated countries.

The scenario ledger category is three zero-reward navigation controls with AI weight zero, so its zero cost and zero re-enable time are UI navigation rather than a political-power store.

## Mission quality notes

| Mission | Owner/category/region | Requirement and duration | Success | Failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_form01_complete_first_integration_session` | FORM-01 Congress / formed carrier / north-western formable | Manually activated only, manual-only availability, `long_treaty` deadline | Explicit first-stage ratification removes it | Timeout uses `independence_wave_form01_fail_integration_deadline`; inactive progression cancels it | Low |
| `independence_wave_form02_complete_first_maritime_board` | FORM-02 Union / formed carrier / maritime formable | Manually activated only, manual-only availability, `long_treaty` deadline | Explicit first-stage ratification removes it | Timeout uses `independence_wave_form02_fail_integration_deadline`; inactive progression cancels it | Low |
| `independence_wave_form04_complete_first_league_session` | FORM-04 League / formed carrier / league formable | Manually activated only, manual-only availability, `long_treaty` deadline | Explicit first-stage ratification removes it | Timeout uses `independence_wave_form04_fail_integration_deadline`; inactive progression cancels it | Low |
| `independence_wave_rival_bloc_respond_to_invitation` | Rival Bloc / invitee / league network | Delivery effect activates it, manual-only availability, invitation-response deadline | Acceptance or decline removes the local response through the invitation helpers | Timeout expires the invitation; invalid pending acceptance declines it | Low |
| `independence_wave_coordinate_reclamation_fronts` | High Chaos / radical-league coordinator / distinct member-state-owner witness | Radical charter, authorization focus, formation minimum, exact preflight, reserve, strategic and security affordability, `long` deadline | Valid witness pays before issuing the bounded claims and finite war goals | Timeout starts the documented crisis path; participant invalidation now runs shared operation cleanup | Low statically after repair, pending runtime matrix |

The current static inventory contains 43 Event 006 mission blocks.

All 43 declare an explicit `available` block, a timeout effect, and a cancellation trigger.

All 18 selectable missions declare `ai_will_do`.

The remaining 25 non-selectable missions have explicit availability rather than relying on the engine default.

Nineteen missions intentionally rely on a bare cancellation trigger without a local cancellation effect.

The re-audited repaired missions and DM-58 do not set a paid active receipt before their relevant cancellation path, and their relevant lifecycle helpers own any state cleanup, so this pattern is not a safe generic patch target.

## Cost and requirement clarity notes

DM-58 exposes its complex witness through `independence_wave_coordinate_reclamation_fronts_preflight_tt` and its two resource families through `independence_wave_cost_reclamation_front`, rather than dumping the raw member-state-owner search into the player tooltip.

The rival-bloc invitation, acceptance, reserve, host, patron, and leadership actions use target, route, or member validity plus equipment, convoy, fuel, command-power, or XP transactions instead of flat political-power exchanges.

The country-specific conference choices that use ordinary political-power costs are timed route commitments with a success or cancellation path, not passive modifier purchases.

There are 104 unique Event 006 `custom_cost_text` identifiers in the current decision files.

The immediately prior 2026-07-28 localisation re-audit confirmed the base, tooltip, and blocked variants for that set, and neither repair introduced a new cost identifier.

The only raw numeric cost or timer assignments in the Event 006 decision files are the three scenario-ledger navigation controls at zero cost and zero re-enable time.

All gameplay cost, duration, factory-use, value, and AI tuning references found in the re-audited decision surface use script constants or dedicated dynamic payment helpers.

## AI validity and route-lock notes

DM-58 is gated by high-chaos eligibility, radical-revisionist league route, charter-compliant membership, its authorization focus flag, no current league crisis, a formation-minimum check, and the exact witness preflight.

The decision is fire-once and the shared-operation global flag blocks concurrent reclamation operations.

The rival-bloc invitation uses a network-member target array, a target validity trigger, and a cancellation trigger that clears the inviter's active-target state when the target becomes invalid before delivery.

The pending-invitation mission cannot self-complete after the repair, and its AI is intentionally blocked because acceptance and decline have their own AI-routed decisions.

The static AI evidence does not replace live AI target selection or balance testing.

## Localisation and tooltip notes

No new player-facing key was added in this audit.

The four repaired deadlines retain their existing titles, descriptions, and timeout tooltips.

DM-58 retains its preflight, cost, complete, failure, and timeout tooltip contract.

No raw long trigger was newly exposed to the player by the repairs.

## Cleanup and exploit-risk notes

`independence_wave_revalidate_reclamation_front_operation` now calls `independence_wave_cleanup_reclamation_front_operation` when the currently unregistering country appears in `global.independence_wave_reclamation_front_members` during an active operation.

The shared cleanup clears the active-operation flag, coordinator target, state receipt flags, readiness fields, all three frozen witness arrays, and the operation count.

Finite war goals remain deliberately finite rather than being removed during early cleanup, which matches the documented no-reversal policy.

The scan found no `create_unit` effect in Event 006 decision files.

The only direct core grants are one-shot vanilla formable compatibility decisions protected by the vanilla global formation flags and the Event 006 CHU or ASY shortcut guards.

The reclamation claim and war-goal surface is bounded by one active operation, the coordinator's completion flag, the exact preflight witness, and finite expiry.

The repeatable treasury public-works project has an extended duration, a major cooldown, civilian-factory burden, strategic payment, and capital or value-state requirements, so it is not a free construction loop in source.

## Decision-owned GUI evidence

The founding category's `independence_wave_status_scripted_gui` resolves to `independence_wave_status_window`.

`hoi4.gui_inspect` produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dab7f08f82d5d2b3a25ea0f9574019f31bcfff4be4c35fadb906d8d394f16c0a/d803d5bafe6f4910e18e29f386b8b692bb1e7dce26b43038bac5bb211d59c6fc/gui-inspect.6420b62f98b21e5a.json` for the synthetic `normal` scenario.

`hoi4.gui_render` produced the linked normal, disabled, and long-text artifacts at 1920x1080, including `independence_wave_status_window-full.png`, `independence_wave_status_window-click-regions.png`, and the state matrix under artifact root `a37882066da3563afbf8d918981d8227150dd48a194a981fc798179668e580a7`.

The render reports 426 modelled elements, 54 approximated elements, 64 ignored elements, one missing element, four unsupported elements, and 12 unresolved elements.

The GUI tool also reports repository-wide truncated diagnostics, so it does not isolate an Event 006 layout defect that is safe to patch in this decision audit.

No GUI rewrite was attempted.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_mission_post_dm58_deadline_reaudit_2026_07_28.md`

No decision, mission, category, scripted-GUI, or localisation identifier changed.

## Meaningful validation

- Re-inventoried 43 Event 006 mission blocks and asserted explicit availability, timeout effects, cancellation triggers, and AI coverage for every selectable mission.
- Verified the four repaired deadline missions directly in current source and followed their manual activation, timeout, and cancellation contracts.
- Verified the DM-58 revalidation, shared cleanup, and league-member unregister call order directly in current source.
- Scanned cost and timer assignments, free-unit effects, building rewards, core grants, claims, and war goals for passive stores, raw magic values, and repeatability guards.
- Used `hoi4.probability_inspect` and the partial named empty-state evaluation for DM-58 AI evidence instead of treating `ai_will_do` as a click probability.
- Inspected and rendered the existing decision-owned status window without changing GUI source.

## Skipped meaningful validation

No Hearts of Iron IV process was launched, and no live scenario, save/load, or AI execution result is claimed.

The probability evaluation intentionally used an empty named static state to expose missing inputs, so it is evidence of unresolved AI state rather than a numeric AI result.

No separate broad-design plan was written because no broad design expansion or unresolved source policy remains after the participant-invalidation repair.

## Remaining issues

Event 006 remains incomplete at the parent level because the runtime lifecycle matrix, full AI and balance scenarios, and whole-event acceptance evidence remain open.

No fallback or simplification was introduced by this audit.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.
