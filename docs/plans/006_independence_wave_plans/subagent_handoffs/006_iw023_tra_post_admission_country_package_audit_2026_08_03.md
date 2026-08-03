# IW-023 TRA post-admission country-package audit

## Scope and authority

This is a source-only country-package audit of the currently admitted Event 006 IW-023 Transylvania package.

The review uses `006_iw023_tra_runtime_scenario_admission_reconciliation_2026_08_03.md` as the current admission authority and treats `006_iw023_tra_independent_source_admission_audit_2026_08_03.md` as historical evidence where it is superseded by the current dispatch source.

No gameplay, country, tag, state, focus, decision, AI, asset, or localisation source was changed by this audit.

The package is admitted in the current source: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` includes `iw_023` in the runtime content-attestation whitelist and the normal and scenario preflight branches require the exact TRA origin contract.

The review does not claim a live game run, save/load test, release transfer, AI simulation, or FORM-08 mutation proof.

## Country package coverage checklist

| Surface | Current source coverage | Result |
|---|---|---|
| Tag and identity | Vanilla `TRA` remains the carrier; `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` requires `original_tag = TRA` and package id `iw_023`. | PASS |
| Duplicate country registration | No mod-owned TRA country/history/leader replacement was found; vanilla `countries/Transylvania.txt`, TRA history, and TRA character roster remain authoritative. | PASS |
| Current map anchor | `state = 84` is the exact required capital and anchor; state 76 is optional compact territory. | PASS |
| Host survival | `ROM = 46` is the protected former-host state in `006_current_installed_map_package_bindings.csv`; runtime requires the former host and protected state pointers. | PASS in source; live transfer untested |
| Starting force | IW-023 maps to `mountain_frontier`, military tradition 68, reinforcement mask 654, and no navy/air inheritance. | PASS in source; live force receipt untested |
| Ideas and ledgers | `tra_divided_border_authority`, `tra_danube_settlement`, five route ideas, and frontier/federal ledgers are installed and cleaned by package effects. | PASS |
| Politics and parties | Five TRA route installers set ideologies, party names, popularity, elections, route ideas, and ledger changes. | PASS in source |
| Focus ownership | TRA keeps `austro_hungarian_releasable_focus`; Event 006 attaches the additive shared overlay and does not call `load_focus_tree`. | PASS |
| Decisions and mission | One timed mission and eleven authored TRA decisions are registered, gated, localised, and removed by cleanup. | PASS |
| AI | TRA strategy file covers survival, army, artillery, defence, infrastructure, production, emergency response, and former-host restraint. | PASS in source; semantic balance risk noted below |
| Localisation and icons | TRA package names, ideas, mission, decisions, tooltips, and reused Event 006 decision sprites are present. | PASS |
| Cleanup | TRA package cleanup removes package-local missions, decisions, ideas, ledgers, route flags, lifecycle flags, and AI; generic reset clears shared focus, force, network, and FORM-08 runtime. | PASS in source |
| Portraits and flags | Vanilla TRA flag, Iuliu Maniu portrait, and recruited character assets are preserved; no fictional portrait or invented symbol is introduced. | PASS |

## File surface checklist

The admitted package surface is present across the following files and identifiers.

- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`: `is_independence_wave_tra_package`, `is_independence_wave_exact_package_iw_023_tag_available`, `is_independence_wave_iw_023_runtime_ready`, `can_initialize_independence_wave_iw_023`, `has_prepared_independence_wave_iw_023_setup`, and `has_complete_independence_wave_iw_023_setup`.
- `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt`: `independence_wave_setup_iw_023_transylvania`, five TRA government installers, ledgers, route lifecycle, and `independence_wave_cleanup_iw_023_transylvania`.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: runtime content attestation, exact normal preflight, and exact scenario preflight for `iw_023`.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt`: package loader, reservation, and random candidate selection for `iw_023`.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt`: exact TRA availability, state 84 anchor, and reservation-group checks.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`: IW-023 binding `TRA`, anchor `84`, optional extension `76`, host `ROM`, protected state `46`, group `RG-DANUBE-BORDERLAND`.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`: IW-023 `mountain_frontier`, tradition `68`, and five reinforcement paths.
- `common/scripted_effects/006_independence_wave_force_package_effects.txt` and `common/scripted_effects/006_independence_wave_force_effects.txt`: mapping probe/application and dynamic starting force.
- `common/ideas/006_independence_wave_transylvania_ideas.txt`, `common/decisions/006_independence_wave_transylvania_decisions.txt`, and `common/decisions/categories/006_independence_wave_transylvania_categories.txt`: package ideas, mission, decisions, and category.
- `common/ai_strategy/006_independence_wave_transylvania.txt`: TRA AI priorities and restraint strategy.
- `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/austro_hungarian_releasable_shared.txt`, and `common/scripted_effects/006_independence_wave_focus_effects.txt`: additive focus carrier and framework assignment.
- `localisation/english/006_independence_wave_transylvania_l_english.yml` and `interface/006_independence_wave.gfx`: player-facing text and reused Event 006 sprites.

