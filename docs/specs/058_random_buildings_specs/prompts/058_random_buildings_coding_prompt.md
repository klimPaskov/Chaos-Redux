# Event 58 implementation prompt

Implement Event 58, Random Buildings, in the Chaos Redux repository as a complete Minor Repeatable event.

## Accepted source design

Read and treat every file under `docs/specs/058_random_buildings_specs/` as acceptance criteria. Read all Event 58 plans and handoffs under `docs/plans/058_random_buildings_plans/` and record whether each is implemented, promoted, queued, rejected, superseded, or blocked.

Before editing, read `AGENTS.md`, the required offline Paradox wiki pages, relevant installed vanilla documentation, and the current project skills for events, event planning, decisions and missions, assets, subagents, improvement loops, achievements where documented, and any exact engine surface touched. Inspect at least one current Chaos Redux event pattern and one installed vanilla precedent for every nontrivial engine operation.

Use `chaosx_repo_explorer` first because the live repository file map, existing building registries, map helpers, camp APIs, facility APIs, achievement patterns, and event-log identifiers are not known from the planning environment. Give it a context-complete prompt and keep it read-only.

## Core event contract

Keep the canonical entry event `chaosx.nr58.1` and register ID `58` as Minor Repeatable, Chaos level `1`, Positive Economy cluster member, Medium severity.

A successful firing is one bounded global transaction. Freeze the set of loaded land states for the transaction, process each state independently, and revalidate before every placement. Do not add a recurring `on_daily`, `on_weekly`, `on_monthly`, or equivalent whole-world scan.

Process active layers in this order:

1. baseline ordinary state construction
2. Evolution I expanded state construction at `200+`
3. Evolution II provincial construction at `400+`
4. Evolution III exceptional construction at `600+`

Each enabled higher layer adds to every lower active layer. It never replaces an earlier result. A state may receive no result in one layer when its valid candidate pool is exhausted. Do not substitute a different construction family merely to guarantee a grant.

Run a global preflight after selection and before committing the event. If no active layer can produce any valid result anywhere, cancel without consuming repeatable weight, reducing its cap, changing the timer, recording a normal event-history firing, or registering Event 58 Chaos.

## Provider registry

Implement an owner-extensible Event 58 provider registry. Do not build one giant hardcoded switch inside the entry event.

Each provider needs a stable ID, owning system, layer, risk band, base weight, global availability, state or province validation, capacity validation, placement callback, owner initialization callback, responsibility rules, uniqueness rules, display family, and cleanup expectations. A malformed or incomplete provider fails closed and cannot enter selection.

Event 58 owns selection and transaction accounting. The provider owner keeps the building or facility's normal mechanics, lifecycle, map entity, evidence, condemnation, population effects, decisions, removal, and cleanup. Event 58 must call the complete owner adapter atomically. Prove callback readiness before mutation. A failed attempt may reroll only after proving that it left no partial structure or owner state. A provider that cannot guarantee this remains blocked. Do not place a visual or numeric shell of a special building.

Owner systems decide whether Event 58 can bypass technology. Technology bypass never bypasses DLC, map validity, capacity, uniqueness, mutually exclusive facility rules, or owner-system prerequisites that are required for a valid live instance. Receiving an event-owned structure through Event 58 must not mark that structure's source event as fired.

## Weighted selection

Select a risk band first, then select among valid candidates inside that band. If a selected band has no valid candidate, fall toward safer bands only. Never reroll upward into a rarer band. This prevents candidate exhaustion from making camps, reactors, or exceptional structures common.

Use centralized script constants for weights, caps, floors, count formulas, thresholds, and Chaos values. Apply the probability scenarios in `quality/058_random_buildings_probability_scenarios.md` as named acceptance cases.

Route every weighted surface through `chaosx_ai_probability_auditor`. Establish the baseline with `hoi4.probability_inspect` before source changes. After implementation, use the same named scenarios and `hoi4.probability_compare`. The auditor remains read-only. Do not claim exact normalized odds when the candidate pool or external provider state is incomplete.

## Baseline and Evolution I

Implement the families and risk envelopes defined in Parts 2 and 4 of the spec. Ordinary baseline construction should dominate. Infrastructure, air bases, anti-air, radar, and fuel silos should appear regularly. Civilian factories, military factories, and valid coastal dockyards should be meaningful but controlled. Synthetic refineries and owner-approved strategic structures remain uncommon. Concentration camps remain a tightly limited restricted result and must enter the camp system through its owner adapter.

