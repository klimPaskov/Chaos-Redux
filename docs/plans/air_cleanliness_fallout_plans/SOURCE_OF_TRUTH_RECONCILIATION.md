# Source of Truth Reconciliation

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Authority order

Use the following precedence when two sources disagree:

1. The latest direct user constraints in the continuation prompt.
2. The accepted source specifications under `docs/specs/air_cleanliness_fallout_specs/`.
3. Resolved implementation decisions, proofs, and current status under `docs/plans/air_cleanliness_fallout_plans/`.
4. Live repository behavior as evidence of what currently exists.
5. Earlier archives and uploaded Air Cleanliness documents as historical design context.

Live code does not silently override accepted design. A difference between code and design becomes an implementation task or an explicit parent decision.

## System identity and path ownership

Air Cleanliness and Fallout are an unnumbered global system package. Fallout is a terminal world rewrite and a manual scenario, not ordinary a numbered random event content.

Canonical working paths use the system slug:

- `docs/specs/air_cleanliness_fallout_specs/` for accepted system specifications
- `docs/plans/air_cleanliness_fallout_plans/` for implementation plans, audits, and handoffs
- system-owned asset folders named for `fallout_world_end` and `air_cleanliness`
- `events/fallout_world_end_events.txt` as the only Fallout event-definition file
- `chaosx.fallout` as the dedicated Fallout event namespace

Fallout has no numbered random-event identity and no ownership relationship with another feature package. Remove stale event definitions, callers, sprites, and asset paths instead of retaining compatibility shims in another namespace.

## Reconciled design decisions

### Fallout trigger eligibility

Accepted rule:

- Fallout may become eligible after Air Contamination reaches or exceeds 100 percent.
- A scripted terminal event may request Fallout immediately.
- The manual Fallout scenario may request Fallout after its seven-day strike interval.
- Fallout does not require Chaos above 1000.

Implementation interpretation:

- `100 percent` is the eligibility threshold for the normal contamination route.
- Eligibility does not have to mean guaranteed immediate transition.
- Risk can rise with contamination, state exposure, persistent winter depth, nuclear use, and other terminal causes.
- A direct scripted caller can bypass the gradual risk model.
- A guaranteed upper contamination threshold may remain as a tuning safety rail, but it is not the sole trigger.

### Fallout presentation

Accepted rule:

- Fallout is not a normal super-event.
- No super-event slot, quote, normal super-event option, shared audio id, borrowed asset, or borrowed path is used.
- Dedicated Fallout audio still plays during the blackout and follows the existing super-event audio preference.
- The screen becomes black.
- Centered text appears one sentence or beat at a time.
- The world rewrite occurs while control is withheld.

Implementation interpretation:

- Delete the old Fallout event block from `events/chemical_warfare_events.txt`.
- Add the complete Fallout chain to `events/fallout_world_end_events.txt` under `chaosx.fallout`.
- Migrate Air Contamination and scripted terminal callers directly to the Fallout request helper or a Fallout-owned entry event.
- A dedicated independent scripted GUI and a scripted transition state machine own the presentation.
- The GUI has no close button during processing.
- The transition ends only after world rewrite validation and player continuation are complete.

### Winter model

Accepted rule:

- Winter phases are state based.
- Phases are visible in a new mapmode.
- Phases affect population, buildings, supply, state categories, and decisions.
- Winter includes flavour events with actual effects.

Implementation interpretation:

- The live persistent state model owns phases 0 through 6, exposure, recovery, adaptation, food, shelter, reclamation, water, refugee, disease, and damage ledgers.
- The existing monthly contamination host pass is extended instead of adding another world-wide monthly pass.
- Population loss uses the shared Chaos Meter Deaths pipeline.
- Building and state-category damage use bounded, persistent exposure logic.
- State phase, exposure, recovery, and adaptation are kept distinct.

### Treaty layer

Accepted source design includes an Air Cleanliness Treaty at severe contamination. The live monthly host now calls one treaty coordinator around the existing state pass. It initializes the bounded member, violator, active-donor, active-inspector, and relief-route ledgers, removes invalid routes before winter pressure, resolves founder succession, issues retry-safe generation-bound invitations on a quarterly cadence, and maintains sanctions only on membership or violation edges. Fallout silently ends operational projects while preserving treaty memory.

Decision for implementation planning:

- Keep the treaty layer active through the bounded coordinator.
- Use array-backed membership and explicit entry, exit, violation, donor-project, annexation, Fallout-pause, and route cleanup receipts.
- Use Global Cleaning Day as a paid global cleanup project.
- Use Joint Filter Convoy as a paid state-targeted project that creates a temporary Air Winter relief route.
- Keep evacuation corridors, Fallout-era successor memory, relief votes, major-burner policy, and the broader treaty event families as incomplete work.
- Treat inspection refusal as a distinct accepted member violation that reuses expulsion, treaty-owned embargoes, opinion penalties, and relief-loss consequences without claiming weapon use.
- Do not restore broad repeated country-to-country opinion or embargo loops.

### Successor countries

Accepted rule:

- Many successor identities use existing base tags, releasables, dynamic civil-war tags, and cosmetic tags.
- The 99-row matrix is a candidate pool.
- It is not a requirement to spawn every candidate at once.
- Every active survivor receives non-generic focus content.

