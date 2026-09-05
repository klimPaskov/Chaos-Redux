# Event 006 League lifecycle audit handoff — 2026-09-05

## Status and scope

Status: implemented, narrow non-weighted lifecycle cleanup applied; the wider Event 006 League chain remains partial where authored transitions have no current caller.

Owner: bounded Event 006 League lifecycle auditor/patcher, for parent `/root`.

Audit scope: `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/decisions/006_independence_wave_decisions.txt`, `common/national_focus/006_independence_wave_focus.txt`, `events/006_independence_wave_support_events.txt`, and exact League localisation/GFX references.

The required `AGENTS.md`, decision, event, subagent, and scripted-GUI skills, the offline Paradox wiki pages, vanilla documentation and examples, the accepted League state-machine diagram and League specification, and the current Event 006 addendum were reviewed before editing.

No new phase, charter, GUI, event, decision, asset, country, fallback, or generic content was added.

No AI weight, `ai_chance`, MTTH, random-list, strategy-factor, selector, or other probability-bearing surface was changed.

## Issue list sorted by severity

### P1 — fixed: dissolution left active charter-generation state alive

`independence_wave_dissolve_league_to_network` cleared member and founder arrays and entered `dissolved_network`, but did not clear the five global charter pillar flags, `independence_wave_radical_charter_active`, `independence_wave_league_failed_rescue`, the global leader variable/event target, the global congress-leader variable, or the current-leader country flag.

The accepted diagram permits `dissolved_network` to re-enter `informal_network`, so the next founding cycle could inherit a completed charter and make `independence_wave_adopt_charter_pillar` unavailable after all five pillars had been set.

The stale radical flag also blocked the existing DM59 transform gate, the failed-rescue latch could feed later crisis logic, and leader pointers could continue to resolve to a departed or dead scope.

### P2 — unresolved by scope: authored League transitions have incomplete reachability

`independence_wave_proclaim_consultative_league`, `independence_wave_upgrade_consultative_league`, `independence_wave_reform_league`, `independence_wave_normalize_reformed_league`, `independence_wave_reunify_rival_leagues`, `independence_wave_dissolve_league_to_network`, and `independence_wave_restart_informal_network` are defined in the effects file, but the current repository census found no active caller for most of those transitions.

Adding a caller would widen the requested surface into new gameplay content, so this remains a parent-owned design/integration issue and was not added as part of this audit.

### P2 — unresolved by scope: shared status GUI has production diagnostics

The existing decision-attached `independence_wave_status_window` was inspected and rendered read-only, but the render reports `GUI_TAB_STATE_CONFLICT`, missing hover/selected/locked/disabled/warning/completed/empty-list/full-list/minimum-value/maximum-value coverage, missing animation fallbacks, and visible-overlap diagnostics.

This is the shared Statehood Ledger window rather than a dedicated GUI introduced and owned by a named Event 006 event, and no accepted layout change was in scope; no GUI source was modified.

### P2 — unresolved by scope: founding-congress cancellation is narrow

DM45 `independence_wave_convene_founding_congress` cancels for an inactive country, but its cancellation block does not independently test current network membership, client control, or route validity.

The activation and selectable triggers still require the intended network/member/phase gates, and the current decision file contains unrelated worktree edits, so a cancellation rewrite would require a separate runtime scenario proving the stale mission state and a parent review.

### P3 — unresolved evidence: weighted candidate pools are incomplete

The direct `hoi4.probability_inspect` route accepted the existing decision source, but the mission adapter returned zero available candidates pending five required inputs and the charter adapter returned two candidates with two unresolved inputs.

The named `chaosx_ai_probability_auditor` subagent route was not callable in this environment, so no quantitative weighted conclusion is claimed and no weighted surface was changed.

## Applied patch

Changed file: `common/scripted_effects/006_independence_wave_effects.txt`.

Changed effect: `independence_wave_dissolve_league_to_network`.

Changed effect: `independence_wave_restart_informal_network`.

Both effects now clear the five active charter globals: `independence_wave_charter_sovereign_equality`, `independence_wave_charter_mutual_defense`, `independence_wave_charter_anti_puppetry`, `independence_wave_charter_arbitration`, and `independence_wave_charter_common_development`.

Both effects now clear `independence_wave_radical_charter_active` and `independence_wave_league_failed_rescue` at the dissolved-network to re-entry boundary.

Both effects now clear `independence_wave_league_current_leader` from the saved `independence_wave_league_leader_target` and the variable-held leader scope when present, then clear `independence_wave_league_leader_target`, `global.independence_wave_league_leader`, and `global.independence_wave_congress_leader`.

