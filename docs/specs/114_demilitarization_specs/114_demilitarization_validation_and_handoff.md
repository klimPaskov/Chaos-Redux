# Demilitarization: validation and implementation handoff

This document translates the accepted gameplay design into evidence requirements. It contains proposed implementation boundaries and unproven native capabilities. It is not a report that the game has been implemented or tested.

The full gameplay specification is in the seven design files. The user brief fixes the universal border rule, war suspension, peace restoration, three evolution concepts, and independence of Event 096. Controller-based geometry, cumulative stage timing, monotonic capital treatment, cohesion, response costs, personnel returns, and achievements are parent-authored expansion choices.

## Resolve native capabilities before building dependent systems

| Gate | Required proof | What does not establish the result |
| --- | --- | --- |
| GATE-01: true land adjacency | Exact installed state/province edge classification, including straits and impassable borders. | A neighbouring-state result without an edge-type check. |
| GATE-02: existing units and zero usable space | Real formations survive the complete required DMZ footprint, with valid behaviour when every domestic state is restricted. | A default teleport to the capital, a replacement army, or an exempt border capital. |
| GATE-03: partial personnel loss | An exact existing division loses actual soldiers without template changes, equipment damage masquerading as desertion, or casualty registration. | Reducing the national manpower pool, organisation, recruitment, or a general strength modifier. |
| GATE-04: selected peaceful disband | Exactly one intended formation disappears and its actual personnel and equipment disposition is measurable. | Deleting every division of the same template or assuming destruction has disband refunds. |
| GATE-05: persistent identity and accounting | Delayed notices, programme targets, loss receipts, and personnel returns retain valid identities and pay once. | A temporary event target treated as an immortal division identifier. |
| GATE-06: complete DMZ source ownership | Every applicable writer can acquire, retain, and release its own obligation through the aggregate. | An initial boolean snapshot or an unguarded reference count. |
| GATE-07: lifecycle coverage | First-war, last-war peace, controller, owner-only, capital, release, annexation, and save reconciliation are covered at valid callback boundaries. | A hidden periodic global sweep or a guessed callback name. |
| GATE-08: production integration | Current IDs, event/cluster registry, canonical workbook, history actors, resources, and actual UI consumers agree. | Negative search results or a supplied CSV treated as current registry authority. |

These are development proof tasks. They are not questions the user must answer before receiving this specification.

The inspected offline reference supports state DMZ setting, actual division iteration, division destruction, group disband filtering, and state-based army teleportation. It does not settle all the semantics above. Keep an unsupported mechanic blocked and report the exact missing proof. Do not quietly weaken the design to make a validator pass.

## Source ownership and transaction authority

The physical state DMZ must equal the OR of valid current source obligations. Sources use idempotent membership with owner identity. Repeated acquisition does not increment an unguarded counter.

Each Event 114 claim records its current holder country and generation. An old-controller cleanup may release only the receipt it still owns. It cannot remove a replacement claim held by the new controller.

Migrate the relevant Event 001 and Event 018 direct writes and cleanup through narrow owner adapters in the same integration. Preserve those events' own non-DMZ behaviour. Inventory installed vanilla and other-mod writers, including history and treaty expiry. An unknown external source must remain an explicit compatibility gap.

A loss receipt contains the event generation, actor, exact formation identity, operation identity, selected outcome, and measured result. Physical mutation has one owner. Receipts already consumed are not fresh operation results.

Caller-owned temporary outputs must be initialised before helper calls. Preserve native callback ROOT and FROM meaning. State pointers require state-appropriate validation. Entering a country scope does not rebind the original ROOT.

## Accounting that must balance

For a personnel incident:

**Actual deployed-personnel decrease = immediate native return + living personnel recorded as unavailable.**

For a delayed return:

**New recruitable credit = exact unconsumed amount due from that receipt.**

For equipment removed from a dissolved formation:

**Actual issued-equipment decrease = actual stockpile recovery + recorded unrecoverable equipment.**

Reconcile any native refund before applying a correction. Template capacity and expected stockpile changes are not actual observations. Verify whether country aggregates update within one transaction and whether other reinforcement operations can contaminate the measurement.

Partial desertion retains equipment. Spontaneous dissolution uses 80% actual equipment recovery and 90-day personnel return. Voluntary consolidation uses actual immediate native refunds. These outcomes must remain distinguishable.

Military service accounting must not call civilian population-transfer or civilian Deaths helpers. Unusual formations with zero human manpower must not generate human deserters from template labels.

## Bounded lifecycle work

Use one authorised activation pass. Thereafter, process registered actors and deduplicated dirty state neighbourhoods from actual changes.

The offline on-actions reference supports the intended first-war and last-war boundaries. Capture the new controller, old controller, and changed state before helper rescoping. Reconcile after a native transfer is stable, while preserving immediate war-entry release.

An event-owned country worker can schedule its own next due review. It stops for wartime losses and does not accumulate missed desertion. Due personnel returns retain calendar dates.

