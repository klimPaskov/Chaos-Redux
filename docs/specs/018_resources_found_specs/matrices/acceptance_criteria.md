# Event 018 Full Acceptance Criteria

This checklist defines completion. A checked item must be supported by implementation evidence, not a placeholder or future-work note.

## Source design and classification

- [ ] Event ID remains 18.
- [ ] Canonical entry uses the `chaosx.nr18.1` root.
- [ ] Event remains Minor Repeatable.
- [ ] Event belongs to Economy (pos).
- [ ] Cluster member severity is Medium.
- [ ] Event is enabled by default only after the rework is implementation-ready.
- [ ] Baseline works when all four evolutions are disabled.
- [ ] Baseline lifecycle stages are not logged as evolutions.
- [ ] Every final design change is represented in source specs or has an explicit plan disposition.

## Random discovery

- [ ] Owner selection excludes invalid actual nonhuman and terminal actors.
- [ ] State selection verifies owned and controlled valid state.
- [ ] Impassable and incompatible states are excluded.
- [ ] Standard resource selection is truly random among oil, aluminium, rubber, tungsten, steel, and chromium.
- [ ] Terrain affects presentation and state weighting, not final resource-type legality.
- [ ] Baseline deposit is centered around 100.
- [ ] Repeat firing can create a new field.
- [ ] Repeat firing can enrich an existing active field.
- [ ] Duplicate resource rolls stack in the same state.
- [ ] Different resource rolls create a multi-resource field.
- [ ] Repeat events use follow-up text rather than replaying the first-discovery tutorial.

## Field persistence and resource ledger

- [ ] Every active field has one stable field record.
- [ ] Field record contains state, discoverer, owner, controller, discovery date, discovery count, stage, posture, and status.
- [ ] Event-owned oil is stored separately.
- [ ] Event-owned aluminium is stored separately.
- [ ] Event-owned rubber is stored separately.
- [ ] Event-owned tungsten is stored separately.
- [ ] Event-owned steel is stored separately.
- [ ] Event-owned chromium is stored separately.
- [ ] Total Event 018 resource amount can be calculated safely.
- [ ] Distinct resource count can be calculated safely.
- [ ] Largest single-resource amount can be calculated safely.
- [ ] Field survives repeat discovery without duplicate initialization.
- [ ] Field survives temporary occupation.
- [ ] Field transfers safely with state ownership.
- [ ] Contracts and political rights are reviewed separately from physical state transfer.
- [ ] Annexation and country removal clean stale targets and selections.
- [ ] A state cannot hold duplicate active field records.

## Field UI and values

- [ ] Decision category opens for the owner.
- [ ] Compact scripted GUI header shows selected state.
- [ ] Header shows Event 018 resource composition.
- [ ] Header distinguishes Event 018 additions from total state resources.
- [ ] Developed Yield is visible as integer and band.
- [ ] Excavation Depth is visible as integer and band.
- [ ] Workforce Safety is visible as integer and band.
- [ ] Foreign Pressure is visible as integer and band.
- [ ] Subsurface Disturbance becomes visible only after its reveal.
- [ ] Breach Pressure becomes visible only in Evolution III.
- [ ] Each value has cause-and-effect tooltip direction.
- [ ] Selected-field cycle works for multiple fields.
- [ ] Lost or closed selected field advances to next valid field.
- [ ] Human field selection does not block AI evaluation of all fields.
- [ ] Static fallback exists for every animated UI state.

## Administration and baseline economy

- [ ] National resource authority posture exists.
- [ ] Domestic commercial charter posture exists.
- [ ] Foreign concession posture exists.
- [ ] International commission posture exists when unlocked.
- [ ] Strategic reserve or suspension posture exists.
- [ ] Posture changes require transition cost and time.
- [ ] Geological appraisal is an active project.
- [ ] Deeper testing can improve the field and raise depth.
- [ ] Primary works create a meaningful state or yield change.
- [ ] Transport project changes rail, infrastructure, supply, or route behavior.
- [ ] Heavy machinery changes yield and depth.
- [ ] Local processing creates a meaningful map or production effect.
- [ ] Worker settlement or administration can reduce labor strain.
- [ ] Safety actions materially reduce accident and later death risk.
- [ ] Stable mature-field identities exist.
- [ ] Field maintenance does not become a tray of tiny passive modifiers.

## Trade and diplomacy

