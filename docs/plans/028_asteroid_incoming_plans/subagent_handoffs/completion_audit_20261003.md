# Event 028 current completion audit, 2026-10-03

Disposition: **incomplete**, with implemented source tranches, concrete implementation gaps, provisional worker work, missing provenance, and blocked native evidence separated below.
This is a read-only completion audit, not a completion claim or design approval.
The parent owns review, integration, final documentation reconciliation, commits, and completion.
The auditor writes only this new report and does not edit gameplay, GFX, localisation, assets, audio, workbook, or parent documentation.
No game was launched, no other logs or saves were sought, and no user test was requested.

## Authority, source contract, and snapshot

Acceptance basis is the supplied parent/user instruction to implement every file in the Event 028 spec pack, including Part 10, the tuning matrix, and every AI-prompt case, without simplifications.
Spec location, historical status labels, earlier audits, and current implementation are not separate approval evidence.
All 23 files under `docs/specs/028_asteroid_incoming_specs/` were read completely: parts 1 through 10, specification index, tuning matrix, AI probability prompt, achievement prompt, asset prompt, decision/mission prompt, super-event prompt, coding prompt, goal prompt, catalog reconciliation, source crosswalk, design review, and research basis.
`AGENTS.md` and the complete event, subagent, improvement-loop, event-planning, event-assets, decision/mission, MTTH, super-event, and XLSX skills were applied.
No skill was changed.

The shared tree moved during this audit.
The snapshot below was captured at HEAD `cbeb25d4ffe892875674fd4454894bf1168b9e73`.
The runtime helper and decision file had concurrent uncommitted changes, so HEAD alone does not identify the inspected bytes.
Line references below identify these inspected files, not an immutable future revision.
The parent later explicitly confirmed the history lookup was implemented, and the architect delivered an updated actual-source handoff during this audit.
That correction is honored rather than repeating the earlier scan defect as current.

