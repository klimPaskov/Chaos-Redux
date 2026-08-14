# IW-031 Kosovo decision and FORM-09 member-surface audit — 2026-08-10

## Scope and disposition

This handoff records the final active audit of IW-031 Kosovo decisions and missions plus the FORM-09 Balkan Federation member, invitation, consent, territory, and post-formation project surfaces.

The audit found four bounded lifecycle or gate defects and patched them without changing AI weights, reward magnitudes, project costs, route design, or the shared GUI layout.

No commit or staging was performed, and concurrent parent and sibling edits were preserved.

## Issue list by severity

- High, fixed: the shared member-ledger generic branch could admit a country that merely selected family 9 without the exact Balkan package gate; the branch now excludes `balkan_federation` and routes FORM-09 through `is_independence_wave_form09_member`.
- Medium, fixed: an active Border Board project could survive a new war or loss of capital control because `available` is not a post-selection cancellation trigger; the project now cancels with visible consequences.
- Medium, fixed: a shared FORM-09 membership response could continue after its diplomatic connection was lost and record consent during war; all three response decisions now cancel only for FORM-09 when that connection helper fails.
- Low, fixed: the former-host cancellation path evaluated a former-host scope without first asserting that a living host existed; the variable-scope check is now guarded.
- Low, unresolved by design: durable sovereignty remains an immediate one-shot decision, and the KOS `corridor_priority` constant remains unused by the current strategy source.

## Changed files and identifiers

- `common/decisions/006_independence_wave_kosovo_decisions.txt`
  - `independence_wave_kos_settle_former_host_ledgers` now guards the `var:independence_wave_former_host` war check with `has_independence_wave_living_former_host = yes`, avoiding invalid former-host scope evaluation when the former host no longer exists.
