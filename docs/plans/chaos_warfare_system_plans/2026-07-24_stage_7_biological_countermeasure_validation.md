# Stage 7 Biological Countermeasure Validation

Status: the bounded ordinary-pathogen countermeasure tranche is implemented and source-audited.

The overall Stage 7 plan and the full Chaos Warfare goal remain incomplete.

## Accepted boundaries

This tranche implements the surveillance, quarantine, field-hospital, antibiotic, vaccination, border-control, international-assistance, and containment-mission requirements in numbered specification 06 and the biological-agent countermeasure matrix.

Weapon potency is strictly `Tularemia < Anthrax < Plague < Smallpox`.

Only Smallpox is classified as the severe ordinary biological weapon.

The four strategic biological raids retain the same base delivery outcome factors: 0.50 success, 0.12 critical success, and 0.10 disaster.

Agent potency changes the lifecycle after a real release.

It does not change whether the delivery platform reaches its target.

After normalizing only the four agent names, the complete success, critical-success, and disaster factor blocks are byte-identical across all four raids and share SHA-256 `848218959be84707c89337190980832af3f3dfb1f767be9c265b889d96fc76eb`.

The internal 90/180/270/365-day containment bands measure the maximum current outbreak intensity in the selected state.

They do not classify Anthrax, Plague, or Tularemia as severe weapons.

Weaponized zombies remain outside the ordinary-pathogen project, treatment, payload, spread, and AI paths.

## Implemented source surfaces

- `common/script_constants/biological_countermeasure_constants.txt` centralizes costs, durations, capacity commitments, response values, treatment limits, AI factors, and containment outcomes.
- `common/scripted_triggers/biological_countermeasure_triggers.txt` owns national investments, exact-state eligibility, public agent-threat facts, bounded international access, treatment service state, and containment outcome gates.
- `common/scripted_effects/biological_countermeasure_effects.txt` owns equipment debit, capacity reservation and return, response activation, antibiotic courses, vaccination, international transparency, containment resolution, and exact-state cleanup.
- `events/biological_countermeasure_events.txt` owns a hidden self-scheduled cleanup job for countries with recorded biological border closures.
- `common/decisions/biowarfare_disease_containment_decisions.txt` owns 25 timed response actions and three immediate decision surfaces.
- `common/decisions/categories/biowarfare_disease_containment_categories.txt` keeps the response family discoverable while preserving ordinary-pathogen and zombie separation.
- `common/scripted_effects/biological_lifecycle_effects.txt` provides exact agent recovery, state response cleanup, public confirmed-use facts, and current modifier refresh.
- `common/ideas/cbw_ideas.txt` provides continuing surveillance, antibiotic production, and Smallpox vaccination programs.
- `common/dynamic_modifiers/biowarfare_state_modifiers.txt` exposes distinct detected-outbreak and quarantine effects.
- `interface/biological_countermeasures.gfx` registers the type-correct countermeasure sprites.
- `localisation/english/chaosx_decisions_l_english.yml`, `localisation/english/chaosx_ideas_l_english.yml`, and `localisation/english/chaosx_modifiers_l_english.yml` describe current costs, state effects, commitments, and failure behavior.
- `docs/biological_warfare/biological_countermeasures.md` documents the mechanic, ownership, assets, AI behavior, and future work.

## Costs and commitments

| Action | Immediate cost | Duration | Continuing or committed effect |
| --- | --- | --- | --- |
| Expand Medical Capacity | 50 Political Power, 120 Support Equipment, 40 Trucks | 90 days | Adds 20 Medical Capacity |
| Expand Biological Security | 50 Political Power, 80 CBRN Instruments, 80 Support Equipment | 90 days | Adds 20 Biological Security |
| Activate surveillance | 40 Political Power, 80 CBRN Instruments, 60 Support Equipment, 20 Trucks | 60 days | Commits 10 Medical Capacity and adds 25 Surveillance |
| Deploy field hospitals | 10 Political Power, 10 Command Power, 120 Support Equipment, 60 Trucks, 20 CBRN Instruments | 7 days | Commits 8 Medical Capacity to the exact state |
| Impose quarantine | 25 Political Power, 10 Command Power, 80 Support Equipment, 40 Trucks, 200 Infantry Equipment, 1,000 manpower, 1% Stability | 10 days | Applies exact-state quarantine |
| Dispatch antibiotics | 10 Political Power, 50 Support Equipment, 20 Trucks | 3 days | First state service commits 5 Medical Capacity |
| Start Smallpox vaccination | 150 Political Power, 250 Support Equipment, 100 Trucks, 50 CBRN Instruments | 180 days | Commits 10 Medical Capacity |
| Request international mission | 30 Political Power, 50 Support Equipment, 25 Trucks, 20 CBRN Instruments | 14 days | Commits 8 Medical Capacity to the exact state |
| Start containment mission | 35 Political Power, 15 Command Power, 150 Support Equipment, 75 Trucks, 40 CBRN Instruments | 90, 180, 270, or 365 days | Commits 10 Medical Capacity |

A continuing successful or partial containment result also consumes 75 Support Equipment, 30 Trucks, and 10 CBRN Instruments.

