# Event 016 remnant-hearing report-art wiring handoff

Date: 2026-08-02

## Scope

This bounded non-model tranche adds one dedicated aftermath report scene for the archive and surviving-remnant hearings. It replaces the generic research-lab picture only on Event 016's project-causal aftermath events; the qualifying-defeat news headline, project outcomes, decisions, ideas, and remnant receipts are unchanged.

## Runtime asset and consumers

| Runtime DDS | Sprite | Consumers |
| --- | --- | --- |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_aftermath_remnant.dds` | `GFX_report_event_016_brilliant_scientist_aftermath_remnant` | `chaosx.nr16.301`, `.303`, and `.310` through `.318` |

The source master remains in the ignored asset workspace under `docs/assets/016_brilliant_scientist/report_news_expansion/source_masters/aftermath/`. The processed preview and evidence DDS remain alongside it. The runtime DDS is `210x176` uncompressed 32-bit BGRA with the existing Event 016 report header contract and exact size `147968` bytes. It was reprocessed through the standard sepia report-card pipeline on 2026-08-02 so its transparent corners, tilt, shadow, and sepia channels match the accepted report contract.

## Presentation boundary

The scene shows inspectors, soldiers, surviving archives, sealed crates, and an intact machine component after the Kruger State or enclave has fallen. It is deliberately shared across the remnant-hearing family because the event descriptions already name the exact clone, machine, paleogenetic, xenobiological, portal, temporal, biological, alien, singularity, or prototype residue. Project-specific aftermath variants remain queued until they have distinct consumers rather than being substituted into unrelated outcomes.

## Ownership and validation

The parent owns `.gfx` registration, event picture assignment, documentation, and final checks. The scene was visually reviewed at native `210x176` size. The runtime DDS header was checked for width, height, uncompressed BGRA masks, 32-bit pixels, and exact payload length. Event Inspector coverage for `chaosx.nr16.301`, `.303`, and `.310` through `.318` returned no blockers in the focused report pass.
