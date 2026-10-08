# Event 099 Sandstorm implementation contracts

## Authority and completion status

This supporting file translates the written Sandstorm design into ownership and validation contracts without replacing the idea-first Parts 01 through 07.
The final written choices supersede alternatives in the earlier architecture handoffs, including their possible later creation cutoffs, additional public values and withdrawable dust proposals.
All new `sandstorm_*` identifiers and new dust adapters below are proposed APIs requiring implementation and owner acceptance.
Existing source declarations and documented owner seams are labeled separately.
No HOI4 MCP, native parser, gameplay, map rendering, save or payment validation was performed in the original 2026-10-07 planning task.
Current source/MCP observations are retained separately in the [2026-10-08 import evidence](../../plans/099_sandstorm_plans/099_import_evidence_2026-10-08.json) and do not certify the proposed APIs or native effects.

The current public identities are **Intensity** and **Estimated exposed civilians**.
The latter estimates unique current residents within the union footprint, not cumulative daily exposures or an unsheltered population.
Shelter and mask issue change mortality risk separately, while actual evacuation and deaths change remaining residents.
Forecast dates, lifecycle status and completion dates remain contextual information under Part 01.

## Exact inspected evidence

All repository references use commit `a3ef485c5da7e2337122eca04ac65c175050f251`.
Ranges are original one-based inclusive lines.
The original planning workspace stored architect copies under `sandstorm_work/repo_evidence/architect/` and curator ranges in `repo_evidence/curator/reading_manifest.json`.
Those historical workspace paths are provenance labels rather than installed repository paths, and source snapshot archives are deliberately not imported.
The table below and [embedded source ledger](099_sandstorm_source_reading_ledger.json) retain the durable source identities, pin and relevant ranges.
Future implementation must reopen the pertinent current files and installed references.
The table identifies source evidence rather than native execution proof.

| ID | Repository artifact | Blob SHA | Relevant ranges |
| --- | --- | --- | --- |
| E1 | `events/099_desert_storm.txt` | `398bf85501b5b04f60453fb82e5ec58cd866987f` | 1 to 50 |
| E2 | `common/scripted_triggers/chaosx_dynamic_triggers.txt` | `965f7f83d133ab1e616299adf422c16325db9ffb` | 78 to 154 |
| E3 | `common/scripted_effects/chaosx_dynamic_effects.txt` | `06e1b00524b565f1a6421bc6c9db720193ab69db` | 46 to 60, 64 to 287, 291 to 397, 530 to 716 |
| E4 | `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt` | `cef6676950b7c1cd70dc9ca6108af4176d0f578a` | 88 to 98 |
| E5 | `common/dynamic_modifiers/chemical_state_modifiers.txt` | `64606458c22bc049c9956f4ee5b02c8284391920` | 1 to 14 |
| E6 | `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` | `909724da89e70cbaa8dbe87e62b43585769fcb49` | 100 to 175, 1170 to 1230, 1270 to 1284 |
| E7 | `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | `afc9255950157681d0202484f20d06cea9bd747c` | 3358 to 3373, 4225 to 4235 |
| E8 | `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | `3388a4f0e618a2061c03efe2e50e7e1796e8cef7` | 523 to 555 |
| E9 | `docs/systems/air_cleanliness/contamination_source_ledger.md` | `40fe577375f977aef64fdfe06f71eb297afab187` | 12 to 53 |
| E10 | `docs/systems/air_cleanliness/natural_sources.md` | `a76da9390fcd79061e9665f2365cd2d1f9a5884a` | 7 to 58 |
| E11 | `common/scripted_effects/cbrn_protection_effects.txt` | `3554fb47e8699a8246b8c47b534510458dea3ca9` | 769 to 901, 1122 to 1456, 1834 to 1940 |
| E12 | `common/scripted_effects/cbrn_scripted_effects.md` | `58fbc89406f05ff4cfea2b019b9c991fc6e0a29e` | 243 to 303, 631 to 779, 848 to 877, 1141 to 1151 |
| E13 | `docs/systems/universal_cost_modifier.md` | `f053e8d76ef5d7232fd622a18b7ae7d9faa77e83` | 7 to 24, 66 to 82, 135 to 147 |
| E14 | `docs/systems/migration_system.md` | `0d2bfdb3994cab5f446495727a02e3fc38cfeec3` | 7 to 23, 49 to 53, 69 to 77 |

