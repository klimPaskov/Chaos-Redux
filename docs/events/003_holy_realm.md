# The Holy Realm

## Overview

The Holy Realm is event ID 3 and remains registered as a fire-once Chaos Redux event. It transforms Tibet, or a Tibet-centered Himalayan country, into a full country path rather than a short event chain. The route starts as a mountain refuge, becomes a Bodhisattva-led state, creates the Arhat Administration, reaches the Buddha Mandate, and can branch into restraint, peacekeeping, coercive pacification, Divine Sovereignty, or Final Silence.

The custom Holy Mandala Panel and Final Silence Ledger are represented through degraded UI mode in the decision category until a custom scripted GUI is built. The degraded UI shows the four core counters directly in the category description:

- Spiritual Legitimacy
- Compassion Drift
- Mandala Reach
- Final Silence Pressure

## Flow

1. `chaosx.nr3.1` redirects the event to Tibet if possible, otherwise to a Tibet-centered eligible country.
2. `chaosx.nr3.2` forms the Holy Realm, sets cosmetic tag `THR`, loads `THR_focus`, initializes counters, records the refuge evolution, opens decisions, and warns human players.
3. Bhutan, Nepal, and Tibet can receive a Himalayan unity invitation through `chaosx.nr3.3`.
4. The focus tree drives the major stages:
   - `THR_bodhisattva_accepts_seal` fires the Bodhisattva stage.
   - `THR_arhats_take_office` creates the Arhat Administration.
   - `THR_buddha_mandate` fires the Buddha Mandate super event.
   - `THR_throne_without_body` and `THR_doctrine_last_war` open Divine Sovereignty and the final doctrine.
   - `THR_final_silence` can start the world-end branch only when all hard gates pass.
5. Decisions provide Arhat oversight, refugee policy, diplomacy, doctrine selection, final warning behavior, and foreign containment responses.

## System Integration

The Holy Realm extends existing Chaos Redux systems rather than creating parallel ones:

- Chaos Meter: stage changes and Final Silence add chaos through `add_chaos_meter_value`.
- Evolutions: milestones record to the shared event-log evolution pipeline as evolution type `3`.
- Event logs: event ID 3 has a dedicated event-detail description and Holy Realm evolution label.
- Super events: values `7`, `8`, and `9` display Buddha Mandate, Final Silence, and thermonuclear Final Silence.
- World-end scenarios: Final Silence sets `world_end` and `world_end_final_silence`.
- Settings: Final Silence is blocked by `world_end_disabled`.
- Multiplayer behavior: human countries receive warning events when the Realm forms, when the Buddha Mandate becomes visible, and when the final doctrine is armed.
- Condemnation: Final Silence adds unconventional-warfare condemnation and applies existing diplomatic consequences.
- Deaths: Final Silence strike waves use the shared `chaos_meter_register_state_civilian_deaths_percent` pipeline.
- Air cleanliness: Final Silence applies air contamination unless the air cleanliness setting is disabled.
- Nuclear and wasteland logic: strike waves use `nuclear_fallout_state`, nuclear death reason constants, and `air_contamination_degrade_state_category`.
- World threats: Buddha Mandate, Divine Sovereignty, final warnings, and armed doctrine can set `world_threat_source_holy_realm`.

## Final Silence Conditions

Final Silence uses strict standard conditions:

- the Holy Realm exists and is the acting country
- the Holy Realm is sovereign
- the final doctrine is armed and not renounced
- the date is later than 1944.12.31
- Chaos Meter is above `1000`
- the Holy Realm has more factories than every other country
- nuclear or scripted strike capability exists
- `world_end` is not already active
- `world_end_disabled` is not set

If the date is later than 1946.12.31 and thermonuclear technology or doctrine exists, the thermonuclear variant is used. It applies larger air damage, higher death percentages, stronger fallout, faster state-category degradation, a separate global flag, and super-event image/audio ID `9`.

## Reserved Hooks

The Holy Realm reserves clean internal memory flags for later chains without implementing them:

- `holy_realm_memory_himalayan_unity`
- `holy_realm_memory_himalayan_refusal`
- `holy_realm_memory_snow_line_labs`
- `holy_realm_scripted_strike_network`
- `holy_realm_final_silence_engine`

No Germany, Mengele, Tibet expedition, Malta Crusader, Teutonic Order, Final Crusade, or Atlantis content is implemented here.

## Icons And Assets

The current implementation uses existing vanilla/mod focus icons and existing decision category icons. The following super-event art files are registered and can be replaced with dedicated art without renaming code references:

- `gfx/super_events/super_event_buddha_mandate.dds`
  - referenced as `GFX_super_event_buddha_mandate`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_final_silence.dds`
  - referenced as `GFX_super_event_final_silence`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_final_silence_thermonuclear.dds`
  - referenced as `GFX_super_event_final_silence_thermonuclear`
  - registered in `interface/chaosx_super_events.gfx`

The country leader still uses the existing `GFX_portrait_THR_godly_figure` asset.

## Future Plans

- Replace degraded UI mode with a custom Holy Mandala Panel and Final Silence Ledger scripted GUI.
- Add dedicated art for the three super-event images.
- Add state-map visualization for Final Silence struck, fallout, wasteland, and silent states.
- Add deeper foreign coalition events if the world-threat framework gains multi-source response packages.