Evolution I performs a second state-building roll. Advanced structures remain a minority, rare structures remain rare, and extreme structures such as extermination camps remain exceptionally uncommon. Nuclear, civilian-nuclear, heavy-water, electrical-grid, stronghold, gulag, camp, and other owner-built providers use their real capacity and lifecycle rules.

## Evolution II province packages

Use the state as the selection scope and real provinces as the construction targets.

Land-fort results should add one level to every relevant foreign-border province in the state that is valid and has room. Coastal-fort results should cover every relevant sea-facing province that is valid and has room. Naval-base results should upgrade a suitable existing base or use a verified valid coastal province. Railway results should upgrade a useful existing segment or build a short verified connection through the state. Supply-hub results require strict geographic and logistics validation and may include only the bounded connector work accepted by the spec.

Use HOI4 MCP map inspection and rewrite tools for connected province, state, adjacency, railway, supply, and coastal evidence. Do not replace an unsupported railway or supply-hub operation with infrastructure. Block the provider and report the exact engine limitation when the accepted operation cannot be implemented safely.

## Evolution III exceptional construction

Build a global set of valid exceptional provider-location pairs. Select a limited number according to the accepted dynamic count formula and caps. Revalidate before placement. Do not place two exceptional results in one state during the same firing. Do not fall back to an ordinary building when no exceptional candidate remains.

Dams, special-project facilities, landmarks, state-modifier structures, and unusual event-owned structures must use exact location rules and complete owner initialization. A provider with no exact safe placement contract remains blocked.

## Event, log, evolution, cluster, and Chaos wiring

Create the player report flow without one popup per state. Give each human player one compact report using the established multiplayer pattern. Report world totals, the active layers, exhausted-layer counts, the player's owned-state results, and a compact family summary. Do not retain an unbounded state-by-state persistent ledger.

Wire event names, debug names, history, Event Details, actor behavior, repeatable state, event toggles, cluster details, and every related scripted-localisation selector. This is a global event with no single responsible country. Do not display a misleading actor flag.

Log each evolution once when its layer first successfully contributes to a firing. Respect independent evolution enablement. A disabled layer must not place results, set its recorded flag, or gate lower layers.

Register Event 58 direct Chaos only on the accepted one-time concrete milestones. Preserve generic Chaos sources from wars, deaths, contamination, and other owner systems without duplication.

## Achievements and assets

Implement the three achievements in Part 5 with complete tracking, disqualifiers, localisation, icons, documentation, and runtime consumers. Ensure that cluster firing counts as a valid natural Event 58 route where specified and normal force-trigger testing does not unlock natural-firing achievements.

Use the asset prompt for one generated report image and the achievement prompt for three distinct achievement triplets. Use native transparency for achievement icons and the current event-art consumer rules for the report image. Preserve source evidence, final DDS files, manifests, sprite handoffs, and final wiring. Keep asset work within the accepted inventory.

## Localisation and documentation

Write final in-world localisation from the direction in the spec. Keep the tone concrete and dry. Describe the visible construction wave and its consequences. Do not expose internal probabilities, risk bands, provider IDs, tuning history, implementation notes, or future hidden candidates.

Update Event 58 documentation, the event log and Event Details wording, achievement descriptions, asset crosswalk, and all other required player-facing surfaces. Replace the stale ID 58 identity `The Industrial Complex` with `Random Buildings` on Event 58 surfaces.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`. The exported Events row must match the accepted ID, name, type, status, Chaos level, cluster, role, details, evolution summaries, achievement summary, and final player-facing wording. Update Positive Economy cluster membership and availability fields only from verified final implementation facts.

## Required specialist passes

Use the supplied context-complete prompts for:

- registry architecture
- probability audit
- report and achievement assets
- localisation audit
- workbook update
- near-completion improvement review
- final completion audit

Use the HOI4 MCP event tools before and after the event-chain change. Use map tools for every province package. Record exact blockers when an MCP route is unavailable. Source-only review is not equivalent evidence.

## Completion standard

Do not use a placeholder, generic fallback, silent reduction, partial owner callback, arbitrary province, hardcoded future-provider switch, recurring global scan, or per-state popup flood.

Before claiming completion, resolve every acceptance row in `quality/058_random_buildings_acceptance_matrix.md`, every probability scenario, every asset row, every achievement, every workbook field, and every accepted plan or handoff. Produce a concrete completion report listing files changed, identifiers, implemented layers, provider coverage, map evidence, probability comparison, assets, achievements, documentation, workbook export, meaningful validation, and every remaining blocker or simplification. State explicitly when there are no simplifications.
