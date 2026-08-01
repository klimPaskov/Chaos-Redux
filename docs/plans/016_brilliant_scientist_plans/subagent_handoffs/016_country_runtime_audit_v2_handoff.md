# Event 016 Kruger State country-package audit v2

Date: 2026-08-01

Scope: static and runtime-contract audit of the KRG country package and the host-to-Kruger State formation paths. This handoff is limited to the country package, its project-derived military contract, and containment/formation cleanup. No gameplay files were patched in this audit.

## Executive disposition

The static KRG package is broadly covered: the tag, country definition, dormant history, fixed Warren Kruger character, route portraits and flags, 100-focus tree, route AI plans, project-force equipment/technologies, localisation, and static map data are present. The package is intentionally dormant until a formation or takeover path activates it.

The blocking unresolved issue is country instantiation for the charter, rebellion, and enclave routes. `brilliant_scientist_form_kruger_state_from_verified_plan` requires `KRG = { exists = no }`, then transfers states directly with `set_state_owner_to = KRG` and `set_state_controller_to = KRG` before entering a `KRG = { ... }` scope. The formation path contains no `release`, `release_puppet`, `create_dynamic_country`, or `change_tag` operation. The vanilla effects documentation defines `set_state_owner_to` only as assigning the owner of a state, while `release` and `create_dynamic_country` are the documented country-instantiation effects. Because KRG history has no state cores, this direct assignment is not a proved way to instantiate a playable country and may no-op or leave formation in an invalid scope. Parent implementation must design and validate an explicit instantiation transaction before claiming sovereign formation complete.

This is a runtime-contract finding, not a definitive claim about every engine build. No game launch was performed, and the installed read-only tools cannot prove the dynamic country transition.

## Country-package coverage checklist

| Surface | Status | Evidence and action |
| --- | --- | --- |
| Tag registration | Covered | `common/country_tags/016_brilliant_scientist_country.txt:8` registers `KRG = "countries/Kruger State KRG.txt"`. Vanilla tag/history/country scans found no KRG collision. Workshop-wide collision scan remains unresolved because the prior scan timed out. |
| Country definition and graphics | Covered | `common/countries/Kruger State KRG.txt` contains western European graphics and a stable color. KRG route cosmetics are in `common/countries/016_brilliant_scientist_cosmetics.txt`. |
| Dormant history | Intentional but formation-sensitive | `history/countries/KRG - Kruger State.txt:9-15` uses bootstrap capital state 1, dormant OOB, zero research slots, zero stability/war support, and neutral 100 politics. This is safe only while KRG is never statically instantiated outside the runtime formation path. |
| Dormant OOB | Covered | `history/units/016_brilliant_scientist_dormant.txt` is an empty dormant package; no free starting army is granted by static history. |
| Leader and identity | Covered at static layer | `common/characters/016_brilliant_scientist_characters.txt` defines fixed `KRG_warren_kruger` and institutional `KRG_continuity_network`. Runtime promotion in `common/scripted_effects/016_brilliant_scientist_country_effects.txt:15` adds the sovereign role; no random leader-name pool is used. |
| Advisors/scientist | Covered at static layer | `common/scripted_effects/016_brilliant_scientist_effects.txt` adds Kruger advisor and scientist roles at runtime. See the scripted `recruit_character` risk below. |
| State and map data | Static pass | Read-only `hoi4_map_inspect` for state 1 passed province, state-region, adjacency, supply, railway, port, and locator checks. Dynamic facility-network territory selection and ownership transfer remain untested. |
| Focus loading | Covered statically | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:20` declares `brilliant_scientist_kruger_state_focus_tree`; the tree has 100 authored focuses and runtime loading is gated by the active KRG trigger. Prior focus inspection reported 100 focuses, 0 diagnostics, and 108 connectors. |
| Decisions and missions | Present | KRG foundation, project, safeguard, foreign-integration, terminal, and evolution decision files are present under `common/decisions/`; containment outcomes call the formation or takeover effects. Runtime availability after formation is blocked by the instantiation finding. |
| Ideas and lifecycle | Covered statically | Country ideas, project-force ideas, focus ideas, and lifecycle effects are present under `common/ideas/` and `common/scripted_effects/`; starting ideas are applied by `brilliant_scientist_apply_starting_country_ideas`. |
| Project forces | Covered by contract | `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`, `common/units/016_brilliant_scientist_project_forces.txt`, and matching equipment/technology files gate materialisation by carried project history, facility state, capped receipts, and conventional guard coexistence. |
| Localisation | Static pass | `localisation/english/016_brilliant_scientist_country_l_english.yml`, focus/decision/idea localisation files cover KRG name, adjective, parties, leader, route names, ideas, focuses, decisions, and tooltips. |
| Flags and portraits | Static pass | `gfx/flags/KRG.tga` and six KRG route flags exist; KRG leader stage portraits exist under `gfx/leaders/KRG/`; the Event 016 GFX reference audit found 478 texture references and no missing files. |
| AI | Static pass | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` has formation, project, route, diplomacy, and terminal plans. A source cross-check found 97 AI-listed KRG focus IDs after plan IDs were excluded, with no missing focus IDs. Formation cannot be exercised until instantiation is fixed. |