| Inspected file | SHA-256 |
| --- | --- |
| `events/028_asteroid_impact.txt` | `E9C436B8D1393F354BF5BE6235CCC2FB4205E0413309EAAD7DAF60267F9BA943` |
| `common/scripted_effects/028_asteroid_incoming_effects.txt` | `44A5519E86A8E6FCAAF0C681F84ECC77D365383A7CD4092D3D9CB450FAD08A44` |
| `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` | `0A902614C03D060B159DADBA42C706D3C203CB0F448884E7AB10AC4BF2643214` |
| `common/scripted_effects/028_asteroid_incoming_recovery_effects.txt` | `74CE4D5EA35D22894713B88AFA32C97E9FA1F6C1C2BB000035A0AC6E7CB1C34F` |
| `common/scripted_effects/028_asteroid_incoming_capital_effects.txt` | `A54F762738B32671B3E7A64F87BCF3470989562C41D031822B5B0716504E2D8B` |
| `common/scripted_triggers/028_asteroid_incoming_triggers.txt` | `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B` |
| `common/decisions/028_asteroid_incoming_decisions.txt`, provisional changes included | `E954ED3B45307AD519E773D4F7F0B7FB5898D386B4CB95BACE173248A929C6FD` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67` |
| Exported event CSV | `465050976A1134E57945CEC56E95232E6C54FA2A8B4C5A3B569B0D638230D2C0` |

The new crater effect/trigger/dynamic-modifier files and decision hooks remain owned by the decision worker and explicitly unintegrated.
Their source presence, changing tooltips, and preliminary tests do not close the corresponding requirements.
The new asset manifest/crosswalk/GFX handoff belong to the separate documentation curator.
Their creation repairs missing documentation links but does not recover absent source images or establish visual/native acceptance.

## Completion by surface

| Surface | Status | Current proof and practical limit |
| --- | --- | --- |
| Major registration, Calm World preflight, three-pair board, cancellation | Implemented source tranche, native blocked | Root `.1`, internal return board `.8`, viable-pair predicates, dispatcher readiness gate, and 19 source scenarios exist. Native selection, pause, fire-once, and multiplayer behavior remain unproved. |
| Two-day geographic lock | Partial | Saved state survives original-country changes in source. Current-capital continuity exists, but loss of all backups after lock and historical display snapshots remain gaps. |
| Main/fragment damage and Deaths | Partial | Strongest-profile planner, exact before/after population receipts, separate Deaths reasons, and building inventory exist. Helper-output lifetime, repeated building damage, long-array processing, permanent-state project handling, documented nuclear detonation versus visual-only intent, and native transactions are unresolved. |
| Fragment eligibility and evolution toggles | Partial | Threshold/count/geographic separation logic exists. Fragment owner/controller classification and current enable-state checks at impact are incomplete. |
| Dust, national protection, Air Cleanliness | Implemented repairs with remaining gaps | Current-stage 15/30/45% compensation, weather sign, historical injection preservation, monthly pressure, and pre-cleanup reconnection award exist. Strategic destruction is absent from opening dust calculation. Full tuning/lifecycle scenarios remain unrun natively. |
| Event 013 aftermath | Source wiring present, delivery blocked | One exact family/group/origin contract and four accepted scheduled calls are configured. Actual job delivery, downstream effects, receipts, and cleanup have no current native evidence. |
| Recovery decisions/missions | Partial | Exact country-owned target reservations and cancellation exist. Flat costs, one-state substitutes for broader objectives, emergency expiry, and mapped failure consequences remain gaps. |
| Crater actions | Partial, worker WIP | Committed wrappers still include flag-only outcomes. New physical outcomes are provisional and wrappers/lifecycle integration remain parent work. Supplied-garrison proof is blocked. |
| Current-control armour | Source implemented for the generated site set, native blocked | Main +100% and each of up to six generated fragments +20% are rebuilt from current control. No additional cap appears inside that six-site plan. Zero-base armour, land-only scope, piercing thresholds, peace/annex/civil-war transfer, and high-stack native behavior remain unproved. |
| Achievements | Partial | Five root-registry entries and persistent award flags exist. Near-miss settings repair passes 16 source cases. Government recovery inherits the incomplete mission proof. Geographic evolution eligibility and all persistence/conquest/reset scenarios remain open. |
| History, Event Details, reports, news | Partial | One-row outcome data update exists and parent applied direct history lookup. Event028-specific Details/history/evolution selectors are absent from current shared consumers, affected-country count is cleared too soon, and historical names/flags are not frozen. |
| Visual package | Wired runtime, provenance blocked | 52 DDS files and their consumers are recorded. Missing commissioned masters, unknown inherited news provenance, achievement process lineage, and overwritten rejected evidence prevent full asset completion. |
| Super-event audio | Source package/wiring present, playback unrun | Unique slot 116 WAV, source/rights notes, music catalog, and six volume wrappers exist. Current WAV hash matches the research note. Text research requirements remain unfulfilled in the supplied records. |
| AI/probability | Blocked specialist evidence | Existing specialist owns every weighted surface. No current numeric ranking, full sweep, or baseline/current comparison can be claimed from this audit. |
| Documentation/catalog/commits | Partial | Parent tranches are committed, workbook row and export agree, curator records are new. Catalog wording differs from runtime Details, several source descriptions overstate implementation, and WIP tranches have not been accepted/committed. |

The accepted design uses an ordinary category with a static picture and explicitly rejects a dedicated Event 028 GUI, new focus tree/country/formable, custom model, third evolution, terminal route, and manual scenario in `design_review.md:122`.
No `chaosx_event_ui_worker`, portrait, custom-unit audio/counter, 3D, animation, focus-tree, or unrelated GUI requirement is invented by this audit.
Shared event-log/details/settings/super-event frameworks remain parent-owned.

## Concrete implementation findings

### F01. Required temporary helper outputs are not initialized in their callers

Severity: high, source-contract failure with runtime outcome unobserved.
Contract: Part 3 population/building transaction and actual-loss acceptance, coding prompt:41, plus `chaos-redux-events/SKILL.md:163` helper-output lifetime.

`028_asteroid_incoming_effects.txt:1160` calls `asteroid_incoming_load_profile_fractions` at :1170, then population/building consumers at :1171 and :1172.
The four fraction outputs are first created inside `asteroid_incoming_load_profile_fractions` at :462 to :465.
No caller-side initialization of those output names was found in the current event sources.
Likewise `asteroid_incoming_prepare_selected_building_loss` first creates `asteroid_incoming_remove_levels` at :596, and callers such as :711 immediately use the result in the next helper.
`asteroid_incoming_capture_selected_building_receipt` first creates `asteroid_incoming_selected_actual` at :646, while :715 consumes it after return.
The lock-result output is first created in `asteroid_incoming_lock_candidate_pair` at :105, then consumed by runtime acceptance at :559.

Offline Data structures:440 explicitly warns that first-created temporary values may disappear on scripted-helper return and says prior caller initialization preserves modifications.
This is not proof of an observed zero-loss impact, but it invalidates an unconditional completion claim for the physical transaction and lock.
Narrow action: parent initialize consumed outputs at every relevant call boundary and audit nested meta/helper outputs under conservative call-frame cleanup, then retain actual-source and native transaction evidence.
No change to damage percentages or balance target is needed.

### F02. Capital failure after lock does not stop center destruction

Severity: high, confirmed source control-flow gap.
Contract: Part 2:160 to :182, Part 3:152 to :158, Part 10:171.

`028_asteroid_incoming_capital_effects.txt:151` finds the country whose current documented capital pointer is the locked state and selects a fully controlled surviving candidate.
At :205 or :207 it sets `asteroid_incoming_capital_relocation_failed` when relocation or backup selection fails.
`028_asteroid_incoming_runtime_effects.txt:1330` calls that helper, then proceeds through :1333 to :1344 to physical destruction without checking the failure flag.
`asteroid_incoming_locked_target_pair_is_valid` in triggers:160 only checks the locked state and living owner/controller, not the current capital owner's surviving backup.

A valid country can lose its last usable backup during the two-day lock, leaving this branch unprotected.
The 23 capital source cases cover ranking, current actual capital, recipient attribution, and planned-fragment backups, not a safe resolution of that late-loss contingency.
Narrow action: parent prevent the destructive transaction from continuing on relocation failure and resolve the post-lock contingency consistently with fixed coordinates and no redirection.
If extending the accepted fail-closed contingency is necessary, record that explicit disposition rather than silently leaving an active government without viable capital territory.
Annexer identity must remain distinct from the original target.

### F03. Fragment centers lack actual-nonhuman and system-country exclusions

Severity: high, confirmed eligibility gap added by the parent's current instruction.
Contract: Part 5:44 to :59 and Part 2's target classification distinction.

`asteroid_incoming_state_is_valid_fragment_site` in triggers:261 calls `asteroid_incoming_state_is_valid_target` at :269.
That generic predicate at :44 checks terrain, population/settlement, wasteland/site state, and `OWNER`/`CONTROLLER` existence at :52 and :53.
It does not check either country against `is_actual_nonhuman_country`, CXT, or another system-only identity.
The neighbor preference at :295 similarly only requires owner/controller existence.
All fragment `random_state` paths in runtime:774, :804, :831, and :840 use `asteroid_incoming_state_is_valid_fragment_selection` at triggers:309 and inherit this gap.
Main-country filtering at triggers:59 is not called by this fragment route.

The shared actual-nonhuman classifier is distinct from `is_special_chaos_country` at `chaosx_dynamic_triggers.txt:40` and :10.
Using the broad Special Chaos exclusion would incorrectly discard ordinary human societies.
Narrow action: parent define/verify the bounded system-only exclusions and apply actual-nonhuman checks to both fragment owner and controller without excluding human Special Chaos actors.
This changes candidate eligibility, so the existing probability specialist must capture the baseline and compare the owner-applied patch under identical named scenarios.
The auditor has sent this exact finding to specialist `01a100d6-07b6-7d42-b3a0-fa58cf98f322` and has not patched it or selected a tuning target.

### F04. Impact evolutions still use stale opening eligibility after settings change

Severity: high, confirmed source gate gap.
Contract: Part 5:10, :206 to :211, and event skill's same-limit enable gate.

The opening stores `asteroid_incoming_evolution_i_eligible` and `_ii_eligible` in `events/028_asteroid_impact.txt:48` to :81.
At impact, runtime:685 requires the I snapshot plus `asteroid_incoming_fragmentation_is_enabled`.
Despite its name, that trigger at :912 only checks current Chaos >=600.
It does not query the shared evolution toggle.
Event `.4` activates minerals at event:331 to :340 from the II snapshot and applied-fragment flag without rechecking current II enablement or the current 800 threshold.
Evolution recorded flags are set at event:362 and :375 outside a current-enable limit.

Disabling I or II after opening/confirmation can therefore leave evolved physical behavior or internal recorded state despite the disabled setting.
The recent near-miss repair correctly rechecks both current settings, but it does not fix the impact route.
Narrow action: parent use the shared current enable contract at the final pre-resolution gates and recorded-flag gate, preserving clean baseline impact when I is disabled and retaining fragmented damage without minerals when only II is disabled.
Record the intended threshold snapshot/current policy because the present I and II threshold handling differs.
Any probability-bearing eligibility change needs the existing specialist baseline/compare cycle.

### F05. Repeated building tokens receive more than one damage pass

Severity: high, confirmed duplicate source dispatch, with executed losses unobserved.
Contract: Part 3:56 to :67, tuning matrix:11 to :26 and :69, strongest single-profile physical receipt.

`028_asteroid_incoming_effects.txt:688` explicitly damages building families, then :1071 adds another strategic-inventory pass.
Repeated tokens include `naval_base` (:772 and :1139), reactors, rocket sites, all three special facilities, dams, canals, biological/chemical facilities, and camp-site anchors.
Sixteen tokens occur twice in that applicator.
The second pass reads remaining levels and applies another fraction, so it is not merely another registration or presentation consumer.

For example, Ring 2 has logistics fraction 0.55 and strategic fraction 0.50 in constants:335 and :336.
With four naval-base levels and the declared rounding, the first pass requests two and the later strategic pass requests one of the remaining two, giving three removed levels instead of one category's intended profile.
That source arithmetic exceeds the 45% to 65% Ring 2 logistics band.
This example is a source-model implication, not an observed engine result.
Narrow action: parent deduplicate the inventory by token and assign one category fraction and one before/after receipt per physical building surface.
Also verify province-based buildings, rail segments, facilities, and queued state projects against the actual native consumer rather than assuming an aggregate building reader proves all installations are gone.
The source comment at :1158 explicitly leaves project clearing to the parent, and no complete project-invalidation proof was found.

### F06. Historical country name and flag are pointers, not a saved display snapshot

Severity: high, confirmed source representation gap.
Contract: Part 2:96 to :106 and :114 to :123, Part 8:190 to :199, Part 10:226.

`asteroid_incoming_accept_selected_target` at runtime:540 to :555 saves the country pointer, country ID, state pointer/ID, and capital boolean.
It does not freeze the historical display name or flag/cosmetic context.
Event:378 saves that live country as the super-event target.
Localisation:67, :92, :96, and :348 calls live `GetName` on country/state targets or a history actor.
Cosmetic/name changes can rewrite the historical intended target, and an absent target has no explicit historical-name fallback in these strings.

Narrow action: parent provide an engine-supported durable historical name/flag representation and a former-target presentation path, keeping live crater controller data separate.
Do not clone a country or replace original-target identity with the annexer just to display a name.
The required native cosmetic-change/annexation rendering evidence remains missing.

### F07. Cleanup erases the affected-country count before consumers display it

Severity: high, confirmed lifetime gap.
Contract: Part 3 country aggregation, Part 8:131 to :168, Part 10:183.

The country aggregation appends unique recipients to `global.asteroid_incoming_affected_country_entries` at effects:1211.
Event `.4` schedules `chaosx.news.32` for the next day at event:397, then calls `asteroid_incoming_cleanup_transaction` at :414.
That cleanup clears the recipient array at effects:1618.
Global impact news localisation:67 and the currently unwired intended Event Details string at :92 read that array's `^num`.
The value becomes zero after cleanup even when reports were queued for multiple countries.

Narrow action: parent persist the finalized unique-country total before clearing working arrays and bind historical/global text to that receipt.
Retain the one-country-report-per-incident dispatch rather than keeping transient arrays forever or appending extra normal history rows.

### F08. Logistical costs and transport preservation remain flat substitutes

Severity: high, confirmed design shortfall.
Contract: Part 6:254 to :262, tuning matrix:147 to :157, Part 2 transport stance and tuning matrix:131.

Constants:109 to :150 define the same one civilian factory, 80 support equipment, 60 trucks, 800 manpower, two trains, 300 fuel, twenty convoys, and fixed prepared alternatives.
Decision hospital affordability/payment at decisions:49 and :103 to :112 consumes those literals through constants.
Rail payment at :212 to :221 follows the same fixed/prepared split.
No incident-population/state-count/distance/industry/dust-stage quote calculation governs these amounts.
Civilian-factory use is a literal one and ordinary commitment is thirty days at decisions:68 and constants:96.
Reserve floors are useful protection but do not implement capacity- and incident-scaled cost.

The transport stance at runtime:662 to :668 grants fixed trains/support/trucks/fuel without a snapshot of movable reserve at risk or a matching loss/prevention receipt.
This is a stockpile grant, not evidenced preservation of a bounded share of otherwise disrupted reserves.
Narrow action: parent implement coherent scaled quotes shared by display, affordability and debit, retain four spendable-type limits/reserve floors, and use real at-risk reserve accounting for the stance.
Do not change fixed population or armour anchors.

### F09. National and regional missions are reduced to one-state floor tests

Severity: high, confirmed unapproved simplification.
Contract: Part 6:108 to :180, achievement 2 conditions in Part 10:43 to :55.

`asteroid_incoming_stabilize_zone_mission_conditions_met` at triggers:729 tests one `asteroid_incoming_recovery_target_state`, not the two worst states.
Network conditions at :749 check one state's infrastructure/rail/supply and one capital connection, not the national network linking major industry and damaged states.
Outer-ring conditions at :768 check absence of two modifiers and a factory floor in one saved state, not all Ring 3/light-fragment states and the Ring 2 threshold.
Regional economy conditions at :790 require fixed floors in one state, not a meaningful restored share of surviving pre-impact regional capacity.
The pre-impact per-state receipts at effects:694 exist but are not used as this mission's comparison baseline.

Success helpers at recovery:632, :677, and :700 publish national completion/legacy flags from those one-state checks.
Government achievement at runtime:2006 accepts the resulting network/outer flags, so it inherits insufficient recovery proof.
The deadlines delay completion but do not add missing objective coverage.
Rail-route cancellation is present, so this audit does not claim the route can be absent throughout the hold.
Actual supply status and continuously maintained thresholds still lack a full acceptance scenario.
Narrow action: parent bind each accepted objective to its bounded incident state/route set and snapshot share, preserve country-local reservations, and publish national flags only after the full accepted proof.
Verify native success versus timeout ordering because completion-day thresholds and static native timeouts coincide.

### F10. Emergency expiry and specified failure consequences are incomplete

Severity: medium/high, source gaps with worker repair still provisional.
Contract: Part 3:101 to :114 and :236 to :240, Part 6:26, :118 to :130, and :280 to :298.

Committed `asteroid_incoming_emergency_action_state_is_valid` at triggers:577 requires an affected repairable state and absence of `asteroid_incoming_local_emergency_resolved`.
It does not test whether rescue burden and relevant timed emergency modifiers have expired.
Natural rescue completion at runtime:1120 to :1132 clears rescue flags but does not set the local emergency-resolution flag.
That can keep the emergency surface at triggers:417 open and reconstruction/dust phases suppressed after the burden ends.
The decision worker's emergency-burden predicate is not yet parent-integrated.

`asteroid_incoming_recovery_mission_failure` at recovery:655 adds timed pressure and clears the target.
It does not perform the specified failure death receipt, target recovery extension, or bounded future repair-cost escalation.
The monthly casualty path is separately bounded but does not prove a mission-specific failure outcome.
Narrow action: parent integrate the reviewed expiry predicate and implement the accepted failure outcomes against exact incident receipts, with idempotent cancellation/timeout and no punishment from stale callbacks.

### F11. Crater outcomes remain flag-only until wrappers and lifecycle are integrated

Severity: high, current committed outcome gaps and unintegrated repair.
Contract: Part 6:216 to :252 and no-flag-only-outcome requirement in the parent assignment.

Committed recovery helpers at :542, :554, :592, :605, and :619 set security/survey/reconnaissance/disruption/offensive flags without the promised physical/intelligence/research/supply/combat effects.
The old access helper at :567 adds one infrastructure level to every controlled normal neighbor, without bounded forts or a two-access-state plan.
Current decision hooks still call these old helper names while new worker effects have distinct `asteroid_incoming_apply_crater_*` and `asteroid_incoming_apply_rival_crater_*` entry points.
The parent explicitly retains wrapper/lifecycle integration after review.

Worker WIP includes original-site intel, local supply disruption, bounded forts, survey and offensive effects, separate delayed receipts, and read-only emergency predicates.
Those changes are not accepted final behavior merely because provisional `.txt` files and updated tooltips exist.
Its division-placement trigger at crater_triggers:175 uses `divisions_in_state` but explicitly states at :173 that it does not prove those divisions are supplied.
The installed `num_divisions_in_states` documentation at triggers_documentation:6626 likewise does not document a supplied-status filter.

Narrow action: parent review and integrate every mapped wrapper, source and receipt lifecycle, then audit control churn and delayed callbacks.
Exact supplied-garrison support remains a dependency requiring defensible engine evidence or an explicitly accepted design disposition.
Do not quietly replace supplied divisions with national army size, division placement alone, or a supply-hub flag.

### F12. Strategic destruction does not contribute to opening Dust Load

Severity: medium/high, confirmed formula omission.
Contract: Part 4:13 to :25 and tuning matrix:62.

Runtime:1201 accumulates `global.asteroid_incoming_destroyed_strategic_levels`.
`asteroid_incoming_recalculate_dust` at :1354 uses deaths, industry, logistics, footprint, fragment and secondary points, but never adds that strategic total.
Radar, forts, anti-air and other strategic installations therefore do not feed the accepted bounded logistics/strategic destruction contributor.
Narrow action: parent include the intended unique physical levels in the existing bounded contributor, after deduplicating F05, without creating another public currency or counting one building twice.

### F13. Footprint array scans can truncate at the installed 1000-iteration ceiling

Severity: high for the declared large-array scenario, actual affected footprint size unobserved.
Contract: process every affected state once, Part 7 performance rules, parent request for source arrays >1000.

`asteroid_incoming_record_footprint_profile` at effects:204 searches an arbitrarily sized footprint using `while_loop_effect`.
`asteroid_incoming_process_footprint` at runtime:1333 also iterates one array index per while-loop iteration.
Installed defines:25 fixes `MAX_EFFECT_ITERATION = 1000`.
No continuation, batching, hard proof that every possible footprint is <=1000, or failure on incomplete processing was found.
The subsequent cleanup clears the arrays.
An entry at index 1000 cannot be reached by the current while-loop pass.
This is a proven boundary in the source model, not a claim that an observed normal impact reached 1001 states.

The separate history lookup defect has been repaired by the parent with sequence difference, both identity checks, individual array bounds, and impact-secondary bounds.
That removes the Event 028 row search ceiling, but not these physical loops or the shared sanitizer's coverage limit.
Narrow action: parent use a verified scope iterator or bounded continuation batches for all supported large arrays and retain 999/1000/1001 fixtures.
Do not silently cap the accepted physical footprint.

### F14. Near-miss settings proof is improved, but true geographic eligibility is still missing

Severity: medium/high, partial achievement contract.
Contract: Part 10:17 to :27 and Part 5:27 to :29.

The current near-miss path rechecks both shared toggles and correctly suppresses the award after either is disabled.
Sixteen actual-source award cases pass and the non-award miss body equals its before version.
However, opening `_eligible` flags at event:48 to :81 represent threshold and toggle state, not the minimum of two valid separated fragment centers.
No pre-miss geographic eligibility proof is consumed at runtime:319 to :321.
The repaired source test does not contain a less-than-two-valid-fragments eligibility case.
Narrow action: parent settle the precise pre-choice eligibility rule for the dangerous form and evaluate it read-only without generating fragments on a miss.
Any candidate-pool change must use the specialist baseline/compare route.
The existing miss body has no physical damage, dust, fragment, crater-material, nuclear, or hidden punishment calls.
That source finding is separate from unrun native no-aftermath scenarios at every Chaos tier.

### F15. Required asset lineage is missing despite wired DDS files

Severity: completion blocker.
Contract: Part 9:181, asset prompt:134 to :144, Part 10:228 to :229, asset skill manifest/candidate-lineage and achievement processing contracts.

The curator's new `asset_records_20261003.md:179` records 45 missing explicit commissioned-master links: the selected category source plus 44 state/idea/decision/achievement source paths.
The inherited impact-news original master, author/source/rights are separately unknown.
Report/news-close-passage/super-event sources survive, but their full tool/candidate lineage has not been independently reverified.
The accepted category DDS survives while its retained prompt describes the rejected train/tent candidate, not the accepted crater/rail source.
Four rejected category evidence files were overwritten, as disclosed at `final_audit.md:99`, and no external recovery source was supplied.
The achievement worker reports independently generated states, while the current skill requires one transparent subject with deterministic grey/not-eligible derivation and canonical template equality.
Current DDS triplets and native round trips do not reconstruct missing source-process proof.

`manifest.md`, `coverage_crosswalk.md`, and `gfx_handoff.md` now exist and identify exact requirements/consumers.
This is a useful documentation repair, not final asset approval.
Narrow action: parent review the curator handoff, recover original masters/receipts and correct lineage where possible, or commission a compliant final replacement package within the accepted visual brief.
Keep irreversible rejected-evidence loss and inherited-news uncertainty explicit.
An exception or weaker provenance standard requires an explicit disposition under the no-simplification instruction.
Keep the temporary workspace while blocked and promote durable facts before authorized final cleanup.

### F16. Super-event text research requirements have no durable proof

Severity: completion blocker.
Contract: super-event prompt:13 to :33, :74, coding prompt:47.

The research file `docs/super_events/028_asteroid_incoming_super_event_research.md:7` explicitly covers only audio.
It contains a substantial audio candidate/rights/conversion package, not eight quote candidates, five remark candidates, exact selected-text source/translation evidence, or text-worker handoff.
Runtime localisation:346 uses a Francis Bacon quotation and :347 uses a remark.
The localisation handoff at :68 and :69 calls them verified/sourced but gives no corresponding source-page/edition/attribution evidence in the Event 028 records searched.
This audit does not call the quotation false, and it does not invent a source for the remark.
Narrow action: parent obtain the required bounded `chaosx_super_event_text_researcher` record and reconcile the exact shipped title/quote/remark with it before text completion.

### F17. Catalog wording and some parent source-completion claims are stale

Severity: medium, concrete documentation/catalog gap.
Contract: event skill's exact spreadsheet/Details alignment, catalog reconciliation:56, Part 10:233 to :236.

The authoritative workbook was read with `read_only=True` and was not saved.
Event 028 is row 29, with `Major`, Calm World level `1`, blank cluster, and `Needs Testing`.
Its C29 Details and evolution cells agree with the currently exported CSV row.
They do not equal the intended Event028 `asteroid_incoming.event_details.description` at localisation:85.
C29 begins with an implementation/recording description and lists recorded deaths/destruction/recovery/control surfaces, while that intended string has different wording.
The string itself is currently unwired, as F19 confirms, so this is not represented as a comparison with a successfully rendered native Details panel.
Evolutions include tier/threshold/stage metadata around their prose, so exact runtime-wording alignment must be verified through the owning selectors rather than inferred from matching meaning.
The export's current hash differs from the historical export hash in `final_audit.md:85`, so that older export record is not current-byte evidence.

`overview.md:23` calls current-control stacking uncapped, :25 describes complete meaningful recovery behavior, and :35 formerly referenced absent records.
The record references have been repaired by the curator, but F08 to F12 remain implementation gaps rather than tooling-only future work.
The historical `final_audit.md` is explicit about incompletion and some known gaps, but its broad implemented-source paragraph at :34 and late artifacts do not prove the current requirement set.
Narrow action: after parent integration facts and final wording are available, route exact workbook/localisation alignment to the spreadsheet worker, regenerate all exports, and reconcile parent docs and acceptance tables.
Do not promote `Playable` or default enablement from this audit.

### F18. The explosion call is documented as nuclear detonation, not presentation only

Severity: high, unsupported visual-only completion claim, with actual native consequences unobserved.
Contract: Part 3:198 to :215, Part 9:9 to :21, Part 10:207 to :212.

Runtime:1220 and :1271 call `launch_nuke`, with thermonuclear/nuclear bomb type respectively and `use_nuke = no`.
Installed `effects_documentation.md:4745` to :4760 describes that effect as launching a nuke at a state/province.
Its `use_nuke` comment at :4756 refers only to consuming a nuke from stockpile.
Offline `Effects - Hearts of Iron 4 Wiki.md:1517` likewise says it nukes the selected province and defines `use_nuke` only as stockpile deduction.
The project precedent at `023_sov_nuclear_bombs_runtime_effects.txt:703` explicitly says `launch_nuke` detonates.
Neither reference documents a presentation-only switch in the call used by Event028.

The event-specific global guard can suppress guarded custom nuclear callbacks while it is set.
It does not demonstrate suppression of native detonation damage, engine statistics, native achievements, or delayed callbacks.
The fragment call also occurs after Event028's measured building/population receipt, so any native physical consequence would be outside that measured asteroid transaction.
This audit does not fabricate an executed secondary loss or nuclear achievement.
It rejects the inference that `use_nuke = no` proves visual-only behavior.
Narrow action: parent establish a verified presentation-only explosion route that preserves the accepted visual scale, or retain an explicit engine-capability blocker until supported behavior is proven.
Do not silently remove the requested visual, replace it with a weaker fallback, or label detonation as accepted presentation without evidence.

### F19. Current shared consumers do not expose the event's Details/history/evolution text

Severity: high, confirmed integration gap.
Contract: Part 8:125 to :199 and Part 10:225, plus event skill's complete log/details/evolution contract.

`GetEventsLogEventDetailDescription` is defined in `chaosx_scripted_localisation_events_log.txt:5728`.
It has no Event028/`asteroid_incoming_event.id` branch and ends with `always = yes` generic fallback at :6882 to :6884.
`chaosx_gui_l_english.yml:634` calls this selector and :635 says no additional event detail is recorded.
An exact runtime search of `common`, `interface`, and localisation outside the owning Event028 YML finds no consumers of `asteroid_incoming.event_details.*`, `asteroid_incoming.history.*`, or `asteroid_incoming.evolution.*`.
The constants define distinct evolution types 2801/2802 at `028_asteroid_incoming_constants.txt:456` and :457, but current shared log effect/localisation/GUI sources have no matching type registration or selector branch.
The shared helper `events_log_add_event_detail_evolution_preview` at log effects:2934 appends requested preview rows, but no Event028 call to supply those two rows was found.

Event name mapping, N/A reasons, the shared history-sequence binding at effects:796 to :797, and the raw evolution recorder calls do exist.
Those narrower surfaces do not expose the required premise, outcome-specific details, controller summary, two toggleable preview rows, named logged evolutions, and related history views.
The controller-summary getter in the Event028 localisation file is reached by its intended Details strings, which are currently unused.
Narrow action: parent restore/integrate exact Event028 branches and preview rows in the existing shared framework, including all current/history/selected-detail evolution text and toggle coverage, without appending duplicate Major history or introducing a dedicated GUI.
Then align the workbook to the actual final visible text and retain current MCP/source/native limits.

## Implemented tranches and accepted-plan disposition

| Plan or handoff | Disposition | Evidence / remaining dependency |
| --- | --- | --- |
| Original 23-file design pack | Accepted source contract under the supplied user instruction, partially implemented | All mapped content stays required. No smaller substitute or additional broad design is accepted here. |
| `dust_and_achievement_repair_20261003.md` | Implemented source tranche | Commit `21a6b80769c905a3cc3d1316886bf9571c991131`, current-stage protection, no opening refund, four accepted Event 013 calls, elapsed holds, award-before-cleanup, independent reservations. Native and broader acceptance remain open. |
| `availability_20261003/repair.md` | Implemented source tranche | Commit `829f4db894d90a08570e5483377189ca51638771`, three-country preflight, `.8` return board, dispatch ordering, current-capital helper integration. 19 availability cases freshly rerun. F02 remains. |
| `subagent_handoffs/capital_continuity_20261003.md` | Implemented source helper tranche | Parent integration and 23 source cases are attributed evidence. Exact native capital/annexer movement and late no-backup disposition remain unresolved. |
| `near_miss_selection_20261003.md` | Implemented source tranche | Commit `e0598a512291568dc79596a91acb428f9796f99c`, 16 freshly rerun cases and unchanged non-award miss body. F14 and native acceptance remain. |
| `state_icon_placement_20261003.md` | Implemented asset placement tranche | Commit `cdc3afb452bdeb74924389561b0d5bb6552c6930`, seven byte-preserved DDS moves, eight paths, native 32x32 reopen/equality. Does not recover masters. |
| `subagent_handoffs/history_lookup_20261003.md` | Parent-applied source repair, actual-source audit verified, parent commit pending | Current runtime:382 uses direct sequence difference with identity and column bounds. Updated handoff records acceptance and actual before/after AST execution. Auditor freshly reran all 22 cases, including indices 1000 and 1500, missing-column rejection and unchanged matched writes/tail. Native acceptance remains blocked. |
| `subagent_handoffs/architect_recovery_target_isolation_20261003.md` | Implemented source repair | Persistent country-local pointer, paid-project reservation, and local lifecycle cleanup are present at recovery:194 to :296. Seven source-model cases are attributed, native evidence blocked. |
| Decision worker crater/action tranche | Unresolved WIP, not parent-integrated | Exact helper wrappers, lifecycle, supplied-unit dependency, current source tests, handoff, probability comparisons and parent review remain. Do not commit it as finished from this audit. |
| `subagent_handoffs/asset_records_20261003.md` | Implemented documentation repair, parent review/commit pending | New manifest/crosswalk/GFX handoff and permanent snapshot exist. Provenance/native acceptance remain blocked. |
| Earlier explorer/icon/art/localisation/spreadsheet/baseline handoffs | Historical evidence, superseded where current source differs | Preserve useful provenance and named scenarios. Do not use early unwired/missing-source or verification claims as current approval. Curator dispositions identify exact replacements. |
| Manual design-review improvement list | Accepted through current full-package user direction | Its accepted improvements are mapped into Parts 1 to 10. Rejected bloat remains rejected. No new improvement plan is needed to conceal these already specified gaps. |

The auditor performs no staging or commits.
Existing finished tranches have the explicit parent commits above.
Unfinished gameplay and documentation tranches need handoff, parent review, relevant validation, and a scoped parent commit when finished.

## Meaningful validation performed and limits

Fresh read-only execution:

- `python -B .tools/validation/validate_028_availability.py --fixture docs/plans/028_asteroid_incoming_plans/availability_20261003/source_scenarios.json`: **19 source-model cases pass**, including distinct country count, occupied/empty/wasteland/transferred/contested backups, partial center with valid full-control backup, nonhuman/CXT exclusions, friendly relationships, pending/resolved/opening guards, matching `.1`/`.8` option bodies, and preflight-before-dispatch/accounting ordering.
- `python -B .tools/validation/validate_028_near_miss.py`: **16 actual-source award cases pass**, including each current toggle disabled after opening, low Chaos, missing previews, prior aftermath, manual/debug/force/AI/nonhuman rejection, and enabled 800/900 cases.
  It also proves unchanged non-award miss operations relative to its exact before commit, with before runtime SHA-256 `29c86060bc17499b5d0132c4d5ed4428e0e245fefa72dd82c7670a8645aff10c`.
- The authoritative workbook was opened read-only and Event028 row 29 was compared with the exported event CSV row.
  Values agree with each other, but intended Event028 wording differs and current visible selector integration is absent as F17/F19 record.
- The actual final WAV hash was checked and equals research SHA-256 `AC3841688C9235404FCF3717630A69A44DAFCA362775F7A372EFB7E093CBFE59`.
- The updated history handoff's read-only appendix was freshly executed against the actual before and current after ASTs.
  All **22 cases pass**, with zero invalid after-array accesses and no partial writes in rejected cases.
  The fixture hash is `5244B4A022BF209590080817F8368E8B4DDA6A789D9273973A4D434B1CDD8719`, before runtime hash `10D679880DFD53DD826E7D90DE3F1708A27EA2924E6F2C784BE64D318A475FAB`, and after runtime hash `0A902614C03D060B159DADBA42C706D3C203CB0F448884E7AB10AC4BF2643214`.
  Shared sanitizer and view refresh are explicit recorded stubs, so their execution, runtime object scopes, persistence and native rendering remain outside this model.
- Bounded source searches and direct reads traced current capital selection, failure continuation, both fragment actor scopes, profile/helper lifetimes, duplicate building dispatch, dust contributors, report-array cleanup, mission completion sets, persistent achievement resets, and current WIP wrapper boundaries.
- A final exact consumer search confirmed F19: intended Event028 Details/history/evolution strings are unused in current shared runtime selectors, which fall through to generic Details text.

These checks do not execute the engine, supply an exact normalized probability, prove decoded asset creation lineage, observe a save, or validate native destruction/capital movement.
The initial availability command omitted its required fixture argument and returned usage error, then the correctly parameterized invocation above passed.
That command-line mistake is not reported as a gameplay failure.
The supplied QA `cycle1/error.log` has no explicit Event028 lines according to the parent's supplied evidence, but is not globally clean or gameplay acceptance.
No absence-of-errors inference closes these requirements.

### Part 10 scenario disposition, every required case

All native outcomes below are unrun/unproved in this audit, not asserted failures.
Source defects are identified separately by finding ID.

| Part 10 case | Source status and exact outstanding proof |
| --- | --- |
| 1. Low-Chaos baseline impact | Planner/receipt/dust source exists, F01/F05/F07/F12 block full proof. Need actual zero center, three ring losses, reports and dust receipts. |
| 2. Low-Chaos miss | Source body has no physical aftermath, 16 award tests include 799 and rejection cases. Need native no-impact/no-dust/no-evolution/major consumption. |
| 3. Fragmentation 600 to 699 | Three planned, minimum two applied source. F03/F04/F13 and native separated-pool/damage/log evidence remain. |
| 4. Fragmentation plus minerals 800 to 899 | Five planned and fixed +100/+20 source. Need current-toggle acceptance, source/native profile loss, controller armour and complete logs. |
| 5. Six-fragment plan/reduced pool at 900 to 999 | Goal six, bounded attempts and clean fewer-than-two rollback exist. Need actual count reduction, separation, honest region/count reports and native high-stack proof. |
| 6. Capital impact/backup | 23 parent source cases cover selector ranking/recipient identity. F02 late loss remains. Native actual-pointer relocation before destruction unproved. |
| 7. Three-country cross-border ring | Source shortest-ring planner/recipient dedupe exists. Need actual geography, stronger-overlap receipt and one popup per living recipient, with F07 count retained. |
| 8. Target annexed during lock | Fixed state pointer and original-annexed flag exist. Need native annexer capital continuity and historical name/flag display, F02/F06. |
| 9. Main/fragment outer overlap | Planner replaces by stronger numeric profile. Need actual one population/building receipt per state, including duplicate building family and >1000 boundary. |
| 10. Main crater wartime transfer | Native callback source checks old enemy with main material before refresh, resets holds and derives new benefit. Need executed war transfer, exact enemy modifier loss, conquered hold and no peaceful award. |
| 11. Fragment peace transfer | Current controller count/ideas derive from registered sites. Need native peace/ownership/annex callback coverage without stale copies or farmed action rewards. |
| 12. Reload during target lock | Persistent globals/targets are present. No save supplied or observed, no source claim establishes serialization or delayed delivery. |
| 13. Reload during severe dust | Persistent dust/pressure/protection records exist. Need stage/hold/injection/reservoir idempotence and retained program identity across reload. |
| 14. Invalid late-world N/A | 19 source cases freshly pass. Native country count, current event-view N/A and prefire refusal remain unproved. |
| 15. Nuclear isolation after every visual | F18 identifies documented detonation semantics, while `use_nuke = no` only disables stockpile deduction. Asteroid custom callback guards exist. Need a verified presentation-only route and native no-damage/no-nuclear-ledger/condemnation/retaliation/fallout/achievement proof for main and fragments. |
| 16. Achievement persistence/hold resets | Elapsed-day receipts, control-loss/annex reset and pre-cleanup reconnection award are present. Need every achievement reload/reset/direct-vs-subject/peace-vs-war case, correct national mission proof, and actual icon process evidence. |

### Tuning-matrix coverage

| Required tuning family | Audit outcome |
| --- | --- |
| Main 100/50/25/5 population, building bands and durations | Fixed constants/durations exist, actual transaction proof blocked by F01/F05 and native absence. No accepted percentages changed here. |
| Fragment 50/25/5, center buildings and recovery | Constants/separate profiles exist, classification/current-toggle/native profile evidence missing. |
| Rescue monthly fractions, caps, floors and duration | Per-state 6/4/6/3 month receipts, medical reduction, protected loss helper and rescue reason exist at runtime:1012 to :1138. Actual applied Deaths and expiry/action/failure behavior remain unrun. |
| Three/four/five/six fragments and >=two applied | Source tiers/count rollback/separation exist. Native distribution, actor exclusions and complete probability pass remain missing. |
| Dust contributors/caps | Existing bounded deaths/industry/logistics/footprint/fragment/secondary terms read. Strategic omission is F12. Actual receipts depend on physical transaction correctness. |
| Four stages, production/supply/weather, opening/monthly air | Repaired source values and positive bad-weather penalty exist. Current-stage protection and no historical-injection refund exist. Complete coexisting-source and settings/native scenarios unrun. |
| Thirty-day hold, stage decay, maximum extra three, expected 16 to 24 months | Current monthly source has hold/date guard and six/five/four/three decay plus capped mitigation. Full horizon/secondary-recovery scenarios unrun. |
| Basic/organized/hardened 15/30/45% | Stage-scaled compensation helper exists, attributed parent source verification, no independent current native proof. |
| Target score/diversity/isolation | Reach/population/industry/logistics/VP scorer and diversity preference exist. Required relative weighting, island penalty and diversity threshold evidence belongs to the specialist and remains unresolved. |
| Preparedness | Command duration and medical reductions exist. Transport accounting is the fixed grant at F08. Full stance benefit/cost comparison unrun. |
| Armour +20/+60/+100/+160/+200/+220 and uncapped generated-set stacking | Six fragment idea slots each +0.20 and main +1.00 exist. No arbitrary balance reduction authorized. Actual zero-base/positive-base/non-land/piercing/transfer and high-stack acceptance unrun. |
| Capacity/incident-scaled decision bands, supplied guards and reserve floors | Fixed floors exist, scaled amounts missing at F08 and supplied-garrison support blocked at F11. |

### AI-prompt case coverage and ownership

All weighted analysis is routed to `chaosx_ai_probability_auditor` `01a100d6-07b6-7d42-b3a0-fa58cf98f322`.
The auditor requested its current complete status, sent F03's fragment owner/controller gap to it, and received its completed read-only surface ledger before closing this report.
No new child was spawned to duplicate that specialist, and no independent balancing or probability calculation is substituted here.
The existing `availability_probability_20261003.md` records exposed routes returning 600-second timeouts and a rejected local fixture schema, with no current artifact/revision/numeric result.
Historical partial 20260905 results in `final_audit.md:75` to :83 had incomplete pools and unresolved contexts, so they do not validate the current source.

| Required scenario | Accepted expectation | Current evidence status |
| --- | --- | --- |
| AST_AI_01 | Stable democratic peace, miss dominates three friendly/neutral targets | Native specialist evaluation unresolved. |
| AST_AI_02 | Losing democratic existential war, only hostile major plausibly competes | Native specialist evaluation unresolved. |
| AST_AI_03 | Fascist total war, enemy leader high, neutral near zero | Native specialist evaluation unresolved. |
| AST_AI_04 | Peaceful nonaligned minor, miss strongly dominates | Native specialist evaluation unresolved. |
| AST_AI_05 | Existing destructive identity, best enemy can dominate under its actual route | Route/strategy completeness and specialist evaluation unresolved, not inferred from ideology alone. |
| AST_AI_06 | Subject/faction ally protected, enemy competes | Protected factor appears before adds. No normalized native pool/result claimed. |
| AST_AI_07 | Fragment risk at 700 raises miss versus identical 500 | Snapshot/current-toggle and candidate-pool inputs incomplete, specialist compare unresolved. |
| AST_AI_08 | Near-capitulation raises existential enemy use versus stable case | Specialist evaluate/sweep unresolved. |
| AST_AI_09 | Existing mineral advantage raises miss against distant enemy | Score helper exists, current eligibility/native scenario unresolved. |
| AST_AI_10 | All three protected, miss effectively certain | Protected relation helper exists, full native pool and ranking unresolved. |
| Recovery 1 | High preventable deaths, adequate supplies, hospitals first | Source weights present, exact eligibility/cost/candidate evidence unresolved. |
| Recovery 2 | Disconnected capital, rail first | Route source present, actual supply and ordering unresolved. |
| Recovery 3 | Collapsing front/low trains suppress reconstruction | Fixed reserve floors exist, scaled quote/strategy evidence unresolved. |
| Recovery 4 | Severe dust/strong industry prioritizes hardening | Stage weighting present, capacity scaling and specialist evaluation unresolved. |
| Recovery 5 | Threatened main crater prioritizes security | Crater action WIP and supplied requirement unresolved. |
| Recovery 6 | Distant enemy site does not outweigh homeland defense | Complete bounded site-value/defense strategy and specialist evidence unresolved. |
| Recovery 7 | Urgent local need delays global contribution until reserves | Floors/phase logic present, F08/F10 and specialist evaluate unresolved. |

Required sweeps are also unresolved individually: Chaos 0 to 999, capitulation progress, ally/neutral/enemy relationship, weak minor to faction-leader target value, fragmentation off/on, stability/war support, and exposed chooser route identity.
Preparedness options, target-state scoring, fragment selection, all recovery/crater decision and mission scores, and strategic site handling require the same specialist coverage.
Decision scores are willingness scores, not click probabilities.
Complete four-option pools, actual target bindings, uncertainty, and current baseline/after source identities must be retained before claiming normalized probabilities or deltas.
F03/F04/F14 eligibility repairs cannot bypass baseline-audit/owner-patch/compare.

## MCP evidence and exact blockers

The connected tool catalog exposes `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, reference context/search/read, older bounded `source_lookup`, map inspect, and probability routes.
It does not expose `hoi4.script_validate`.
Source lookup has no `view`/`keyPath` in this connected schema.
No connected server version/health or native task negotiation was established, so helper-expansion jobs/tasks were not asserted or used.

