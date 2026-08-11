# Event 012 Africa localisation audit

Date: 2026-08-06

Status: patched with unresolved MCP presentation limits recorded below.

## Scope

This pass audited the current Event 012 English localisation and scripted-localisation sources against the linked event, decision, focus, scripted GUI, technology, unit, equipment, character, portrait, cosmetic-tag, achievement, event-log, and super-event sources.

The audit preserved concurrent work and changed only player-facing localisation plus this handoff.

## Changed files

- `localisation/english/012_africa_elephant_l_english.yml`
- `localisation/english/012_african_union_l_english.yml`
- `localisation/english/012_africa_event_log_l_english.yml`
- `localisation/english/012_africa_super_events_l_english.yml`
- `localisation/english/012_africa_world_order_l_english.yml`
- `localisation/english/012_africa_world_union_war_l_english.yml`
- `localisation/english/012_africa_achievements_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_localisation_audit_2026-08-06.md`

## Missing key list

No confirmed missing Event 012 localisation keys remain after the patch.

The audit added the missing names and descriptions for all eight strange-force subunits, all sixteen corresponding equipment archetype and variant IDs, and all eight bridge technologies. Elephant subunit, equipment, and technology text was already present.

Added key families:

- `gorilla_heavy_infantry`, `gorilla_heavy_infantry_desc`, `africa_gorilla_heavy_infantry_equipment`, `africa_gorilla_heavy_infantry_equipment_desc`, `africa_gorilla_heavy_infantry_equipment_1`, `africa_gorilla_heavy_infantry_equipment_1_desc`, `africa_gorilla_heavy_infantry_tech`, `africa_gorilla_heavy_infantry_tech_desc`
- `pan_sappers`, `pan_sappers_desc`, `africa_pan_sappers_equipment`, `africa_pan_sappers_equipment_desc`, `africa_pan_sappers_equipment_1`, `africa_pan_sappers_equipment_1_desc`, `africa_pan_sappers_tech`, `africa_pan_sappers_tech_desc`
- `stone_cohorts`, `stone_cohorts_desc`, `africa_stone_cohorts_equipment`, `africa_stone_cohorts_equipment_desc`, `africa_stone_cohorts_equipment_1`, `africa_stone_cohorts_equipment_1_desc`, `africa_stone_cohorts_tech`, `africa_stone_cohorts_tech_desc`
- `riverborn`, `riverborn_desc`, `africa_riverborn_equipment`, `africa_riverborn_equipment_desc`, `africa_riverborn_equipment_1`, `africa_riverborn_equipment_1_desc`, `africa_riverborn_tech`, `africa_riverborn_tech_desc`
- `forest_giants`, `forest_giants_desc`, `africa_forest_giants_equipment`, `africa_forest_giants_equipment_desc`, `africa_forest_giants_equipment_1`, `africa_forest_giants_equipment_1_desc`, `africa_forest_giants_tech`, `africa_forest_giants_tech_desc`
- `oracle_recon`, `oracle_recon_desc`, `africa_oracle_recon_equipment`, `africa_oracle_recon_equipment_desc`, `africa_oracle_recon_equipment_1`, `africa_oracle_recon_equipment_1_desc`, `africa_oracle_recon_tech`, `africa_oracle_recon_tech_desc`
- `disaster_wardens`, `disaster_wardens_desc`, `africa_disaster_wardens_equipment`, `africa_disaster_wardens_equipment_desc`, `africa_disaster_wardens_equipment_1`, `africa_disaster_wardens_equipment_1_desc`, `africa_disaster_wardens_tech`, `africa_disaster_wardens_tech_desc`
- `plague_carriers`, `plague_carriers_desc`, `africa_plague_carriers_equipment`, `africa_plague_carriers_equipment_desc`, `africa_plague_carriers_equipment_1`, `africa_plague_carriers_equipment_1_desc`, `africa_plague_carriers_tech`, `africa_plague_carriers_tech_desc`

The three decision IDs `africa_world_prepare_continental_war_restore`, `africa_world_prepare_continental_war_break_compact`, and `africa_world_prepare_continental_war_settlement` intentionally use the shared explicit `name = africa_world_prepare_continental_war` and `desc = africa_world_prepare_continental_war_desc` keys. They are not missing-key defects.

## Duplicate key list

None. The final Event 012 scan found 19 English localisation files, 4,361 keys, 4,361 unique keys, and zero duplicate groups.

