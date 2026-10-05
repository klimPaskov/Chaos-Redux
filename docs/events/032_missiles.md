# Event 032 — Missiles

Event 032 is the bounded worldwide missile-program event owned by `chaosx.nr32`. It is a Minor Repeatable event with ID `32`, Calm World minimum chaos, no cluster membership, and entry event `chaosx.nr32.1`.

## Runtime contract

The shared event dispatcher calls `missiles_prepare_random_event_fire` during Event 32 preflight and then opens the hidden entry event. The entry event's immediate effect is the only global firing transaction.

`missiles_global_firing_transaction` increments one firing receipt, clears and freezes `global.missiles_frozen_recipients`, classifies every country once as accepted, deferred, or skipped, and processes only the frozen accepted array. Recipient receipt IDs make a country idempotent within the firing. The transaction stores the accepted count in the shared history-payload override so the shared repeatable handler records one Event 32 history row after the entry event returns.

Each frozen recipient receives the immediate hidden event `chaosx.nr32.5`, which binds `ROOT` to that recipient for its country and launch-state helpers. The receipt gate covers programme setup, evolution adoption, rogue-incident evaluation, and pressure accounting together. These receivers finish within the global transaction and do not create history rows or player popups.

First-package recipients call the existing Event 16 reaction helper in their own country scope. Event 16 owns the host and personal receipts, so an earlier non-host recipient cannot suppress the current host's reaction.

The same transaction owns the first-news guard and emits `chaosx.nr32.3` only once. Human recipients receive one delayed country report through `chaosx.nr32.2`; AI recipients are initialized silently. No Event 32 daily, weekly, monthly, or other recurring whole-world scan exists.

Event 32 is in the shared default-enable allowlist (`event_log_event_is_reworked_default_enabled`). The repeatable event array, shared event-type resolver, cap reduction, weight recovery, pacing update, unfired counts, and history row remain owned by the shared event system.

## Country-program API

The following country-scoped effects form the public Event 032 program contract.

| API | Inputs | Outputs and side effects |
| --- | --- | --- |
| `missiles_initialize_program_record` | Current country | Initializes missing persistent records and achievement state without granting a package. |
| `missiles_process_frozen_recipient` | Immediate `.5` receiver with recipient `ROOT` and a live frozen-firing receipt | Applies one complete recipient transaction, including adoption and pressure accounting, once per firing. |
| `missiles_initialize_or_advance_program` | Current country and optional `missiles_scenario_country_bypass_active` | Applies exactly one normalized technology step, the appropriate reserve package, readiness/control changes, site package, AI profile, status idea, and receipt. It does not record the global history row. |
| `missiles_normalize_technology_stage` | Current country | Derives the highest supported logical stage from installed rocket technologies and stores the normalized stage. |
| `missiles_apply_next_technology_step` | Current country with normalized stage | Grants one next valid installed technology step and records an unresolved mapping instead of granting unrelated technology when no branch is available. |
| `missiles_apply_mature_program_package` | Current country at complete stage | Applies the one-time mature reserve, capacity, readiness, command, and mature-line package. |
| `missiles_refresh_program_status_idea` | Current country | Replaces the single Event 032 status idea and refreshes phase flags. |
| `missiles_clamp_program_values` | Current country | Clamps reserve custody at zero and readiness/control to the inclusive 0–100 range. |
| `missiles_evaluate_country_evolution_adoption` | Current country | Applies separately gated country adoption flags for unlocked evolutions whose country prerequisites are met. |
| `missiles_assign_ai_profile` | Current country | Assigns a persistent doctrine profile from war status, guidance, custody, control, payload availability, and evolution state. |

Operational Reserve and reserved missiles are separate variables. Reserve changes are bounded by the country cap and physical site custody, while prepared operations debit a site-held allocation exactly once. An operation's missiles are allocated to its participating sites in whole missiles by spare capacity: each pass offers every site with room an equal whole share of what remains, so the allocations always sum exactly to the order when the sites' combined capacity covers it, and a site that receives nothing leaves the order. If a reserving site is captured or destroyed, or its owner scuttles it, before launch, the order ends and the missiles readied at that site are lost once while the rest return to reserve; a natural disaster that does not wreck the site cancels the order and returns all of them.

