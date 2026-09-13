# Event 57 Asset Production Prompt

Create the complete visual asset package for Chaos Redux Event 57, The Black Market, from `docs/specs/057_the_black_market_specs/09_assets_and_achievements.md`.

Follow the current repository versions of `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` when an inherited consumer proves animation is required, and `chaos-redux-subagents`.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Required reference inspection

Inspect the exact canonical families under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Required folders:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/achievements/`

Confirm the active runtime consumer and native size for every asset type. The decision-category-picture folder must have a labeled `contact_sheet.png`. Create it and update the reference README and catalog when missing.

## Report pictures

Create independent generated period-documentary scenes at `210x176` for:

1. `black_market_first_contact`
2. `black_market_seized_shipment`
3. `black_market_grand_auction`

Use 1936 to 1945 clothing, cargo, architecture, lighting, vehicles, and materials. Show guarded depots, concealed cargo, false logistics, mixed military stock, neutral transport, and anonymous intermediaries. Do not use modern containers, computers, neon crime imagery, readable generated text, national stereotypes, gore, or a central crime boss.

Final runtime folder:

`gfx/event_pictures/057_the_black_market/`

Proposed sprites:

- `GFX_report_event_057_black_market_first_contact`
- `GFX_report_event_057_black_market_seized_shipment`
- `GFX_report_event_057_black_market_grand_auction`

## Category icon and texticon

Create:

- `black_market_category`, a compact decision-category icon with a sealed crate and route or key motif
- `black_market_credit_texticon`, a small stamped account chit or ledger token for Market Credit

Use genuine native transparency, a dark outline, subtle shadow, stable centering, and strong readability at final size. No text, skulls, modern padlocks, coins as the main subject, fake checkerboards, white matte, or opaque square background.

Confirm the exact texticon precedent and dimensions before production.

## Category pictures

Create four separate static category pictures, each designed for the inspected consumer:

- `black_market_category_local_circuit`
- `black_market_category_international_network`
- `black_market_category_underground_economy`
- `black_market_category_anything_has_a_price`

The current reference family uses `114x101`, but do not assume that size without inspecting the live consumer.

The pictures should show increasing scale through depots, rail, ports, neutral freight, industrial material, technical cases, and exceptional guarded cargo. Do not use a world map as the main subject. Do not paint fake buttons, meters, values, or controls into the image.

Proposed sprites:

- `GFX_057_black_market_category_local_circuit`
- `GFX_057_black_market_category_international_network`
- `GFX_057_black_market_category_underground_economy`
- `GFX_057_black_market_category_anything_has_a_price`

## Decision icons

Create independent transparent `32x32` art for:

- `black_market_buy_lot`
- `black_market_sell_surplus`
- `black_market_commission`
- `black_market_open_route`
- `black_market_safer_route`
- `black_market_intelligence`
- `black_market_compartmentalize`
- `black_market_burn_route`
- `black_market_penetration`
- `black_market_suppression`
- `black_market_grand_auction`
- `black_market_underwrite`

Each icon needs its own source art and final-size composition. Do not resize category, focus, idea, or achievement art to satisfy a decision icon.

## Achievements

Create completed `64x64` art and the required grey and not-eligible states for these exact proposed IDs:

- `57_the_black_market_no_questions_asked`
- `57_the_black_market_enemy_quartermaster`
- `57_the_black_market_embargo_has_holes`
- `57_the_black_market_liquid_assets`
- `57_the_black_market_invisible_empire`
- `57_the_black_market_customs_seizure`
- `57_the_black_market_prototype_without_a_project`

Use the icon directions in the source spec. Achievement DDS files stay directly under `gfx/achievements/` and use the full achievement ID as basename.

## Workflow and outputs

Use narrow asset subagents according to the current asset skill. Generated scenes belong to `chaosx_generated_event_art`. Icons and achievement triplets belong to `chaosx_icon_artist`.

For each asset:

- retain source evidence
- retain the exact prompt and source mode
- preserve native alpha where required
- create processed PNG preview
- create final DDS
- validate dimensions, framing, readability, transparency, and edge quality
- create contact sheets at native size
- record proposed sprite and runtime path
- write a manifest and `gfx_handoff.md`

Use the temporary workspace:

`docs/assets/057_the_black_market/`

The parent owns final non-portrait `.gfx` wiring and gameplay consumers. Before full completion, promote durable provenance, prompt, review, and runtime crosswalk facts into permanent Event 57 documentation, confirm that no runtime path points into `docs/assets/`, then delete the completed temporary event workspace.

Do not substitute an unrelated existing icon, primitive local drawing, opaque placeholder, sourced modern photo, or weak resize. Mark a blocked asset honestly.
