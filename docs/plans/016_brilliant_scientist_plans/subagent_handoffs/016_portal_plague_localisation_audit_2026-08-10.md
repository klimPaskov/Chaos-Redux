# Event 016 Portal Raids and Event 020 Black Plague Localisation Audit

Date: 2026-08-10

## Scope and outcome

This pass audited the player-facing localisation for `portal_raider`, `teleportation_equipment`, both native Portal Warfare raids, their target and outcome tooltips, the Black Plague weaponization special project, and the Kruger/Mengele access and completion registry. It also reconciled the Portal Raider production status in `.tmp/016_brilliant_scientist_technologies_and_units.md`.

The two raid descriptions and shared outcome tooltips now describe uncertain insertions and visible consequences directly. The raid category no longer exposes internal history or lifecycle implementation language, and its availability tooltip now matches the actual category gate. The Black Plague project description now names the six-phase work in concrete terms without revealing which alternate provider granted access.

No gameplay, model, entity, GFX, sound, tool, or spreadsheet file was changed. No fallback wording or substitute asset claim was introduced.

## Changed files and identifiers

- `localisation/english/chaosx_raids_l_english.yml`
  - `brilliant_scientist_portal_raid_available_tooltip`
  - `raid_category_brilliant_scientist_raids`
  - `tooltip_raid_category_brilliant_scientist_raids`
  - `raid_type_brilliant_scientist_portal_facility_raid_desc`
  - `raid_type_brilliant_scientist_portal_special_project_facility_raid_desc`
  - `brilliant_scientist_portal_raid_preparation_available_tt`
  - `brilliant_scientist_portal_raid_failure_actor_tt`
  - `brilliant_scientist_portal_raid_failure_target_tt`
  - `brilliant_scientist_portal_raid_limited_success_actor_tt`
  - `brilliant_scientist_portal_raid_limited_success_target_tt`
- `localisation/english/020_black_plague_weaponization_l_english.yml`
  - `black_plague_weaponization_program_desc`
