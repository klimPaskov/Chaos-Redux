# Event 012 Gods participant roster capacity — 2026-09-26

Disposition: **implemented within the active user goal; campaign coverage and target-list presentation remain unverified**.

## Acceptance basis

The active user goal requires every valid major and player country to enroll independently while retaining a bounded participant registry. The prior source cap of 64 could silently stop enrollment before all eligible countries in a large campaign were considered; no accepted spec required a 64-country ceiling.

## Source correction

The current vanilla and Chaos Redux `common/country_tags/` files contain 609 distinct country-tag definitions. `gods_of_africa_timing.max_participants` is now 640, so every country tag currently defined by those two sources can fit if it satisfies the existing major/player and validity filters. The cap remains centralized in `common/script_constants/012_africa_gods_constants.txt` and must be raised if the installed tag set grows beyond 640.

The census remains the existing one-time Event 012 candidate pass in `common/scripted_effects/012_africa_world_order_effects.txt`; the change adds no recurring world scan, random selector, extra public value, or alternate participant-registration path. `gods_of_africa_initialize_registry` and the 90-day owner-local review still consume the maintained candidate/participant arrays.

## Evidence and remaining limits

The candidate count and all currently installed tag definitions were counted from the workspace and vanilla tag files. Source review confirms the census checks `gods_of_africa_candidate_count < constant:gods_of_africa_timing.max_participants` before registration. No campaign was run, so actual enumeration, late-player onboarding, and behavior when multiple human countries are present remain unverified.

Host target decisions draw from the expanded participant array. The ordinary decision panel has no dedicated scripted GUI or MCP row-layout route; decision-row density at the 640-participant ceiling remains a presentation review item. No row cap was added because that would again make eligible participants unselectable. Probability and campaign evidence remain separate; this roster-size change does not tune AI weights.
