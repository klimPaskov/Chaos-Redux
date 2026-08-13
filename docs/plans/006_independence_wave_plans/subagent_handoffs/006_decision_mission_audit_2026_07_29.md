# Event 006 decision and mission audit — 2026-07-29

## Scope and verdict

This is a fresh source audit of Event 006 decisions, missions, targeted league actions, the pre-wave crisis, the DM-58 reclamation transaction, FORM-03 ratification, cost localisation, AI gates, cleanup, and the decision-owned Statehood Ledger GUI.

No completion claim is made.

The static decision layer is partially sound, but the event remains on HOLD because the existing runtime evidence holds remain open. The custom-cost and GUI-tooltip defects listed from the audit snapshot were repaired by the parent in commit `478adb4c5` and the final bounded localisation audit records zero missing cost triplets.

No gameplay file was changed by this audit.

## Post-audit repair note

This handoff preserves the snapshot findings below for traceability. The current source has exactly one `_blocked` and one `_tooltip` companion for each of the 133 `custom_cost_text` bases in the audited Event 006 surface, and the Statehood Ledger refresh button is bound to `independence_wave_status_gui_refresh_tt`. See `subagent_handoffs/006_localisation_audit_2026-07-29.md` and commit `478adb4c5` for the repaired evidence. DM-58 lifecycle, AI, cancellation, save/load, and live GUI holds remain open.

## Issues, sorted by severity

### Medium — 29 custom costs are missing required blocked and hover localisation

`custom_cost_text` selects `<key>_blocked` when its trigger fails and `<key>_tooltip` on hover according to [Decision modding](C:\Users\klimp\OneDrive\Documents\Paradox%20Interactive\Hearts%20of%20Iron%20IV\mod\chaos_redux\paradox_wiki\Decision%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md:299).

All 29 identifiers below have a base key but neither required companion, so unavailable buttons and their cost hovers can display unresolved localisation keys instead of a comprehensible material requirement.

| Localisation file | Missing custom-cost identifiers |
| --- | --- |
| `localisation/english/006_independence_wave_decisions_l_english.yml` | `independence_wave_cost_pre_wave_crisis` |
| `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml` | `independence_wave_iw_cog_cabinet_cost`, `independence_wave_iw_cog_charter_cost`, `independence_wave_iw_cog_depot_cost`, `independence_wave_iw_cog_force_cost` |
| `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml` | `independence_wave_iw_region_cabinet_cost`, `independence_wave_iw_region_charter_cost`, `independence_wave_iw_region_depot_cost`, `independence_wave_iw_region_force_cost` |
| `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml` | `independence_wave_iw022_charter_cost`, `independence_wave_iw022_coastwatch_cost`, `independence_wave_iw022_ledger_cost`, `independence_wave_iw022_security_compact_cost` |
| `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml` | `independence_wave_iw025_charter_cost`, `independence_wave_iw025_depot_cost`, `independence_wave_iw025_federal_compact_cost`, `independence_wave_iw025_mounted_reserve_cost` |
| `localisation/english/006_independence_wave_iw035_livonia_l_english.yml` | `independence_wave_iw035_charter_cost`, `independence_wave_iw035_coastal_watch_cost`, `independence_wave_iw035_depot_cost`, `independence_wave_iw035_federal_compact_cost` |
| `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml` | `independence_wave_iw059_cabinet_cost`, `independence_wave_iw059_constitutional_cost`, `independence_wave_iw059_depot_cost`, `independence_wave_iw059_officer_cost` |
| `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml` | `independence_wave_iw085_assembly_cost`, `independence_wave_iw085_cavalry_cost`, `independence_wave_iw085_oasis_cost`, `independence_wave_iw085_regency_cost` |

Recommended local repair: add exactly `<key>_blocked` and `<key>_tooltip` for each listed base key in its owning UTF-8-BOM localisation file, retaining the same dynamic cost values and icons as the base string.

### Low — the Statehood Ledger refresh button has no explanatory hover text

`independence_wave_status_refresh` has an enabled scripted-GUI effect but no `pdx_tooltip` in `interface/006_independence_wave.gui`.

The other six ledger buttons have explicit tooltips, so add `independence_wave_status_gui_refresh_tt` in `localisation/english/006_independence_wave_gui_l_english.yml` and bind it only to this button.

### Runtime HOLD — DM-58 participant invalidation needs an explicit lifecycle matrix

`independence_wave_coordinate_reclamation_fronts` in `common/decisions/006_independence_wave_decisions.txt` has a sound static preflight and paid-commit order, but its `cancel_trigger` has no `cancel_effect`.

This does not currently prove an orphaned mutation because costs, claims, wargoals, and staging arrays are only changed in `complete_effect` after the witness is frozen.

