# Event 006 CAT focus-ownership audit v87 — 2026-08-02

## Scope and verdict

This is a bounded follow-up for the Catalonia Event 006 package. The task message labels the package as `CAT/IW-157`, but the repository's Catalonia package is `IW-014` (`constant:independence_wave_package_id.iw_014`); `IW-157` is the separate WPG/West Papua research hold. This handoff audits CAT/IW-014 and does not change IW-157/WPG.

Verdict: **HOLD / no safe local patch**. CAT's adapter currently requests the Event 006 full framework, while its implementation notes call the route an additive overlay. Converting only the assignment and prepared trigger to `additive_overlay` would expose a flag without exposing CAT's shared focuses on the carrier tree. The installed vanilla CAT carrier has `generic_focus` and no CAT-specific tree or Event 006 shared-focus imports. Preserve the vanilla tree and keep CAT and FORM-07 fail-closed until a reviewed carrier-insertion design exists.

No CAT gameplay, focus, trigger, effect, dispatcher, formable, asset, or localisation file was patched in this audit. Only this blocker handoff was added.

## Country-package coverage checklist

| Surface | Result | Evidence and boundary |
| --- | --- | --- |
| Tag and country identity | PASS for dormant carrier | Vanilla registers `CAT = "countries/Catalonia.txt"` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:200`; the Event 006 package trigger requires `original_tag = CAT` at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:8-12`. No duplicate country shell is present. |
| Package identity and anchor | PASS / dormant | CAT uses `iw_014`, reservation group `RG-165`, and state 165 in `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:8-32` and `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:18-25`. This does not admit the package. |
| Setup and cleanup | Present, fail-closed | `independence_wave_setup_iw_014_catalonia`, final validation, and cleanup are in `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:305-420`. The setup only reports success when the prepared contract passes; cleanup removes the mission, eleven project decisions, seven CAT ideas, ledgers, and route flags. |
| Politics and leaders | Reuse boundary PASS | Vanilla CAT history recruits `CAT_lluis_companys` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CAT - Catalonia.txt:80`; route effects promote that same character at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:161-248`. No Event 006 replacement portrait or advisor asset is introduced. |
| State and host | Source-coherent, runtime unproved | State 165 is the Catalan compact anchor, with former host SPR required by `can_initialize_independence_wave_iw_014_package` at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:14-32`. Fresh-map ownership, controller, host survival, and dynamic force output remain unobserved. |
| Decisions, mission, ideas, and AI | Source-present, dormant | CAT's 420-day mission and eleven project decisions are in `common/decisions/006_independence_wave_catalonia_decisions.txt:15-225`; seven CAT lifecycle ideas are in `common/ideas/006_independence_wave_catalonia_ideas.txt`; strategy layers are in `common/ai_strategy/006_independence_wave_catalonia.txt`. Their visibility remains gated by `is_independence_wave_cat_package`. |
| Localisation and assets | Source-present, no new CAT asset | CAT project, focus, idea, party, and tooltip keys are in `localisation/english/006_independence_wave_catalonia_l_english.yml`. The adapter intentionally reuses the vanilla CAT flag and Companys portrait; no advisor, dossier, operative, or generated CAT portrait is authorized. |
| FORM-07 | HOLD | CAT's prepared trigger requires `has_independence_wave_formable_commit_readiness = yes` at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:114-121`; the exact CAT/NAV/GLC identity, flag, member, and integration writers remain incomplete. No FORM-07 admission was added. |

## Focus ownership contract

The conflicting contract is concrete in the current source:

- CAT setup writes `independence_wave_focus_assignment_input = constant:independence_wave_focus_assignment.full_framework` and calls `independence_wave_assign_focus_framework` at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:305-317`.
- The CAT prepared proof requires `independence_wave_full_focus_framework` and the `full_framework` assignment at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:97-98`.
- The six CAT shared-focus roots are imported by `independence_wave_focus_tree` at `common/national_focus/006_independence_wave_focus.txt:75-82`. The first CAT node also requires `independence_wave_prepare_capital_administration` and `can_use_independence_wave_full_focus_framework` at `:3532-3543`, so it is authored against the full Event 006 tree rather than a vanilla carrier.
- Additive assignment deliberately refuses unreviewed trees. `can_attach_independence_wave_additive_focus_carrier` requires `independence_wave_focus_carrier_registered` and a reviewed carrier tree, currently only ICE/`iceland_tree`, at `common/scripted_triggers/006_independence_wave_focus_triggers.txt:50-64`.
- The vanilla CAT country history has no CAT focus tree; it only completes generic focuses at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CAT - Catalonia.txt:34-43`. The installed vanilla `generic_focus` tree is defined at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/generic.txt:18-30` and does not import any CAT or Event 006 shared focus.