## Missing or stale surfaces

The current gameplay source has no proven local TRA package omission requiring a narrow patch.

`docs/systems/006_independence_wave_transylvania_package.md` is stale and should be reconciled by the parent documentation owner: its admission section still says IW-023 is absent from the compile-time content-attestation set and that admission is closed, while the current dispatch source attests and preflights `iw_023`.

The same system document says the mod focus copy is “byte-equivalent” to vanilla apart from eight imports; literal source comparison shows formatting/BOM differences in addition to the imports, so the wording should be changed to a semantic-preservation claim if documentation is updated.

The older independent audit handoff also contains the superseded attestation blocker; it must not override the later runtime-admission reconciliation handoff.

## Map and state setup

The current installed-map contract is state 84 (`84-Transylvania.txt`) as the required TRA capital and anchor, with state 76 (`76-Northern Transylvania.txt`) as optional compact extension.

State 47 is not a TRA anchor in the current map: vanilla `47-Greece.txt` is Thessaly with owner GRE, while current TRA package bindings and every exact TRA trigger use state 84.

The protected former-host state is state 46 (`46-Romania.txt`) through `ROM=46` in the binding CSV; changing the package to state 47 would violate the current map contract and is not warranted by this audit.

The read-only map inspection covered states 47, 46, 76, 84, 82, and 106 and returned `inspectedStateCount = 6` with state/region, bitmap, network, and adjacency checks parsed for the selected set.

