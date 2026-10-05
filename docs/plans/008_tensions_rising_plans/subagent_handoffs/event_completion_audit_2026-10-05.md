# Event 008 Tensions Rising completion audit, 2026-10-05

Disposition: partial implementation; completion blocked by unresolved behavior, documentation alignment, and missing mandatory MCP delivery.
This is a read-only release audit, not implementation acceptance.
The only file authored by this auditor is this handoff.
No gameplay, localisation, asset, spreadsheet, source design, index, or Git commit was changed.
Other agents were active; today's localisation handoff and corresponding current text were reviewed separately from the earlier source snapshot.

## Scope and evidence boundary

Reviewed `events/008_tensions_rising.txt`, all seven Event 008 common-file families named in the parent prompt, its event-image GFX, its report/news DDS files, all five achievement triplets, the Event 008 achievement registry section, shared registration/timer/settings/evolution-log/detail call sites, every file in the source-spec package except the prompt-length measurement, both historical Event 008 handoffs, the follow-up improvement addendum, today's localisation handoff, the current overview, and the authoritative workbook's Event 8 and Cluster 3 rows.
No dedicated decision, mission, country package, focus tree, formable, portrait, custom 3D unit, unit sound package, native raid, super-event, terminal scenario, or event-owned scripted GUI is specified or implemented for this event.
A bounded search of `common/decisions`, `common/national_focus`, `common/scripted_guis`, and `common/ai_strategy` found no Event 008/tensions-rising identifiers.
The shared Event Log and Event Details interfaces do not require an Event 008 `chaosx_event_ui_worker` handoff.
Their linked text and data were source-reviewed; their wrapping, states, hierarchy, click regions, and resolution behavior were not rendered by this audit.

The runtime event inventory is the root `.1`, ten visible incidents `.2`–`.10` and `.12`, border callbacks `.13`–`.15`, Thin Wire callback `.20`, and opinion expiry `.21`.
There is no `.11`; the scheduler deliberately skips that number, so its absence is not a missing incident.
Stage IV is non-terminal and no Event 008 world-end or super-event asset package is required.

## Current mechanics and coverage