An initial request incorrectly used a filesystem path as `workspaceId` and omitted `selector.kind`.
The live validator rejected it, requiring a slug workspace ID and `selector: {kind: "event", eventId: ...}`.
The initial compare also incorrectly supplied a Git SHA as an analysis revision and an unsupported `after.current` key.
These are auditor request-validation errors, not engine evidence or service failures.
They were corrected by omitting the optional workspace selector, using the event discriminator, and using the recorded 64-character event-analysis revision for the comparison baseline.

Corrected minimal resolver requests used `.4`, depth one, one node, one edge/no helper expansion, and terminal render with no HTML.
Both returned `isError=true` and `timed out awaiting tools/call after 600s`.
The corrected reference-context request used surface `event`, limit two, and likewise timed out after 600 seconds.
No graph, render, current source revision, continuation URI, scenario hash, numeric acceptance, or comparison artifact was returned by these completed retries.
Corrected opening inspect, `.8` options render, cached-baseline compare, one-result wiki search, twenty-line source lookup, and state-64 lookup-only map retry were also submitted, with their terminal statuses recorded in the final addendum below.
`reference_read` cannot be claimed from a returned citation because no new citation/revision bundle was delivered.

Every in-scope branch remains covered by the source audit and affected by the missing current structural evidence: opening/confirmation/return/miss/unavailable, target preparedness, delayed main/fragment resolution, recipient reports/closeout, and dust milestones.
A focused trace/render cannot establish workspace helper/lifecycle coverage even if it returns successfully.
Historical artifacts in `final_audit.md` preserve earlier partial evidence, including event revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, deferred helper/lifecycle analysis, unresolved helper catalog entries, incomplete probability pools, and partial map diagnostics.
They are not current validation of the new source tranches.