Every displayed tuning value is read from a script constant.

## Exact-state and cleanup proof

Field-hospital and international-mission commitments are reserved at dispatch, so parallel actions cannot spend the same Medical Capacity twice.

If either paid deployment loses exact-state eligibility before arrival, only its reserved Medical Capacity returns.

Political Power, Command Power, equipment, supplies, manpower, and Stability already spent are not refunded by failed actions.

Both deployments store the original provider and ordinary-outbreak cycle.

They cannot attach to a later episode after the original outbreak ends.

Quarantine orders store the same provider and cycle pair, without a refundable capacity reservation.

The first dispatched Anthrax, Plague, or Tularemia treatment course reserves one shared state service.

Later supported courses in the same state share that service without a second capacity debit.

Shared service reuse requires the recorded provider to equal the acting country.

The service remains reserved while any supported agent has an active or in-transit course.

When the last treated agent recovers, or when the last paid course cannot arrive, the exact recorded provider receives the reserved capacity and no Political Power or equipment refund.

Agent recovery clears only that agent's treatment course flags, counter, and cooldown.

Each in-transit course stores the original provider and exact matching agent episode count.

An expired order cannot apply to a newly seeded episode of the same agent.

Final state cleanup restores any remaining recorded commitments only after no ordinary episode remains.

Reopening the final exact bilateral border closure removes both relation-rule overrides and clears their registration flag.

The first closure starts one country-owned cleanup job.

The job checks only the recorded array, removes extinct or no-longer-adjacent targets, stops when no closure remains, and never runs through an all-country pulse.

The spread calculation checks both directions of the stored country pair without creating a global border proxy.

## International access and hidden information

International medical access uses active Condemnation inspection or observer arrangements, the engine's bounded allied-country scope, or the engine's bounded outward-guaranteed-country scope.

It does not scan every country, infer an inverse guarantee, fabricate a donor, or maintain a proxy relationship flag.

Emergency treatment availability uses exact local detection or an agent-specific global confirmed-use fact written at the real confirmed-use lifecycle transition.

It does not reveal a secret foreign project.

The doomsday batch writes the matching public fact only for agents with a positive consumed stockpile.

Smallpox vaccination uses the same public-information rule.

Confirmed deliberate attribution requires a deliberate or doomsday source.

International transparency may increase evidence and suspicion on an ordinary spread record, but it cannot convert spread or accident evidence into confirmed weapon use.

Public confirmed-use history is written independently from actor-owned penalties, so an actor that ceases to exist cannot erase the public historical fact.

## Agent-specific response

Anthrax, Plague, and Tularemia each have separate emergency development, continuing production, exact-state course counts, cooldowns, and diminishing treatment behavior.

Smallpox uses vaccination and never receives antibiotic protection.

The lifecycle retains the matrix's non-monotonic agent identities while preserving the overall potency ladder.

Tularemia keeps the strongest military-disruption identity, Anthrax the strongest persistent local burden, Plague the strongest rapid connected spread, and Smallpox the highest strategic catastrophe risk.

Only Smallpox receives the severe doomsday result.

## AI inspection

The installed current-version probability adapter classified 25 `days_remove` entries as mission AI surfaces and resolved all 25 without an unresolved input.

Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/083709e33aad5e0defd66a256ca92e7efafa03a8c566c889f24d8dab4cd37788/cf17a1a7c667279070151e6577cb976dd28313b9de00a339ea6fd15d30e88040/probability-inspect-b297960f0a90.json`

The same source produced three immediate decision AI surfaces and zero unresolved inputs.

Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d89c46f1162ad8a9cdf2c7089c34d02c4fa061349410dff89cd346f96a28b0c3/4df2b37ca7329dee2db2d4e3725623b1cf716907e89f19343048e4778be756e7/probability-inspect-b297960f0a90.json`

AI distinguishes Smallpox and Plague response urgency from delivery reliability.

Chinese emergency profiles prioritize surveillance, exact-state medical response, treatment, and transparent assistance.

Democratic profiles favor surveillance, vaccination, and international assistance.

Authoritarian profiles favor quarantine.

Low-industry profiles suppress expensive national programs.

## Asset evidence

The Stage 7 biological countermeasure package contains ten unique 32-by-32 decision icons and two unique 64-by-64 idea icons with source masters, processed PNGs, final DDS files, contact sheets, a manifest, and a GFX handoff.

The field-hospital and Smallpox decision surfaces reuse their existing type-correct sprites.

All twelve registered countermeasure DDS references resolve.

No file under `gfx/interface/military_raids/` was overwritten or replaced.

## Specialist audit disposition

The decision and mission specialist reported one obsolete lifecycle helper call, five broad country scans, a failed-arrival Medical Capacity leak, stale border-override registration, and an apparent documentation encoding issue.

The obsolete call now uses `bio_lifecycle_refresh_state_modifiers`.

All agent threat scans now use exact public confirmed-use facts.

International access now uses bounded engine relation scopes.

Failed antibiotic arrivals release capacity only when no supported service remains.

The final border pair now unregisters both overrides.