E6 through E8 are inspected offline documentation snapshots and require current installed-reference confirmation.
The 73-state desert classifier in E2 supplies no desert-family geometry or ocean adjacency.
The pinned map tree contains only `buildings.txt`, and installed province geometry and current Windows game documentation were unavailable here.
E1 implements a selected-country Event 013 dust gateway, with no moving-front runtime.

## Pinned and proposed API boundaries

| Surface | Status | Contract boundary |
| --- | --- | --- |
| `call_natural_disaster` | Current shared declaration, E3 | Event 013 owns resolved local jobs and aftermath |
| `apply_exact_state_civilian_population_loss` | Current declaration requiring correction, E3 | Name alone does not establish measured-loss conformance |
| `damage_state_building_dynamic` | Current shared declaration, E3 | STATE scope with explicit building token and positive damage |
| `cbrn_refresh_state_civilian_mask_snapshot` | Current inspected owner helper, E11 | Refreshes real effective coverage without issuing equipment |
| `cbrn_distribute_requested_masks_to_state` | Current inspected owner helper, E11 | Shared owner debits stock and preserves issued ledgers |
| Dust respiratory snapshot adapter | Proposed neutral protection-owner seam | Returns verified coverage, respiratory quality, units, controller and freshness |
| `cbrn_complete_civilian_shelter_movement` | Current chemical-response completion seam, E12 | Not a Sandstorm household-policy helper |
| Dust aerosol admission adapter | Proposed narrow Air-owner extension | Adds accepted pressure once through existing aerosols ownership |
| `universal_cost_*` quote and transaction family | Documented current owner seam, E13 | Exact component parameters and native payment need validation |
| `sandstorm_*` lifecycle and response helpers | Proposed Event 099 declarations | Own orchestration and receipts without copying shared ledgers |

In this table, current means present at the recorded original pin, not independently verified in the import checkout.
A source-only precedent does not certify scope, persistence, atomicity or symmetry.
Missing adapters remain release dependencies and do not authorize deleted mechanics or parallel owner systems.

## Sparse season and front identity

The proposed season ledger stores schema version, monotonic season ID, global fire-once receipt, original start, stop at start plus 360 days, stage, admission counters, material receipts, source balances and scheduler lease.
Front rows store stable ID, lineage, revision, status, source family, geometry, heading, speed, material, intensity profile, due interval and inherited stop.
Numeric sparse aligned arrays and explicit identity lookups replace invented token-keyed maps.
Compaction preserves alignment, and row offsets never serve as durable front identities.
Consumed front IDs remain tombstoned through receipt retention.

| Form | Active cap | Cumulative admitted births |
| --- | --- | --- |
| Baseline | 1 | 1 |
| The Great Dust Wall | 1 | 1 |
| Splinter Storms | 4 | 8 |
| The Returning Storm | 6 | 16 |
| The World of Dust | 8 | 24 |

Initial source starts, every split child and every reseed spend births.
Merge replacement identity does not spend a birth.
Stage advancement unlocks only unused capacity and never resets spent births, reservoirs, receipts or clocks.
Initial and active evolution entry both require the viable manifestations described in Part 06.
Splits reserve all child geometry, material allocations and capacity before atomically retiring the parent.
Merges consume parents once, conserve remaining material and inherit source-use and consequence history.

Creation requests retain identity, viability and a bounded pending deadline.
The creation window requires elapsed season time strictly below 300 days.
At elapsed time of 300 days or more, reject every new material draw, reseed and split birth, including an old queued request.
All fronts enter compulsory taper by day 330 and retire by day 360.
Earlier material exhaustion is normal, and typical duration bands are attenuation targets rather than independent expiry clocks.
Returns and conservative mergers cannot renew lifetime.

Per-desert season balances deduplicate actual swept emitting-land contact across simultaneous fronts and inherited lineages.
The two-reseed family allowance and finite material allocation survive return, split, merge and host transfer.
Waiting does not replenish them.
No evolution flag, stage record or unlock grants Chaos.

## Geographic and forecast contract

The proposed generated catalog records installed game version, map hashes, valid desert families, emitting cells, physical neighbors, distances, state projection and strategic-region projection.
It must cover the mandatory Sahara, Arabian, Australian, Gobi and Central Asian audit and every additional admitted family.
Origin selection first uses eligible families, then viable connected openings, avoiding political subdivision bias.

