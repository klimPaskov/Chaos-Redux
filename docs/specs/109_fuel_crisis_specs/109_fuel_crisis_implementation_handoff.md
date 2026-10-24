# Fuel Crisis: implementation and verification handoff

## The implementation target

Implement the world loss defined in Parts 1 and 2 as one admitted Event 109 occurrence. Its opening immediate hidden effect sets national stored fuel to exactly zero for every country existing at that resolution. Acknowledgment only closes the announcement. It does not apply, delay, reverse, or repeat the effect.

The preferred native operation is `set_fuel = 0` in each current country scope of one `every_country` pass. This operation has both repository offline reference support and an existing mod precedent. Installed native documentation and MCP evidence must confirm the supported operation before gameplay implementation.

The design identity is Event 109 Fuel Crisis, Minor Fire-Once, Chaos level 1, Severe member of Various Anomalies cluster 11. The user explicitly accepted cluster 11 Severe membership on 24 October 2026, with existing event eligibility unchanged. Former catalog identity 114 is historical only under the user-authorized migration; the parent owns the workbook and shared-registry writes. No runtime activation, workbook migration, native analysis, or live validation is claimed by this specification.

The user explicitly supplied the identity, one-time all-country reserve wipe, unchanged upstream oil economy, ordinary recovery, no evolutions, and connection to Event 101 Tasks. The 109-owned receipt contract and Part 1's transient Chaos calculation are parent-promoted planning choices within that brief. They are neither tested code nor additional mechanics explicitly requested by the user.

## One owner for the world occurrence

### Admission and receipt

The event needs a small owner record to distinguish an accepted occurrence from a duplicate delivery. Shared Fire-Once eligibility alone does not provide that distinction.

Use a 109-owned occurrence sequence, a consumed-sequence record, and persistent natural-consumed state. A receiving-country pending context carries the admitted sequence and whether the shared dispatcher owns history and pacing. Exact identifiers belong to the approved implementation schema. These records serve only Fuel Crisis and its Tasks occurrence key.

Preserve the accepted receipt's origin as ordinary shared selection, normal non-force manual dispatch, deliberate force, or raw direct debug. This is existing occurrence provenance, not a separate anti-console system. The first committed occurrence consumes natural eligibility regardless of origin. A force-first or raw-debug-first occurrence therefore leaves both the trusted owner state and shared fired record closed to later ordinary selection. Later force receipts never clear natural-consumed state.

An ordinary request is admitted only when the natural occurrence is unused and the shared fired record does not already identify 109 as fired. An already pending handoff prevents another request from replacing its context. Admission supplies one receipt. The opening immediate claims that receipt before any country fuel write, then completes the world pass and records the completed occurrence.

The claim prevents reentry while the effect is running. Completion means that the sweep and one-time manifestation have finished. This ownership distinction does not imply native rollback or permission to retry a partially executed sweep. Native execution and save boundaries must be verified.

A duplicate sender is rejected before sending the opening event and before shared accounting. A duplicate opening callback rejects the already consumed receipt before touching fuel, transient counts, Tasks, presentation, or owner accounting. Rejection must not create another historical record or another minor-event pacing update.

Occurrence sequences are identity values. Installed evidence must establish an exact integer range and a safe admission limit. They must not wrap, reset on reload, or depend on formatted decimal strings. Reject admission at a verified limit rather than reuse an old key.

### Normal, force, and direct debug entry

| Entry route | Required admission | Result |
| --- | --- | --- |
| Ordinary shared selection or normal manual trigger | Natural occurrence unused, shared eligibility satisfied, no pending handoff | One new receipt and one world wipe |
| Ordinary request after completion | Natural-consumed state or shared fired record indicates completion | No event gameplay and no duplicate shared accounting |
| Explicit Force Trigger Mode dispatch or supported force helper | A deliberate force request with a fresh 109-owned receipt | One new world wipe for that force occurrence |
| Duplicate delivery of an accepted normal or forced request | Receipt already consumed | No fuel write, manifestation, Tasks handoff, history, or pacing |
| Raw direct opening event before the initial occurrence | No admitted pending context, no natural-consumed state, no shared 109 fired record | Adopt an initial receipt with raw direct-debug origin and commit the same world operation |
| Raw direct opening event after completion | No fresh dispatcher-admitted receipt | No-op, including when the receiving country has Force Trigger Mode enabled |