| Surface | Current coverage/status | Source evidence | Gaps and smallest next action |
| --- | --- | --- | --- |
| Root and automatic registration | Implemented in source; MCP blocked | `events/008_tensions_rising.txt:37-55`; `common/scripted_effects/chaosx_logic_effects.txt:287,656-657`; `common/scripted_effects/chaosx_settings_effects.txt:4083-4084`; `common/scripted_triggers/chaosx_settings_triggers.txt:10` | Repeatable registration and default enablement exist. Verify calm WT-full rejection and evolved eligibility together with the evolution toggle fix. |
| Stage packets and Chaos history | Implemented in source; partial controls | `common/scripted_effects/008_tensions_rising_effects.txt:53-102,190-229`; `common/script_constants/008_tensions_rising_constants.txt` | Packets are 100/0, 100/10, 200/15, 500/25, 1000/50 WT/Chaos. Disabled evolution behavior still applies; see F1. |
| Distributed world tension | Implemented in source; runtime effect unobserved | `common/scripted_effects/008_tensions_rising_effects.txt:104-188`; `common/scripted_triggers/008_tensions_rising_triggers.txt:45-48` | Existing nonspecial countries receive named-threat slices. Current declarations match the documented packet distribution, but actual saturation/rounding and recipient coverage have no runtime evidence here. |
| Tension Pulse | Partial | `common/scripted_effects/008_tensions_rising_effects.txt:277-480`; `common/scripted_effects/chaosx_logic_effects.txt:465` | Strength replacement, stored caps, and timer consumer exist. The duration budget does not represent elapsed remaining time; see F4. |
| Relations and expiry | Partial | `common/scripted_effects/008_tensions_rising_effects.txt:482-688`; `common/opinion_modifiers/008_tensions_rising_opinion_modifiers.txt`; `events/008_tensions_rising.txt:313-326` | Mutual timed modifiers exist, but selector fallbacks bypass recent-actor cooldown and the counter records applications rather than proven distinct live modifiers; see F5. |
| Ten delayed incidents | Implemented in source; partial scheduling/cleanup | `events/008_tensions_rising.txt:58-251`; `common/scripted_effects/008_tensions_rising_effects.txt:776-1110` | Every visible incident has a real pressure bundle and none calls the main effect recursively. The recent-damage branch precedes stage pools, and queued incidents have no terminal guard; see F2 and F7. |
| Frontier clash and callbacks | Implemented in source; MCP/runtime blocked | `common/scripted_triggers/008_tensions_rising_triggers.txt:83-111`; `common/scripted_effects/008_tensions_rising_effects.txt:1124-1282`; `events/008_tensions_rising.txt:254-292` | Independent peaceful valid countries and adjacent owned/controlled states are checked; `change_state_after_war = no` and win/loss/cancel effects exist. Delivery after world-end and actual successful start/callback behavior remain unproved. |
| AI posture ideas | Implemented in source; probability evidence pending owner | `common/ideas/008_tensions_rising_ideas.txt:10-77`; `common/scripted_effects/008_tensions_rising_effects.txt:690-774,998-1021` | Four hidden timed ideas and recent-application flags exist. Parent routed the mandatory weighting audit to `chaosx_ai_probability_auditor`; this audit does not substitute source reasoning for that pass. |
| Evolution rows and Event Details | Source linkage implemented; partial behavior and visual evidence | `common/scripted_effects/008_tensions_rising_effects.txt:231-275`; `common/scripted_effects/chaosx_events_log_effects.txt:2608-2626`; `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:7119-7120,7691-7721,8535-8565,9387-9417`; `localisation/english/008_world_tension_rises_l_english.yml:72-81` | Four stage previews, titles, selected bodies, and stage-record gates exist. Toggle behavior differs from gameplay; current shared-UI rendering and row actor/default behavior remain outside proven MCP coverage. |
| Five achievements | Partial | `common/achievements/chaos_redux_achievements.txt:1736-1820`; `common/scripted_effects/008_tensions_rising_effects.txt:1046-1059,1284-1363`; `events/008_tensions_rising.txt:295-326`; `localisation/english/chaosx_achievements_l_english.yml:364-378` | Definitions, hidden states, localisation, and icon triplets exist. Thin Wire's continuous WT requirement, Blackout's distinctness, and One Denial's actor-specific 120-day window are not fully implemented/proven; see F5–F6 and F8. |
| Popup text | Today's wording and constant-backed display patch implemented; partial context fidelity | `docs/plans/008_tensions_rising_plans/subagent_handoffs/localisation_audit_2026-10-05.md`; `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt:8-117` | All three getters select current chaos tier after immediate effects. Tier-crossing or later changes can misdescribe the actual firing; see F3. |
| Assets | Runtime files/aliases present; provenance/review incomplete | `interface/008_tensions_rising_event_images.gfx:1-12`; `interface/chaosx_achievements.gfx:1073-1130`; overview Assets paragraph; historical report regeneration handoff | Report has a live consumer. News is registered but unused by this chain. Required permanent row-level provenance/review coverage is absent; see assets below. |
| Docs, plans, catalog | Partial/stale | `docs/events/008_tensions_rising/overview.md`; source package and addendum; `docs/spreadsheets/chaos_redux_events_catalog.xlsx` Event 8 / Cluster 3 | Current workbook status is `Needs Testing`, but details/evolutions still hold the prose preceding today's localisation patch. Source-package single-member Diplomatic Panic and `Implemented` status claims are stale. |

## Findings

**F1 — Evolution disable controls suppress logging but leave evolved behavior active.**
`get_tensions_rising_stage` reads only chaos-tier flags at effects lines 53–82.
The main effect unconditionally applies the evolved WT, Chaos, pulse, relation, posture, scheduling, and achievement bundle at lines 93–100.
`is_current_evolution_enabled` appears only in the stage recorder at lines 231–275.
The shared trigger at `common/scripted_triggers/chaosx_settings_triggers.txt:51-54` explicitly reads disabled-stage state.
This contradicts the event skill's evolution-control contract and the source evolution specification's disabled-stage behavior.
Recommendation: make automatic availability, applied-stage selection, delayed-incident eligibility, and popup selection share the same enabled-stage policy, preserving the usable calm baseline.
Validate disabled Stage I–IV separately, WT-full baseline rejection, direct/manual firing, and queued delivery after a toggle.

**F2 — Queued incidents can continue after a terminal state.**
The visible incident immediates have no `world_end` trigger or guard, their common effect at lines 963–969 always applies its bundle, and the border roll at lines 1124–1159 has no terminal-state condition.
The generic random-event selector may stop new roots, but it does not guard already scheduled Event 008 deliveries.
Recommendation: guard delayed visible pressure and new border-clash starts against `world_end`, while allowing necessary cleanup and already-started clash callbacks to settle.
Validate an incident scheduled before terminal transition and delivered afterward.