Implementation interpretation:

- No base tag is repurposed until its current package and event ownership are recorded.
- Cosmetic tags provide visible identity without requiring a unique base tag for every identity.
- Dynamic tags are used only after pool capacity and crash risk are verified.
- Country packages are implemented and audited in regional batches.

### Focus architecture

Accepted rule:

- Every selected country uses an archetype skeleton, regional overlay, and country memory overlay.
- Each country is manually customized.

Implementation interpretation:

- The three layers are design composition layers.
- Engine implementation uses either verified shared-focus composition or a compiled reviewed full tree.
- Each active tree contains at least one unique country-memory branch with its own gameplay consequences.
- A pair of token focuses does not satisfy the country-memory requirement.

### Mutant identities

Accepted rule:

- Mutant countries are fictional high-chaos content.
- They must not be represented as real radiation science.

Implementation interpretation:

- Mutant routes use explicit fictional presentation and high-chaos gates.
- Research notes and implementation docs distinguish real fallout effects from invented mutation content.
- Real-world public health or genetics claims are not used to justify fictional outcomes.

## Live-code conflicts and dispositions

| Surface | Live state | Accepted state | Required action |
| --- | --- | --- | --- |
| Fallout event ownership | Fallout definitions live in `events/fallout_world_end_events.txt` under `chaosx.fallout`, and the stale non-Fallout block is absent | every Fallout event uses the dedicated file and namespace | keep future Fallout definitions, callers, assets, and audio inside the dedicated ownership boundary |
| Fallout threshold | the normal Air Contamination route can request Fallout at 100 percent, and terminal callers use the same idempotent coordinator | eligibility begins at 100 percent and direct scripted callers exist | retain the request receipts and do not restore a Chaos-above-1000 requirement |
| Winter | persistent phases 0 through 6 drive state ledgers, consequences, mapmodes, ordinary-map visuals, responses, and a reviewed event pilot | persistent state phases and phase-specific effects | finish the remaining treaty and event work while preserving the single monthly host |
| Treaty | one host-owned bounded lifecycle, paid cleanup project, paid filter convoy, paid verification mission, founder succession, cause-aware violation sanctions, annex cleanup, pre-pressure route reconciliation, exact donor and inspector cleanup, and silent Fallout pause | active severe-contamination diplomacy and mitigation layer | expand evacuation, relief votes, major-burner policy, direct successor memory, and manually reviewed treaty event families |
| Air docs | current system docs describe the live partial implementation and identify remaining work | must describe live and accepted implementation | update the current system docs and proof index after each reviewed tranche |
| Scenario registry | the writable checkout reaches SCN-013 while raw id 12 remains separately reserved | Fallout must use the next id after the highest live assignment | SCN-014 is reserved in Fallout-owned constants without renumbering existing ids, and public activation waits for the sweep gate |
| Mapmode strip | the selected and deselected strips are 380 by 18 with 19 exact 20-pixel frames | Deaths owns slot 18, contaminated states owns slot 19, and Air Winter uses dedicated per-mode sprites | resolved in `AIR_WINTER_MAPMODE_ICON_PROOF.md` without changing an asset |
| Province sweep | 41 dormant batches expand the installed map into 10,154 native province calls | every valid province receives a thermonuclear strike before the seven-day clock | static route and ledger proven, with native acceptance and callback load retained as runtime blockers |

## Documentation disposition

Accepted Ash-week orientation disposition:

- The user approved `FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` on 2026-07-18.
- Its accepted sequence, identifier roles, delays, deterministic outcomes, parity, recovery, registry refusal, six-asset requirement, and non-activation rules are incorporated into `specs/01_living_world_event_ecosystem.md`, `specs/03_fallout_timeline_and_campaign_pacing.md`, and `specs/12_event_content_budget_and_acceptance.md`.
- Suffixes `62` through `84` are reserved for the accepted package.
- Four matching event blocks at `62` through `65`, their localisation, all six dedicated assets, and sprite registrations are implemented. The nineteen remaining blocks, caller, log and detail rows, manual coverage rows, and registry-backed late components are not implemented.
- Both scheduler activation flags remain unset and the living-world count remains 0 of 660.
- The caller remains blocked until successor allocation, player continuation, and all required candidate registries are proven.

Current implementation authority:

- `docs/systems/air_contamination_mechanic.md` describes the live Air Contamination system.
- `docs/air_cleanliness_winter.md` describes the live Air Winter implementation and its reported gaps.
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md` records the overall partial status and hard blockers.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md` owns Fallout file, namespace, asset, and audio boundaries.

Historical notes remain evidence only when they conflict with those current sources. Any remaining world-end overview that states every ending requires Chaos above 1000 or every ending uses an ordinary super-event must identify Fallout as the dedicated exception. Scenario documentation may name SCN-014 only as a reserved identity until the exact native sweep release gate passes.

Do not erase historical source material. Mark superseded notes where needed and keep one current implementation document per system.

## Promotion rule

The expanded source pack is a system specification package, not an ordinary numbered event specification. When added to the repository, use the unnumbered system area. This implementation package belongs under:

`docs/plans/air_cleanliness_fallout_plans/`

Accepted implementation facts should be promoted into current system documentation after code exists. Working blockers, audits, migration notes, and tranche handoffs remain in the plans folder.