The supported force feature is a deliberate replay tool. A country flag enabling force mode is not itself a new occurrence identity. An opening event delivered twice must not wipe fuel that countries rebuilt after its first delivery.

Raw debug entry that adopts the initial receipt also owns its single shared Fire-Once accounting call because it bypassed the dispatcher. Dispatcher-admitted entry leaves that accounting to the dispatcher. Both routes use the same event-owned commit behavior. They must not contain parallel copies of the wipe, Chaos calculation, or Tasks occurrence creation.

Direct debug support does not require a second live event ID. The implementation must retain one canonical opening identity, `chaosx.nr109.1`, and document supported debugging through that identity and the existing force surface.

### Native handoff gate

The candidate handoff invokes the opening country event without a delay and consumes its pending context in immediate. Repository offline documentation describes no-delay country events as instant and immediate as executing when the event fires. That is supporting source evidence, not proof of the installed build's scheduling.

Before implementation, verify that the pending receipt is consumed before another admitted request can overwrite it. Do not pass a receipt through a mutable latest global value and assume a queued callback retains the old value. If native scheduling is asynchronous, obtain a documented callback-bound handoff or keep this implementation route blocked. Do not invent event payload fields or a new shared transaction framework.

The shared dispatcher currently sends the country event before its type-specific accounting. Preserve one accounting owner and demonstrate actual execution order through the supported native and MCP evidence. An entry guard based solely on `global.fired_events` is insufficient because that array's state at entry depends on this order.

Part 4's achievement accepts an ordinary shared occurrence or a normal non-force manual dispatch that passes shared eligibility. Forced and raw direct-debug origins are excluded by this achievement's design. The existing registry's campaign validity contract is an additional requirement. Copy the frozen origin into the existing Tasks occurrence context and check it at the genuine success callback. A later change to the current force-mode setting cannot rewrite an old receipt's origin.

## The world pass

The affected set is every existing country at resolution, including the coordinating country. It must not be reduced by human control, AI control, major status, subjects, state ownership, ideology, faction, current fuel demand, or unusual Chaos Redux identity.

The native candidate iterator is `every_country`. The offline scope reference describes these country iterators as excluding nonexistent countries, while `every_possible_country` includes them. A country created after the completed occurrence is outside that occurrence's set.

Keep `set_fuel = 0` directly in the iterated country scope. In an event, `ROOT` remains the recipient and `THIS` represents the current scope. Returning to ROOT for the setter would repeatedly clear the recipient. If owner counters require a scope return, that return contains counter accumulation only. Local positivity and major/war predicates remain in the iterated country.

This is one serial immediate sweep observed as one event resolution. It must not schedule a country event for each target, advance time, create or annex countries, or invoke Tasks from inside the loop. The design does not claim simultaneous memory writes or native transactional rollback.

Countries already empty receive the same setter and remain zero. Their lack of positive loss affects only the onset Chaos count. It never exempts them from the sweep.

The event makes no changes to oil resources, oil-state ownership or control, resource access, buildings, refinery output, silos, storage capacity, imports, trade agreements, military orders, fuel consumption rules, or ordinary production rules. Exact before-and-after evidence must verify those surfaces. Subsequent engine production and deliveries may restore fuel on the next ordinary update.

The reserve target is national fuel. Native unit buffers remain governed by the engine. Do not add division, fleet, aircraft, supply, or equipment modifications to simulate immediate immobility. The specification promises the reserve loss rather than every operational consequence occurring on the same frame.

The existing `remove_fuel_from_stockpile` helper negates its caller's temporary amount in place and calls `add_fuel`. It supplies neither a stockpile reading nor an exact-zero guarantee. It should not be repurposed for this wipe. Getter arithmetic would introduce unnecessary unit conversion, precision, and native clamping dependencies. Literal zero represents the invariant target. Any project constant used for that target requires verified acceptance in the native setter field.

## One-time Chaos accounting

Part 1's promoted starting balance values are:

| Pre-wipe affected count N | Base world contribution |
| --- | ---: |
| 0 | 0 |
| 1–2 | +10 |
| 3–9 | +15 |
| At least 10 | +20 |

Add 5 once when at least two of the positive-loss countries are majors currently at war. Cap the event's total contribution at 25. This is one world add after the sweep.

Read each country's positive national reserve before clearing it. Increment N at most once for that country. Increment W at most once if that same positive-loss country satisfies the native major and current-war predicates. Count countries rather than wars, opponents, or combat fronts.

The offline trigger reference supports `has_fuel > 0`, `is_major = yes`, and `has_war = yes`. Installed evidence must confirm the fuel predicate's precision for tiny positive reserves and the supported definition of a major. Do not convert `fuel_k`, which represents thousands, to an integer and accidentally discard small positive reserves.

Keep the counters transient. They describe one onset, not a global recovery service. Select one band, add the qualifying wartime supplement once, and call the verified shared world manifestation helper once with the same occurrence key or its supported deduplication context. Never multiply the contribution by the affected countries or stack another generic Event 109 manifestation award.

An empty-world occurrence still consumes its receipt and records its history. It contributes zero Chaos. Ordinary refilling, later shortages, oil competition, war effects, and Tasks outcomes do not trigger another Event 109 add or an Event 109 refund.

The shared manifestation helper's exact interface, precision, cap behavior, and source ownership remain implementation evidence requirements. No signature is prescribed here.

## The bounded connection to Tasks

The core wipe is independent of the availability of Event 101. The accepted connection is complete only when the Event 101 adapter and its achievement dependency are implemented against verified Tasks evidence. If Event 101 is unavailable, the core may proceed after its own gates, but the whole accepted Fuel Crisis feature must be reported as partially implemented.

When the verified adapter is enabled, capture the necessary onset context before fuel is cleared. Part 3 owns the player-only selection, the two alternative contracts, and their feasible candidate checks. Preserve pre-wipe D0, C0, positive F0, and occurrence membership for supported potential candidates. D0 describes active-commitment demand rather than the collapse of actual consumption caused by starvation. Missing native accessors are explicit blockers rather than reasons to substitute nominal trade, zero demand, or a guessed capacity.

Part 3's reserve contract uses a target of `min(14 × D0, 50% × C0)` in consistent verified fuel units and seven complete daily observed intervals. The selected qualifying action may be verified conservation or recurring supply improvement. Its dependable-oil alternative uses actual post-assignment source action and usable delivery measures with fourteen complete daily observed intervals. The first qualifying observation starts at zero elapsed days. A failed condition resets the hold, and a missed interval cannot be inferred from a later value or reconstructed on load. Daily observations do not establish every intraday value.

Deadlines adapt within 90–180 days using Part 3's feasible action lead and replenishment forecasts, a 30% uncertainty margin, applicable hold and completion allowances, and upward rounding to five days. Reject a rounded forecast longer than 180 days instead of clamping it to fit. Part 3 supplies the exact formulas and is the authority for eligibility, frozen assignment contracts, measurements, and expiry order.

Event 101 selects its player under its own rules. It may consider a Fuel Crisis candidate in the first 90 days after onset, but there is no guaranteed assignment and no reroll of a multiplayer recipient solely to obtain an eligible recovery country. Do not assign a mission to every affected country. At most one Fuel Crisis task may be issued to a country per occurrence.

Pass the same 109 receipt as the Tasks occurrence key after the world pass. This prevents a repeated callback from creating another task and lets the Tasks owner associate its terminal result with the original shock. Acknowledgment never creates the task.

Event 101 owns assignment probability, candidate selection, timing, progress evaluation, rewards, failure, terminal outcome, and cleanup. Event 109 owns only pre-wipe context capture and one accepted occurrence handoff. There is no new 109 global poller, recovery monitor, or AI mission assignment.

A fresh deliberate force occurrence replaces the old crisis context. The Tasks owner neutrally cancels any active contract from that replaced context, then applies its ordinary eligibility to the new receipt. Country disappearance, loss of human control, feature disablement, and technical invalidity follow the neutral lifecycle cancellation rules in Part 3. Ordinary campaign setbacks remain risks under the original contract. The adapter must not create a second terminal reward or failure path.

