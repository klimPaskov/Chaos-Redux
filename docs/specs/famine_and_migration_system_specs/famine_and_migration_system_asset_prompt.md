# Asset Prompt: Famine and Migration Mechanics

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, separate famine and migration asset consumers, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

Use `chaos-redux-event-assets` for all final visual work. Use `chaos-redux-frame-animation` only if later implementation evidence proves that a changing state needs motion. The accepted design uses static assets.

These are separate mechanics with no event IDs. Use a stable documentation/package folder such as `famine_and_migration_system` under the relevant asset category; that umbrella filename is not a runtime identifier and must not be emitted by gameplay, GUI, localisation, or sprite code.

## Required reading and reference inspection

Before production:

- read `AGENTS.md`
- read `chaos-redux-event-assets`
- inspect `assets/vanilla_reference/README.md` and `CATALOG.md`
- inspect the matching contact sheet for every asset type
- inspect the active vanilla or Chaos Redux sprite and GUI consumer
- inspect the decision category picture family at `assets/vanilla_reference/icons/decision_categories/pictures`
- create or update the picture-family contact sheet and catalog only if the local library is missing required reference evidence

Do not wire reference PNGs into runtime files.

## Asset inventory

Use `famine_and_migration_system_asset_matrix.csv` as the complete accepted inventory.

The package includes these families, with separate famine and migration category consumers:

- two decision category icons: `famine_category` and `migration_category`
- two static decision category pictures: `famine_category_picture` and `migration_category_picture`
- four distinct famine-stage state modifier icons: `famine_state_supply_strain`, `famine_state_acute_shortage`, `famine_state_famine`, and `famine_state_catastrophic_famine`
- five distinct migration state modifier icons: `migration_state_exodus`, `migration_state_reception`, `migration_state_overcrowded`, `migration_state_trapped_border`, and `migration_state_return`
- decision icons for `famine_decision_release_reserves`, `famine_decision_relief_convoy`, `famine_decision_airlift`, `famine_decision_evacuation`, `migration_decision_evacuate`, `migration_decision_open_border`, `migration_decision_close_border`, `migration_decision_quarantine`, `migration_decision_distribute`, `migration_decision_integrate`, and `migration_decision_return`
- report images for `report_event_famine_generic`, `report_event_famine_island_blockade`, `report_event_migration_wartime_evacuation`, `report_event_migration_closed_border`, `report_event_famine_relief_arrival`, `report_event_migration_nuclear_evacuation`, and `report_event_migration_return`
- `famine_deaths` and `migration_deaths_forced_displacement` Deaths reason icons or texticons only when the inspected Deaths UI has a valid consumer for them

## Source mode

### Gameplay icons

Use ImageGen through `chaosx_icon_artist`.

Every icon family needs:

- its own asset-type-specific prompt
- transparent unused canvas when the vanilla family uses transparency
- one centered readable subject
- strong silhouette at native size
- dark outline and subtle shadow where the reference family uses them
- no opaque square background
- no checkerboard pixels
- no white halo
- no generated text
- no resized substitute from another asset type

Famine-stage icons must show a clear visual escalation without graphic bodies. Use food, route, storage, ration, and infrastructure symbols.

Displacement icons must distinguish departure, reception, overcrowding, trapped movement, and return.

Decision icons must be designed for the inspected native decision size. Do not resize focus or idea art to satisfy them.

### Decision category picture

Use either a sourced archival image with clear rights and provenance or a generated 1936 to 1945 documentary-style scene.

Visual direction:

A wartime railway platform, border reception point, or relief station with civilians, luggage, relief staff, and transport. The picture should communicate movement and reception. It must not contain fake buttons, meters, labels, readable generated text, modern clothing, modern vehicles, modern barriers, or a map interface.

The picture is presentation only.

### Report images

Use generated period-documentary imagery for generic dynamic incidents unless a real historical photograph is required by the final text and has clear rights.

Requirements:

- period clothing, vehicles, architecture, transport, and photographic technology
- no modern objects
- no cinematic color grading
- no generated text
- no graphic injury or corpses
- no fabricated likeness of a real person
- no identifiable real victim unless using a sourced archival image with recorded provenance

The nuclear evacuation image can use alternate-history documentary imagery with ash, distant destruction, medical staff, and organized movement. Keep injury non-graphic.

## Stable asset naming

Lock stable lowercase snake_case basenames before generation.

Recommended shared paths after verifying the active consumer:

```text
gfx/interface/decisions/famine_and_migration_system/
gfx/interface/state_modifiers/famine_and_migration_system/
gfx/event_pictures/famine_and_migration_system/
```

Do not create an event-number folder.

Proposed sprite basenames should follow the IDs in the asset matrix.

## Production package

During active work, use a temporary evidence folder such as:

```text
docs/assets/famine_and_migration_system/
```

Include:

- manifest
- prompts
- source PNGs
- sourced originals and provenance where applicable
- processed PNGs
- contact sheets
- final DDS files or exact runtime-copy handoff
- `gfx_handoff.md`

Before either mechanic and their connected asset package can be called complete:

- move final runtime files into engine-facing folders
- verify every asset has a live consumer
- promote durable provenance, prompt, review, and crosswalk facts into permanent system documentation
- verify no runtime reference points into `docs/assets/`
- remove the temporary workspace after all work and review are complete

## Review standards

For every icon, inspect native size and at least 4x nearest-neighbor scale.

For the full family, create contact sheets showing:

- filename
- native dimensions
- transparency
- visual alignment
- stage order
- no white matte
- no opaque square background
- no duplicated or resized substitute art

For report images, verify:

- period accuracy
- subject clarity
- no modern detail
- no malformed hands or transport
- no visible generated text
- correct crop at runtime size

## Handoff

Return:

- created source and processed files
- final DDS paths
- sprite names
- target `.gfx` files
- dimensions
- source mode
- prompt or source URL
- provenance and license status
- contact sheets
- blocked items
- any uncertainty in the Deaths icon consumer

Do not edit gameplay, decisions, scripted effects, localisation, or the event catalog. The parent implementation agent owns final non-portrait wiring.
