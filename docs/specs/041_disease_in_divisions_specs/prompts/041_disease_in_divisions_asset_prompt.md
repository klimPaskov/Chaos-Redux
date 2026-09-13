# Asset production prompt for Event 41: Disease in Divisions

Create the complete visual asset package for Event 41 under the Chaos Redux asset rules. Read `AGENTS.md`, `chaos-redux-event-assets`, and the full Event 41 specification pack before production.

Use separate source art for each asset family. Do not satisfy decision, idea, category, report, status, or achievement art by resizing an image made for another surface.

## Working and final paths

Use the temporary working folder:

`docs/assets/041_disease_in_divisions/`

Place final runtime assets under event-scoped engine folders using `041_disease_in_divisions` as the event folder where the consumer allows it.

Before final completion, promote durable provenance, prompt, review, and runtime crosswalk facts into permanent Event 41 documentation, verify that no runtime reference points into `docs/assets/`, then remove the temporary event workspace.

## Reference inspection

Before producing each family, inspect the matching canonical references and contact sheet under:

`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`

Required families include:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/ideas/`
- `icons/state_modifiers/` or the exact current formation-status consumer family
- `icons/achievements/`

If the decision category picture `contact_sheet.png` is missing, build it from the reference images, label every filename and native dimension, and update the reference README and catalog before production. Reference images are review material and must never be wired, traced, recolored, or shipped.

## Source modes

Use generated period-documentary art for the report image and category picture because the event is fictional, country-neutral, and should not falsely assign a real photographed epidemic to one army. Use native ImageGen through the designated asset worker.

Use generated symbolic art for icons. Every alpha-backed icon must begin with genuine native transparency. Preserve alpha through processing and DDS conversion. Background removal is fallback-only and must be recorded and edge-validated.

## Report event image

Create one `210x176` report image.

Working basename:

`041_disease_in_divisions_report`

Suggested sprite:

`GFX_report_event_041_disease_in_divisions`

Visual direction:

- World War II field medical environment
- one coherent frontline rear area
- overcrowded field hospital or treatment tent
- sick soldiers, medics, stretchers, period ambulance or rail evacuation in the same scene
- damaged supply environment visible without making a map the subject
- documentary photographic realism from 1936 to 1945
- country-neutral uniforms and equipment where possible
- no gore
- no modern masks, ambulances, plastics, digital equipment, or readable generated text
- no cinematic color grading
- no generic command-table composition

## Static decision category picture

Create a separate static category picture designed for the current runtime consumer. Inspect the exact sprite and GUI size before final output. The canonical reference family currently uses `114x101` examples, but the active consumer decides the final size.

Working basename:

`041_disease_in_divisions_category_picture`

Suggested sprite:

`GFX_041_disease_in_divisions_category_picture`

Visual direction:

- closer treatment-camp composition than the report image
- medics separating sick and healthy military areas
- clear period tents, stretchers, bedding, water or sanitation equipment
- one strong focal subject at small size
- no fake buttons, meter, labels, ledger rows, or text
- static only

## Decision category icon

Create one category icon for the military epidemic system.

Working basename:

`041_disease_in_divisions_category`

Suggested sprite:

`GFX_decision_category_041_disease_in_divisions`

Motif direction:

A military helmet or field cap beside a medical satchel and fever thermometer, with a clear disease or quarantine cue. Keep it readable and period-appropriate.

## Army Infection Pressure icon and texticon

Create a compact pressure symbol for category status and cost or tooltip use where the current UI supports it.

Working basename:

`41_army_infection_pressure`

Suggested sprites:

- `GFX_41_army_infection_pressure`
- the matching registered texticon token if the implementation uses one

Motif direction:

A military formation symbol under a fever or contamination pulse. Avoid a generic biohazard symbol when the event has not identified a biological weapon.

## Formation and aftermath icons

Create distinct icons for:

- active affected formation
- recovering formation
- field epidemic preparedness
- exhausted medical service
- shattered infected front aftermath when a separate icon is required

Use the exact current state-modifier, unit-status, or idea consumer references before selecting size and canvas.

Suggested basenames:

- `41_affected_formation`
- `41_recovering_formation`
- `41_field_epidemic_preparedness`
- `41_exhausted_medical_service`
- `41_shattered_infected_front`

## Decision icons

Create separate `32x32` decision icons for every implemented action. Each needs its own source art designed for small readability.

Baseline family:

- `41_rotate_sick_formations`
- `41_quarantine_camps`
- `41_expand_field_hospitals`
- `41_sanitize_camps_supply`
- `41_medical_evacuation`
- `41_repair_medical_corridor`
- `41_emergency_medical_mobilization`
- `41_isolate_military_district`
- `41_abandon_contaminated_sector`
- `41_restrict_offensives`
- `41_fight_through_outbreak`

Evolution I family:

- `41_inspect_allied_formations`
- `41_separate_coalition_camps`
- `41_exchange_medical_reports`
- `41_restrict_military_access`

Evolution II family:

- `41_close_military_port`
- `41_controlled_demobilization`
- `41_protect_civilian_transport_hubs`
- `41_international_medical_coordination`

Use a coordinated period medical and military palette, while giving every icon a distinct silhouette. Do not create one master icon and crop or recolor it into the full family.

## Achievement icons

Create separate `64x64` completed icons for:

- `chaosx_41_the_line_holds`
- `chaosx_41_every_soldier_accounted_for`
- `chaosx_41_quarantine_the_coalition`
- `chaosx_41_war_without_plague`

Use the exact motif directions in the achievement prompt. Produce grey and not-eligible variants when the repository achievement consumer requires the triplet.

## Package requirements

For every asset, provide:

- source PNG
- processed PNG preview
- final DDS
- exact dimensions
- source mode
- prompt and background mode where generated
- reference family inspected
- contact sheet
- alpha and small-size readability review
- suggested sprite name
- final runtime path
- manifest entry
- `gfx_handoff.md` entry

Reject opaque square backgrounds, white halos, fake checkerboards, unreadable small details, modern equipment, visible generated text, and reused art from another icon type.
