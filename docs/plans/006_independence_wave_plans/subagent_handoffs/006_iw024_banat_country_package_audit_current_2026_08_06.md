# IW-024 Banat (`AXX`) country-package audit — current 2026-08-06

## Scope and verdict

This handoff records the parent review of the IW-024 Banat package after the bounded country-package and portrait tranches. AXX is source-attested and conditionally selectable through the central Event 006 dispatcher. It remains subject to the normal exact-tag, host-survival, reservation, collision, force, synchronized-transaction, and final-validation gates; this handoff does not claim a live release, save/load, or player-owned balance result.

## Identity, map, and origin contract

- Carrier: registered `AXX` Banat; no new tag, replacement country definition, or vanilla history overwrite was introduced.
- Region/archetype/depth: `balkans_danube`, `mountain_or_frontier`, regional depth.
- Exact anchor/capital: state `82`; the current-map gate requires state 82 to be owned and controlled by the released AXX carrier.
- Former host: `ROM`; setup and runtime proofs require the ROM former-host scope and a protected ROM-owned remnant state.
- Reservation group: `RG-DANUBE-BORDERLAND`; the sibling TRA/AXX capacity remains bounded by the matrix and unique anchor checks.
- Origin separation: the package requires the Event 006 origin and rejects Soviet Collapse origins.

## Playable package surfaces

- Leader/roster: sourced male Otto Roth is archived as a `source_placeholder` portrait, attached by the synchronous `chaosx.nr6.350` checkpoint, and reused for the civilian-large and army-large consumer roles. No advisor, dossier, small, female, or invented leader portrait was added.
- Setup: `common/scripted_effects/006_independence_wave_banat_package_effects.txt` initializes baseline laws, politics, civic/defence ledgers, lifecycle ideas, the command roster, shared focus framework, p24 force mapping, AI profile, route families, host/league/formable hooks, and five reinforcement pathways.
- Visible values: `independence_wave_axx_civic_mandate` and `independence_wave_axx_mountain_defence` are changed by focuses, projects, routes, host settlement, and failure cleanup. No political-power store or passive checklist substitute is used.
- Government/routes: constitutional, popular-council, traditional, emergency-military, and patron-client routes are paid and mutually exclusive through the package decision surface.
- Decisions/mission: `common/decisions/006_independence_wave_banat_decisions.txt` supplies one bounded founding mission and eleven costed projects with administration, security, diplomatic, strategic, factory, and time costs. Projects cancel on capital loss, host-war invalidation, route withdrawal, or package cleanup.
- Ideas: two lifecycle ideas and five route ideas are wired in `common/ideas/006_independence_wave_banat_ideas.txt`.
- AI: `common/ai_strategy/006_independence_wave_banat.txt` adds survival, former-host restraint, settled-state, and emergency-commission layers. The installed MCP probability adapter does not expose the AXX `ai_strategy_factor` surface, so no quantitative AI-balance claim is made.
- Cleanup: package decisions, mission, ideas, variables, flags, command roster receipt, and portrait receipt are cleared by the identity-specific cleanup adapter.

## Asset disposition

The Otto Roth source package is `006_iw024_banat_otto_roth_portrait_source_placeholder_2026_08_06.md` and its durable archive under `docs/assets/portraits/006_independence_wave/iw024_banat_otto_roth_source_placeholder_2026_08_06/`. Runtime DDS wiring is `gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds` with sprite `GFX_portrait_AXX_independence_wave_otto_roth` in `interface/006_independence_wave_iw024_banat_portraits.gfx`.

The base flag ladder is `gfx/flags/AXX.tga`, `gfx/flags/medium/AXX.tga`, and `gfx/flags/small/AXX.tga`. The accepted source is the flat ImageGen alternate-history civic synthesis in `source_png/AXX_banat_imagegen_flat_raw.png`, with red/white/blue bands, a restrained gold lion silhouette, and river bars. It is explicitly not presented as an attested historical Banat flag. The earlier detailed heraldic-shield source is retained as rejected evidence and is not the runtime consumer.

## Validation evidence

- `python -B .tools/audit_event6_allocator.py` passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 24 content-attested packages, 22 compatible reservation groups, the 20-package static witness, and the 6/8/10/14/20 ladder.
- `python -B .tools/audit_event6_flags.py` passes all 102 registered Event 006 flag families; AXX's replacement ladder has exact 82x52, 41x26, and 10x7 bottom-origin uncompressed 32-bit TGA headers and readback equality.
- `python -B .tools/audit_event6_scenario_matrix.py` passes all 32 SCN-008 cells and eight edge cases.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reports zero external country-definition and identity-surface collisions for the protected Event 006/Soviet tag scope.
- `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; its large-workspace deferral is recorded rather than treated as a full runtime proof.
- `hoi4.focus_inspect` for `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED`; the five reported layout warnings and fourteen unrelated vanilla continuous-focus icon diagnostics are not AXX-specific runtime blockers.
- Targeted source scans found balanced braces, no unsupported `<=`/`>=`, no whole-world on-action iteration, no undefined AXX-prefixed scripted calls, and no missing AXX decision icon sprites.

## Current MCP evidence

- `hoi4.probability_inspect` with adapter `decision_ai_will_do` and source `{ "path": "common/decisions/006_independence_wave_banat_decisions.txt" }` returned `PROBABILITY_SOURCE_INSPECTED`, one candidate, ten required inputs, zero unresolved diagnostics, and `poolComplete = false`. The source hash is `ab8595935e7f95aaa473fd4f9085486cb4036e125fc381852c7e5370e8a20457`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5de510e2e32e7af0a733d2583e8cee238d39c707095c08ab78bba1b38654ebd9/3b792a0979c1fea3743e81041e17c511b33e4dc24aced9e776b5f8097a1d2e3b/probability-inspect-ab8595935e7f.json`.
- `hoi4.probability_inspect` with adapter `mission_ai_will_do` against the same source returned `PROBABILITY_SOURCE_INSPECTED`, eleven candidates, thirteen required inputs, zero unresolved diagnostics, and `poolComplete = false`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c36dd5dc3d33d64082b448f726aeb6bd7c1ac7082a3fb4b39ce6f8d947714877/1dda72f2a49b549dc0e1c2224bbbd0ee8617cb43fb6becf3bd55ac769b2d879e/probability-inspect-ab8595935e7f.json`.
- `hoi4.probability_inspect` with adapter `ai_strategy_factor` and source `{ "path": "common/ai_strategy/006_independence_wave_banat.txt" }` returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request`; no strategy ranking or quantitative AXX balance claim is made.
- Focused `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; the workspace-wide helper/lifecycle projection was deferred by the installed MCP. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b88d56605efd2c666ed70571dee0f4b350a5a7dec9dcaa6d7f3870ecfd06a499/a58df4c4e1ae89d1db1577fa52ac51e07a612a1db3adffe0206321bfd5203f22/event-lint-944ba605ebe4.json`.

## Remaining limits

The AXX probability surface is typed-state incomplete in the installed MCP adapter, so no normalized AI ranking, survival, timing, or route-dominance claim is made. Live game execution, save/load, and player-owned transition evidence remain outside this handoff. The Danubian FORM-08 family remains separately fail-closed and does not inherit AXX package admission.