- `common/decisions/006_independence_wave_form09_decisions.txt`
  - `independence_wave_form09_ratify_border_board` now cancels when the carrier enters a war or loses capital control while the 120-day project is active, in addition to the existing post-formation identity guard.
  - Its cancellation applies the existing five-point legitimacy, recognition, and security losses plus five instability and now exposes `independence_wave_form09_ratify_border_board_cancel_effect_tt`.
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt`
  - The three shared membership-response decisions now cancel only for FORM-09 when `has_independence_wave_form09_connection_to_inviting_carrier` becomes false, preserving other family behavior.
  - The conditional cancel effects expose `independence_wave_form09_invitation_response_cancel_effect_tt` without adding another gameplay penalty.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
  - The generic family-selected member-ledger branch now explicitly excludes `balkan_federation`; FORM-09 rows must pass `is_independence_wave_form09_member` and therefore the exact BBX/BAX/BOS/MAC/MNT/KOS package, anchor, ownership, control, capital, and setup gates.
- `localisation/english/006_independence_wave_form09_l_english.yml`
  - Added `independence_wave_form09_ratify_border_board_cancel_effect_tt` and `independence_wave_form09_invitation_response_cancel_effect_tt`.
  - The file remains UTF-8 with BOM, and the new response key is present exactly once.

## Lifecycle and cost audit

The KOS founding mission `independence_wave_kos_hold_cantonal_compact_together` is activation-backed, intentionally `available = { always = no }`, lasts 570 days, resolves when both ledgers reach 60 and a route government exists, and applies the idempotent project-failure penalty on timeout or invalid package/capital cancellation.

The ten paid KOS project IDs are all enumerated by `has_independence_wave_kos_active_package_project`, so at most one timed project can be selected at once.

KOS project timers are 75 days for depot, agrarian, and workers-council projects; 120 days for guards and territorial-command projects; and 180 days for former-host ledgers, federal charter, and Balkan corridor.

`independence_wave_kos_codify_durable_sovereignty` is the deliberate one-shot ordinary decision with `fire_only_once = yes`; it applies the strategic cost and final settlement immediately after its stable-ledger, route-government, founding-settlement, capital, and project-lock gates pass.

The shared cost helpers consume command power, manpower, infantry/support equipment, army experience, convoy/train reserve, stability, war support, and civilian-factory commitments as appropriate; neither KOS nor FORM-09 uses a political-power store or a free-unit reward loop.

The FORM-09 Border Board is a 120-day diplomatic-standard project whose completion only changes the public ledgers and clears its open flag; it does not add territory, cores, claims, units, or stockpile.

## Cost and requirement clarity

KOS custom cost tooltips route to the shared administration, security, diplomatic, and strategic cost definitions, and the complete effects subtract the same command, manpower, equipment, experience, convoy/train, stability, and war-support values that the availability triggers advertise.

The civilian-factory modifier is a visible project commitment rather than a hidden political-power exchange, and every paid KOS action requires capital control plus the active-project lock before selection.

FORM-09 invitation, consent, and Border Board tooltips now have matching localisation keys; no new player-facing identifier is left without localisation in the touched surfaces.

## Mission quality notes

- Owner/category/region: KOS owns `independence_wave_kos_cantonal_compact_category` in the Balkans-Danube region; the founding mission requires IW-031 setup, a controlled capital, and an unresolved compact, lasts 570 days, succeeds when both visible ledgers reach 60 with one route government, and fails on timeout or invalid package/capital cancellation.
- KOS project missions: the ten paid actions use the same owner/category and project-ready, capital-control, affordability, route, host, network, stable-ledger, and one-active-project requirements; completion pays the declared material cost before its focus/effect reward, cancellation applies the one-time failure penalty, and the active-project helper prevents duplicate starts.
- FORM-09 post-formation project: BLX owns `independence_wave_form09_balkan_category` in the Balkans region; the Border Board requires a committed FORM-09 carrier, open arbitration, peace, capital control, and diplomatic-standard affordability, lasts 120 days, succeeds by clearing open and raising the public ledgers, and now cancels on war, capital loss, or carrier loss with retryable penalties and no reward loop.
- Shared response missions: FORM-09 full integration, autonomous membership, and withhold responses run through the shared membership category with 180-day, 120-day, and 75-day timers respectively; consent is recorded only at timer removal, while the new family-conditional connection guard cancels stale responses before consent.

## Invitation, consent, territory, and cleanup audit

FORM-09 invitation issuance already requires `has_independence_wave_form09_member_candidate`, which now includes KOS only with the exact IW-031 package, generation force package, state 802 anchor, ownership, control, and capital conditions.

FORM-09 consent requires a pending invitation, a no-war diplomatic connection or same-region relationship, recognized-or-later status, and no severe instability for AI consent; shared human response decisions are available through the shared membership category.

The new response cancellation guard prevents an already-started FORM-09 response timer from recording consent after war or connection loss.

The member-ledger exclusion closes the prior path where a candidate that merely selected family 9 could enter the generic family branch instead of the exact Balkan package gate.

FORM-09 full integration transfers only frozen consenting member units and stockpile once, then transfers only the reviewed exact anchor state for each original package tag; autonomous members retain their territory, forces, and institutions.

KOS focus helpers are idempotent through one-time flags for assembly, communities, guards, host ledgers, and corridor rewards.

KOS cleanup removes the founding mission and all ten project decisions, clears project and route flags and pressure variables, removes package ideas, retires package characters, and clears the failure latch.

FORM-09 cleanup removes the Border Board decision, autonomous-member ideas and flags, carrier identity, BLX global reservation, post-formation flags, and public project flags.

## Cleanup and exploit-risk notes

KOS project failure is latched once per active failure and reset only when a new project begins or the package is cleaned up, preventing duplicate cancellation penalties while preserving meaningful retry cost.

FORM-09 completion is one-shot through `border_arbitration_complete`; integration is one-shot through `integration_committed`; full members transfer existing assets rather than creating free units, and autonomous members receive no territorial or equipment duplication.

## Weighted logic evidence

Fresh `hoi4.probability_inspect` for `common/decisions/006_independence_wave_kosovo_decisions.txt` with `decision_ai_will_do` passed with one ordinary candidate, ten required inputs, zero source diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdc409eaeaab49a373e2cf0d466c4952d460dbe2753a918d070985b0633981e9/c0370d5c50dd8c7a01feca6a47d694a85b7ef7cfde67ec344fbc372acd29119f/probability-inspect-61b11f4c4102.json`.

Fresh KOS mission inspection after all KOS decision edits passed with ten candidates, thirteen required inputs, zero source diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed00f6c00d7e281753383ab1527c525c5a143ec5643d9ba84b3777f2089ca48e/9bbe721867de444a709538d57b6f0dea4f314d845e3ccab34aac03842f7a53b6/probability-inspect-08ba3e9fc7b4.json`.

The KOS mission evaluation used four named empty-state scenarios and returned partial analysis `probability-1b69d23cb1ec220b47809162` with ten never-eligible diagnostics because package, capital, ledger, host, route, and resource state were intentionally unasserted; no normalized selection probability is claimed.

Fresh FORM-09 mission inspection after the cancel patch passed with one candidate, four required inputs, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f4e2c80f61a07b1a8d315e27e1098630e7cf3596fad864f6e197dee1b7d39fb/c27fcca38aa706484e4d40ab256722e3a2d42b06ea8ce608d0365940dfeff7ff/probability-inspect-615fa0b643ce.json`.

