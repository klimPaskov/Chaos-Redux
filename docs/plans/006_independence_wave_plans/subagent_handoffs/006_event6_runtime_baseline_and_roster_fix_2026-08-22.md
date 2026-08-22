# Event 006 dormant-carrier initialization repair

Date: `2026-08-22`

## Scope

This tranche repairs the manual `chaosx.nr6.1` standalone path for dormant Event 006 carriers. It does not promote any package, relax the content-attestation boundary, or claim live in-game completion.

## Source changes

- `common/scripted_effects/006_independence_wave_banat_package_effects.txt` now restores AXX's `civilian_economy`, `export_focus`, and `volunteer_only` laws before `can_initialize_independence_wave_iw_024_package` is evaluated.
- `common/scripted_effects/006_independence_wave_thrace_package_effects.txt` applies the same ordering for BAX and IW-027.
- `common/scripted_effects/006_independence_wave_epirus_package_effects.txt` applies the same ordering for BBX and IW-028.
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` adds guarded AFX/AGX baseline-law helpers and invokes them before the IW-006/IW-007 initialization contracts.
- `history/general/006_independence_wave_additional_character_recruitment.txt` registers the AFX and AGX leader/commander pairs through `every_possible_country`, so an absent-at-start carrier has the exact roster required by its setup trigger after instantiation.

The AXX/BAX/BBX trigger files currently use fixed numeric state scopes (`82`, `184`, and `185`) for their anchor/capital checks. `rg` finds no `capital_scope` reference in those three files; the pasted line-17 `capital_scope` diagnostics therefore do not describe the current source revision.

## Validation evidence

- `.tools/audit_event6_allocator.py` passed with 149 publishers, 32 attested packages, 20 static standalone witness packages, the 3/4/5/7/10 count ladder, and the retired pre-event crisis surface.
- `.tools/audit_event6_country_api.py` passed with zero missing or duplicate country API rows.
- `.tools/audit_event6_flags.py --strict` passed for all 102 registered package rows.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 cells and 8 edge cases.
- A focused `capital_scope` scan returned no matches in the three user-reported package trigger files.
- `hoi4.event_inspect` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; the remaining partial status is the expected workspace-wide helper projection limit.

## Runtime boundary

No live game receipt is available in this coding session, so this handoff proves source ordering and startup-roster coverage only. Event 006 remains a broader HOLD/PARTIAL feature: the static boundary admits 32 of 193 selectable non-overlay rows, and the full package matrix still contains unattested or unverified rows.