The opening must satisfy Part 02's physical area, connectedness and minimum state-intersection requirements together.
Depth, minimum speed and finite stall allowance must yield the intended residence profile.
The 450 to 900 km depth and 120 to 240 km/day central ranges cannot be independently sampled because some combinations violate the three to seven-day normal passage target.
Evolved geometry and turns must similarly preserve the stated fourteen-day passage bound or identify a genuinely separate return or additional front.

Land and sea share one physical movement model.
Diplomatic access and military strait links neither block atmospheric coast crossings nor create distant teleports.
Every update records swept cells, including intermediate crossings and rotation.
Sea cells project to visual and air consumers without resident population or building damage.

Current footprint, committed approach, likely corridor and watch area derive from the same persisted front state.
Reloading or opening a panel cannot redraw steering.
Map projection cannot use generic native route arrows without inspected support.
A static icon, random destination after a sea delay or country-wide substitute does not fulfill moving geometry.

Recurring work visits sparse active fronts, dirty cells, touched states, affected regions and bounded response queues.
No recurring whole-world state or country scan is authorized.
Global presentation denominators require a verified native aggregate or valid owner-maintained cache, with freshness proof, rather than a hidden recurring census.
Missing denominator proof prevents falsely awarding the global milestone.

## Interval authority and late work

The proposed dispatcher uses delayed events as wake requests rather than stored impact authority.
It validates the current season, lease, due time, front revision and interval receipt before advancing work.
Temporary variables remain synchronous inputs.
A saved event target does not freeze mutable variables on its country or state.

Each committed simulation interval has one authoritative swept footprint and one aggregate state dose.
The local density rule is the strongest contribution plus one quarter of the others, capped at extreme, as specified in Part 02.
Transitions cannot charge the same interval twice.
One front leaving cannot clear a state still covered by another.

Bounded catch-up may consume only preexisting authoritative interval data whose geometry, times, exposure, protection and consequence receipts remain valid.
Missing history must not be reconstructed by inventing old random paths or applying current severity retrospectively.
An unprovable gap becomes a recorded validation failure.
Catch-up remains bounded and must finish any physical mutation before the absolute horizon.

At or after the horizon, perform no new population loss, organization drain or building or railway damage, even for an uncommitted packet nominally dated earlier.
Retire acute coverage, stop future emissions, close scheduling and retain a diagnostic for missed work.
Already committed historical receipts may be finalized without replaying their mutations.
No backdated deaths compensate for an invalid queue.
This policy makes the horizon a real end to damage rather than only a displayed date.

Host takeover changes the scheduler lease and host identity without recreating the season.
The new host processes only still-valid due work.
Old-host wakes, repeated wakes and completion callbacks have no independent authority to advance a paid response or damage interval.

## Population correction and direct exposure

Correct or replace E3's population implementation before enabling 099 casualty commits.
Lines 656 and 668 to 674 round the protected floor and selected request without the required upward floor rounding and downward available-person flooring.
Lines 692 to 698 log the selected amount without measuring post-mutation population.
The existing owner/controller recruitable-credit reconciliation at lines 556 to 623 must be preserved and verified.

The corrected STATE primitive accepts explicit requested people, minimum remaining people, reason, Deaths logging policy, target country, target-presence flag and one-shot supplied proof.
Its existing input names are `state_civilian_population_loss_requested`, `state_civilian_population_loss_minimum_remaining`, `state_civilian_population_loss_reason`, `state_civilian_population_loss_log_deaths`, `state_civilian_population_loss_target_country`, `state_civilian_population_loss_has_target_country` and `state_civilian_population_loss_contract_supplied`.
Caller initializes `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`.
The completed contract performs one physical debit, returns measured actual loss and records only that measured result through the shared Deaths path.
A wrapper must not log through a mutating Deaths call and then debit population again.

Read current `state_population_k` at each valid commit and convert thousands to people.
Use the smaller of 1,000 residents and current population as the protected minimum without creating residents.
Current geographic coverage, interval duration, intensity and the three Part 04 risk channels produce one expected direct loss.
Fractional people carry in the state receipt until a whole-person request is available.
Do not round every small update upward or turn a discarded fractional remainder into a final death.
Unavailable whole-person requests do not become future death debt.

Shelter, masks and actual overlap facts modify the channels once before the aggregate transaction.
Migration cohorts already debited from the resident state are excluded.
Route deaths remain the migration owner's slice of its transfer, and later famine deaths remain separately attributed.
Direct accidents, suffocation and structural harm do not each roll an additional mortality pool.

