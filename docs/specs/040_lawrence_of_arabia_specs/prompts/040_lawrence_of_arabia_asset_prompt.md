# Event 40 Asset Production Prompt

Create the authorized visual asset package for Chaos Redux Event 40, Lawrence of Arabia.

## Required reading

Read these sources in full before production:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md` only if a later accepted brief adds animation
- `.agents/skills/chaos-redux-super-events/SKILL.md` for federation super-event images
- every file under `docs/specs/040_lawrence_of_arabia_specs/`
- relevant installed vanilla asset definitions and canonical skill-local reference contact sheets

Do not create or wire gameplay, event, decision, focus, localisation, GUI, or spreadsheet files unless a parent prompt grants that exact scope.

## Temporary workspace

Use:

`docs/assets/040_lawrence_of_arabia/`

Final runtime DDS files must go into event-scoped runtime folders. No runtime path may point into `docs/assets/`.

## Grounded portrait

Create one canonical portrait package for T. E. Lawrence through `chaosx_portrait_creator`.

Requirements:

- identity classification: `grounded_source_only`
- search installed vanilla and Chaos Redux for `T. E. Lawrence`, `Thomas Edward Lawrence`, `Lawrence of Arabia`, and reasonable identity variants
- record character and portrait ownership matches
- use an unchanged attributed archival photograph of Lawrence as the identity master
- reject actors, film stills, reenactors, statues, illustrations, generated faces, and reconstructed likenesses
- create the exact lossless head-and-shoulders crop and crop evidence required by the portrait workflow
- use `source_placeholder` mode as the accepted final mode for this task
- produce deterministic `156x210` PNG and DDS output
- retain one stable runtime basename across adviser, commander, operative, or leader consumers when the engine framing permits it
- do not create several inconsistent Lawrence faces
- record source URL, archive, creator when known, license or rights status, retrieval date, hashes, crop coordinates, review, runtime path, and proposed sprite

Proposed basename:

`GFX_portrait_040_te_lawrence`

Proposed runtime folder:

`gfx/leaders/040_lawrence_of_arabia/`

The portrait worker owns portrait-specific GFX and existing character portrait references only.

## Archival report images

Research and prepare period source images through `chaosx_asset_source_researcher`.

Required source directions:

1. Lawrence with Faisal and other Arab leaders or officers
2. Lawrence with Arab and Allied officers at Aqaba
3. Hejaz Railway, railway sabotage, or a route scene suitable for Evolution I

The main event image should show the coalition and local actors behind the campaign. Do not use a lone romantic portrait as the only event scene.

Use period archive images, record provenance and rights, retain original source bytes when permitted, create processed PNG previews, and convert only approved candidates to the inspected report-event DDS format.

Proposed runtime basenames:

- `040_lawrence_arrival`
- `040_lawrence_network`
- `040_lawrence_railway`

Proposed runtime folder:

`gfx/event_pictures/040_lawrence_of_arabia/`

## Decision category picture

Create one static decision category picture.

Working asset ID:

`040_lawrence_intervention_category`

Source mode:

- sourced archival group scene when a fitting and usable image exists
- generated period-authentic scene only when the image does not fabricate a real person's likeness

Composition:

- liaison meeting, guarded conference, arms and papers under local supervision, or a multi-actor political scene
- one clear subject group
- local leaders and officers visibly active
- no fake buttons, meters, labels, map arrows, readable generated text, or film imitation

Inspect the canonical decision-category picture references and the active runtime consumer before selecting the final canvas.

Proposed runtime folder:

`gfx/interface/decisions/040_lawrence_of_arabia/`

## Icon packages

Route icon production to `chaosx_icon_artist`.

Create separate source art for each UI family. Do not resize a focus icon into an idea or decision icon.

### Decision category icon

- `040_lawrence_category`
- subject direction: field notes, headcloth, and a restrained liaison seal

### Target decision icons

- `040_lawrence_national_custody`
- `040_lawrence_gold_ledger`
- `040_lawrence_guarded_access`
- `040_lawrence_turned_contact`
- `040_lawrence_expose_network`
- `040_lawrence_detain_mission`
- `040_lawrence_independent_charter`
- `040_lawrence_arab_congress`

### British decision icons

- `040_lawrence_gold_and_arms`
- `040_lawrence_officer_cadres`
- `040_lawrence_red_sea_route`
- `040_lawrence_desert_air_route`
- `040_lawrence_base_agreement`
- `040_lawrence_client_reinforcement`
- `040_lawrence_recovery_operation`

### Idea icons

- `040_lawrence_british_mission`
- `040_lawrence_independent_partner`
- `040_lawrence_exposed_network`
- `040_lawrence_british_arabian_system`
- `040_lawrence_anti_intervention_confidence`
- `040_lawrence_uneven_administration`
- `040_lawrence_rival_commands`
- `040_lawrence_promise_debt`
- `040_lawrence_federal_mistrust`
- `040_lawrence_personal_settlement`

### Focus icon families

Create coordinated but separate focus art for:

- British federal compact
- sovereign Arab congress
- Lawrence personal settlement
- federal administration
- oil, rail, port, and air-route development
- army and irregular integration
- recognition and accession
- regional-order capstones

The final focus list comes from implementation. Do not bulk-generate icons before stable focus IDs exist.

### Achievement icon triplets

Create eligible, grey, and not-eligible states for every accepted achievement ID:

- `chaos_redux_040_uncrowned_kingdom`
- `chaos_redux_040_promises_kept`
- `chaos_redux_040_better_bargain`
- `chaos_redux_040_every_ledger_has_a_name`
- `chaos_redux_040_gold_without_chains`
- `chaos_redux_040_desert_conference`
- `chaos_redux_040_rails_ports_promises`

Achievement DDS files remain directly under `gfx/achievements/` and use the full achievement ID in the filename.

## Federation flags and emblems

Create flags only after the parent locks the country tag or cosmetic tags and completes collision review.

Required route families:

- British Arabia
- Independent Arab Federation
- Lawrence's Kingdom

Historical or attested symbols require source research first. ImageGen produces the final flat designs.

Reject fabric, folds, flagpoles, scenery, perspective, gradients, fake text, invented pseudo-Arabic lettering, and unresearched heraldry.

Produce normal, medium, and small files under the engine flag roots with the locked tag filenames.

Create a faction or league emblem only when implementation adds a runtime consumer.

## Super-event images

Create three separate super-event image packages after the super-event research brief locks each role.

Working IDs:

- `040_british_arabia_formed`
- `040_independent_arab_federation_formed`
- `040_lawrences_kingdom_formed`

British Arabia image:

- federal delegates and officers under visible British sponsorship
- local political actors remain central
- formal and uneasy tone

Independent Arab Federation image:

- congress, public charter, or proclamation led by local governments
- sovereign and constitutional tone
- no lone Lawrence-centered composition

Lawrence's Kingdom image:

- Lawrence among local rulers, officers, and institutions
- strange personal settlement without parody
- use the approved grounded Lawrence identity if he appears

Do not use film stills or fabricate a real person's face.

## Background and transparency rules

- icons, emblems, and other alpha-backed families request native transparent ImageGen output
- preserve alpha through processing and DDS conversion
- full-canvas report and super-event images keep the background required by their consumer
- flags remain full-canvas opaque flat designs
- background removal is fallback-only and must be documented

## Animation and 3D boundary

Do not create baseline animation, animated portraits, or custom 3D assets.

A later accepted animation brief must use real per-frame source art and a HOI4 frame sheet. A later 3D brief must use the full Meshy and Blender pipeline. Neither surface is authorized by this prompt.

## Deliverables

For every authorized asset provide:

- original source or ImageGen source evidence
- processed PNG preview
- final DDS where the runtime consumer is locked
- contact sheet
- manifest row
- provenance and rights notes
- dimension and alpha review
- proposed sprite or engine filename
- `gfx_handoff.md`
- blocker state for any asset without defensible source or consumer

Do not use placeholders, resized unrelated icons, actor likenesses, or unsupported historical symbols.