- `.tmp/016_brilliant_scientist_technologies_and_units.md`
  - Quantum Transit technology-family row
  - Portal Raider unit-family row
  - reusable unit-family registry paragraph
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_plague_localisation_audit_2026-08-10.md`

## Display before and after

- Availability previously claimed that sixty Teleportation Equipment were required to open the category. The category trigger only checks Weaponized Transit Doctrine and the `Quantum Transit Raiders` template. Equipment remains a preparation requirement and is still stated in `brilliant_scientist_portal_raid_preparation_available_tt`.
- The category was called `Kruger Strategic Raids` even though the native category is available to any valid technology and template holder. It is now `Portal Warfare Raids`.
- The category tooltip previously described native reservation, cancellation, expiry, and history behavior. It now gives the six-battalion formation size, seven-day preparation time, sixty-equipment reserve, and ten-Command-Power cost.
- Both raid descriptions previously promised that Portal Raiders would materialize. They now say that the formation will attempt the breach and distinguish the state-installation raid from the exact special-project-facility extraction raid.
- Failure and limited-success tooltips previously exposed native history records and a persistent history marker. They now state damage, experience, retained control, and installation damage without implementation-facing language.
- The Black Plague description previously grouped the work under abstract vectors, risks, failures, and tradeoffs. It now names surveillance, clinical samples, transport controls, delivery, and containment.

## Audit lists

### Missing keys

None found in the assigned surfaces. The portal category, two raid types, both target names, preparation and launch requirements, four shared outcome levels, `portal_raider`, `teleportation_equipment`, the portal weaponization technology, Black Plague project, and Black Plague phase-role tokens all resolve to localisation keys.

### Duplicate keys

None found within the four inspected localisation files. The scoped Portal Raider, Teleportation Equipment, portal technology, and raid keys were also unique in the inspected English localisation set.

### Scripted localisation issues

None found. The assigned raid and technology strings do not call scripted localisation. Existing Event 020 constants, state-name tokens, formatting codes, and localisation substitutions were not changed.

### Dynamic text opportunities

- The six-battalion formation size, seven-day preparation, sixty-equipment reserve, and ten-Command-Power cost are file-scoped raid constants. A future gameplay-owner change could promote them to localisation-readable script constants, but a localisation-only pass cannot make these values dynamic safely.
- The per-battalion `portal_raider` equipment values are likewise static in player-facing text and tied to current unit/equipment definitions.
- Provider-specific Black Plague text could name Kruger or Mengele dynamically, but generic project text deliberately avoids that reveal. Adding provider-specific text would require project or scripted-localisation wiring and is not justified by this bounded pass.

### Cross-surface mismatches

- Fixed: category availability text no longer includes the equipment reserve that is checked only during raid preparation.
- Fixed: the shared failure-target tooltip no longer refers only to a facility state when it is also used by the state-installation raid.
- Fixed: the category name no longer implies that Kruger is the only possible holder.
- Verified in source: `black_plague_weaponization_directorate_has_access` covers the current Kruger host and Mengele directorate access, `black_plague_weaponization_actor_is_valid` exposes the project through either the native Event 020 state or directorate access, and completion clears the availability flag while setting `directorate_special_project_black_plague_completed`.
- Verified in source: the reusable CBRN registry suppresses the Black Plague entry after `sp:black_plague_weaponization_program` is complete.

### Encoding concerns

None. `chaosx_raids_l_english.yml`, `016_brilliant_scientist_country_l_english.yml`, `016_brilliant_scientist_projects_l_english.yml`, and `020_black_plague_weaponization_l_english.yml` all retain UTF-8 BOM encoding. They contain 105, 206, 584, and 74 localisation keys respectively, with no within-file duplicates.

### Prose-quality repairs

- Vagueness: the Black Plague project now names the work performed, and the raid category names its concrete formation and resources.
- Bloat: lifecycle and history implementation language was removed from the category and outcomes.
- Obvious explanation: no tooltip now narrates the existence of native raid history or hidden markers to the player.
- Repetition: failure and limited-success text no longer repeats the same history-record sentence.
- Overcomplication: long raid-result sentences were split where the normal and critical consequences needed separate emphasis.
- Style rules: semicolons were removed from the changed player-facing raid descriptions, uncertain outcomes no longer read as guaranteed, and internal terms such as `native raid history` and `persistent portal-raid history marker` were removed.

### Sourced quotations

No sourced or attributed quotation appears on the inspected surfaces. No quotation was changed.

## Dynamic tokens preserved

All existing dynamic state names, script-constant displays, equipment substitutions, icons, formatting codes, and scripted localisation calls in the inspected files were preserved. The changed strings contained no dynamic tokens.

## MCP and source validation

- Portal technology inspection resolved `brilliant_scientist_portal_warfare_weaponization_tech` with no blockers: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af1ced24355b454e511a4bf7e58fb5ca78b0c9a9e9984ea771bdef20720684ba/227c300390a057c438cdf46b7357d4be21351e2effb8c6ad0742b391a0595be3/technology-trace-28ecce4721e4.json`.
- Technology rendering completed with partial inventory projection and no blockers: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a8c97ffa51b5d34f3e28020319383847c30b227911e996ae891c5b648de908b/9ebc29ec7273fb9983724d3d2ab1724a251835eece66f1adda371630f66290cf/technology-technology-28ecce4721e4.png`.
- Event 016 lint returned no blocking diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd81c6baacc7bff60df69b4bcfff724e86bfdb7e74ebf968747859033d283916/a3cc955cdbd74e926152bb095315144c3731812906123865fac6a6f063126ca3/event-lint-c11a255294fb.json`.
- Event 020 lint returned no blocking diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/930af2ce05afd7a5add4d62b52a84ad97efc3774a6838a09f9d5d1e2b8e2eef5/8d48528170e2ff4b1912dc4c8ed29f085e2f97db3f8ebac2f5b83f7dd0ba8a6b/event-lint-c11a255294fb.json`.
- Event renders completed only as partial overview projections. The Event 016 and Event 020 selectors produced effectively identical overview imagery, so they are not treated as reliable proof of individual text layout or overflow.
- The installed MCP package has no special-project inspector or renderer. Black Plague visibility, availability, narrative localisation, and completion were therefore verified against source and vanilla special-project documentation only. This is not equivalent to engine or rendered special-project evidence.

## Skipped validation and remaining decisions

- No in-game validation was performed. Consumer validation belongs to the user.
- No spreadsheet comparison or edit was performed because spreadsheets were explicitly outside this task.
- Parent resolution: `brilliant_scientist_portal_warfare_weaponization_tech_desc` now states that the doctrine improves Quantum Transit Raiders and enables Portal Warfare raids against hostile installations.
- The Portal Raider model, entity, actions, and sounds remain unwired pending accepted production. Counter art is wired. No fallback production or fallback wording was approved or introduced.
- No separate mechanic plan was written because the findings did not reveal a missing mechanic within this localisation scope.

## Simplifications and blockers

The technology-description recommendation remains unapplied because of the file write failure above. The absence of a special-project MCP inspection/render route prevents engine-level display and overflow evidence for the Black Plague project. No other simplification was made.
