# Event 006 IW-177 Fiji country-package audit

Date: 2026-07-27

Scope: Country-package coverage, setup safety, cleanup safety, and playability for FIJ/IW-177 after the current Pacific package tranche.

This handoff is limited to FIJ and does not implement FORM-39 content, add a new country package, or promote FIJ to runtime content attestation.

## Audit baseline

The audit used `AGENTS.md`, the Chaos Redux subagent, event, focus-tree, decisions, event-assets, and improvement-loop skills, the required offline Paradox wiki pages under `paradox_wiki/`, the relevant vanilla Hearts of Iron IV documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, and the vanilla FIJ country, state, history, flags, and localisation precedents.

The installed HOI4 MCP package exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved tooling limitation rather than a claim of technology completion.

## Coverage checklist

| Surface | Result | Evidence or remaining issue |
| --- | --- | --- |
| FIJ tag and package id | PASS | `FIJ` resolves to `countries/Fiji.txt`; IW-177 is `constant:independence_wave_package_id.iw_177 = 177`; `is_independence_wave_fij_package` requires original tag FIJ, active country, and package id IW-177. |
| State and capital | PASS with narrow footprint | Vanilla state `636-Fiji.txt` is the sole reserved anchor and capital; the package requires state 636 to be owned and controlled and records the living former host. No extended territory is claimed. |
| Reservation group | PASS | IW-177 uses `RG-PACIFIC-ISLANDS`; state 636 and the group are reserved through the region-13 package registry, preventing FIJ/SAM/FSM-style collision. |
| Politics and parties | PASS | FIJ starts democratic with the configured 44/12/34/10 popularity split, elections enabled, four localized party names, and a centrism country leader. |
| Leader and portrait | CONDITIONAL | `FIJ_independence_wave_founding_congress_chair` is Ratu Sir Lala Sukuna with a male leader record and GFX/DDS consumer; the source is a circa-1940s National Archives of Fiji/Wikimedia image against a 1936-centered baseline and remains provisional pending the parent source/date gate. |
| Flags and country visuals | PASS for reused vanilla shelf | Vanilla FIJ flag triplets are present for all four ideologies and three sizes; no new flag identity is invented. |
| Focus framework | PASS for current framework | `independence_wave_focus_tree` imports the FIJ root and capstone; the six connected shared FIJ branch focuses are included by prerequisite-connected shared-focus loading. The full-framework assignment is used because vanilla FIJ starts on the generic tree. |
| Decisions and mission | PASS | The FIJ founding-congress category, one 250-day mission, six staged decisions, costs, cancel triggers, timeout failure, AI weights, and localisation are present. |
| Ideas | PASS | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` have lifecycle transitions, allowed checks, modifiers, and shared idea icons. |
| Dynamic force and equipment | PASS with runtime gate | IW-177 maps to `coastal_maritime`, force level 53, with local infantry/coastal guard priorities and the p177 force mapping; the shared loader materializes the force only when command structure and roster readiness are true. Vanilla FIJ has no OOB, production lines, or large starting army to preserve. |
| Technology | INCOMPLETE TOOLING | Vanilla FIJ begins with the ordinary small-island baseline; the package does not add a bespoke technology branch. No installed Technology Tree Viewer is available, so prerequisite/unlock rendering could not be independently inspected. |
| Industry, supply, and navy | PASS with vanilla baseline | State 636 retains vanilla infrastructure 2, naval base 1, local supply 0, and one victory point; the package AI prioritizes dockyards, infrastructure, fuel, convoys, and coastal defense instead of adding broad map changes. |
| AI and playability | PASS with risks recorded | Three FIJ AI strategy blocks cover survival, founding restraint, and severe-host-threat defense; focus and decision AI weights are present. No country-specific focus-order script was added. |
| Formable and host admission | BLOCKED BY DESIGN | Setup selects `melanesian_federation` and requires `independence_wave_fij_melanesian_route_adapter_complete`; no FORM-39 carrier/member transaction, consent adapter, X-tag, or PNG/WPG member package is installed. FIJ therefore remains fail-closed. |
| Cleanup and rollback | PATCHED | FIJ has its own `independence_wave_cleanup_iw_177_fiji`; the shared FORM-48 cleanup guard no longer includes FIJ. |
| Runtime attestation | BLOCKED | The FIJ package tranche explicitly leaves FIJ out of canonical content attestation until the Melanesian adapter and source/date gate are resolved. |

## File-surface checklist

The following current package surfaces were inspected and are present.

- `common/script_constants/006_independence_wave_pacific_constants.txt`: pressure, ledger, politics, duration, modifier, and FIJ AI constants.
- `common/script_constants/006_independence_wave_package_constants.txt`: IW-177 package id and shared package registration values.
- `common/ideas/006_independence_wave_pacific_ideas.txt`: the three FIJ ideas and their allowed checks.
- `common/ai_strategy/006_independence_wave_pacific.txt`: survival, restraint, and host-threat strategies.
- `common/decisions/categories/006_independence_wave_pacific_categories.txt`: `independence_wave_fij_founding_congress_category`.
- `common/decisions/006_independence_wave_pacific_decisions.txt`: the FIJ mission and six decision ids from `independence_wave_fij_convene_constituent_congress` through `independence_wave_fij_ratify_island_compact`.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`: exact FIJ identity, lifecycle, setup, formable, host, force, and final-completion gates.
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`: FIJ setup, politics, pressure and ledger adapters, focus rewards, force dispatch, final validation, FIJ cleanup, and the corrected FORM-48 cleanup guard.
- `common/national_focus/006_independence_wave_pacific_focus.txt`: six connected FIJ shared focuses.
- `common/national_focus/006_independence_wave_focus.txt`: full framework import and assignment surface.
- `common/characters/006_independence_wave_pacific_characters.txt`: `FIJ_independence_wave_founding_congress_chair`.
- `interface/006_independence_wave_pacific_portraits.gfx`: `GFX_portrait_FIJ_independence_wave_founding_congress_chair`.
- `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`: current provisional portrait consumer.
- `localisation/english/006_independence_wave_pacific_l_english.yml`: FIJ country parties, leader, ideas, category, mission, decisions, focuses, and tooltips.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`: IW-177 package loader and state 636 anchor reservation.
- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt`: IW-177 plan, reservation-group, FIJ-tag, and state-636 availability checks.
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`: exact IW-177 package availability.
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`: Melanesian family registry profile without a FIJ-admission adapter.
- `history/states/636-Fiji.txt`: vanilla map anchor, ownership, core, manpower, port, infrastructure, supply, and victory point precedent.
- `history/countries/FIJ - Fiji.txt`: vanilla FIJ start used as the setup baseline.
- `common/country_tags/00_countries.txt` and `common/countries/Fiji.txt`: vanilla tag registration and country definition precedent.

## Findings by package surface

### Cleanup and FORM-48 safety patch

Before this audit, `independence_wave_dispatch_pacific_package_cleanup` sent FIJ/IW-177 through `independence_wave_form48_origin_cleanup` because the outer OR included `original_tag = FIJ` with package id IW-177.

That was unsafe because FORM-48 is the Pacific Regional Federation route owned by HBX/IW-184, HAW/IW-173, and FSM/IW-179, while FIJ selects the separate FORM-39 Melanesian Federation family.

The outer OR in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` now contains only `HBX` plus IW-184, `HAW` plus IW-173, and `FSM` plus IW-179 before calling `independence_wave_form48_origin_cleanup`.

