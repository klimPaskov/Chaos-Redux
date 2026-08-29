# Event 006 runtime roster and cost localisation repair

Date: 2026-08-29

## Scope

This tranche repairs the release-time package checkpoint and the compact decision-cost presentation for Event 006.

## Gameplay disposition

- An earlier version of this tranche attempted to put guarded `recruit_character` effects for SCO, WLS, RHI, BAY, and BRI into the hidden `chaosx.nr6.10` event and called that event from the IW-004 setup path.
- That runtime recruitment change was reverted by `0afb89a82` after live launch evidence showed that the engine accepts `recruit_character` during game/history initialization, not during event execution. The seventeen resulting validation errors disappeared after the revert; the repair ledger records the same finding at `docs/testing/live_qa/20260829_1335_main_menu_repair/repair_ledger.md`.
- `events/006_independence_wave.txt` therefore keeps `chaosx.nr6.10` as an empty synchronous compatibility checkpoint. The separate `chaosx.nr6.350` checkpoint remains the active idempotent roster/portrait assertion path for packages that already have their fixed characters available; it does not recruit characters at runtime.
- Fixed-tag character ownership remains in `history/general/006_independence_wave_character_recruitment_registry.txt`. If an absent carrier cannot receive its fixed roster through history initialization, the package remains fail-closed until an engine-safe generation mechanism is designed and proven; no generic runtime fallback is introduced here.
- `common/scripted_effects/006_independence_wave_western_package_effects.txt` still calls the empty compatibility checkpoint during IW-004 setup for source compatibility. This call does not create a pre-event crisis surface, change package admission, alter allocator weights, change event timing, or change country release scope.

## Error reconciliation

The pasted `capital_scope` errors name the former split files `006_independence_wave_epirus_package_triggers.txt`, `006_independence_wave_thrace_package_triggers.txt`, and `006_independence_wave_banat_package_triggers.txt`; those files are absent from the current source and survive only as provenance comments in the consolidated registry.

The active consolidated Balkan trigger registry uses explicit numeric state scopes for its fixed anchors and contains no raw dormant-country `capital_scope` call.

The release path can still abort every selected country when a package fails its all-or-nothing prepared-roster proof. The reverted runtime recruitment attempt does not resolve that dependency for absent carriers, and the current source intentionally preserves the fail-closed behavior rather than using an unsupported event-time `recruit_character` fallback.

## Localisation changes

`localisation/english/006_independence_wave_decisions_l_english.yml` keeps every dynamic cost component and icon but replaces padding spaces and unnecessary line breaks with compact `·` separators in both available and blocked cost strings, including provisional-capital costs.

The two-stage patron cost still distinguishes its `Start` and `Later` payments, and alternative reserve costs retain their slash or `or` semantics.

## Validation

Focused Event 006 validators run after the revert and subsequent documentation/localisation tranches: `.tools/audit_event6_allocator.py --strict`, `.tools/audit_event6_country_api.py --strict`, `.tools/audit_event6_flags.py --strict`, `.tools/audit_event6_form16.py --strict`, `.tools/audit_event6_scenario_matrix.py --strict`, and `.tools/audit_event6_gui_matrix.py --strict`.

Source assertions include checking that no executable references to the old split trigger filenames remain, the consolidated Balkan package files contain no `capital_scope`, the hidden `.10` event contains no runtime `recruit_character` effects, fixed-character IDs remain in the history registry, and the cost-localisation block contains no padding double spaces.

No live game, save/load, or MCP runtime claim is made here.

## Remaining risks

The broader Event 006 audit remains HOLD/PARTIAL because absent-carrier history coverage still needs an engine-safe solution and runtime proof, the probability and GUI MCP routes were unavailable, several package and asset/documentation findings remain open, and live consumer validation belongs to the user.
