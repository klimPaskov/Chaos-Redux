# Event 006 source-of-truth map

Curated: 2026-07-14

Scope: documentation reconciliation only. This file does not change gameplay, localisation, assets, the event workbook, or accepted Event 006 design.

## Authority order

1. The seven files under `../../specs/006_independence_wave_specs/specs/` are the accepted design authority.
2. The accepted package identities, tag assignments, dispositions, and reservation groups remain binding in `../../specs/006_independence_wave_specs/research/006_package_research_resolution.csv` and `../../specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`.
3. The dated files under `package_bindings/` are the numeric implementation authority for the installed 2026-07-14 map snapshot. They may narrow or disable a package when exact geography is unavailable. They do not broaden an accepted disposition.
4. The corrected descriptions in `../../specs/006_independence_wave_specs/research/006_super_event_text_research.md` are the promoted super-event description authority. Approved titles, buttons, and quotes remain unchanged.
5. Research, architecture, asset, and collision handoffs remain working evidence until their status below is promoted. Gameplay source files remain authoritative for implemented behavior.

When these layers disagree, preserve the accepted design and record the implementation blocker. Do not invent a fallback.

## Dated installed-map and tag snapshot

| Evidence | Verified result |
| --- | ---: |
| Accepted packages | 206 |
| Unique package IDs | 206, `IW-001` through `IW-206` |
| Bound packages | 149 |
| Unbound packages | 57 |
| Distinct current state IDs referenced | 205 |
| Installed state files | 1,081, IDs 1 through 1081 |
| Accepted reservation groups | 111 |
| Reservation membership references | 206, each package exactly once |
| Collision rows | 14 |
| Same-group collision rows | 12 |
| Cross-group automatic blockers | 1 |
| Cross-group route exclusions | 1 |
| Reused registered tags | 78, all present |
| Reserved new Event 6 tags | 128, all ending in `X` |
| Reserved-tag registry collisions | 0 |
| Reserved-tag cosmetic-key collisions | 0 |

The installed map has no Chaos Redux state-history override, root map override, or relevant `replace_path`. Every referenced current state exists. Every bound anchor is contained in its compact set, and no compact state is duplicated in its extended set.

Collision state IDs: `42`, `249`, `256`, `354`, `425`, `427`, `432`, `441`, `764`, `900`, `902`, `950`, `982`, and `986`.

### Accepted dispositions preserved

| Accepted disposition | Count |
| --- | ---: |
| `automatic_pool_ready` | 11 |
| `automatic_pool_ready_if_not_living` | 44 |
| `automatic_pool_ready_if_unique_state_exists` | 77 |
| `high_chaos_only` | 32 |
| `formable_or_route_only` | 9 |
| `specific_community_variant_only` | 30 |
| `scenario_variant_only` | 3 |

### Current readiness result

| Current verdict | Count |
| --- | ---: |
| `ready_automatic` | 10 |
| `ready_if_tag_not_living` | 44 |
| `ready_unique_state_confirmed` | 53 |
| `ready_high_chaos` | 28 |
| `route_only_bound` | 9 |
| `scenario_only_bound` | 1 |
| `specific_variant_only_bound` | 4 |
| `disabled_no_unique_current_state` | 29 |
| `specific_variant_only_unbound` | 26 |
| `scenario_only_unbound` | 2 |

The 57 unbound packages remain unavailable until an accepted design change or a future installed map supplies exact geography. A nearby broad state is not an authorized substitute.

## Machine-readable binding layer

- `package_bindings/006_current_installed_map_package_bindings.csv`: one current binding and readiness row for every package.
- `package_bindings/006_current_map_reservation_groups.csv`: all 111 accepted groups with bound and unbound members.
- `package_bindings/006_current_map_state_collisions.csv`: all 14 recomputed shared-state rows.
- `package_bindings/006_current_installed_map_binding_audit.md`: evidence, semantics, rebindings, disabled packages, collision gates, and host-survival implications.

## Decisions that remain unresolved

### State 354 Trabzon

`IW-067` Lazistan in `RG-LAZISTAN` and `IW-068` Pontus in `RG-PONTUS` are both otherwise automatic candidates. Their accepted reservation groups are distinct.

Recommended parent decision: preserve both accepted groups and add an explicit state-level mutual exclusion before either candidate becomes selectable. Do not merge the design taxonomy silently.

### State 441 Kashmir

Automatic `IW-139` Kashmir in `RG-NORTHWEST-SOUTH-ASIA` overlaps route-only `IW-149` Himalayan confederation in `RG-NORTHEAST-HIMALAYA`.

Recommended parent decision: require the Himalayan confederation route to consume or exclude the active Kashmir reservation. Preserve both accepted group identities.

## Super-event source state

### The League of New States

