# Event 35: Great Depression 2.0

## Overview

Event 35 is a Minor Repeatable, Chaos level 1, Low-severity member of the Negative Economy cluster.

The event targets one valid major or player country, including a non-major player, and rejects active depressions, special Chaos actors, nonhuman economies, incompatible crises, and countries without a usable civilian economy.

Independent firing uses `chaosx.nr35.1` and owns normal event pacing.

Event 34 collapse, financial contagion, worldwide conversion, and relapse use the reusable start-or-deepen contract and never consume normal pacing.

## Public crisis model

`great_depression_depression_severity` is the only persistent Event 35 number presented for direct player management.

Severity is bounded from 0 to 100 and is presented through scripted localisation with its current value, qualitative band, trend, next threshold, phase, leading causes, current doctrine, selected Depression Center, active objective, and relapse state.

Hidden pressure components describe unemployment, credit, freight, relief capacity, confidence, center conditions, exposure, and opening shocks without becoming additional public meters.

Threshold hysteresis prevents phase and band oscillation around boundary values.

The lifecycle moves through Panic and Contraction, Depression, Stabilization, and Recovery.

Maximum-severity, social, supplier, and national-breakdown consequences use receipt flags or receipt variables so that one crisis episode cannot apply the same maximum consequence repeatedly.

## Reusable crisis API

The public gateway is `great_depression_start_or_deepen` in `common/scripted_effects/035_great_depression_effects.txt`.

Callers supply a contract version, caller type, source event and episode, receipt id, pacing and history policy, severity input, evolution proof, and source-specific proof fields.

The contract fails closed when required evidence, source scopes, snapshots, relationship proofs, worldwide context, or relapse history is missing.

The supported callers are independent Event 35 firing, Event 34 collapse, financial-contagion conversion, worldwide-depression conversion, and relapse.

An active compatible crisis is deepened in place, while an inactive compatible country receives a new globally unique episode id and a fresh episode ledger.

The active-country registry is sparse and bounded, and the shared global-host daily hook evaluates only registered Event 35 countries and registered global-pressure rows.

## Event 34 inheritance

Event 34 freezes its collapse snapshot before removing boom-only bonuses and calls Event 35 for the same country.

The snapshot carries Event 34 evolution, final and peak Overheating, landing result, reserve state, completed projects, inherited regions, shock evidence, repeat history, and the collapse receipt.

Baseline maps to Event 35 baseline, Evolution I maps to Financial Contagion, Evolution II adds Social Collapse, and Evolution III adds The Second Great Depression with a very-high starting Severity profile.

If Event 35 is already active, the inherited collapse deepens the existing episode and does not add another depression modifier.

Event 34 retains the inherited-crash achievement `chaos_redux_034_the_long_fall`.

The public Event 35 report selects source-aware opening prose for the inherited hard landing, financial contagion, social collapse, worldwide contraction, relapse, and ordinary national paths while retaining the same Severity state readout.

## Recovery doctrines and decisions

The six recovery doctrines are Emergency Public Works, Rescue Strategic Industry, Stabilize Finance and Trade, Austerity and Retrenchment, Direct State Planning, and Let the Market Clear.

Each doctrine has its own mapped actions, AI preference profile, crisis legacy, and recovery tradeoffs.

The decision category contains 75 decisions and 15 missions.

Dynamic costs are calculated from the usable economy and grouped into doctrine, policy, center, freight, relief, credit, industrial, contagion, social, liquidation, and global-recovery families.

No action charges more than four resource types.

The custom cost contract contains matching normal, blocked, and tooltip localisation keys and debits the same political power, manpower, fuel, trains, convoys, support equipment, civilian-factory commitment, stability, or war support shown to the player.

The selected-center flow uses state targets, one occupied action slot, cooldowns, project receipts, state status validation, and cleanup on transfer or crisis closure.

Missions activate without an entry debit, require affordability at completion, and debit their displayed mapped action cost exactly once on successful completion. Cancellation and timeout do not create a second charge or refund an unspent cost.