When Tasks is disabled, no player is eligible, an existing task prevents admission, or the Tasks owner declines the request, the wipe still happens. Do not force a replacement objective. When accessors or the adapter API are unverified, report the connection and the Tasks-dependent achievement as blocked. Do not manufacture compatible function names.

## Identity, registration, and shared consumers

Complete the parent-owned accepted ID migration before runtime registration or writing catalog rows from implementation. The inspected pre-migration catalog snapshot placed Custom Laws at 109 and Fuel Crisis at 114. The user accepted the uploaded Event 109 identity and authorized catalog migration on 24 October 2026, making 114 historical for Fuel Crisis. The parent owns the workbook and registry updates, including the displaced Custom Laws identity and any historical save records. Do not overwrite unrelated content or translate old 114 fired records automatically.

This documentation subtask does not edit the workbook. The parent owns the user-authorized catalog migration and should use `chaosx_spreadsheet_doc_worker` and the repository's XLSX workflow. The workbook is the editable catalog source. CSV snapshots remain exports.

Register the reconciled 109 identity as Minor Fire-Once through the existing category and all-events machinery. Its player-facing Chaos level 1 maps to internal `constant:chaos_meter_tier_id.tier_0` in the inspected repository. Eligibility level is distinct from the numeric onset manifestation contribution.

Cluster membership is Various Anomalies 11, Severe. This registration must preserve the event’s existing eligibility and ordinary occurrence admission. It does not authorize changes to its trigger, selection weights, repeat guards, or runtime hooks.

Keep the event name, debug name, shared event log, Event Details, history, localization, asset references, and catalog identity consistent. Do not infer a catalog status from this handoff or historical source snapshots. Parent-owned catalog work determines any future status statement.

Part 4 owns the one native announcement, its acknowledgment, the log image, and the difficult Tasks-dependent achievement. Shared log and details changes remain parent-owned framework integration. Their data consumers must be inspected and rendered when changed. No event-specific scripted window is introduced by this specification, so `chaosx_event_ui_worker` is not assigned shared framework work.

## Save and context ownership

Persistent consumed state survives ordinary save/load. Reload must not resend the sweep or allocate a new natural receipt. The shared system's full initializer clears fired records, so it is not a safe event migration shortcut. A narrowly verified registration or migration path must preserve trusted consumed state.

The occurrence belongs to the world, not to the survival of its coordinating country. Annexation, release, a civil war, a player tag switch, or the disappearance of the original host does not reset natural eligibility. Any pending country-scoped context and Tasks candidate must remain valid through the proven immediate handoff or be rejected before commit.

Later-created countries receive ordinary native creation and stockpile behavior. A country already existing during the sweep is included even if it is a dynamic tag. No annexation or country-creation callback performs a retrospective wipe.

History must identify the event and accepted occurrence without blaming the coordinating country. Optional actor context is presentation metadata. It must not become a prerequisite for keeping the world receipt consumed.

## Future Subagent Usage Map

The following assignments are for later authorized implementation and validation against this specification. Each role receives an explicit prompt with exact allowed paths, source revision, accepted requirements, available tool evidence, and a parent-specified handoff path. These are bounded assignments rather than authority to expand the event.