Creation packages evaluate all country factors first and round the resulting grant to whole missiles before changing Operational Reserve.
Committed stock and prepared allocations are not rounded or regenerated by this creation step.

First-package recipients advance from their normalized existing research just as repeat recipients do.
A completed supported line produces the mature package and remains a valid mapping on later firings.
Technology grants suppress their separate notification because the human recipient already receives the country report.

## Launch-state contract

Launch sites are state-scoped physical records registered only in a state owned and controlled by the current country. A candidate must be valid land, have usable infrastructure and supply, and not be wasteland, isolated, scuttled, or an occupied enemy state.

Site scoring considers infrastructure, supply, defense, strategic depth, strategic-region dispersion, capital status, frontline exposure, and existing-site priority. Existing damaged or upgradeable sites are repaired or upgraded before a new site is selected. The capital is a fallback, not an automatic first choice, and a one-state minor uses its sole valid state when it meets the contract.

Each site stores level, physical capacity, site-held reserve, hardening, security, damage, capture, isolation, compromise, rogue state, strategic-region identity, controller identity, and lifecycle receipts. The physical capacity ladder is derived from site level rather than receiving a raw scenario missile count: levels one through four map to initial, reinforced, expanded, and strategic capacity. Site count and saturation capacity remain finite.

Capture, civil-war split, release inheritance, annexation, state destruction, occupation, and scuttling use the lifecycle helpers in `032_missiles_operations_effects.txt`. The current controller must be proven before custody changes. A prepared operation tied to a captured or destroyed site is cancelled or reassigned through its receipt, and reserve is never recreated by repair, inheritance, or recovery.

A captured site puts its new controller into the incident phase until the site is resolved. One captured state at a time is offered through four final, mutually exclusive decisions: guard it (the site stays inactive and its stored missiles stay sealed), study it (the same, plus a guidance-training gain), integrate it (a guided program only; the site joins the network and its surviving missiles join Operational Reserve once), or scuttle it (the site and its stored missiles are destroyed once). When no controlled captured state awaits resolution the capture incident closes and the program leaves the incident phase. After a country's own launch goes wrong, the incident phase also offers accelerated recovery (once per incident), emergency guidance recalibration for the next launch after a breakup, wrong-state hit, dud, neutral accident, or self-strike, debris investigation when the missile came down in its own or a faction partner's territory (confirming attribution and adding guidance training), and, for an unconfirmed neutral accident, a political denial that closes the incident with worse relations and leaves the record disputed. Inspecting the incident closes the response, so these actions come first. A former controller, or a country whose captured site is retaken, refreshes its own network, captured-site marker, and rogue closure through the immediate hidden receiver `chaosx.nr32.7`, so no network helper runs under another country's ROOT. Network totals count integrated sites in occupied states and skip unresolved captured sites.

## Operation API and state machine

The operation layer in `common/scripted_effects/032_missiles_operations_effects.txt` and `common/scripted_triggers/032_missiles_operations_triggers.txt` freezes actor, victim, exact target state, target profile, strike profile, site, payload, reserve, range, and incident linkage before preparation.

The ordinary flow is target selection, preparation, commitment revalidation, launch, guidance resolution, interception, drift, impact, conventional or special consequence delivery, evidence and attribution, incident receipt, achievement recording, and cleanup. A prepared operation cannot silently retarget. Reservation, launch consumption, cancellation, failed release, capture, and scuttle each have separate bounded receipts.

The four strike profiles are Precision, Strategic, Saturation, and Counterforce. They have distinct capacity demands, preparation times, readiness costs, command burden, target restrictions, defense interaction, damage spread, and AI weights. Saturation requires both the Saturation Arsenals evolution and country adoption. The adapter uses scripted launch resolution because the installed native raid surface does not expose the Event 032 site-custody, payload, guidance, attribution, incident, and cleanup contract.