The National Employment Guarantee cannot be started again while its automatic mission is active, and its bounded partial-timeout result is terminal for that episode so the partial relief cannot be farmed through repeated activation.

## Depression Centers

A normal episode selects one to three Depression Centers, bounded by the central registry cap.

The center ledger keeps aligned state, stage, project, loss receipt, factory baseline, project timing, owner, and Event 35 loss arrays.

Mapped center statuses include distressed, idled, shuttered, abandoned works, protected, public works active, reopened, and hollowed industrial district.

Mapped projects include emergency public works, strategic-industry rescue, credit clearing, austerity administration, state coordination, controlled liquidation, freight restoration, reopening, and center protection where their doctrine and state gates permit them.

Factory loss is delayed until sustained severe failure or a deliberate liquidation action.

Factory-loss receipts compare against the frozen center baseline, remain capped, and prevent duplicate physical losses.

State transfer revalidates ownership, removes invalid active projects, preserves applicable scars and legacies, and keeps the aligned registry coherent.

Repeat episodes retain bounded doctrine legacies and recovery scars while applying diminishing returns to repeated relief.

## National Breakdown and Social Collapse

Baseline National Breakdown opens only after sustained severe failure and runs through a warning, prevention mission, proof gate, and one recorded outcome in `chaosx.nr35.6`.

The baseline outcome always offers an emergency settlement and cabinet replacement. Its AI weights are `45` and `35`; the remaining `20` weight belongs to civil conflict only when the strict force, territory, leadership, capacity, shared-adapter, and recent-war gates succeed. The shared Event 21 civil-conflict adapter is fail-closed, and a rejected handoff resolves through the idempotent non-war emergency outcome.

Social Collapse adds organized actors, sector conflict, national unrest, government crisis, and revolutionary breakdown states.

Coup, separatist, and civil-conflict outcomes require distinct actor, severity, duration, stability, territorial, government, and shared-system gates.

The coup and regional-autonomy branches use `chaosx.nr35.4` and `chaosx.nr35.5`; failed extreme routes do not invent a fallback faction or civil war.

## Bounded incident pools

`common/scripted_effects/035_great_depression_incident_effects.txt` owns the ordinary incident clocks, state and partner selectors, complete candidate pools, receipt history, and qualitative application adapters.

The baseline pool contains factory gate closures, unpaid wages, freight yards idle, local credit cooperatives, municipal relief failure, successful reopening shifts, skilled workers leaving, unfinished works abandoned, regional aid requests, and war-orders revival.

The Financial Contagion pool contains correspondent failure, foreign-currency obligations, trade-credit withdrawal, bank holidays, debt conferences, rescue-loan failure, supplier concessions, capital flight, clearing blocs, coordinated rescue, and partner abandonment.

Social Collapse uses six stage-one families—local strike committee, unemployed march, plant-closure wage dispute, relief offices overwhelmed, veterans demanding employment, and regional council retrenchment refusal—followed by sector strike, factory occupation, coordinated layoff refusal, business lockout, relief demonstration, and security-force refusal at stage two.

Stage three adds general strike, nationwide factory occupation, hunger riots, mutiny or refusal, emergency cabinet collapse, and rival movements.

Stage four adds cabinet authority loss, recovery-program failure, army emergency powers, parallel administration, regional secession threat, and foreign-patron conditions on aid.

The final rung chooses among coup attempt, regional uprising, separatist conflict, full civil war, negotiated power transfer, emergency dictatorship, and revolutionary coalition, while retaining the existing strict political and Event 021 gates.

Only one due review runs for a registered active country during the weekly pulse. A candidate must retain a usable owned and controlled state or a proved contagion relationship, the last family is cooled down, the aligned receipt ledger has capacity, and a no-op branch defers the review when no candidate is valid.

Incident outcomes change the public Severity through the same clamped action path and expose only a qualitative current incident. Routine incidents do not delete factories or add Chaos; sustained center failure, deliberate liquidation, shared humanitarian pressure, and one-shot abnormal outcomes remain owned by their existing guarded systems.

