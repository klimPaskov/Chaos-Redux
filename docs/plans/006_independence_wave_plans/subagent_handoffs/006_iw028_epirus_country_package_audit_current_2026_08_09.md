# IW-028 Epirus package audit handoff

Date: 2026-08-09

Status: source-attested and admitted to the current Event 006 closure.

## Locked identity and reservation

- Package: IW-028 Epirus.
- Runtime carrier: `BBX`, a registered dormant Event 006 `X`-ending carrier shell.
- Installed anchor: state `185`, Epirus.
- Optional extension: state `805`, Northern Epirus; it is trimmed if it cannot be allocated without violating unique-state or host-survival rules.
- Former host: `GRE`, with the host retaining its protected remnant.
- Reservation group: `RG-185` / `rg_185`.
- Region: Balkans and Danube.
- Package depth: standard.
- Archetype: mountain or frontier.
- Force profile: mountain frontier, with package mapping `p28`.
- Formable family: Balkan Federation.

FORM-09 is registered through the shared transaction with `BBX` and `BAX` as reviewed carriers and `BOS`, `MAC`, and `MNT` as compatible member packages. The carrier adopts the X-ending `BLX` cosmetic identity; it does not allocate another country tag or replace the carrier's Event 006 package.

## Package surfaces reviewed

The package-specific effects, triggers, decisions, ideas, constants, AI strategy, historical character consumers, localisation, portrait GFX, central dispatcher, Region 03 loader, synchronous roster checkpoint, and shared-tree hooks were reviewed together.

- `common/scripted_effects/006_independence_wave_epirus_package_effects.txt` owns setup, two visible ledgers, lifecycle ideas, five government routes, host settlement, league/network action, paid projects, force mapping, final validation, and generation-safe cleanup.
- `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt` proves exact tag, anchor, host, separate political and command rosters, ledgers, focus framework, route, formable, force, AI, and cleanup readiness. The founding mission is not treated as an active project, so its remediation decisions remain usable.
- `common/decisions/006_independence_wave_epirus_decisions.txt` exposes one 330-day founding mission and eleven concrete administration, security, diplomatic, strategic, route, host, and network projects with time and resource costs. Mission success requires both stable package ledgers and a selected route government. No political-power store or free-unit loop is used.
- `common/decisions/categories/006_independence_wave_epirus_categories.txt` registers the visible Epirus Civic Council category for the exact prepared BBX package.
- `common/ideas/006_independence_wave_epirus_ideas.txt` defines two lifecycle ideas and five mutually exclusive route ideas.
- `common/script_constants/006_independence_wave_epirus_constants.txt` centralizes politics, ledger thresholds, project duration, and AI tuning. All six politics distributions sum to 100.
- `common/ai_strategy/006_independence_wave_epirus.txt` provides survival, former-host restraint, settled compact, and emergency mountain-defence layers.
- `common/characters/006_independence_wave_epirus_characters.txt` keeps sourced male Georgios Christakis-Zografos as the political leader and uses separately sourced male officer Spyros Spyromilios as the corps commander. No advisor, high-command, dossier, or small-portrait surface is defined.
- `localisation/english/006_independence_wave_epirus_l_english.yml` contains the package's party, idea, mission, decision, tooltip, cost, ledger, and sourced historical identity text.
- `interface/006_independence_wave_iw028_epirus_portraits.gfx` wires both runtime portrait DDS files.
- `gfx/leaders/006_independence_wave/portrait_BBX_independence_wave_georgios_christakis_zografos.dds` and `portrait_BBX_independence_wave_spyros_spyromilios.dds` are 156x210 original-source placeholders. Their attributed originals, explicit crops, provenance, processed candidates, and DDS handoffs are archived under `docs/assets/portraits/006_independence_wave/`.
- The BBX flag uses the historically attested 1914 Northern Epirus geometry. Public-domain flag photograph, stamp, and clean-reference evidence, the ImageGen reconstruction source, flattened master, final TGAs, prompt, manifest, and hashes are retained under `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/`; all ideology variants intentionally use the same historical design.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt`, `events/006_independence_wave.txt`, and `common/national_focus/006_independence_wave_focus.txt` carry the central setup, final-validation, cleanup, exact planner, two-character roster, and generic-focus hooks.

## Source and MCP evidence

- `python -B .tools/audit_event6_allocator.py`: PASS. The current closure is 26 attested selectable packages across 24 compatible reservation groups, 167 unattested selectable rows, a 20-package static witness, and the 6/8/10/14/20 ladder.
- `python -B .tools/audit_event6_flags.py`: PASS. All 102 registered Event 006 tag families have complete flag ladders.
- `python -B .tools/audit_event6_scenario_matrix.py`: PASS. All 32 SCN-008 mode/intensity cells and eight edge-case receipts remain present.
- `python -B .tools/audit_event6_country_api.py`: PASS. Broad and resolved carrier inventories have no missing or duplicate API entries.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`: PASS. The protected Event 006/Soviet tag audit reports zero external country-definition or identity-surface collisions; Random Events Mod is excluded by accepted policy.
- Package-local checks found balanced politics distributions, no tool-output contamination, no unsupported comparison operators, no stale Thrace identifiers, and no missing player-facing BBX localisation keys.
- Shared focus inspection returned `FOCUS_INSPECTED`, revision `adad547aea4964b1f06733fffbefa10c303548937fd4c036e3a99e6e39f99a87`, 184 focuses, 193 connectors, zero crossings, zero node intersections, and no too-close same-row pairs. Its 14 blocking icon diagnostics belong to installed vanilla continuous focuses rather than Event 006. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25a4e5aae4b873e4e2accdc2bf64bc4e3822cfac24b3f0ecdbd3f4acd305c7ad/2a3fd762c44b0f3f60fd5673a1bb7f72d9d5a158570a4c5c6f9368106c61af2e/focus-inspect.adad547aea4964b1.json`.
- Event lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL`, revision `2517cfba88646855fe92476143951b53d1670fd91f8c6b9926dcd6f84264ab39`, with no blocking diagnostics; the large workspace deferred whole-workspace helper projection. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c21d644440b0f92d354e55157d32a744da925f920532479961ded226f7f37138/50649dfe37dbeb259b10cb7be179dfc900a7abad91a02d4283cb687933cabe19/event-lint-2517cfba8864.json`. A later forced refresh returned an MCP internal error after the two-character roster edit, so this remains partial evidence rather than a post-edit whole-workspace pass.
- Map inspection returned `MAP_INSPECTED` and resolved both selected state records 185 and 805. The workspace-wide validator also reported unrelated installed `map/buildings.txt` position and port diagnostics; no global map-clean claim is made. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cc7f9daa96e82b96e667ed301cd51b46d93a37b5ec728edee4f441867db4803/6b809ad9d5d0a1656a4eccacdaa79ad7a3346997b325858ffe9ecbbe040ce146/map-inspect.1840a1b9e0813e56.json`.
- Decision probability inspection returned `PROBABILITY_SOURCE_INSPECTED`, one discovered candidate, ten required runtime inputs, zero unresolved source diagnostics, and `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c538f8a94d1d1fe4f2ad4fedcc38886907a3315274e470880380517a6de76fa7/3092513b65cb90e4bdf41bee02cbff8fb383a77ac8bd607c8630cc561c2216ee/probability-inspect-840a326a55fe.json`. The AI-strategy adapter returned `PROBABILITY_SURFACE_EMPTY`; no quantitative BBX probability or AI-balance claim is made.

