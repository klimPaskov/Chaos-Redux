# Event 032 — Missiles

Event 032 is the bounded worldwide missile-program event owned by `chaosx.nr32`. It is a Minor Repeatable event with ID `32`, Calm World minimum chaos, no cluster membership, and entry event `chaosx.nr32.1`.

## Runtime contract

The shared event dispatcher calls `missiles_prepare_random_event_fire` during Event 32 preflight and then opens the hidden entry event. The entry event's immediate effect is the only global firing transaction.

`missiles_global_firing_transaction` increments one firing receipt, clears and freezes `global.missiles_frozen_recipients`, classifies every country once as accepted, deferred, or skipped, and processes only the frozen accepted array. Recipient receipt IDs make a country idempotent within the firing. The transaction stores the accepted count in the shared history-payload override so the shared repeatable handler records one Event 32 history row after the entry event returns.

The same transaction owns the first-news guard and emits `chaosx.nr32.3` only once. Human recipients receive one delayed country report through `chaosx.nr32.2`; AI recipients are initialized silently. No Event 32 daily, weekly, monthly, or other recurring whole-world scan exists.

The default event pool is enabled by the shared reworked-event allowlist only after the implementation is installed. The repeatable event array, shared event-type resolver, cap reduction, weight recovery, pacing update, unfired counts, and history row remain owned by the shared event system.

## Country-program API

The following country-scoped effects form the public Event 032 program contract.

| API | Inputs | Outputs and side effects |
| --- | --- | --- |
| `missiles_initialize_program_record` | Current country | Initializes missing persistent records and achievement state without granting a package. |
| `missiles_initialize_or_advance_program` | Current country and optional `missiles_scenario_country_bypass_active` | Applies exactly one normalized technology step, the appropriate reserve package, readiness/control changes, site package, AI profile, status idea, and receipt. It does not record the global history row. |
| `missiles_normalize_technology_stage` | Current country | Derives the highest supported logical stage from installed rocket technologies and stores the normalized stage. |
| `missiles_apply_next_technology_step` | Current country with normalized stage | Grants one next valid installed technology step and records an unresolved mapping instead of granting unrelated technology when no branch is available. |
| `missiles_apply_mature_program_package` | Current country at complete stage | Applies the one-time mature reserve, capacity, readiness, command, and mature-line package. |
| `missiles_refresh_program_status_idea` | Current country | Replaces the single Event 032 status idea and refreshes phase flags. |
| `missiles_clamp_program_values` | Current country | Clamps reserve custody at zero and readiness/control to the inclusive 0–100 range. |
| `missiles_evaluate_country_evolution_adoption` | Current country | Applies separately gated country adoption flags for unlocked evolutions whose country prerequisites are met. |
| `missiles_assign_ai_profile` | Current country | Assigns a persistent doctrine profile from war status, guidance, custody, control, payload availability, and evolution state. |

Operational Reserve and reserved missiles are separate variables. Reserve changes are bounded by the country cap and physical site custody, while prepared operations debit a site-held allocation exactly once.

## Launch-state contract

Launch sites are state-scoped physical records registered only in a state owned and controlled by the current country. A candidate must be valid land, have usable infrastructure and supply, and not be wasteland, isolated, scuttled, or an occupied enemy state.

Site scoring considers infrastructure, supply, defense, strategic depth, strategic-region dispersion, capital status, frontline exposure, and existing-site priority. Existing damaged or upgradeable sites are repaired or upgraded before a new site is selected. The capital is a fallback, not an automatic first choice, and a one-state minor uses its sole valid state when it meets the contract.

Each site stores level, physical capacity, site-held reserve, hardening, security, damage, capture, isolation, compromise, rogue state, strategic-region identity, controller identity, and lifecycle receipts. The physical capacity ladder is derived from site level rather than receiving a raw scenario missile count: levels one through four map to initial, reinforced, expanded, and strategic capacity. Site count and saturation capacity remain finite.

Capture, civil-war split, release inheritance, annexation, state destruction, occupation, and scuttling use the lifecycle helpers in `032_missiles_operations_effects.txt`. The current controller must be proven before custody changes. A prepared operation tied to a captured or destroyed site is cancelled or reassigned through its receipt, and reserve is never recreated by repair, inheritance, or recovery.

## Operation API and state machine

The operation layer in `common/scripted_effects/032_missiles_operations_effects.txt` and `common/scripted_triggers/032_missiles_operations_triggers.txt` freezes actor, victim, exact target state, target profile, strike profile, site, payload, reserve, range, and incident linkage before preparation.

The ordinary flow is target selection, preparation, commitment revalidation, launch, guidance resolution, interception, drift, impact, conventional or special consequence delivery, evidence and attribution, incident receipt, achievement recording, and cleanup. A prepared operation cannot silently retarget. Reservation, launch consumption, cancellation, failed release, capture, and scuttle each have separate bounded receipts.

