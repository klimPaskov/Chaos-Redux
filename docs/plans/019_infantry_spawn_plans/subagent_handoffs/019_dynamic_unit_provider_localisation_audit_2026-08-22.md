# Event 19 Dynamic Unit Provider Localisation Audit

Date: 2026-08-22

Auditor: `chaosx_localisation_auditor`

## Outcome

The dynamic provider presentation migration is localisation-complete for all 19 registered providers after a narrow repair to two live decision-cost selectors and several cost-description clarity fixes.

All providers `501-514`, `518`, and `520-523` return exactly three positive presentation tokens: family name, request cost, and sustainment cost. All 57 top-level token keys exist once, and all 57 nested localisation references resolve once. No valid provider row can reach the generic ledger-backed profiles.

Provider `523` is covered by `Cannibal Irregular Hosts`, a request description that names its equipment and manpower obligations, and a sustainment description that states those field obligations are already carried by the Formation Ledger.

## Sources Reviewed

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Event 19 overview, unit-family coverage, specification parts 2, 6, and 7, and the dynamic-provider API completion handoff
- Offline Paradox wiki pages for localisation, events, decisions, data structures, triggers, effects, modifiers, scopes, on actions, ideas, and AI
- Vanilla `documentation/loc_objects_documentation.md`, `documentation/loc_formatter_documentation.md`, `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, and `common/decisions/_documentation.md`
- The Event 19 provider owners, muster board, first-reception, derivative-package, event, scripted-localisation, and English-localisation sources named in the audit scope

## Provider Presentation Contract Evidence

The provider callback census found one `chaos_unit_family_provider_<ID>_event19_get_presentation` callback for each of these IDs:

`501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 518, 520, 521, 522, 523`

Each callback assigns exactly these three temporary variables, using its own ID-matched token keys:

- `infantry_spawn_family_provider_name_loc_token = token:chaos_unit_family_<ID>_name_loc`
- `infantry_spawn_family_provider_request_cost_loc_token = token:chaos_unit_family_<ID>_request_cost_loc`
- `infantry_spawn_family_provider_sustainment_cost_loc_token = token:chaos_unit_family_<ID>_sustainment_cost_loc`

The source census returned `providers=19 errors=0`. The localisation resolution census returned `topTokens=57 missingTop=0 nestedRefs=57 badNested=0`.

Owner source locations are:

- `501-503`: `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`
- `504-510`, `522`: `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`
- `511`: `common/scripted_effects/002_zombie_outbreak_effects.txt`
- `512-513`: `common/scripted_effects/012_africa_effects.txt`
- `514`: `common/scripted_effects/010_death_effects.txt`
- `518`: `common/scripted_effects/018_resources_found_cave_effects.txt`
- `520`: `common/scripted_effects/020_black_plague_effects.txt`
- `521`: `common/scripted_effects/cbrn_doctrine_effects.txt`
- `523`: `common/scripted_effects/014_cannibalism_effects.txt`

## Consumer Evidence

- Muster board: `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt` resets the three provider tokens, dispatches the owner callback, requires all three values to be greater than zero, appends aligned name/request/sustainment arrays, and copies the selected row into the three `infantry_spawn_muster_gui_selected_family_*_loc_token` variables.
- Decisions: the selected request and sustainment base, blocked, and tooltip cost keys render the matching request or sustainment token with `GetTokenLocalizedKey`. The title renders the selected name token.
- First reception: `common/scripted_effects/019_infantry_spawn_evolution_effects.txt` validates all three provider tokens and freezes the name token into `infantry_spawn_first_family_reception_name_loc_token`. Event `chaosx.nr19.105` renders that exact variable in its description and accepting-option tooltips.
- Natural derivative report: `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt` validates all three provider tokens and freezes the name token into `infantry_spawn_natural_derivative_report_family_name_loc_token`. Event `chaosx.nr19.206` renders that exact variable and clears it after acknowledgement.
- Derivative identity: both derivative release paths validate all three provider tokens and copy the name token into `infantry_spawn_derivative_family_name_loc_token`. The record is asserted positive and later cleared. No current player-facing localisation reads the stored identity token; this is a correct identity record, not a display fallback.

The old `GetInfantrySpawnSelectedFamilyRequestCost`, `GetInfantrySpawnSelectedFamilySustainmentCost`, and management-cost display selectors have no remaining source references. `GetInfantrySpawnFirstFamilyReceptionPicture` remains a deliberate visual-profile selector and does not select family names or costs.

The generic `infantry_spawn_family_request_cost_profile_ledger_backed` and `infantry_spawn_family_sustainment_cost_profile_ledger_backed` keys have definition-only references. None of the 57 valid provider tokens points to either key. The positive-token gate prevents a valid provider row from falling back to a generic family or cost.

## Provider 523 Evidence

`common/scripted_effects/014_cannibalism_effects.txt` exposes provider `523` only while the cannibal system is active, cleanup is incomplete, and an eligible state exists. It is spawn-only, does not use the training path, and exposes sustainment only for live family divisions while the system remains active. Provider settlement succeeds without an immediate provider stockpile debit because exact equipment and manpower obligations are recorded through its Formation Ledger manifest. The Event 19 wrapper still charges the dynamically displayed political-power and command-power request overhead. The patched request and sustainment prose states this split directly.

## Audit Lists

### Missing keys

None.

### Duplicate keys

None among the 57 provider presentation keys or within `019_infrantry_spawn_l_english.yml`.

### Scripted localisation issues

- Fixed `infantry_spawn_request_selected_anomalous_family_cost`, which still called deleted `GetInfantrySpawnSelectedFamilyRequestCost` scripted localisation.
- Fixed `infantry_spawn_sustain_selected_family_cost`, which still called deleted `GetInfantrySpawnSelectedFamilySustainmentCost` scripted localisation.
- No obsolete hardcoded family name or cost selector remains in `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`.

### Dynamic text opportunities

- Replaced the static `2,000` Alien Laser Weapons request and sustainment display with `constant:alien_infantry_landing.reserve_equipment`.
- No other in-scope provider cost value remains statically duplicated where an existing variable or constant is available.

### Cross-surface mismatches

- Fixed the sustainment decision description calling every selected provider a `nonhuman host`; provider `523` represents human cannibal irregulars.
- No remaining mismatch was found between provider action type and the neutral decision wording. The request decision says it will `call` or `create` a formation rather than claiming every provider trains one. Provider-specific cost text distinguishes training, manifestation, landing, and Formation Ledger obligations.

### File encoding concerns

None. `localisation/english/019_infrantry_spawn_l_english.yml` retains UTF-8 BOM, contains no `:0` keys, contains no indented key definitions, and has no malformed key lines in the in-scope scan.

### Prose-quality issues and repairs

- Vagueness: ledger-backed text now says which obligations the Formation Ledger carries and whether any resources are paid immediately.
- Bloat: removed implementation-like `provider settlement` phrasing from valid ledger-backed provider costs.
- Obvious explanation: no title-restating or button-narrating sentence was added; request and sustainment text retains only cost and operational consequence.
- Repetition: repeated generic debit language was replaced with short provider-specific host, brood, battalion, or cannibal-obligation wording where that distinction matters.
- Overcomplication: split semicolon-linked ledger explanations into direct sentences.
- Style-rule repair: removed player-facing semicolons from the inspected ledger-backed profiles and replaced the inaccurate `nonhuman` category label.

### Sourced quotations

No sourced or attributed quotation appears on the inspected provider, decision, first-reception, or derivative-report surfaces. No quotation was edited.

## Patch

### Changed files

- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_dynamic_unit_provider_localisation_audit_2026-08-22.md`

