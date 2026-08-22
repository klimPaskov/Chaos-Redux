# Captured Biological Facility Recovery

## Overview

Captured biological arsenals are resolved through native land raids. There is no decision-based deployment path. The controller must assign a division containing a Biosecurity Assault Detachment to an Army Headquarters with a Biological Security Section, reserve a route-specific package of protective and containment equipment, and prepare either a secure-and-preserve raid or a safe-destruction raid.

The system tracks one exact designated national arsenal state. Hearts of Iron IV stores equipment nationally rather than inside states, so the first hostile capture of that designated arsenal moves the former custodian's currently unallocated Anthrax, Plague, Tularemia, and Smallpox payloads into an exact state ledger. Payload already reserved by a native raid is not part of the national stockpile snapshot and is therefore not counted twice. This is a declared gameplay representation of a centralized arsenal, not a claim that every national payload was historically stored in one building.

## Capture and control sequence

1. A country designates its one stockpile-safety arsenal state through the existing arsenal system.
2. `on_state_control_changed` receives the exact new controller, old controller, and changed state. It does not search for a substitute state.
3. On the first hostile capture, the system snapshots the former custodian's four live unallocated payload counts, removes those exact aggregate amounts across all equipment producers once, and stores them on the changed state.
4. The state records the original custodian, current controller, remaining payload by agent, total hazard, and one delayed hazard due date.
5. A further third-party control change keeps the same payload ledger and updates only the exact controller pointer.
6. The former custodian may explicitly designate a replacement arsenal while the original site is occupied. That deliberate relocation clears the country's active pointer but preserves the captured state's original-custodian and payload records.
7. Recapture by the original custodian restores the exact remaining payload. If no replacement arsenal exists, the original designation and source are rebound to the retaken state; if a replacement exists, its active designation remains untouched and the obsolete marker is cleared from the retaken site.
8. If the facility remains unresolved when its targeted state event matures, a bounded share of one available agent is debited and enters the shared ordinary biological lifecycle as a captured-facility accident. The same exact state may schedule another check only while payload remains.

No daily, weekly, monthly, or all-country sampling pulse is used.

## Native recovery raids

### Secure and Preserve the Biological Facility

- Preparation: 21 days.
- Command Power: 25.
- Required formation: one selected division containing `cbrn_biosecurity_assault_detachment`, assigned to an Army Headquarters containing `cbrn_hq_biological_security_section`.
- Additional reserved stores: 80 gas masks, 50 decontamination sets, 40 CBRN instrument sets, 60 support equipment, and 30 motorized equipment.
- Limited success transfers 40 percent of every surviving captured agent to the controller and leaves the remainder in the exact state ledger.
- Success and critical success transfer every surviving captured payload and resolve the facility hazard.
- Preservation outcomes retain program evidence for attribution against the recorded original custodian.

### Destroy the Biological Facility Safely

- Preparation: 14 days.
- Command Power: 20.
- Required formation: one selected division containing `cbrn_biosecurity_assault_detachment`, assigned to an Army Headquarters containing `cbrn_hq_biological_security_section`.
- Additional reserved stores: 80 gas masks, 70 decontamination sets, 30 CBRN instrument sets, 70 support equipment, and 30 motorized equipment.
- Limited success destroys 50 percent of every surviving captured agent and leaves the remainder in the exact state ledger.
- Success and critical success destroy every surviving payload, resolve the hazard, and remove one level of `biowarfare_facility` from the exact state.

Both raids use native preparation, formation selection, equipment reservation, success calculation, outcome history, cooldown, and AI evaluation. Failure causes formation damage and releases a bounded share of one remaining agent through the shared biological lifecycle. There is no decision click, scripted proxy launch, inferred state, or fallback target.

## Headquarters and division layers

The Biosecurity Assault Detachment is the mandatory division layer. Character-scoped raid success modifiers check the selected division's own unit leader for `cbrn_hq_has_biological_security_section`. A missing section applies a fail-closed `-10` success weight, making the operation unable to succeed; the exact assigned section then provides the intended `+0.25` recovery bonus. A different headquarters elsewhere in the country cannot satisfy either check.

The current raid API restricts `unit_requirements` to battalion and equipment checks. It does not expose a character trigger that can hide an otherwise eligible division in the unit-selection list. The required character-scoped success factor is therefore displayed in native unit selection and enforces the requirement at resolution without inventing a national-HQ proxy. AI also rejects the zero-chance formation through `ai_min_success_chance`. A player can still select an invalid formation, but that formation cannot produce a successful recovery outcome; no alternate effect or refund is supplied.

