# Infantry Spawn asset prompt

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation`. Inspect the relevant reference folders before creating any asset. This prompt defines asset needs only. It does not grant permission to edit gameplay, localisation, GFX, GUI, or spreadsheets unless the implementation parent explicitly expands scope.

Event id: 019. Event slug: infantry_spawn.

## Required reference folders

- idea and national spirit icons: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- decision and category icons: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- focus icons: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- report event images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- flags: `.agents/skills/chaos-redux-event-assets/assets/flags`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Package structure

Create a full asset manifest under `docs/assets/019_infantry_spawn/manifest.md` and a GFX handoff under `docs/assets/019_infantry_spawn/gfx_handoff.md`. Final in-game DDS assets should use event-scoped folders where the surface permits it.

## Report and news images

Source mode: generated documentary-style images unless implementation decides a real archival image is required for a specific non-fictional surface. The event is fictional, so generated period-authentic imagery is appropriate.

Required image directions:

| Asset working label | Type | Direction |
| --- | --- | --- |
| report_event_sudden_muster | report image 210x176 | soldiers appearing in a town square, rail yard, or barracks courtyard with 1936-1945 documentary framing |
| report_event_depot_disorder | report image 210x176 | crates, rifles, officers, rail wagons, and confused mustering without readable text |
| report_event_possessed_general | report image 210x176 | unsettling commander and troops in a period staff or field setting, no real likeness |
| report_event_chaos_barracks | report image 210x176 | high-chaos barracks with strange units, restrained supernatural mood, no modern props |
| news_event_first_barracks_revolt | news image 397x153 | first serious military revolt caused by spawned units, black and white |
| news_event_first_chaos_splinter | news image 397x153 | first zombie, ghost, golem, or registry chaos splinter, black and white |

Report images must receive the report-card treatment. News images must be black and white.

## Icons

All icons use `$imagegen` unless the parent provides source art. Do not derive one icon type by resizing another.

| Asset | Type and size | Direction |
| --- | --- | --- |
| idea_muster_fatigue | idea 64x64 | tired troops, paperwork, boots, and fading reserve symbol |
| idea_command_confusion | idea 64x64 | crossed signals, broken insignia, command baton or map pins |
| idea_supply_strain | idea 64x64 | rails, crates, fuel cans, and overburdened logistics |
| idea_formation_absurdity | idea 64x64 | mismatched helmets, tank treads, cavalry tack, and strange roster motif |
| idea_officer_appetite | idea 64x64 | officer cap, grasping hand, shadowed epaulette |
| idea_chaos_leakage | idea 64x64 | cracked barracks seal with faint supernatural seepage |
| decision_category_muster_ledger | category icon | stamped army ledger, no readable text |
| decision_inspect_wave | decision 32x32 | magnifying glass over insignia or dog tags |
| decision_sort_depots | decision 32x32 | crates and rail switch |
| decision_standardize_formations | decision 32x32 | aligned helmets or formation blocks |
| decision_request_random_unit | decision 32x32 | dice or sealed roster with military symbol, no numbers |
| decision_quarantine_chaos_units | decision 32x32 | containment cordon and barracks door |
| decision_exorcise_ghost_companies | decision 32x32 | pale unit silhouette and sealing mark |
| decision_bind_golem_cadres | decision 32x32 | stone hand and military strap |
| decision_authorize_base_zombies | decision 32x32 | sealed medical or military zombie cadre symbol |

## Possessed general portraits

Generate twenty fictional commander portraits. They should look scary and possessed, but still period-appropriate and usable in HOI4. Record apparent gender presentation in the manifest and require matching name pools. Do not use real people.

Groups:

- four staff officers
- four frontline commanders
- four militia leaders
- four logistics or depot officers
- four high-chaos officers

Target size: 156x210 unless existing commander pattern requires another size. Include source PNG, processed PNG, final DDS, and manifest entries.

## Flags and country identity assets

Generate fictional flags for:

- Barracks State base and ideology variants if needed
- Ragged horde base and profile variants
- Grey host base and profile variants
- Stone host base and profile variants
- Mixed impossible army placeholder profile only if implementation creates a visible package

Flags must be readable at 82x52, 41x26, and 10x7. Do not use text. Do not create ideology variants as simple recolors.

## Shared breakaway focus tree icons

Create focus icon families for the shared crisis tree:

- opening survival trunk
- human command route
- irregular integration route
- depot economy route
- expansion against parent route
- high-chaos route
- settlement route
- ragged horde overlay
- grey host overlay
- stone host overlay

Each focus icon should be designed for 94x86. The final implementation agent will assign exact focus ids.

## Achievements

The achievement prompt contains the full list. Create completed 64x64 icons for every achievement direction, then grey and not-eligible variants if the achievement system requires them. Use the achievement reference folder and overlay workflow.

## Animated UI package

Follow `chaos-redux-frame-animation`. Each animation needs real source frames, a static fallback, frame sheet, final DDS, preview GIF, contact sheet, manifest, and GFX handoff.

| Animation | Target | Frame plan direction |
| --- | --- | --- |
| muster_category_seal_animated | decision category or GUI header | 8 frames, stamped paper or brass seal with subtle live flicker |
| command_coherence_meter_animated | scripted GUI meter frame | 6 or 8 frames across stable, strained, cracked state families |
| officer_demand_warning_animated | warning card | 8 frames, epaulette or eye-glint motif drawn per frame |
| chaos_leakage_warning_animated | warning card | 8 frames, supernatural seepage or particles drawn per frame |
| random_unit_button_available_animated | button state | 6 frames, readable availability glow from separate source frames |

Static presentation can be used only if the implementation parent records why animation would reduce clarity.

## Super-event image directions

If the implementation accepts the planned escalation super-events, produce generated super-event images for:

- first global possessed command revolt
- first chaos splinter country from Infantry Spawn
- optional triggerable scenario maximum launch

Use 457x328 final DDS, strong central composition, period-authentic military scene, no generated text, no modern props.
