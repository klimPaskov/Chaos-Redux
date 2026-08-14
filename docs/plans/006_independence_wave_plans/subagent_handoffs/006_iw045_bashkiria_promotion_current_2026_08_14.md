# IW-045 Bashkiria promotion receipt — 2026-08-14

## Decision

The parent has promoted IW-045 Bashkiria through the central Event 006 content-attestation and deterministic Join gates after the package-local audit reached a source-backed pass. This receipt supersedes the earlier adapter-only IW-045 boundary; it does not claim whole-event completion.

## Central changes

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` now includes `iw_045` in the content-attestation OR list while preserving the separate adapter and exact dormant identity/preflight gates. `common/scripted_effects/006_independence_wave_join_effects.txt` now evaluates `iw_045` immediately after IW-044 and before IW-033 in the deterministic first-success Join order. No other adapter-only ID was widened.

The static allocator witness was updated in `.tools/audit_event6_allocator.py` to expect IW-045, 32 attestations, and 29 compatible reservation groups. The central two-gate preflight still requires both an adapter and content attestation, and the SCN-008 branch remains independently guarded.

## Current authority

The current allocator pass reports 149 publishers, 32 content-attested selectable packages, 29 compatible reservation groups, 161 unattested selectable rows out of 193 non-overlay rows, and 40 runtime adapters. The eight adapter-only IDs that remain fail-closed are IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM. The deterministic Join order is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-045, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184.

The active automatic and SCN-008 ladder remains 3/4/5/7/10, with World Collapse also targeting 10. Static allocator, SCN-008 matrix, flag-family, and country-tag audits pass at the current source boundary; these are source/static checks rather than live transaction or save/load proof.

## IW-045 package evidence

The package is bound to dormant vanilla BSK, exact anchor state 651/Ufa, an actual living former host, and the origin-separation contract. Package-local setup, final validation, cleanup, seven lifecycle ideas including `bsk_oilfield_council`, ten canonical paid projects, the five shared focus hooks, p45 mounted-mobile forces, localisation, AI source, and generation-safe cleanup are present. The shared roster checkpoint uses vanilla Yakov Bykin with a character-scoped source-placeholder portrait override and cleanup restore; the portrait archive keeps original sources directly in the Event 006 portrait parent and all processed evidence in its single `processed` child, with no 156x210 archive files. Four generated alternate-history route flag ladders have normal, medium, and small runtime TGAs with QA evidence; no neutral `BSK.tga` replacement is claimed.

## Engine evidence and limits

The current state-651 map inspection and render are successful for the selected state, with unrelated workspace-wide map diagnostics making aggregate validation false. The current Event `.350` state-flow inspection/render is partial with zero selected blocking diagnostics because helper/lifecycle projections are deferred. The current shared focus inspection resolves 184 focuses, 196 connectors, zero crossings, zero node intersections, and two long connectors; remaining authored detours and unrelated vanilla continuous-focus icon diagnostics keep focus acceptance bounded. The BSK AI strategy exposes no weighted surface, and its mission pool remains incomplete with empty typed fixtures; no quantitative probability, ranking, timing, dominance, starvation, or live AI-balance claim is made. No Technology Tree Viewer is available, and no live game or save/load validation is claimed.

## Whole-event disposition

Event 006 remains HOLD / PARTIAL because 161 selectable rows remain unattested and the accepted scope still has open formable reachability, shared focus diagnostics, typed probability evidence, super-event 23 audio/wrapper/firing work, technology evidence, and live runtime validation. The IW-045 promotion is intentionally narrow and does not admit the remaining adapter-only IDs or widen any unrelated fail-closed gate.

## Evidence references

The package-local evidence is recorded in `006_iw045_bashkiria_country_core_2026_08_14.md`, `006_iw045_bashkiria_package_admission_audit_current_2026_08_14.md`, `006_iw045_bashkiria_decisions_2026_08_14.md`, `006_iw045_bashkiria_focus_hooks_2026_08_14.md`, `006_iw045_bashkiria_localisation_final_audit_2026_08_14.md`, `006_iw045_bashkiria_flag_asset_handoff_2026_08_14.md`, `006_iw045_bashkiria_portrait_source_placeholder_2026_08_14.md`, and `006_iw045_bashkiria_probability_audit_2026_08_14.md` in this handoff directory. Current event and focus MCP artifact URIs and the static audit outputs are preserved in the parent package and whole-event handoffs.