### Local reference fallback read for the findings

Installed game root is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Offline wiki root is the workspace `paradox_wiki\`.
These were direct local reads, not successful MCP reference retrieval.

| Local source | Relevant lines read | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 433 to 442 temporary lifetime/scoping, 1216 to 1220 array/scope iterators and loop ceiling | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 257 annex scope, 450 to 462 control-change scopes | `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A` |
| Installed `documentation\effects_documentation.md` | 8573 to 8586 while-loop schema | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation\triggers_documentation.md` | 4603 to 4626 railway path, 6626 to 6639 division-in-state count without supplied filter | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `documentation\modifiers_documentation.md` | 1752 to 1755 armour modifier categories | `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E` |
| Installed `documentation\dynamic_variables_documentation.md` | 180 to 181 actual capital pointer | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| Installed `common\defines\00_defines.lua` | 25 actual loop ceiling | `405A24CE579815443CAFE052CFF1361E20C712CA8182E3F10CCBF45330DD4BE4` |

Additional exact wiki/installed/vanilla citations and source hashes remain in the capital, dust, placement, and history handoffs.
Their source citations support syntax/precedent claims, not native execution or design approval.
F18 additionally reads installed `effects_documentation.md:4745` to :4760 and offline `Effects - Hearts of Iron 4 Wiki.md:1517`.
The latter file's exact SHA-256 is `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.