`common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt` was inspected but did not require a patch.

### Changed localisation keys

- Live selectors and decision description: `infantry_spawn_request_selected_anomalous_family_cost`, `infantry_spawn_sustain_selected_family_cost`, `infantry_spawn_sustain_selected_family_decision_desc`
- Dynamic Alien Infantry values: `infantry_spawn_family_request_cost_profile_alien_infantry`, `infantry_spawn_family_sustainment_cost_profile_alien_infantry`
- Provider sustainment prose: `infantry_spawn_family_sustainment_cost_profile_mutated_zombie`, `infantry_spawn_family_sustainment_cost_profile_elephant`, `infantry_spawn_family_sustainment_cost_profile_africa_strange_force`, `infantry_spawn_family_sustainment_cost_profile_greater_ghost`, `infantry_spawn_family_sustainment_cost_profile_cave_brood`, `infantry_spawn_family_sustainment_cost_profile_rat_brood`, `infantry_spawn_family_sustainment_cost_profile_chaos_assault_battalion`, `infantry_spawn_family_sustainment_cost_profile_cannibal_irregular`, `infantry_spawn_family_sustainment_cost_profile_ledger_backed`
- Provider request prose: `infantry_spawn_family_request_cost_profile_mutated_zombie`, `infantry_spawn_family_request_cost_profile_elephant`, `infantry_spawn_family_request_cost_profile_africa_strange_force`, `infantry_spawn_family_request_cost_profile_greater_ghost`, `infantry_spawn_family_request_cost_profile_cave_brood`, `infantry_spawn_family_request_cost_profile_rat_brood`, `infantry_spawn_family_request_cost_profile_chaos_assault_battalion`, `infantry_spawn_family_request_cost_profile_cannibal_irregular`, `infantry_spawn_family_request_cost_profile_ledger_backed`

