# Event 016 context decision and mission audit handoff

## Audit identity

- Date: 2026-08-01
- Mode: patch-capable decision and mission audit
- Scope: Event 016 host-context events `.4/.5`, Directorate project incidents, Directorate foreign liaison, foreign operations, containment, and directly related lifecycle helpers
- Skills used: `hoi4-decisions-missions`, `chaos-redux-events`, `hoi4-focus-trees`, and `chaos-redux-subagents`
- Reference basis: required offline Paradox wiki decision, event, trigger, effect, scope, localisation, AI, modifier, on-action, idea, and data-structure pages, plus vanilla decision/effect/trigger documentation and targeted vanilla mission/foreign-decision precedents
- Safe boundary: this handoff patches only the two Event 016 Directorate decision files named below and does not redesign transfer, containment, foreign frameworks, event content, or focus routes

## Changed files and identifiers

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`
  - `brilliant_scientist_computation_incident_mission`
  - `brilliant_scientist_electronics_incident_mission`
  - `brilliant_scientist_materials_incident_mission`
  - `brilliant_scientist_rocketry_incident_mission`
  - `brilliant_scientist_high_energy_incident_mission`
  - `brilliant_scientist_biomedical_incident_mission`
  - `brilliant_scientist_teleportation_incident_mission`
  - `brilliant_scientist_cloning_incident_mission`
  - `brilliant_scientist_robotics_incident_mission`
  - `brilliant_scientist_paleogenetics_incident_mission`
  - `brilliant_scientist_xenobiological_synthesis_incident_mission`
  - `brilliant_scientist_biological_weapons_incident_mission`
  - `brilliant_scientist_alien_arms_incident_mission`
  - `brilliant_scientist_temporal_incident_mission`
  - `brilliant_scientist_singularity_incident_mission`
- `common/decisions/016_brilliant_scientist_directorate_foreign.txt`
  - `brilliant_scientist_offer_controlled_research_access`
  - `brilliant_scientist_open_joint_laboratory`
  - `brilliant_scientist_accept_foreign_protection_framework`
  - `brilliant_scientist_restrict_foreign_research_access`
  - `brilliant_scientist_terminate_foreign_research_frameworks`

## Local corrections

### Project incident mission cancellation

Before the patch, each of the fifteen project-incident missions cancelled only after its family `*_incident_resolved` flag appeared.

If Kruger left the host while an incident was active, the former host lost access to the response decision because it was no longer the current host, but the active mission still timed out and applied its failure damage and state penalties there.

Each mission now also cancels when `brilliant_scientist_is_current_host` fails.

The cancellation clears the matching active incident flag, records the matching resolved flag, removes the matching dynamic incident modifier, and clears the shared project-incident lock.

The change does not refund previously spent response costs, repair damaged projects, change incident timers, or alter a normal incident success or timeout.

### Directorate foreign-context cancellation

Before the patch, a pending Directorate foreign action cleared only `brilliant_scientist_foreign_action_in_progress` when its host or selected actor became invalid.

The pending review flag and global selected-actor/state context could therefore remain on an inaccessible former host until another review or world-end cleanup happened.

Each timed liaison action now also clears `brilliant_scientist_foreign_approach_under_review` and calls the existing `brilliant_scientist_clear_foreign_context` helper.

This only cleans an uncompleted context.

It does not dissolve a completed controlled-access, joint-laboratory, or protection framework.

## Issue list by severity

### High: atomic transfer leaves host-context state and foreign-framework targets behind

`brilliant_scientist_transfer_kruger_atomically` in `common/scripted_effects/016_brilliant_scientist_effects.txt` clears current-host, facilities, and evolution scheduling state but does not clear `brilliant_scientist_context_assistant_conflict_pending`, `brilliant_scientist_context_briefing_resolved`, or the four context-choice flags.

The scheduled `chaosx.nr16.5` then fails its current-host trigger on the former host, leaving the pending context state inert.

The same transfer path does not clear `brilliant_scientist_controlled_research_access_partner`, `brilliant_scientist_joint_laboratory_partner`, `brilliant_scientist_joint_laboratory_site`, or `brilliant_scientist_foreign_protection_partner`.

Those persistent global targets can only be cleaned by the old host's termination decision, which becomes unavailable when it loses current-host status.

This conflicts with the Event 016 decision prompt's transfer cleanup contract.

Recommended parent fix: add a transfer-specific cleanup effect in `common/scripted_effects/016_brilliant_scientist_effects.txt` before host status changes.

It should clear the transient context flags and use the same guarded target/flag cleanup already implemented by `brilliant_scientist_terminate_foreign_research_frameworks`.

The parent should decide whether the four original context-choice flags are retained strictly as former-host history or cleared for a possible later reappointment, then make that policy explicit.

### Medium: directorate outcome event `.6` uses decision AI syntax

`events/016_brilliant_scientist_directorate_outcomes.txt` defines event `chaosx.nr16.6` with `ai_will_do` in its options.

Country-event options require `ai_chance`, as the new `chaosx.nr16.4` and `chaosx.nr16.5` correctly demonstrate.

Recommended parent fix: change only the option AI blocks of `chaosx.nr16.6` to `ai_chance`, retaining their existing constant bases and modifiers.

### No additional local decision defect found

The foreign-operation target-array decisions check actor existence, contest status, host lifecycle, world-end state, live-operation locks, transfer locks, and their own one-shot ledgers in both availability and cancellation paths.

Containment validates the exile recipient again at resolution and reopens the sovereignty board rather than forcing an invalid transfer.

The institutional-capture trigger retains its country and numeric proof gates and does not rely on territory selection.

## Decision category lifecycle notes

| Surface | Owner and lifecycle | Audit result |
| --- | --- | --- |
| `brilliant_scientist_directorate_category` | Current host, then sovereign KRG, with `visible_when_empty` and the existing Directorate scripted GUI | The category does not create a hidden decision store. Independent Capacity and Grievance remain GUI-hidden while their derived control status is visible. |
| Directorate institutions and facilities | Current host, construction or timed action, completion flag or re-enable timer, cancellation on loss of host status | Costs combine political power with manpower, equipment, fuel, factories, and industrial burden where their fiction needs material capacity. |
| Directorate project board | Current host, selected project and stage ledger, one active stage lock, incident mission/response or timeout | Stage, damage, suspension, replication, and incident flags prevent duplicate project force or reward loops. |
| Directorate foreign liaison | Current host selects one actor context, finishes one liaison action, then clears selected actor/state context | Pending action cancellation now cleans the selected context. Completed framework targets still need the parent transfer cleanup above. |
| Foreign operations | Foreign actor selects a current host from its bounded host array, resolves a timed action or immediate diplomatic event, and records per-host ledgers | Host, actor, transfer, world-end, and incoming-operation limits are checked before and during the operation. |
| Containment | Current host during sovereignty deadline or requested resolution, one containment action lock, outcome effect validates transfer or resolves a non-country crisis | No free retry loop was found. Invalid exile/defection recipients reopen or resolve safely rather than transferring to an invalid country. |

## Mission quality notes

| Mission family | Owner, category, and region | Requirement and duration | Success, failure, and duplicate risk |
| --- | --- | --- | --- |
| `brilliant_scientist_loyalty_review_mission` | Current host, Directorate, national | Internal Security Section, no current security action, explicit activation, and `brilliant_scientist_directorate_timing.loyalty_review_days` | Timeout snapshots the live Directorate state and raises the review request. Cancellation clears the security lock. The request flag and re-enable timing prevent stacking. |
| Fifteen `*_incident_mission` entries | Current host, project board, national | Exact active family flag and technical, industrial, biological, or exotic timeout constant | A matching response pays material cost and resolves/repairs the family. Timeout damages that exact family. The patch cancels and cleans the incident after host loss so an inaccessible former host cannot receive failure damage. |
| `brilliant_scientist_sovereignty_deadline_mission` | Current host, containment, national | Sovereignty deadline activation and shared deadline duration | Resolution closes the board; expiry creates the containment pressure path. Its flags make the mission non-duplicative. |
| KRG foundation, continuity, portal, temporal, and terminal missions | Sovereign KRG, KRG categories, national or selected-state surface as appropriate | Route flags, focus unlocks, valid target state/country, project stage, and dynamic capacity or debt gates | Timed missions use explicit timeout/cancel paths, and terminal commitments are mutually exclusive through the existing terminal commitment variable and flags. |

## Cost and requirement clarity

The audited Directorate actions do not operate as flat political-power exchanges.

Facility, security, project-response, foreign-framework, and containment decisions pair political power with their appropriate trains, convoys, motorized equipment, support equipment, fuel, manpower, experience, factories, or active production burden.

The gate values are the spend amount minus one and the effects apply the matching negative spend constant, so a decision cannot start without the required material.

The `chaosx.nr16.4/.5` choices have no resource cost because they are single appointment-context event choices, not repeatable economic decisions.

Their causal value changes are routed through the shared clamp and government-control helpers rather than local static effects.

The map decisions retain controlled-state, infrastructure, building, supply, and sea-route requirements in custom tooltips rather than exposing raw trigger chains.

## AI validity and route-lock notes

`chaosx.nr16.4` and `chaosx.nr16.5` use `ai_chance` with the existing constant table and relevant posture, war, ideology, and Directorate-state modifiers.

Directorate decisions use constant-backed `ai_will_do` weights, while foreign operations use the dedicated MTTH weights and daily target-validity cancellation.

No decision was found that can target a capitulated foreign actor, closed route, current KRG host, world-end state, invalid containment recipient, or invalid facility state through the normal availability path.

The only AI syntax defect found is the older `chaosx.nr16.6` event option issue listed above.

## Localisation and tooltip notes

The `.4/.5` title, option, and conditional description keys resolve in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`.

