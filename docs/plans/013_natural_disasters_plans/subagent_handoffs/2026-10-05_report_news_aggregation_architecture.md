# Event 013 report and news aggregation architecture

## Status and boundary

Disposition: `superseded` by [the Event 013 report/news implementation handoff](../2026-10-05_report_news_implementation_handoff.md).

The parent accepted the G2/G4 report and news aggregation design on 2026-10-05, and source implementation now owns the current behavior. This earlier architecture document remains as a historical record of the pre-implementation proposal and its rejected/unresolved alternatives; it is not the current implementation contract. Its historical report-request inventory and proposed helper layout must not be read as current source evidence.

The replacement handoff records current source evidence, scope and spam limits, G1/G5/G6 work, cost changes, assets, documentation dispositions, required fixture scenarios, and exact MCP blockers. Engine render/compare and province-building getter semantics remain unresolved and are not represented as verified.

## Exact report-request inventory

Line references are to the source revision recorded below and can move during concurrent parent edits.
All seven direct calls to `natural_disaster_schedule_family_report` in `common/scripted_effects/013_natural_disasters_effects.txt` were inspected.

| Line | Caller | What happened before the request | Accounting rule |
| --- | --- | --- | --- |
| 1136 | `natural_disaster_sync_open_card_to_evolution_ii` | An existing unresolved card acquires a causal route and a follow-up job. | Presentation update only, with zero new deaths and zero new building damage at this point. |
| 8980 | `natural_disaster_execute_chain_followup` | Conditional population loss, conditional building damage, and state disruption have run. | Commit this follow-up's freshly initialized outcome deltas, including explicit zeros for branches that skipped damage or deaths. |
| 9107 | `natural_disaster_apply_terminal_failure_consequence` | Recovery scores and disruption worsen, and a future chain can be queued. | Zero new deaths/building loss here, while preserving the terminal outcome and new producer job. |
| 9392 | `natural_disaster_apply_neighbor_impact` | A neighbor receives actual population loss, building damage, and its own aftermath card. | A distinct consequence receipt for this exact neighbor and source impact, under the inherited parent sequence. |
| 9535 | `natural_disaster_execute_repeated_impact` | A repeat hit applies population loss and building damage, then schedules a chain. | A distinct repeat-hit receipt even when state, family, or segment equals an earlier hit. |
| 9610 | `natural_disaster_execute_ocean_impact_proxy` | The coastal observation card records an offshore origin and schedules a tsunami, explicitly zeroing deaths and damage. | Record the origin and observer state with zero physical loss, and count later tsunami consequences separately. |
| 9741 | `natural_disaster_execute_impact` | Primary population loss, building damage, card activation, and chain scheduling run. | Commit the primary hit before the following regional-spread helper enters neighbor states. |

The ordinary-impact report request precedes `natural_disaster_apply_regional_spread` at approximately 9755, so a report request cannot mean the producer transaction is finished.
Follow-up processing can queue further disease work after its report request at 8980.
The scheduler at 8118-8133 currently randomizes a delay, enqueues a new state job, sets the state report date, and updates abnormal history for every request.
It should become a request/update hook rather than an additive accounting hook.

## Outcome provenance

`chaos_deaths_change`, immediately after `chaos_meter_register_state_civilian_deaths_percent` at 5436, is the actual returned loss for that application.
The source seeds this output to zero before the call, copies it into `natural_disaster_last_deaths` at 5437, and adds it to `natural_disaster_total_deaths` at 5438.
Freeze that returned output before the famine adapter or any nested transaction can overwrite it.
`natural_disaster_last_deaths` means the last loss application, and it becomes stale whenever a later branch does not apply population loss.
`natural_disaster_total_deaths` is a cumulative state/card ledger, and its history snapshot at 11105 cannot be added once per report request.
Summing report snapshots counts Evolution II updates and terminal recovery failures as repeat deaths.

`natural_disaster_damage_transport`, `industry`, `ports`, `air`, `resources`, and `shelter` are profile/category indicators initialized by `natural_disaster_prepare_family_profile`, beginning at 4663.
The building helper at 5061-5074 copies those profile indicators back into persistent card fields regardless of whether an eligible building existed.
They are not measured building-level deltas or proof that a building was damaged.
`natural_disaster_damage_points` and `natural_disaster_building_damage` are requested/scaled damage inputs, with secondary and tertiary scaling, rather than verified engine loss.
Preserve these fields for existing recovery/achievement mechanics while creating separate factual report fields.

