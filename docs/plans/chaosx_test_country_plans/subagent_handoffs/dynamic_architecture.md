# CXT Dynamic Architecture Handoff

## Scope and outcome

The CXT harness now has a true runtime technology scan and bounded opt-in registries for the surfaces for which HOI4 exposes no documented database enumeration. The change owns only CXT scripted effects, the CXT on-action file, and the CXT testing documentation. No technology, project, equipment, unit, or unrelated definition file was edited.

## Files changed

- `common/scripted_effects/chaosx_test_country_technology_effects.txt`
- `common/scripted_effects/chaosx_test_country_special_project_effects.txt`
- `common/scripted_effects/chaosx_test_country_stockpile_effects.txt`
- `common/scripted_effects/chaosx_test_country_unit_effects.txt`
- `common/scripted_effects/chaosx_test_country_effects.txt`
- `common/on_actions/chaosx_test_country_on_actions.txt`
- `docs/testing/chaosx_test_country.md`
- `docs/plans/chaosx_test_country_plans/subagent_handoffs/dynamic_architecture.md`

`common/script_constants/chaosx_test_country_constants.txt` was reviewed but did not need a new tuning value; the existing three-division count and stockpile amount remain the source of truth.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `chaosx_test_country_complete_all_technologies` | Country scope; no caller inputs. Enumerates `global.technology`. | Grants each missing technology at level 1 with no popup and marks the technology layout dirty only when a grant was applied. | Initial setup, console refresh, weekly dynamic sync. |
| `chaosx_test_country_register_extension_effect` | Country scope; temporary `chaosx_test_country_registration_extension_effect = token:<hidden_idea_carrier>`. | Adds a unique carrier to `global.chaosx_test_country_registered_extension_effects` and reports whether the entry was newly inserted. | Package wrapper called from bounded `on_startup` registration plus additive `on_daily_CXT` repair. |
| `chaosx_test_country_apply_registered_extension_effects` | Country scope; no caller inputs. | Resolves each hidden-idea carrier with `GetTokenKey` and meta-dispatches the matching `<carrier>_apply` package setup effect. | Initial setup, console refresh, daily registered sync. |
| `chaosx_test_country_register_special_project` | Country scope; temporary `chaosx_test_country_registration_special_project = sp:<id>` special-project scope. | Adds a unique project object to `global.chaosx_test_country_registered_special_projects`. | Caller-owned bounded `on_startup` registration plus additive `on_daily_CXT` repair, or one-time package setup. |
| `chaosx_test_country_complete_registered_special_projects` | Country scope; no caller inputs. | Completes every not-yet-completed project in the persistent registry using `complete_special_project = var:...`. | Static all-project helper, console refresh, daily registered sync. |
| `chaosx_test_country_register_equipment` | Country scope; temporary `chaosx_test_country_registration_equipment = token:<id>`. | Adds a unique equipment token to `global.chaosx_test_country_registered_equipment`. | Caller-owned bounded `on_startup` registration plus additive `on_daily_CXT` repair, or one-time package setup. |
| `chaosx_test_country_fill_registered_equipment` | Country scope; no caller inputs. | Uses `GetTokenKey` through `meta_effect` to add the configured stockpile amount for every registered equipment token. | Static stockpile fill, therefore initial setup, refresh, and weekly refill. |
| `chaosx_test_country_register_frontline_subunit` | Country scope; temporary `chaosx_test_country_registration_frontline_subunit = token:<id>`. | Adds a unique frontline token to `global.chaosx_test_country_registered_frontline_subunits`. | Caller-owned bounded `on_startup` registration plus additive `on_daily_CXT` repair, or one-time package setup. |
| `chaosx_test_country_register_support_subunit` | Country scope; temporary support token plus `chaosx_test_country_registration_support_anchor = token:<anchor>`. | Adds aligned support and anchor entries to two persistent global arrays. | Caller-owned bounded `on_startup` registration plus additive `on_daily_CXT` repair, or one-time package setup. |
| `chaosx_test_country_create_registered_unit_roster` | Country scope; no caller inputs. | Processes unhandled registry entries, unlocks each subunit, creates a recruitable template, spawns three full divisions, and records processed tokens in CXT-local arrays. | Initial setup, console refresh, and daily registered sync. |
| `chaosx_test_country_sync_registered_content` | Country scope; no caller inputs. | Runs registered package setup effects, project completion, equipment refill, and unit creation. | Initial setup, `on_daily_CXT`, console refresh, and first-time package repair. |
| `chaosx_test_country_sync_dynamic_content` | Country scope; no caller inputs. | Runs the guarded runtime technology scan. The outer weekly hook then runs the static and registered stockpile helper once. | `on_weekly_CXT`. |

