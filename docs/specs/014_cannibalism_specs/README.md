# Event 014 Cannibalism Source Specification

This directory holds the source design for Event 014, Cannibalism.
The event begins as a containable wartime military-predation crisis.
Failed containment, exploitation, cross-border spread, and high chaos can produce ritual cells, remote communes, eight reusable warlord countries, the public Hannibal Lecter unification, and ordinary or Wendigo terminal routes.

Current implementation status, provenance and open evidence gates live in one place, [package status](quality/package_status.md).
This README states the accepted scope, the package map, the authority order, the shared-system boundaries and the open design questions.

## Accepted scope

- Classification: Minor Fire-Once, outside every cluster.
- Origins: Island Host, Siege Commune and March Host only; Prison Host is rejected as an origin, package, portrait slot, route, scenario type, GUI surface or super-event identity.
- Focus trees: 68 local warlord, 108 unified, 28 Wendigo overlay.
- Warlord countries: eight origin-agnostic reusable slots, CBA through CBH, each with seven regional name and portrait variants, for 56 distinct fictional regional HOI4-style finals.
  The parent accepted native ImageGen for these invented male human identities within the user-authorized implementation scope; the requirement is not simplified.
- AI: two country scorers, two decision-weight MTTH entries, six unified targeted-decision consumers, and separate pre-lock and post-lock Wendigo profiles.
- Objectives: eight maintained mission families and seven added paid action families.
- Wendigo closure: paid-only Pack recruitment, bounded casualty receipts, complete-batch capacity checks, active-enemy epoch reset, inherited winter cells, structural Pack, origin and commander stages, and four terminal-hunt surfaces.
- Unification economy: Larder logistics with route loss and territorial capacity, and hidden hoards with their loyalty review, investigation and seizure (Part 7).
- Achievements: 18 real achievement definitions plus an 18-entry staged read-only tracker.
- Scenario: `SCN-010`, The Hunger Lines, with Discipline Collapse, Ritual Cells, Silent Islands, Warlord States and Convergence; a successful launch also starts the famine-owned Hunger Lines famine on its node states (Part 11).
- Event Details: two independent post-reveal terminal rows and toggles.
- Presentation: four action super-events with unique images and audio IDs 49, 50, 52 and 53, two protected leader portrait sheets rooted in the exact canonical `hannibal.dds` and `hannibal_wendigo.dds`, and one distinct icon per unified decision and mission.
- Units: nine inactive custom irregular-infantry/cavalry sub-units with stable gameplay identities, locked-template consumers and an additive CXT registration bus, and no new equipment archetype.
  Seven families have bespoke models; Bone Riders reuses vanilla `sprite = cavalry`, Network Cadre reuses vanilla `sprite = infantry`, and the Scavenged Elephant Column uses vanilla `elephantry`.
  Model production is closed at seven packages, and model inputs must begin from actual Internet-sourced or user-supplied modern artwork with only faithful ImageGen enhancement (2026-08-22 amendment).
- No Event 014 animation toggle or player animation preference exists.
- Runtime layout: the dedicated script, GUI and localisation loaders are consolidated into 23 merge-safe files, one per incompatible HOI4 loader schema.

## Package map

- `specs/` contains the twelve source specification parts.
- `matrices/` contains focus, decision, AI, country, idea, asset, super-event, world-reaction, state-machine, and secrecy maps.
- `focus_graphs/` contains Mermaid architecture diagrams retained as design history and route orientation.
- `research/` contains historical, cultural, and source-reading records.
- `prompts/` contains the original bounded implementation and audit prompts; each carries a historical build-contract banner and must not be re-run.
- `quality/` contains the current package status, definition-level validation evidence, the anti-spoiler review and the manual improvement-loop review.
- `PACKAGE_MANIFEST.md` lists every file with bytes, lines and SHA-256 over current bytes.

## Source-of-truth and supersession map

Accepted design comes from explicit user decisions or parent acceptance within the authorized scope, with the twelve spec parts recording the intended design.
File location, date, a status label or implementation does not establish approval.
Current implementation facts are read in this order:

1. Live gameplay, localisation, GFX, audio, and asset files.
2. [Agent decisions of 2026-10-04](../../plans/014_cannibalism_plans/agent_decisions_2026-10-04.md), taken under the user's full design authority for the takeover, and the [2026-10-03 continuation report](../../plans/014_cannibalism_plans/2026-10-03_continuation_report.md) with its receipt reconciliation and portrait reviews.
3. `docs/events/014_cannibalism/overview.md` for the canonical mechanic overview, with `larder_logistics.md`, `hidden_hoards.md`, `gui_data_contract.md`, `inheritance_storage_contract.md` and `helper_output_ownership.md` beside it.
4. Current asset manifests under `docs/assets/014_cannibalism/`.
5. The 2026-07-15 consolidation audits under `docs/plans/014_cannibalism_plans/audits/`, which are historical evidence for frozen tranches, not current full-package proof.

The two improvement addenda in `docs/plans/014_cannibalism_plans/improvement_loop/` are recorded implementation history; H-01, H-02, H-03, M-01, the constituent technology union and the unified decision icons are implemented within that frozen scope.
Their optional ideas A through C (cross-origin joint operations, recovery case files and inspection compacts) remain `unresolved`, unaccepted proposals rather than an implementation queue.
The 2026-07-11 `014_live_asset_gap_map.md` and `014_remaining_static_asset_ledger.md` are superseded production snapshots, while `014_flag_asset_frozen_ledger.md` and `014_gui_dimension_ledger.md` remain frozen contract records accounted for by the current asset manifests.
`event014_final_completion_audit_2026-07-13.md` is a historical pre-origin-removal checkpoint; its four-origin counts are not current evidence.

## Reveal and cultural boundary

Hannibal Lecter is public only after `cannibalism_reveal_complete`.
Before that flag, no player-facing event, evolution row, decision, focus, GUI, Event Details row, achievement tracker row, scenario, portrait, country identity, super-event, or audio presentation may expose his name, face, silhouette, command title, or a claim that one individual directs the network.

The accepted design forbids actor likenesses and living Indigenous ceremonial, sacred, tribal or authenticity framing.
The transformed route uses wholly invented Chaos Redux imagery.

## Shared-system boundaries

Part 9 is the single description of each link; this list only names the owners.

- Famine and migration (`docs/specs/famine_and_migration_system_specs/`, reworked on 10 October 2026): the famine system owns food stages, reserves, relief and refugee cohorts, and the Hunger Lines famine hook; Event 014 owns cells, nodes, Field Hunger, consumption and the Larder.
  States owned or controlled by Event 014 countries leave both humanitarian mechanics, and a capture by an Event 014 country sends front flight from the former owner's neighbouring states.
- Natural disasters (Event 013): Event 014 reads disaster shortage flags and its logistics completion credits the current recovery phase once through `cannibalism_apply_shared_relief_to_current_state`.
- Soviet camp famine: read as shortage evidence and relieved by the same bridge.
- Random Terror (Event 031): owns the cannibal clash incident and its atrocity Condemnation against Event 014 countries.
- Deaths, Chaos Meter, world threat, Event 10 Death, Event 2 Zombies, Event 7 Fury, CBRN and fallout: Part 9.

## Validation boundary

The package records definition-level and filesystem evidence, bounded regional art approval and scoped historical audits.
No current full-package or in-game completion is inferred; the open evidence gates and their owners are listed in [package status](quality/package_status.md).

## Open questions

Each item below is proposed (spec audit 2026-10-10), not accepted design, and needs parent or user acceptance before implementation.
None adds a public value, a decision or a meter.

### P-014-A. Field Hunger reads the shared famine stage

- Problem: `cannibalism_state_has_famine_pressure` reads only the Event 013 and Soviet camp famine flags, so a real famine committed by the famine and migration system adds no Field Hunger, no logistics delay and no host-selection weight.
  The Hunger Lines scenario therefore puts famine on the exact Event 014 node states without feeding the cannibal crisis it is named after.
- Proposal: owner Event 014, consumer side only.
  A state counts as shortage when `famine_food_stage_requires_mortality` holds (acute shortage or worse) and as severe shortage when `famine_food_stage` is at least `famine_food_stage.famine` or the state carries `famine_crisis_concealed`.
  The existing constants then apply unchanged: `weekly_shortage_hunger` (4), `weekly_severe_shortage_hunger` (3), `logistics_shortage_add_days` (14), `host_shortage_score` (25) and `state_shortage_score` (16).