| Role | Purpose and owned files | Inputs and required outputs | Evidence and parent boundary |
| --- | --- | --- | --- |
| `chaosx_repo_explorer` | Resolve remaining uncertainty around installed references, occupied identity, native fuel behavior, and Event 101 paths. Writes only its assigned exploration report under the 109 plan directory | All five parts, pinned evidence, unresolved path list. Returns exact file map and dependency order | Read-only source and applicable MCP evidence. No implementation or catalog edits. Use only for the remaining uncertainties |
| `chaosx_scripted_system_architect` | Own a narrow 109 receipt and commit implementation if assigned. Candidate files are `events/109_fuel_crisis.txt` and parent-approved 109 effect, trigger, and constants definitions. Shared dispatch hooks are assigned individually | Accepted specification, native API proof, current dispatcher, verified manifestation helper. Returns exact changed files, context contract, and state-flow evidence | Event inspection, render, and comparison plus native evidence. Parent owns shared framework integration and final review |
| `chaosx_decision_mission_auditor` | Audit the two Event 101 contracts and adapter. Touch only exact 101 mission, trigger, effect, or decision files authorized after discovery | Part 3, frozen context contract, verified Tasks API and delivery accessors. Returns feasibility, admission, terminal outcome, and cleanup review | Decision and linked GUI evidence. Parent owns the broader Tasks system. No new 109 recovery service |
| `chaosx_ai_probability_auditor` | Read-only audit of changed shared candidate pools and Event 101 player selection. Writes only the assigned probability handoff | Exact before and after sources, complete or explicitly bounded candidate sets, named scenarios, immutable baseline hashes | Required probability inspection and matched evaluation or comparison. Does not patch weights or choose balance targets |
| `chaosx_localisation_auditor` | Own only assigned 109 keys in `localisation/english/_chaosx_events_l_english.yml` and any exact parent-approved shared text files | Part 4 text, actual runtime keys, state and consumer list. Returns concise prose and coverage audit | Source, encoding, and applicable render evidence. No mechanics changes and no unrelated text cleanup |
| `chaosx_asset_source_researcher` | Inspect period references and provenance if that source research is needed for the accepted generated depot scene. Owns only source notes and reference evidence | Part 4 scene constraints and exact intended consumers | Distinguish factual reference material from the fictional generated scene. Does not replace the accepted source mode or wire GFX |
| `chaosx_generated_event_art` | Produce the accepted generated depot scene and its report and news crops. Owns source image, processed assets, manifest, and GFX handoff | Part 4 scene direction, inspected native reference families, target sizes, runtime basenames, final destinations, and handoff path | Native-size processing and image review evidence. Parent owns GFX wiring and actual consumer review |
| `chaosx_icon_artist` | Produce the one achievement icon and required completed, grey, and not-eligible states under the current owner workflow | Part 4 achievement direction, immutable reference template, exact root consumer key, 64 by 64 target, and asset handoff | Source and template provenance, native-size comparison, DDS round-trip, and all state variants. Parent owns registry, localisation, and runtime wiring |
| `chaosx_spreadsheet_doc_worker` | Later update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Parent-approved identity reconciliation, exact rows and fields, final player-facing mirror text | Repository XLSX skill and workbook verification. No workbook write during this planning task and no Markdown documentation ownership |
| `chaosx_documentation_curator` | Reconcile 109 specifications, event documentation, evidence indexes, and plan handoffs | Accepted decisions, implementation dispositions, actual source and MCP artifacts. Returns a consistent completion and blocker record | Writes assigned documentation only. Parent decides acceptance and completion. No gameplay or workbook edits |
| `chaosx_improvement_loop_planner` | Perform the mandatory near-completion depth and scope review. Writes one bounded addendum or closure handoff under the 109 plan directory | Full specification, current implementation, accepted dispositions, assets, AI and Tasks evidence, and unresolved handoffs | Read-only required inspections and honest missing-tool report. Parent resolves every recommendation before completion and promotes accepted design into the specification |
| `chaosx_event_completion_auditor` | Read-only final audit across the five parts, code, assets, Tasks dependency, and validation evidence | Final source revision and all owner handoffs. Returns finished, partial, blocked, and missing surfaces separately | Required event and applicable consumer evidence. Cannot treat a functioning wipe as completion of a blocked Tasks adapter or achievement |

Spawn roles with `fork_turns="none"`, use the current supplied role profile and model, and pass complete explicit context. The parent owns overall integration, shared consumers, achievement wiring, final source review, and completion claims. The user performs live-game validation.

## MCP Usage Map

The supplied project role definitions document the tool names below. None was exposed as a callable HOI4 tool in this planning environment. Future work begins by inspecting actual capabilities and schemas, verifying service health, and selecting a supported route. Documented names are not a claim that an installed service is available.