Conventional impact resolves real strategic building levels, supply, air and coastal facilities, command targets, and counterforce sites with bounded damage. Population loss and military loss are submitted through supported shared Deaths routes exactly once. Neutral and self-strike outcomes are attributable failure results and severe outcomes remain bounded by the guidance and collateral tuning.

## Guidance and payload delivery

Guidance is derived from normalized technology, training, readiness, maintenance, site condition, range, barrage size, command control, hardening, and the Unreliable Guidance state; it is not an unnecessary permanent parallel meter. Guidance outcomes include on-target, degraded, wrong-object, near-miss, breakup, wrong-state, neutral, self-strike, and site-accident results where the supported adapter can distinguish them.

Special Warheads never grants technology, policy, stockpile, or payload inventory. Chemical delivery requires the existing chemical air-interdiction technology, an eligible existing agent, real stockpile, approved policy, missile reserve, and site custody. Biological delivery requires an existing supported biological technology and real equipment. Nuclear and thermonuclear delivery require their existing technologies and a positive real nuclear stockpile.

Special-payload orders are three costed decisions available while Special Warheads is enabled and adopted: Integrate Special Payload (opens the family choice, stores the fitted warhead at a secure site, and then asks for standing orders), Select Special Payload (conventional is always available), and Set Special-Payload Policy (prohibited, retaliation only, military targets only, wartime, or emergency delegation). Humans issue them while choosing an objective for a selected enemy; the AI uses them in any working phase. No order changes an operation that is already prepared.

A prepared special operation holds its warhead from the moment preparation is accepted. A nuclear, thermonuclear, or biological warhead leaves the national stockpile into one held receipt; aborting or cancelling the operation returns it once, and a confirmed release consumes it once without a second debit. Chemical agent stays in the CBRN ledgers, which expose no route back into storage, so its sufficiency is proven against the frozen target at preparation and the agent is debited at release. If the warhead cannot be reserved, the missile reservation is returned and the order is refused.

After confirmed release, `missiles_consume_special_payload` consumes the held warhead (or debits chemical agent) and the missile allocation once, then submits the delivery context to the shared CBRN, Deaths, Air Cleanliness, evidence, Condemnation, and Fallout consequence owners. No shared consequence is called for a blocked preparation, interception, breakup, or pre-release accident, and Event 032 never sets `world_end`.

## Evolution tracks

The five tracks have independent eligibility, delayed pacing, disable gates, global unlock receipts, Event Log evolution rows, country adoption checks, AI factors, interactions, and disabled-safe branches.

Eligibility is recounted live over the durable programme registry `global.missiles_program_registry`, never by a world scan. Rogue Launch Commands needs Gathering Storm and at least one vulnerable programme (weak command control, compromise, civil war, low stability, or a damaged, captured, or occupied site). Unreliable Guidance needs Rising Chaos, an operational programme, and real strain: two programmes with low readiness, stored missiles beyond site capacity, three committed launches worldwide, or half the advanced programmes never investing in guidance. Saturation Arsenals needs Chaos Tier, at least two operational programmes forming at least 40% of the live programme pool, and two programmes at war. Special Warheads needs Totalen Chaos and one programme that owns both the technology and the physical stock of a supported payload. Automatic Retaliation needs at least 900 chaos, no world end, two operational programmes, and one responding programme (advanced stage, hardened secure site, command control 75, and a response reserve) at war with another operational programme.

When a track first becomes eligible it arms one delayed job: its base delay (Rogue 120, Guidance 105, Saturation 90, Special 120, Retaliation 150 days) is halved under high pressure, lengthened when fewer than two programmes exist, and spread at random between three quarters and five quarters. The first high-chaos firing instead arms short jobs 21 days out, staggered 14 days apart. The job runs as `chaosx.nr32.190` on a living registered programme, recounts eligibility, and commits at most one due track per run through the shared evolution log behind `is_current_evolution_enabled`, re-queuing itself a week later when another track is also due; a track whose eligibility lapsed by its due date is dropped until it qualifies again. Every Event 32 firing runs the same evaluation, and while an enabled track is still locked one evolution watch (`chaosx.nr32.191`) on the host repeats it every 30 days, so a track that becomes eligible between firings is armed without waiting for another firing. After an unlock, every registered programme refreshes its access through `chaosx.nr32.8`. Disabling a track clears its pending job at the next evaluation, and a removed host hands pending jobs to another living programme.