The FIJ-specific cleanup call remains separate and still clears the IW-177 mission, six decisions, three ideas, FIJ variables, FIJ lifecycle flags, formable selection, the adapter flag, excluded-route flags, the full-framework tree, and the FIJ leader.

### Setup, host, and map safety

`can_initialize_independence_wave_iw_177_package` requires the exact FIJ package, Southeast/East Asia/Oceania region, regional depth, port/island archetype, a state-636 anchor owned and controlled by FIJ, a living former host different from ROOT, and capital state 636.

The region-13 registry reserves only state 636 and the `RG-PACIFIC-ISLANDS` group, so this package does not silently claim Fiji's unrelated overseas or hypothetical Melanesian member territory.

The vanilla state remains a small island with 180,000 manpower, infrastructure 2, a level-1 naval base in province 4286, local supply 0, and one victory point; no map rewrite was performed.

The host settlement path uses the protected former-host pointer and the living-host checks, so a destroyed or missing former host cancels the bilateral settlement decision rather than dereferencing a stale target.

The `independence_wave_fij_settle_colonial_accounts` decision intentionally has no capital-control requirement because it is a diplomatic former-host settlement; this asymmetry is recorded for review, not changed without design direction.

### Politics, leader, portrait, flags, and parties

`independence_wave_initialize_fij_politics` sets democratic government and elections, applies the configured 44/12/34/10 popularity distribution, assigns all four FIJ party names, promotes the Sukuna character to centrism, and sets provisional authority.

The leader is a male country-leader character with a large portrait reference, a documented name and description, and an expiry date; no advisor, operative, commander, or high-command asset is claimed by IW-177.

The current DDS/GFX exists, but the source/date handoff identifies it as a circa-1940s archival image against the event's 1936-centered baseline, so parent source acceptance remains a runtime admission gate.

Vanilla FIJ democratic, communist, neutrality, and fascist normal, medium, and small flags are present and reused; no fictional flag or unreviewed historical symbol was added.

### Focus, decisions, ideas, and localisation

