# 107 Lootboxes source and decision receipt

## Scope and evidence boundary

This is the evidence and authority record for the completed planning package. The package develops the supplied Event 107 brief into a complete design, acceptance matrix, and separate production prompts. It does not report gameplay implementation, final asset production, native rendering, or live HOI4 execution.

The complete supplied Project Source set was read before substantive design work. Four readers covered 91 distinct text or configuration contents, represented by 133 supplied copies and 2,618,237 unique source bytes. Five archive extractions include the nested subagent archives. Differing older and current versions were fully read. Byte-identical copies were verified by SHA-256 instead of being misrepresented as different designs.

`107_lootboxes_source_coverage.json` preserves every supplied source copy, its hash, size, original location, reader, and complete read ranges. Line ranges are inclusive. Character ranges are half-open Unicode character ranges. The receipt includes the source-container identities and explains that source locations are provenance labels rather than files bundled into this ZIP.

The primary brief is `107 - Lootboxes(4).md`, SHA-256 `a821661f05ab62365fb1011941776b93c30a69af45329ed8543a6c56cbc71a23`. The latest supplied aggregate archive is `all-project-sources(20261010-064959).zip`. The complete distinct source inventory includes that archive, the older supplied source archive, standalone project sources, and all differing role definitions. The full-reading result is independent of the later targeted repository inspection.

## Authority and reconciliation

The user's explicit Event 107 brief and output requirements govern this package. Current supplied project instructions govern workflow and shared contracts where they do not conflict with that brief. Older differing sources remain part of the reading record. They do not silently override the current source contract. Later repository observations establish what was actually observed at one revision, rather than granting permission to redesign unrelated systems.

| Conflict or ambiguity | Selected planning treatment | Production consequence |
| --- | --- | --- |
| Brief calls this Event 107 Lootboxes, while inspected catalog snapshots associate 107 with Rule, 111 with Resistance, 112 with Lootboxes, and 114 with Fuel Crisis | Use the requested Event 107 identity throughout this planning package | Reconcile the current canonical workbook and real owners before implementation. Do not overwrite an unrelated row or assume the snapshot labels are safe migration instructions |
| Brief references Fuel Crisis as 109, while inspected catalog identity differs | Preserve the brief's intended Fuel Crisis connection as a system relationship | Resolve its actual current id and owner before wiring. Do not invent a new Fuel Crisis implementation |
| Exact 50 PP purchase versus shared dynamic cost guidance | The exact user price remains authoritative | Use a verified fixed-price route and preserve applicable payment/neutral-receipt conventions |
| Older asset paths and conversion guidance versus current supplied asset skill | Use the current reference root, conversion tool, dimensions, and native format requirements | Do not revive an older helper path merely because it appeared in a previously supplied source |
| General recurring-host patterns versus current restrictions on broad polling | Use event-owned bounded callbacks and supported native AI opportunities | No new generic all-country periodic loop without the user's explicit authorization |
| Project MCP evidence requirements versus the tool registry available here | Record the missing native routes and provide exact future usage maps | Planning can finish. Native implementation claims remain unavailable until the actual tools and game environment are used |
| Brief asks for a complete expanded design rather than implementation blueprints | Specify rules, outcomes, contracts, coverage, and measurable acceptance | Final supported syntax, identifiers, source fixtures, and localisation belong to implementation |

The canonical workbook is the editable catalog authority. Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and generate exports using the current exporter after actual implementation facts justify them. Neither the workbook nor any repository catalog was edited during this planning session.

## Fixed requirements and selected planning choices

The following distinction prevents an illustrative number from becoming an accidental user requirement.

| Area | Fixed by the supplied brief | Selected in this expanded plan |
| --- | --- | --- |
| Access | Standalone Minor event, fire once, permanent country access | One compact category with purchase and pending-box resumption behavior |
| Payment | Exactly 50 PP, free opening and resumption, one pending box | Fixed-price integration with fresh transaction evidence and duplicate protection |
| Opening | Large central animated chest, dimmed background, five meaningful accepted interactions, real frames and physical sounds | Explicit sealed, busy, accepted-stage, reveal, resume, and local-input rules |
| Rewards | All five rarities from first access, Common most frequent, Legendary rarest and strongest, Mythic second rarest, complete useful prizes | Concrete family eligibility and delivery contracts, component counts, qualified provider reuse, and capacity certification |
| Adaptation | Soft suppression of Common after poor results, no guaranteed pity or rarity sequence | Bounded 0 to 100 poor-result history, illustrative Common plus 2 and non-Common minus 3 updates, and a conditional non-Common split of 65:25:8:2 |
| Evolutions | Premium at 200+, Bonus Drops at 400+, Chaos Loot at 600+, subject to actual shared unlock and pacing | Automatic Premium incidence within the same purchase action, four visual shells, and a purchase-time reward snapshot |
| Influence | Hidden country influence driven chiefly by openings, independent of rarity, capable of becoming severe with only Common prizes | Separate lifetime history, recoverable burden, cadence, finite episode state, and temporary relief |
| Symptoms | Increasing national harm must coexist with genuine rewards | Four bounded working-label symptom families, one opening-level episode budget, at most one delayed opportunity, finite expiry, and no recurring punishment generated by inactivity |
| Recovery | Only the country's own meaningful actions that actually reduce global Chaos, no passive or foreign credit | A proposed source-specific actual-contribution receipt, bounded shares, causal anti-farming, and protection against banked or delayed retroactive credit |
| AI | Same cost, odds, rewards, and influence through a scripted resolver, no human chest window | Strategic PP reserve, urgent-commitment guard, public shortage inputs, and bounded purchase opportunities |
| Achievements | Challenging, event-specific achievement design and separate handoff | Four multi-condition routes covering defensive use, productive peace, genuine recovery, and rare-result restraint |

