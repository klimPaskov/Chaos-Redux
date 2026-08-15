# Event 006 achievement former-host scope hardening

Date: 2026-08-12.

## Change

`common/scripted_effects/006_independence_wave_achievement_effects.txt` now requires `has_independence_wave_living_former_host = yes` before the voluntary-reunion remnant disqualifier dereferences `var:independence_wave_former_host`.

The war recorder now applies the same living-former-host guard to both active-country war branches before testing the former-host tag relationship.

The puppet, release-as-puppet, autonomy-change, and annexation on-actions use the living-host trigger before their former-host tag checks, preventing a stale variable from being dereferenced before the guarded disqualifier runs.

## Reason

An Event 006 origin can retain a stale former-host variable after host annexation or another origin-ending cleanup path, so checking only `has_variable` could attempt to scope into a non-existent country and weaken the intended fail-closed achievement lifecycle.

The valid reconquest, peace, and anchor-loss paths already use the living-host trigger, so this change aligns the remaining recorder/disqualifier paths without changing successful qualification semantics.

## Validation and limits

The edited effect file remains brace-balanced and the three new guards are present exactly at the former-host dereference sites.

The current HOI4 MCP event route is unavailable because the workspace artifact provenance manifest is invalid, so no fresh engine trace or live achievement unlock claim is made.

No achievement definitions, localisation, assets, or package admission lists were changed.
