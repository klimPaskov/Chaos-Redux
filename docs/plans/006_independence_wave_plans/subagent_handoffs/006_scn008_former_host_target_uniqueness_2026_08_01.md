# Event 006 SCN-008 Former Hosts target-uniqueness repair

Date: 2026-08-01

## Scope

This handoff closes the bounded v67 core improvement finding for SCN-008 Universal Belligerence: Former Hosts. It changes only the post-commit scenario war target reservation and leaves country admission, wave allocation, focus content, assets, formables, and the ordinary Wars of Separation rule unchanged.

## Source change

`common/scripted_effects/006_independence_wave_scenario_effects.txt` now gives `independence_wave_scenario_start_host_war` a temporary global policy input, `global.independence_wave_scenario_former_host_unique_policy`.

`independence_wave_scenario_start_universal_belligerence` sets that policy only for the Former Hosts branch and clears it after the bounded loop. The existing `independence_wave_scenario_clear_belligerence_target_marks` helper also clears the policy before and after a Universal launch.

When the policy is enabled, a living former host must not already have `independence_wave_scenario_belligerence_targeted`; the host is marked and appended to `global.independence_wave_scenario_belligerence_targets` before declaration, retained after a successful war, and removed immediately after a failed declaration. A temporary `independence_wave_scenario_host_target_saved` guard prevents stale event-target scopes from being cleaned when a later actor is rejected because its shared host was already reserved.

When the policy is absent, `independence_wave_scenario_start_all_host_wars` retains the accepted Wars of Separation behavior: every release with a viable former host may open its own separation war, including releases sharing one host.

## Acceptance witnesses

- `UFH-01`: IW-008 RHI and IW-010 AJX may share the accepted RG-RHINE-SAAR former host. Universal Former Hosts reserves Germany once; the first eligible actor in frozen order opens the war and the later actor receives the regional-threat result.
- `UFH-03`: a failed declaration removes the host mark and array entry so a later same-host actor may try.
- `WOS-01`: Wars of Separation does not set the Universal policy, so both releases retain their individual viable host-war path.
- `UFH-06`/`CLEAN-01`: the existing bounded target-array cleanup clears marks and the policy before the next launch.

## Validation

- Script braces for the touched scenario effect: `812/812`.
- No unsupported `<=` or `>=` operators in the touched effect.
- `python -B .tools/audit_event6_allocator.py`: PASS; 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-008 ranked packages, 13 attestations, 12 compatible groups, doubled 6/8/10/14/20 ladder, and Event 005-first joint ordering unchanged.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`: PASS; 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, Random Events root excluded per user decision.
- Focused MCP event lint for `chaosx.nr6.3`: status `ok`, no blocking diagnostics; the workspace-wide issue count remains deferred by the MCP large-analysis boundary.

No fallback, duplicate target registry, new war path, on-action, package admission, tag, localisation key, or asset was introduced. The whole Event 006 status remains HOLD / PARTIAL because package depth, focus geometry, formables, assets, and other accepted completion surfaces remain open.