## Financial Contagion

Financial Contagion activates only at Rising Chaos and spreads through proved relations such as faction, war, overlord, trade, guarantee, and neighboring economic links.

The sparse relationship ledger records source country, source episode, source receipt, qualitative exposure stage, and relationship type on the receiving country, with aligned target rows on the source.

Exposure is qualitative and bounded.

Partner actions can support, supervise, clear, supply, withdraw, contain, or convert a relationship according to the mapped target gates.

Provider support is counted once per globally unique source episode through a bounded receipt set, so one partner cannot farm a source while remaining able to support another valid episode.

Conversion calls the fail-closed API with the proved source and receipt and deepens an existing compatible crisis rather than duplicating it.

Event 34 suppliers enter through the supplier adapter and retain their own Overheating and contract-risk rules.

## The Second Great Depression

Evolution III activates one global lifecycle at Totalen Chaos.

Activation itself grants zero Chaos.

The first concrete bounded worldwide-pressure application emits one announcement, one super-event, and one guarded abnormal-outcome Chaos receipt.

Worldwide pressure is lighter than a national crisis and is tracked in a bounded registry of valid major or player economies.

Worldwide conversion uses the preserved global activation source, one globally unique conversion receipt, a conversion interval, a cursor, and the Event 35 fail-closed API.

International recovery requires material contributions from distinct countries, recipient improvement, sustained proof, and no final supplier collapse.

Supplier risk can reset recovery proof without replaying the worldwide shock or creating a second global episode.

The global lifecycle progresses through shock, contraction, coordination, recovery, international reconstruction, and retirement.

## Shared-system adapters and Chaos accounting

Event 35 uses owner adapters for humanitarian pressure, occupation, Deaths, Condemnation, environmental effects, event history, evolutions, clusters, Event 21 civil conflict, Event 34 suppliers, and the shared Chaos meter.

Evolution activation and lifecycle bookkeeping do not add Chaos.

Guarded Event 35 Chaos receipts are reserved for concrete abnormal outcomes such as maximum national failure, national breakdown, extreme social outcomes, civil conflict, worldwide pressure, supplier collapse, or corresponding recovery relief.

Global and local receipt totals are kept separately so that the event cannot duplicate shared sources or replay the same outcome.

## AI and weighted logic

AI doctrine and action behavior is split among relief coalition, strategic mobilizer, financial stabilizer, state coordinator, fiscal retrencher, and liquidation gambler profiles.

Affordability, urgency, wartime industry needs, financial pressure, center condition, partner safety, supplier Overheating, and locked-state gates modify action choices.

The baseline, Financial Contagion, Social Collapse stage, and final Social Collapse outcome pools use centralized common, uncommon, rare, major, severe, positive, and no-incident weights with target validation and last-family cooldowns.

Event choice weights are defined for the crisis report, coup response, and regional-autonomy response.

The named probability scenarios are defined in `docs/specs/035_great_depression_specs/035_great_depression_ai_probability_matrix.md`. The implementation report records the current evidence boundary: source and candidate-pool inspection succeeded, but the MCP transport closed before the required named evaluations, sweeps, sequence checks, and same-scenario comparison completed.

## Achievements

Event 35 owns six achievement contracts: Back to Work, Every Center Reopened, Containment Line, Social Peace, Lean but Standing, and Recovery of Nations.

Each contract is driven by durable proof written by Event 35 evaluators and is exposed through eligible, grey, and not-eligible assets. The contracts are grouped in the single root Chaos Redux achievement registry, which owns `unique_id = chaos_redux_achievements`.

Event 34's Long Fall remains owned by Event 34 but shares the Event 35 asset package and collapse proof.

## Presentation and asset wiring

`interface/035_great_depression.gfx` registers the decision category, every decision and mission sprite, condition and legacy sprites, center-status sprites, evolution sprites, and the seven achievement texture triplets. The achievement contracts are grouped in `common/achievements/chaos_redux_achievements.txt`, and `interface/035_great_depression_achievement_aliases.gfx` supplies the ID-aligned inherited Event 34 sprite names.

