# CXT Country Package Dynamic Audit

## Verdict

The current CXT dynamic-maintenance design is structurally in scope and preserves the static harness baseline, but completion remains conditional on the live-engine checks and cleanup items below.

The final audit pass made no gameplay or existing-documentation edits; it adds this handoff only.

## Country package coverage checklist

- Tag registration is consistent for `CXT` in `common/country_tags/chaosx_test_country.txt`, `common/countries/Chaos Redux Test Country.txt`, `history/countries/CXT - Chaos Redux Test Country.txt`, and `localisation/english/chaosx_test_country_l_english.yml`.
- The history shell is intentionally landless and dormant with neutrality at 100 percent and zero starting research slots; `chaosx_test` records the origin country and capital, switches to CXT, annexes the origin with `transfer_troops = no`, and restores the capital.
- The country localization includes the base name, adjective, definition, party names, and party long names for all four ideologies.
- The runtime flag set is present at `gfx/flags/CXT.tga`, `gfx/flags/medium/CXT.tga`, and `gfx/flags/small/CXT.tga`; no CXT leader, advisor, portrait, focus tree, decision route, or GUI surface is expected for this test shell.
- The setup creates an occupation fixture, six distinct special-facility campuses where legal states exist, CBRN doctrine and camp fixtures, the static military roster, and the stockpile/resource fixture.
- The randomized facility/state-transfer and occupation paths are source-reviewed only; they can legally terminate with fewer requested facilities if the map has no eligible state or coastal slot.

## Dynamic architecture findings

### Accepted source design

- `common/scripted_effects/chaosx_test_country_technology_effects.txt` now loops over `global.technology`, guards each entry with `has_tech = var:...`, grants with variable `set_technology`, suppresses popups, and marks the technology layout dirty only when a grant was applied. This removes the old fixed 663-entry technology snapshot.
- Special projects use `set_temp_variable = { var = ... value = sp:my_project }`, persist the object in `global.chaosx_test_country_registered_special_projects`, and consume it with `is_special_project_completed = var:...` and `complete_special_project = var:...`. No `token:sp` form is used.
- Equipment and land subunit registries carry `token:<id>` values, deduplicate with `is_in_array`, and use `GetTokenKey` through `meta_effect` where the effect field is static. Support registrations retain an aligned support-anchor array; the caller must choose a compatible line anchor.
- The generic extension registry now uses the documented tokenizable hidden-idea carrier `token:chaosx_cxt_extension_event014_cannibalism` from `common/ideas/014_cannibalism_cxt_extension_ideas.txt`. `meta_effect` resolves the carrier key and dispatches `[EXTENSION_EFFECT]_apply`, which currently reaches `chaosx_cxt_extension_event014_cannibalism_apply` in `common/scripted_effects/014_cannibalism_cxt_test_effects.txt`. This replaces the earlier unsupported raw scripted-effect token carrier.
- Initial setup completes the static projects and technologies, applies doctrine/camp/facility fixtures, fills the static stockpile, creates the 88 static unit templates and divisions, and then consumes registered content.
- Console refresh completes missing technologies, consumes registered extension/project/equipment/unit registries, refills the static and registered stockpile, and restores resources without re-running the static project list or duplicating processed registered divisions.
- Core `on_daily_CXT` restores resources and runs registered-content synchronization. Core `on_weekly_CXT` runs the dynamic technology scan once and then the stockpile refill once; weekly synchronization no longer creates registered templates or repeats project completion.
- The registry guards, processed-subunit arrays, package global flag, and static flame-tank flag make repeated registration and repeated refresh calls idempotent at source level.

### Current finding requiring parent follow-up

- `common/on_actions/014_cannibalism_on_actions.txt` still calls `chaosx_test_country_sync_registered_content` in its `on_daily_CXT` block after the package registration helper. The core CXT `on_daily_CXT` block in `common/on_actions/chaosx_test_country_on_actions.txt` already calls the same synchronizer, so an initialized CXT receives two full registered-content passes on that day. Processed units and guarded package effects prevent duplicate divisions, but registered equipment is refilled twice and extension/project loops are repeated. Remove the package-owned sync call and retain registration-only fallback before completion.

## Registration contract and first-command behavior

