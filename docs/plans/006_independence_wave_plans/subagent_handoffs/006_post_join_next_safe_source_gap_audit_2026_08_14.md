# Event 006 post-Join next-safe-source-gap audit

Date: 2026-08-14

Audit base: `6fc828454b813c0cfe6660a255991b431bf39867` (`Implement scoped Event 006 Join conversion`)

Mode: read-only completion audit. No gameplay, localisation, asset, workbook, or runtime file was changed.

## Disposition

No additional narrow source patch is justified after the Join conversion commit.

The strongest remaining accepted requirement gap is the Part 5 country-package breadth contract. Current source authority remains 40 runtime adapters, 32 content attestations across 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows. Eight adapter-only rows remain deliberately fail-closed: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179. IW-047 MEL and IW-050 KOM remain package-local, unadmitted, and outside deterministic Join.

This is not a mechanical OR-list defect. Adding any unattested ID to `has_independence_wave_runtime_package_content_attestation_for_execution_id` without its complete independent package evidence would defeat the accepted fail-closed policy. Part 5 requires identity, tag policy, anchor and territory, host survival, leadership, parties, ideas, forces, reinforcement, economy and logistics, relationships, recognition, league behavior, ambitions, source-mode evidence, AI, focus or overlay assignment, decisions, localisation, and documentation before admission. A one-line attestation or adapter expansion is therefore unsafe.

## Exact source and authority evidence

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:7-35` defines the package contract and `:1060-1084` defines the ready-package validation gate and mandatory runtime skip for missing surfaces.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:8-59` contains the 40 runtime adapter IDs. `:159-208` contains the exact 32-ID content-attestation allowlist. `:211` makes content attestation a preflight requirement.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:5`, `:116`, and `:124` preserve the current 40 / 32 / 29 / 161 authority and the MEL/KOM fail-closed boundary.
- `.tools/audit_event6_allocator.py` passed on the audited worktree and reported 149 publishers, 40 adapters, the eight adapter-only fail-closed IDs, 32 attestations, 29 compatible reservation groups, the `3/4/5/7/10` ladder, and World Collapse target 10.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 type and intensity cells plus eight declared edge cases.
- `.tools/audit_event6_flags.py` reported 102 registered Event 006 tags and 102 complete flag families.
- `.tools/audit_event6_country_api.py` passed with 191 resolved unique carriers, zero missing registrations, and zero duplicates.
- `.tools/audit_event6_form16.py` passed the ARM/GEO/AZR member, territory, consent, mutation, cleanup, and fail-closed readiness contract.

## Closed source gaps not reopened

- Join is implemented by `6fc828454`, with exact 32-package conversion parity and preserved MEL/KOM exclusion.
- The TAT AI strategy mirror mismatch identified by the earlier package scan is already corrected in `common/ai_strategy/006_independence_wave_tatarstan.txt`.
- KOM roster checkpoint, project lifecycle, strategic costs, and cost localisation are already repaired by the current committed tranche.
- The Iberian founding missions are already serialized by `fe7fd3925`.
- Evolution incident disable cleanup and package cost-localisation triplets are already repaired.
- Focus-layout warnings, rights and provenance gates, dedicated GUI evidence limits, and probability-adapter limitations were excluded from candidate selection for this pass.

## Current event MCP evidence

All twelve Event 006 event files were submitted to file-scoped `hoi4.event_inspect` at current event revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`. Every inspection returned `EVENT_INSPECTED_PARTIAL`, status `ok`, one linked artifact, and no selected blocking diagnostic. The partial status remains structural source evidence rather than engine or live-runtime proof.