- [ ] Foreign interest uses actual deficit, route, relations, war, proximity, rivalry, and field value.
- [ ] Only high-value foreign candidates receive active actions.
- [ ] Buyer, investor, strategic claimant, and crisis behavior are distinct.
- [ ] Owner can invite bids.
- [ ] Owner can sign a persistent export contract.
- [ ] Contract records buyer, term, access, and lifecycle.
- [ ] Route loss interrupts delivery.
- [ ] Occupation interrupts or changes delivery.
- [ ] Suspension pauses or breaches contract.
- [ ] Closure settles or terminates contract.
- [ ] Buyer disappearance cleans contract.
- [ ] Owner can reserve output for domestic use.
- [ ] Owner can balance competing buyers.
- [ ] Foreign investor can offer machinery and transport.
- [ ] Exclusive access creates rival pressure.
- [ ] Concession influence is visible and bounded.
- [ ] Nationalization requires preparation and creates compensation consequences.
- [ ] Fair compensation can settle dispute.
- [ ] Smuggling pressure has actual causes and state-route counterplay.
- [ ] Espionage and sabotage can be exposed.
- [ ] Diplomatic reaction strength reflects material stake.
- [ ] Event uses normal strategic resources and does not create a parallel trade currency.

## Commission and border conflict

- [ ] International commission can emerge from severe competition or mediation.
- [ ] Commission defines quotas, inspection, and troop restrictions.
- [ ] Demilitarization is negotiated rather than random.
- [ ] Field guards remain possible under demilitarization.
- [ ] Commission compliance can be maintained or violated.
- [ ] Commission dissolution cleans rules and targets.
- [ ] Border claimant requires a real claim or mapped dispute.
- [ ] Adjacency alone cannot create a claim.
- [ ] Border crisis requires high field importance and pressure.
- [ ] Competing survey stage exists.
- [ ] Customs or road confrontation stage exists.
- [ ] Armed patrol incident stage exists.
- [ ] Timed frontier mission uses named state, supply, or troop objectives.
- [ ] Border war uses a limited contest where designed.
- [ ] Owner victory has settlement.
- [ ] Claimant victory transfers state and field safely.
- [ ] Stalemate can create commission or ceasefire.
- [ ] State transfer preserves physical ledger and changes contracts.
- [ ] Border conflict cannot fire from impossible military conditions.

## Suspension and closure

- [ ] Suspension is reversible and distinct from closure.
- [ ] Suspension suppresses extraction and risk growth.
- [ ] Suspension retains field ledger and maintenance decisions.
- [ ] Baseline closure is a multi-step project.
- [ ] Closure scales with yield, depth, resource diversity, contracts, danger, and control.
- [ ] Closure settles workers and contracts.
- [ ] Closure removes every Event 018 resource addition.
- [ ] Closure removes no preexisting state resource.
- [ ] Closure cleans modifiers, decisions, targets, and UI.
- [ ] Permanently closed state is excluded from future Event 018 selection.
- [ ] Partial closure is visibly distinct and does not claim permanent prevention.

## Evolution I

- [ ] Evolution I has a pre-fire opening.
- [ ] Pre-fire opening adds 2 to 4 independent large rolls in one state.
- [ ] Duplicate rolls stack.
- [ ] Evolution I has an active-field entry.
- [ ] Active entry adds deposits and compound-field decisions.
- [ ] Multi-resource administration is playable.
- [ ] Integrated processing corridor is meaningful.
- [ ] Foreign Pressure sensitivity increases.
- [ ] Commission and DMZ routes can open.
- [ ] Evolution I has a stable non-supernatural ending.
- [ ] Evolution I logs through shared evolution system.

## Evolution II

- [ ] Evolution II has a stronger pre-fire opening.
- [ ] High-stage first firing still begins with discovery and gradual incidents.
- [ ] Worker sickness incidents use concrete ordinary explanations first.
- [ ] Corrosion and missing-worker incidents exist.
- [ ] Safety investment reduces deaths and slows danger.
- [ ] Subsurface Disturbance reveal has physical evidence.
- [ ] Disturbance is visible after reveal.
- [ ] Disturbance changes available actions and evolution timing.
- [ ] Creature incidents remain underground at first.
- [ ] Player can restrict workings.
- [ ] Player can conduct scientific or military survey.
- [ ] Player can conceal and militarize with consequences.
- [ ] Player can begin full closure.
- [ ] Worker and field deaths use shared Deaths system.
- [ ] Real state population is reduced safely.
- [ ] Evolution II can stabilize if Evolution III is disabled.
- [ ] Evolution II logs through shared evolution system.

