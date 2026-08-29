# Event 006 runtime roster and cost localisation repair

Date: 2026-08-29

## Scope

This tranche repairs the release-time package checkpoint and the compact decision-cost presentation for Event 006.

## Gameplay changes

- `events/006_independence_wave.txt` now gives `chaosx.nr6.10` an idempotent release-time roster checkpoint for SCO, WLS, RHI, BAY, and BRI.
- The checkpoint uses guarded `recruit_character` effects for the fixed Event 006 advisor IDs that absent carrier tags cannot receive from vanilla country-history loading.
- `common/scripted_effects/006_independence_wave_western_package_effects.txt` calls the checkpoint during IW-004 setup before the Brittany prepared-roster assertion.
- The checkpoint does not change package admission, allocator weights, event timing, pre-event visibility, or country release scope.

## Error reconciliation

The pasted `capital_scope` errors name the former split files `006_independence_wave_epirus_package_triggers.txt`, `006_independence_wave_thrace_package_triggers.txt`, and `006_independence_wave_banat_package_triggers.txt`; those files are absent from the current source and survive only as provenance comments in the consolidated registry.

The active consolidated Balkan trigger registry uses explicit numeric state scopes for its fixed anchors and contains no raw dormant-country `capital_scope` call.

The release path can still abort every selected country when a package fails its all-or-nothing prepared-roster proof, so the new checkpoint addresses the remaining confirmed absent-carrier failure mode without reintroducing a pre-event crisis surface.

## Localisation changes

`localisation/english/006_independence_wave_decisions_l_english.yml` keeps every dynamic cost component and icon but replaces padding spaces and unnecessary line breaks with compact `·` separators in both available and blocked cost strings, including provisional-capital costs.

The two-stage patron cost still distinguishes its `Start` and `Later` payments, and alternative reserve costs retain their slash or `or` semantics.

## Validation

Focused Event 006 validators to run after this handoff are `.tools/audit_event6_allocator.py --strict`, `.tools/audit_event6_country_api.py --strict`, `.tools/audit_event6_flags.py --strict`, `.tools/audit_event6_form16.py --strict`, `.tools/audit_event6_scenario_matrix.py --strict`, and `.tools/audit_event6_gui_matrix.py --strict`.

Source assertions include checking that no executable references to the old split trigger filenames remain, the consolidated Balkan package files contain no `capital_scope`, all five checkpoint branches reference valid character IDs, and the cost-localisation block contains no padding double spaces.

No live game, save/load, or MCP runtime claim is made here.

## Remaining risks

The broader Event 006 audit remains HOLD/PARTIAL because the probability and GUI MCP routes were unavailable, several package and asset/documentation findings remain open, and live consumer validation belongs to the user.