## Household policy and masks

D1 is a modeled Event 099 household retreat policy with its own preparation, effective time, minimum commitment and six-hour control handover.
It has no stockpile fee and supplies the economic sacrifice in Part 05 only while actual exposure is present.
It does not claim counted shelter beds or exact sheltered headcount.
Do not call the paid CBRN shelter helper, chemical shelter completion helper or chemical response flags.

The proposed dust adapter reads neutral real mask coverage and weighted respiratory quality from the protection owner.
Both are percentages from zero through one hundred, with explicit freshness and current-controller proof.
The Part 04 respiratory fraction is their lesser value divided by one hundred.
The dust interpretation changes only the specified breathing and outdoor component and preserves its combined residual-risk floor.
It must never fabricate a chemical agent class to obtain proof from `cbrn_calculate_action_protection`.

Shared protection alone owns real automatic issue, donor debit, fitting, filter wear and control-transfer losses.
A snapshot refresh neither creates equipment nor purchases a second issue.
Storm clearance preserves already issued masks and replacement demand.
Missing dust proof is diagnosed and blocks claimed mask benefit rather than being silently interpreted as protection.

## Military and air release gates

Part 03's numerical tables specify observable outcomes rather than assumed same-named local modifier tokens.
Implement every visibility, coordination, reconnaissance, planning, movement, organization, attack, defense, breakthrough and air consequence through verified local consumers.
Country intelligence, map opacity and commander-wide penalties cannot replace battlefield-local effects.

E6 documents controller-specific speed, owner-relative enemy speed and `attacker_modifier`, while E5 supplies a state attack precedent.
Their combination still requires occupied-state, ally, enemy, neutral-transit and outside-attacker proof.
One battle must not receive two complete storm bundles merely because both participants are covered.
D4 follows only the purchasing country's eligible local formations.

E8 documents `every_state_division`, and E7 documents `set_unit_organization` on a zero-to-one scale.
The actual current-value reader and geographic membership remain native gates.
Weather drain only lowers organization and respects the ten-percent weather floor without healing a unit already below it.
Lost organization is not restored from a pre-storm snapshot.

Local air projection must cover land and ocean regions, affected airfields and actual operations for both sides.
Static weather-region modifiers in E6 do not prove an event-controlled regional writer.
D5's field, wing and mission relationship requires demonstrated operation-local effects and owned cleanup.
A zero comparable accident baseline needs an explicit verified interpretation.
No national air penalty or arbitrary aircraft-stock destruction substitutes for the required local disruption.

## Physical damage and repair ownership

E3's `damage_state_building_dynamic` takes explicit temporary building token and positive damage in a state already selected by the footprint.
Do not use `damage_buildings_in_random_states` because it reselects geography and includes an independent population branch.
Railway damage must identify actual exposed segments and preserve other owners' damage.

Use the parent's deterministic mixed-intensity age refinement as the implementation proposal for Part 04.
Normal hours contribute one equivalent hour, severe hours two, extreme hours four and weakening hours zero toward a forty-eight-equivalent-hour grace.
Only the fraction of an interval beyond that threshold contributes physical damage.
Thus forty-eight normal hours, twenty-four severe hours and twelve extreme hours have the same qualifying age.
Retain the passage receipt until forty-eight hours fully clear, so alternating bands and merge identities cannot restart grace.
Apply each band's rate to its qualifying excess time, with the Part 04 entry-capacity snapshot and passage caps.

Already damaged capacity is not available again until actual repair restores it.
D2 and D5 airfield protection use the stronger applicable reduction rather than additive duplicate reductions.
Cleanup does not repair buildings, erase rail damage or recreate levels.
M3 observes actual repair and access restoration without creating a second payment or free restoration.
The proposed accepted repair adapter retains actual remaining damage receipts by cause and passage within each native building or segment pool.
Allocate a verified actual repair delta proportionally across known remaining damage amounts, capped by each receipt, and retain fractional attribution without duplicating the physical repair.
Unresolved competing damage, demolition, construction or unexplained capacity changes earn no claimed 099 repair credit until identified.
M3 freezes a positive initial eligible damage cohort and fourteen-day clear-weather assessment budget.
Only actual returning footprint pauses it, and clearance resumes the same remaining budget without incorporating new damage into the original denominator.
Authority loss interrupts it, and the absolute ACH03 and ACH05 windows do not inherit the pause.

## Response and payment authority

