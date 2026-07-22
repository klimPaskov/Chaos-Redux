# Fallout NZL Lifeboat State pilot depth review

Date: 2026-07-22

Status: accepted bounded closure addendum. The sea-road correction and Fallout-owned country-memory correction are promoted into the pilot specification, implemented, and passed the final focused audit in `subagent_handoffs/2026-07-22_fallout_nzl_sea_road_event_log_completion_audit.md`. No broad expansion is recommended.

## Review boundary

This planning pass reviewed the accepted New Zealand Lifeboat State pilot specification, asset brief, achievement handoff, engine proof, current dormant implementation, and all nine NZL package audits and handoffs. It also checked the existing Fallout Event Log framework and the source ownership and allocation ledgers.

This is a planning document only. It changes no gameplay, localisation, assets, manifests, specifications, spreadsheets, or skills. Hearts of Iron IV was not launched. The installed package has no Technology Tree Viewer, so no technology-tree visualization or technology-write path was available. No technology change is proposed.

There is no earlier unresolved improvement-loop addendum for this pilot. The completion audit explicitly found none. This file is the first and should be the last broad depth review unless its required corrections are implemented, promoted, queued with a reason, or rejected with a reason.

## Outcome

The pilot should stop expanding after two bounded corrections:

1. Make `fallout_nzl_license_every_sea_road` produce a real recurring convoy operating tradeoff through existing decisions and chain scoring.
2. Give the four NZL country-memory chains a Fallout-owned history and detail surface without assigning them to a normal Chaos event id, Zombie Event 2, the 660 living-world ledger, or the absent SCN-014 row.

The current architecture should otherwise remain fixed at 42 focuses, 18 decisions and missions, 14 ideas, 26 event blocks, four visible values, three cosmetic identities, three starting formations, one optional escort formation, and three achievements.

Additional focuses, decisions, ideas, popup events, country packages, formables, factions, super-events, animated headers, or spawned forces would add volume more than play. The existing implementation already has distinct routes, delayed results, visible resource pressure, exact bilateral targets, military failure states, a Year 10 conclusion, AI plans, bounded units, and durable campaign memory.

## Evidence for closure

| Surface | Current depth | Review disposition |
| --- | --- | --- |
| Four visible values | Harbor capacity, Food security, Parliament trust, and Sea-lane security are initialized, clamped, displayed, spent, recovered, and used by decisions, chain scores, route gates, Year 10, and achievements. | Keep. Do not add a fifth value or a separate scripted GUI. |
| Routes and pressure | Humanitarian play spends harbor, food, convoys, and political capacity to build exact relief partnerships. Isolation spends trust, command capacity, convoys, and naval experience to police exact sea lanes and, only when proven, an exact aggressor. | Keep. Close the sea-road operating-cost mismatch inside this loop. |
| Failure states | Failed major missions set a durable failure receipt. The event chains have success, partial, and failure bands. Pirate defeat is distinct from settlement. Foreign basing and last-berth closure carry permanent achievement consequences. | Keep. Do not add a generic collapse meter or random disaster layer. |
| Diplomacy | The external chain selects one deterministic valid coastal successor, records the exact partner, supports a second humanitarian partner, records rejection, and never invents a substitute pirate target. | Keep. Do not add annexation claims, a formable, or an automatic faction. |
| Year 10 | A 3,650-day timed receipt, route completion, and all four stable values gate a final three-choice delayed result. The outcome records a persistent late identity. | Keep. Expose its memory in Fallout details rather than add a second finale. |
| Forces | The package is additive to vanilla NZL and contributes three weak two-battalion formations, state-targeted Home Guard defenses, bounded port fortification, and one paid escort formation. | Keep. More free units or a free navy would weaken the convoy economy and duplication proof. |
| AI | Both routes have package-gated plans, focus order, research preferences, advisor priorities, and action weights. Human and AI events share costs, scores, and results. | Keep. Add only sea-road reserve behavior. Vanilla NZL plan retirement remains a separate engine blocker. |
| Event memory | Opening memory feeds domestic scoring, domestic memory feeds external scoring, and external memory feeds Year 10. Each chain writes generation-bound result receipts and closes stale callbacks. | Keep. Present this memory in the Event Log. Do not add more event blocks to restate it. |
| Visual layer | Four report images, three flag families, 24 focus icons, 14 idea icons, 18 action icons, one category icon, and nine achievement states exist. Static value presentation is appropriate. | Keep. The failed radio dossier card remains a frozen blocker, not an invitation to use a fallback. |

