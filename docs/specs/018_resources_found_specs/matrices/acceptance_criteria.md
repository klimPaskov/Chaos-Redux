# Event 018 Full Acceptance Criteria

This checklist defines completion. A checked item must be supported by implementation evidence, not a placeholder or future-work note.

## Evidence mode and proof boundary

Checkbox state is reconciled against the current implementation on 2026-07-12.

- `[x]` means the accepted requirement is supported by current deterministic script definitions, exact fixtures, focused static audits, registered runtime assets, documentation, or workbook evidence.
- The user explicitly waived launching Hearts of Iron IV for this pass. Checked engine-facing scenarios therefore record accepted definition-based and static evidence. They do not claim observed live gameplay, combat, GUI scale, music playback, or campaign AI behavior.
- All 363 accepted requirements are closed. The fresh event-completion, selected-field UI and localisation, and asset and audio audits returned PASS after their recorded repairs.
- Optional ideas rejected by the improvement-loop review are outside the accepted Event 018 design and are not completion blockers.

Primary evidence is indexed in [the static acceptance report](../../../plans/018_resources_found_plans/018_static_acceptance_report.md), [the implementation-depth disposition](../../../plans/018_resources_found_plans/018_resources_found_implementation_depth_addendum.md), [the improvement-loop closure handoff](../../../plans/018_resources_found_plans/improvement_loop_closure_handoff.md), and the focused auditor and production handoffs under `docs/plans/018_resources_found_plans/subagent_handoffs/`.

## Source design and classification

- [x] Event ID remains 18.
- [x] Canonical entry uses the `chaosx.nr18.1` root.
- [x] Event remains Minor Repeatable.
- [x] Event is not assigned to an event cluster.
- [x] Event is enabled by default only after the rework is implementation-ready.
- [x] Baseline works when all four evolutions are disabled.
- [x] Baseline lifecycle stages are not logged as evolutions.
- [x] Every final design change is represented in source specs or has an explicit plan disposition.

## Random discovery

- [x] Owner selection excludes invalid actual nonhuman and terminal actors.
- [x] State selection verifies owned and controlled valid state.
- [x] Impassable and incompatible states are excluded.
- [x] Standard resource selection is truly random among oil, aluminium, rubber, tungsten, steel, and chromium.
- [x] Terrain affects presentation and state weighting, not final resource-type legality.
- [x] Baseline deposit is centered around 100.
- [x] Repeat firing can create a new field.
- [x] Repeat firing can enrich an existing active field.
- [x] Duplicate resource rolls stack in the same state.
- [x] Different resource rolls create a multi-resource field.
- [x] Repeat events use follow-up text rather than replaying the first-discovery tutorial.

## Field persistence and resource ledger

- [x] Every active field has one stable field record.
- [x] Field record contains state, discoverer, owner, controller, discovery date, discovery count, stage, posture, and status.
- [x] Event-owned oil is stored separately.
- [x] Event-owned aluminium is stored separately.
- [x] Event-owned rubber is stored separately.
- [x] Event-owned tungsten is stored separately.
- [x] Event-owned steel is stored separately.
- [x] Event-owned chromium is stored separately.
- [x] Total Event 018 resource amount can be calculated safely.
- [x] Distinct resource count can be calculated safely.
- [x] Largest single-resource amount can be calculated safely.
- [x] Field survives repeat discovery without duplicate initialization.
- [x] Field survives temporary occupation.
- [x] Field transfers safely with state ownership.
- [x] Contracts and political rights are reviewed separately from physical state transfer.
- [x] Annexation and country removal clean stale targets and selections.
- [x] A state cannot hold duplicate active field records.

## Field UI and values

- [x] Decision category opens for the owner.
- [x] Compact scripted GUI header shows selected state.
- [x] Header shows Event 018 resource composition.
- [x] Header distinguishes Event 018 additions from total state resources.
- [x] Developed Yield is visible as integer and band.
- [x] Excavation Depth is visible as integer and band.
- [x] Workforce Safety is visible as integer and band.
- [x] Foreign Pressure is visible as integer and band.
- [x] Subsurface Disturbance becomes visible only after its reveal.
- [x] Breach Pressure becomes visible only in Evolution III.
- [x] Each value has cause-and-effect tooltip direction.
- [x] Selected-field cycle works for multiple fields.
- [x] Lost or closed selected field advances to next valid field.
- [x] Human field selection does not block AI evaluation of all fields.
- [x] Static fallback exists for every animated UI state.