The FORM-09 four-scenario evaluation returned partial analysis `probability-fe14a57f9efc304ac44013d2` with four unresolved items and no diagnostics because the empty fixture did not assert carrier, war, capital, or project state.

Fresh shared membership-response inspection passed with eighteen discovered candidates, fifty required inputs, zero source diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b648f229551ae1d347b587844c332a8e948f1302d4ff7ddca36b246666c12f35/38d55abb180e01d5f940d036a9c51ac0d320f5057d5b46a9ac187e5654e4a1e0/probability-inspect-fcb8a8261c6a.json`.

The shared response evaluation used two empty-state scenarios and returned partial analysis `probability-50ca12c76479f534d3aad268` with six never-eligible or unsatisfied-modifier diagnostics; this is parser and uncertainty evidence, not a runtime AI balance claim.

The requested boolean war-state sweep was attempted and returned the exact blocker `PROBABILITY_SWEEP_RANGE_REQUIRED` because every sweep path requires a numeric range or explicit alternatives; no sweep result is claimed.

No AI weight or probability-bearing modifier changed, so no `hoi4.probability_compare` was required or fabricated.

## AI validity and route-lock notes

KOS AI scores remain urgent for the founding crisis and emergency command, high for most material projects, standard for former-host/federal/network actions, and doubled only under the declared war or host-threat modifiers; the MCP evidence is score and eligibility evidence, not a click probability.

FORM-09 response AI still requires the exact invitation family and route connection, while the carrier commit path requires aligned frozen ledgers, minimum three members, minimum three consents, minimum three anchors, identity attestation, and the exact carrier-anchor proof.

The active-project and one-shot flags prevent AI repetition, and no invalid dead-country target or impossible border route was introduced by these patches.

## GUI evidence

The FORM-09 category now attaches the shared `independence_wave_formable_state_puzzle_scripted_gui`; mandatory read-only `hoi4.gui_inspect` for `chaosx_independence_wave_formable_state_puzzle_window` returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/707364b6ae0603969adff6020b6f37d42d748fedaf7e92613d3d2fbde099e3be/c7029e24af00a562496c7d77851fbc710d0eedb6cc6f9683e5bb258ed0427b23/gui-inspect.e4e316bf469650af.json`.

The inspect result is complete for the window but reports workspace-wide aggregate diagnostics, including a truncated 3717-error graph collection, 1551 visible-overlap diagnostics in the bounded validation set, and 14 missing plus 15 unresolved fidelity items; these are not treated as FORM-09-local layout defects.

Mandatory `hoi4.gui_render` returned `GUI_RENDERED` for normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1920×1080 and 1366×768, with linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/807d036607ab95bf45484026903e1debf4ae1e4b1914b92d070a84f44db3651e/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

No GUI rewrite was necessary or performed.

## Localisation and tooltip gaps

The two new cancellation tooltips are present exactly once in the UTF-8-BOM FORM-09 localisation file, and all touched custom-effect-tooltip references resolve.

The existing completion tooltip retains its authored ledger deltas; no raw implementation trigger was exposed to the player by this audit.

## Remaining warnings and skipped validation

The KOS durable-sovereignty action remains an intentional immediate one-shot decision rather than a timed mission; changing it into a timed project would be a design change outside this bounded audit.

The KOS `corridor_priority = 78` constant remains unused by the current KOS strategy source and should be reviewed by the parent as possible deferred tuning or dead configuration.

Typed runtime probability fixtures for package identity, state 802 control, former-host scope, ledgers, route flags, resource affordability, and invitation state remain unresolved; no live save, gameplay, or normalized click-probability claim is made.

Hearts of Iron IV was not launched, in accordance with `AGENTS.md`.

Skills and references used were `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, the required offline Paradox wiki pages, and the required vanilla documentation pages.

## Recommended parent follow-up

1. Keep the four bounded source patches and the two localisation keys together when promoting IW-031 and FORM-09.
2. Supply typed KOS and FORM-09 scenarios for package setup, state 802 control, former-host existence/war, invitation connection, ledger thresholds, route government, and cost affordability, then rerun `hoi4.probability_evaluate` and a supported sensitivity path.
3. Decide whether the immediate `independence_wave_kos_codify_durable_sovereignty` action is intentionally distinct from the timed project family, and either retain this design or write a broader plan before changing it.
4. Review `corridor_priority = 78` against the KOS strategy file and document or wire it through an owner-approved balance change.