| Track | Runtime effect |
| --- | --- |
| Saturation Arsenals | Increases bounded capacity and barrage scale, requires several sites or sufficient physical capacity, raises guidance pressure, and changes reserve-floor and AI target-value rules. |
| Unreliable Guidance | Adds drift and failure outcomes, pressure from range and barrage size, and response decisions for investigation and containment. |
| Special Warheads | Enables country-specific integration only when an existing payload owner has the required technology, policy, stockpile, and custody. |
| Rogue Launch Commands | Derives command pressure from real control, stability, civil war, site count, reserve, and compromise, then opens one capped incident per country with a foreign-actor check where required. |
| Automatic Retaliation | Adds Off, Supervised, Delegated, and Automatic posture states, warning verification, bounded queue receipts, response windows, and linked delayed retaliation operations. |

An evolution unlock grants access, not adoption. Saturation Arsenals is adopted only through the Adopt Saturation Doctrine decision, which needs a guided program with an active site, more than 15 factories, working command control and readiness, and no rogue command, and costs command power, support equipment, and fuel; a country may delay or decline it. Adoption raises the reserve ceiling, and every saturation bonus reads the live enabled-and-adopted trigger. Automatic Retaliation gives a country access to the warning network with its posture Off; the Set Retaliation Posture decision (command power and readiness, medium cooldown, unavailable during a warning, a committed retaliation, or a severed network) opens the posture choice, where Supervised needs network command and Automatic keeps its higher command gate. The warning event's accept option, the Accept the Current Response decision, and the Delegated or Automatic posture share one response route and one gate, which also requires a launch-capable site, the response reserve, and a country able to prepare a strike. Each warning can be delayed once, and the outcome of the last warning (delayed, proven false, expired, or answered) is cleared when the next warning opens, so a false alarm never blocks the automatic answer to a later attack. Automatic retaliation never calls the launch path recursively. Warning events are delayed ordinary country events and every response is bounded by root generation, root participants, per-country response, linked incidents, queue slots, surviving site, and reserve limits. Low Retaliation Network starts no destructive incident; Maximum remains finite.

## Decisions, missions, and crisis actions

`missiles_program_management_category` is one ordinary category with the static picture `GFX_decision_cat_picture_032_missiles`. Its compact description exposes reserve, readiness, command control, technology, site count, guidance, target, posture, and current crisis without painting a fake meter or adding a dedicated scripted GUI.

The category is phase-gated across establishment, maintenance, expansion, operations, preparation, incident, rogue-command, and retaliation states. A country at war with a working site and stored missiles uses the operations view; replenishment, readiness, guidance, and launch-authority work stay available there whenever no strike can be prepared, while a human has not started choosing a target, and always for the AI, so a worn-down program at war can recover. Phases refresh when a war relation begins for both participants, when a country makes peace (which also clears an unfinished target choice), after maintenance actions, and when a warning closes. It exposes target selection, precision/strategic/saturation/counterforce preparation, launch/abort, reserve/readiness/guidance/security work, site construction/hardening/repair/recovery/scuttling, incident response, payload integration, and posture/warning actions. Every spendable action uses the same ability and payment checks for human and AI countries and no action uses more than four spendable cost types.

Timed missions cover site survey, secondary-site construction, strike preparation, site repair, site recovery, warning verification, and retaliation-network restoration. Completion, timeout, cancellation, target invalidation, and capture cleanup clear the matching mission and operation receipts; missions do not act as passive stockpile checklists.