The safe factual hook is inside `natural_disaster_damage_selected_building` at 4964, immediately around each existing `damage_building` invocation.
Initialize caller-owned pre/post getter outputs and a zero delta for every invocation.
Read `damaged_building_level@<exact building token>` before and after, then add only the measured positive difference to the consequence receipt.
Use a verified meta substitution for the static building token and preserve the existing command, guards, target selection, and ordering.
The installed dynamic-variable reference documents this getter, but does not settle aggregation semantics for province buildings.
Validate naval-base and supply-node getters separately, including multiple provinces, absent buildings, fully damaged buildings, and partial saturation.
If a province getter cannot measure the command's actual target, numeric province damage remains unresolved rather than being replaced with requested damage.

Map each measured building token to its actual physical category, such as infrastructure/supply nodes to transport, factories/dockyards to industry, naval bases to ports, and air bases to air.
Store per-token deltas as well as category totals so a repeated building token is counted only through its observed incremental loss.
Resource and shelter consequences require their own applied-effect evidence and terminology because the profile flags do not prove a resource or shelter building was damaged.
Keep measured building damage, affected-state counts, and applied resource/shelter disruption as separate units.
Never label a sum of category flags as destroyed buildings.

## Receipt and registry design

Use an Event 013 global sequence registry with stable sequence identity and sparse aligned rows, independent of controller-owned transport queues.
Each sequence row owns planning depth, pending producer-job count, in-flight producer depth, consequence-capable open-card references when complete final totals are required, participant references, finalized state, and global news status.
Represent booleans with flags or receipt states, not numeric 0/1 gameplay variables.
Maintain a country/sequence delivery receipt separately from the physical consequence ledger.
A country-wide `last_reported_sequence_id` is insufficient because interleaved sequences can finish out of order.

Allocate one durable consequence ID for each scheduled damaging job before enqueue, and carry it in a new aligned queue field through enqueue, dequeue, and transfer.
Do not allocate a new ID when transferring or retrying the same job.
A synchronous neighbor gets a unique child consequence ID registered while its parent producer remains in flight.
One consequence can contain death and several building deltas, so those subcalls share the same ID and commit together at the enclosing consequence boundary.
Use separate component receipts if a consequence can legitimately resume partial execution.
Before application, reserve the consequence receipt with its sequence, exact state, frozen owner/controller, family, segment, and provenance.
Before commit, match those fields again and reject an already committed receipt.
Private frames must be keyed by the stable consequence ID or use a real persistent parent-linked stack.
A single set of private fields on the state or worker is still unsafe when nested work revisits the same state or country.
Do not use shifting array positions as durable receipt identity, and defer compaction until no active frame references those positions.
Restore an outer frame only through its stored parent receipt, never through a temporary loop index surviving a nested helper.
The ID protects accounting only and must not introduce a substitute physical-effect execution path.
The existing physical idempotence guards remain responsible for damage execution.

Commit immutable rows containing sequence ID, consequence ID, exact state pointer, state identity, impact date, family, segment, original owner/controller, deaths delta, measured building-token deltas, factual category presence, warning outcome, and applied disruption.
State pointers alone cannot identify a consequence because a state may be hit repeatedly.
A `(sequence, state, family)` key would wrongly collapse repeat hits and aftershocks.
Keep state lists and family lists deduplicated for presentation, while summing every distinct committed consequence once.
Global totals sum physical receipts once even if caller/global policies cause multiple country recipients to see them.

## Proposed helper map

