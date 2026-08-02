# IW-018 ARX Sardinia Country Package Re-audit (2026-08-02)

## Disposition

IW-018 (`ARX`, Sardinia, Event 006 anchor state 114) is a static package PASS and remains admitted to the exact runtime-content attestation set. No ARX gameplay, localisation, focus, decision, or asset source was patched during this re-audit. The package is wired to the shared `independence_wave_focus_tree` under the one-generic-tree contract; it does not require or contain a bespoke ARX focus tree.

This is a country-package audit only and is not a completion claim for the whole Event 006 system. The remaining focus-geometry diagnostic is global to the shared tree, not an ARX-local package blocker.

## Country package coverage checklist

| Surface | Result | Evidence |
|---|---|---|
| Tag and country shell | PASS | `common/country_tags/006_independence_wave_countries.txt` registers `ARX = "countries/006_independence_wave_ARX.txt"`; `common/countries/006_independence_wave_ARX.txt` supplies the graphical shell. |
| History and starting laws | PASS | `history/countries/ARX - Sardinia.txt` intentionally contains baseline laws and the five runtime roster characters only; territory, forces, production, ideas, and focus assignment are package-runtime responsibilities. |
| State, anchor, capital, and host | PASS | Vanilla `history/states/114-Sardinia.txt` provides state 114, capital/port/airbase/naval infrastructure, VP, resource, manpower, and ITA/SPM cores; ARX setup requires ownership/control and protects the former host. |
| Politics and parties | PASS | `independence_wave_initialize_arx_politics` sets the four party names/popularities, democratic elections, and provisional assembly; route effects install Lussu, Mella, or Verne and the route idea. |
| Leaders, characters, and portraits | PASS | `common/characters/006_independence_wave_mediterranean_characters.txt` defines Lussu, Mella, `ARX_gavino_piras` with runtime identity Vittorio Verne, and advisors Michele Corda/Efisio Satta; all active portrait metadata is male and matches its runtime DDS. |
| Shared focus tree and ARX route | PASS | `common/scripted_effects/006_independence_wave_focus_effects.txt` assigns `independence_wave_focus_tree`; `common/national_focus/006_independence_wave_focus.txt` contains six ARX module focuses with prerequisites, route gates, rewards, icons, localisation, and AI weights. |
| Decisions and founding mission | PASS | `common/decisions/006_independence_wave_mediterranean_decisions.txt` defines the ARX category, hold-island mission, eight single-project lanes, cancellation/failure, and FORM-05 maritime congress project. |
| Ideas and lifecycle | PASS | `common/ideas/006_independence_wave_mediterranean_ideas.txt` defines ARX crisis, mature council, constitutional, labor, crown, and mountain-guard ideas with ARX gates and lifecycle cleanup. |
| Starting forces, technology, industry, and supply | PASS | `independence_wave_setup_iw_018_sardinia` loads profile `iw018`, coastal-maritime force profile p18, military tradition 52, navy inheritance, no air inheritance, and dynamic force application; no static OOB or production line contradicts the package contract. |
| AI and playability | PASS | `common/ai_strategy/006_independence_wave_mediterranean.txt` provides ARX island-survival, host-threat, civic-maritime, crown/guard, and restraint strategies; the shared generic AI profile is assigned with the shared tree. |
| Formable and network hooks | PASS | `common/scripted_triggers/006_independence_wave_form05_triggers.txt` and the corresponding effects include ARX anchor 114, delegation, maritime congress, prospective carrier, connection, member, and cleanup paths. |
| Localisation and assets | PASS | ARX country/party/leader/advisor/idea/decision/focus/AI keys are present in `localisation/english/006_independence_wave_countries_l_english.yml` and `006_independence_wave_mediterranean_l_english.yml`; three promoted ARX leader portraits, flags, focus icons, decision icons, and idea icons are registered. |
| Cleanup and collision safety | PASS | ARX cleanup removes its mission, decisions, ideas, variables, route/formable/network/incident/setup flags; Event 005 collision gates reject occupied anchors/hosts and state 114 is disjoint from the Event 005 core footprint. |

## File surface checklist

The authoritative ARX surfaces are `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_ARX.txt`, `history/countries/ARX - Sardinia.txt`, `common/characters/006_independence_wave_mediterranean_characters.txt`, `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`, `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_mediterranean_decisions.txt`, `common/ideas/006_independence_wave_mediterranean_ideas.txt`, `common/ai_strategy/006_independence_wave_mediterranean.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_form05_triggers.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `events/006_independence_wave_mediterranean.txt`, the two ARX/mediterranean localisation files, the ARX portrait and asset `.gfx` files, and the promoted ARX DDS files under `gfx/leaders/006_independence_wave/`.

## Missing or stale surfaces

No ARX-local missing surface or clear patchable defect was found. The old unreferenced `portrait_ARX_independence_wave_gavino_piras.dds` and `portrait_ARX_independence_wave_vittorio_pala.dds` remain tracked shelf assets and are not runtime admission evidence; deleting them would be outside this audit scope.

The historical source ledger contains an older `Vernè`/encoding variant, but current runtime character/localisation keys, promoted DDS metadata, and the accepted v78 handoff consistently use `Vittorio Verne`; this is evidence history rather than a runtime mismatch and was not rewritten.

The pre-wire v76 note that described a missing IW-018 attestation is superseded. Current `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` includes `iw018` in `has_independence_wave_runtime_package_content_attestation_for_execution_id`, runtime preflight, and scenario preflight.

## Validation and remaining risks

`python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, 13 compatible reservation groups, and the documented automatic ladder 6/8/10/14/20.

The package was cross-traced through its tag, state 114, setup/complete triggers, runtime setup/cleanup effects, shared focus assignment, six ARX focuses, decision category/mission/projects, ideas, character roster, portrait/GFX registrations, AI profile, FORM-05 hooks, Event 005 collision gates, and localisation. No game launch was performed. The installed package exposes no Technology Tree Viewer, so technology-tree runtime rendering remains an unresolved global tooling limitation.

The remaining meaningful risk is the global shared `independence_wave_focus_tree` geometry diagnostic already recorded by Event 006 documentation; it is not evidence of an ARX-specific route or loading defect. Live runtime execution and in-game balance remain parent/user validation surfaces.

## Changes and simplifications

Gameplay, map, localisation, focus, decision, idea, AI, portrait, flag, and GFX source files were not changed. This handoff is the only file added by this re-audit. No fallback, placeholder, route omission, or country-identity simplification was introduced.