All probability percentages, burden bands, recovery conversion, episode timing, modifier magnitudes, AI reserves, and achievement thresholds are planning choices or tuning anchors. Their associated invariants are mandatory. Native balance may adjust the anchors while preserving the complete reward ladder, exact price, concealed influence, strategic AI, finite consequences, and credible recovery.

New descriptive names are working labels. The package does not supply final player-facing localisation. Existing titles retained from the brief are treated as supplied terminology.

## Repository evidence

Repository inspection was read-only and pinned to `klimPaskov/Chaos-Redux` at `a3ef485c5da7e2337122eca04ac65c175050f251`, the inspected `master` head with commit date 2026-10-06. Directory and search results narrow the investigation. They do not prove exhaustive absence across every repository file.

### The shared meter needs actual-applied contribution evidence

The inspected `add_chaos_meter_value` body rounds a requested delta, applies it, clamps the meter at zero, and later passes the requested delta to History. It does not return a measured actual-applied negative amount. Consequently, an initial value of 1 and a request of minus 3 can produce one point of real reduction while History records minus 3. A zero-floor request can appear negative in History without changing the meter. The planning consequence is a narrow actual-delta adapter around the authoritative mutation, before downstream callbacks. This is a proposed integration change, not an existing API. [Inspected writer](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaos_meter_effects.txt#L4514-L4618)

History can merge the latest compatible war row without creating a new sequence. Its actor rules suppress generic and specified world-state reasons, and its view is rebuilt according to sorting and filtering. It does not contain the full causal action identity, contributor allocation, or one-time recovery receipt required here. A History sequence may be a diagnostic link. A displayed row or mutable History scan cannot be the recovery authority. [History writer](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaos_meter_effects.txt#L4287-L4494)

### Attribution must follow each actual source

The inspected native hooks use different meanings for their country scope. Liberation identifies a liberator, subject freedom identifies the freed subject, and restoration can identify a beneficiary rather than the responsible actor. Monthly decay has no country contribution. These differences require source-specific contributor rules. They do not support granting recovery to every country mentioned in a negative History entry. [Native hooks](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/on_actions/chaosx_on_actions_chaos_meter.txt)

Event 009 suppresses ordinary peace callbacks while collecting a capped settlement batch. Its inspected pending-delta helper saves a primary actor and calls the writer without establishing a new immutable contributor allocation. Event 107 therefore needs one actual batch reduction, verified successful relations, causal provenance, and bounded contributor shares. Existing finite pair cooldowns do not supply this receipt. [Settlement batching](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/009_white_peace_effects.txt#L1027-L1148)

### Already peaceful countries need a verified nonwar route

The environmental bridge accumulates fractional contamination changes globally before converting whole units into Chaos. Provenance must survive that conversion so passive or foreign contributions cannot be credited to the last actor. The inspected treaty document describes a sponsor-owned Global Cleaning Day, but its listed scripted-effect owner returned 404 at the pinned revision. A successful listing of 415 scripted-effect entries showed no matching `air_cleanliness` owner. This is an unresolved owner dependency. It does not prove that no equivalent implementation exists elsewhere. [Environmental conversion](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaos_meter_effects.txt#L5089-L5227) [Treaty document](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/air_cleanliness/air_cleanliness_treaty.md#L65-L95)

The release design requires verified existing nonwar restorative paths for already peaceful recipients. It does not claim a universal current route from the inspected code. At zero Chaos or while the meter refuses a change, lasting recovery credit is zero. Finite symptoms still expire, so restoring ordinary national performance never requires buying again or manufacturing a conflict.

### Fixed price and qualified equipment reuse need deliberate integration

The current cost documentation defines composed quotes and neutral payment receipts. A zero eligibility mask means all cost families, so zero cannot be treated as an automatic opt-out. The exact 50 PP requirement needs a verified fixed-price route. No existing exclusion switch is assumed from documentation alone. [Current cost contract](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md)

Event 019's inspected registry offers provider and token resolution for established equipment, including the Coal Golem token. Its broader materialization chain also creates templates, units, and ledgers. Lootboxes may reuse a qualified pure equipment provider after proving eligibility. It must not call the entire soldier creation chain or bypass country and evolution requirements. [Provider resolution](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt#L4118-L4305)

## What the available checks establish

The source coverage check establishes full reading of the supplied Project Source set. Targeted GitHub reads establish the observations above at the pinned source revision. Independent review establishes documented planning findings and their disposition. Rational arithmetic establishes the internal behavior of the illustrative rarity formula across the tested finite grid.

Those checks do not establish native effect validity, resource-cap behavior, GUI input support, actual animation playback, physical sound playback, multiplayer isolation, save execution, technology applicability, or calibrated AI selection probability. `107_lootboxes_implementation_handoff.md` assigns those gates to concrete future owners and MCP routes. Part 6 provides stable acceptance scenario IDs and explicit pass conditions.

No gameplay repository file was changed. The user remains responsible for live HOI4 execution and any resulting game evidence. Planning completion does not change an event's implementation status to Playable.
