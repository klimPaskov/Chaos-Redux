# Biological raid neighbor tooltip handoff, 2026-09-27

Disposition: implemented for the bounded localisation patch. Native equipment disposition after a completed or cancelled raid remains unresolved.

## Changed files and keys

- `localisation/english/biological_sabotage_raids_l_english.yml`: `bio_sabotage_raid_failure_actor_tt`.
- `localisation/english/biological_battlefield_raids_l_english.yml`: `bio_battlefield_preparation_available_tt`, `bio_battlefield_failure_actor_tt`, `bio_battlefield_limited_actor_tt`, `bio_battlefield_success_actor_tt`, `bio_battlefield_critical_actor_tt`, `bio_battlefield_context_rejected_actor_tt`, `bio_battlefield_context_rejected_target_tt`.
- `localisation/english/016_brilliant_scientist_biological_raids_l_english.yml`: `brilliant_scientist_biological_raid_failure_actor_tt`.
- `localisation/english/biological_facility_recovery_raids_l_english.yml`: `bio_facility_capture_secure_failure_tt`, `bio_facility_capture_destroy_failure_tt`, `cbrn_bio_facility.4.desc`.
- `localisation/english/zombie_weaponized_raids_l_english.yml` does not exist; no replacement file was created.

The sabotage and scientist failure text previously asserted payload loss or consumption. Battlefield failure, success, and rejected-context text similarly asserted full payload loss or consumption. The scripts record native reservation and some internal history values, while installed raid documentation establishes only that `essential_equipment` is collected after creation. Revised text states the verified failure, release, evidence, Condemnation, and affected-state consequences without promising equipment destruction or recovery. The battlefield preparation text now uses the documented collection timing. The facility failure and breach text replaces internal response-system narration with concrete release, illness, care, evidence, and remaining-stockpile consequences. Event-owned biological consequences and all key IDs were retained.

## Audit findings

- Missing keys: none identified among the inspected raid outcome references and assigned localisation files. A full repository key inventory was outside this bounded audit.
- Duplicate keys: none in the four existing assigned files.
- Scripted localisation issues: none found in the changed keys; `[bio_facility_notice_state.GetName]` was preserved.
- Dynamic text: `$LOCATION$` and `[bio_facility_notice_state.GetName]` already provide the target/state name. The facility's 40 and 50 percent values remain static; their source constants were checked, but adding dynamic bindings requires an owning script change.
- Cross-surface mismatch: the removed resource-destruction assertions were stronger than installed native raid documentation. The event catalog workbook was not edited. The spreadsheet owner should review `cbrn_bio_facility.4.desc` if that prose is mirrored there; its final wording is in the changed localisation file.
- Encoding: the four inspected files retain UTF-8 BOM. No encoding concern found.
- Prose: vagueness was reduced in rejected-context and scientist failure text; bloat and repetition were removed from battlefield outcome lists; obvious implementation explanations such as response tracking and national record were removed; long administrative phrases were simplified; style repairs keep concrete actor and consequence language. No em dash or semicolon was introduced.
- Sourced quotations: none in the inspected or changed raid text. No quotation was edited.

## Evidence and validation

- Offline wiki: `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, Bindable localisation lines 260-275, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`; Quick checklist lines 59-72 for BOM. The live `hoi4.reference_context`, `reference_search`, and `reference_read` routes worked.
- Installed documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md`, lines 167-180, revision `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e`. It says required equipment is collected after raid creation. It does not define completed-outcome destruction or cancellation refunds.
- Source branches inspected: `common/raids/biological_sabotage_raids.txt`, `common/raids/016_brilliant_scientist_biological_raids.txt`, `common/scripted_effects/biological_battlefield_effects.txt`, `common/raids/biological_facility_recovery_raids.txt`, `common/scripted_effects/biological_facility_capture_effects.txt`, and the two linked event-bridge files. Facility failure dispatches an accidental release and leaves remaining material; battlefield failure can leave evidence and Condemnation; invalid battlefield context has no release.
- Read-only MCP event traces for `biological_native_raid_bridge.2`, `chaosx.nr16.951`, and `biological_native_raid_bridge.4` returned `EVENT_INSPECTED_PARTIAL` at revision `c667b1897a5180f60b8895da5d08653ca6a4387b25419e98251c72bdfa1545df`. The sabotage trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5805886cd0a7a95589e5e5968a125f27fd08f9f67cc4ea72f28fcb74c40d077/6ce53a1397015f17b070233e2096d68fe8b48773318238c94bb6969644ad9e2a/event-trace-c667b1897a51.json`. The bounded sabotage neighborhood render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d62cfbdda2a0549f9acc9827358a6012c3fa98059aab67e03010e0c5e2f08d2b/883032449d1315d825e1d15818d8544bbcae3abd6eafbf76dafb3ccfbdbda9c8/event-neighborhood-c667b1897a51.json`. These inspect/render results establish graph coverage only; they do not settle native equipment retention or in-game text layout.
- Checked BOM and duplicate keys in each assigned existing file; all four had BOM and no duplicate keys. `git diff --check` was clean. No gameplay, workbook, or live-game validation was performed because this patch changes only localisation and live gameplay belongs to the user.

## Remaining uncertainty

Native raid equipment destruction, return, and cancellation behavior is not documented by the installed raid source and was not inferred from internal bookkeeping. The production raid tooltip layout and exact in-game wrapping were not available through a raid-specific MCP render route. A standalone Technology Tree Viewer is not exposed in the tool list; no technology surface was changed here. No new plan addendum was needed.