| Helper | Required scope and inputs | Outputs, side effects, and call sites |
| --- | --- | --- |
| `natural_disaster_report_begin_sequence` | Calling COUNTRY, frozen accepted sequence ID and policies. | Register/open planning producer before `natural_disaster_plan_sequence`, then close planning after the planner returns, including rejection cleanup. |
| `natural_disaster_report_begin_consequence` | Exact STATE with durable consequence ID, sequence ID, and frozen owner/controller. | Zero component outputs, establish private frame, and reject committed duplicates before ordinary/repeat/neighbor/follow-up consequence work. |
| `natural_disaster_report_commit_consequence` | Exact STATE and matching private frame. | Commit immutable fresh outputs once, register factual families/states, update aggregate projections, and clear the private frame on every return. |
| `natural_disaster_report_measure_building_delta` | Exact STATE, building token, and existing command context. | Caller-seeded measured delta and factual category output around the existing selected-building command. |
| `natural_disaster_request_sequence_report` | STATE, exact sequence ID, and update context. | Replace scheduler behavior at all seven report-request sites without adding physical totals. |
| `natural_disaster_register_sequence_news_candidate` | STATE with exact sequence/consequence and current policy. | Evaluate existing non-random eligibility, remember qualifying families and severity, and reserve one sequence candidate instead of a news row per state. |
| `natural_disaster_try_finalize_sequence_reports` | COUNTRY worker or callback with frozen sequence ID. | Check global closure, project deduplicated recipients, set delivery receipts before firing, and dispatch at most one major news item. |
| `natural_disaster_cleanup_sequence_report_runtime` | Explicit sequence identity and terminal ledger state. | Remove transient aligned rows and private frames only after producer, delivery, and snapshot references finish. |

These are event-local helpers, not a new central router or generic cross-event system.
They take documented variable/token inputs and `= yes` calls rather than named scripted-effect argument blocks.
Every caller must initialize helper outputs before invoking them.
Temporary variables are unscoped and not durable transaction storage.

## Exact scope transitions

In `chaosx.nr13.2`, COUNTRY W is the worker recipient and ROOT remains W throughout its immediate effect.
`natural_disaster_process_due_job` selects W's queue row, copies all values into a W-owned private persistent frame, and records STATE S explicitly before row removal.
Entering S from W makes THIS=S, PREV=W, and ROOT=W.
Entering S's controller C then makes THIS=C, PREV=S, and ROOT still W.
Entering S's owner O has the same nesting, with THIS=O and PREV=S.
Freeze O and C into normal fields on S's consequence frame before nested adapters, spread helpers, or country iterators execute.
Read those fields explicitly when committing rather than trusting ROOT, a deeper PREV chain, a shared temporary, or a mutable regular target alias.

In a participant loop country P, store P explicitly before entering any state.
For delivery to D, enter the validated D country and call the report event there.
The receiving event's ROOT becomes D, and its FROM follows the originating effect-chain ROOT contract rather than automatically meaning the impacted controller.
Descriptions must therefore use their explicit aggregate context, not FROM or the current state's live owner/controller.
Normal state pointers identify persistent map objects and should be checked against exact expected identity and ledger markers.
`exists = yes` is COUNTRY-only and belongs in actual owner/controller/recipient scopes.
`scope_exists` on a variable scope cannot prove pointer validity.

Regular event targets can carry the selected scope through a fired event, but point to mutable objects and do not freeze variable values.
A named global event target for the latest report/news would be shared across concurrent sequences and must not be used as snapshot storage.

## Ordered execution and closure

```text
begin accepted sequence planning under stable sequence ID
register every successfully scheduled producer job once
close planning frame after all primary scheduling succeeds or rejects

worker selects one due row and freezes its full private job frame
if producer job: add in-flight guard before removing queue row
remove all aligned queue fields and release only that transport reservation
decrement pending producer count exactly once for a claimed producer receipt
validate exact state, current job receipt, and actual responsible country
dispatch physical helper with fresh zero outcome components
register any new child producer before releasing parent's in-flight guard
commit each actually applied consequence once
record presentation updates without adding old consequence values
release in-flight guard and private frame on all success/stale/cancel paths
try global sequence closure using frozen sequence ID

when closure is eligible:
  freeze final physical ledger and project recipient buckets
  validate recipient existence and deduplicate (sequence, recipient)
  reserve report delivery receipt before country_event
  reserve sequence news receipt before one news_event with major=yes
  preserve immutable snapshots until no display/option reference remains
  remove transient registry rows through idempotent cleanup
```

Warnings are not additive consequences.
Keep delivery-reserved and delivery-acknowledged states distinct if a new receiver event or validation trigger can reject the call.
The receiving event must acknowledge the exact sequence/country receipt, and a rejected reservation may be repaired only after proving no popup was dispatched.
An observation failure alone does not authorize a second firing.
Report/news transport and cosmetic reassessments are not physical producers.
Impacts and all follow-up jobs capable of adding consequences or children are producers.
The parent must classify actual reassessment/recovery callbacks that can invoke terminal failure as future producers, rather than treating every reassessment as cosmetic.
Cancellation, prevented chains, and invalidated targets release the exact producer receipt once.
Queue transfer changes neither pending count nor consequence identity.

