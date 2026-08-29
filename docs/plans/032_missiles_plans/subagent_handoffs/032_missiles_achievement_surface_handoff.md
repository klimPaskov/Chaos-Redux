# Event 032 achievement surface handoff

## Scope

This handoff covers only the eight Event 032 achievement definitions, their persistent evidence triggers and effects, and their English localisation.

The implementation does not edit Event 032 events, decisions, scenario adapters, core missile effects, shared settings, the event spreadsheet, generated CSV exports, or the shared achievement GFX registry.

## Achievement IDs

The root registry adds exactly these eight IDs:

- `chaos_redux_032_exact_distance`
- `chaos_redux_032_still_on_the_line`
- `chaos_redux_032_break_the_chain`
- `chaos_redux_032_keys_returned`
- `chaos_redux_032_no_second_sun`
- `chaos_redux_032_empty_the_silos`
- `chaos_redux_032_sky_full_of_steel`
- `chaos_redux_032_long_reach`

Each entry uses the established `custom_override_tooltip` wrapper and separates eligibility from the historical completion trigger.

## Persistent state contract

The new effect file initializes country-scoped counters and arrays, records operation and war receipts, stores deadlines and clock dates, and writes final receipt flags only after the complete criteria trigger is true.

The new trigger file checks the persistent counters, distinct-ID arrays, dates, receipts, achievement grant guards, and disqualifier flags instead of treating one Event 032 firing as completion.

The Event 032 owner must call `chaosx_032_achievement_initialize_country` when the ordinary missile program is initialized.

The Event 032 owner must set the documented `chaosx_032_input_*` variables and call the matching recorder at the operation, incident, site, war-start, war-resolution, repair, and timed-survival boundaries.

The distinct state and country counts for `exact_distance`, distinct saturation states for `sky_full_of_steel`, and opening and removed site arrays for `empty_the_silos` are persisted by the effects file.

The `sky_full_of_steel` caller must provide `chaosx_032_input_required_damage` from the Event 032 strategic-damage tuning source because the requested criterion names a threshold without defining a numeric value.

The `no_second_sun` incoming recorder also requires `chaosx_032_input_incoming_from_enemy` in addition to the payload and war identity.

The `still_on_the_line` repair recorder requires the repair site ID to match the damaged site ID retained by the damage recorder.

The `long_reach` caller must refresh `chaosx_032_achievement_record_long_reach_snapshot` while the qualifying line is active so the 180-day clock can be completed without a world-wide polling hook.

The caller must set `chaosx_032_achievement_required_evolution_enabled` to one immediately before invoking an evolution-gated recorder and use the matching gate wrapper.

The gate wrappers are `chaosx_032_achievement_latch_retaliation_evolution`, `chaosx_032_achievement_latch_rogue_evolution`, `chaosx_032_achievement_latch_special_warhead_evolution`, and `chaosx_032_achievement_latch_saturation_evolution`.

Missing evolution input fails closed and permanently marks the relevant achievement as disqualified.

## Shared disqualifiers

The shared campaign trigger rejects the persistent SCN-015 receipt, force bypass, debug bypass, ceased-country receipt, scenario bypass, and scenario-launched flags.

The per-achievement completion trigger rejects its persistent `*_granted` guard and its evolution-disabled flag.

The marker effects are `chaosx_032_achievement_mark_scn015_disqualifier`, `chaosx_032_achievement_mark_force_bypass`, `chaosx_032_achievement_mark_debug_bypass`, and `chaosx_032_achievement_mark_country_ceased`.

The achievement surface never sets `*_granted`, because that flag is the post-receipt guard owned by the eventual achievement consumer.

## Criteria coverage

`exact_distance` records twelve conventional precision receipts, twelve distinct target states, four distinct enemy countries, valid on-target or limited-success outcomes, and the centralized precision civilian-death cap.

`still_on_the_line` records three hardened and secure sites in three regions at readiness and command control 85 or higher, the damaged-site receipt, two retained operational sites, and repair within 180 days.

`break_the_chain` records chain depth two or higher, four countries, an actionable warning, a resolved warning, no retaliation or special payload, incident closure, and a 90-day survival clock.

`keys_returned` records rogue recovery with reserve or prepared-operation evidence, no unauthorized launch, no scuttle, restored security, control 75 or higher, and no foreign seizure or destruction.

`no_second_sun` records prewar delivery and stockpile evidence, an incoming enemy nuclear or thermonuclear strike, survival, war victory, no own special launch, and retention of a delivery option through resolution.

`empty_the_silos` freezes an opening enemy manifest of at least three sites, requires player-credited conventional removal of every opening site, rejects ally-only credit, special payloads, deliberate civilian command strikes, rebuilding, and requires war victory.

`sky_full_of_steel` records five conventional saturation operations in one war, ten distinct enemy strategic states, the caller-provided damage threshold, command control 35 or higher through the final launch, the 365-day deadline, and war victory.

`long_reach` records full technology, a mature line, three sites in three regions, the mature reserve threshold, readiness and control 90 or higher for 180 days at war with a major, all three operation types, and two surviving operational sites.

## Localisation and assets

`localisation/english/032_missiles_achievements_l_english.yml` contains the eight names, descriptions, detailed tooltips, a shared eligibility tooltip, a shared locked-state tooltip, and per-achievement locked-state strings.

The localisation file is UTF-8 with BOM.

The standard runtime triplets would be `gfx/achievements/<achievement_id>.dds`, `gfx/achievements/<achievement_id>_grey.dds`, and `gfx/achievements/<achievement_id>_not_eligible.dds`, with matching `GFX_achievement_<achievement_id>` aliases in `interface/chaosx_achievements.gfx`.

No Event 032 achievement-specific source icon art exists in the inspected asset report, and no genuine package could be produced within this bounded ownership surface.

All eight icon triplets and their shared GFX aliases remain blocked and intentionally unwired.

## Validation and remaining work

The registry contains exactly eight new Event 032 IDs and no icon or unrelated files were added.

The new localisation file was byte-checked for the UTF-8 BOM and all eight IDs have name, description, detailed tooltip, and locked-state keys.

The new scripted files were checked for balanced Clausewitz block braces, unsupported `<=` or `>=` operators, and matching public trigger and effect identifiers.

Live HOI4 launch and in-game validation were not performed, as required by the repository instructions.

The parent Event 032 implementation still needs to invoke these recorders at real runtime boundaries and needs to provide the missing achievement icon package and shared GFX aliases before the achievement surface can be considered fully integrated.