## Scripted localisation issue list

None confirmed.

- Four Event 012 scripted-localisation files define 46 unique methods with no duplicate method names.
- Their 872 literal `localization_key` branches resolve to 666 unique English keys, with zero missing branch keys.
- All 43 custom `GetAfrica...` methods referenced by Event 012 localisation resolve to a defined method.
- No direct `§` or `£` format character occurs in the scripted-localisation source.

## Dynamic text opportunities

No new dynamic localisation was required for the patched unit, equipment, or technology names.

Existing dynamic actor, country, state, route, cost, timer, action-result, constitutional, and super-event clauses were preserved. The 102 action contracts retain all six expected fields, giving 612 of 612 name, selector, description, full-result, partial-result, and failure-result keys.

Actions 85, 87, and 92 still summarize some thresholds in broad terms. A future owning decision pass could expose the existing constants directly if exact threshold transparency is desired.

## Public names, characters, portraits, flags, and achievements

- All 48 Event 012 cosmetic country IDs have direct public `NAME`, `DEF`, and `ADJ` values, giving 144 of 144 required fields.
- The 16 priority-member public names are direct English values: Asante, Oyo, Sokoto, Kanem-Bornu, Manden, Kongo, Buganda, Aksum, Harar, Kilwa, Nubia, Luba, Lunda, Great Zimbabwe, Merina, and Zulu.
- No Event 012 localisation value uses `GetTag` or `GetTagDef`.
- Twenty-two character name references resolve to localisation, and all 22 referenced portrait sprites exist in interface source.
- All 44 Event 012 achievements retain `_NAME`, `_DESC`, and `_tooltip` coverage, giving 132 of 132 required fields.
- All 394 focus IDs retain name and description coverage.
- Event source contains 964 explicit Event 012 localisation references, with zero missing keys.

## Afaan Oromoo and source-language safeguard

The exact required strings occur once each in runtime localisation:

- `africa_absurd_regnal_name_01: "qaama saalaa koo xuuxaa"`
- `africa_absurd_regnal_name_02: "haadha kee waliin wal qunnamtii saalaa raawwadhe"`

They occur only as visible values in `localisation/english/012_africa_priority_member_characters_l_english.yml`. Neither string occurs in runtime script, identifiers, filenames, tags, sprite names, asset names, character keys, technology keys, unit keys, achievement keys, or debug names.

No additional obscene English or source-language ruler or court string was found in the runtime Event 012 surface. The two required strings remain pending native-speaker review for idiom, dialect, and offensiveness as recorded in the language protocol. Their exact spelling was preserved.

## Sourced quotation preservation

The four selected super-event quotations and attributions remain byte-for-byte unchanged in localisation:

- Marcus Garvey: `building up for themselves a great nation in Africa.`
- General Act of the Conference at Berlin: `to enable them, if need be, to make good any claims of their own.`
- Carl von Clausewitz: `War is a mere continuation of policy by other means.`
- Percy Bysshe Shelley: `Nothing beside remains.`

Only two original dynamic super-event clause strings were repunctuated. No sourced quotation, attribution, dynamic token, or formatting code was altered.

## Prose-quality repairs

### Vagueness

The six world-order leader descriptions no longer call their subjects generic fictional leaders or refer to a technical package. They now identify the constituencies, settlements, and institutions that support each leader's authority.

### Bloat

The host-succession event, event-log, and decision descriptions were shortened. Internal phrases about generations, relinking, reloading a focus tree, host pointers, and hidden annexation chains were replaced with the actual constitutional result, inherited obligations, and land or sovereignty limits.

### Obvious explanation

`Event 12`, `Event 013`, `refusal flag`, and `super-event package gate` wording was removed from player-facing text. The text now states the visible action, cost, recovery period, risk, or constitutional consequence.

### Repetition

The priority-member promotion action now uses one consistent public result across its action name, selector, full result, and long description.

### Overcomplication

The compact-host recognition, succession, and final-union descriptions were split into direct sentences with concrete actors and consequences.

### Style-rule repair

All sentence semicolons and em dashes were removed from the 19 Event 012 English localisation files. The patch preserves dynamic tokens and formatting codes.

Changed prose keys outside the added unit families:

