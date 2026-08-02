# Fallout Laboratory Citizenship chain proof

## Scope

This proof covers the dormant ordinary Fallout chain Laboratory Citizenship. It does not claim that Fallout itself is an ordinary event, that the blackout is active, or that the Fallout-owned scheduler has been accepted by the live engine.

## Registry and identity

- Candidate id: `838`.
- Transaction key: `710091`.
- Route: `7214`.
- Event blocks: `chaosx.fallout.838` through `chaosx.fallout.844`.
- Event Log history: `9197`.
- Human opening, hidden AI opening, human result, hidden AI result, human callback, hidden AI callback, and cleanup use the seven event blocks in that order.
- The candidate is registered in `common/scripted_effects/fallout_consolidated_effects.txt` after candidate `831`.

## Candidate boundary

The candidate requires a current-generation East Asian Technate with Manchurian Reactor Keeps memory, a current state carrying the closed Failed Calculation memory, produced Air Winter and Supply Access receipts, surviving population and native infrastructure, a foreign neighbor, bounded Disease pressure, durable citizenship ledgers, and one affordable branch. It selects the lowest eligible owner-controlled industrial or arms state and uses the same Fallout ordinary-request envelope as the preceding reviewed chains.

## Deterministic chain

The opening freezes the country, state, owner, controller, generation, Air Winter values, Supply Access, and lowest authenticated foreign neighbor before payment. The four branches are Universal Rights, Service Tiers, Apprentice Path, and Strict Technocracy. The result is graded from the frozen state values and the citizenship ledgers after exactly `56` days. The callback runs after exactly `360` days and writes durable citizenship memory. Both stages apply bounded state and country effects, including Deaths requests on failure paths, then record authenticated Event Log payloads.

## AI and cleanup

The hidden AI branch scorer uses the same affordability checks, branch constants, ledger grade, delayed result, callback, and cleanup as the human path. Owner, controller, generation, target, neighbor, ticket, and request-token checks are repeated at every delayed boundary. Cleanup releases reservations and transient receipts idempotently and records cancellation only for a stale authenticated row.

## Localisation, Event Log, and assets

Opening, branch tooltips, all twelve result descriptions, callback descriptions, Event Log payloads, dynamic modifier names, and opinion modifier names are present in `localisation/english/fallout_consolidated_l_english.yml` with UTF-8 BOM encoding. Event Log detail and name routers are present in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. The dedicated sprite is `GFX_report_event_fallout_laboratory_citizenship`, backed by the DDS and manifest in `docs/assets/838_laboratory_citizenship/`.

## Validation boundary

Static inspection covered the owned event ids, localisation references, helper calls, dynamic modifiers, opinion modifiers, constants, braces, quote parity, and forbidden punctuation. Focused Event Inspector lint is the intended engine-facing review surface for `chaosx.fallout.838`. No HOI4 process was launched. Scheduler activation, host authority, save recovery, multiplayer delivery, live Event Log rendering, full-screen blackout integration, and exact engine-native world sweep remain outside this proof.