## Evolution III

- [ ] Evolution III pre-fire opening creates a very large deposit of every standard resource.
- [ ] First firing at Evolution III preserves gradual Evolution II incidents.
- [ ] Public perimeter breach event exists.
- [ ] Breach Pressure becomes visible.
- [ ] Settlement attacks exist.
- [ ] Transport disruption exists.
- [ ] City intrusion can occur.
- [ ] Population flight or evacuation is represented without duplicating another event system.
- [ ] Monster hunts require supplied hard-attack capable forces.
- [ ] Hunt success and failure are distinct.
- [ ] Evacuation uses trains, trucks, routes, time, and receiving capacity.
- [ ] Continued extraction worsens visible crisis and exploitation score.
- [ ] Partial sealing delays but does not prevent Evolution IV.
- [ ] Full sealing requires suspension, evacuation or control, engineering, and surface containment.
- [ ] Successful full seal removes all Event 018 resources.
- [ ] Successful full seal permanently prevents Evolution IV for the field.
- [ ] Successful full seal has no secret supernatural punishment.
- [ ] Evolution III can remain containable if Evolution IV is disabled.
- [ ] Evolution III logs through shared evolution system.

## Evolution IV emergence

- [ ] Evolution IV cannot occur on the first discovery day.
- [ ] Final breach uses dynamic timing and a public-crisis minimum.
- [ ] Cave country uses one stable tag.
- [ ] Cave country is registered as special chaos and actual nonhuman.
- [ ] Cave country receives field state and capital safely.
- [ ] Former owner and controller receive correct aftermath.
- [ ] Existing cave-country case is handled.
- [ ] Origin field history is recorded.
- [ ] Starting army uses exploitation history.
- [ ] Starting army minimum is credible.
- [ ] Starting army never exceeds 30 divisions.
- [ ] High safety, evacuation, and sealing can reduce opening strength.
- [ ] Cave country declares war on all current land neighbors.
- [ ] Newly adjacent land neighbors are declared upon once.
- [ ] Emergence uses unique super-event image and audio.
- [ ] Evolution IV logs through shared evolution system.

## Cave-country package

- [ ] Public country name and adjective are original and map-readable.
- [ ] Ruling party and sub-ideology are original nonhuman identities.
- [ ] Leader is literally a cave monster.
- [ ] Leader has an original authored name or original nonhuman pool.
- [ ] No human regional name pool is used.
- [ ] Static leader portrait exists.
- [ ] Animated leader portrait package exists with real source frames.
- [ ] Base flags exist in normal, medium, and small sizes.
- [ ] Any world-end cosmetic identity has distinct flags.
- [ ] Starting ideas have lifecycle and counterplay.
- [ ] Base cave template is very slow and heavily armored.
- [ ] Hard attack and piercing are effective counters.
- [ ] Cave country has no normal manpower economy.
- [ ] Cave country has no normal equipment economy.
- [ ] Core brood training queue is disabled.
- [ ] Captured factories support cave systems rather than human weapons.
- [ ] Cave country has no ordinary trade.
- [ ] Cave country has no ordinary faction membership.
- [ ] Cave country has no routine navy or air force before world end.
- [ ] Country has enough supply to function at origin.
- [ ] Origin loss creates a severe but clean crisis.

## Captured-resource deployment

- [ ] Total strategic resources in captured state are summed correctly.
- [ ] Capacity uses floor of total divided by 10.
- [ ] State capacity is capped at 10.
- [ ] Origin state is excluded regardless of resource total.
- [ ] Capacity requires continuous control for activation period.
- [ ] Activation is visible and interruptible.
- [ ] New divisions spawn automatically and sequentially.
- [ ] Several state captures do not create an instant stack.
- [ ] Human player can see capacity and next spawn.
- [ ] AI can manage queue and targets.
- [ ] Destroyed division frees one capacity slot.
- [ ] Losing a state starts a grace period.
- [ ] Excess divisions weaken rather than vanish.
- [ ] Recapturing capacity can restore support.
- [ ] Liberating state removes anchor after cleanup.
- [ ] Ordinary resource output can be restored safely.

## Cave focus tree and decisions