## Remaining blockers and narrow next actions

1. Parent fix the physical/helper/late-capital/duplicate-building/report-lifetime gaps first, with the current source and exact receipts under review.
2. Route fragment owner/controller and evolution eligibility changes through the existing probability specialist's baseline/owner-patch/compare cycle.
3. Complete accepted scaled logistics, bounded national/regional objectives, emergency/failure lifecycle, and crater wrappers rather than closing them as minor polish.
4. Resolve the supplied-unit dependency explicitly and retain the exact unsupported-query evidence until an accepted solution exists.
5. Review the updated history-helper handoff and freshly rerun 22-case actual-source proof, then commit the finished bounded tranche through the parent.
6. Review/commit curator records, recover missing asset/text provenance, and keep irreversible evidence loss and inherited-news limits disclosed.
7. Integrate the missing current Event028 shared Details/history/evolution consumers, then align final visible wording, workbook and exports after implementation facts are stable.
8. Obtain current event inspect/render/compare, map, and every probability scenario/sweep/compare artifact when the service is healthy, retaining unresolved helper/lifecycle limits.
9. Keep Event028 disabled by default while these gates remain open.

There are known simplifications and omissions, principally flat cost/reserve grants, reduced mission proof, flag-only crater outcomes awaiting integration, missing supplied-garrison proof, and incomplete asset/text provenance.
The audit grants no exception to the user's no-simplification requirement.
The parent goal remains incomplete.