| Surface | Documented route or required capability | Evidence required |
| --- | --- | --- |
| Opening event, receipt, world pass, and direct/force entry | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_inspect` (`mode = compare`) | Full relevant entry and helper expansion, state-flow evidence, supported event impact analysis, and matching before/after comparison. Retain unresolved native scheduling findings |
| Changed shared log, Event Details, or settings data consumer | `hoi4.gui_inspect`, `hoi4.gui_render` | Exact selectors, baseline and changed source identity, matching states, resolutions, scales, text, images, and click-region evidence. Use only documented render comparison support |
| Changed shared candidate pool and 101 player selection | `hoi4.probability_inspect`, `hoi4.probability_inspect`, `hoi4.probability_analyze` (`analysis = sweep`), `hoi4.probability_analyze` (`analysis = compare`), and `hoi4.probability_analyze` (`analysis = render`) as appropriate | Named scenarios, complete or bounded pool, immutable baseline and current source paths and hashes, eligibility changes, and matched comparisons. Distinguish scores from probabilities |
| Installed fuel setter, scope, precision, and event timing | Capability inspection first, then installed native documentation and the supported native analysis route | Exact build and documentation paths, supported parameter types, precision, national reserve versus unit buffers, and immediate handoff order |
| Save persistence and observed reserve values | Capability inspection first and the repository save-inspection workflow | Exact save identity, build, world country set, fuel representation, consumed state, and timing of each observation. Do not invent a save-tool name |
| Actual announcement and achievement consumers | Capability inspection first, then the documented inspection or rendering route for the real consumer | Consumer identity, event instance, asset and text coverage, acknowledgment behavior, and achievement dependency. A structural event graph alone does not establish visual correctness |

The deterministic setter has no outcome lottery. Probability work is confined to selection and candidate-pool surfaces affected by registration or the Tasks adapter. Do not analyze an invented AI policy distribution or create a special probability engine for fuel recovery.

MCP evidence must retain source revision, selectors, scenario identifiers or hashes, artifact references, relevant analysis bounds, and unsupported findings. Inspection does not replace source review or installed native documentation. A render does not prove a fuel state write. User observations do not replace the required documentary and MCP evidence.

## Scenario validation matrix

These are required evidence scenarios for later authorized validation. They are not tests performed during this planning task.

| Scenario | Required observation | Evidence owner and timing |
| --- | --- | --- |
| Mixed positive, empty, tiny, and very large reserves | Every existing national reserve is exactly zero at the end of one invocation, including the recipient. Empty countries remain included | Native documentation, MCP impact analysis, and later same-resolution save or state inspection |
| Upstream oil economy unchanged | Resources, control, access, refineries, silos, capacity, imports, trade, and fuel production rules retain their pre-event state | Matched source/state comparison before time advances |
| Ordinary recovery | A surplus country accumulates fuel on later native updates. A deficit country may remain short without a new event penalty | Later user validation with observed production, delivery, and consumption |
| Receipt delivered twice | First accepted delivery commits once. Second delivery changes no reserve, Chaos, Tasks, history, or pacing | Entry and shared-dispatch state-flow evidence, then a bounded duplicate scenario |
| All countries empty | One consumed occurrence, normal history, zero world Chaos contribution | Same-resolution count and manifestation evidence |
| Chaos bands and wartime supplement | N boundaries 0, 1, 2, 3, 9, and 10 select one band. W boundaries 1 and 2 add the supplement once. Total never exceeds 25 | Verified native predicates and one source-add trace |
| Save/load and registration migration | Consumed state and occurrence identity survive. Loading or registering 109 does not wipe again or reopen natural eligibility | Save inspection and narrowly scoped migration evidence |
| Deliberate force replay | Fresh force receipt clears newly recovered reserves once and receives its own occurrence accounting | Explicit force route evidence and later bounded replay observation |
| Force or raw debug before natural selection | The first committed occurrence consumes natural eligibility and cannot qualify the achievement. Later ordinary selection remains closed | Owner and shared fired-state comparison plus frozen receipt-origin evidence |
| Raw direct debug entry | Unused natural occurrence may commit once and account once. Later raw entry and duplicates are no-ops | Both debug entry states with owner and shared fired records |
| Country creation and annexation | Existing dynamic tags are included. Later-created tags are not retrospectively wiped. Host annexation cannot reopen the world occurrence | Scope and persistence analysis plus relevant supported observations |
| Multiplayer observers | One world commit, one shared history record, and at most one announcement per human observer regardless of acknowledgment timing | Supported multiplayer context analysis and later user-run observation |
| Tasks disabled or declined | Core wipe and natural recovery remain intact. No forced assignment, AI task, reward, failure, or 109 poller appears | Adapter gating and Tasks-owner admission evidence |
| Tasks enabled | D0/C0/F0 and occurrence membership captured before the wipe, verified player selection afterward, same instance key, one contract, complete daily observed holds, feasible adaptive deadline, one terminal outcome | Part 3 API/accessor evidence and 101-owned mission validation |
| Context ownership | Country predicates run on the iterated country, owner counters run on the owner, receipt survives the opening handoff, accounting has one owner | Exact scope trace and synchronous native handoff evidence |
| Achievement dependency | Part 4's achievement reacts only to the verified qualifying Tasks terminal outcome for the correct occurrence | Verified adapter and achievement consumer evidence. Blocked while Event 101 is unavailable |

No global country-recovery poller is needed to satisfy any scenario. Task-specific monitoring remains with Event 101. Validation must distinguish the immediate reserve postcondition from later production ticks and distinguish national stockpile loss from native unit-buffer behavior.

## Repository evidence and remaining gates

Targeted read-only inspection used `klimPaskov/Chaos-Redux` at commit `a3ef485c5da7e2337122eca04ac65c175050f251`, dated 2026-10-06T15:21:52Z. The packaged `109_fuel_crisis_repository_evidence.json` preserves the source register, Git blob identities, retrieved-copy hashes, and bounded identity searches. The evidence and decisions file records the source links and review limits.

| Finding | Exact pinned source |
| --- | --- |
| Direct fuel setter and ratio setter documented separately | `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, lines 1710 and 1718–1720 |
| Existing exact-zero mod use | `events/053_mysterious_man.txt`, line 54 |
| Existing cost helper mutates input and calls additive effect | `common/scripted_effects/chaosx_dynamic_effects.txt`, lines 752–755 |
| Every-scope iteration, existing-country restriction, ROOT and THIS, and country iterators | `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 45–51, 260–262, and 506–515 |
| Fuel getters are thousands and a capacity ratio | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 1516–1518 |
| Positive fuel, major, and war predicates | `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, lines 1522, 953, and 1077 |
| Offline immediate and no-delay event behavior | `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 182 and 194–203 |
| Level 1 maps to tier 0 | `common/scripted_effects/chaosx_logic_effects.txt`, lines 156–177 |
| Fired nonrepeatable exclusion | Same logic file, lines 860–884 |
| Handler guards fired append but still records history and pacing | Same logic file, lines 1129–1158 |
| Handler comment says zero, actual new_weight assignment is 1 | Same logic file, lines 1140–1142 |
| Force bypass, normal fired checks, explicit bypass lifetime, and manual dispatch context | `common/scripted_effects/chaosx_settings_effects.txt`, lines 1663–1671, 1683–1693, 1727–1729, and 1759–1763 |
| Generic event send precedes shared type accounting | Same settings file, lines 4938–4968 |
| Random Stuff uses the whole authoritative pool | `common/scripted_effects/chaosx_event_cluster_effects.txt`, lines 4234–4241 and 4344–4364 |
| Full initialization clears shared fired records | `common/scripted_effects/chaosx_logic_effects.txt`, lines 27–35 |

No 109 or 114 implementation was found in the inspected event filename listing, exact `nr109` and `nr114` code searches, or category registration. Both code searches returned zero with incomplete-results false. The events listing contained 162 entries. A recursive tree request failed, so this is a bounded inspection finding rather than proof covering all historical files.

Installed native documentation, callable HOI4 MCP tools, the verified Event 101 API and actual delivery accessors, matched native presentation evidence, and user live-game validation were unavailable here. No gameplay source was edited and no HOI4 process was launched.

Future implementation may mark a surface complete only against its own evidence. The core can be implemented separately from the blocked adapter, but the Event 101 connection and Tasks-dependent achievement remain visible completion blockers. Do not report catalog status from this historical handoff. The parent reviews implementation against the accepted specification and required validation.