The four strike profiles are Precision, Strategic, Saturation, and Counterforce. They have distinct capacity demands, preparation times, readiness costs, command burden, target restrictions, defense interaction, damage spread, and AI weights. Saturation requires both the Saturation Arsenals evolution and country adoption. The adapter uses scripted launch resolution because the installed native raid surface does not expose the Event 032 site-custody, payload, guidance, attribution, incident, and cleanup contract.

Conventional impact resolves real strategic building levels, supply, air and coastal facilities, command targets, and counterforce sites with bounded damage. Population loss and military loss are submitted through supported shared Deaths routes exactly once. Neutral and self-strike outcomes are attributable failure results and severe outcomes remain bounded by the guidance and collateral tuning.

## Guidance and payload delivery

Guidance is derived from normalized technology, training, readiness, maintenance, site condition, range, barrage size, command control, hardening, and the Unreliable Guidance state; it is not an unnecessary permanent parallel meter. Guidance outcomes include on-target, degraded, wrong-object, near-miss, breakup, wrong-state, neutral, self-strike, and site-accident results where the supported adapter can distinguish them.

Special Warheads never grants technology, policy, stockpile, or payload inventory. Chemical delivery requires the existing chemical air-interdiction technology, an eligible existing agent, real stockpile, approved policy, missile reserve, and site custody. Biological delivery requires an existing supported biological technology and real equipment. Nuclear and thermonuclear delivery require their existing technologies and a positive real nuclear stockpile.

After confirmed release, `missiles_consume_special_payload` debits the actual payload and the missile allocation once, then submits the delivery context to the shared CBRN, Deaths, Air Cleanliness, evidence, Condemnation, and Fallout consequence owners. No shared consequence is called for a blocked preparation, interception, breakup, or pre-release accident, and Event 032 never sets `world_end`.

## Evolution tracks

The five tracks have independent eligibility, delayed pacing, disable gates, global unlock receipts, Event Log evolution rows, country adoption checks, AI factors, interactions, and disabled-safe branches.

| Track | Runtime effect |
| --- | --- |
| Saturation Arsenals | Increases bounded capacity and barrage scale, requires several sites or sufficient physical capacity, raises guidance pressure, and changes reserve-floor and AI target-value rules. |
| Unreliable Guidance | Adds drift and failure outcomes, pressure from range and barrage size, and response decisions for investigation and containment. |
| Special Warheads | Enables country-specific integration only when an existing payload owner has the required technology, policy, stockpile, and custody. |
| Rogue Launch Commands | Derives command pressure from real control, stability, civil war, site count, reserve, and compromise, then opens one capped incident per country with a foreign-actor check where required. |
| Automatic Retaliation | Adds Off, Supervised, Delegated, and Automatic posture states, warning verification, bounded queue receipts, response windows, and linked delayed retaliation operations. |

Automatic retaliation never calls the launch path recursively. Warning events are delayed ordinary country events and every response is bounded by root generation, root participants, per-country response, linked incidents, queue slots, surviving site, and reserve limits. Low Retaliation Network starts no destructive incident; Maximum remains finite.

## Decisions, missions, and crisis actions

`missiles_program_management_category` is one ordinary category with the static picture `GFX_decision_cat_picture_032_missiles`. Its compact description exposes reserve, readiness, command control, technology, site count, guidance, target, posture, and current crisis without painting a fake meter or adding a dedicated scripted GUI.

The category is phase-gated across establishment, maintenance, expansion, operations, preparation, incident, rogue-command, and retaliation states. It exposes target selection, precision/strategic/saturation/counterforce preparation, launch/abort, reserve/readiness/guidance/security work, site construction/hardening/repair/recovery/scuttling, incident response, payload integration, and posture/warning actions. Every spendable action uses the same ability and payment checks for human and AI countries and no action uses more than four spendable cost types.

Timed missions cover site survey, secondary-site construction, strike preparation, site repair, site recovery, warning verification, and retaliation-network restoration. Completion, timeout, cancellation, target invalidation, and capture cleanup clear the matching mission and operation receipts; missions do not act as passive stockpile checklists.

## SCN-015

Missile Age is the Event 032-owned triggerable scenario at raw ID `15`, between Fallout raw ID `14` and the existing Global Jihad selector raw ID `16`. The collision-audited identity is registered in the shared name, entry, ID-sort, and eligibility surfaces and uses the shared four-level intensity selector.

The five profiles are Global Proliferation, Saturation War, Command Breakdown, Special Payload Crisis, and Retaliation Network. The adapter performs static profile gating in the shared window and an exact bounded roster preflight at launch, then freezes candidate, priority, and selected arrays before committing packages. It records stable failure reasons for invalid selection, no profile pool, disabled gate, missing site plan, missing war, missing payload owner, missing retaliation participants, package failure, duplicate launch, and missing breakdown candidate.

Successful setup records one scenario launch and the selected profile/intensity. Failed preflight records one failed attempt, leaves no durable package mutation, clears transaction and country bypass flags, and sends one review event only to a human origin country. The adapter never creates a normal Event 32 random-event history row, grants a special payload, calls a recursive launch, or sets a terminal flag.