- A future definition-token package should call an idempotent registration wrapper from an additive `on_startup` block scoped into an existing country, preferably the current `random_country = { limit = { exists = yes } ... }` pattern, and retain an additive `on_daily_CXT` registration block for save-load repair.
- A package that only registers on `on_daily_CXT` has a documented one-day delay before a first console command can consume its entries. The Event 014 startup wrapper is intended to avoid that delay for fresh starts without assuming that dormant landless CXT is instantiated.
- Facilities, doctrines, and general systems should expose package-owned direct setup effects guarded by a stable package flag or existing state. They may use the hidden-idea extension carrier and `_apply` naming contract, or a direct startup/daily helper while the package is being integrated; recurring weekly hooks are for maintenance such as stockpile refill only.
- The Event 014 wrapper registers eight currently missing Chaos Redux subunits (`cannibal_bone_guard`, `cannibal_feast_cohort`, `cannibal_feast_guard`, `cannibal_island_reavers`, `cannibal_march_predation_column`, `cannibal_network_cadre`, `cannibal_scavenger_warband`, and `cannibal_siege_eaters`) plus four existing vanilla equipment tokens. The unrelated `common/units/014_cannibalism_irregular_infantry.txt` definition file was not edited.

## Inventory and behavior evidence

- Static special-project literals: 83, comprising 49 vanilla projects and 34 Chaos Redux projects.
- Static stockpile: 72 `add_equipment_to_stockpile` blocks, consisting of 71 concrete types (45 current non-archetype Chaos Redux equipment definitions plus 26 dependency definitions) and one registered-equipment meta loop. The four Event 014 equipment registrations are existing vanilla dependencies already represented by the static baseline.
- Static land subunits: 88 explicit unlocks/templates, split as 41 frontline and 47 support. Event 014 adds eight registered frontline entries, for 96 covered land subunits and 49 frontline plus 47 support at runtime.
- Static divisions: three per static template, or 264. Event 014 contributes three per registered template, or 24 more once processed.
- The runtime technology inspection found 663 technology database nodes in `global.technology`; the source loop is therefore no longer tied to that count.
- No bare whole-world `on_daily`, `on_weekly`, or `on_monthly` hook was found in the CXT dynamic-maintenance path. The core maintenance hooks are tag-scoped `on_daily_CXT` and `on_weekly_CXT`; Event 014 uses a bounded `on_startup` country scope, `on_daily_CXT`, and narrow lifecycle hooks.

## Official documentation versus source-only inference

### Engine or official-documentation support

- The offline Data structures page states that ideas are tokenizable, that token values can be stored in variables and arrays, and that `GetTokenKey` is intended for meta effects. It specifically recommends dummy ideas for arbitrary values, supporting the hidden-idea carrier now used by Event 014.
- The official `effects_documentation.md` documents `meta_effect` and accepts `complete_special_project = var:my_project_var`.
- The official `triggers_documentation.md` documents `is_special_project_completed = var:my_project_var`.
- The offline On actions page and vanilla examples establish that `on_startup` has no default scope and must explicitly enter a country; the current bounded `random_country` wrapper follows that pattern without requiring CXT to own a state.
- The installed dynamic-variable documentation exposes `global.technology` as a technology database array. The existing Chaos Redux technology-union helper provides a matching variable-token precedent for guarded grants.

### Source-only or unverified

- The exact runtime behavior of assigning an `sp:<project_id>` object to a temporary variable, storing that value in a global array, and later consuming it through both special-project triggers/effects is supported by the documented input forms and source pattern, but was not executed in a live HOI4 process.
- The exact runtime behavior of constructing a custom scripted-effect name from a hidden-idea token with `[EXTENSION_EFFECT]_apply` is strongly supported by the documented token/meta-effect mechanism and the dummy-idea recommendation, but remains unverified without a live save.
- The `random_country` startup registration is source-safe and avoids dormant-CXT scope assumptions, but ordering before a console command has not been validated in a live start/save path.
- Dynamic template trainability, support-anchor legality, three-division spawning, facility transfer execution, camp activation, tag-switch/annex behavior, and repeated-save refresh behavior are source-only because this audit did not launch HOI4 or run a live console session.

## MCP and validation evidence

- Read-only technology inspection was run against workspace `mod_chaos_redux_ea3b2d67c2c0`; the scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/9bfdfbabae705ea9f14c6a7d47d9bbc752953dab2d46ef42f7ee462b24f948cc/technology-scan-a5b6bbb48967.json`. The scan reports 663 technology nodes, but its validation is partial/false because helper projections were deferred and inline files were truncated.
- The technology summary render artifacts are under `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90ea57ab0f0fd8ac5421176836eb2d18007bb997a2aad71a20def7fee553b38c/`, including `technology-summary-a5b6bbb48967-manifest.json`, `.json`, `.svg`, and `.png`; these are inspection evidence, not a full runtime pass.
- Read-only map inspection was run against the current workspace and found 1,081 states, 304 regions, and 534 ports. The map inspection reported unrelated global map diagnostics in `map/buildings.txt`, including invalid building positions and port adjacency; no map file was changed by this audit.
- The state-layer map render with coastlines, ports, state buildings, supply nodes, and railways passed its offline validation and is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41f03b07c45491bb51246c8b4abac0c265ddb0fd30dd96739bc0b548952b80c3/eed8acfc8e698d4721a9406ed7669fb8ca28fdcd3d207cc37af3f3986ddde0ac/map-state.png` with companion JSON/HTML artifacts.
- No live HOI4 execution was performed. An Event Viewer pass was not rerun in this final one-action handoff turn; Event 014 lifecycle and registration behavior therefore remain source-only for this audit.
- No probability audit was required because the audited CXT surfaces contain no AI strategy factor, `ai_will_do`, `ai_chance`, MTTH, or other weighted target change.

