# IW-057 Far Eastern Republic package core handoff

## Disposition

IW-057 FER is package-local and HOLD/FAIL-CLOSED. The source-backed adapter is implemented behind explicit parent-owned identity, rights, roster, capital, and origin gates. Central attestation, normal/scenario preflight, dispatcher, Join, vanilla FER history, portraits, flags, and cosmetic tags were intentionally left untouched.

## Files changed

- `common/script_constants/006_independence_wave_far_eastern_constants.txt`
- `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`
- `common/decisions/categories/006_independence_wave_far_eastern_categories.txt`
- `common/decisions/006_independence_wave_far_eastern_decisions.txt`
- `common/ideas/006_independence_wave_far_eastern_ideas.txt`
- `common/ai_strategy/006_independence_wave_far_eastern.txt`
- `localisation/english/006_independence_wave_far_eastern_l_english.yml`
- `common/national_focus/006_independence_wave_focus.txt`
- `docs/events/006_independence_wave/far_eastern_republic_package.md`

## Package contract

The package ID is `iw_057` and the country tag is FER. The installed region-05 loader orders state 408 before state 409 under reservation group RG-408-409. Both anchors are handled transactionally by package triggers, and the package never assumes that 408 is always present.

The adapter uses `volga_urals_siberia_far_east`, regional package depth, `river_or_corridor`, `regular_defectors`, military tradition `p57`, and the shared five-pathway regional-defectors reinforcement mask. Naval and air inheritance are required before prepared setup can pass.

The founding mission is `independence_wave_fer_hold_railway_council`. The ten serialized projects are `independence_wave_fer_secure_railway_ports`, `independence_wave_fer_integrate_coastal_guards`, `independence_wave_fer_register_fer_communities`, `independence_wave_fer_settle_former_host_ledgers`, `independence_wave_fer_ratify_constitutional_autonomy`, `independence_wave_fer_adopt_railway_charter_compact`, `independence_wave_fer_convene_coastal_councils`, `independence_wave_fer_establish_coastal_emergency_command`, `independence_wave_fer_codify_durable_sovereignty`, and `independence_wave_fer_open_pacific_corridor`.

The package uses `independence_wave_fer_congress_cohesion` and `independence_wave_fer_rail_security` as clamped ledgers. The package exposes constitutional, popular-council, patron-client, and emergency-military route installers, with no traditional-restoration route or route-specific flag output.

## Parent-owned gates

`independence_wave_iw_057_identity_rights_cleared` and `independence_wave_iw_057_command_roster_ready` are required before the local roster checkpoint can publish `independence_wave_command_roster_ready`. The package does not create or reuse a character and does not claim a portrait or institutional source.

Vanilla FER history currently uses capital state 563, while the Event 006 registry orders 408 and 409. The local runtime trigger therefore requires an ordered anchor and a capital in one of those anchors, leaving admission blocked until the parent resolves the capital/anchor policy. No map rewrite was made.

The neutral FER flag ladder remains unresolved. No FER source master, runtime TGA, DDS, GFX sprite, cosmetic tag, or flag override was created by this tranche.

## Evidence

The mandatory map inspection for states 408 and 409 returned `MAP_INSPECTED` with selected state and network checks available, but aggregate validation remains false because unrelated workspace building and port-position diagnostics are truncated. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea26cd826bed9fb358ce4a3ce41cd0da865d30628fef46a088e5b841279c3c75/f75e84c397c6843033475b5d8f90119cb737995730a17ded486800088d2fdd9c/map-inspect.b5b6f687d205e3ef.json`.

The mandatory focus inspection returned `FOCUS_INSPECTED` after the FER hooks and one pre-existing unmatched closing brace were reconciled. The current tree has 73 parsed nodes, 81 connectors, no crossings or node intersections, and 14 unrelated diagnostics, mostly vanilla continuous-focus icons plus authored layout warnings. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3cdd3f566663246fa47b8311ab0866dd897341dc15f731a09c74a7de2d1dad5/b19c80ec55dfc0fe53f719dec523a997d6a5b074cd4c64d6294b73c0399b722e/focus-inspect.38900658b3dffab6.json`.

The corresponding focus render returned `FOCUS_RENDERED` with source-linked HTML, SVG, JSON, source-map, and plan artifacts. The render retained the existing layout hash `436cada0493e0729f64eca15c262b54c3cc92bc53b788ebf55e2e12a0c27ea84`.

The focused Event 006 scan returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and deferred workspace-wide helper/lifecycle projections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfe44b52276914a5e860272a86ee2ed49791894833dbd5b5dbe710c8a7b3a90b/a5aab58a07811c7c1774afab2eef061bd11500b161b3882af3f6318c055963f5/event-scan-307dfcac585c.json`.

The bounded Event 006 overview render returned `EVENT_RENDERED_PARTIAL` with source-linked JSON, SVG, PNG, HTML, and manifest artifacts. The render is partial because the workspace-wide projection is deferred. Manifest artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/933d679b3915aaf1d76ccefe8b482f194ba7029fb12d1e1e5b654f9793d0669c/a1e5b84582c18fe7a030bd2d076bcc601379530814111b263e25eac6f4369113/event-overview-307dfcac585c-manifest.json`.

The mandatory probability inspection for `ai_strategy_factor` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44e020acbc163bb07c50786c280a104391ed9a8ce48ddac7fda7cf38269489d8/c0f025aa3d47fa824e0d0dd26902a4584458fa65f48a6b8bfecf710920752191/probability-inspect-4b1b9d0035ee.json`. This is structural evidence only and is not a quantitative AI balance claim.

## Validation

The Event 006 allocator audit remains at 149 publishers, 40 adapters, 32 attested packages, 29 compatible groups, and 161 unattested selectable rows with the existing eight adapter-only IDs. The scenario matrix audit still passes all 32 cells and 8 edge cases. FER source files have balanced braces and no unsupported `<=` or `>=` operators. The FER localisation file is UTF-8 BOM encoded and contains no 156x210 portrait reference.

## Remaining blockers

- Parent must resolve vanilla FER capital 563 versus ordered Event 006 anchors 408 and 409 before any runtime admission.
- Parent must provide a source-backed FER institutional or leader roster and rights receipt before setting the identity and roster flags.
- Parent must decide whether a historical, reused, or explicitly generated FER flag is allowed; no neutral flag attestation exists in this tranche.
- Event005 Soviet-origin release and former-host ownership must remain separate from Event006 FER origin.
- Typed FER probability scenarios are still unavailable, and the no-weighted-surfaces result does not support a balance claim.
- Central attestation, normal/scenario preflight, dispatcher, and Join remain intentionally unchanged.