## Shared ownership and bridges

Event 16 retains ownership of its Brilliant Scientist missile-crisis reaction helper. Event 23 retains nuclear breakthrough and stockpile ownership, and Event 76 retains weapons-test ownership. Event 5, Event 6, Event 13, Event 21, civil-war, occupation, release, and annexation paths call only the narrow Event 032 site/custody adapters they own. Natural-disaster damage is fail-closed and controller-validated, with bounded capacity recovery and explicit reserve settlement.

Event Logs owns the single global firing row, shared repeatable pacing, and the five global evolution rows. Event 032 owns operation, warning, incident, attribution, and achievement receipts but does not append a second global firing row for country processing.

## Achievements

The eight achievements are Exact Distance, Still on the Line, Break the Chain, Keys Returned, No Second Sun, Empty the Silos, Sky Full of Steel, and Long Reach. Persistent trackers record distinct target states/countries, operation profiles, site manifests, war identity, warning roots, chain depth, payload use, damage thresholds, repair windows, survival clocks, evolution gates, and disqualifiers. Scenario-origin, force, debug, ceased-country, special-payload, neutral/self-strike, ally-credit, rebuild, and unauthorized-launch disqualifiers are recorded at the relevant boundary.

Each achievement has completed, grey, and not-eligible DDS assets and matching aliases in `interface/032_missiles.gfx`. No achievement is unlocked by a single Event 032 firing.

## Visual asset package

The final package contains the report image, first-news image, static category picture, category icon, three program ideas, five site-state modifiers, three status texticons, five guidance icons, four posture icons, 27 decision icons, seven mission-family icons, and 24 achievement-state icons.

Runtime files are installed in `gfx/event_pictures/032_missiles/`, `gfx/interface/decisions/032_missiles/`, `gfx/interface/ideas/032_missiles/`, `gfx/interface/state_modifiers/032_missiles/`, `gfx/texticons/032_missiles/`, and `gfx/achievements/`. Source provenance, consumer mapping, hashes, individual DDS round-trips, contact sheets, and visual findings are in `docs/events/032_missiles/asset_audit.md` and `docs/assets/032_missiles/manifest.md`.

The exact native-raid missile-delivery icon consumer is unavailable in the installed raid namespace, so no unrelated CBRN or nuclear icon was substituted. Launch/abort/accept-response decisions reuse the authorized Event 032 launch, incident, and warning icons because the asset contract did not authorize separate art for those actions; this reuse is documented in the asset audit.

No portrait, flag, focus art, super-event art, scenario-specific picture, custom 3D model, skeletal animation, frame-animation package, or dedicated scripted-GUI asset is part of Event 032.

## Validation record and blockers

The repository-side asset audit decoded and visually reviewed all 82 runtime DDS files at native resolution and found no crop, bleed, alpha, alignment, or readability defect. Localization and reference audits cover Event 032 events, decisions, missions, scripted localization, achievements, shared Event Log names, and the default-enable allowlist.

The mandatory HOI4 MCP event and technology routes were invoked with narrow selectors. Current bounded Event inspect/render and technology inspect/render artifacts were returned, while Event comparison first returned `EVENT_COMPARISON_BASELINE_REQUIRED` and its artifact-backed retry returned `EVENT_GRAPH_ARTIFACT_INVALID`; technology comparison first returned `TECH_REVISION_NOT_CACHED` and its artifact-backed retry returned `TECH_GRAPH_ARTIFACT_INVALID`. A later completion-auditor observation began at Event revision `410c82bea077…` but did not return a reproducible full artifact, so the parent artifact remains the ledger reference. The Event and technology artifacts remain partial or non-source-accurate because the service defers workspace-wide helper/lifecycle analysis and reports unrelated workspace diagnostics. Exact artifacts and blockers are recorded in `docs/plans/032_missiles_plans/032_missiles_test_results.md`; source review is not presented as engine evidence.

The required live Hearts of Iron IV save, GUI, native raid, achievement, consequence, save/reload, and long-campaign checks were not launched because autonomous desktop testing is outside the authorized scope. The remaining user-run checks are listed in `docs/specs/032_missiles_specs/032_missiles_test_matrix.md`.

The no-DLC technology adapter preserves the logical stage contract by mapping the installed rocket line and using the supported `improved_rocket_engines` successor when the optional improved-guidance project technology is unavailable. This is a documented functional normalization path, not a grant of nuclear, chemical, biological, Kruger, or unrelated technology.

## Future extension

A future accepted asset brief may add a dedicated missile-delivery raid icon after the installed raid adapter exposes a stable Event 032 consumer. Any such change must retain the current scripted custody and consequence contract and pass the same visual consumer audit.

A future balance pass may add campaign telemetry to the named probability scenarios, but it must keep the bounded recipient transaction, finite retaliation chain, exact reserve custody, and same-scenario probability comparison requirements.