| Event file | Inspect artifact |
| --- | --- |
| `events/006_independence_wave.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c94aac4e59fcc5919350d02188774d2a025415b3c126eb6b346cad99720f1755/11f7c3d854a62e5d60a99525e153d4c7f0efbf78b23de63b7fe4de1ac34b9830/event-scan-741883f50501.json` |
| `events/006_independence_wave_join.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99ebba0a1f68db243f3c14dbe0722506728345212d757e58c31d5f4dd5e755ae/4cab88582afd6de7708a72b57d816d5ac126cbc86c53957d6dc37fb09d07e665/event-scan-741883f50501.json` |
| `events/006_independence_wave_scenario.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e802636da2a1ce57ea1c4f3facf4d80fe68f284e9ca1a22ada92b2b65309773a/7bf978cf1aff4560946b3d0184db9e7111e1d522ff0906602a11b092242df8ac/event-scan-741883f50501.json` |
| `events/006_independence_wave_rhineland_bavaria.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0c6e7e40f3d96d17cb3c1c0ccdd09d621bff0288627cd700cf2838768cb78d8/4bf72f7892aa394c8f3b5181152ff2cbb9c75b541731a4c5568a33fb19cd5c15/event-scan-741883f50501.json` |
| `events/006_independence_wave_wallonia_frisia.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22749812bb459f4458d9257d35baf666fdfeedaa18f3edeb043100784bdd1be1/80c98a2d5d7d2b192b7c1ce2b7b7a92a1907306386e3ac0aec03145214730dca/event-scan-741883f50501.json` |
| `events/006_independence_wave_mediterranean.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd0094da8716808f3b8d8d570a0e2417a1c397369f234fc502797e570bc120dd/f094b8deb208f872fd4236025c8f47c6753ab16c08c03345b1a5ce60edc9260e/event-scan-741883f50501.json` |
| `events/006_independence_wave_form01_02_04.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a896dd44941c223b36bf50a38e3bc99fa24adb01d76f82fb7a7e7e3f9dc9a615/78f0bd5a66b22d35a8600bd8ee6de31700179e7599041eace6326aea74ee06f4/event-scan-741883f50501.json` |
| `events/006_independence_wave_form05.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f292af53ea9e44c39c1cc0369a206bba83a3b7ba0a5a538b4535b411c0464123/0c5e9d44df8d139526d39217af034321cf3b5f4555c666a17d60ba52b7935843/event-scan-741883f50501.json` |
| `events/006_independence_wave_form16_events.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/221d6aa3c8ed74a1a299066b93f72d5f1e1952b3e30f9b5f161c2fafcf4bebec/17f316799e2f4582a455df9057199a0bd7edb45caaf99bfd09015c292f5cc56a/event-scan-741883f50501.json` |
| `events/006_independence_wave_iw043_iw058.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4897f2f0de0f8522d5a6cee8fbd8ec1d4be81b9bb73790599db14a2d2de863e/6b3931b53b8ea1ee31d09a203543d51f4e13f298bba1c6f745e5f78eecf3f887/event-scan-741883f50501.json` |
| `events/006_independence_wave_iw093_iw098.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d87cf6dcb25272923f8750347aa48a69b0177b165dd012cb7f11d38de2d1968/afc11a71c02bc6b00a6f7833abdd686975b2b5827744d2fee871f2569b7d324d/event-scan-741883f50501.json` |
| `events/006_independence_wave_evolution_incidents.txt` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/322de31536872a6a3ed2f8093ebc5081006603217d9375e68547d229bef68947/0f6d56da15d35614d6c977e340ca91e1df50839a7b8d56ff1180126f8520ce03/event-scan-741883f50501.json` |

`hoi4.event_render` overview calls returned `EVENT_RENDERED_PARTIAL`, status `ok`, with JSON, SVG, PNG, and manifest artifacts for eight files: the root event file, scenario, Rhineland/Bavaria, Mediterranean, FORM-01/02/04, FORM-05, FORM-16, and IW-093/IW-098. The parallel calls for Join, Wallonia/Frisia, IW-043/IW-058, and evolution incidents reached the exact MCP client blocker `timed out awaiting tools/call after 180s`. Their successful inspections remain recorded above, but this source review is not a substitute for the missing render artifacts.

The required comparison from pre-change revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2` to current revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b` returned `EVENT_REVISION_NOT_CACHED`, status `error`, with zero artifacts. The exact blocker is that the requested event graph revision is not cached. No before-and-after comparison claim is made.

No new weighted source defect or proposed weighted change was identified, so this pass did not create a probability patch cycle. Current KUB/TAT evidence remains the bounded score-only or partial evidence recorded in `006_event6_probability_current_2026_08_13.md` and the current AI evidence recheck. It supports no quantitative probability claim.

## MCP evidence required for any future package admission

A future bounded package tranche should not patch central admission first. Its evidence should include file-scoped event inspect and render for any new package event or setup call, map inspect and render for every exact anchor and territory binding, focus inspect and render for a package tree or overlay, GUI inspect and render only if the package introduces an Event 006-owned dedicated interface, and a `chaosx_ai_probability_auditor` pass for every weighted decision, mission, focus, event option, random list, or AI strategy surface. After any weighted patch, the same scenarios require `hoi4.probability_compare`. After any event-source change, preserve a cached event baseline and run `hoi4.event_compare`.

## Accepted-plan disposition and next action

No accepted plan is promoted or rejected by this audit. The seven accepted spec parts remain authoritative. The current Join tranche is implemented. The 32 admitted packages remain admitted. The eight adapter-only rows and MEL/KOM remain fail-closed. The 161-row breadth backlog remains unresolved.

Recommended next action is a separately scoped country-package admission tranche only after one specific unattested package has a complete identity, source, map, gameplay, AI, localisation, asset, and documentation packet. No central adapter or attestation edit should be made from this audit alone.

Event 006 remains HOLD / PARTIAL. This handoff makes no whole-event completion claim.