## Administration and baseline economy

- [x] National resource authority posture exists.
- [x] Domestic commercial charter posture exists.
- [x] Foreign concession posture exists.
- [x] International commission posture exists when unlocked.
- [x] Strategic reserve or suspension posture exists.
- [x] Posture changes require transition cost and time.
- [x] Geological appraisal is an active project.
- [x] Deeper testing can improve the field and raise depth.
- [x] Primary works create a meaningful state or yield change.
- [x] Transport project changes rail, infrastructure, supply, or route behavior.
- [x] Heavy machinery changes yield and depth.
- [x] Local processing creates a meaningful map or production effect.
- [x] Worker settlement or administration can reduce labor strain.
- [x] Safety actions materially reduce accident and later death risk.
- [x] Stable mature-field identities exist.
- [x] Field maintenance does not become a tray of tiny passive modifiers.

## Trade and diplomacy

- [x] Foreign interest uses actual deficit, route, relations, war, proximity, rivalry, and field value.
- [x] Only high-value foreign candidates receive active actions.
- [x] Buyer, investor, strategic claimant, and crisis behavior are distinct.
- [x] Owner can invite bids.
- [x] Owner can sign a persistent export contract.
- [x] Contract records buyer, term, access, and lifecycle.
- [x] Route loss interrupts delivery.
- [x] Occupation interrupts or changes delivery.
- [x] Suspension pauses or breaches contract.
- [x] Closure settles or terminates contract.
- [x] Buyer disappearance cleans contract.
- [x] Owner can reserve output for domestic use.
- [x] Owner can balance competing buyers.
- [x] Foreign investor can offer machinery and transport.
- [x] Exclusive access creates rival pressure.
- [x] Concession influence is visible and bounded.
- [x] Nationalization requires preparation and creates compensation consequences.
- [x] Fair compensation can settle dispute.
- [x] Smuggling pressure has actual causes and state-route counterplay.
- [x] Espionage and sabotage can be exposed.
- [x] Diplomatic reaction strength reflects material stake.
- [x] Event uses normal strategic resources and does not create a parallel trade currency.

## Commission and border conflict

- [x] International commission can emerge from severe competition or mediation.
- [x] Commission defines quotas, inspection, and troop restrictions.
- [x] Demilitarization is negotiated rather than random.
- [x] Field guards remain possible under demilitarization.
- [x] Commission compliance can be maintained or violated.
- [x] Commission dissolution cleans rules and targets.
- [x] Border claimant requires a real claim or mapped dispute.
- [x] Adjacency alone cannot create a claim.
- [x] Border crisis requires high field importance and pressure.
- [x] Competing survey stage exists.
- [x] Customs or road confrontation stage exists.
- [x] Armed patrol incident stage exists.
- [x] Timed frontier mission uses named state, supply, or troop objectives.
- [x] Border war uses a limited contest where designed.
- [x] Owner victory has settlement.
- [x] Claimant victory transfers state and field safely.
- [x] Stalemate can create commission or ceasefire.
- [x] State transfer preserves physical ledger and changes contracts.
- [x] Border conflict cannot fire from impossible military conditions.

## Suspension and closure

- [x] Suspension is reversible and distinct from closure.
- [x] Suspension suppresses extraction and risk growth.
- [x] Suspension retains field ledger and maintenance decisions.
- [x] Baseline closure is a multi-step project.
- [x] Closure scales with yield, depth, resource diversity, contracts, danger, and control.
- [x] Closure settles workers and contracts.
- [x] Closure removes every Event 018 resource addition.
- [x] Closure removes no preexisting state resource.
- [x] Closure cleans modifiers, decisions, targets, and UI.
- [x] Permanently closed state is excluded from future Event 018 selection.
- [x] Partial closure is visibly distinct and does not claim permanent prevention.

## Evolution I

- [x] Evolution I has a pre-fire opening.
- [x] Pre-fire opening adds 2 to 4 independent large rolls in one state.
- [x] Duplicate rolls stack.
- [x] Evolution I has an active-field entry.
- [x] Active entry adds deposits and compound-field decisions.
- [x] Multi-resource administration is playable.
- [x] Integrated processing corridor is meaningful.
- [x] Foreign Pressure sensitivity increases.
- [x] Commission and DMZ routes can open.
- [x] Evolution I has a stable non-supernatural ending.
- [x] Evolution I logs through shared evolution system.

## Evolution II