### Display before and after

Before the patch, the two live custom-cost keys called scripted-localisation functions that no longer existed after the provider migration, so their cost text could render unresolved. They now read the exact selected provider request or sustainment token already cached by the Muster Board. Alien Infantry cost text now tracks its source constant instead of duplicating `2,000`. Ledger-backed providers now tell the player that exact obligations are recorded in the Formation Ledger and distinguish those obligations from immediately paid request overhead.

All dynamic tokens, formatting codes, resource icons, cost constants, timers, event identities, and proper names were preserved. The only categorical term removed was the inaccurate word `nonhuman`. No exception or quotation uncertainty remains.

## MCP Evidence and Limitations

`hoi4.event_inspect` lint for `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL` with no report issues in the bounded graph:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d7915c1fbae30668f31aa542185fa67dbcdaabc80a7fc2310f75e5cc667c6b0/82c2dc0bae2da60119cfe044ae150c04711146c3a3299e2a95cd4c5bf3e3848d/event-lint-43f28961e452.json`

Source-linked option renders were generated for the two provider-name event consumers:

- Event `chaosx.nr19.105`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76ecb5dc36a52714482da9b191948ce6880908426d9bf2922247b0d89d92f426/134dd574e48ae37f962ee99d3e529c2a6f6ba5bb8b81c3900fe6279dd08b634d/event-options-43f28961e452.json`
- Event `chaosx.nr19.206`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4437c32c187386bb58e526baaf76fb6139b182cd21469786676b3fb1a1e9b8d7/c4a9d6c1e938f017e3ae4daf0dc640e20a597e66d9e9acb835e4e82e53562e60/event-options-43f28961e452.json`

Both renders returned `EVENT_RENDERED_PARTIAL`. The server deferred workspace-wide helper projections and lifecycle passes because of workspace size. The event renderer provides event-chain diagrams rather than an in-game localised event-dialog layout, so it cannot establish pixel-level localisation overflow. This is the exact MCP blocker; source coverage and token resolution were verified separately and are not presented as equivalent visual evidence. Event 19 has no scripted GUI in this audit scope.

## Meaningful Validation

- Provider callback census: 19 callbacks, exactly three ID-matched presentation assignments each, zero errors.
- Token resolution census: 57 top-level keys, 57 nested references, zero missing or multiply defined references.
- Consumer trace: verified positive-token gates and correct name/request/sustainment assignment for the Muster Board, event 105, event 206, and both derivative identity paths.
- Cost trace: compared provider-owned payment/evaluation callbacks with the displayed request and sustainment profiles, including Alien Infantry's landing reserve and provider 523's Formation Ledger obligations.
- Localisation integrity: UTF-8 BOM present; 3,025 parsed keys; zero duplicate keys; zero invalid key forms in the file.
- Obsolete-selector scan: no remaining source reference to the deleted selected-family cost functions or management-cost selector.

No in-game test was run because live consumer validation belongs to the user under repository rules. Pixel-level event-dialog overflow validation was unavailable through the installed event MCP route. There is no scripted GUI to inspect or render.

## Unresolved Wording Decisions, Simplifications, and Blockers

No unresolved wording decision or unapproved simplification remains in the bounded localisation scope. The only evidence limitation is the MCP partial-analysis and event-dialog overflow limitation recorded above.
