# Event 029 - Riches Found

Event 029 is a Minor Repeatable event rooted at `chaosx.nr29.1`. It selects one uniformly random eligible ordinary country, grants that country exactly 1,000 political power once, and registers one valid owned and controlled state as a persistent mine. The mine record belongs to the state, while decisions, risks, contracts, presentation, aggregate benefits, and the controller idea are rebuilt for the current controller.

Event 029 is not an event cluster member. Its ordinary lifecycle remains separate from Event 018 Resources Found: it does not add ordinary strategic resources, create or enter Event 018 caves, reveal Oth-Kesh, call The World Opens Below, or use Event 018 terminal routes. Event 018 field and cave markers and existing Event 029 mine records are explicit target exclusions.

## Discovery and state ownership

The shared random-event dispatcher calls `riches_found_prepare_random_event_fire`. That helper draws one country from the complete eligible ordinary-country set, then draws one legal state inside that country and saves the owner/state pair as regular event targets. Event Details and manual availability use the same preparation contract and fail closed when no valid pair exists; the player-facing target line shows `N/A` instead of inventing a recipient.

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

The baseline phases are discovery and claims, the rush, physical development, revenue settlement, foreign concessions, armed protection and raids, and consolidation, closure, or control crisis. Each phase exposes three to five ordinary actions at once. The shared mission budget permits one to three active missions depending on the current mine and controller conditions.

## Baseline lifecycle

The claims phase surveys the deposit, registers claims, freezes claims, recognizes local claims, reserves the deposit, or opens a claims court. Rush actions establish camp administration, local labor, specialist labor, armed workers, or a truce. Development actions build rail or port access, processing works, housing, shaft reinforcement, and workforce systems. Revenue actions choose central receipts, local revenue, citizens' dividends, a development fund, disclosure, audits, and stabilization measures.

Foreign participation is represented by one state-owned contract record with one partner, review clock, renewal state, and term flags. Compatible limited-concession, offtake, and infrastructure-access terms can be layered with the same partner without creating multiple contracts. Exclusive concessions block those amendments. Renewal, expiry, publication, audit, nationalization, and buyout paths clear grants and partner state through the same lifecycle helpers.

The security and crisis layer includes mine police, private guards, army cordons, pay-route protection, raid responses, occupation administration, transfer settlements, temporary closure, repair, collapse response, restoration, permanent sealing, and cleanup. Mission sequence and cooldown proofs prevent repeated completions from farming counters, benefits, or achievement progress. Permanent historical disqualifiers are not cleared by ordinary mission cleanup.

## Evolutions and late outcomes

Event 029 registers exactly three evolution rows:

1. The Resource Curse at Chaos Tier, 600+.
2. Gold Disease at Totalen Chaos, 800+.
3. Demons Beneath the Mine at World Collapse, 1,000+.

The active mine pulse can enter an enabled evolution after its state gates and MTTH resolve. Before the opening event is shown, the prepared state can also receive an evolved opening when the current chaos level and state profile satisfy the same track contract. Each registered track records one evolution-log row and cannot record it twice.

The Resource Curse layers dependence, patronage, concession capture, illicit revenue, reform, and sovereign-control pressure over the ordinary mine lifecycle. The Gilded Sovereignty is a late Resource Curse outcome, not a fourth evolution row.

Gold Disease is a fictional compulsive administrative and social crisis. It uses Event 029-specific pressure, movement, sanitation, quarantine, administration, and containment state and never invokes the biological outbreak, disease, or plague systems.

Demons Beneath the Mine uses an Event 029-specific supernatural-force record, deep-excavation pressure, bargains, evacuation, scientific, religious, engineering, sealing, and containment routes. It does not reuse Event 018 underground actors, Oth-Kesh, or any existing terminal entity. The Bottomless Account is a late Demons Beneath the Mine outcome, not a fifth evolution row.

## AI and probability contract

AI willingness is centralized through Event 029 constants and file-scoped aliases for country scale, ideology, war pressure, desperation, occupation, neighboring interest, concession seeking, raiding, multiple-mine burden, public-value thresholds, route state, and crisis state. Controller, occupier, partner, neighbor, and raider behavior is evaluated through the named scenarios in `docs/specs/029_riches_found_specs/029_riches_found_ai_probability_scenarios.md`.

The HOI4 MCP probability workflow treats the computed values as relative willingness scores among currently available actions, not literal click probabilities. Baseline inspection, named scenario evaluation, threshold sweeps, bounded owner patches, and same-scenario comparison belong in `docs/plans/029_riches_found_plans/`.

