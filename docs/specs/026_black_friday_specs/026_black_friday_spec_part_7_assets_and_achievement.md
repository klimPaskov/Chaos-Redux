# Assets and achievement

> **2026-09-20 native-raid boundary:** The accepted CBRN overhaul moves Japan's chemical and biological campaign attacks to native raids with multi-day preparation and engine-reserved payment. No documented raid lifecycle hook has yet proved that reservation during a one-day Black Friday sale can credit this achievement before the later outcome. The five-family design below remains accepted for transactions with a confirmed receipt; Japan native raid eligibility is unresolved, and the retired attack-decision adapter is not evidence for it. See the [CBRN amendment](../chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) and [requirement ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md).

## Visual package

Event 26 needs three distinct visual families.

| Asset | Role | Target and placement direction |
| --- | --- | --- |
| Black Friday report image | Player-facing Friday popup | Process through the current report-event pipeline, with final runtime placement under `gfx/event_pictures/026_black_friday/` |
| Black Friday active-sale idea icon | One-day human-player status marker | Original 64 by 64 idea or national-spirit icon under `gfx/interface/ideas/026_black_friday/` |
| Event 26 achievement triplet | Normal, grey, and not-eligible achievement states | Original achievement-specific source art and current Vanilla-sized triplet in `gfx/achievements/` |

Each family requires its own source art. The idea icon cannot be a resized report image. The achievement art cannot be a resized idea icon.

## Report image direction

### Subject

Show a crowded late-1930s or early-1940s commercial scene where civilians, civil servants, and uniformed quartermasters rush to secure goods. Crates, paper invoices, shop counters, supply boxes, and hurried clerks should suggest that ordinary shopping and state procurement have merged for one day.

### Composition

Use a clear central crowd or purchasing counter. Keep the frame readable at report-event size. A few military or government details can establish the wider scope without turning the image into a war-room scene.

### Source mode

Use generated period documentary art because the event is fictional and needs one coherent scene. The final source should resemble a staged news photograph from the 1936 to 1945 period.

### Avoid

- readable generated signs or price text
- current brands and logos
- modern shopping carts and checkout equipment
- digital displays
- modern clothing, vehicles, packaging, or architecture
- cinematic color grading
- maps as the main subject
- exaggerated panic or violence

## Active-sale idea icon direction

Create a compact HOI4 idea icon centered on a paper price tag tied to a small gear or supply crate. A strong downward price symbol can appear as a graphic mark without readable text. Use a clear silhouette, dark outline, restrained shadow, and transparent unused canvas.

The icon must remain legible at 64 by 64. Fine print, several small objects, and a full shop scene will fail at that size.

## Achievement design

### Working label

`Five Departments`

The implementation agent must write the final achievement name and description after localisation review. The working label is an identifier for planning only.

### Player challenge

During one naturally selected Event 26 sale, one human-controlled country must complete paid actions from five distinct registered cost-surface families before the next daily tick.

The five families must include:

- at least one institutional family, such as a law, advisor, officer role, or intelligence action
- at least one material or commitment family, such as equipment, fuel, convoys, trains, factories, or dockyards
- at least one family that does not use political power as its paid resource

### Eligible transactions

A transaction counts when:

- Event 26 came from automatic random selection
- the sale is active
- the transaction had a positive ordinary current cost
- the country paid a positive discounted amount
- the action completed or committed successfully
- the logical family has not already been credited for that country during the current sale
- the action belongs to the final cost coverage registry
- the transaction credits only the registry-defined primary achievement family, even when the action pays several resource types

At least five successfully committed logical actions are therefore required. One multi-resource action cannot supply several family credits.

### Disqualifiers

The achievement cannot unlock when:

- Force Trigger Mode started Event 26
- a manual settings launch selected Event 26
- the transaction was free before the sale
- the transaction was refunded or rolled back before successful completion
- the transaction was an AI action
- the same logical family is repeated
- the event has already expired

### Tracking

Track progress per human country for the current active sale. Store one credited flag or family ledger entry per logical family. Clear temporary progress after expiry. Award the achievement immediately when the fifth valid family completes.

A refundable action should count only after successful final commitment. This avoids complicated rollback of achievement progress.

### Achievement tooltip direction

The description should tell the player to use five different types of purchase during one natural Black Friday and mention the institutional and material requirements. It should not expose internal family IDs or registry names.

## Achievement icon direction

Create original achievement art showing an overloaded government purchasing desk or ledger surrounded by a supply crate, a military file, a fuel can, and a price tag. Keep one main subject and strong contrast. The image should suggest many departments buying at once.

The grey and not-eligible variants must follow the current Chaos Redux achievement workflow and exact current Vanilla precedent. They are asset states, not independent redesigns.

## Asset handoff requirements

The asset package must include:

- generated source PNG for each original asset family
- saved prompt and source-mode note
- processed PNG preview
- final DDS file or achievement DDS triplet
- exact dimensions
- transparency evidence for the idea icon
- contact sheet showing final alignment and readability
- manifest entries
- proposed sprite names and final runtime paths
- `gfx_handoff.md`

Final sprite names should stay stable once implementation begins. The parent implementation agent owns non-portrait `.gfx` wiring and gameplay references.