## File-surface checklist

The core country surface is present in the following files: `common/country_tags/016_brilliant_scientist_country.txt`; `common/countries/Kruger State KRG.txt`; `common/countries/016_brilliant_scientist_cosmetics.txt`; `history/countries/KRG - Kruger State.txt`; `history/units/016_brilliant_scientist_dormant.txt`; `common/characters/016_brilliant_scientist_characters.txt`; `common/scripted_effects/016_brilliant_scientist_country_effects.txt`; `common/scripted_effects/016_brilliant_scientist_effects.txt`; `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`; `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`; `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`; KRG decision files under `common/decisions/`; KRG project-force files under `common/units/`, `common/units/equipment/`, `common/technologies/`, and `common/scripted_effects/`; Event 016 containment and KRG event files under `common/scripted_effects/` and `events/`; and the Event 016 localisation/interface/GFX files.

No missing static KRG file surface was found. The missing surface is an explicit country-instantiation step in the fixed-tag formation transaction, not a missing file.

## Missing or stale surfaces

1. Formation instantiation is unresolved at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:753-850`. The state transfer helper starts at line 617 and writes `set_state_owner_to = KRG` and `set_state_controller_to = KRG` at lines 630-631. The form helper checks `KRG = { exists = no }` at line 763 and then immediately transfers the capital and selected states. There is no documented country creation or release effect in this path.
2. The KRG history file has no state-level cores. Any release-based repair must explicitly account for the target capital/core and the autonomy state, and must be validated against the vanilla release semantics before touching the map transaction.
3. Workshop collision status is unresolved because the prior broad scan timed out. Vanilla installation scans found no KRG collision. A bounded workshop scan or an explicit collision record is still needed before final tag-uniqueness claims.
4. The installed technology viewer is not a usable completion proof. `hoi4_tech_inspect` returned `TECH_INSPECTED_PARTIAL` for the portal technology with 651 workspace technologies, 1,787 aggregate issues, and helper projections deferred. There is no installed Technology Tree Viewer. Event 016’s direct source cross-check did find all referenced `brilliant_scientist_*_tech` IDs defined exactly once.

## Map, state setup, and transfer safety

Static state 1 is valid according to the read-only map artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbbe03105f5ba527b1faf42488ffe2b661096a60e5381acf13555708523e2d9f/3b07280913b263a7a33b11800ec480c31e01a347344411bd6121b413bc8d67b3/map-inspect.7a97dc33e0aa6656.json`. The territory planner and capital selection logic are present in `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` and the country effects file. The planner distinguishes primary facility, connected facility, prototype works, port/rail hub, and takeover capital priorities in accordance with the spec.

The transfer helper cores only the charter route’s selected states and the frozen formation capital for rebellion/enclave; other selected states become claims or occupied territory. This is directionally correct, but all dynamic runs remain untested because the target KRG country may not exist when the first owner transfer executes. The parent should run a dry-run/review/apply/post-validation sequence around any fix and retain recovery evidence for failed formation.

Takeover is structurally safer because `brilliant_scientist_transform_host_into_kruger_state` retains the existing host tag and map, then applies KRG government, leader, ideas, guard/project packages, focus tree, and cleanup. It still needs a live scenario check for host army retention and old-host flag cleanup.

## Politics, leader, portrait, flag, advisor, and party issues

The fixed leader contract is respected: Warren Kruger is a named character, runtime role promotion uses the same character, and the continuity-network portrait is institutional rather than a personal random-name pool. Party names, route blocs, country name/adjective keys, and route cosmetic flags are present in `localisation/english/016_brilliant_scientist_country_l_english.yml` and the cosmetic country file.

The dormant country history has no static leader and zero stability/war support. That is intentional for a dormant tag but would be an invalid playable start if KRG leaked into the map before the runtime initializer. The initializer applies the government, fixed leader, roles, ideas, research slots, diplomacy, and project state after formation.

One engine/style risk remains at `common/scripted_effects/016_brilliant_scientist_effects.txt:2594`: `brilliant_scientist_appoint_kruger_from_opening` calls `recruit_character = KRG_warren_kruger` inside a scripted effect. Existing repository guidance treats scripted-effect/on-action recruitment as unsafe; this was not changed because it belongs to the opening chain and a safe replacement requires parent-wide role-creation review. It is a secondary risk, not the formation blocker.