`interface/chaosx_pictures.gfx`, `interface/035_great_depression.gfx`, and `interface/chaosx_super_events.gfx` register the six scene images, category picture, and super-event image.

The complete 60-file icon inventory with source, processed, DDS, dimensions, alpha bounds, checksums, and runtime paths is stored in `docs/assets/035_great_depression/icon_manifest.json`. Together with six event/news images, the decision-category picture, and the super-event image, the Event 35 visual package contains 68 runtime DDS files.

The regular icon families are eight decision/category icons under `gfx/interface/decisions/035_great_depression/`, eight mission icons in the same folder, three evolution icons in the same folder, twelve condition and legacy icons under `gfx/interface/ideas/035_great_depression/`, and eight state-status icons under `gfx/interface/state_modifiers/035_great_depression/`.

The idea or national-spirit textures use the installed 60x68 `national_spirit_ideas_grid` canvas, and the three evolution textures are consumed by the existing event-log evolution-detail image bridge.

The complete per-file visual audit, source-to-runtime crosswalk, orphan scan, repair evidence, and current review disposition are in `docs/assets/035_great_depression/audit/asset_audit.md`.

The achievement family contains eligible, grey, and not-eligible files for each of the six Event 35 contracts and Event 34 Long Fall under `gfx/achievements/`.

The scene files are `report_event_great_depression.dds`, `report_event_great_depression_boom_collapse.dds`, `report_event_great_depression_contagion.dds`, `report_event_great_depression_social_collapse.dds`, `report_event_great_depression_recovery.dds`, and `news_event_great_depression.dds` under `gfx/event_pictures/035_great_depression/`, plus `decision_cat_picture_great_depression.dds` and `gfx/super_events/035_great_depression/super_event_great_depression.dds`.

The super-event uses visible slot `105`, playback ID `106`, the researched Roosevelt quote, the Keynes reaction, and the unique CC0 recording of Chopin's *Funeral March in C minor, Op. posth. 72 no. 2* performed by Aya Higuchi.

The runtime audio is `sound/035_great_depression/super_event_106_second_great_depression.wav`, while the source, processed OGG, rights evidence, and checksums remain under `docs/assets/035_great_depression/`.

## Localisation, logs, and catalog

`localisation/english/035_great_depression_l_english.yml` owns event, decision, mission, cost, status, evolution, achievement, news, and super-event text.

The seven achievement contracts expose the engine-facing `_NAME` and `_DESC` keys in the shared registry without unreferenced lower-case title or description aliases.

The shared event name map, event-log actor map, event-details content, evolution details, and cluster surfaces identify Event 35 consistently.

The catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Event 35 is recorded as Minor Repeatable, Chaos level 1, Negative Economy cluster member, and Low severity, and the three catalog CSVs are export-only derivatives.

## Test-country support

`chaosx_cxt_extension_event035_great_depression_apply` is the package-owned idempotent setup effect, and `chaosx_cxt_extension_event035_great_depression` is its matching modifier-free hidden-idea carrier.

`common/on_actions/035_great_depression_cxt_on_actions.txt` registers its hidden-idea carrier during startup and through the narrow `on_daily_CXT` fallback.

The setup exposes independent start, Event 34 handoff, contagion conversion, worldwide conversion, relapse, center, severity, social, global-recovery, and achievement proof scenarios without introducing a recurring world scan.

## Future plans and suggestions

Future depth can add more doctrine-specific event prose, more regional center descriptions, additional historically grounded supplier relationships, and country-specific AI preferences without changing the single public Severity contract.

Any future expansion should preserve the fail-closed caller proofs, aligned bounded registries, one-shot consequence receipts, owner adapters, and the separation between national crisis severity and lighter global pressure.

No dedicated scripted GUI is required by the current package; if one is introduced later, it must remain Event 35-owned and use the mandatory event UI worker and MCP visual workflow.