The new mission and foreign cancellation cleanup has no new player-facing state, cost, or effect and therefore needs no localisation key.

The audited decision surface already uses custom requirement and effect tooltips for material costs, state selection, and containment outcomes.

## Cleanup and exploit-risk notes

The patched incident cleanup prevents transfer from becoming a forced former-host incident timeout or an orphaned negative dynamic modifier.

The patched liaison cleanup prevents a dead/invalid selected actor from holding the next foreign review hostage.

No free unit, equipment, core, war-goal, or project-force loop was found in this decision slice.

The unresolved high-severity transfer cleanup can still preserve stale context and completed foreign-framework global targets, so Event 016 should not claim full transfer cleanup until the parent patch lands.

## Scripted GUI evidence

Read-only inspection of `brilliant_scientist_directorate_scripted_gui` established that it is a decision-category presentation surface with `window_name = "kruger_directorate_container"`.

The initial GUI inspection artifact records the expected wrapper-name mismatch: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e006968e617e961d98bc2b782058d307c72bc20e565312474107934921b4b0f1/700feec8c636e379d308f2eff8b8b538af759857a91583304e2a821b05e67090/gui-inspect.8282fc10d4c6acc7.json`.

Inspection of `kruger_directorate_container` reached the workspace scan-byte limit, so no render was claimed and no GUI file was changed.

Source inspection shows only tab and refresh presentation controls, with no decision-owned cost/effect button that lacks a gameplay equivalent.

## Validation

- Checked exact single definitions for `chaosx.nr16.4`, `chaosx.nr16.5`, and `chaosx.nr16.6`.
- Checked the eleven new context event title, conditional description, and option localisation keys against the Event 016 English localisation file.
- Verified all fifteen incident-mission blocks contain the host-loss guard, family modifier removal, and shared incident-lock cleanup.
- Reviewed the two-file patch diff and ran `git diff --check` for the changed decision files.
- Compared mission activation, timeout, cancellation, targeted-decision, and explicit custom-cost behavior with the offline wiki and vanilla AST and foreign-influence precedents.

## Skipped validation

No Hearts of Iron IV session was launched because live game validation is user-owned by repository policy.

The linked scripted GUI could not be rendered because the GUI inspector reached its workspace scan-byte limit.

No broad transfer/effect patch was made because this subagent's approved editing scope was decision/mission and directly paired localisation files only.

## Remaining issues and parent actions

1. Patch `brilliant_scientist_transfer_kruger_atomically` or a directly invoked transfer cleanup helper to clear the context follow-up state and completed foreign-framework global targets.
2. Replace event-option `ai_will_do` with `ai_chance` in `chaosx.nr16.6`.
3. Re-run the Event 016 transfer path audit after that effect patch, specifically with an active project incident, a pending Directorate foreign action, a completed foreign framework, and the 45-day `.5` follow-up pending.

## Simplifications, omissions, and blockers

No simplification was made in the patched decision behavior.

The full Event 016 transfer cleanup remains incomplete until the parent-owned effect and event corrections listed above are implemented.