The cleanup is idempotent at restart so a saved or scripted state that reaches `dissolved_network` without the normal dissolution caller cannot carry active charter-generation state into the next informal network.

Historical receipts remain intact, including `independence_wave_league_dissolved`, `independence_wave_league_dissolution_date`, `independence_wave_first_league_congress_news_fired`, `independence_wave_durable_league_proclaimed`, and `independence_wave_league_reformed`.

Before behavior: dissolution removed members and founders but left the active charter, radical route, failed-rescue latch, and leader pointers visible to later triggers.

After behavior: dissolution and the subsequent restart boundary preserve historical receipts while starting a clean charter and leadership generation.

## Decision-category lifecycle notes

The League category is `independence_wave_league_category` (`The League Congress`) and currently contains DM45 founding congress, DM46 charter pillar adoption, DM47 leadership challenge, DM60 expulsion vote, DM61 coup, and DM62 war mandate, with phase and role gates controlling their visibility.

DM45 opens the regional conference, registers the founding congress preparation, and opens the charter vote on success; timeout applies the existing failure path and reopens congress preparation.

DM46 accepts one charter pillar per decision and maps the fifth accepted pillar to the existing formal-league proclamation effect.

DM47 manages the existing leadership term and is gated to the current compliant member context.

DM60, DM61, and DM62 remain untouched because their AI and crisis weights are probability-bearing and the task forbids changing them without a baseline/compare audit.

The reset boundary now matches the state-machine expectation that a dissolved League is a new founding attempt rather than a continuation of its prior charter generation.

## Cognitive-load notes

The League category has six authored primary actions, but phase, role, crisis, and member gates prevent all six from being simultaneously actionable in the normal lifecycle.

DM45 and DM47 are missions, while DM58 reclamation is in the existing high-chaos category, so the League category does not intentionally expose more than three simultaneous active missions.

The category description exposes eight raw dynamic values — cohesion, common cause, patron capture, shared reserve, member confidence, replicable-opening confidence, revisionist pressure, and completed revisionist actions with a threshold — without phase, member-count, next-action, or consequence framing.

The raw values are locally meaningful to the authored mechanics, but their threshold significance and player response are not all clear from the category text; this is a future localisation/UI readability task and was not changed under the lifecycle-only boundary.

The existing Statehood Ledger GUI is the decision-owned visual consumer reviewed by MCP; its production render diagnostics are recorded above and remain outside this patch.

## Mission quality notes

DM45 `independence_wave_convene_founding_congress` is owned by an active network member/founding country in the League category and covers the network/congress region; it requires recognition, the League unlock, network membership, the relevant informal/preparation phase, and no active crisis.

DM45 uses the strategic-duration mission cost, succeeds by opening conference/preparation/charter state, times out through `independence_wave_fail_congress` with the existing penalties and retry path, and cancels only for an inactive country; duplicate risk is limited by its one-shot and phase gates but the global single-congress guard remains a parent-owned integration concern.

DM47 `independence_wave_challenge_league_leadership` is owned by a compliant active member in the League category and network region; it requires standing, formal/durable League state, and the existing challenge gates.

DM47 uses the standard mission duration, resolves through the existing leadership effect or timeout loss/delta path, and cancels on inactive/nonmember/client/crisis state; its fire-once and phase gates limit duplicate missions.

DM58 `independence_wave_coordinate_reclamation_fronts` is owned by the League/radical member context in the high-chaos category and the authored Middle Volga region; it requires the frozen witness/owner set, at least three participating members, and the existing coordination gates.

DM58 uses the long strategic cost, resolves finite reclamation fronts and war-goal outputs, and routes timeout/failure into crisis and the existing cleanup effect; its coordination flag, aligned arrays, one-shot gate, and cleanup reduce duplicate risk.

## Cost and requirement clarity

DM45 and DM47 each use four spendable cost types in the strategic cost path: stability, command power, dynamic transport capacity, and a civilian factory, all represented with the existing texticons.

DM46 uses two spendable types in the diplomatic-standard path: command power and dynamic transport capacity, with icon-first localisation.

DM58 and `independence_wave_rescue_threatened_member` each use four spendable types: command power, dynamic transport capacity, infantry equipment, and support equipment, all represented with texticons.

No reviewed decision exceeds four distinct spendable cost types, and no reviewed cost string spells out a spendable resource name in place of its texticon.

Non-consumed requirements are carried by the existing custom triggers and decision tooltips; the main clarity gap is the category description's unlabelled threshold/value block rather than a cost/effect mismatch.

## AI validity and route-lock notes