## Documentation accuracy

- The current `docs/testing/chaosx_test_country.md` still describes the obsolete raw `token:cannibalism_apply_cxt_test_content` carrier and calls the extension carrier unresolved. Its contract section must be refreshed to describe the hidden-idea carrier and `_apply` dispatcher before the parent claims documentation completion.
- `docs/plans/chaosx_test_country_plans/subagent_handoffs/dynamic_architecture.md` likewise still names `token:<scripted_effect_name>`, labels the old carrier unresolved, and lists weekly registered synchronization even though `chaosx_test_country_sync_dynamic_content` now performs only the technology scan. These are documentation defects, not a reason to revert the current source design.
- The accurate future-package requirements are startup pre-registration plus daily repair for definition tokens, direct idempotent setup for facilities/doctrines/general systems, and weekly maintenance only for recurring refill work.

## Current relevant file surface

- `common/on_actions/chaosx_test_country_on_actions.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `common/scripted_effects/chaosx_test_country_effects.txt`
- `common/scripted_effects/chaosx_test_country_technology_effects.txt`
- `common/scripted_effects/chaosx_test_country_special_project_effects.txt`
- `common/scripted_effects/chaosx_test_country_stockpile_effects.txt`
- `common/scripted_effects/chaosx_test_country_unit_effects.txt`
- `common/scripted_triggers/chaosx_test_country_triggers.txt`
- `common/script_constants/chaosx_test_country_constants.txt`
- `common/scripted_effects/014_cannibalism_cxt_test_effects.txt`
- `common/ideas/014_cannibalism_cxt_extension_ideas.txt`
- `common/country_tags/chaosx_test_country.txt`
- `common/countries/Chaos Redux Test Country.txt`
- `history/countries/CXT - Chaos Redux Test Country.txt`
- `localisation/english/chaosx_test_country_l_english.yml`
- `gfx/flags/CXT.tga`, `gfx/flags/medium/CXT.tga`, and `gfx/flags/small/CXT.tga`
- `docs/testing/chaosx_test_country.md`
- `docs/plans/chaosx_test_country_plans/subagent_handoffs/dynamic_architecture.md`

## Changed files and ownership

- This final audit action added `docs/plans/chaosx_test_country_plans/subagent_handoffs/country_package_dynamic_audit.md` only.
- The other listed dynamic files contain the current parent/shared worktree implementation and earlier bounded CXT audit comments; this subagent did not commit or revert them.
- The unrelated Event 014 unit-definition file and unrelated dirty assets were not touched.

## Blockers and remaining risks

1. Remove the duplicate Event 014 daily synchronizer call.
2. Refresh the two stale dynamic-architecture documents to the hidden-idea carrier contract and current weekly call order.
3. Run the live-engine acceptance path for startup registration, `e chaosx_test`, refresh, daily repair, weekly maintenance, special-project variable arrays, dynamic extension dispatch, template trainability, support anchors, stockpile refill, facility/camp state setup, and tag-switch/annex behavior.
4. Treat the unrelated map diagnostics as an external baseline risk; they were not caused or fixed by this CXT audit.
5. Global registries intentionally persist for the save and have no cleanup/reset path; stale entries after content removal or mod changes can dispatch invalid carriers or preserve obsolete definitions.
6. A future package that skips startup registration incurs the documented one-day delay, and a future support package that supplies an incompatible anchor can fail to produce a legal template.

No CXT gameplay file was changed in this final handoff action, and no claim of full engine validation is made.

## Parent resolutions after audit

- The Event 014 daily hook no longer performs a second full synchronization every day. The extension-registration helper now returns `chaosx_test_country_extension_registration_added`, and Event 014 runs immediate synchronization only when that value shows a newly inserted carrier; the core CXT daily hook owns recurring synchronization.
- `docs/testing/chaosx_test_country.md` now documents the modifier-free hidden-idea carrier, `_apply` dispatcher, startup registration, conditional daily repair, and current weekly call order.
- `dynamic_architecture.md` now records the accepted hidden-idea carrier integration and the resolved daily/weekly ownership.
- The live-engine acceptance risks, persistent-registry cleanup limitation, support-anchor responsibility, and unrelated map diagnostics remain as reported above.