Therefore, changing CAT setup to `additive_overlay`, adding CAT to the carrier trigger, or replacing the first prerequisite with a generic focus would not make the six CAT nodes visible on `generic_focus`; it would claim an overlay that the engine has not inserted. Copying or overriding the entire vanilla generic tree to add imports would violate the requested vanilla-tree preservation and is not a bounded local fix.

## File-surface checklist

| Surface | Current state | Required next action |
| --- | --- | --- |
| `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt` | Full-framework setup and CAT cleanup are wired; no CAT carrier registration exists. | Keep fail-closed. Add an assignment only after a reviewed tree/import mechanism is chosen. |
| `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt` | Prepared proof requires full framework and full assignment. | Do not weaken to additive until the carrier can actually render the six roots. |
| `common/scripted_triggers/006_independence_wave_focus_triggers.txt` | Additive carrier trigger accepts only ICE/`iceland_tree`. | A future CAT branch must name a real CAT owning tree and prove its imports; `generic_focus` alone is insufficient. |
| `common/national_focus/006_independence_wave_focus.txt` | CAT roots are imported only into `independence_wave_focus_tree`; node prerequisites are full-tree IDs. | Rework only under a parent-approved carrier design; do not copy the generic tree as a shortcut. |
| `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | CAT setup/final-validation/cleanup wrappers are present. | Leave wrappers dormant. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | CAT runtime/scenario wrappers exist, while compile-time attestation remains excluded. | Preserve exclusion until the focus and FORM-07 gates close. |
| `common/decisions/006_independence_wave_catalonia_decisions.txt` and CAT ideas/AI/localisation | Implemented source surfaces exist. | No changes required for this ownership blocker. |

## Map, state, military, technology, industry, and supply

The current installed-map binding keeps CAT on state 165 with SPR as former host and `RG-165`; the package trigger requires state 165 ownership/control and a protected host-state record. Vanilla state 165 remains the source authority for Barcelona's victory point, factories, airbase, port, infrastructure, and coal. No map rewrite is needed for this focus-only blocker.

CAT's p14 force mapping, reinforcement flags, technology inheritance, and dynamic starting-force call are already wired through the CAT setup effect and shared force helpers. Because CAT remains unattested and no live release was run, this audit does not claim divisions, stockpiles, navy/air inheritance, supply, production, or host survival in play.

## Admission and formable boundary

CAT/IW-014 remains outside the compile-time content-attestation OR in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`; its exact runtime and scenario wrappers are therefore dormant. The CAT prepared trigger still requires the unresolved Iberian `FORM-07` commit-readiness contract. No attestation, release, automatic selection, or FORM-07 identity/flag/member/integration flag was created by this audit.

## Validation performed

- Read the CAT package effects/triggers, shared focus assignment effects/triggers, CAT focus nodes, dispatcher wrappers, and current CAT handoffs.
- Read the installed vanilla CAT history, generic focus tree, country tag, character, state, and country surfaces.
- Used the offline National focus modding reference: `shared_focus` imports a focus and its prerequisite-connected focuses into a specific `focus_tree`; a flag alone is not an insertion mechanism. `allow_branch` is evaluated when the owning tree is loaded and can be refreshed only for that tree.
- Ran exact `rg`/PowerShell source scans for `iw_014`, `iw_157`, CAT focus IDs, `generic_focus`, `iceland_tree`, `full_framework`, and `additive_overlay` across the Event 006 surfaces.
- Attempted the read-only `hoi4_focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`/`independence_wave_focus_tree`; the installed inspector returned `SCAN_BYTE_LIMIT`, so no MCP focus-render or diagnostic claim is made from that attempt.
- No Hearts of Iron IV process, save, or live release was launched.

## Changed files

- Added `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw014_cat_focus_ownership_blocker_v87_2026_08_02.md`.
- No gameplay, focus, trigger, effect, dispatcher, formable, map, asset, or localisation file was changed.

## Cross-package ARX orphan-portrait disposition

The tracked files `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds` and `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds` are no longer referenced by runtime character records, `.gfx` sprite definitions, localisation, or package effects after the sourced Mella/Verne replacement. They should not remain in the runtime asset tree as live alternatives. Recommended disposition is **archive provenance in the dated ARX portrait handoffs, then delete these two tracked orphan DDS files in an explicit asset-cleanup commit after the parent confirms the repository-wide zero-reference scan**. This CAT handoff does not delete or move them.

## Remaining blocker and parent action

Keep CAT/IW-014 and FORM-07 fail-closed. To proceed, the parent must choose and document one of two designs: (1) provide a real CAT-owned focus tree that imports the six shared roots, accepting the ownership implications; or (2) extend a reviewed vanilla carrier/import contract that genuinely inserts those roots while preserving CAT's existing tree. Only after that design, the CAT focus prerequisites, and the FORM-07 identity/member/flag/integration gates are independently accepted should the package request additive assignment or content attestation.