## Required spec corrections

### 1. Complete the licensed sea-road operating loop

#### Design problem

The accepted focus promises numbered permits, patrol windows, reduced piracy exposure, and higher convoy operating cost. The current focus grants 7 Sea-lane security, removes 4 Harbor capacity, and opens Last-Berth Closure. This is a one-time value exchange. It does not create a permit, a patrol window, or an operating cost.

The correction should reuse `fallout_nzl_fishery_quota_compact` and `fallout_nzl_quiet_seas_patrol`. It must not add a nineteenth decision or a fifteenth idea.

#### State contract

Add one permanent flag, one generation receipt, one timed flag, and one counter:

- `fallout_nzl_sea_road_licensing_active` records completion of the focus in the current package.
- `fallout_nzl_sea_road_license_generation` equals the current Fallout transition generation.
- `fallout_nzl_sea_road_patrol_window_current` is a 90-day timed country flag.
- `fallout_nzl_sea_road_license_serial` counts issued operating windows for current-generation memory and details display.

Use a reusable `fallout_nzl_issue_sea_road_patrol_window` effect and a fail-closed `fallout_nzl_sea_road_patrol_window_is_current` trigger. The effect should increment the serial, stamp the current generation, and refresh the 90-day timed flag. Reset and package cleanup must clear all four records. The timed flag duration should use `constant:fallout_nzl_duration.cooldown` through a temporary or normal variable if the duration field rejects a constant token.

Do not add a recurring on-action. The current timed flag and existing player actions are enough.

#### Focus correction

`fallout_nzl_license_every_sea_road` should:

- set the active licensing flag and current generation receipt
- open `fallout_nzl_fishery_quota_compact` even if the shared economy focus has not yet done so
- retain the immediate 7-point Sea-lane security gain as the benefit from mapped approaches and a public register
- remove the current 4-point Harbor capacity loss, since the recurring convoy cost becomes the real tradeoff
- keep opening Last-Berth Closure

The focus itself should not remove convoys. A focus completion effect has no safe affordability transaction, while the decisions already expose costs and availability before the player commits.

#### Existing decision changes

| Existing action | Without licensing | With current-generation licensing |
| --- | --- | --- |
| Fishery Quota Compact | Preserve the current 25 Political Power, 350 manpower, 7 Food security gain, and 4 Sea-lane security loss. | Require and consume 5 convoys in addition to the existing costs. Issue or renew the 90-day patrol window. Grant 7 Food security and 4 Sea-lane security instead of reducing security. |
| Quiet-Seas Patrol | It cannot normally appear before the isolation route and licensing focus. Preserve a fail-closed non-licensed branch for stale-state safety. | Require and consume 10 convoys instead of 5, retain the 12 Navy Experience cost, issue or renew the patrol window, and grant 12 Sea-lane security instead of 7. |

The 5 and 10 convoy values already exist as `fallout_nzl_cost.convoy_low` and `fallout_nzl_cost.convoy_medium`. No new numeric cost is needed.

The fishery action becomes the peacetime operating cycle. Fishing crews carry permit numbers and patrol reports while the state pays convoy hulls to keep the licensed approaches covered. Quiet-Seas Patrol is the wartime surge. This makes the same law materially different in peace and war without adding another decision family.

#### Route pressure and event consequences

Only the external and Year 10 score calculations should read the patrol window:

- add a 4-point score adjustment when the isolation route has a current licensed patrol window
- subtract 4 points when the isolation route has active licensing but no current window
- do not change humanitarian scoring
- do not block Year 10 outright when the window lapses

Put these values in the shared NZL score constants. Apply them directly in `fallout_nzl_calculate_external_result` and `fallout_nzl_calculate_late_result`, or pass an explicit chain phase into a helper. Do not make the shared opening or domestic score read a route state that does not yet exist.

This gives a lapsed operating cycle a real but recoverable consequence. The player can still reach Year 10, but a neglected cordon makes the final result harder. No passive value drain and no world iteration are needed.

#### AI behavior