**F3 — Main popup can display a different packet from the one applied.**
The root applies its packet immediately; stage selection occurs before Chaos gain at effects lines 85 and 95.
`add_chaos_meter_value` changes the meter and calls `update_chaos_meter_tier` at `common/scripted_effects/chaos_meter_effects.txt:4436-4455`.
All three popup getters instead read current `chaos_tier` in `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt:8-117`.
For example, a Stage I firing near the next tier boundary can apply 100 WT/10 Chaos and then display the Stage II 200 WT/15 Chaos summary.
Constant-backed display values remove duplicated numbers but do not preserve the applied stage.
Recommendation: retain a stable applied-packet context for the visible popup and review overlapping outstanding reports, rather than reading a mutable campaign tier.
Validate a tier-crossing firing and a report left open while another event changes Chaos.

**F4 — Pulse extension operates on the original stored budget instead of remaining duration.**
The only assignments to `global.tensions_rising_timer_pulse_days` are initial/replacement assignment, equal-strength extension, and reset after the timed flag has expired at effects lines 329–363 and 471–474.
There is no elapsed-time debit or due-date conversion.
Each equal-stage firing refreshes the timed flag from that stale budget through duration buckets at lines 390–459.
Example source scenario: Stage I receives a 45-day pulse; on day 40 an equal firing should extend the five remaining days by 30, while current code adds 30 to the stored 45 and refreshes a 75-day flag.
The overview discloses duration buckets but does not disclose this remaining-time substitution.
Recommendation: preserve a due date or compute remaining duration before extension, retain parser-safe duration handling, and compare early/late equal-stage repeats plus stronger/weaker replacements under the same scenarios.

**F5 — Relation diversity and Blackout's distinct active count are not established.**
Actor fallback at lines 550–555 and target fallback at lines 596–602 omit the recent-actor exclusion.
Every successful application increments `global.tensions_rising_active_opinion_modifiers` by two at lines 607–613, including the border-start path at lines 1263–1267.
Expiry event `.21` blindly subtracts two at event lines 320–325.
There is no pair/modifier identity receipt, current modifier existence check, renewal distinction, or stale-expiry validation.
Thus the implementation proves an application counter with delayed decrements, not ten distinct live opinion records.
Native repeated-modifier refresh/stack semantics were not established by the short installed effect reference, so exact overcount behavior remains unresolved rather than claimed as observed.
Recommendation: validate same-pair/same-stage repeats, cross-stage repeats, exhausted candidate pools, and border overlap; make counter additions/expiry correspond to distinct owned records and retain cooldown safeguards.

**F6 — One Denial's global window can admit an actor past its own 120 days.**
Recent relation actors last 150 days (`@TENSIONS_RISING_RECENT_RELATION_COUNTRY_DAYS`, effects line 15), while the global recent-damage window lasts 120 days and refreshes on every pair application (lines 612,1266).
The war hook at lines 1345–1352 accepts either actor's 150-day flag while any global window is active.
An actor damaged on day 0 can therefore satisfy the hook on day 140 if an unrelated pair refreshed the global window on day 130.
Recommendation: give achievement eligibility its own actor-owned 120-day receipt, independent of the 150-day selection cooldown, and test unrelated-pair refresh.

**F7 — Normal relation success shadows several follow-up pools.**
Relations are selected before scheduling (effects lines 97 and 99), and any successful pair sets `tensions_rising_recent_relation_damage` (line 612).
The stage II+ recent-damage branch at lines 907–918 comes before the Stage II insurance/staff-car pool at lines 927–935 and the later WT-aware pools.
In a campaign with ordinary valid relation pairs, evolved scheduling therefore repeatedly uses the denial/border/fleet/rumour pool; Insurance Market and Staff Cars need the recent-damage branch to be absent.
Stage I can also select the original calm-map incident without a full-WT condition (lines 919–925), although today's localisation renames/rephrases it as a frontier incident.
This is source control-flow evidence, not a numerical probability or observed starvation rate.
Recommendation: have the probability owner evaluate full local pools and branch eligibility before any weight change; disposition the older world-condition-aware pool design rather than silently treating every incident as equally reachable.