It does leave cancellation due to membership loss, client-route lock, or high-chaos invalidation without an explicit player-facing outcome or source-level test evidence.

Do not add a failure flag automatically, because a cancellation caused by another coordinator's success or a route transition is not necessarily a failed reclamation action.

Required live matrix: start DM-58, then separately remove a witness member, change a witness state owner, lock the coordinator route, dissolve the league, save/load, and let the 365-day callback fire after a new coordinator is possible.

## Decision category lifecycle notes

The main Event 006 categories expose concrete commitments rather than a political-power store, using equipment, manpower, command power, experience, civilian-factory commitments, supply/capital control, league ledgers, route gates, and target validity.

The source scan found 394 Event 006 decision blocks with names, 57 timed missions, and 19 selectable missions.

Every timed mission has `activation` and `timeout_effect`.

Every selectable mission has a duration, completion, timeout, cancellation trigger, and AI block.

Fifteen selectable missions do not define `cancel_effect`, but their reviewed source applies material costs and persistent results only on completion or timeout, so no stale charge or target pointer is statically demonstrated.

The three rival-bloc missions with a `visible` block are `independence_wave_rival_bloc_respond_to_invitation`, `independence_wave_rival_bloc_commit_shared_reserve`, and `independence_wave_rival_bloc_challenge_leadership` in `common/decisions/006_independence_wave_rival_bloc_decisions.txt`.

Mission `visible` does not control mission display, but the two selectable missions also have meaningful `activation` gates and the response mission is deliberately activated by effect with `activation = { always = no }`, so this is redundant source noise rather than a confirmed lifecycle failure.

## Mission quality notes

| Mission or transaction | Owner / category / region | Requirement and duration | Success, failure, duplicate-risk result |
| --- | --- | --- | --- |
| `independence_wave_open_host_crisis` | Former host / crisis category / pressure state | Occupation resistance above 50 or stability below 35%; 120 days | Costs security resources on selection, queues only the normal release coordinator on timeout, and records cancelled, blocked, queued, committed, or requester-loss histories. Source lifecycle is coherent; the custom-cost localisation companion keys are missing and save/load, AI selection, requester annexation, and allocator execution remain live holds. |
| `independence_wave_coordinate_reclamation_fronts` (DM-58) | Radical compliant league member / high-chaos league / multi-owner fronts | Focus authorization, three compliant members, injective three-owner preflight, and reserve gate; long mission | The witness is revalidated before both costs and finite claim/wargoal application. Operation cleanup clears state receipts, arrays, and the global coordinator target through `chaosx.nr6.309`. Duplicate target risk is statically addressed; active-mission invalidation remains the HOLD above. |
| `independence_wave_call_charter_expulsion_vote` (DM-60) | Recognized league authority / League Enforcement / target member capital | Recorded factual ground and strategic plus factory commitment; 120-day project | Stores a validated target, resolves or fails the vote, and clears the active target on both removal and cancellation. AI stays very low except on repeated or recorded breaches. |
| `independence_wave_sponsor_member_coup` (DM-61) | Compliant league member / League Enforcement / target member capital | Anti-puppetry charter, live member, no civil war or war, and security-standard material cost; immediate | Starts the civil war through the dedicated helper and records a factual expulsion ground. Cooldown limits repeat use; target validity is checked at selection. |
| `independence_wave_request_charter_war_mandate` (DM-62) | Defensive-congress compliant member / League Enforcement / external target capital | Mutual defence, defensive route, valid external target, diplomatic plus factory commitment; 45-day project | Writes one 365-day target-specific authorization only after completion, clears previous and active target pointers, and applies a separate cancellation consequence. The war on-action consumption path still requires live proof. |
| `independence_wave_form03_ratify_confederal_charter` (FORM03-D11) | LCX carrier / FORM-03 / Low Countries | Resolved language scope and both values at least 70; 360 days | Full ratification, compromise, or rupture is explicit, with cancellation resolving through the same timeout helper. FORM-03 runtime progress and accession evidence remain part of the whole-event hold. |

## Cost and requirement clarity

The custom-cost pairing scan found no decision with only `custom_cost_trigger` or only `custom_cost_text`.

The 29 missing localisation companions are therefore presentation defects, not missing payment guards.

The pre-wave crisis uses `can_pay_independence_wave_security_standard_cost` and a matching one-time `independence_wave_pay_crisis_cost` effect for manpower, Army Experience, Command Power, infantry equipment, support equipment, and stability.

DM-58 rechecks its static preflight in `has_independence_wave_reclamation_front_preflight`, then performs the separate effect-side injective witness search before any resource spend.

DM-60 through DM-62 use capital-target checks and explicit active-target storage and clearing rather than raw country scans at remove time.