The six project missions are goal-style. A program without a working site surveys one owned, controlled state for 60 days and founds its launch site there. A program with a working site, fewer than four sites, and a reason to expand (a single working site or more stored missiles than its sites can hold) builds a secondary site in a non-capital state over 90 days. A damaged, compromised, or isolated site can be suspended in the incident or maintenance phase, and at war when no strike can be prepared; it leaves launch planning and returns after 45 days with its damage cleared and any isolation lifted, or in its current condition if the repair programme fails. Loyal forces retake a rogue site once at least two divisions stand in its state after 14 days, within the 30-day rogue crisis. Warning verification resolves after 3 days, and a severed retaliation network is restored after 60 days once Command Control, readiness, and an active site are back and no rogue command holds a site. Severing the network starts the restoration immediately, and the restoration decision stays available in the maintenance and operations phases until the network is restored. Each project keeps its own state pointer and due date, and none is cancelled by an unrelated change of program phase.

A rogue crisis records its site in its own pointer, `missiles_rogue_site_state`, chosen when the incident is selected, so a damage, disaster, or capture incident opened during the crisis keeps `missiles_incident_site` and stays open when the crisis ends; the crisis closes its own incident record only while it is the current incident. Isolate the Rogue Site and Scuttle the Rogue Site target only that site from the country's site registry (`missiles_site_is_rogue_incident_site`). Isolating or scuttling any other site, or a strike or disaster wrecking another site, leaves the crisis open. Isolate One Retaliation Site targets the country's own working sites from the same registry. An isolated site, whether cut off by the government, seized by a region, or isolated from the retaliation network, keeps its stored missiles but leaves the network: a strike being prepared there is cancelled and its reservation returns once, and the site can then be suspended and repaired, which returns it to service. The AI scuttles a rogue site mainly to keep a special warhead out of rogue or enemy hands and otherwise prefers isolation.

## SCN-015

Missile Age is the Event 032-owned triggerable scenario at raw ID `15`, between Fallout raw ID `14` and the existing Global Jihad selector raw ID `16`. The collision-audited identity is registered in the shared name, entry, ID-sort, and eligibility surfaces and uses the shared four-level intensity selector.

The five profiles are Global Proliferation, Saturation War, Command Breakdown, Special Payload Crisis, and Retaliation Network. The adapter performs static profile gating in the shared window and an exact bounded roster preflight at launch, then freezes candidate, priority, and selected arrays before committing packages. It records stable failure reasons for invalid selection, no profile pool, disabled gate, missing site plan, missing war, missing payload owner, missing retaliation participants, package failure, duplicate launch, and missing breakdown candidate.

Successful setup records one scenario launch and the selected profile/intensity. Failed preflight records one failed attempt, leaves no durable package mutation, clears transaction and country bypass flags, and sends one review event only to a human origin country. The adapter never creates a normal Event 32 random-event history row, grants a special payload, calls a recursive launch, or sets a terminal flag.

## Shared ownership and bridges

Event 16 retains ownership of its Brilliant Scientist missile-crisis reaction helper. Event 23 retains nuclear breakthrough and stockpile ownership, and Event 76 retains weapons-test ownership. Event 5, Event 6, Event 13, Event 21, civil-war, occupation, release, and annexation paths call only the narrow Event 032 site/custody adapters they own. Natural-disaster damage is fail-closed and controller-validated, with bounded capacity recovery and explicit reserve settlement.

Event Logs owns the single global firing row, shared repeatable pacing, and the five global evolution rows. Event 032 owns operation, warning, incident, attribution, and achievement receipts but does not append a second global firing row for country processing.

## Achievements

The eight achievements are Exact Distance, Still on the Line, Break the Chain, Keys Returned, No Second Sun, Empty the Silos, Sky Full of Steel, and Long Reach. Persistent trackers record distinct target states/countries, operation profiles, site manifests, war identity, warning roots, chain depth, payload use, damage thresholds, repair windows, survival clocks, evolution gates, and disqualifiers. Scenario-origin, force, debug, ceased-country, special-payload, neutral/self-strike, ally-credit, rebuild, and unauthorized-launch disqualifiers are recorded at the relevant boundary.

