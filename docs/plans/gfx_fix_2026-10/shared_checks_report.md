# Shared sprites: tooling and diagnostic handoff

The shared commands live in `.tools/gfx/` with a README and 20 focused tests.
The requested batch defringe/despill, alpha, slot/margin, unit-counter and canonical BGRA DDS commands are implemented.
The mechanical writer imports the asset skill's canonical writer, checks the complete one-level legacy header and exact payload, verifies decoded pixel equality and installs outputs without clobbering an unapproved competing writer.
All 20 tests passed, including native counter references, field/noise detection, frame separation, spill-mask bounds and report/output collision protection.
The independent Luna audit covered the first 18 tests; the parent added counter-CLI frame metadata, stock counter margins and the speckle-field regression.

`alpha_audit_before.json` and `alpha_audit_after.json` contain the requested per-frame check for 407 registered entries across TNC/Ukraine, camp glyphs/tabs, deselected mapmodes and the shared small-unit sets.
There are 195 warning entries after the pass, with no decode/path failures.
The warning is literally mean below 200 on nonzero-alpha subject pixels, not proof that every warned icon is defective.
The exact vanilla infantry silhouettes themselves average 162.254 (large) and 164.212 (small) because of antialiasing, while disabled/hover consumers can intentionally use low opacity.
The counter command therefore uses the supplied exact vanilla reference for opacity/palette comparisons and coherent NATO-field triage, leaving the separate literal alpha check unchanged.

`shared_counter_checks.json` checks 177 shared counter aliases and flags 148 for convention review.
It checks both frames, canvas, opacity/palette, distinct states, pale/black structure and a coherent field comparable to the reference; it cannot establish the correct unit subject, glyph semantics, complete border or line weight without visual review.
The small-counter margin default is zero because the inspected stock NATO frame fills the top and bottom of its 30x12 frame.

`shared_matte_checks.json` records all four shared transparency/matte findings from the plan.
The opaque coal-golem rectangle and faint Livens overlay cannot supply a safe opaque cut-out interior for this pass.
The hunger spirit's black matte and scientist trait's painted white glow are not chroma rims and require source/art review.
The Livens hover overlay's intended partial opacity is also a consumer-specific exception to the generic alpha warning.
No unrelated shared artwork was automatically keyed, made opaque, repainted or rescaled.

The canonical slot profiles and their verified override arguments are documented in the README.
Full source/pixel inventory evidence and original hashes are in `cross_cutting_inventory.json` and `inventory_report.md`; installed family reports and output hashes are in `005_report.md`, `015_report.md` and `repair_candidates.json`.
The five requested command families are complete; diagnostic warnings and pending art exceptions are not silently claimed as completed artwork.

## Orchestrator live checks

No shared unit, camp or mapmode art was replaced in this tranche, so their findings need the owning asset sessions.
On a paused 1936 USA fixture, compare the stock infantry counter in the division designer, on-map small view and NATO setting to the inspected reference DDS files, confirming the expected green/white normal states and pale NATO field with black glyph.
For a warned custom counter, capture both normal and NATO views for its asset owner; an automated pass alone does not prove a readable correct glyph.
Use `alpha --list <owned_paths.json> --json <report.json>` and `counter <owned_strip.dds> --surface <large|small> --reference <exact_vanilla.dds>` after each owner's replacement.