**F8 — Thin Wire checks full WT at the endpoints, not continuously.**
The watch starts at Stage III+ full WT and peace at effects lines 1306–1317.
The war relation callback breaks player peace, and `.20` checks peace/full WT at day 180 (`events/008_tensions_rising.txt:295-310`).
No Event 008 hook invalidates the watch when WT drops below full between those checks.
A dip followed by recovery can still satisfy the final check, while the achievement tooltip promises 180 days at 100% WT.
Recommendation: establish continuous-full-WT tracking through an existing bounded world-tension change path, or obtain and record a design disposition for endpoint semantics; do not introduce an unauthorized periodic world scan.

## MCP calls and blockers

The connected metadata exposed `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.source_lookup`, and the three reference routes.
Exposure did not establish service health.
No refresh, repository-wide `state_flow`, helper expansion, rewrite, job cancellation, or native MCP task was requested.
Initial event selectors omitted `kind`; validation returned `MCP error -32602 ... Invalid discriminator value ... at selector.kind`.
One correction used `id` instead of `eventId`; validation returned `expected string ... at selector.eventId` and `Unrecognized key: "id"`.
Those schema mistakes were corrected and are not classified as route unavailability.

Corrected requests:

| Route | Request bounds | Result at handoff writing |
| --- | --- | --- |
| `hoi4.event_inspect` | `mode=trace`, `{kind:event,eventId:chaosx.nr8.1}`, downstream, depth 3, max 40 nodes / 80 edges, helpers false | Failed: `tool call failed for hoi4_agent_tools/hoi4.event_inspect ... timed out awaiting tools/call after 600s`. No source revision, graph, diagnostics, or artifact received. |
| `hoi4.event_render` | `{kind:namespace,namespace:chaosx.nr8}`, overview, downstream, depth 3, max 40 nodes, helpers false, HTML false | Failed: `tool call failed for hoi4_agent_tools/hoi4.event_render ... timed out awaiting tools/call after 600s`. No JSON/SVG/PNG artifact received. |
| `hoi4.event_compare` | namespace selector, max chain/render 40, render true, default cached/current inputs | Failed: `tool call failed for hoi4_agent_tools/hoi4.event_compare ... timed out awaiting tools/call after 600s`. No baseline identity, graph comparison, coverage, or artifact received. A same-file comparison has not been substituted. |
| `hoi4.source_lookup` | `apply_tensions_rising_event_effect`, scripted effect, references false, max one definition / 25 lines | Failed: `tool call failed for hoi4_agent_tools/hoi4.source_lookup ... timed out awaiting tools/call after 600s`. No indexed definition revision received. |
| `hoi4.reference_context` | event, delayed events/immediate scope/border callbacks, limit 4 | Failed: `tool call failed for hoi4_agent_tools/hoi4.reference_context ... timed out awaiting tools/call after 600s`. |
| `hoi4.reference_search` | `country_event`, game_doc/wiki, limit 2 | Pending delivery. No returned citation available to pass to `reference_read`. |

The exact current blocker is unavailable final MCP delivery, not proof that the requested server operations failed internally.
No event artifact URI exists in this audit at writing time.
Even a successful focused trace/render would omit workspace-wide helper/lifecycle analysis; with helper expansion and full state-flow explicitly excluded by parent scope, helper lifecycle completeness would still need to be reported as a limit.
The required event inspect/render/compare gate is not satisfied by the source review.
The probability audit was routed by the parent to `chaosx_ai_probability_auditor`; no finished baseline/scenario/render/compare handoff had been supplied to this auditor at writing time.
Read and integrate the owner's final evidence before completion claims.

## Task-specific verification and missing scenarios

Performed a manual source walk from root through stage packet, timer, relation selection/application/expiry, posture, scheduling, all ten incident bundles, state selection, clash callbacks, and achievement hooks.
Verified source registration of Event 8 as repeatable and default-enabled, all sixteen event definitions, four evolution preview rows and stage selectors, five achievement definitions and all fifteen achievement sprite aliases, and the non-transfer declaration on border clashes.
Decoded DDS headers for all seventeen runtime files: report 210x176, news 397x153, and fifteen achievement files 64x64; all advertise 32-bit RGB plus alpha with no FourCC compression.
This header check does not establish artwork provenance, pixel quality, round-trip equality, review acceptance, or native consumption.
Read the workbook with `openpyxl` in read-only mode; no formulas, formatting, rows, or exports were altered.
Event 8 is `Needs Testing`; Cluster 3 is `Diplomacy`, members `8,17,36,59`, severities `Medium,Medium,High,High`, status `Partially Available`.
Event 8 Details and Evo I–IV still contain the pre-2026-10-05 localisation prose, so the workbook owner must mirror the final assigned keys and run `.tools/export_event_catalog_csv.py`.