- [x] Evolution II has a stronger pre-fire opening.
- [x] High-stage first firing still begins with discovery and gradual incidents.
- [x] Worker sickness incidents use concrete ordinary explanations first.
- [x] Corrosion and missing-worker incidents exist.
- [x] Safety investment reduces deaths and slows danger.
- [x] Subsurface Disturbance reveal has physical evidence.
- [x] Disturbance is visible after reveal.
- [x] Disturbance changes available actions and evolution timing.
- [x] Creature incidents remain underground at first.
- [x] Player can restrict workings.
- [x] Player can conduct scientific or military survey.
- [x] Player can conceal and militarize with consequences.
- [x] Player can begin full closure.
- [x] Worker and field deaths use shared Deaths system.
- [x] Real state population is reduced safely.
- [x] Evolution II can stabilize if Evolution III is disabled.
- [x] Evolution II logs through shared evolution system.

## Evolution III

- [x] Evolution III pre-fire opening creates a very large deposit of every standard resource.
- [x] First firing at Evolution III preserves gradual Evolution II incidents.
- [x] Public perimeter breach event exists.
- [x] Breach Pressure becomes visible.
- [x] Settlement attacks exist.
- [x] Transport disruption exists.
- [x] City intrusion can occur.
- [x] Population flight or evacuation is represented without duplicating another event system.
- [x] Monster hunts require supplied hard-attack capable forces.
- [x] Hunt success and failure are distinct.
- [x] Evacuation uses trains, trucks, routes, time, and receiving capacity.
- [x] Continued extraction worsens visible crisis and exploitation score.
- [x] Partial sealing delays but does not prevent Evolution IV.
- [x] Full sealing requires suspension, evacuation or control, engineering, and surface containment.
- [x] Successful full seal removes all Event 018 resources.
- [x] Successful full seal permanently prevents Evolution IV for the field.
- [x] Successful full seal has no secret supernatural punishment.
- [x] Evolution III can remain containable if Evolution IV is disabled.
- [x] Evolution III logs through shared evolution system.

## Evolution IV emergence

- [x] Evolution IV cannot occur on the first discovery day.
- [x] Final breach uses dynamic timing and a public-crisis minimum.
- [x] Cave country uses one stable tag.
- [x] Cave country is registered as special chaos and actual nonhuman.
- [x] Cave country receives field state and capital safely.
- [x] Former owner and controller receive correct aftermath.
- [x] Existing cave-country case is handled.
- [x] Origin field history is recorded.
- [x] Starting army uses exploitation history.
- [x] Starting army minimum is credible.
- [x] Starting army never exceeds 30 divisions.
- [x] High safety, evacuation, and sealing can reduce opening strength.
- [x] Cave country declares war on all current land neighbors.
- [x] Newly adjacent land neighbors are declared upon once.
- [x] Emergence uses unique super-event image and audio.
- [x] Evolution IV logs through shared evolution system.

## Cave-country package

- [x] Public country name and adjective are original and map-readable.
- [x] Ruling party and sub-ideology are original nonhuman identities.
- [x] Leader is literally a cave monster.
- [x] Leader has an original authored name or original nonhuman pool.
- [x] No human regional name pool is used.
- [x] Static leader portrait exists.
- [x] Animated leader portrait package exists with real source frames.
- [x] Base flags exist in normal, medium, and small sizes.
- [x] Any world-end cosmetic identity has distinct flags.
- [x] Starting ideas have lifecycle and counterplay.
- [x] Base cave template is very slow and heavily armored.
- [x] Hard attack and piercing are effective counters.
- [x] Cave country has no normal manpower economy.
- [x] Cave country has no normal equipment economy.
- [x] Core brood training queue is disabled.
- [x] Captured factories support cave systems rather than human weapons.
- [x] Cave country has no ordinary trade.
- [x] Cave country has no ordinary faction membership.
- [x] Cave country has no routine navy or air force before world end.
- [x] Country has enough supply to function at origin.
- [x] Origin loss creates a severe but clean crisis.

## Captured-resource deployment

- [x] Total strategic resources in captured state are summed correctly.
- [x] Capacity uses floor of total divided by 10.
- [x] State capacity is capped at 10.
- [x] Origin state is excluded regardless of resource total.
- [x] Capacity requires continuous control for activation period.
- [x] Activation is visible and interruptible.
- [x] New divisions spawn automatically and sequentially.
- [x] Several state captures do not create an instant stack.
- [x] Human player can see capacity and next spawn.
- [x] AI can manage queue and targets.
- [x] Destroyed division frees one capacity slot.
- [x] Losing a state starts a grace period.
- [x] Excess divisions weaken rather than vanish.
- [x] Recapturing capacity can restore support.
- [x] Liberating state removes anchor after cleanup.
- [x] Ordinary resource output can be restored safely.