## Closing evidence addendum

The final corrected retries returned the following terminal evidence.
All completed failed calls below returned `isError = true` with `timed out awaiting tools/call after 600s` and no revision/artifact.

| Route and exact bounded request | Result |
| --- | --- |
| `event_inspect`, `mode=trace`, selector `{kind:event,eventId:chaosx.nr28.1}`, depth 1, nodes 1, edges 1, helpers false | 600.385 seconds, timeout |
| `event_render`, `view=options`, selector `.8`, depth 1, nodes 1, helpers false, HTML false | 600.455 seconds, timeout |
| `event_compare`, before analysis revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, `.1` event selector, chain/render nodes 1, render false | 600.455 seconds, timeout, no structural delta |
| `reference_search`, query `fire_only_once`, wiki-only, limit 1 | 600.455 seconds, timeout, no citation for a subsequent revision-bound read |
| `source_lookup`, exact `asteroid_incoming_relocate_current_capital`, references false, one definition, twenty lines | 600.455 seconds, timeout |
| `map_inspect`, lookupOnly true, stateIds `[64]`, queryLimit 1, overview false | Submitted, still awaiting a terminal tool result at cutoff. The generic orchestration was terminated without a map artifact. No server-side job cancellation or map validation result is claimed. |

The earlier corrected `.4` one-node trace, terminal render, and limit-two reference context also timed out after approximately 600.05 seconds each.
One earlier follow-up orchestration delivered no retained terminal payloads, so it is not counted as successful or timed-out native evidence.
The final retries above retain the actual returned errors and distinguish the still-unreturned map request.
The parent's separately supplied minimal map/render timeouts remain attributed evidence, not substituted for this map request's missing terminal result.