| Family | Authority | Payment and completion boundary |
| --- | --- | --- |
| D1 Household retreat | Current civilian controller | No stock debit, six-hour preparation, actual-exposure sacrifice and twenty-four-hour commitment |
| D2 Protect machinery | Relevant facility controller | PP and support equipment plus verified two-factory preparation commitment |
| D3 Essential corridor | Valid physical route authority | PP, support equipment, trucks and fuel for one nonoverlapping section |
| D4 Field command precautions | Country commanding eligible formations | CP and Army Experience with local response and slower-operation sacrifice |
| D5 Airfield preservation | Airfield controller and own relevant operator | PP and support equipment with observed local reduced-operation policy |

Quote complete current costs using the universal cost owner and the same target-specific ordinary calculation for display, affordability and confirmation.
Requote immediately before payment because a saved quote is neither a reservation nor a payment receipt.
Preflight every component and protected commitment before any benefit.
Record actual successful component debits under one transaction and unique component IDs.
On execution failure, refund only recorded actual debits once through the owner.
Settle only after the transaction's refund boundary is correctly resolved.
A successfully paid preparation later overtaken by the wall is an interrupted project, not an invented full refund.

Factory time is an explicit commitment through a verified owner seam rather than a hidden additional consumed resource.
Do not reserve unavailable or already committed factories twice.
Unsupported payment kinds and factory commitments require exact adapters.
D3 shows all four payable components in its complete tooltip even when only three compact icons fit.

Responses store payer, target, authority revision, transaction, preparation time, physical protection, operational policy and completion receipt separately.
Capture stops the former operator's future policy while preserving completed facility protection where Part 05 requires it.
Release only unused future commitment, preserving elapsed factory time and consumed materials.
Missions observe paid responses and actual outcomes without charging again.
M1 diversion closes neutrally, M2 measures valid service intervals and M3 measures actual repaired capacity.
Renewals and automated purchases use the same validity, quote, reserve and receipt gates as manual purchases.
D4 and D5 admit only one preparation or effective package for their canonical authority and physical target, with no early timer refresh or duplicate manual and automated purchase.
One formation receives at most one D4 contribution across overlapping eligible operating areas.
D3 traffic risk uses canonical route cells clipped to actual footprint and requires verified useful traffic, while idle or blocked paid routes contribute no invented service or traffic risk.
M2 requires a complete six-hour qualifying exposed interval, useful throughput and an applied D3 benefit, and zero-exposure diversion closes neutrally.

## Shared owner links and accounting

Use the [migration owner](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/migration_system.md) for evacuation, cohorts, route risk, destination safety, reception and exact transfer.
Use the [protection owner](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/cbrn_scripted_effects.md) for real issue and owner acceptance of the proposed neutral dust adapter.
Repair links select actual native construction or railway work and remain blocked until the chosen interface and allocation consumer are inspected.
The [cost owner](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md) owns quote composition, actual-paid refunds and settlement.
Famine receives proven access or pressure through its own accepted adapters without an event-owned stage meter.

The [Air owner](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/air_cleanliness/natural_sources.md) requires a narrow accepted extension before 099 can submit dust pressure.
The season admission allowance is at most two basis points of additional monthly reservoir pressure, subject to actual accepted room under the shared four-basis-point cap.
Store only actual admitted pressure in the 099 allowance receipt and deduplicate cadence independently of movement updates.
Do not impersonate an Event 013 sequence or create a new visible source category.
Clearing a footprint stops its future emission requests without subtracting from the shared aerosol reservoir or accepted atmosphere.
Existing decay, recovery, source history and actual-net-delta Chaos conversion remain Air-owned.

Versioned Heat Wave and Acid Rain facts must prove coincident geography and time before the bounded Part 04 risk interaction.
Missing or stale proof produces no guessed interaction.
Companion owners must not award the same interaction premium twice.

Part 07's event-owned Chaos receipts have a maximum positive total of 35.
Each reversal references an actual awarded receipt and cannot exceed it.
Flags, menus, logs, threshold changes and ordinary movement add zero.
Shared Deaths and atmospheric change keep their own conversion without duplicated geographic bonuses.
An already reversed milestone cannot be farmed by another split, return or merge.

## Legacy migration and cleanup