Queues that exceed the native 1,000-operation loop ceiling must preserve their unvisited suffix. Save/load reconciliation resumes valid work, not the original physical incident.

Explicit ownership-only transfers and capital changes need owner notifications where native coverage is missing. The final implementation must prove those wake-up paths. A rare local reconciliation event cannot repair a change that never wakes it.

## Registry and owner map

| Surface | Current documented or inspected owner |
| --- | --- |
| Event entry and repeatable registration | Event entry chaosx.nr114.1, global.repeatable_events, and common/scripted_effects/chaosx_logic_effects.txt. Reconcile type, dispatch, and enable allowlist. |
| Event names and debug labels | localisation/english/chaosx_event_names_l_english.yml and the existing event-log/debug scripted localisation selectors. |
| History, evolution, and detail data | common/scripted_effects/chaosx_events_log_effects.txt. Prepare global or real-country actor context before the shared recorder. |
| Event text | Resolve the supplied _chaosx_events_l_english.yml versus chaosx_events_l_english.yml path difference against the current checkout. |
| Peace cluster | common/script_constants/event_cluster_constants.txt and common/scripted_effects/chaosx_event_cluster_effects.txt. Preserve existing cluster ID 4 and implemented member-row identities. |
| Chaos change and history | common/scripted_effects/chaos_meter_effects.txt, including add_chaos_meter_value and record_chaos_meter_history_entry. |
| Chaos reasons | Existing common/script_constants/chaos_meter_constants.txt ownership. Check collisions before adding event-specific reason identities. |
| Achievements | common/achievements/chaos_redux_achievements.txt and root gfx/achievements/ outputs. |
| Catalog workbook | docs/spreadsheets/chaos_redux_events_catalog.xlsx. Inspect through the owner spreadsheet workflow before editing. |
| Event documentation | docs/events/114_demilitarization/ and the relevant shared system documentation after implementation. |
| Asset working evidence | docs/assets/114_demilitarization/ with durable provenance promoted before final cleanup. |

The shared Chaos entry accepts a requested change and custom-reason context, rounds the request, applies the current meter policy, and records a history entry when appropriate. Do not bypass that policy or claim the requested change was applied when the shared system blocked it.

The ordinary history recorder runs before the entry event's immediate body. A global opening needs the real shared no-actor convention prepared in time. A random dispatch country is not automatically the cause of a worldwide event.

The current Peace runtime setup requires a White Peace context. Change that requirement to follow selected member contexts so 114 can initiate a valid peacetime burst. Preserve High's shared effective severity floor and separate it from the event's catalog Chaos level.

## Concrete acceptance matrix