No AI target, AI weight, mission score, event chance, MTTH, random selection, strategy factor, or selector was changed.

The source-level route/member/alignment triggers enforce active origins, network membership, founder/member array alignment, current phase, non-client control, and valid current-country scopes where authored.

Direct probability evidence was collected with `hoi4.probability_inspect` for the existing decision source, but candidate availability remained unresolved because the required scenario inputs were not supplied by the adapter.

`chaosx_ai_probability_auditor` was not callable as a named route in this environment, and no `hoi4.probability_compare` pass was needed because no weighted patch was made.

## Localisation and tooltip gaps

The reviewed League decision names, descriptions, and cost strings are present in `localisation/english/006_independence_wave_decisions_l_english.yml`, and reviewed spendable costs use the correct texticons.

The League category description is dense and exposes raw values without enough threshold/consequence/action framing; it should be addressed only by a separately accepted localisation/UI readability task.

No exact League GFX reference is missing from `interface/006_independence_wave.gfx`; the referenced DDS assets are present.

The GUI MCP render reports missing animation fallbacks and state-coverage/overlap diagnostics, but this shared GUI was not altered.

## Cleanup and exploit-risk notes

The patch removes the stale active-generation state at both the terminal dissolution effect and the re-entry boundary, so repeated or out-of-order invocation is safe with respect to the cleaned flags, targets, and variables.

Member/founder arrays, member flags, discredited flags, cross-regional clocks, and ideas were already cleaned by the existing dissolution effect and remain unchanged.

DM58 finite front and war-goal cleanup was already present and remains the owner of its timeout/failure cleanup; no new free-unit, equipment-farming, war-goal-spam, or cooldown loop was found in the reviewed lifecycle surfaces.

The patch does not clear historical dissolution/news/achievement receipts, so it does not erase the authored historical record while preventing stale active-state reuse.

## Evidence and validation

`hoi4.gui_inspect` succeeded for `independence_wave_status_window` with 48 inspected elements, source revision `e58eeb5d952204c05c9a7ee1f9ab2151dca52df61bc42d3398f6810714431319`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68bdc0c51ec572682898510277944b41806d9f513a5391b83bc7d4f81c0eb99b/c01719612e3ea4b3ecf523aa28b90c0b7d1d5ab610a44dcec9112d2e45103a0a/gui-inspect.e58eeb5d952204c0.json`.

`hoi4.gui_render` covered normal, active, long-text, and missing-localisation states at 1920x1080 and 1280x720; it returned `GUI_RENDERED` with five variants, but validation reported `GUI_TAB_STATE_CONFLICT` and the diagnostics recorded above.

`hoi4.event_inspect` scanned `events/006_independence_wave_support_events.txt` as `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; the artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a00b9a4f9c5b09b66c1d8a0f75b76cb27be51872c75704113fe47989d898cb7/6b60d102abe34b1f100deaa32f5260c3b36dc0c479e3b4c9c29c5ba666b6cb98/event-scan-b21215aa484b.json`.

`hoi4.event_render` rendered the existing `chaosx.nr6.35` neighborhood as `EVENT_RENDERED_PARTIAL` with no blocking diagnostics; the PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/105457baad94648d6687d0a876389073ac56a2683c014c57e5785efd76eea066/d58da67bee6b31fea6705d825a79135c8f6eabede5c6b1475fd4e84ada6c346c/event-neighborhood-b21215aa484b.png`.

`python -B .tools/audit_event6_scenario_matrix.py` passed with 32 scenario cells and 8 edge cases.

`python -B .tools/audit_event6_flags.py` passed with 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families.

Vanilla documentation/examples confirmed the `clear_variable`, `clear_global_event_target`, `has_event_target`, and event-target scope patterns used by the patch.

Skipped meaningful validation: no live HOI4 launch or save/load test was performed; no runtime lifecycle scenario was available through the current MCP route; no named `chaosx_ai_probability_auditor` route or probability compare was run because the patch does not touch weights; no GUI rewrite was attempted because the inspected window is a shared existing UI and no accepted layout change exists.

## Remaining issues and handoff boundary

The parent should separately decide how to make the authored consultative/reform/rival/dissolution branches reachable without inventing unapproved decisions, events, phases, or fallback content.

The parent should separately evaluate DM45 cancellation with a runtime scenario that proves a mission can persist after network/client invalidation.

The parent should separately route the shared Statehood Ledger GUI diagnostics to the authorized shared-GUI owner if a layout repair is accepted.

No new plan or addendum was written; this required dated handoff is the only documentation artifact created by this subtask.

The gameplay change is intentionally unstaged and uncommitted so the parent can review it with the other agents' worktree edits.