## Achievements

Seven achievements use historical flags, dates, counters, transfer proofs, disqualifiers, and bounded registry checks rather than deriving history from the current state alone:

- `029_public_fortune` rewards the original discoverer for mature, legitimate, orderly public development without an exclusive concession or Resource Curse.
- `029_claim_jumper` rewards a valid new controller that settles and holds another country's operational mine without leaving the old contribution behind.
- `029_the_pay_train_runs` requires three distinct route-risk protection successes without an intervening robbery or duplicate mission count.
- `029_all_that_glitters` requires three safe, active mines under one valid capped aggregate for the verification period.
- `029_no_man_owns_the_mountain` requires non-destructive recovery from The Gilded Sovereignty.
- `029_close_the_account` requires controlled evacuation and sealing after The Bottomless Account while removing the positive supernatural contribution.
- `029_the_last_shift` requires evacuation, a valid assistance route, permanent sealing, and avoidance of mass death, purge, reopening, and supernatural agreement.

Each achievement has completed, grey, and not-eligible DDS variants in `gfx/achievements/`, registered in `interface/029_riches_found.gfx`.

## Runtime files

- Event definitions: `events/029_riches_found.txt`.
- Constants and MTTH: `common/script_constants/029_riches_found_constants.txt` and `common/mtth/029_riches_found_mtth.txt`.
- Core, harm, history, achievement, and CXT effects: `common/scripted_effects/029_riches_found_effects.txt`, `common/scripted_effects/029_riches_found_harm_effects.txt`, `common/scripted_effects/029_riches_found_log_effects.txt`, `common/scripted_effects/029_riches_found_achievement_effects.txt`, and `common/scripted_effects/029_riches_found_cxt_effects.txt`.
- Gameplay and achievement triggers: `common/scripted_triggers/029_riches_found_triggers.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.
- Decisions, missions, and category: `common/decisions/029_riches_found_decisions.txt` and `common/decisions/categories/029_riches_found_categories.txt`.
- State presentation and country ideas: `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` and `common/ideas/029_riches_found_ideas.txt`.
- Narrow lifecycle and CXT hooks: `common/on_actions/029_riches_found_on_actions.txt` and `common/on_actions/029_riches_found_cxt_on_actions.txt`.
- Scripted localisation and English text: `common/scripted_localisation/029_riches_found_scripted_localisation.txt`, `localisation/english/029_riches_found_l_english.yml`, and `localisation/english/029_riches_found_decisions_l_english.yml`.
- Sprite registration: `interface/029_riches_found.gfx`.
- Authoritative event catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Shared registration and presentation adapters remain in the event-system, Event Logs, Event Details, settings, achievement, and scripted-localisation owner files. Event 029 does not own or add a dedicated GUI file.

## Icon and sprite wiring

The complete asset inventory and the approved evacuation-action/evacuation-mission semantic reuse are recorded in `docs/assets/029_riches_found/icon_manifest.md`. All Event 029 sprite declarations live in `interface/029_riches_found.gfx`.

- Report cards use `GFX_report_event_riches_found_*` and live in `gfx/event_pictures/029_riches_found/`.
- The category picture and category icon are `GFX_decision_cat_picture_riches_found` and `GFX_decision_category_riches_found` in `gfx/interface/decisions/029_riches_found/`.
- Decision icons use `GFX_decision_riches_found_*` in the same decision folder.
- Mission icons use `GFX_mission_riches_found_*` in the same decision folder.
- State modifier icons use `GFX_riches_found_state_*` in `gfx/interface/state_modifiers/029_riches_found/`.
- Controller, route, and evolution ideas use `GFX_idea_riches_found_*` in `gfx/interface/ideas/029_riches_found/`.
- Achievement triplets use `GFX_achievement_029_*` and runtime files under `gfx/achievements/`.

## CXT registration

Event 029 registers the modifier-free carrier `chaosx_cxt_extension_event029_riches_found`; CXT dispatches `chaosx_cxt_extension_event029_riches_found_apply`. The fixture initializes only the bounded registry and readiness state and does not fire Event 029, grant political power, create a mine, or activate an evolution. Startup registration uses one existing country and the existing-save repair path is restricted to `on_daily_CXT`.

## Future plans

A future non-mutating diagnostic could render a compact registry ledger showing each mine sequence, state, recorded controller, aggregate slot, contribution, contract partner, mission owner, and evolution flags for faster transfer debugging.

A future balance review could expand the named scenario matrix with observed campaign telemetry while retaining the same bounded MCP comparison contract and without turning willingness scores into claimed click probabilities.
