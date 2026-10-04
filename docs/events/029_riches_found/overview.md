# Event 029 - Riches Found

## Documentation status and acceptance

This overview describes the current source implementation and accepted design, with unresolved validation recorded in the [2026-10-03 progress report and resume packet](../../plans/029_riches_found_plans/2026_10_03_resume_packet.md).
Acceptance comes from the user's explicit request to implement `docs/specs/029_riches_found_specs/` fully, without simplifications, fallbacks, placeholders, or omitted routes.
Source presence does not prove engine behavior, balance, route acceptance, or gameplay completion.
The parent is reviewing mission and custom-cost integrity, new specialist audits remain pending, and same-scenario probability comparison evidence is incomplete.
The 2026-08-29 repository exploration and probability baseline are historical snapshots superseded for current progress by the dated resume packet.

Event 029 is a Minor Repeatable event rooted at `chaosx.nr29.1`. It selects one uniformly random eligible ordinary country, grants that country exactly 1,000 political power once, and registers one valid owned and controlled state as a persistent mine. The mine record belongs to the state, while decisions, risks, contracts, presentation, aggregate benefits, and the controller idea are rebuilt for the current controller.

Event 029 is not an event cluster member. Its ordinary lifecycle remains separate from Event 018 Resources Found: it does not add ordinary strategic resources, create or enter Event 018 caves, reveal Oth-Kesh, call The World Opens Below, or use Event 018 terminal routes. Event 018 field and cave markers and existing Event 029 mine records are explicit target exclusions.

## Discovery and state ownership

The shared random-event dispatcher calls `riches_found_prepare_random_event_fire`.
That helper builds a pool with one entry per eligible ordinary country, then selects a valid state through its preferred/broad weighted branches and saves the owner/state pair as regular event targets.
Event Details and manual availability use the preparation contract.
The accepted design requires a fresh valid pair and `N/A` when none exists.
Preparation resets readiness for each call, records a fresh state selection through `riches_found_save_prefire_state`, and validates that exact country/state pair before publishing readiness.
An empty pool or a call that selected no state leaves readiness at zero, even when regular event targets from an earlier call remain in the effect chain.
Same-scenario MCP evidence for that transaction remains unresolved.

`riches_found_commit_discovery` initializes the state record and pays the discovery grant only after the state was registered successfully. The state flag `riches_found_discovery_grant_paid` makes the 1,000-political-power grant idempotent, so direct refiring, controller cycling, occupation, and repeatable Event 029 occurrences cannot pay twice for the same mine.

The persistent state record contains the mine sequence, original discoverer, current recorded controller, four public values, hidden risk values, phase, operating state, contracts, missions, route history, controller-transfer history, evolution history, achievement state, and presentation state. A bounded global array contains at most 64 registered Event 029 mine states and is the only cross-mine registry.

## Controller transfer and aggregate benefit

The narrow `on_state_control_changed` hook uses the documented scope contract in which `ROOT` is the new controller, `FROM` is the old controller, and `FROM.FROM` is the changed state. It reconciles only when that state is an Event 029 mine. Annexation, peace-conference completion, and capitulation traverse only the bounded mine registry to cover ownership and occupation transitions that do not necessarily emit the same control change.

Reconciliation removes the old controller's contribution, records the new controller once, migrates selected-mine and mission ownership, refreshes the state modifier and controller idea, and rebuilds both affected country aggregates. It does not copy the state record or leave a second contribution behind.

The country aggregate applies marginal factors of 1.00 to the first controlled mine, 0.60 to the second, 0.25 to the third, and 0.10 to later mines. Contribution components are capped and rebuilt from the bounded registry, so transfer cannot duplicate them and temporary occupation receives the explicit occupied-control factor rather than an owner-equivalent windfall. The same rebuild replaces one mutually exclusive controller stage—Windfall Receipts, Managed Mineral Revenue, Resource-Dependent Treasury, Captured Revenue State, Gold-Sick Administration, Infernal Accounts, or Reformed Resource Settlement—rather than adding one permanent idea per mine.

## Decision category and public values

`riches_found_mine_management` is one ordinary decision category with the static picture `GFX_decision_cat_picture_riches_found`. There is no Event 029 scripted GUI.

The category description presents:

- Extraction Pressure as the primary value;
- Mine Development as a supporting value;
- Local Order as a supporting value;
- Revenue Legitimacy as a supporting value.

Scripted localisation converts exact values into concise bands and adds only the phase, operating state, contract, active-mission, transfer, and evolved-track context currently relevant to the selected mine. State-targeted decisions select the mine directly; a multiple-mine controller can change the selected mine without creating a duplicate state record.

The baseline phases are discovery and claims, the rush, physical development, revenue settlement, foreign concessions, armed protection and raids, and consolidation, closure, or control crisis.
The accepted presentation requires three to five primary actions per ordinary phase, at most six, and one to three active missions.
Actual visibility, mission capacity, objective freshness, cleanup, and payment integrity remain subject to the parent's current review and the pending decision audit.

## Baseline lifecycle

The claims phase surveys the deposit, registers claims, freezes claims, recognizes local claims, reserves the deposit, or opens a claims court. Rush actions establish camp administration, local labor, specialist labor, armed workers, or a truce. Development actions build rail or port access, processing works, housing, shaft reinforcement, and workforce systems. Revenue actions choose central receipts, local revenue, citizens' dividends, a development fund, disclosure, audits, and stabilization measures.

Foreign participation is represented by one state-owned contract record with one partner, review clock, renewal state, and term flags.
Compatible limited-concession, offtake, and infrastructure-access terms use the existing partner record, while exclusive concessions block amendments.
The parent corrected `riches_found_begin_contract` to require exclusive request 1 and the stored exclusive contract type, and corrected limited-contract amendment refresh to run through the current `CONTROLLER`.
These source repairs and their validation limits are recorded in `docs/plans/029_riches_found_plans/subagent_handoffs/2026_10_03_parent_contract_repairs.md`.
Land-only foreign availability, including the required distant naval-power route, remains unresolved.
Renewal, expiry, publication, audit, nationalization, buyout, and payment integrity remain subject to the pending audits.

The security and crisis layer includes mine police, private guards, army cordons, pay-route protection, raid responses, occupation administration, transfer settlements, temporary closure, repair, collapse response, restoration, permanent sealing, and cleanup. Mission sequence and cooldown proofs prevent repeated completions from farming counters, benefits, or achievement progress. Permanent historical disqualifiers are not cleared by ordinary mission cleanup.

### Closure, collapse, and recovery