The documentation source contains a valid UTF-8 en dash.

The reported mojibake came from the shell display path rather than the stored text.

The scripted-system architecture audit also identified stale delayed orders, non-idempotent reservations, treatment-provider crossover, stale non-neighbor border pairs, evidence-only deliberate attribution, and shared Black Plague cleanup collisions.

Delayed responses now bind to the exact original provider and ordinary-outbreak cycle or agent episode count.

Field-hospital, international-mission, and containment reservations now use explicit committed markers, and every refund is gated by its matching marker.

Treatment service reuse now requires the stored provider to equal the acting country.

The country-owned border cleanup event removes invalid pairs without a broad pulse.

Attribution now requires an approved deliberate source before probable or confirmed attack status can be released.

Black Plague and ordinary-pathogen cleanup now preserve each other's independently owned hospital and quarantine state.

The timed antibiotic cooldown uses a file-local literal-compatible `@` token mirrored by the central script constant, following the current event-skill duration rule.

The final localisation audit found raw availability trigger output, incomplete sunk-cost disclosure, and overstated international access documentation.

Every remaining program, border, and stand-down gate now uses a localized custom availability tooltip.

Failed field-hospital, quarantine, antibiotic, and international deployments now enumerate the non-refundable Political Power, Command Power, equipment, supplies, manpower, and Stability that each action actually spends.

International access documentation now matches the implemented inspection, observer, allied-country, outward-guarantee, and Condemnation compliance gates.

The final architecture and decision audits found an unsafe in-loop border-array mutation, punitive controller-loss containment resolution, stale containment reservations, and paid actions that did not explicitly require an outbreak-cycle marker before debit.

Border cleanup now collects invalid entries in a temporary scope array before changing the persistent closure array.

Containment currentness now requires the recorded provider to retain control, and stale cycle or control records clear and refund the recorded capacity without applying success, partial success, or failure mutations.

Field-hospital, quarantine, international, and containment availability now requires the lifecycle's ordinary-outbreak cycle marker before any cost can be paid.

The localisation, scripted-system architecture, and decision/mission specialists re-audited those corrections and reported no unresolved defect in their bounded surfaces.

## Source scenarios

The bounded source review covered:

1. A field hospital and international mission dispatched in parallel cannot spend reserved Medical Capacity twice.
2. A paid medical deployment that loses exact state control returns capacity but not equipment.
3. Overlapping Anthrax and Plague treatment courses share one state service and release it only after the final active or pending service ends.
4. A course whose outbreak recovers during transit does not apply treatment, returns the otherwise unused capacity, and does not refund equipment.
5. Smallpox never qualifies for antibiotics and cannot inherit an ordinary-agent treatment flag.
6. A secret foreign biological project cannot unlock domestic treatment or vaccination.
7. A confirmed public use unlocks only the matching agent response.
8. Reopening one of several border pairs retains the relation overrides, while reopening the final pair removes them.
9. Full, partial, and failed containment outcomes mutate only active ordinary agents in the selected state.
10. Weapon strength changes post-release harm while all four strategic raids retain the same base delivery outcome factors.
11. A delayed field hospital, quarantine, or international mission from a completed outbreak cannot attach to a later outbreak cycle.
12. A delayed antibiotic course cannot attach to a later episode of the same agent.
13. Repeated reservation helper calls cannot debit field-hospital, international-mission, or containment capacity twice.
14. A treatment service reserved by another controller cannot be reused without transferring or refunding its recorded commitment.
15. A border target that ceases to exist or stops being adjacent is removed by the country-owned cleanup job.
16. Spread or accident evidence can become suspicious but cannot become probable or confirmed deliberate use.
17. Black Plague cleanup cannot clear an independently active ordinary-pathogen hospital or quarantine.
18. A doomsday batch unlocks only the countermeasures for agents whose stockpiles were actually consumed.
19. Final ordinary-pathogen lifecycle cleanup cannot clear an independently active Black Plague hospital or quarantine.
20. Multiple invalid border entries are collected before removal, so cleanup cannot skip a stale pair by mutating the array being iterated.
21. Containment controller loss or cycle mismatch clears the exact reservation and refunds its surviving provider without applying an outbreak outcome.
22. Field-hospital, quarantine, international, and containment actions cannot pay their costs without an ordinary-outbreak cycle marker.
23. Every decision availability block added or retained by this tranche presents a localized custom trigger tooltip.

These are source and adapter scenarios.

They do not substitute for the Stage 14 live package scenarios.

## Unresolved Stage 7 boundary

`events/biowarfare_events.txt` still contains legacy immediate `apply_*_contamination` callers and legacy MTTH research or spread paths.

`common/scripted_effects/biowarfare_effects.txt` still contains independent contamination calculations and idea-only treatment paths.

Every caller must be migrated to an exact lifecycle route and the legacy identifiers must then be removed.

No compatibility wrapper, proxy, or fallback is permitted.

Biological designers, the remaining country-specific program and AI coverage, final route integration, stockpile-safety closure, package scenarios, improvement-loop work, and final Stage 7 audits remain open.

This validation does not close Stage 7 or the full Chaos Warfare goal.