New 099 entry routes to one global season while retaining stable event identity and the tier-1 and cluster contract.
Do not retain E1's Wider Disaster Seasons dependency.
Existing Event 013 local dust jobs remain separately owned, including in-flight work created by the old bridge.
Do not copy private Event 013 queues or generate daily Event 013 aftermath cards.
Versioned migration must distinguish an old 099-fired receipt from unrelated local dust and prevent another fire-once opportunity.
Ambiguous legacy ownership is diagnosed rather than guessed.

| Owned object | Clearance or interruption | Final season closure |
| --- | --- | --- |
| Acute 099 military, air and industrial contribution | Recompute union and remove only at zero coverage | Retire all remaining 099 contributions |
| Geometry and forecast cache | Refresh sparse dirty scopes | Remove active projections and preserve history |
| D1 household policy | End exposed sacrifice and apply control handover | Close only 099 policy |
| D2 and D5 physical preparation | Preserve completed protection under valid duration and passage rules | Expire acute 099 bonuses at clearance and retain completed-work receipts and consumed-material history |
| D3 and D4 operational policy | Stop invalid local benefit and sacrifice | Close 099 operating policy |
| Factory commitment | Release unused future capacity | Release only remaining 099 commitments |
| Payment receipt | Refund only proved failed execution | Retain settlement and duplicate-refund evidence |
| Population and Deaths | Preserve committed measured loss | Preserve historical receipts |
| Building and railway damage | Keep actual damage and repair work | No automatic repair |
| Shared issued masks | Protection owner handles transfer and wear | No stock refund or deletion |
| Aerosol pressure and atmosphere | Stop future local emissions | No guessed subtraction |
| Migration and famine | Notify through accepted owner seam | Preserve independent live obligations |
| Event 013 dust and aftermath | Never clear through 099 cleanup | Remain Event 013-owned |

### Bounded observation after the front closes

Closing the front scheduler ends every new 099 acute-weather mutation, including uncommitted historical damage, by the immutable day-360 horizon.
It does not cancel a legitimate recovery, evacuation, settlement or achievement assessment that began from verified season receipts.
The existing recovery and achievement coordinators retain a sparse queue of qualifying districts, formations, routes and cohorts with explicit owner, reason, remaining assessment time or absolute deadline, and terminal status.
The migration and famine owners continue their independently valid obligations through their own schedulers.
No new recurring global state or country scan is introduced.

M3 can spend its remaining fourteen-day clear-weather assessment budget after the season closes, without resetting that budget or its original damage cohort.
ACH099_03 keeps its absolute fourteen-day deadline after second clearance.
ACH099_05 keeps its absolute twenty-one-day deadline after global season closure.
ACH099_04 keeps its twenty-one-day safety and supply observation after actual settlement, even if a valid migration cohort settles after the front has ended.
Other qualifying tasks retain their expressly specified windows, including ACH099_08's seven days after its formations clear.
Native repair progress, ordinary owner-managed migration outcomes and observation of current conditions remain permitted and do not reopen weather damage or material admission.

Retain the required damage allocations, paid-work receipts, cohort identities, eligibility snapshots and consumed front tombstones until their bounded live obligations reach a terminal result.
Then release observer work and archive immutable outcome and deduplication history under the existing owner's retention policy.
Reload and host transfer preserve deadlines and remaining time.
Missing owner observations remain unverified, and closure supplies neither assumed success nor a second award opportunity.
This is a lifecycle dependency of existing systems, not another player-facing meter or a longer storm.

## Required validation evidence

Source tests must cover floor rounding, fractional population, one debit, measured Deaths, exact quotes, partial refunds, duplicate receipts, aligned arrays and cutoff operators.
Native evidence must cover actual population and owner/controller manpower, local military symmetry, land and sea air operations, continuous visible geography and payment behavior.
Save and reload must preserve front identities, geometry, steering, admission counts, material balances, fractional carry, paid preparations and receipt states.
Control transfer must reconcile authority, facility protection, shared mask ownership, route validity and unused commitments without refunds or duplicate benefits.
Host loss must preserve season identity and make old wakes harmless.
Test day-300 creation rejection, day-330 taper and day-360 acute-weather mutation rejection, including delayed work and queued evolution entry.
Also prove that a qualified late-season recovery or settlement completes its original bounded observation window after front closure without new 099 weather damage, discarded receipts, timer resets or repeated awards.
Trace split, return, reseed, merge and overlap without repeated state doses.
Retiring 099 alongside acid rain, ash, smoke, migration, famine and Event 013 dust must preserve their ownership.
Unresolved engine or owner proof remains an explicit release gate and never a silent feature cut.