## Focus, decisions, ideas, and asset issues

The 100-focus tree is individually authored, route-gated, and localised. Static focus inspection found no diagnostics. AI plans reference existing focus IDs and route-specific triggers. KRG decision files cover foundation, clone/machine, paleo/xeno, portal/temporal, canonical/exotic, foreign integration, safeguard, and terminal surfaces. No missing icon references were found in the Event 016 GFX audit.

Starting ideas are applied by `brilliant_scientist_apply_starting_country_ideas` and include the laboratory-state, inherited portfolio, fragmented-command, experimental-supply, and formation-specific scientific-exodus concepts. Lifecycle effects and cleanup calls exist. The remaining issue is execution order: those effects are only reached after the country scope is valid.

## Starting military, technology, industry, supply, and production

The static history grants no army, equipment, manpower, production lines, or research slots. The runtime package provides a capped conventional laboratory guard and only materialises project-derived formations when exact project history, matching facility flags, operational state, and receipt guards are present. The project-force units are inactive in the normal designer, and their equipment is non-interchangeable and deployment-gated.

`brilliant_scientist_inherit_limited_former_host_technology` grants baseline infantry/support technology and a narrow former-host subset rather than the full host tree. Research slots and project capabilities are rebuilt by the runtime initializer. This matches the spec, but the zero-slot dormant history makes any pre-formation KRG start non-playable by design.

The project-force triggers distinguish paleogenetics from xenobiology and require matching reserve/hatchery or vat/control-center facilities. Temporal forces require the temporal synchronization/debt/anchor history. The force package includes transaction and materialisation receipt guards, so no static infinite duplication was found.

## AI and playability

AI route plans exist for charter, rebellion, enclave, takeover, project deployment, diplomacy, and terminal routes. Route-specific weights and focus availability are present, and no missing KRG focus reference was found. The decisive playability risk is formation instantiation: AI can reach a formation outcome whose target country scope is not guaranteed to exist. Do not close the country audit until a formation scenario confirms that KRG receives the intended states, capital, cores/claims, leader, ideas, focus tree, research slots, supply, and project package.

## Containment formation and cleanup

Containment effects route partial uprising, full rebellion, and charter outcomes to `brilliant_scientist_form_kruger_state_from_verified_plan` and institutional takeover to `brilliant_scientist_transform_host_into_kruger_state` (`common/scripted_effects/016_brilliant_scientist_containment_effects.txt:370,390,432`). The route identity cleanup effect now clears `brilliant_scientist_route_sovereign_directorate` alongside the other sovereign-route flags in `common/scripted_effects/016_brilliant_scientist_country_effects.txt:894`; no additional local cleanup patch was necessary.

Project on-actions retry deferred force packages on state-control changes and clear project/war/capitulation state in `common/on_actions/016_brilliant_scientist_project_on_actions.txt`. Machine-opponent and capitulation cleanup hooks are present in `common/on_actions/016_brilliant_scientist_kruger_state_on_actions.txt`. Live verification is still required for state transfer, old-host residual flags, event targets, and project-force receipt cleanup.

## Required parent follow-up

1. Resolve the fixed-tag formation transaction before claiming charter, rebellion, or enclave playability. Compare a validated `release`/autonomy-free sequence, a `create_dynamic_country` sequence, or another approved engine-supported instantiation path against vanilla documentation and existing map ownership. Preserve capital/facility selection and ensure the target scope exists before any `set_state_owner_to` call.
2. Re-run a bounded tag-collision check over approved workshop paths and record the result.
3. Exercise at least one formation and one takeover scenario in the user-owned live session. The agent must not launch HOI4; this handoff records the source-level and read-only checks only.
4. Revisit `recruit_character` in the opening scripted effect with the country/character implementation owner. Do not silently rewrite it as part of the formation fix.
5. If the instantiation repair changes state cores, claims, autonomy, or country flags, update the Event 016 country package spec/plan and perform map post-validation with rollback/recovery evidence.

## Validation and limitations

Read-only checks completed: required offline wiki and vanilla documentation review; vanilla KRG tag scan; static focus/AI cross-reference (100 focuses, no missing AI focus IDs); Event 016 GFX texture-reference audit (478 references, 0 missing); project-force technology ID cross-reference; and `hoi4_map_inspect` for state 1. The technology inspection was partial and cannot serve as a clean tree proof. No game launch, save mutation, or runtime formation/takeover scenario was performed.

No intentional content simplification was introduced by this audit. The formation instantiation contract, workshop collision status, and live dynamic-territory/cleanup behavior remain unresolved blockers or validation gaps.
