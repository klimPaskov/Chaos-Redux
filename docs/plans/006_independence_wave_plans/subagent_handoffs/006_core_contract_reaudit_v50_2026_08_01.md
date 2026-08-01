# Event 006 core contract re-audit v50 — 2026-08-01

## Scope

This parent-owned tranche closes the Event 006 character-handoff contract after the v49 audit and records the current readiness boundary for FIJ, DOX, SOK, CHU, and ASY.

## Character handoff repair

The repository event skill forbids `recruit_character` in scripted effects and on actions.
All Event 006 package-effect roster calls now use the hidden synchronous event `chaosx.nr6.350`.
The event file owns the guarded `recruit_character` operations, while package effects retain role promotion, route guards, date gates, cleanup, and attestation ownership.
The handoff covers SCO, WLS, RHI, BAY, AJX, COR, HBX, HAW, FSM, FIJ, CHU, ASY, DOX, and SOK roster branches.

The original candidate ID `chaosx.nr6.15` conflicted with the existing Bavaria district-incident event in `events/006_independence_wave_rhineland_bavaria.txt`.
The shared roster event and every new call site were moved to unused ID `chaosx.nr6.350`; the Bavaria incident remains `chaosx.nr6.15`.

SOK keeps Dikko and Bello on the pre-cutover, Event-012-safe branch and only recruits Siddiq after the existing post-cutover trigger.
CHU and ASY route-specific roles remain guarded by their institutional route flags.
DOX and SOK remain guarded by their prepared-scope triggers, so no living or Soviet-origin country is overwritten.

## FIJ readiness boundary

IW-177 setup no longer writes `independence_wave_fij_melanesian_route_adapter_complete`.
That flag remains a readiness-owned gate for the FORM-39 FIJ/PNG/WPG adapter and cannot be inferred from the route surface alone.
The FIJ source audit found no defensible rights-cleared male portrait dated on or before the 1936 baseline; the strongest National Archives of Fiji candidate is explicitly circa 1940s.
FIJ therefore remains fail-closed without a new portrait, DDS, or GFX fallback.

## Current core evidence

- `python -B .tools/audit_event6_allocator.py` passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 13 attested packages, and the accepted 6/8/10/14/20 ladder.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passes with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions; the explicitly excluded Random Events roots remain skipped.
- Focused Event Viewer lint for `events/006_independence_wave.txt` returns no blocking diagnostics; workspace-wide helper validation remains partial by tool design.
- `common/scripted_effects/006_*.txt` contains no `recruit_character` calls; all static roster recruitment is event-owned.
- No custom Event 006 advisor icons, advisor sprite blocks, or advisor portrait derivatives were added.

## Remaining admission boundary

Only IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-019, IW-173, and IW-184 are content-attested.
IW-043 CHU, IW-058 ASY, IW-179 FSM, IW-093 DOX, IW-098 SOK, and IW-177 FIJ remain fail-closed pending their documented portrait, source, role, territory, or full-package gates.
The core allocator, crisis queue, reusable country API, and tag-registration surfaces are source-closed, but package-specific content, focus geometry, formable admission, super-event/audio closure, and final catalog alignment remain open.

This handoff does not claim whole-event completion and does not authorize a fallback or a goal-blocked status while meaningful package work remains.