- `chaosx.nr12.232.d`, `chaosx.nr12.233.d`
- `africa_host_transfer_actions_category_desc`, `africa_host_transfer_designate_successor_desc`, `africa_host_transfer_commit_successor_desc`
- `africa_priority_member_natural_disaster_launch_tt`
- `africa_promote_compact_host_desc`, `africa_decline_compact_promotion_desc`, `africa_reopen_compact_promotion_docket_tt`
- `africa_action_result_recover_failed_host_proof_failure`, `africa_select_recover_failed_host_proof_desc`
- `africa_action_result_promote_priority_member_package_full`, `africa_action_name_promote_priority_member_package`, `africa_select_promote_priority_member_package`, `africa_select_promote_priority_member_package_desc`
- `africa.event_log.host_succession.detail`, `africa.event_log.host_succession_suspended.detail`, `africa.event_log.host_succession_terminal.detail`
- `africa_super_event_constitution_uncommitted`, `africa_super_event_scramble_expedition_named`
- `africa_world_middle_east_leader_desc`, `africa_world_europe_leader_desc`, `africa_world_asia_leader_desc`, `africa_world_north_america_leader_desc`, `africa_world_south_america_leader_desc`, `africa_world_oceania_leader_desc`
- `africa_world_package.6.d`, `africa_world_package.750.d`, `africa_world_package.756.d`, `africa_world_package.759.t`, `africa_world_package.759.d`
- `africa_world_commit_terminal_political_proof`, `africa_world_commit_terminal_political_proof_desc`, `africa_world_prepare_terminal_handoff`, `africa_world_prepare_terminal_handoff_desc`
- `africa_the_world_is_one_tooltip`

## Cross-surface mismatch notes

- Older localisation handoffs that report 17 or 18 Event 012 English files are stale. The current runtime count is 19 because the event-log and super-event files are present.
- The event catalog workbook was not edited or audited in this pass. Any workbook field that mirrors the changed succession, promotion, leader, final-union, or achievement wording should be checked by the spreadsheet owner before final completion.
- Several world-order strings still use `package`, `ledger`, and `dossier` as in-world institutional language. Clear implementation-only uses were removed, but a wholesale terminology replacement would be a broad prose and design pass outside this narrow patch.
- Model entity IDs and sprite tokens are not themselves localisable. Their visible subunit, equipment, and technology consumers now have complete text coverage.

## File encoding concerns

None found. All 19 Event 012 English localisation files begin with UTF-8 BOM bytes `EF BB BF`. No `:0` versioned key was introduced.

## MCP evidence and limitations

The HOI4 MCP routes were used as required, but several reports are partial because this workspace is very large.

- Event trace for `chaosx.nr12.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/163d7d71115ade5c86cab605afbfb0762f983244fc3a3e77b7dee9c3cef0e9cb/f0b46de0ac638ca059e6e1f57a07c02e2a6ef3046f9cf514155ee98ff1041b31/event-trace-c5c2ec44234b.json`. The tool returned `EVENT_INSPECTED_PARTIAL`.
- Event options render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9e7e58dfbe94ad50dd0145c943331db0c9598dae58111fb8786784026956b74/703918d7084595066f32c1cffe3411a258a837861f42aee18ee859a702829e96/event-options-c5c2ec44234b.json`. The bounded render selected three nodes and omitted the rest of the shared graph, so it is not full event-chain proof.
- Continental focus inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a819aea021bccec3205dc465c567ebc3bd64a13b5129534c3e6683e10687103f/ce255cd45f8db89b3e0cf30dcb39f7ec6478175d0e3e0ed6952a3a6c531d79e8/focus-inspect.69fa499baef61c9e.json`. It resolved all 276 titles in that tree. Its 14 blocking diagnostics concern focus structure or layout, not missing localisation.
- Continental focus render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5354be44bdebfae5e0ac0bb273305da46160cb441de7721088bcf66738958eb/6ebc11d7a56a98d75b1319b5829855dd39e4829d928c43f29e641dd066a77ab7/africa_continental_focus_tree.focus.json`.
- A batch inspection of all eight linked Event 012 focus files did not complete after several minutes and was terminated. The seven priority-member and external-continent trees therefore have complete source key coverage but no completed per-tree MCP artifact from this pass. Source-only coverage is not treated as equivalent visual evidence.
- GUI inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef13d49fab7b5804599a7b3a09131a00a8141d265ad60999c1607a433fac4fba/af82ec5d9c6f4ab4cf3a9d2d71ed7f167906f5616bfb27b2011e901ef19c3841/gui-inspect.a142ec8b74fc5678.json`.
- GUI long-text and missing-localisation state matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/091da5a1082f0a86e1178cc8159300c1c05246bd84abe2e109a7515c511e4f54/47f5fe9466c67c55c2f3916b94aa50ea7dbcbb6e5c0c284605717f3086354a45/africa_charter_window-state-matrix.json`.
- GUI validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc7df104f3a53764e837578f6d9a905d31febb3d000a83311c5fe3d542c0c8c2/0e52d63453bb3724f1b77cc636b8c7df50385824d8954ddd17e21cad6f55aee9/africa_charter_window-validation.json`. The selected `africa_charter_window` render completed, but the MCP source graph reports 1,900 workspace-wide blocking diagnostics and 178 visible overlaps. The long-text and missing-localisation comparison reported zero changed pixels, so this pass cannot honestly certify overflow or missing-key visual behaviour from the renderer. Source references are complete, but visual acceptance remains unresolved.
- Technology scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daeee01592438761022052ec59f7a038331779d62f7b1af05014b79394e90bc5/cc87d3369425c0657da78f494ecc90f5e1a71c2d486d5ecf3bca7758cae5bea6/technology-scan-ac04d6ae63bc.json`. The tool returned `TECH_INSPECTED_PARTIAL` because helper projections were deferred.
- Technology render for `africa_gorilla_heavy_infantry_tech`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11765ec74d988e706fd301a8c74eb0f84a3f9242b77d7b39fa56f879e2486dfb/bf2ea0b8c911025f6411e9a05cb9e39bcbff9ac1ed2a3c6c77034301321f3f8d/technology-technology-ac04d6ae63bc.json`. The render reports `sourceAccurate: false`, so the source coverage scan remains necessary and the render is not full technology-tree proof.