The isolation AI should treat an absent patrol window as a high-priority reason to take Fishery Quota Compact when it can pay the licensed cost and retain at least one `convoy_low` reserve after payment. It should not spend its last five convoys to renew a quiet peacetime window.

Quiet-Seas Patrol should retain high priority during the exact pirate war, but its AI affordability must use the licensed 10-convoy cost. If the AI lacks that reserve, it waits rather than receiving a cheaper hidden path.

Humanitarian AI behavior and the non-licensed Fishery Quota Compact behavior remain unchanged.

#### Player-facing direction

Do not write final localisation from this plan. Implementation wording should make three facts explicit:

- a licensed fishery cycle spends convoy hulls and protects the approaches
- the window lasts 90 days
- the wartime patrol costs more convoys and produces a larger security return

Conditional custom cost text must reflect the actual constants. The current literal cost wording already has a documented drift risk, so the implementer should not add another untracked literal if a scripted display helper can read the tuned value.

#### Acceptance criteria

- Focus count remains 42.
- Decision and mission count remains 18.
- Idea count remains 14.
- Completing the focus creates no free convoy loss and no new recurring poll.
- Non-licensed Fishery Quota Compact preserves its current outcome.
- Licensed Fishery Quota Compact cannot start without 5 convoys and consumes exactly 5.
- Licensed Quiet-Seas Patrol cannot start without 10 convoys and consumes exactly 10.
- Both licensed actions refresh one generation-bound 90-day window.
- External and Year 10 scores distinguish a maintained window from a lapsed one by equal and opposite 4-point adjustments.
- Reset and package invalidation remove active licensing state without leaving a current-generation window.
- Human and AI costs are identical.

### 2. Add Fallout-owned country-memory history and details

#### Ownership problem

The 26 NZL blocks are country-memory events inside the Fallout namespace. They are not a normal Chaos event, not an evolution, not a super-event, not a manual scenario, and not part of the 660 ordinary Fallout living-world release floor.

Do not solve the missing presentation by attaching these blocks to Zombie Event 2, allocating a normal Event id, counting `.127` through `.152` toward 660, or creating SCN-014. Event 2 remains Zombie-only. SCN-014 remains absent until the exact manual province sweep is proven.

#### Shared Fallout memory ledger

Add a small reusable Fallout country-memory ledger rather than an NZL-only normal event row. A committed record needs parallel fields for:

- Fallout transition generation
- country memory id
- chain type
- result band
- selected policy token
- completion date from `global.date`
- primary actor and actor-present marker
- optional secondary actor and actor-present marker
- route token
- Harbor capacity snapshot
- Food security snapshot
- Parliament trust snapshot
- Sea-lane security snapshot

The NZL country memory id is `constant:fallout_country_memory.new_zealand_lifeboat_state`. The four chain types are opening, domestic, external, and Year 10. External records may repeat because the humanitarian route can contact more than one partner. Opening, domestic, and Year 10 should commit at most once per transition generation.

Use the same actor storage and sanitizing pattern as the existing Event Log history arrays. NZL is always the primary actor. The exact external partner is the secondary actor when one exists. A no-partner result records no secondary actor. Committed history should survive later package cleanup. Pending UI selection state may be cleared.

#### Commit points

| Chain | Commit point | Record content |
| --- | --- | --- |
| Opening `.127` to `.132` | First successful application in `fallout_nzl_apply_opening_result` | choice, result, date, NZL actor, four values after application |
| Domestic `.133` to `.138` | First successful application in `fallout_nzl_apply_domestic_result` | choice, result, prior opening result, date, NZL actor, four values after application |
| External `.139` to `.146` | The valid terminal path in `fallout_nzl_close_external_chain` before transaction cleanup | choice, result, route, exact partner or no-partner state, date, NZL actor, optional partner, four values after any basing choice |
| Year 10 `.147` to `.152` | `fallout_nzl_record_year_ten_order` | choice, result, route, date, NZL actor, four final values |

The external commit needs a current package, current chain, current result receipt, and an external-memory deduplication receipt. A stale resolver may still call the close helper for cleanup, but it must not commit history. Recording at the valid close point preserves the optional human or AI basing concession and its final value changes.