## Cave focus tree and decisions

- [x] Opening survival lane exists.
- [x] Origin stabilization exists.
- [x] Brood hierarchy lane exists.
- [x] One Maw route is implemented or an accepted equivalent preserves centralization design.
- [x] Many Chambers route is implemented or an accepted equivalent preserves distributed design.
- [x] Hoard the Veins route is implemented or an accepted equivalent preserves rich-anchor design.
- [x] Hierarchy routes are mutually exclusive.
- [x] Resource economy and anchor lane exists.
- [x] Surface-war doctrine lane exists.
- [x] Stone Phalanx route exists or accepted equivalent.
- [x] Burrow War route exists or accepted equivalent.
- [x] Scree Tide route exists or accepted equivalent.
- [x] Doctrine routes are mutually exclusive.
- [x] Adaptation lane preserves hard-attack counterplay.
- [x] Continental expansion lane uses visible objectives.
- [x] World-end preparation lane is hidden until appropriate.
- [x] Focus rewards use decisions, templates, map effects, anchors, and mechanics rather than tiny modifiers.
- [x] Focus tree has route-specific AI.
- [x] Every focus has localisation and icon coverage.
- [x] Route coverage audit reports merges or deviations.
- [x] Decision categories use phases and selected targets to avoid clutter.

## World threat and world end

- [x] Cave threat registers a source in shared world-threat framework.
- [x] Threat source clears after full defeat.
- [x] Origin continent is stored.
- [x] Eligible continent state group excludes impassable and invalid microstates.
- [x] Continent progress is visible.
- [x] Cave country must own and control every eligible state.
- [x] Temporary control does not instantly trigger world end.
- [x] Verification period exists.
- [x] Chaos must be above 1000.
- [x] Existing world-end state blocks Event 018 terminal trigger.
- [x] Terminal effect sets shared world end and scenario flag.
- [x] Incompatible automatic event progression stops.
- [x] No new ordinary Event 018 fields appear after terminal state.
- [x] World-end super-event uses unique image and audio.
- [x] Cross-continent candidate states are valid and resource-weighted.
- [x] Footholds are geographically distributed.
- [x] Footholds create playable local fronts rather than deleting whole countries.
- [x] Cave country declares war on new foothold neighbors.
- [x] Terminal cave transformation is strong and route-aware.
- [x] World end fires once.

## Defeat and aftermath

- [x] Regional cave defeat can end without mandatory global aftermath.
- [x] Cave country removal cleans flags, targets, AI, and world-threat source.
- [x] Every liberated anchor has cleanup path.
- [x] Resource output restores or remains explicitly scarred according to design.
- [x] Original origin does not automatically restart Event 018.
- [x] Residual incidents end and do not force a secret restart.
- [x] Global defeat super-event fires only after global or near-global crisis.
- [x] Defeat audio and image are unique if super-event exists.
- [x] Reconstruction compact appears only when campaign impact justifies it.
- [x] Deaths, damaged states, and reconstruction are reflected.

## AI

- [x] Owner AI selects posture from need, strength, politics, and risk.
- [x] Owner AI uses safety and closure actions.
- [x] Owner AI does not always maximize extraction.
- [x] Foreign AI interest uses actual material need.
- [x] Claimant AI avoids impossible border wars.
- [x] Foreign aid AI responds to Evolution III and IV.
- [x] Ordinary-country AI prioritizes hard attack and anchor denial.
- [x] Cave AI targets rich reachable states.
- [x] Cave AI protects origin and anchors.
- [x] Cave AI responds to capacity loss.
- [x] Cave AI chooses hierarchy and doctrine from geography.
- [x] Cave AI can complete continent objective.
- [x] Invalid focuses and decisions weight to zero.

## Localisation and event-log presentation

- [x] Final text uses no em dash.
- [x] Final text uses no semicolon in sentences.
- [x] Final text avoids staccato dramatic fragments.
- [x] Final text avoids dialectical hedging and staged contrast formulas.
- [x] Baseline text does not spoil horror.
- [x] Evolution II uses concrete observed symptoms.
- [x] Evolution III explains public actions and requirements.
- [x] Cave text is original and readable, without comedy growling.
- [x] Event Details contains premise only, no effect list or hidden route.
- [x] Event name mapping exists in normal and debug selectors.
- [x] History rows record state, resource, owner, and enrichment status.
- [x] Evolution rows show correct actor, stage, tier, and enable state.
- [x] Evolution Details reflect all four stages.
- [x] Cluster details describe positive economic discovery without spoilers.
- [x] Integer values display without unwanted decimals.
- [x] Localisation files use UTF-8 with BOM.