## Meaningful validation

- Event 012 localisation catalog: 19 files, 4,361 keys, zero duplicate groups, zero versioned `:0` keys.
- Explicit source-reference scan: 113 linked source files, 2,103 references, 1,758 unique references, zero missing keys after excluding the GUI window identifier `africa_charter_window`, which is not a localisation key.
- Event references: 964 explicit references, 863 unique keys, zero missing.
- Scripted localisation: 46 unique methods, 872 branches, zero missing literal branch keys, zero unresolved custom `GetAfrica...` methods.
- Focuses: 394 IDs, zero missing names or descriptions.
- Actions: 102 contracts, 612 expected fields, zero missing.
- Achievements: 44 IDs, 132 expected fields, zero missing.
- Unit, equipment, and technology consumers: 36 IDs, 72 expected name and description fields, zero missing.
- Cosmetic countries: 48 IDs, 144 expected public name fields, zero missing.
- Character and portrait wiring: 22 character name references resolve and 22 portrait sprite references exist.
- Afaan Oromoo runtime scan: exactly one occurrence of each approved string and none outside localisation.

## Skipped meaningful validation

- Hearts of Iron IV was not launched. Repository policy assigns live game validation to the user.
- The seven non-continental focus-tree MCP inspections did not produce completed artifacts because the batch call did not finish and had to be terminated.
- The GUI renderer did not produce trustworthy isolated overflow or missing-localisation evidence because the selected states rendered with zero changed pixels amid broad source-graph blockers.
- The event and technology MCP reports are partial, as described above.
- The event catalog workbook was not inspected or edited because this task did not route spreadsheet ownership or invoke the workbook workflow.

## Unresolved wording decisions and remaining gaps

- Native-speaker review remains required for the exact idiom, dialect, and offensiveness of the two approved Afaan Oromoo strings. No substitute or extra vulgar string was added.
- Decide whether `package`, `ledger`, and `dossier` should remain as the world-order system's public institutional vocabulary. This patch removed only clearly implementation-facing uses.
- The GUI owner must review the linked overlap evidence and obtain a render where long-text and missing-localisation states are visibly distinct before claiming layout acceptance.
- The focus owner must complete MCP inspection and rendering for the seven linked trees that did not return artifacts in this pass.
- The spreadsheet owner should reconcile any workbook text mirroring the changed player-facing strings.

No gameplay mechanic, dynamic token, sourced quotation, portrait, flag, model, sprite, event ID, focus ID, decision ID, action ID, technology ID, unit ID, or achievement ID was changed.

No fallback or gameplay simplification was introduced.