## Portrait and flag review

The Georgios source-placeholder chain preserves the public-domain historical portrait identity. The Spyros Spyromilios chain uses the Athens War Museum public-domain image, explicit crop `[33,4,215,249]`, source SHA-256 `8e991b0d06bbb395ce3a23c76a7329e10f7512d3519fd8b5ad3f02ac632d10fa`, and runtime DDS SHA-256 `632b768513d3f603c19285f416d72be95df90d2d01d0cd866b4b80cc20210145`. Independent parent visual review passed identity, male subject, head-and-shoulders framing, and placeholder readability. No historical portrait was repainted with ImageGen.

The flattened BBX master uses exactly solid blue, white, and black design colours. The source, master, package TGA, runtime TGA, dimensions, uncompressed 32-bit type-2 headers, bottom-left origin, and metadata hashes all match. The normal, medium, and small runtime hashes are `c7dc18e5804be779a84526ad98e44a32ee567662c0ed4f98793a0f09ef75b8f1`, `abd3433d7281567179cdb1b1dd9e36b852bd8d9564b1f9814679994c8195f3e4`, and `255ad2a4cdf4e7b9d50a47b19c78cbb283a38c49ea26c3bb6fbe1967eb82afa3`.

## Post-audit repairs

- The five BBX package focus hooks are reachable through exactly one ordinary full-framework path: capital administration, state inventory, first oath, former-host policy, and recognition of fellow new states. The additive copies remain unavailable during normal full-framework ownership, and the reviewed existing-tree carrier allowlist is unchanged. Post-fix MCP inspection returned 184 focuses, 193 connectors, zero crossings, and zero node intersections at revision `5cc6b3f77de8b229225ec0c287d075a8ef49116a8d0e683fd976bb40d862115a`.
- The p28 reinforcement mask is `647`, which decodes to militia integration, regional guards, secured depots, terrain units, and professional officers. It now matches package setup, readiness triggers, the force-mapping CSV, and Spyros Spyromilios's sourced corps-command role; the unintended capital-border pathway is excluded.
- Player-facing text exposes both current BBX ledger values and the stable threshold, states every package delta exactly, gives each government route a distinct outcome tooltip, removes working labels, and presents dense resource costs in icon-first rows. The final narrow localisation re-audit found no remaining defect in those surfaces.
- The settled MCP probability inspection remains incomplete because the decision adapter indexes one of twelve nested category blocks and the AI-strategy adapter returns `PROBABILITY_SURFACE_EMPTY`. The named scenario evaluation is partial and does not support normalized selection probabilities, dominance, starvation, or rank-reversal claims.
- FORM-09 now has a fail-closed identity, member, territory, military, rollback, and post-formation adapter. Its frozen ledger counts the carrier as one consenting founder, requires two additional consenting reviewed anchors, transfers only certified compact anchors under full-integration consent, preserves autonomous members, and exposes the paid 120-day Federal Border Board project. The `BLX` ImageGen-derived flag family has all 15 runtime variants across the three HOI4 sizes and passes the Event 006 flag-family audit.
- The post-fix country and decision re-audits found no remaining FORM-09 consent defect. Shared paid membership decisions accept family 9, the explicit AI resolver records full integration, autonomy, or refusal against the live proposal, unanswered candidates remain observers, and the integration loop independently requires a frozen accepted invitation before any member mutation. The localisation re-audit also passed the FORM-09 prose, border-board outcome, and all exact Epirus delta tooltips.

## Remaining risks

This admission does not claim live game, save/load, or player-owned transaction evidence because those are outside the current goal. The historical portraits are accepted original-source placeholders rather than styled finals. The typed decision pool is incomplete, the AI-strategy probability surface is unavailable, and the post-roster forced event refresh returned an MCP internal error. Ordinary super-event `23` remains blocked on its separately documented audio/firing package, unadmitted formable families remain fail-closed, and 167 selectable registry rows remain unattested outside IW-028.