The probability specialist's completed ledger confirms no complete 2026-10-03 result, no analysis revision, scenario hash, comparison ID, score trace or render artifact.
Opening `.1` baseline/current compare and `.8` inspect, direct target-country inspect/compare, preparedness `.3` inspect, decision baseline/current inspect, and same-scenario decision compare timed out after 600 seconds.
The fragment-specific inspect lost its result handle, so it supplies no retained evidence.
Confirmation `.2` and one-option report acknowledgements have no separate current MCP result.
Historical five-mission evidence is score-only and remains bound to the older source.
The submitted recovery compare used empty scenario states, so even a returned result would not have proved state-target eligibility.
AST_AI_01 through 10, the complete seven recovery cases, every required sweep, and full current eligibility bindings therefore remain unresolved.

The specialist verified current decision WIP SHA-256 `E954ED3B45307AD519E773D4F7F0B7FB5898D386B4CB95BACE173248A929C6FD` and immutable before decision SHA-256 `E28A8C05814E1A3AB646972138C4349A3B55991588D5D2498BDF42ED3271F164`.
All 21 extracted `ai_will_do` ASTs are identical between those files, with extracted AST hash `666AFB9C58DD027E9A6F278087E025576DAC7D80E8CF21A9E93810CD94DBBE16`.
This proves unchanged authored score formulas, not unchanged eligibility, executed willingness scores or click probabilities.
The timed-out compare was submitted against earlier WIP hash `E071B75EE5AB95B1DA13149FE4F46D56C2568409B3745E7A408A14E0A6BC3F76`, so no comparison artifact is bound to the current WIP.
The specialist independently confirmed F03 from the same current trigger/runtime hashes and made no patch or balance choice.

The updated history handoff was read completely and its actual-source appendix freshly passed all 22 unchanged cases.
Its status is implemented source with native acceptance unresolved, not an unresolved implementation proposal.
The parent still owns its commit.
The runtime physical hash remained `0A902614C03D060B159DADBA42C706D3C203CB0F448884E7AB10AC4BF2643214` at closing verification.
The report exists as a new untracked file at the explicitly owned path.
No gameplay, assets, workbook, parent docs or Git index were changed by this auditor.