## Assets and super-events

- [x] Every required report image has source, processed PNG, DDS, manifest, and GFX handoff.
- [x] Every required news image has source, black-and-white processed PNG, DDS, manifest, and GFX handoff.
- [x] Every super-event image is 457 by 328 and wired.
- [x] Fictional assets are generated through approved image workflow.
- [x] Icons are created separately by asset type.
- [x] Focus icons are not resized into idea or decision icons.
- [x] Cave leader portrait is generated, not sourced from a real person.
- [x] Flags use intentional original designs and correct TGA orientation.
- [x] Every animated asset has real source frames, sheet, static fallback, preview, manifest, and handoff.
- [x] Emergence super-event has unique final track and audio ID.
- [x] World-end super-event has unique final track and audio ID.
- [x] Defeat super-event has unique final track and audio ID if used.
- [x] Audio source, creator, license, duration, and final path are documented.
- [x] Final WAV files are 44.1 kHz.
- [x] Music HTML table lists every track and super-event ID.
- [x] No placeholder, default, generated tone, or undocumented audio remains.
- [x] Quotes and cultural remarks are researched and sourced.

## Achievements

- [x] Achievement set covers ordinary economic mastery.
- [x] Achievement set covers safe full closure.
- [x] Achievement set covers extreme exploitation.
- [x] Achievement set covers border or commission mastery.
- [x] Achievement set covers defeating the cave threat.
- [x] Achievement set covers cave-country capacity play.
- [x] Achievement set covers continent consumption and world end.
- [x] No achievement unlocks merely because the event fired.
- [x] Tracking flags and disqualifiers are implemented.
- [x] Every achievement has completed, grey, and not-eligible icons.
- [x] Achievement IDs, localisation, GFX, assets, docs, and registry agree.

## Documentation, spreadsheet, and audits

- [x] Canonical event doc is updated.
- [x] Cave-country package is documented.
- [x] Dynamic helpers are documented with scope, inputs, outputs, and side effects.
- [x] Asset manifest is complete.
- [x] Super-event research note is complete.
- [x] Music documentation is complete.
- [x] Event catalog workbook matches final in-game Event Details wording.
- [x] Evolution fields match final in-game evolution wording.
- [x] World-end field matches implemented terminal state.
- [x] Cluster and member-severity fields are blank.
- [x] No stale plan or handoff remains without disposition.
- [x] Focus auditor has reviewed the final tree.
- [x] Decision and mission auditor has reviewed the final categories.
- [x] Country package auditor has reviewed the cave tag.
- [x] Localisation auditor has reviewed all visible text and dynamic values.
- [x] Event completion auditor has compared implementation to this package.
- [x] Mandatory improvement-loop planner pass has returned an addendum or closure handoff.
- [x] Every accepted addendum is implemented, promoted, queued with reason, or rejected with reason.

## Meaningful validation proof, accepted static mode

The scenarios below are checked on the deterministic and static evidence recorded in `018_static_acceptance_report.md`. Live engine execution was explicitly waived, so these checks do not represent observed in-game runs.

- [x] Baseline safe-field scenario recorded.
- [x] Repeat enrichment and duplicate-roll scenario recorded.
- [x] Exact closure subtraction scenario recorded.
- [x] Concession ownership-transfer scenario recorded.
- [x] Border dispute and state-transfer scenario recorded.
- [x] Evolution II safety comparison recorded.
- [x] Evolution III successful full-seal scenario recorded.
- [x] Maximum 30-division breach scenario recorded.
- [x] Capacity table states from 0 through over 100 resources recorded.
- [x] Origin-state exclusion recorded.
- [x] Capacity-loss and Unfed Broods scenario recorded.
- [x] Cave AI multi-front campaign recorded.
- [x] World-end chaos and continent gate scenario recorded.
- [x] Cross-continent foothold validity scenario recorded.
- [x] Regional defeat cleanup scenario recorded.
- [x] Global defeat aftermath gating scenario recorded.
- [x] No simplification, fallback, missing AI, missing asset, or missing text remains undisclosed.