- [ ] Opening survival lane exists.
- [ ] Origin stabilization exists.
- [ ] Brood hierarchy lane exists.
- [ ] One Maw route is implemented or an accepted equivalent preserves centralization design.
- [ ] Many Chambers route is implemented or an accepted equivalent preserves distributed design.
- [ ] Hoard the Veins route is implemented or an accepted equivalent preserves rich-anchor design.
- [ ] Hierarchy routes are mutually exclusive.
- [ ] Resource economy and anchor lane exists.
- [ ] Surface-war doctrine lane exists.
- [ ] Stone Phalanx route exists or accepted equivalent.
- [ ] Burrow War route exists or accepted equivalent.
- [ ] Scree Tide route exists or accepted equivalent.
- [ ] Doctrine routes are mutually exclusive.
- [ ] Adaptation lane preserves hard-attack counterplay.
- [ ] Continental expansion lane uses visible objectives.
- [ ] World-end preparation lane is hidden until appropriate.
- [ ] Focus rewards use decisions, templates, map effects, anchors, and mechanics rather than tiny modifiers.
- [ ] Focus tree has route-specific AI.
- [ ] Every focus has localisation and icon coverage.
- [ ] Route coverage audit reports merges or deviations.
- [ ] Decision categories use phases and selected targets to avoid clutter.

## World threat and world end

- [ ] Cave threat registers a source in shared world-threat framework.
- [ ] Threat source clears after full defeat.
- [ ] Origin continent is stored.
- [ ] Eligible continent state group excludes impassable and invalid microstates.
- [ ] Continent progress is visible.
- [ ] Cave country must own and control every eligible state.
- [ ] Temporary control does not instantly trigger world end.
- [ ] Verification period exists.
- [ ] Chaos must be above 1000.
- [ ] Existing world-end state blocks Event 018 terminal trigger.
- [ ] Terminal effect sets shared world end and scenario flag.
- [ ] Incompatible automatic event progression stops.
- [ ] No new ordinary Event 018 fields appear after terminal state.
- [ ] World-end super-event uses unique image and audio.
- [ ] Cross-continent candidate states are valid and resource-weighted.
- [ ] Footholds are geographically distributed.
- [ ] Footholds create playable local fronts rather than deleting whole countries.
- [ ] Cave country declares war on new foothold neighbors.
- [ ] Terminal cave transformation is strong and route-aware.
- [ ] World end fires once.

## Defeat and aftermath

- [ ] Regional cave defeat can end without mandatory global aftermath.
- [ ] Cave country removal cleans flags, targets, AI, and world-threat source.
- [ ] Every liberated anchor has cleanup path.
- [ ] Resource output restores or remains explicitly scarred according to design.
- [ ] Original origin does not automatically restart Event 018.
- [ ] Residual incidents end and do not force a secret restart.
- [ ] Global defeat super-event fires only after global or near-global crisis.
- [ ] Defeat audio and image are unique if super-event exists.
- [ ] Reconstruction compact appears only when campaign impact justifies it.
- [ ] Deaths, damaged states, and reconstruction are reflected.

## AI

- [ ] Owner AI selects posture from need, strength, politics, and risk.
- [ ] Owner AI uses safety and closure actions.
- [ ] Owner AI does not always maximize extraction.
- [ ] Foreign AI interest uses actual material need.
- [ ] Claimant AI avoids impossible border wars.
- [ ] Foreign aid AI responds to Evolution III and IV.
- [ ] Ordinary-country AI prioritizes hard attack and anchor denial.
- [ ] Cave AI targets rich reachable states.
- [ ] Cave AI protects origin and anchors.
- [ ] Cave AI responds to capacity loss.
- [ ] Cave AI chooses hierarchy and doctrine from geography.
- [ ] Cave AI can complete continent objective.
- [ ] Invalid focuses and decisions weight to zero.

## Localisation and event-log presentation

- [ ] Final text uses no em dash.
- [ ] Final text uses no semicolon in sentences.
- [ ] Final text avoids staccato dramatic fragments.
- [ ] Final text avoids dialectical hedging and staged contrast formulas.
- [ ] Baseline text does not spoil horror.
- [ ] Evolution II uses concrete observed symptoms.
- [ ] Evolution III explains public actions and requirements.
- [ ] Cave text is original and readable, without comedy growling.
- [ ] Event Details contains premise only, no effect list or hidden route.
- [ ] Event name mapping exists in normal and debug selectors.
- [ ] History rows record state, resource, owner, and enrichment status.
- [ ] Evolution rows show correct actor, stage, tier, and enable state.
- [ ] Evolution Details reflect all four stages.
- [ ] Cluster details describe positive economic discovery without spoilers.
- [ ] Integer values display without unwanted decimals.
- [ ] Localisation files use UTF-8 with BOM.