`natural_disaster_achievement_mark_sequence_ended` at 10838 is called after dispatch in `natural_disaster_process_due_job`.
Its country-local queue scan can see new child rows scheduled synchronously onto the same country after dispatch, so that narrow ordering is useful.
It cannot see child work assigned to another controller, future late-recovery producers, or synchronous work that left no local row.
It also scans all local job types, including report/reassessment rows, so it is not a physical-report closure predicate.
Leave existing achievement semantics intact unless separately reviewed, and add the global reporting registry rather than reusing this helper as proof of global completion.

## Controller changes and annexation

The queue-transfer helper at 7674 migrates aligned rows for one exact state and preserves reserved due dates.
Carry any new consequence-ID field through its copy, remove, and append operations.
Use a persistent frozen source/destination frame because nested scopes can replace regular aliases and temporary indexes.
If source equals destination, do not remove and reappend rows into the same array being traversed.
Old worker wakeups become harmless empty/stale deliveries.
Transfers never move or delete committed physical receipts and never decrement/reincrement producer counts.

Record original owner/controller in every consequence even if pending presentation is later reassigned to a current controller.
Resolve presentation recipients at flush under an explicit policy, merge receipts for all states routed to the same country, and honor that country's existing sent receipt before appending delivery work.
When the original impacted country still exists but has lost a state, preserve its historical bucket unless the parent explicitly selects responsibility-based recipient semantics.
When it is annexed, explicitly reroute undelivered presentation using the recorded exact state's living controller and preserve the original attribution in the text.
Never fire delayed work solely into a dead tag because its event timer can remain suspended until release.
If no living recipient exists, keep an unresolved undelivered bucket rather than clearing physical totals or claiming a sent report.
One global sequence registry avoids dependence on an annexed caller or anchor country remaining alive.
If a separate deferred flush event is added, its wakeup ownership must also be transferred or repaired by bounded existing callbacks.
The five named source files do not expose all on_action call sites, so native annex/control callback wiring remains parent validation work.

## Presentation, tuning, and migration

Existing family report events 101-125 and news events 201-225 may remain as single-family presentation variants, but no variant may fire once per state.
Mixed families require a mixed title/description selected from immutable aggregate family membership, with an identified state list and actual totals.
A dominant-family picture must not mislabel the mixed sequence's text, and image choice requires parent asset review.
Retain maximum severity, original causal origin, warning distinctions, and per-state recovery consequences instead of replacing them with one synthetic state card.
Report descriptions at localisation line 72 currently read the mutable `natural_disaster_report_state` snapshot, so aggregation needs an explicit presentation context.
Do not assume queued or open event descriptions cache values at dispatch.
Use sequence-specific immutable payload storage with a proven event-instance selector, or verify native caching behavior before using a mutable recipient snapshot slot.
Full state enumeration and concurrent event-instance selection are unresolved engine-facing presentation details, and a shortened list with silently dropped names is not an approved solution.

Keep existing policy values in the constants file and existing news qualification semantics unless the parent approves a policy change.
Move the maximum-one rule into sequence/country receipts rather than family cooldowns.
Preserve family cooldown and first-family history semantics, but freeze candidate qualification when observed and consume throttle receipts at the same defined transaction point.
Do not have the first mixed-family impact prevent the rest of its sequence from appearing in the single summary.
The parent should explicitly settle whether existing caller/global report policies can send aggregates to unaffected observers under G2.
All such destinations still obey one popup per country/sequence and must not multiply physical totals.

Use one `natural_disaster_report_aggregation` constant category with schema for shared deterministic delivery delay, job IDs if added, delivery states if needed, and presentation limits only where an actual engine limit is established.
Prefer a deterministic flush delay over introducing a new weighted/random helper.
Do not add a total-loss cap, a sequence-number precision limit, or a state-list truncation cap without evidence and design acceptance.
If timing still uses existing random report-delay logic, that touched weighted surface needs the parent probability auditor baseline/compare workflow, currently blocked by MCP availability.