The MCP artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5e3f6336e174baebd7b41294b1b876ad0cbc977f4bcfc8df4bb05ce5ae8779d/1007e3fb7ac166280e6a3309d2db7316f103caab63e5372b366828086ea6b009/map-inspect.30f47db55e9f43.json`.

That inspection reported unrelated global `map/buildings.txt` building-position and port-adjacency diagnostics; no TRA-specific selected-state repair was identified, and no map rewrite was performed.

## Politics, leader, portrait, flag, advisor, and party review

The vanilla `TRA` country identity, capital 84, Iuliu Maniu leader, recruited TRA characters, flag, and vanilla portrait paths remain in use.

`events/006_independence_wave.txt` hidden checkpoint `chaosx.nr6.350` validates the Maniu roster before the package marks the command roster ready.

The package adds no fictional personal leader, no generated portrait, no opposite-gender name pool, no invented historical flag, and no unsupported advisor replacement.

The five government installers in `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt` set the route ideology, party name, elections/popularity, route idea, and ledger deltas behind exact TRA route flags.

No source-level politics or identity defect was found.

## Focus, decision, idea, and asset review

The focus contract is additive: `independence_wave_assign_focus_framework` registers the carrier and overlay assignment, while `austro_hungarian_releasable_focus` remains the loaded TRA tree.

The package does not blindly replace or reload the vanilla TRA focus tree, and the Event 006 shared focus chain is gated by the additive carrier contract.

The decision category contains one auto-activated timed mission and eleven decisions covering depots, defectors, assembly, host ledgers, five government routes, settlement codification, and the Danube network.

The seven package ideas cover the divided starting authority, settlement, five route outcomes, and are allowed only for `original_tag = TRA`.

Localisation keys for the package category, mission, decisions, tooltips, parties, and ideas are present in `localisation/english/006_independence_wave_transylvania_l_english.yml`.

The package reuses registered Event 006 decision sprites and therefore does not require a new TRA art package.

No focus, decision, idea, asset, or localisation source defect was found.

## Starting military, technology, industry, supply, and production

The force mapping row for IW-023 selects `mountain_frontier` with military tradition `68`, no navy inheritance, no air inheritance, and reinforcement paths for secure depots, convert defectors, regional guards, terrain units, and a professional officer corps.

The reinforcement mask `654` is the exact sum of those five path bits, and the runtime expected path count is five.

`common/scripted_effects/006_independence_wave_force_package_effects.txt` probes and applies only the validated mapping, while `common/scripted_effects/006_independence_wave_force_effects.txt` creates the mountain-frontier template and starting force at the admitted anchor.

The dynamic force code inherits approved host technology/research context and creates supply-relevant stockpiles through the shared force package; vanilla TRA history remains otherwise intact.

Source review found no narrow setup error in the force, technology, industry, supply, or production contracts.

Actual division counts, equipment stockpiles, supply throughput, production lines, and survival after a live release remain untested because this audit does not launch the game or mutate a save.

## AI and playability

`common/ai_strategy/006_independence_wave_transylvania.txt` covers frontier survival, army/artillery/defence priorities, infrastructure, production, emergency response, and settlement-stage strategy.

The strategy file uses `avoid_starting_wars = -230` during founding restraint and `-430` after settlement.

The vanilla AI documentation states that negative `avoid_starting_wars` values reduce avoidance score and can increase willingness to start wars, whereas positive values are used by vanilla examples for restraint.

This is a balance/runtime risk rather than a proven syntax or admission defect because other Event 006 packages use the same negative “restraint” convention and the intended cross-package tuning is unresolved.

No AI inversion was patched without a seeded scenario comparison and design approval.

No seeded AI focus choice, decision choice, front behavior, diplomacy, supply, or survival simulation was run; these remain meaningful validation gaps for the parent completion pass.

## FORM-08 and Event 005 separation

TRA admission remains separate from FORM-08 formation.

`common/scripted_triggers/006_independence_wave_form08_triggers.txt` accepts TRA only through the exact 84 anchor/capital contract and still requires the corridor, registry member count, consent count, and anchor count proof before mutation.

`common/scripted_effects/006_independence_wave_form08_effects.txt` registers TRA readiness without mutating identity or territory, and the identity/integration adapter is fail-closed until the full proof is present.

The current source does not provide an independent live three-member/three-consent/three-anchor FORM-08 proof, so FORM-08 remains unresolved for the broader Event 006 completion goal.

No Event 005 ownership, tag, origin, or formable contract was changed or implied by this admission.

## Validation receipts and limitations

The current runtime-admission handoff reports the strict allocator and admission suite passing for fifteen exact attested packages, fourteen groups, fifteen anchors, the ladder, SCN-008 matrix/edge cases, strict flags, and collision checks.

This audit independently inspected the TRA package source, current binding rows, vanilla TRA identity/history/characters, force mapping, focus carrier, decisions, ideas, AI, cleanup, and FORM-08 gates.

The read-only MCP map artifact above is the only MCP receipt produced during this audit.

No live Hearts of Iron IV launch, save/load, scenario dispatch, release transfer, AI simulation, or technology viewer run was performed.

The installed package currently exposes no Technology Tree Viewer, so technology-tree visual inspection remains an unresolved tooling limitation.

## Findings and handoff

Finding 1, documentation stale: update `docs/systems/006_independence_wave_transylvania_package.md` to state that current dispatch source admits `iw_023`, and replace the literal “byte-equivalent” focus-copy wording with a semantically reviewed wording.

Finding 2, map wording clarification: retain state 84 as TRA anchor, optional state 76, and ROM protected state 46; state 47 is unrelated GRE Thessaly and must not be substituted from the task shorthand.

Finding 3, AI validation risk: review the negative `avoid_starting_wars` values with seeded scenario evidence before changing shared Event 006 tuning.

Finding 4, unresolved broader blocker: FORM-08 runtime member/consent/anchor proof and live playability evidence remain outside this country-package audit.

Changed files: this handoff only.

Changed tags, state ids, leaders, parties, focus tree ids, localisation keys, formable ids, gameplay effects, or assets: none.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw023_tra_post_admission_country_package_audit_2026_08_03.md`.

Simplifications and omissions: no gameplay patch was made because the admitted TRA package has no proven narrow source defect; live release, AI, supply, balance, and FORM-08 proof remain intentionally unclaimed.