Shared Event Details toggles suspend each evolution through its canonical event/type/stage flag.
Adoption, unlock history, reserve, and physical payload custody persist, while decisions, AI behavior, preparation, commitment, rogue activity, and retaliation responses consult the live enable state.
Ordinary conventional operations remain available when every evolution is disabled.

Each achievement has completed, grey, and not-eligible DDS assets and matching aliases in `interface/032_missiles.gfx`. No achievement is unlocked by a single Event 032 firing.

## Visual asset package

The final package contains the report image, first-news image, static category picture, category icon, three program ideas, five site-state modifiers, three status texticons, five guidance icons, four posture icons, 27 decision icons, seven mission-family icons, and 24 achievement-state icons.

Runtime files are installed in `gfx/event_pictures/032_missiles/`, `gfx/interface/decisions/032_missiles/`, `gfx/interface/ideas/032_missiles/`, `gfx/interface/state_modifiers/032_missiles/`, `gfx/texticons/032_missiles/`, and `gfx/achievements/`. Source provenance, consumer mapping, hashes, individual DDS round-trips, contact sheets, and visual findings are in `docs/events/032_missiles/asset_audit.md` and `docs/assets/032_missiles/manifest.md`.

Native raid icons are conditional on using a native raid adapter.
The documented RaidInstance contract cannot authenticate the exact launch state or multi-site custody required by Event 32, so the accepted scripted route owns the current operation presentation.
Launch, abort, and accept-response decisions reuse the authorized Event 032 launch, incident, and warning icons as documented in the asset audit.

No portrait, flag, focus art, super-event art, scenario-specific picture, custom 3D model, skeletal animation, frame-animation package, or dedicated scripted-GUI asset is part of Event 032.

## Validation record and blockers

The repository-side asset audit decoded and visually reviewed all 82 runtime DDS files at native resolution and found no crop, bleed, alpha, alignment, or readability defect. Localization and reference audits cover Event 032 events, decisions, missions, scripted localization, achievements, shared Event Log names, and the default-enable allowlist.

The mandatory HOI4 MCP event and technology routes were invoked with narrow selectors. Current bounded Event inspect/render and technology inspect/render artifacts were returned, while Event comparison first returned `EVENT_COMPARISON_BASELINE_REQUIRED` and its artifact-backed retry returned `EVENT_GRAPH_ARTIFACT_INVALID`; technology comparison first returned `TECH_REVISION_NOT_CACHED` and its artifact-backed retry returned `TECH_GRAPH_ARTIFACT_INVALID`. A later completion-auditor observation began at Event revision `410c82bea077…` but did not return a reproducible full artifact, so the parent artifact remains the ledger reference. The Event and technology artifacts remain partial or non-source-accurate because the service defers workspace-wide helper/lifecycle analysis and reports unrelated workspace diagnostics. Exact artifacts and blockers are recorded in `docs/plans/032_missiles_plans/032_missiles_test_results.md`; source review is not presented as engine evidence.

The required live Hearts of Iron IV save, GUI, native raid, achievement, consequence, save/reload, and long-campaign checks were not launched because autonomous desktop testing is outside the authorized scope. The remaining user-run checks are listed in `docs/specs/032_missiles_specs/032_missiles_test_matrix.md`.

The no-DLC technology adapter preserves the logical stage contract by mapping the installed rocket line and using the supported `improved_rocket_engines` successor when the optional improved-guidance project technology is unavailable. This is a documented functional normalization path, not a grant of nuclear, chemical, biological, Kruger, or unrelated technology.

## Future extension

A future native adapter requires an authenticated launch-state and instance-receipt contract before it can receive an Event 32 consumer or icon.
Any accepted replacement must retain custody and consequence parity and pass the same visual consumer audit.

A future balance pass may add campaign telemetry to the named probability scenarios, but it must keep the bounded recipient transaction, finite retaliation chain, exact reserve custody, and same-scenario probability comparison requirements.
