# Event 006 overlay registry continuation — 2026-08-25

## Scope and outcome

The two remaining small overlay families, IW-101/IW-102/IW-105 COG and IW-156/IW-196/IW-197/IW-204 final vanilla routes, now share the existing minor-overlay trigger, effect, and decision registries.

The six former parser files are removed:

- `common/scripted_triggers/006_independence_wave_iw101_iw102_iw105_cog_overlays_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw156_iw196_iw197_iw204_overlays_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw101_iw102_iw105_cog_overlays_effects.txt`
- `common/scripted_effects/006_independence_wave_iw156_iw196_iw197_iw204_overlays_effects.txt`
- `common/decisions/006_independence_wave_iw101_iw102_iw105_cog_overlays_decisions.txt`
- `common/decisions/006_independence_wave_iw156_iw196_iw197_iw204_overlays_decisions.txt`

Their executable bodies remain complete under source markers in:

- `common/scripted_triggers/006_independence_wave_minor_overlay_triggers_registry.txt`
- `common/scripted_effects/006_independence_wave_minor_overlay_effects_registry.txt`
- `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt`

The registries now cover thirteen adapter-only overlay packages in total. They still adapt living vanilla carriers and never create Event 006 origins.

## Validation

- The two former trigger files compare byte-for-byte after line-ending normalization inside the receiver, with 125 unique top-level trigger definitions and balanced braces.
- The two former effect files compare byte-for-byte after line-ending normalization inside the receiver, with 295 unique top-level effect definitions and balanced braces.
- The two former decision files compare byte-for-byte after line-ending normalization inside the receiver, with 13 unique top-level category definitions and balanced braces.
- No duplicate top-level trigger, effect, or decision-category identifier was found.
- The maintained Event 006 allocator audit passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, and the unchanged 32-attested/29-group boundary.
- The country API audit passed with 242 broad tags, 191 resolved carriers, no missing tags, no duplicates, and an IW-031 crosswalk pass.
- The SCN-008 scenario matrix, strict flag, FORM-16 contract, and Statehood Ledger semantic source-matrix audits passed.

## Boundary

This is a source-layout consolidation only. It does not widen central admission, change overlay identity or costs, alter on-actions, change package probabilities, add a pre-event category or crisis surface, or claim live parser/runtime evidence.