The six FIJ focuses are connected through the full-framework root and capstone, use FIJ package and capital/host gates, and have localized names, descriptions, tooltips, and existing shared icons.

The founding-congress category is visible only for the exact FIJ package and setup flag; its 250-day mission has activation, cancellation, timeout, and failure effects, and its six decisions expose staged congress, communal, labor/shipping, host-settlement, coastal-guard, and island-compact work.

The ideas transition from `fij_unsettled_congress` to `fij_communal_charter` and finally `fij_coastal_guard_compact` when the congress, communal, and defense flags reach their corresponding thresholds.

The FIJ localisation block covers country parties, Sukuna, all three ideas, the category and description, the mission and failure tooltip, all six decisions, all six decision tooltips, and all six focus keys and tooltips.

### Military, technology, industry, supply, and production

The force mapping row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` identifies IW-177 as `coastal_maritime`, force level 53, with local infantry/coastal guard, engineers, reconnaissance, coastal signals, and maintenance priorities; artillery and logistics remain depot-gated and no armor is introduced.

The shared starting-force loader is called only when the Pacific command structure and roster are ready, which avoids an unscoped free-formation effect on an incompletely initialized package.

The vanilla FIJ history has no OOB and only a small equipment/convoy baseline, so no major army, navy, technology, production-line, or industry expansion was invented in this country audit.

The installed MCP has no Technology Tree Viewer, so no independent technology prerequisite or unlock render was available; this remains unresolved and must not be represented as a technology-tree pass.

### AI and playability

`independence_wave_fij_coastal_congress_survival` prioritizes army, infantry and support equipment, convoys, fuel, infrastructure, and dockyards after package setup.

`independence_wave_fij_founding_restraint` discourages opportunistic wars while the country is not under severe host threat or regional-power conditions, and `independence_wave_fij_host_threat` switches to emergency army and coastal-bunker priorities under severe threat.

The constants centralize FIJ AI priorities and the focus/decision files include AI weights; a bespoke country-specific focus-order script is not present, so the generic full-framework AI remains a playability risk for future balancing.

The `recruitable_population_factor` modifier used by the shared communal idea is documented in vanilla as a state-scoped modifier; its country-idea impact should be confirmed during live balancing before it is treated as a global manpower bonus.

### Formable and content-attestation gating

IW-177 selects `constant:independence_wave_formable_family.melanesian_federation` and requires `independence_wave_fij_melanesian_route_adapter_complete` in `has_prepared_independence_wave_iw_177_package_setup`.

The current registry has the FORM-39 profile only; it does not provide the named FIJ/PNG/WPG member transaction, consent-led adapter, X-tag or route identity, collision protections, or member packages needed for safe admission.

The setup effect intentionally does not set the adapter flag, while FIJ cleanup clears it if a future adapter is installed; this is the correct fail-closed behavior and was not bypassed.

The FIJ tranche also remains outside canonical runtime content attestation until the FORM-39 adapter and the source/date gate are resolved.

## Changed files and identifiers

The gameplay change made for this audit is in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`.

The changed behavior is the FORM-48 cleanup guard in `independence_wave_dispatch_pacific_package_cleanup`; the FIJ/IW-177 AND clause was removed from the OR, with no tag, state, leader id, party id, focus id, localisation key, or formable id changed.

The required audit handoff is this file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fiji_country_audit_2026_07_27.md`.

## Validation evidence

The corrected cleanup block was inspected directly and now lists only HBX/IW-184, HAW/IW-173, and FSM/IW-179 before `independence_wave_form48_origin_cleanup`.

A targeted repository scan found the FIJ adapter flag only as a setup prerequisite and a FIJ-cleanup clear operation; there is no accidental setup writer that would bypass the FORM-39 gate.

Targeted file-existence, identifier, localisation, portrait-GFX, focus-import, state-636, package-registry, and FIJ decision/idea scans were run against the current checkout.

Vanilla FIJ tag, country, history, state, flag, and localisation precedents were inspected, and the required offline wiki and vanilla documentation references were consulted.

No Hearts of Iron IV executable or live save was launched, in accordance with repository instructions; no in-game validation is claimed.

## Remaining blockers and simplifications

- FORM-39 Melanesian Federation remains fail-closed because the adapter, carrier/member transaction, X-tag identity, member packages, consent rules, and collision tests are absent.
- The FIJ Sukuna portrait is present but remains conditional on the documented circa-1940s source/date acceptance gate.
- FIJ has no bespoke advisor, operative, commander, or technology tree content; this is the current package scope, not an assertion that those systems are complete.
- The installed MCP has no Technology Tree Viewer, so technology-tree rendering and comparison remain unresolved.
- No map rewrite, extended territory, large army, major production expansion, or FORM-39 route content was added.

No other country-package gameplay patch was made during this audit.