Every closing action (Temporary Closure, the Gold Disease closure, and an occupier's Deny the Mine) runs `riches_found_begin_temporary_closure`, so the closure state, operating state, phase, review date, and suspended contract persist across presentation refreshes.
While a mine is temporarily closed, `riches_found_service_closed_mine` in the maintenance pulse lowers Extraction Pressure each pulse interval by `riches_found_closure.pressure_decay_per_pulse`, lowers collapse pressure until the closure review date, and lowers Revenue Legitimacy unless the workers are paid or share in the revenue (dividend, local revenue settlement, worker cooperatives, or a public revenue share).
At the review date the mine gains `riches_found_closure_review_complete`; a closure kept in place after that slowly raises collapse pressure unless the shafts were reinforced.
Reopen the Mine is a state-targeted action in the ordinary category, visible only while `riches_found_mine_closure_can_reopen` holds.
It requires the safety and order check `riches_found_mine_reopening_is_safe` (pressure below the reopening ceiling, a rail or port route, and adequate Local Order or a security force), costs light political power, standard manpower and standard support equipment, and runs a recovery inspection for `riches_found_duration.recovery_review_days`.
At the end of the inspection `riches_found_finish_reopening` returns the mine to regulated operation (sealed deep sections stay sealed), reviews any suspended contract with its partner, and sets a reopening cooldown that blocks an immediate second closure; if the payer lost the mine or the check failed, the reopening is cancelled and the payment refunded.

Damage is a persistent physical fact that only a completed restoration clears.
A collapse always implies damage; major-failure and catastrophic collapse incidents close the workings through `riches_found_collapse_mine`, which records harm once per collapse.
Repair is visible on any damaged mine and starts Restore the Shaft; its crews deliver after the decision's removal period only if the payer still holds the mine with the mission running, otherwise the payment is refunded.
The mission completes when `riches_found_restore_shaft_works_ready` holds, and its completion runs `riches_found_complete_shaft_restoration`, which clears damage, route damage and any severe collapse and returns a collapsed mine to regulated operation through the shared recovery helpers.
A partial result reopens a collapsed mine's upper workings as a partial seal while its damage and any severe collapse remain for a later restoration, and a collapsed mine left without repairs after its recovery date loses development each pulse interval.

## Evolutions and late outcomes

Event 029 registers exactly three evolution rows:

1. The Resource Curse at Chaos Tier, 600+.
2. Gold Disease at Totalen Chaos, 800+.
3. Demons Beneath the Mine at World Collapse, 1,000+.

The active mine pulse can enter an enabled evolution after its state gates and MTTH resolve. Before the opening event is shown, the prepared state can also receive an evolved opening when the current chaos level and state profile satisfy the same track contract. Each registered track records one evolution-log row and cannot record it twice.

The Resource Curse layers dependence, patronage, concession capture, illicit revenue, reform, and sovereign-control pressure over the ordinary mine lifecycle. The Gilded Sovereignty is a late Resource Curse outcome, not a fourth evolution row.

Gold Disease is a fictional compulsive administrative and social crisis. It uses Event 029-specific pressure, movement, sanitation, quarantine, administration, and containment state and never invokes the biological outbreak, disease, or plague systems.

Demons Beneath the Mine uses an Event 029-specific supernatural-force record, deep-excavation pressure, bargains, evacuation, scientific, religious, engineering, sealing, and containment routes. It does not reuse Event 018 underground actors, Oth-Kesh, or any existing terminal entity. The Bottomless Account is a late Demons Beneath the Mine outcome, not a fifth evolution row.

### Gold Disease movement routes

`common/scripted_effects/029_riches_found_gold_route_effects.txt` moves Gold Disease only through the specification's six bounded routes, each called by one action or result: Replace the Workforce (and the emergency workforce replacement) sends the old crews to another active mine of the same controller, raising its gold pressure, or to the capital; a completed Protect the Pay Train delivers a shipment to the capital; the Pay Train escort carries wages; Military Control rotates soldiers into the army; guard-theft and false-permit incidents sell stolen material to one foreign controller of a neighbouring state; and a contract that ends while the fever is active sends the sponsor's staff home.
Each route rolls `riches_found_gold_route.spread_weight` against `contained_weight`, multiplied by `restricted_factor` under a quarantine, rationed access or closure.
A spread gives the receiving country a temporary `riches_found_country_gold_fever` (or `riches_found_country_gold_fever_army` for the rotation route) for `country_effect_days`, or raises gold pressure at the receiving mine, and the source mine reports the route and its destination by name.
No route scans the world, runs on a timer or uses the biological outbreak systems.

### Containment and aftermath

Each evolution has an active flag (`riches_found_resource_curse_active`, `riches_found_gold_disease_active`, `riches_found_demons_beneath_mine_active`) separate from its permanent history flag and log row.
`common/scripted_effects/029_riches_found_containment_effects.txt` keeps one per-mine progress value per active track (0 to `riches_found_containment.progress_complete`), reviewed once per controller pulse interval from the maintenance pulse.
Each condition that currently holds adds `step_gain`; fewer than the track minimum decays the progress, and a breaking condition decays it faster and blocks gains.

- The Resource Curse counts an audit (or an independent revenue authority where no concession exists), public terms or state operation, beneficial-owner disclosure where a concession exists, a revenue settlement paid within the last cycle, a development or stabilization fund, Extraction Pressure below the warning band, reined-in private security, and a replaced administration or independent authority. Tolerated corruption, tolerated patronage or illicit capture at its gate break it. Containment sets the Reformed Resource Settlement stage, records a successful reform and can relapse if corruption, patronage or private dominance returns.
- Gold Disease counts gold pressure below its gate, stopped movement (quarantine, rationed access or closure), a revenue settlement, replaced crews or administration without gold-sick guards, no seized material, shipment threat or gang control, and undamaged workings. Severe Extraction Pressure breaks it, and high pressure on an operating mine feeds the fever each review. Containment leaves the permanent `riches_found_state_gold_susceptible` modifier; gold exposure resumes with a susceptibility bonus and the disease relapses when pressure and gold pressure both return.
- Demons Beneath the Mine counts supernatural pressure below its gate, sealed sections or a closure, an evacuated district, active religious, occult or scientific assistance, Extraction Pressure below the warning band, a security force, and sealed-depth integrity at its gate. An open infernal account or deep digging breaks it. The end state is a monitored closure (scientific assistance), a protected closure (religious or occult assistance), a guarded abandoned district (any other closure) or upper workings under strict limits (partial seal); closure end states cannot be reopened, and renewed deep digging relapses the crisis. Permanent sealing remains its own end.

Crisis responses are reusable: revenue distributions and Gold Disease measures last a set number of days and can be renewed, assistance stays for a year, and the capture choices toggle against nationalization and the independent authority. Projects (funds, sealing the deep sections) and population-affecting actions (purge, evacuation) stay one-time per mine, and the corruption bribe pays only once.
The first unmet condition of the highest-priority active track becomes the category header objective, and containment queues one report (`chaosx.nr29.121` to `.123`).

## AI and probability contract

AI willingness is centralized through Event 029 constants and file-scoped aliases for country scale, ideology, war pressure, desperation, occupation, neighboring interest, concession seeking, raiding, multiple-mine burden, public-value thresholds, route state, and crisis state. Controller, occupier, partner, neighbor, and raider behavior is evaluated through the named scenarios in `docs/specs/029_riches_found_specs/029_riches_found_ai_probability_scenarios.md`.

The HOI4 MCP probability workflow treats the computed values as relative willingness scores among currently available actions, not literal click probabilities. Baseline inspection, named scenario evaluation, threshold sweeps, bounded owner patches, and same-scenario comparison belong in `docs/plans/029_riches_found_plans/`.

## Achievements

The accepted package requires seven achievements using historical flags, dates, counters, transfer proofs, disqualifiers, and bounded registry checks.
Tracking helpers exist in `common/scripted_effects/029_riches_found_achievement_effects.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.
At the 2026-10-03 documentation observation, none of the seven IDs below was found in `common/achievements/chaos_redux_achievements.txt`, despite the older icon handoff's registry claim.
Registry integration and unlock/disqualifier validation remain unresolved.


- `029_public_fortune` rewards the original discoverer for mature, legitimate, orderly public development without an exclusive concession or Resource Curse.
- `029_claim_jumper` rewards a valid new controller that settles and holds another country's operational mine without leaving the old contribution behind.
- `029_the_pay_train_runs` requires three distinct route-risk protection successes without an intervening robbery or duplicate mission count.
- `029_all_that_glitters` requires three safe, active mines under one valid capped aggregate for the verification period.
- `029_no_man_owns_the_mountain` requires non-destructive recovery from The Gilded Sovereignty.
- `029_close_the_account` requires controlled evacuation and sealing after The Bottomless Account while removing the positive supernatural contribution.
- `029_the_last_shift` requires evacuation, a valid assistance route, permanent sealing, and avoidance of mass death, purge, reopening, and supernatural agreement.

`interface/029_riches_found.gfx` declares completed, grey, and not-eligible sprite aliases pointing into `gfx/achievements/` for each ID.
All seven exact IDs are registered in `common/achievements/chaos_redux_achievements.txt` and have Career Profile title and description keys.
Commit `01bc85ee3c9f25be8bda48dbdd7dc4d0ed1f98fe` records that integration and the persistent exclusivity, transfer, and aggregate-cap disqualifier repairs.
Full tracking and unlock acceptance remains unresolved.

## Runtime files

- Event definitions: `events/029_riches_found.txt`.
- Constants and MTTH: `common/script_constants/029_riches_found_constants.txt` and `common/mtth/029_riches_found_mtth.txt`.
- Core, incident, harm, history, achievement, and CXT effects: `common/scripted_effects/029_riches_found_effects.txt`, `common/scripted_effects/029_riches_found_incident_effects.txt`, `common/scripted_effects/029_riches_found_harm_effects.txt`, `common/scripted_effects/029_riches_found_log_effects.txt`, `common/scripted_effects/029_riches_found_achievement_effects.txt`, and `common/scripted_effects/029_riches_found_cxt_effects.txt`.
- Gameplay and achievement triggers: `common/scripted_triggers/029_riches_found_triggers.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.
- Decisions, missions, and category: `common/decisions/029_riches_found_decisions.txt` and `common/decisions/categories/029_riches_found_categories.txt`.
- State presentation and country ideas: `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` and `common/ideas/029_riches_found_ideas.txt`.
- Narrow lifecycle and CXT hooks: `common/on_actions/029_riches_found_on_actions.txt` and `common/on_actions/029_riches_found_cxt_on_actions.txt`.
- Scripted localisation and English text: `common/scripted_localisation/029_riches_found_scripted_localisation.txt`, `localisation/english/029_riches_found_l_english.yml`, and `localisation/english/029_riches_found_decisions_l_english.yml`.
- Sprite registration: `interface/029_riches_found.gfx`.
- Authoritative event catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Shared registration and presentation adapters remain in the event-system, Event Logs, Event Details, settings, achievement, and scripted-localisation owner files. Event 029 does not own or add a dedicated GUI file.

## Icon and sprite wiring

The asset inventory and evacuation-action/evacuation-mission semantic reuse are recorded in `docs/assets/029_riches_found/icon_manifest.md`.
That manifest and the inherited asset handoffs remain evidence for parent review, rather than independent acceptance of every asset or reuse claim.
Event 029 sprite declarations live in `interface/029_riches_found.gfx`.
The parent's individual source, processed-PNG, and decoded-DDS review of the nine reports and static category picture is recorded in `docs/plans/029_riches_found_plans/subagent_handoffs/2026_10_03_parent_report_art_review.md`.
That review reports ten current validator passes with exact processed-to-decoded pixels and evidence-to-runtime byte equality.
It establishes standalone art and file-chain review rather than event-chain, category-action, icon-family, or package acceptance.

- Report cards use `GFX_report_event_riches_found_*` and live in `gfx/event_pictures/029_riches_found/`.
- The category picture and category icon are `GFX_decision_cat_picture_riches_found` and `GFX_decision_category_riches_found` in `gfx/interface/decisions/029_riches_found/`.
- Decision icons use `GFX_decision_riches_found_*` in the same decision folder.
- Mission icons use `GFX_mission_riches_found_*` in the same decision folder.
- State modifier icons use `GFX_riches_found_state_*` in `gfx/interface/state_modifiers/029_riches_found/`.
- Controller, route, and evolution ideas use `GFX_idea_riches_found_*` in `gfx/interface/ideas/029_riches_found/`.
- Achievement triplets use `GFX_achievement_029_*` and runtime files under `gfx/achievements/`.

## CXT registration

Event 029 registers the modifier-free carrier `chaosx_cxt_extension_event029_riches_found`, which names the idempotent `chaosx_cxt_extension_event029_riches_found_apply` effect.
Startup registers the carrier through one existing country.
The initialized CXT daily fallback registers unseen content and calls `chaosx_test_country_sync_registered_content`, whose current body only sets `chaosx_test_country_registered_sync_pending`.
It performs no daily grants.
Initial CXT setup consumes registered carriers, and later pending content is applied through the player-triggered **Apply Registered Systems** debug decision.

The Event 029 `_apply` effect requires initialized CXT and the absence of `riches_found_cxt_fixture_initialized`.
It attempts to initialize a mine in the capital only when that state is unregistered and passes `riches_found_state_is_valid_target`.
A registered capital mine receives `riches_found_cxt_fixture_mine`, regulated operation, the physical-development phase, public-development policy, and the configured development, order, and legitimacy fixture values.
The helper refreshes presentation, contribution, and controller aggregate, then sets its one-time country guard only after the capital has the fixture flag.
It does not call the discovery-grant transaction or pay the 1,000 political power.
This is an active mine fixture, rather than an inert readiness-only fixture.
The Event 029 entry in `docs/testing/chaosx_test_country.md` describes that same active fixture and the player-triggered pending-package application.

## Future plans

A future non-mutating diagnostic could render a compact registry ledger showing each mine sequence, state, recorded controller, aggregate slot, contribution, contract partner, mission owner, and evolution flags for faster transfer debugging.

A future balance review could expand the named scenario matrix with observed campaign telemetry while retaining the same bounded MCP comparison contract and without turning willingness scores into claimed click probabilities.