## AI validity and route-lock notes

The 394-decision scan found eight blocks without `ai_will_do`, all automatic deadline/activation-only missions in FORM-01, FORM-02, FORM-04, FORM-05, or FORM-48 rather than player-selectable actions.

The 19 selectable missions all have centrally tuned AI blocks.

The crisis AI uses separately tunable base and pressure multipliers in `common/script_constants/006_independence_wave_crisis_constants.txt`.

DM-58 blocks high-chaos closure, client-route lock, loss of active-country status, and league-member loss through its cancellation conditions.

DM-60 blocks an active league crisis and requires recognized authority, while DM-61 rejects the actor itself, a member already at war, or a member already in civil war, and DM-62 requires the defensive-congress route and a valid external target.

No targetless war-goal, free-unit loop, core-spam loop, or repeatable equipment reward was found in the reviewed crisis, league-enforcement, DM-58, or FORM-03 source.

AI choice order, target selection, and package/focus unlock timing remain runtime evidence gaps rather than source passes.

## Localisation, tooltip, and GUI notes

All 1,071 Event 006 decision references collected from `name`, `desc`, `tooltip`, and `custom_effect_tooltip` resolve to an English localisation key.

The exception is the custom-cost variant convention documented above, which the base-key scan intentionally catches separately.

The decision-owned GUI is presentation only, with effects limited to tab flags, animation preference, and `independence_wave_refresh_country_state`.

No GUI button charges resources, selects a gameplay target, or bypasses the decision/mission action layer.

GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc1f4c5703787f71e8598b76e95b8dbf72350d5e96194f67effd3e8dc933a510/36ba7f85412ac8f390f70cb0fff528a28051278937703829c8fc082d29f2ec29/gui-inspect.5ef25f01e19c82e8.json`.

The inspect model reported 426 modelled, 54 approximated, 64 ignored, one missing, four unsupported, and twelve unresolved items, but its validation result is polluted by approximately 2,000 workspace-wide diagnostics and does not establish an Event 006 GUI source failure.

GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a37882066da3563afbf8d918981d8227150dd48a194a981fc798179668e580a7/6bb5a1a2b4a33d45f0052706b8f39744302a17ecab72156315289adc911f071c/independence_wave_status_window-full.svg`.

The renderer produced the requested normal, warning, long-text, and missing-localisation states at 1920×1080 and 1280×720, but the offline render is evidence only and does not replace user-owned live GUI interaction validation.

`hoi4.event_inspect` was attempted narrowly for `chaosx.nr6.3`, but the MCP transport closed before analysis and yielded no evidence.

## Cleanup and exploit-risk notes

The crisis queue stores one requester receipt, retries through bounded constants, clears the queue and retry state on success, block, exhaustion, or requester-loss recovery, and records history rows.

The DM-58 cleanup effect removes its coordinator target, staged state flags, aligned arrays, and operation receipts while finite war goals retain their deliberate expiry.

DM-60 and DM-62 clear their active league target on both successful removal and cancellation.

The reviewed source prevents DM-58 payment before a viable witness and prevents duplicate state-owner pairs in that witness, reducing equipment loss and target duplication exploits.

The remaining exploit-risk is evidentiary: no live save/load, cancellation, delayed callback, or concurrent-requester execution matrix exists for the crisis or DM-58 paths.

## Validation performed and skipped

Performed static checks:

- 1,071 Event 006 decision localisation references resolve.
- 394 decision blocks were examined for AI and visibility/activation coverage.
- 57 timed missions were checked for activation and timeout coverage, and 19 selectable missions were checked for duration, completion, timeout, cancellation, and AI coverage.
- 133 custom-cost identifiers were checked for trigger/text pairing and cost-localisation variants.
- Current crisis, DM-58, DM-60, DM-61, DM-62, FORM-03, category, queue, cleanup, on-action, and GUI source were traced directly.
- Offline wiki decision guidance and vanilla decision precedents were consulted before the audit.

Meaningful validation not run:

- No live HOI4 session was launched, per repository policy.
- No save/load, AI choice, active-mission cancellation, delayed callback, allocator, war-on-action, focus unlock, or scenario playback evidence was available.
- `hoi4.event_inspect` failed before producing an artifact because its transport closed.

## Remaining blockers for parent review

1. Repair the 29 missing custom-cost `_blocked` and `_tooltip` keys.
2. Decide whether DM-58 cancellation needs a distinct player-facing non-failure receipt after the required lifecycle matrix is run.
3. Retain the whole-event runtime holds from `006_event_completion_audit_v31_2026_07_28.md`, especially allocator, crisis retry/save-load, package/focus, formable, AI, balance, scenario, and live GUI evidence.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_mission_audit_2026_07_29.md`

## Skills used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