An exceptionally large captured payload ledger applies a state-scoped success penalty. This penalty and the assigned-HQ bonus are visible in the native raid success interface.

## Accidents, evidence, and consequences

Captured-facility releases use:

- route `bio_lifecycle_route.captured_facility_release`;
- source `bio_lifecycle_source.captured_facility`;
- result `bio_lifecycle_result.accident`;
- the exact target state;
- the recorded original custodian as actor;
- the exact current controller as victim;
- an exact one-time state-ledger payload debit.

The shared lifecycle then resolves agent-specific incubation, detection, spread, protection, medical load, contamination, deaths, evidence, attribution, and Condemnation. Captured-facility and field-test sources remain accident-class for attribution: sufficient evidence can confirm responsibility for an accident, but cannot relabel the same episode as a deliberate biological attack.

Chaos Warfare doctrine may increase the physical consequences through the shared doctrine snapshot and may reduce only Condemnation. It does not reduce payload debit, evidence, attribution, deaths or their history, contamination or its history, medical saturation or its history, accident records, or public-harm floors.

Existing exact-state genocide discovery remains authoritative for experimentation and cover-up sites. Recovery raids preserve biological-program evidence; they do not duplicate the genocide system's atrocity or cover-up discovery effects.

## AI behavior

- Defensive CBRN profiles and ordinary democratic governments prefer secure preservation.
- Countries with pathogen-handling and rapid-response technologies are more willing to preserve and exploit the material safely.
- Unrestricted Chaos Warfare routes prefer safe destruction over preservation.
- Exceptional state-ledger hazard increases destruction priority and reduces preservation priority.
- Countries lacking advanced handling or response technology receive an additional safe-destruction preference.
- Native unit and equipment requirements remain hard gates for AI as well as players. The AI success threshold also rejects a formation missing its assigned Biological Security Section.

## Assets and wiring

| Runtime use | Sprite | Final DDS | Sprite definition |
|---|---|---|---|
| Secure/preserve raid type | `GFX_raid_type_icon_bio_facility_secure_preserve` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds` | `interface/chaosx_raids.gfx` |
| Destroy-safely raid type | `GFX_raid_type_icon_bio_facility_destroy_safely` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds` | `interface/chaosx_raids.gfx` |
| Recovery raid category and unit marker | `GFX_raid_category_small_biological_facility_recovery_raids`, `GFX_raid_unit_icon_biological_facility_recovery_raids` | Existing `gfx/interface/military_raids/map_icons/raid_unit_icon_biological_raids.dds` | `interface/chaosx_raids.gfx` |
| Capture and breach reports | `GFX_report_event_generic_bioweapon` | Existing same-type biological-weapon report art | Existing `interface/chaosx_pictures.gfx` definition |

The two raid-type icons are independent generated assets with source PNGs, processed transparent previews, contact sheet, validation notes, and hashes under `docs/assets/chaos_warfare_system/stage_7_biological_warfare/captured_facility_raid_icons/`. The existing biological raid category icon and generic biological-weapon report image are intentionally reused on matching asset surfaces; neither has been overwritten or resized.

## Main files

- `common/raids/biological_facility_recovery_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/script_constants/biological_facility_capture_constants.txt`
- `common/scripted_triggers/biological_facility_capture_triggers.txt`
- `common/scripted_triggers/biological_lifecycle_triggers.txt`
- `common/scripted_effects/biological_facility_capture_effects.txt`
- `common/scripted_effects/biological_stockpile_safety_effects.txt`
- `common/on_actions/biological_facility_capture_on_actions.txt`
- `events/biological_facility_capture_events.txt`
- `interface/chaosx_raids.gfx`
- `localisation/english/biological_facility_recovery_raids_l_english.yml`

## Future extensions

- Add a verified native raid scenario test covering an arsenal whose original owner has been fully annexed; do not add an alternate decision or inferred target if the engine cannot expose that raid target.
- Add dedicated raid completion report art only if the native raid UI gains a distinct report-image surface for land recovery operations.
- Connect future intelligence-agency counter-biological traits to preservation evidence quality only when a current-version character or operative scope can be proved at raid resolution.