- Consequences: the famine decisions (Release Food Stores, Import Food, Escort Relief, Airlift Relief) become real Event 014 counterplay because a lower stage removes the pressure, with no second relief payment.
  The famine system's Conceal Hunger gains a second cost, since hidden hunger feeds predation.
  Event 014 writes no famine value, so no feedback loop or double death count arises.
- Acceptance case: launch The Hunger Lines at Low and at Medium; Field Hunger rises by 4 and by 7 per pulse respectively on a host with a famine node, and falls back to the war baseline once famine relief lowers the stage below acute shortage.

### P-014-B. Survivor spread follows real refugee flight

- Problem: the survivor route (`cannibalism_spread_route.survivor`, strength 28, delay 35 days) picks `random_neighbor_state`, while the migration system already moves real survivor cohorts out of the same famine and front states.
  Part 3 promises "humane screening and relief, not indiscriminate closure" as counterplay, but neither migration choice affects the route.
- Proposal: owner Event 014, reading the migration registry only when a survivor spread is selected, bounded by `global.migration_cohort_count`.
  Prefer a destination state that is a live cohort destination (`global.migration_cohort_destinations`) from the source node state (`global.migration_cohort_origins`), falling back to the current neighbour pick.
  A destination country with `migration_medical_reception_active` (Screen Incoming Civilians) halves the queued node strength; a closed border (`migration_reception_policy` at `migration_border_policy.closed`) delays arrival but does not cancel it.
- Consequences: one migration decision becomes Event 014 counterplay and border closure stays a weaker blunt tool, which matches Part 3.
  No new decision, value or periodic scan is added.

### P-014-C. Exposed feeding programs draw real Condemnation

- Problem: `cannibalism_expose_detention_exploitation_in_current_country` sets `cannibalism_feeding_program_exposed` and `cannibalism_feeding_program_exposed_abroad`, but no rule reads either flag, and Event 014 calls no Condemnation source although Parts 2 and 9 promise condemnation for exposed exploitation.
- Proposal: owner Event 014 as caller, the Condemnation system as owner of scaling, history and sanctions.
  The exposure transaction calls `condemnation_add_source` once per exposure with `condemnation_source.atrocity`, `condemnation_visibility.discovered`, `condemnation_severity.major` and the recorded prisoner-feeding civilian deaths, following the Event 031 caller pattern in `random_terror_add_condemnation_source`.
  The two inert flags are then either consumed as the once-only guard or removed.
- Consequences: the exploitation route keeps its battlefield value but now carries the sanctions and inspection pressure the rest of the mod uses for atrocities.

## Changelog

- 2026-10-10 spec audit (Pass 1 and Pass 2).
  - README rewritten around accepted scope, authority, shared-system boundaries and open questions; implementation status, portrait and model provenance moved to the single status record in `quality/package_status.md`.
  - Removed six copies of the 2026-10-03 portrait checkpoint and the duplicated GFX-mapping paragraph from the matrices, validation file and README; git history keeps the original wording.
  - `quality/package_status.md` now records the 2026-10-04 and 2026-10-05 implementation (Larder logistics, hidden hoards, network dossier, command-window pages, March raid, caller-owned outputs), the current 138 decision textures and 41 unified icons, and one list of open evidence gates; the stale claim that GUI information and Larder scaling were missing is removed.
  - Part 9 documents the current shortage inputs, the famine and migration ownership boundary after the 10 October rework, the implemented relief bridge, the Hunger Lines hook contract, the unread exposure flags and the Event 031 cannibal clash.
  - Part 11 names `SCN-010` The Hunger Lines and records its famine hook; Part 12 adds the matching acceptance lines.
  - Part 2 defers the header contents to Part 6 and the implemented `cannibalism_early_header_window`, dropping three extra header values; Part 6 clarifies the static fallback wording and the famine relief boundary.
  - Prompts carry a historical build-contract banner, the asset prompt's skill link points to `.claude/skills/`, and the source-reading manifest records the resolved catalog conflict.
  - Added proposals P-014-A to P-014-C under Open questions.