## Assets and super-events

- [ ] Every required report image has source, processed PNG, DDS, manifest, and GFX handoff.
- [ ] Every required news image has source, black-and-white processed PNG, DDS, manifest, and GFX handoff.
- [ ] Every super-event image is 457 by 328 and wired.
- [ ] Fictional assets are generated through approved image workflow.
- [ ] Icons are created separately by asset type.
- [ ] Focus icons are not resized into idea or decision icons.
- [ ] Cave leader portrait is generated, not sourced from a real person.
- [ ] Flags use intentional original designs and correct TGA orientation.
- [ ] Every animated asset has real source frames, sheet, static fallback, preview, manifest, and handoff.
- [ ] Emergence super-event has unique final track and audio ID.
- [ ] World-end super-event has unique final track and audio ID.
- [ ] Defeat super-event has unique final track and audio ID if used.
- [ ] Audio source, creator, license, duration, and final path are documented.
- [ ] Final OGG files are 44.1 kHz.
- [ ] Music HTML table lists every track and super-event ID.
- [ ] No placeholder, default, generated tone, or undocumented audio remains.
- [ ] Quotes and cultural remarks are researched and sourced.

## Achievements

- [ ] Achievement set covers ordinary economic mastery.
- [ ] Achievement set covers safe full closure.
- [ ] Achievement set covers extreme exploitation.
- [ ] Achievement set covers border or commission mastery.
- [ ] Achievement set covers defeating the cave threat.
- [ ] Achievement set covers cave-country capacity play.
- [ ] Achievement set covers continent consumption and world end.
- [ ] No achievement unlocks merely because the event fired.
- [ ] Tracking flags and disqualifiers are implemented.
- [ ] Every achievement has completed, grey, and not-eligible icons.
- [ ] Achievement IDs, localisation, GFX, assets, docs, and registry agree.

## Documentation, spreadsheet, and audits

- [ ] Canonical event doc is updated.
- [ ] Cave-country package is documented.
- [ ] Dynamic helpers are documented with scope, inputs, outputs, and side effects.
- [ ] Asset manifest is complete.
- [ ] Super-event research note is complete.
- [ ] Music documentation is complete.
- [ ] Event catalog workbook matches final in-game Event Details wording.
- [ ] Evolution fields match final in-game evolution wording.
- [ ] World-end field matches implemented terminal state.
- [ ] Cluster field shows Economy (pos) and Medium severity.
- [ ] No stale plan or handoff remains without disposition.
- [ ] Focus auditor has reviewed the final tree.
- [ ] Decision and mission auditor has reviewed the final categories.
- [ ] Country package auditor has reviewed the cave tag.
- [ ] Localisation auditor has reviewed all visible text and dynamic values.
- [ ] Event completion auditor has compared implementation to this package.
- [ ] Mandatory improvement-loop planner pass has returned an addendum or closure handoff.
- [ ] Every accepted addendum is implemented, promoted, queued with reason, or rejected with reason.

## Meaningful validation proof

- [ ] Baseline safe-field scenario recorded.
- [ ] Repeat enrichment and duplicate-roll scenario recorded.
- [ ] Exact closure subtraction scenario recorded.
- [ ] Concession ownership-transfer scenario recorded.
- [ ] Border dispute and state-transfer scenario recorded.
- [ ] Evolution II safety comparison recorded.
- [ ] Evolution III successful full-seal scenario recorded.
- [ ] Maximum 30-division breach scenario recorded.
- [ ] Capacity table states from 0 through over 100 resources recorded.
- [ ] Origin-state exclusion recorded.
- [ ] Capacity-loss and Unfed Broods scenario recorded.
- [ ] Cave AI multi-front campaign recorded.
- [ ] World-end chaos and continent gate scenario recorded.
- [ ] Cross-continent foothold validity scenario recorded.
- [ ] Regional defeat cleanup scenario recorded.
- [ ] Global defeat aftermath gating scenario recorded.
- [ ] No simplification, fallback, missing AI, missing asset, or missing text remains undisclosed.