The QA collage was inspected at `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/evt008_sheet.jpg`, SHA-256 `69da56e877a5e0475cc0e3bc6f93f98f4dc86543bdeb17bb26ab0c8f7573943e`.
`pop00` shows the baseline Tensions Rising report with the expected report picture and one acknowledgement; no obvious clipping is visible at the collage's provided resolution.
`pop01`–`pop05` show unrelated vanilla reports/news, and `pop06` shows the map without a popup.
This image does not prove Event 008 follow-up, evolved popup, event-log row, achievement, or terminal cleanup coverage.
`evt008_popKK.png` is absent at that external QA folder; repository-local `records/qa` is also absent.

Missing meaningful scenarios include disabled stages, exact tier-boundary packet display, overlapping report contexts, WT-full calm/evolved gating, late pulse renewal, repeated pair/expiry receipts, actor-specific One Denial expiry, continuous Thin Wire tension, insurance/staff-car reachability, no-safe-border fallback, successful border callbacks, and pending delivery after `world_end`.
No live-game execution, supplied-save inspection, numerical balance conclusion, GUI render, or engine outcome claim was performed.

## Assets and documentation

Runtime aliases and containers are present, but an accepted asset requirement-to-runtime crosswalk with permanent provenance and review records is missing.
The absence of `docs/assets/008_tensions_rising/` is not itself a failure: the current skill permits its deletion after durable evidence promotion.
The problem is that the overview and `docs/plans/repo_cleanup/subagent_handoffs/2026-09-05_events_007_010_documentation.md:37-43` explicitly report deletion without verifying replacement provenance records.
The historical report handoff records ImageGen source mode, a generated-image path, processing settings, dimensions, alpha corners, and a visual selection.
Its referenced prompt, source, preview, contact sheet, and manifest are absent from the current package, and there is no equivalent permanent row-level record for the news image or all achievement originals/state variants.
Recover existing historical manifest/prompt/review facts into permanent documentation if available; do not infer generation or acceptance merely from DDS presence or regenerate art without a bounded asset brief.
The news image has a stable alias but no live Event 008 consumer; disposition that required row as retained unused asset or supply an accepted consumer change.
Optional animated event-detail accent has no accepted consumer; no animation package should be demanded or invented.
No portrait, custom unit audio, bespoke counter, or 3D handoff requirement applies to this event.

| Plan/spec record | Implementation/disposition evidence | Remaining disposition |
| --- | --- | --- |
| Main spec / README / coding and goal prompts | Core packets, repeatable identity, non-terminal Stage IV, pulse, relation, incidents, posture and achievements have source implementations. | Partial against listed controls/lifecycles. Preserve planning-era `To Be Reworked` as historical intake, not current workbook state. Expanded acceptance basis is unresolved where only a status label or implementation claim is retained. |
| Evolution/hidden-effect spec | Four stage records/previews and bundles exist. | Disabled gameplay, remaining pulse time, distinct relation memory and continuous achievements remain partial. World-aware pool/scoring proposals need explicit implementation or rejection/queue disposition. |
| Follow-up improvement addendum | Ten real bundles, safe adjacent-state checks, non-transfer effect, cooldowns and result callbacks exist. | The heading `Accepted Design` has no user decision or parent acceptance citation. Record the actual basis, link the implemented source, and state F1/F2/F7 limits before marking promoted/fully implemented. |
| Cluster/achievement matrix, package manifest, context digest, helper handoff and coding prompt | Runtime and workbook use four-member Diplomacy Cluster 3. | Historical one-member low-severity Diplomatic Panic claims are stale; reconcile with the accepted cluster owner contract, rather than promote either claim automatically. |
| Catalog-row research note | Current workbook directly read. | Its `Implemented` status and Diplomatic Panic wording are stale; record `Needs Testing` and current cluster evidence. Today's final strings still need workbook synchronization. |
| Report regeneration handoff | Historical authored package and runtime DDS recorded. | Historical implementation evidence, current provenance/review incomplete; missing temp folder alone is not a blocker. |
| Localisation handoffs | Historical handoff superseded for current wording by `localisation_audit_2026-10-05.md`; assigned file changes and checks are listed. | Current source-context issue F3 and missing render evidence remain; preserve today's concrete handoff and mirror final text in workbook. |
| Overview future proposals | Pair-specific follow-ups, generic pair helper and more cluster members are explicitly unresolved. | Keep unresolved; no new expansion is recommended by this audit. |