- Title remains `The League of New States`.
- Button remains `Small states, one covenant.`.
- The approved Wilson quote remains unchanged in the source specification.
- The corrected broad-leadership description is promoted into the canonical text-research file.
- The accepted `A Trumpet Voluntary` selection remains named.
- Audio ID `6001` is blocked. The exact London Brass Players recording lacks verified United States redistribution clearance. It was not downloaded and must not be processed or wired.

Unblocking requires permission or a waiver for the exact recording. Reopening the recording selection requires explicit user approval.

### Every Border a Casus Belli

- Title remains `Every Border a Casus Belli`.
- Button remains `They have sown the wind.`.
- The approved Hosea quote remains unchanged in the source specification.
- The corrected route-neutral description is promoted into the canonical text-research file.
- Audio ID `6002` is available in the current audio registry snapshot.
- The United States Marine Band source is preserved at `../../assets/006_independence_wave/super_events/audio/source/1812_Overture_-_United_States_Marine_Band.opus`.
- Source bytes: `12,999,461`.
- Source SHA-256: `93c141a2e5782385e8a9b53f5f622afcb604da6f361fe1ca2e160ea4bfe92d3d`.
- Final production remains queued.

Final super-event display slots remain unassigned. The explorer's observation that slots 57 and 58 appeared unused is discovery evidence only and must be rechecked when wiring.

## Artifact disposition ledger

| Artifact or finding | Disposition | Reason and next owner |
| --- | --- | --- |
| Current installed-map package CSV | Promoted | Dated numeric implementation binding for all 206 packages |
| Current reservation-group CSV | Promoted | Preserves all 111 accepted groups and all 206 memberships |
| Current collision CSV | Promoted | Exact 14-row collision ledger |
| Installed-map audit and handoff | Promoted | Evidence-backed map snapshot, rebindings, exclusions, and host-survival gates |
| Trabzon cross-group automatic collision | Unresolved | Parent must choose and implement the explicit state-level exclusion |
| Kashmir route collision | Unresolved | Parent must make the route consume or exclude the reservation |
| Super-event text source verification | Promoted | Source verification and two corrected descriptions were folded into canonical research |
| ASCII omission-mark recommendation for approved quotes | Rejected | This reconciliation was instructed not to alter approved quotes. Revisit only with explicit approval |
| Final super-event display-slot assignment | Queued | Recheck the live slot registry during wiring |
| Super-event audio rights correction | Promoted | Corrects the false claim that both exact recordings were cleared |
| `6001` London Brass Players recording | Blocked | Permission, waiver, or user-approved reselection is required |
| `6002` Marine Band production and wiring | Queued | Source and production recipe are verified, final derivatives are absent |
| Event 6 asset source handoff and three asset ledgers | Queued | Covers 167 eligible packages, but no final binary was produced and individual rights gaps remain |
| Conditional and blocked portrait or symbol sources | Blocked | Resolve each source's exact rights and identity gate before copying or production |
| Event 005 collision handoff | Queued | Integrate the 20 shared tags, geographic exclusions, origin guards, and joint preflight into gameplay |
| Scripted-system architecture handoff | Queued | Transaction design is accepted working guidance, implementation and validation remain parent-owned |
| Repository explorer handoff | Superseded | Its discovery paths remain useful, but its current-state claim predates the new shared release foundation and completed map binding |
| Optional map-tool `MAP_MODEL_BUDGET_BLOCKED` result | Rejected | It is not evidence and no fallback binding was derived from it |

## Asset research boundary

The asset census covers 167 automatic, high-chaos, and scenario-only packages:

- 63 identity-matched registered-base reuse packages
- 44 generated civic-baseline packages
- 35 attested-symbol or restoration-study packages
- 15 exact-community review packages
- 10 signature dossier packages

The 9 route-only and 30 specific-community packages remain outside that production tranche. All 74 registered tag families in the 167-package scope have complete installed flag triplets, but only 63 are approved for identity-matched base reuse. This is availability evidence, not final provenance or production completion.

## Event 005 integration boundary

The collision handoff identifies 20 exact shared tags: `KAR`, `DON`, `KUB`, `CRI`, `TAT`, `BSK`, `CHU`, `MEL`, `UDM`, `KOM`, `YAK`, `BYA`, `ALT`, `NEN`, `FER`, `CIN`, `DAG`, `ARM`, `GEO`, and `AZR`.

Event 005 must publish its exact provisional tag and state footprint before Event 006 draws. Event 005 must also exclude active Event 006-origin countries from terminal adoption and restrict focus replacement to countries actually created by Event 005. These findings are queued gameplay work, not promoted source-design changes.

## Restart pointer

Continue from `006_independence_wave_resume_packet.md`. Any implementation that changes an accepted identity, disposition, title, button, quote, musical selection, or reservation taxonomy requires an explicit parent or user decision recorded before the change.
