# The Clean Certificate chain proof

The dormant chain owns candidate `719`, transaction `710074`, route `7180`, Event Log history `9180`, and `chaosx.fallout.719` through `.725`.

Gameplay source is split across `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_world_end_clean_certificate_event_triggers.txt`, `common/scripted_effects/fallout_world_end_clean_certificate_event_effects.txt`, the Clean Certificate constants, the Clean Certificate dynamic modifiers, and the candidate producer block.

The admission gate requires a current Quarantine owner, completed Returning Disease state memory, native Air Winter and Supply Access receipts, bounded disease and exposure, minimum shelter, supply, adaptation, public health, medicine, cohesion, recognition, and one affordable branch. The candidate selector chooses the lowest eligible native state and stores its id in the generation-bound dispatch envelope.

The four branches are Public Service, Paid Inspection, Political Leverage, and Regional Standard. Costs are branch-specific and use Food, Medicine, Scrap, Power, Fuel, Recognition, and Cohesion without a political-power store. The result resolves after thirty days and schedules the seasonal certification review after one hundred eighty days.

The result and callback use deterministic grades with branch-specific thresholds. Success, partial, and failure update Air Winter, Supply Access, Quarantine ledgers, cause memory, and dynamic modifiers. Failure losses use `apply_exact_state_civilian_population_loss` with `chaos_meter_deaths_reason.fallout_aftermath` and a minimum remaining population.

The Event Log history payloads are written by `fallout_event_719_record_history`. History `9180` routes through `chaosx_scripted_localisation_events_log.txt` to dedicated Clean Certificate detail and name keys.

The dedicated report asset is documented in `docs/assets/719_clean_certificate/manifest.md` and wired through `GFX_report_event_fallout_clean_certificate`.

The chain remains dormant. No scheduler activation flag is set, and no ordinary Fallout scenario registration is added.