## Source revisions and local references

Source hashes below bind the source observations; they are not MCP revisions or proof of acceptance.
The worktree HEAD observed during hashing was `cbb4441ad4c78485bbec40ce8215a9aefe72e168`; other agents may advance it.

| Path | SHA-256 |
| --- | --- |
| `events/008_tensions_rising.txt` | `0813c4ec4f58d164cbfe2182c75c76189658924b2cf88dd40aa3c9942ebbee30` |
| `common/scripted_effects/008_tensions_rising_effects.txt` | `4a912025dcfd60634be365deb9666fc0627fa88373e43e78b1e4cae3a9abae65` |
| `common/scripted_triggers/008_tensions_rising_triggers.txt` | `fdc722ef70f6c8901472d46052f8ee0a49add7583f15c558a11698ffdfb727d4` |
| `common/script_constants/008_tensions_rising_constants.txt` | `5c2cff30c1714ed353c4fedc96a1f53672b41b04ad6e190e0d15b609d6ab562d` |
| `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt` | `9af846e664edad58befdd385831a5636cee5c080b9f1a06da1e05fc668d8f458` |
| `localisation/english/008_world_tension_rises_l_english.yml` | `9af0d2d250da1dc353148e0fd8c6e1772159b66f68e31b2c73eddd9b3e2c2f66` |
| `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_spec.md` | `9c2e391c68fca68b9b0ad4d20751eea37646edf81aa0ec3ebf81b7ee1b211024` |
| `docs/plans/008_tensions_rising_plans/008_followup_incident_improvement_addendum.md` | `02e09a2bc59c0157a6cac2c75345f4cd276b8ba2f751cdd1844d67ced0eed7e6` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `3420053b9cedc45b7bde32562efd00c0169ed74f9a9589ca482370ba8a641d67` |
| `interface/008_tensions_rising_event_images.gfx` | `3e515b70f63f612600c299f719d75d4c807709611773ca30073200a8a5d5e964` |
| `interface/chaosx_achievements.gfx` | `330fd42433f8152a397f4a60675c1bb3f7ea5495b7b2ce148f8e204da6a3c25c` |
| `gfx/event_pictures/008_tensions_rising/report_event_tensions_rising.dds` | `78514319cef4d923ff6fbc6d1d57ba6e1c4f880a37c5880d6461f7f020cefb80` |
| `gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds` | `ba6b06cf5582cbfc353a43e96cf1cd3d2acec34d85e62e63261993cf9ae095ae` |

Relevant references were read directly while MCP citation delivery was blocked:

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:145,182,194-203`: triggered-only events can still have delivery-time triggers, immediate precedes option choice, and delayed effects schedule country events; SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:635-664,1241,1275-1283`: border-war state/side/callback shape and directed opinion modifier application; SHA-256 `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:1835-1842,2943-2966,7990-8028`: COUNTRY scope for opinion/country-event effects, event scheduling fields, and native non-transfer border-war structure; SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/BFTB_Greece.txt:3306-3323`: vanilla non-transfer border-war precedent with side-specific callbacks; SHA-256 `86a78f463a6e44886f2d14fcc1772f3cd0ffdac7a7dc727eb952ef2c1a5063cf`.

These references support the narrow source claims only.
The wiki and installed effect reference do not prove native outcome acceptance or exact duplicate-opinion semantics.
The attempted local `Opinion modding` and `Diplomacy modding` wiki filenames were absent; pertinent opinion-effect content was read from the installed effects reference and offline Effects page instead.

## Parent next actions

Prioritize enabled-stage/terminal safety and packet display context, then resolve the pulse and achievement tracking discrepancies inside the existing helpers.
Obtain the probability worker's complete scenario-specific handoff before changing weights or eligibility and require matching probability comparison for an owner-applied weighted patch.
Retain/recover exact final MCP outcomes and artifact/source/scenario identities; do not issue a completion claim while inspection/render/comparison remains blocked.
Mirror today's localisation into the workbook through its owner and regenerate the three catalog exports.
Reconcile accepted-plan/cluster dispositions and promote sufficient permanent asset provenance/coverage evidence.
After owner changes, re-audit against their new hashes and evidence rather than treating this snapshot as final approval.

Skills used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, and `xlsx`.
No skill file was changed.
No new mechanic or broad improvement addendum is recommended; the remaining work is existing-surface correctness, evidence, and alignment.