| ID | Situation | Required outcome |
| --- | --- | --- |
| T01 | Inland country with several true foreign land borders | Baseline includes every border state and leaves the interior available. |
| T02 | Three successive internal layers | Deeper adds exactly the first inward layer, even after repeated recalculation. |
| T03 | Coastline, island, and strait-only neighbour | No false land-border state. |
| T04 | Exclave and impassable true frontier | Correct political geometry without invented movement access. |
| T05 | Border capital | Restricted at baseline and remains restricted at Total. |
| T06 | Deep inland capital at Total | Sole refuge only if outside all required earlier belts. |
| T07 | One-state country with an existing army | Strict footprint and exact formation preservation both hold. |
| T08 | Mixed province control within one state | The documented whole-state controller rule is applied consistently. |
| W01 | A country declares war or is attacked | Event 114 claims release at its first-war transition. |
| W02 | One of two wars ends | Remain suspended until the last war ends. |
| W03 | Last-war peace after conquest | Rebuild current geography, with no obsolete state snapshot. |
| W04 | Peaceful subject, belligerent overlord | Subject remains restricted until it joins a war. |
| W05 | Two short wars between reviews | Preserve remaining peace interval, costs, notices, and receipts. |
| O01 | 001 then 114, followed by 001 cleanup | 114's physical restriction remains. |
| O02 | 114 then 018, followed by 114 war suspension | 018's current restriction remains. |
| O03 | Vanilla restriction expires under 114 | No resurrection of the expired source when 114 releases. |
| O04 | Old-controller callback after transfer | Cannot clear or recreate the new holder's claim. |
| O05 | Unknown external source | Explicit compatibility gap with no speculative clear. |
| U01 | Evacuation into a valid interior state | Same units, manpower, variants, experience, and templates survive. |
| U02 | Foreign divisions in the host's DMZ | Correct owner and lawful treatment for each formation. |
| U03 | Capital itself in the final footprint | No default relocation into an invalid refuge. |
| D01 | Two divisions with the same template | Only the selected unit loses personnel or dissolves. |
| D02 | Depleted mixed-model formation | Account for actual holdings, not nominal capacity. |
| D03 | Partial desertion | Fielded manpower falls and gear remains, with one matching living-personnel receipt. |
| D04 | Spontaneous dissolution | One unit disappears, exact personnel return obligation, 80% actual gear recovery. |
| D05 | Voluntary consolidation | Immediate actual native refund, no delayed receipt or spontaneous-loss credit. |
| D06 | Zero-human-manpower formation | No invented ordinary soldiers. |
| D07 | War immediately before loss commitment | No new peacetime loss. |
| D08 | Duplicate callback and delayed return | No second debit, credit, random draw, or award. |
| D09 | Annexation before return | Verified succession or consumed native entitlement, with no duplicate manpower. |
| C01 | Each response at exact cost threshold | Correct charge, duration, benefit, and current eligibility. |
| C02 | Programme cancelled by war | Release continuing commitment, retain sunk costs and stated aftermath. |
| C03 | Cadre completion and muster due together | Deterministic fair ordering with one final outcome. |
| C04 | Target disappears during confirmation | Harmless cancellation and no substitute target. |
| C05 | Poor country with no factories | Honest alternatives and AI weights, without free capacity. |
| C06 | Cadres finish one day after the muster deadline | No retroactive programme completion or false saved-formation receipt. |
| C07 | Service conditions complete on a review date | Final earned +4 review benefit and +12 completion each settle once. |
| C08 | Enforcement cancels after its initial benefit | Any cancellation settles its −10 aftermath once and preserves unconsumed backlash. |
| C09 | Notice ends at cohesion 25–34 | Failed-muster −5 follows classification, with no dissolution draw and the stated cooldown. |
| E01 | Evolved first opening | One physical opening and one cohesion initialisation. |
| E02 | Disabled predecessor | No hidden activation or downstream unlock. |
| E03 | Stage activates with no material footprint change | History can record the stage, direct Chaos remains zero. |
| R01 | Repeat inside the country guard | No renewed shock, review reset, or extra loss roll. |
| R02 | All countries at war or no meaningful repeat effect | Honest N/A availability and no empty mandatory context. |
| R03 | Repeat freezes several valid country targets | Each independently guarded valid cohort receives −8 once, with no extra country draw or review. |
| X01 | 096 lock active during loss, consolidation, and war | Event 114 never clears independent restrictions. |
| X02 | 114 and another crisis select the same unit | One mutation owner, second claimant revalidates. |
| H01 | All five achievements and one near-miss each | Historical conditions proven, no final-state shortcut. |
| H02 | Global opening and local loss history | Correct actor, date, event identity, and actual consequence. |
| H03 | Army becomes empty halfway through a timed challenge | No empty-time progress, with the required attempt and review-streak resets. |
| H04 | Recovery charge was blocked or partly clipped | Only actual eligible contribution can be reversed, with whole-charge eligibility consumed once after a successful reduction. |
| Q01 | More than 1,000 queued records | Unvisited work retained and processed once. |
| Q02 | Save/load during notice, programme, and return | Valid identity, remaining times, and committed results survive. |

These are acceptance cases to execute during implementation. None is reported as run in this planning package.

## Specialist and tool sequence

1. The implementation owner reads the accepted design, current AGENTS.md, and current owner skills. Resolve native gates and effective source identity first.
2. Use chaosx_scripted_system_architect for the narrow resolver, callbacks, and exact-unit transactions. The present planning consultation supplies the boundaries, not completed code.
3. Use chaosx_ai_probability_auditor, beginning with hoi4.probability_inspect. Evaluate and sweep the scenarios in world_interactions, then compare and render meaningful results. Use simulation and sequence analysis for review timing and intervention outcomes.
4. Use the actual read-only map inspector and installed adjacency data for T01–T08. Use hoi4.reference_context, reference_search, reference_read, and source_lookup for exact primitive and writer questions.
5. Use hoi4.event_inspect for chaosx.nr114.1, state_flow, and impact with full helper coverage. Use event_render and event_compare on the same verified source graph.
6. Use hoi4.script_validate where exposed, reporting checksPerformed and unresolved arguments honestly. Source validation does not prove native refunds or zero-space army behaviour.
7. Route the ordinary category and missions through the decision skill. Route each visual family through its production specialist and actual consumer checks.
8. Run the actual chaosx_improvement_loop_planner near implementation completion with fork_turns set to none. Resolve its accepted findings. Complete localisation and event-completion audits.

No HOI4 MCP tools were exposed in this planning session. These names identify future routes from the supplied guides. Discover their current schemas and service health before use. Do not fabricate fields or claim calls that did not run.

The implementation agent does not launch HOI4 or ask for a routine log/restart ritual. Review existing or voluntarily supplied live evidence through the project workflow. Report precisely which native behaviours still lack proof.

## Completion boundary

An implementation is incomplete while any required native gate, accepted gameplay feature, source-owner integration, achievement history, asset consumer, or mandatory audit remains unresolved. Do not mark the catalog Playable without the explicit approval required by the project.

This specification package preserves the intended design while exposing those gates. It does not turn an unverified primitive into a promise of a working game feature.