Do not log human roots, hidden AI roots, delayed resolvers, visible acknowledgements, and cleanup blocks separately. One result record per resolved transaction is enough and prevents a 26-line implementation detail from becoming player-visible noise.

#### Event Log surface

Add a Fallout country-memory subsection inside the existing Event Log popup. It should be reachable from the Fallout world-end detail surface and should not appear in the ordinary Events list.

The subsection should show one compact row per committed memory, newest first. A row needs:

- chain title direction based on the existing visible event family, such as Names at the Harbour Door, The Milk Powder Rooms, A Voice Beyond the Weather Band, or Ten Years of Harbour Books
- result band
- completion date
- NZL flag and country name
- partner flag and name for an external record when present

Selecting a row should open its snapshot. The detail should explain the recorded choice, the result, the four value readings, the route in force, and the partner outcome. It must use the stored record, not current variables, so later decisions do not rewrite history.

Map these titles through Fallout country-memory keys. Do not add a normal event-name mapping in `chaosx_event_names_l_english.yml`, since no ordinary event id is being created.

#### Event Details surface

The Fallout details view should include one New Zealand Lifeboat State package card only after a current or historical NZL memory record exists. The card should summarize:

- the lifeboat promise and exact five-state identity
- the four values and their strategic meaning
- humanitarian and isolation route consequences
- the four chain records with dates and outcomes
- current or final route identity
- exact relief partners or exact pirate aggressor when their generation receipts remain valid
- Year 10 status and late result

This is an outcome-detail surface, not an evolution-detail surface. Do not create fake evolution tiers for opening, domestic, external, or Year 10.

The card may reuse the four existing report image families if the Event Log row template supports them. No new report art is required. Static presentation remains preferred.

#### Spreadsheet boundary

Do not add Fallout text to Event 2. Do not add a normal Fallout Events row. Do not add SCN-014 during this correction.

The workbook remains unchanged while SCN-014 is absent. When the broader Fallout scenario passes its exact sweep proof and receives a live scenario row, the NZL package detail should be represented as a child package section of that Fallout scenario, or through a dedicated future Fallout-package catalog schema approved by the parent. It must never be represented as Zombie content.

This means Event Log code can be completed while the spreadsheet activation gate remains blocked by the broader Fallout scenario proof.

#### Acceptance criteria

- Resolving the opening chain writes exactly one opening record in the current generation.
- Resolving the domestic chain writes exactly one domestic record and preserves the opening record.
- Each resolved external transaction writes one record with NZL as primary actor and the exact partner as secondary actor when present.
- The no-partner external route writes a valid record without a fabricated partner.
- Resolving Year 10 writes exactly one final record with all four value snapshots.
- Stale delayed callbacks and package reset cannot duplicate a committed record.
- Records display from stored snapshots even after values, route state, or diplomacy change.
- No NZL chain appears in the ordinary Events list or normal event-weight system.
- Event 2 remains Zombie-only.
- The 26 blocks remain uncounted outside the 660 living-world ledger.
- SCN-014 remains absent.
- No new evolution row, super-event, audio package, or report image is created.

### 3. Correct accepted spec identifiers when promoting this addendum

The accepted spec uses two working script ids that do not match the implemented focus ids:

- `fallout_nzl_port_militia_training_mission` should refer to focus `fallout_nzl_port_militia_drill`. The decision remains `fallout_nzl_port_militia_training_mission`.
- `fallout_nzl_arm_rescue_cutters_action` should refer to focus `fallout_nzl_armed_rescue_cutters`. The decision remains `fallout_nzl_arm_rescue_cutters_action`.

This is documentation reconciliation only. Do not rename the working implementation to match the stale spec labels.

## Optional future depth

No optional gameplay expansion is recommended before activation.

The following ideas were considered and rejected as bloat:

- More event blocks. Thirteen human-visible events across four delayed chains already cover opening law, domestic food politics, foreign contact, and Year 10. The missing value is recall, which the Event Log correction supplies.
- A third route. Humanitarian and isolation already create opposed admission, diplomacy, war, trust, and achievement play. A neutral trade route would dilute both.
- A Pacific formable or automatic faction. Exact bilateral relief and non-annexation are core to the promise. Territorial aggrandizement would reverse it.
- More units or a free fleet. Vanilla NZL remains additive, while the package already has three weak formations, one paid escort, Home Guard mobilization, port defenses, and convoy conversion.
- A fifth visible value. Weather, radio, morale, and legitimacy already feed Harbor capacity, Parliament trust, and Sea-lane security.
- A second Year 10 event family. The current final chain has three choices, deterministic memory, route pressure, and result bands. The detail surface should make that history legible.
- A scripted standalone GUI or animated header. Four slowly changing values remain clearer in the static decision-category header.
- A super-event. The pilot is a country package within a world-end system. It does not need a second world-scale interruption, quote, reaction set, or audio wrapper.
- More generated art. The current visual family is complete except for the frozen Radio Service Coordinator blocker. That blocker cannot be bypassed with a generic portrait, silhouette, emblem, recolor, or relaxed threshold.

After the two required corrections are implemented, further improvement-loop expansion should stop unless live play produces a specific, evidenced shallow point. Mere availability of more historical material is not enough reason to add mechanics.

## Historical and regional basis

The remaining correction is grounded in documented New Zealand institutions and geography:

- New Zealand's wartime coastal, trans-Tasman, and South Pacific shipping was a vital short-sea network. Government and naval control shaped routes, cargoes, and convoy practice. This supports a licensed-route system whose benefit depends on paying for real hulls, not a free abstract modifier. Source: [Under the Southern Cross](https://nzhistory.govt.nz/war/the-merchant-navy/under-the-southern-cross) and [The longest lifeline](https://nzhistory.govt.nz/war/the-merchant-navy/the-longest-lifeline), Manatu Taonga.
- The New Zealand government issued emergency regulations to control shipping in local waters in September 1939, while convoy practice and commerce-raider risk shaped wartime sailing. This supports registers, numbered windows, and bounded patrols as historical inspiration. It does not make the fictional Fallout pirate system a historical claim. Source: [Merchant Navy timeline](https://nzhistory.govt.nz/war/the-merchant-navy/timeline), Manatu Taonga.
- New Zealand maritime radio links coastal stations, weather and navigation warnings, distress traffic, and South Pacific coverage. This supports the existing radio, weather, partner, and patrol connections. It does not justify another radio minigame. Source: [The Maritime Radio Service for New Zealand](https://www.maritimenz.govt.nz/readiness-and-response/beacons-and-communications/maritime-radio-service-for-new-zealand/), Maritime New Zealand.
- Dairy production and export depended on cooperative organization, central marketing, refrigeration, and shipping. Wartime government purchase and direction give the Dairy Relief Board, milk rail, and licensed fishery transactions a regional institutional basis. Source: [Dairy exports](https://teara.govt.nz/en/dairying-and-dairy-products/page-11), Te Ara.
- New Zealand naval defense used local patrols, minesweeping, signals, merchant conversions, reservists, and coastal vessels. This supports paid rescue cutters and bounded patrol forces. It argues against spawning a large free navy. Source: [Second World War, Royal New Zealand Navy](https://nzhistory.govt.nz/war/royal-new-zealand-navy/second-world-war), Manatu Taonga.
- Pacific search and rescue requires cooperation across dispersed island states, including Samoa, but this is inspiration for exact bilateral relief only. It does not resolve ownership of state 726 or the Aotearoa overlap. Source: [Search and rescue in the Pacific](https://www.maritimenz.govt.nz/readiness-and-response/maritime-incident-readiness-and-response-mirr/rescue-coordination-centre-rccnz/search-and-rescue-in-the-pacific/), Maritime New Zealand.

The accepted symbol research remains authoritative for the Southern Cross, maritime ensign, silver fern, rescue-service language, protected emblems, and Maori cultural caution. No new symbol family is required by this addendum.

## Implementation surfaces affected

The parent implementer should expect the required corrections to touch only these surface families:

- NZL focus reward, decision costs and results, reset cleanup, score constants, score helpers, AI decision weights, conditional cost display, and their docs
- Fallout country-memory record helpers and storage
- Event Log effects, scripted GUI hooks, scripted localisation, popup layout only if the existing world-end detail container cannot host the rows, and direction-only player text
- the accepted NZL spec after design acceptance
- the engine proof and completion records after implementation evidence exists

No change is proposed to event suffix allocation, package territory, cosmetic tags, characters, achievements, idea count, focus layout, action count, starting forces, super-events, scenario registry, or the 660 ledger.

## Blockers outside this design correction

This addendum does not close or redesign these release blockers:

1. The Radio Service Coordinator version 10 source failed the frozen paper-mean and bottom-variation gates across 96 candidates. Keep the failed gate unchanged. No fallback and no threshold relaxation are permitted.
2. Samoa state 726 remains excluded and needs a compatible Independence Wave disposition receipt.
3. The Aotearoa overlap on states 284 and 723, including the GRX conflict surface, needs an explicit current-generation disposition.
4. The live allocator still needs exact assignment, capital, player-continuation, materialisation, and map-return receipts. Do not add the activation caller early.
5. Vanilla NZL AI plans still need an engine-safe additive retirement proof. Do not replace or weaken pre-Fallout vanilla definitions speculatively.
6. Runtime event-target retention, generated-character promotion, multiplayer authority, exact province sweep, and map return remain unproven.
7. SCN-014 remains absent until the exact manual province sweep passes.

## Meaningful validation scenarios for the parent

After implementation, validate at least these source and runtime cases before changing package status:

1. Isolation peace case. Complete sea-road licensing, take the licensed fishery action, confirm the extra 5 convoys are consumed, confirm the 90-day window, and confirm Food and Sea-lane security rise by the designed amounts.
2. Isolation lapse case. Let the patrol window expire before an external or Year 10 score, then prove the exact 4-point penalty and no passive daily or monthly loss.
3. Isolation war case. Start the exact pirate war, run Quiet-Seas Patrol, confirm the 10-convoy and 12 Navy Experience costs, the 12-point security gain, and the refreshed window.
4. Humanitarian regression case. Confirm the original Fishery Quota Compact cost and security tradeoff remain unchanged without sea-road licensing.
5. AI reserve case. Give isolation AI 5 convoys, then 10 or more. It must preserve the last reserve in the first case and operate the licensed cycle in the second when other gates pass.
6. Four-chain memory case. Resolve opening, domestic, one partnered external transaction, one no-partner or second-partner transaction in a separate run, and Year 10. Confirm exact dates, result bands, actor records, partner records, and four value snapshots.
7. Stale callback case. Invalidate the package before a delayed resolver returns. It must clean up without committing or duplicating an Event Log memory.
8. Ownership case. Confirm Event 2 still displays only Zombie material, the ordinary Events list contains no NZL Fallout row, the 660 count remains unchanged, and SCN-014 remains absent.
9. Dormancy case. With no activation caller and no current package receipt, no NZL package card, decision, focus tree, event, or unresolved radio portrait can become player-visible.

## Promotion and closure handoff

The parent accepted both required corrections on 2026-07-22. The sea-road contract, decision transactions, score pressure, AI reserve rule, country-memory presentation contract, and two corrected focus identifiers were merged into the pilot specification. The sea-road code, country-memory History rows, exact Event Details, partner presentation, and generation-isolated package card are implemented. The final focused audit found no unresolved correction regression. The older completion and status-reconciliation handoffs remain dated pre-correction history and are superseded for these two surfaces.

The rejected optional expansion ideas are not future promises. The engine proof must change only after the corresponding code and focused audit evidence exist.

The two required corrections are implemented, so this broad improvement-loop pass is closed. The parent should finish the independent radio, allocator, conflict, vanilla AI retirement, and runtime proof blockers, preserve the Zombie-only spreadsheet ownership, and keep the package dormant until every release gate passes.

Parent handoff:

- Closed correction: Fishery Quota Compact and Quiet-Seas Patrol operate generation-bound 90-day licensed windows, and all four chain outcomes use a dedicated Fallout country-memory ledger inside the Event Log.
- Research basis: wartime short-sea control, maritime radio and weather coverage, dairy cooperative logistics, local naval defense, and Pacific rescue coordination.
- Architecture preserved: 42 focuses, 18 decisions and missions, 14 ideas, 26 event blocks, four values, three starting formations, one optional escort, three achievements, no super-event.
- Resolved fit: the existing world-end detail surface hosts a generation-isolated package card, while shared History and Event Details host the exact chain rows.
- Prior addendum status: none existed. This addendum is promoted and implemented.
- Closure decision: stop broad pilot expansion unless later evidence identifies a specific defect.