Migration order: add receipt/frame fields and documentation, instrument factual losses, extend enqueue/dequeue/transfer alignment, implement global producer lifecycle, replace seven report requests and three news requests, implement immutable country/news snapshots and mixed localisation, then remove unused per-impact presentation queue creation.
Preserve the per-state impact/recovery queues, history rows, dates, missions, and physical effects.
Review abnormal history's report-date fields when changing scheduler meaning rather than leaving a report date that never delivers.
Do not commit this architecture as completed gameplay implementation.

## Required parent decisions and meaningful validation

Complete final totals and early delivery cannot both include consequences that have not happened yet.
Terminal recovery failure at 9057-9107 can schedule damaging same-sequence work after impact queues become empty.
For a complete final report, consequence-capable open cards must keep the sequence producer barrier open until they resolve, expire safely, or permanently lose that ability, potentially delaying delivery for months.
An earlier single summary can instead state confirmed totals to its report date, preserve later physical ledger updates, and emit no second popup, but that timing boundary needs explicit parent acceptance.
It is not silently selected here.

Validate two states in one country, two countries in one sequence, interleaved sequences completing in reverse order, mixed family repeat hits, a fully prevented chain, offshore proxy followed by tsunami, regional neighbor spread, skipped population/building branches, Evolution II updates, terminal recovery failure, identical source/destination transfer, split pending state ownership, annexed caller/controller, duplicate worker deliveries, stale state receipts, and reentrant nested adapters.
For totals, reconcile every unique committed death delta against the physical loss output, and every building delta against immediate pre/post getter differences.
Test already damaged or absent buildings and province-building getter semantics separately.
For display stability, hold one popup open while another sequence for the same country fires, and verify titles, totals, state names, and options remain bound to their own sequence.
Required MCP chain and post-change comparison evidence is blocked by the reported timeouts.
No runtime tests were performed by this worker.

## Local reference evidence

- Offline snapshot `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, captured 2026-09-19, lines 263-327 for event targets, 425-457 for variables and temporary outputs, 1069-1115 for arrays, and 1667-1679 for state building/owner/controller getters.
- Offline snapshot `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, captured 2026-09-19, lines 260-267 for ROOT/PREV/owner/controller.
- Offline snapshot `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, captured 2026-09-19, lines 27-35 for event scope inheritance and dormant-country timers, and 145-149 for triggered-only and major news behavior.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 2943-2968 for country events, 3374-3392 for building damage, 5053-5078 for news events, and 6496-6514 for event targets.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, lines 2708-2715 for COUNTRY-only existence, 3844-3852 for event-target presence, and 6554-6569 for undamaged building checks.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`, lines 1101-1144 for building and owner/controller getters, including `damaged_building_level@arms_factory`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, lines 216-245, and installed `common/script_constants/documentation.md`, lines 1-65 for cross-file constant access, supported fields, schema, and examples.
- Vanilla precedent `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/Generic.txt`, lines 1983-2009 and 2026-2037, for a country event consuming an explicit state target.

The initially searched installed `documentation/scripted_variables_documentation.md` does not exist.
The correct installed reference is `documentation/dynamic_variables_documentation.md`, read directly afterward.
Shared `chaosx_dynamic_effects.txt` and helper docs were deliberately not inspected because the parent restricted source reading to the five named Event 013 files.
Their reuse audit is still required before a parent adds a generic helper.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was changed.

## Source revisions

SHA-256 values recorded on 2026-10-05 after source reading, without MCP revision support.

- common/scripted_effects/013_natural_disasters_effects.txt: 8D3ADDAD3ECBD9B36685B01DC684088A8506C21A82C06CD82550283ACDE8AE82
- common/script_constants/013_natural_disasters_constants.txt: 20A9F9E6ED27C5573FF2445D25615880499D8FD14FCA9C8485F6E24A29F51231
- events/013_natural_disasters.txt: BE47AE6E83360FB341812B05B6002A00801B5B271C2F9B9272BFE53733D412EA
- common/scripted_localisation/013_natural_disasters_scripted_localisation.txt: 1A2C60A86BC38EA01CA8B5EFCCE0451529CAF2EFCD949A9BFA8BF427535951DE
- localisation/english/013_natural_disasters_l_english.yml: 4DB9C3AF0773583150D5E8D4364C682DB858EF6516CFB36C68ECCAA7F313A8E6
- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md: 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4
- paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md: 18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49
- paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md: 96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md: 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md: 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md: 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md: 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md: E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/Generic.txt: 96D510E119EC0548C3957689395674C7361C6689D2C7D0D65D1C0E024956EC26
