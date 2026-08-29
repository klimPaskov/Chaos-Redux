# Asset production prompt for Event 028: Asteroid Incoming

Read `AGENTS.md`, `chaos-redux-event-assets`, the matching canonical reference folders, and all Event 028 specification parts before creating files. Use context-complete project subagents with `fork_context=false`. Character portrait work is outside this package.

## Owner and workspace

- Event ID: 028
- Event slug: asteroid_incoming
- Temporary evidence root: `docs/assets/028_asteroid_incoming/`
- Permanent runtime folders should be event scoped under the correct asset family.
- Preserve source PNGs, prompts, processed PNGs, final DDS files, contact sheets, manifest entries, and `gfx_handoff.md` while the event remains active or blocked.
- Do not edit gameplay, localisation, GUI, GFX, event, decision, achievement, or spreadsheet files unless the parent grants exact scope.

## Reference gate

Before production, inspect `assets/vanilla_reference/README.md`, `CATALOG.md`, and the exact contact sheet for each asset family. Follow the owning installed-vanilla sprite or GUI consumer. Reference images are review material and must not be shipped, traced, recolored, or reused as final art.

Generated art uses the official ImageGen route. If that route is unavailable, mark the affected rows blocked. Do not substitute primitive shapes, unrelated icons, local drawings, or resized assets from another family.

## Event and news art

Create these generated fictional documentary images.

1. `asteroid_tracking`
   - Type: report event image
   - Final canvas: 210x176 RGBA
   - Direction: 1936 to 1945 observatory, photographic plates, telescope instruments, scientists working under urgent time pressure
   - Avoid modern computers, readable equations, space-agency branding, and impact imagery

2. `asteroid_target_emergency`
   - Type: report event image
   - Final canvas: 210x176 RGBA
   - Direction: railway evacuation, field hospitals, civil shelters, water stores, or archives moving under a strange sky
   - Avoid modern emergency vehicles, gore, generic war-room maps, and mushroom clouds

3. `asteroid_impact_report`
   - Type: report event image
   - Final canvas: 210x176 RGBA
   - Direction: collapsed rail and industrial outskirts, dust-covered streets, period rescue crews, displaced civilians
   - Keep the scene country neutral so dynamic localisation can serve every affected country

4. `asteroid_fragment_report`
   - Type: report event image
   - Final canvas: 210x176 RGBA
   - Direction: smaller impact flash, descending debris trail, and regional damage from a distant survivable viewpoint
   - Create independent source art, not a crop of the main impact image

5. `asteroid_close_passage`
   - Type: news image
   - Final canvas: 397x153, black and white
   - Direction: observatory dome, telescope silhouette, public viewing point, or a bright object crossing the night sky
   - Avoid modern astrophotography and any visible collision

6. `super_event_028_asteroid_impact`
   - Type: super-event image
   - Final canvas: 457x328
   - Direction: vast impact flash and rising debris over a period landscape or industrial region, seen from a distant viewpoint with period buildings or transport for scale
   - Keep the image dynamic-target neutral with no flags or unique landmarks
   - Avoid a mushroom-cloud copy, modern skyline, orbital Earth view, map, text, or fantasy magic

## Decision category picture

Create `asteroid_recovery_category` as an independent generated category picture.

- Inspect the canonical category-picture family and active consumer before fixing runtime canvas.
- Use 114x101 only as a reference-family guide.
- Show a rescue rail line, dust protection, damaged infrastructure, and darkened sky in one period documentary composition.
- Do not paint fake buttons, meters, values, state pieces, text, or controls into the image.

## State and modifier icon families

Use the exact state-modifier and idea reference families. Create independent source art for each type.

### State modifier family

- `main_asteroid_crater`
- `catastrophic_impact_zone`
- `major_impact_zone`
- `outer_shock_zone`
- `fragment_crater`
- `heavy_fragment_damage`
- `light_fragment_damage`

Keep the family coherent through fractured ground, debris, broken transport, obscured sky, and crater material. Main crater and fragment crater must be distinct from radiation and each other.

### Idea and dynamic modifier family, 64x64

- `asteroid_residual_haze`
- `asteroid_global_dust_veil`
- `asteroid_impact_winter`
- `asteroid_severe_impact_winter`
- `asteroid_dust_protection`
- `asteroid_recovery_burden`
- `asteroid_main_crater_material`
- `asteroid_fragment_material`

Use spirit-style composition. Dust icons should emphasize atmosphere, filters, or obscured industry. Mineral icons should show dense metallic or shock-formed material without fantasy glow.

## Decision icon family, 32x32

Create one clear silhouette per action.

- `mobile_hospitals`
- `emergency_rail_corridor`
- `clear_unstable_debris`
- `emergency_water_filters`
- `rebuild_supply_spine`
- `restore_outer_ring_industry`
- `rehouse_displaced_workers`
- `harden_factories_against_dust`
- `protect_transport_reserves`
- `atmospheric_observation_network`
- `secure_crater_perimeter`
- `survey_extraordinary_material`
- `fortify_crater_access`
- `reconnoiter_crater_site`

Do not derive 32x32 icons by resizing idea, focus, category, or achievement art.

## Achievement icons

Create completed, grey, and not-eligible 64x64 triplets for the five accepted achievements. Use the exact achievement IDs locked by the parent and keep files directly under `gfx/achievements/` according to engine convention.

Themes:

- Close passage through a narrow gap
- Government and restored rail beyond a crater
- One main fragment and three smaller fragments over armored plate
- Piercing a mineral-strengthened armored plate
- Global transport and observation under a clearing sky

Use the canonical not-eligible overlay workflow. Do not produce the not-eligible state by recoloring the grey icon.

## Processing and handoff

- Preserve every original source image and prompt.
- Process transparent icons to real transparency with no checker remnants, white matte, opaque square, or white halo.
- Validate readability at native size and over a checker background.
- Convert final PNGs with the repository DDS workflow and verify dimensions, alpha, and decoded round trip.
- Place final DDS files in the correct Event 028 runtime folders.
- Write one manifest row per asset with source mode, prompt, target surface, dimensions, final path, sprite proposal, checksums, and status.
- Produce contact sheets by asset family.
- Return `complete`, `needs_user_review`, or `blocked` for every row.
- Record any missing reference, ImageGen failure, consumer uncertainty, or rejected generation. Do not use an unapproved fallback.