The static 83-project, 71-equipment, and 88-subunit inventories remain the baseline. They are not described as runtime enumeration and are not replaced by empty registries.

## Constants and tuning plan

No new constants were needed. Existing `chaosx_test_country.stockpile_amount`, `chaosx_test_country_count.research_slots`, and file-scoped `@CXT_TEST_UNIT_COUNT` continue to control the existing fixture. The registration layer deliberately carries definition identity, not balance values. If registered templates later need a different division count or stockpile amount, add one CXT script constant and route both static and registered paths through it rather than adding per-package literals.

## Event target and cleanup plan

No event targets are introduced. Technology uses the engine database array, while extension/project/equipment/subunit registries are save-global arrays because their registrations must survive until CXT is selected. Entries are deduplicated and intentionally persist for the save; there is no automatic cleanup path because removing an entry would make previously registered content disappear from the test harness. A future explicit debug reset command could clear these arrays if save-local experimentation requires it, but that is outside this bounded change.

## Migration plan

1. The generated 663-line technology grant was replaced by `for_each_loop = { array = global.technology }`, following the existing `union_compatible_researched_technologies_from_donor` variable-token pattern.
2. The explicit project, equipment, and unit baselines remain in place so current behavior is preserved.
3. Future package owners add a modifier-free hidden-idea carrier, a matching idempotent `<carrier>_apply` setup effect, a bounded-country `on_startup` registration block, and an additive `on_daily_CXT` repair block. The repair path synchronizes immediately only when the extension-registration helper reports that it inserted a new carrier.
4. A support subunit registration must provide a compatible line anchor; the caller owns that compatibility decision because the engine exposes no generic subunit metadata collection.

## Evidence, risks, and blockers

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` documents `global.technology` as an array of technology database objects and `researched_techs` as a country technology array.
- `.../documentation/script_collection_input.md` and `common/collections/_documentation.md` document no special-project, equipment, or subunit collections.
- `.../documentation/effects_documentation.md` documents variable forms for `complete_special_project`, while `add_equipment_to_stockpile` has a static `type` field; the equipment loop therefore uses a meta effect and `GetTokenKey`.
- The existing `common/scripted_effects/chaosx_dynamic_effects.txt` technology-union helper proves the guarded variable-token `set_technology` pattern used here.
- The setup-effect extension bus uses a modifier-free hidden idea as the documented tokenizable carrier. `GetTokenKey` supplies the stable carrier id and the meta effect appends `_apply`; the exact dispatch remains source-only until live consumer validation.
- The weekly scan touches the installed technology array only for CXT, skips already completed technologies with `has_tech`, and marks the tree layout dirty only when at least one grant was applied, limiting recurring effect churn.
- The mandatory read-only HOI4 technology scan and summary render inspected the current runtime database at 663 technology nodes. The scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/9bfdfbabae705ea9f14c6a7d47d9bbc752953dab2d46ef42f7ee462b24f948cc/technology-scan-a5b6bbb48967.json`, and the summary render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/technology-summary-a5b6bbb48967-manifest.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/technology-summary-a5b6bbb48967.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/technology-summary-a5b6bbb48967.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/technology-summary-a5b6bbb48967.png`. Both MCP results are partial and validation is false because helper projections are deferred; this is engine inspection evidence, not a full runtime pass.
- The registration contract is opt-in, not magical enumeration. Each content package owns a bounded `random_country` startup registration plus an idempotent daily fallback, avoiding a dependency on a dormant CXT country object. This gives first-command coverage when the startup action runs; the remaining ordering is source-only until a live save validates that the startup action precedes the console effect in every supported start path.
- Future facility, doctrine, and general-system additions use package-owned idempotent `_apply` helpers through the same hidden-idea extension registry; no separate database array is required.

## Parent follow-up

Review the runtime CXT hook in a live save, then require every future content package to use the documented hidden-idea carrier, `_apply` setup effect, startup registration, and conditional daily repair contract. Keep the static baselines for reviewability, and do not call the full static roster from recurring hooks.

## Parent integration after handoff

The parent replaced the provisional raw scripted-effect token with a documented tokenizable carrier. Each package defines a modifier-free hidden idea, registers that idea token at startup and from its tag-specific daily repair hook, and provides a country-scoped idempotent scripted effect whose name is the carrier id plus `_apply`. CXT resolves the idea token through `GetTokenKey`, appends `_apply` in a meta effect, runs the package setup, and then processes any project, equipment, or unit definitions registered by that setup.

The weekly dynamic helper now performs only the runtime technology scan, followed by one stockpile refill in its on-action caller. The package daily fallback invokes the registered-content synchronizer only when `chaosx_test_country_extension_registration_added` reports that a new carrier was inserted; ordinary recurring synchronization remains owned by the core CXT daily hook.
