# IW-015 GLC country-package audit — 2026-09-12

Disposition: `NO-CHANGE / FAIL-CLOSED / NO PROMOTION RECEIPT`.

This is a bounded audit of IW-015 Galicia against the accepted Event 006 specifications and matrices, the current source-of-truth map, the Iberian package documentation, the current GLC handoffs, the current GLC source, the required vanilla references, and read-only HOI4 MCP evidence. No source-correct local gameplay defect was proven, so no gameplay source file was patched.

The package remains an adapter-only vanilla-carrier overlay. This handoff does not claim central admission, content attestation, deterministic Join eligibility, SCN-008 release capacity, live-game completion, or save/load completion.

## Accepted binding

The accepted package binding is `IW-015` / `iw_015`, carrier and `original_tag = GLC`, Galicia anchor state `171`, reservation group `RG-171`, region `Mediterranean and Iberia`, depth `standard`, archetype `agrarian_regional`, and former host `SPR`.

The accepted carrier contract preserves vanilla GLC history, tag, flag family, and leader roster. It does not authorize a replacement country shell, new country tag, new identity, invented flag, additive real-person leader, global admission change, or weakened origin, reservation, former-host-survival, or pre-event gate.

## Files and specifications inspected

The country/package surfaces inspected were:

- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`
- `common/decisions/006_independence_wave_iberian_decisions.txt`
- `common/ideas/006_independence_wave_ideas_registry.txt`
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/characters/006_independence_wave_characters_registry.txt`
- `history/general/006_independence_wave_character_recruitment_registry.txt`
- `common/country_tags/006_independence_wave_countries.txt`
- `common/countries/cosmetic.txt`
- `interface/006_independence_wave_portraits_registry.gfx`
- `localisation/english/006_independence_wave_iberian_l_english.yml`

The authority and current handoff surfaces inspected were:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/events/006_independence_wave/iberian_registered_packages.md`
- `docs/events/006_independence_wave/systems/country_registry.md`
- `docs/events/006_independence_wave/systems/formable_registry.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_glc_package_reaudit_2026-09-05.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw015_glc_flag_identity_2026-09-03.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw015_glc_portrait_gate_2026-09-03.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_glc_no_additive_roster_repair_2026-08-30.md`

The required offline Paradox wiki pages and relevant installed vanilla documentation were consulted before source review, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, event, decision, idea, AI, country creation, focus, technology, equipment, and division references.

Vanilla references included `common/country_tags/00_countries.txt:202`, `common/countries/Galicia.txt`, `history/countries/GLC - Galicia.txt`, `history/states/171-Galicia.txt`, vanilla GLC flags and ideology variants, and the installed GLC portrait definition.

## Country package coverage checklist

| Surface | Result | Evidence and remaining boundary |
| --- | --- | --- |
| Tag and country registration | PASS for registered-carrier reuse | Vanilla `GLC` maps to `countries/Galicia.txt`; no Event 006 GLC tag is present in `common/country_tags/006_independence_wave_countries.txt`. |
| Identity and history | PASS at carrier level | Vanilla GLC history remains the source of capital, politics, research, leaders, and starting setup. No replacement country history or invented identity is present. |
| Anchor and reservation | PASS source-level | `iw_015` binds state `171` and `RG-171`; planner uniqueness and state availability remain guarded in `can_plan_independence_wave_package_iw_015`. |
| Former host and collision safety | PASS source-level | Setup requires a live former host with its protected state still owned by the host; the package is absent from central admission and Join surfaces. Allocator audit passed with IW-015 in the adapter-only fail-closed set. |
| Setup, cleanup, and generation lifecycle | PASS source-level | GLC setup, validation, dispatch, and cleanup are generation-bound and restore vanilla portrait state when an override exists. No live/save-load proof is claimed. |
| Leaders and roster | PASS for preserved vanilla roster | Fuco Gómez and Alfonso Daniel Castelao remain the two required non-ruling-only GLC country-leader roles. The prior duplicate Castelao character/recruitment consumer is absent. |
| Portrait role and rights | ID wiring PASS; evidence gate unresolved | The existing Castelao role receives the package-specific GFX override once per generation and cleanup restores the vanilla GFX. Rights/date/provider receipt and `source_placeholder` versus older `styled_final` terminology remain unresolved. |
| Flags and route variants | Carrier family PASS; opening receipt unresolved | The installed vanilla GLC normal/medium/small and ideology families are complete. Democratic setup resolves `GLC_democratic.tga`, whose 1936 period/rights review remains open. No flag was copied, repainted, or promoted. |
| Parties and politics | PASS source/localisation coverage | Five GLC route installers set the accepted party names, ideologies, popularity, laws, and route ideas. No unapproved cosmetic tag is assigned. |
| Focus tree | PASS source and MCP layout evidence | GLC uses the shared `independence_wave_focus_tree`; no separate invented tree or route was added. See MCP section for current inspect/render limits. |
| Decisions and mission | PASS source/localisation coverage | The GLC council mission and eleven package decisions are present with visibility, availability, cancellation, effects, and localisation. No decision surface required a safe local repair. |
| Ideas and advisors | PASS for accepted scope | Seven GLC ideas have GLC-only allowed checks and lifecycle cleanup. No new advisor or unsupported real-person consumer was added. |
| Units, technology, industry, and supply | PASS source-level; no live balance receipt | Generic p15 `territorial_defense` force mapping, current-generation force gates, vanilla GLC history, and the accepted industry/port context are present. No GLC-specific technology dependency or major balance change is authorized by this audit. |
| AI and weighted logic | Source present; quantitative receipt blocked | GLC territorial, host-restraint, settled-port, and emergency strategy rows are present. The routed `chaosx_ai_probability_auditor` is not callable, and direct probability discovery found no weighted surface for this source. No weights were changed. |
| Localisation and assets | PASS for active package keys; external asset receipts unresolved | GLC package, route, decision, mission, party, and idea keys are present. The portrait and flag handoffs retain unresolved provenance/period decisions. |
| Formable and adapter boundary | PASS fail-closed | FORM-07 binds GLC to exact package `iw_015` and state `171`, but identity/flag/member/attestation gates remain closed. No formable readiness or central admission flag was set. |

## Tag, state, history, host, and collision audit

Vanilla `00_countries.txt:202` maps `GLC` to `countries/Galicia.txt`, and vanilla `history/countries/GLC - Galicia.txt:1` sets capital state `171`. The vanilla state source `history/states/171-Galicia.txt` identifies state `171`, 1936 owner `SPR`, `GLC` core, victory points, infrastructure, dockyard, air-base, arms-factory, and naval-base context. This agrees with the accepted current-map binding and does not justify a state-history patch.

The planner trigger at `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:142-148` checks package and reservation uniqueness, GLC carrier availability, and state 171 availability. The loader at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:414-426` binds `iw_015`, `RG-171`, `GLC`, state `171`, the anchor target, and the primary host. Reservation uses the existing `independence_wave_reserve_package_iw_015` contract at `:597`, not a new or widened allocator path.

The Iberian setup predicate at `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:52-70` requires the exact package id, region, depth, archetype, saved anchor state 171 owned and controlled by GLC, a living former host with its protected state still owned by that host, state 171 as capital, and both preserved vanilla leaders. The prepared setup predicate at `:198-238` repeats origin, anchor, host, roster, route, focus, force, lifecycle, and capital requirements. The exact runtime predicate at `:274-277` is deliberately not a content attestation.

Dispatch preflight keeps IW-015 in the existing adapter allowlist but does not add it to central attestation, scenario capacity, or deterministic Join. The exact execution checks at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:388-389` and the scenario check at `:558-559` remain untouched. No collision or invalid-host transfer was proven.

The allocator validator passed with 149 publishers, 40 runtime adapters, 32 attested packages, 29 compatible reservation groups, and the eight adapter-only fail-closed IDs including `IW015`.

## Politics, leaders, portraits, flags, advisors, and parties

The vanilla GLC history defines Fuco Gómez as the Marxist leader and Alfonso Daniel Castelao as the liberal leader, with Vicente Martínez Risco and Santiago Casares Quiroga as the other vanilla roles. The current package trigger requires Fuco and Castelao with `ruling_only = no`; no opposite-gender portrait/name pairing was found, and no fictional random-name pool is involved.

The current source contains no GLC entry in `common/characters/006_independence_wave_characters_registry.txt` or `history/general/006_independence_wave_character_recruitment_registry.txt`. The accepted no-additive-roster repair is still in effect, so no second Castelao identity is created and no new advisor or commander is invented.

The shared roster checkpoint at `common/scripted_effects/006_independence_wave_effects.txt:3296-3313` applies `GFX_portrait_GLC_alfonso_daniel_castelao` to the existing Castelao country-leader role once per package generation. Setup reset and cleanup at `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:479-484` and `:637-642` restore `GFX_portrait_Alfonso_Daniel_Castelao`. The GFX consumer at `interface/006_independence_wave_portraits_registry.gfx:149-152` points to `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`.

The portrait gate records a grounded source/archive and a byte-validated runtime DDS, but the author/scan-chain rights, date wording, lack of an independent rights reviewer, lack of provider/RunPod receipt, and the current `source_placeholder` versus older `styled_final` terminology are unresolved. The supplied Bóveda input is not mapped to a GLC consumer and must not be relabelled onto Castelao. No portrait file, GFX entry, character, fallback, or identity was changed by this audit.

The flag gate records the untouched vanilla GLC family as semantically Galician and engine-complete, while the actual democratic opening selects `GLC_democratic.tga`. Its period fit for a 1936 Event 006 opening and redistribution rights remain `needs_user_review`. No GLC mod flag, cosmetic tag, or country-specific flag GFX exists or was invented.

The five route installers and party keys are source-wired in `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:248-323,494-497`; the active route party and idea localisations remain in `localisation/english/006_independence_wave_iberian_l_english.yml:146-157`. No election, law, faction, guarantee, subject, or diplomacy defect requiring a local GLC patch was proven.

## Focus, decisions, ideas, assets, and localisation

The shared focus tree is assigned through the existing package framework. The read-only focus inspection found 184 focuses, 196 connectors, zero crossings, and zero node intersections. One long authored connector remains from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`; the only other warning was an unrelated vanilla continuous-focus localisation warning. No GLC-specific focus loader, prerequisite, icon, or localisation gap was found.

The GLC decision surface at `common/decisions/006_independence_wave_iberian_decisions.txt:205-397` includes the timed mission `independence_wave_glc_hold_council_together` and eleven decisions: `independence_wave_glc_secure_inland_depots`, `independence_wave_glc_integrate_coastal_guards`, `independence_wave_glc_reconcile_council_and_port`, `independence_wave_glc_settle_former_host_ledgers`, `independence_wave_glc_ratify_atlantic_charter`, `independence_wave_glc_convene_workers_port_council`, `independence_wave_glc_confirm_municipal_covenant`, `independence_wave_glc_establish_coastal_command`, `independence_wave_glc_accept_protected_customs_mandate`, `independence_wave_glc_codify_sovereignty`, and `independence_wave_glc_open_iberian_network`. Their package-local trigger/effect/localisation coverage is present.

The seven accepted ideas are `glc_contested_council`, `glc_atlantic_compact`, `glc_constitutional_charter`, `glc_workers_port_council`, `glc_municipal_atlantic_covenant`, `glc_coastal_security_command`, and `glc_protected_customs_mandate`; their allowed checks and cleanup are present. No icon or manifest patch was required.

The current worktree has a concurrent localisation diff removing two obsolete `GLC_independence_wave_alfonso_daniel_castelao` strings. This audit did not author, revert, stage, or rely on that concurrent edit; current source search finds no active Event 006 consumer for those obsolete strings. All active GLC package, party, idea, decision, mission, and tooltip keys remain present.

## Starting military, technology, industry, supply, AI, and playability

The accepted force mapping resolves IW-015 to p15 `territorial_defense` with the documented institutional officer commission and territorial/coastal role. The shared force loader requires a current-generation mapping, roster, reinforcement program, and package lifecycle before materializing the dynamic force. No additive army, navy, air wing, equipment, technology, production, research slot, supply, railway, port, or manpower change is source-correct within this bounded audit.

No GLC-specific technology tree or technology dependency is present. The read-only vanilla `infantry_weapons` technology inspect/render route timed out after 180 seconds for both requests, so no technology MCP acceptance claim is made. A standalone Technology Tree Viewer was not exposed in the installed tool inventory and could not be independently verified as available; this is recorded as a tooling gap rather than a package defect.

The GLC AI rows at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:867-901` cover territorial survival, former-host restraint, settled-port development, and emergency command with GLC/origin/setup guards. The direct read-only probability discovery for `ai_strategy_factor` on this source returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces` and zero candidates. The required routed `chaosx_ai_probability_auditor` is not callable in this runtime, so no typed scenario balance or probability receipt is claimed and no AI weights were changed.

## Formable, adapter, admission, and attestation boundary

FORM-07 remains bound to exact CAT state 165, NAV state 792, and GLC state 171. Its GLC member proof requires package `iw_015`, original tag `GLC`, setup/readiness, exact anchor ownership/control, route/member policy, and the independently guarded identity/flag/attestation contract. The current formable source deliberately remains fail-closed; this audit did not set any identity, flag, readiness, attestation, or promotion flag.

IW-015 remains outside central content attestation, automatic/scenario release capacity, and deterministic Join. No source patch was made to central registries, global vanilla overrides, attestation, origin, reservation, host survival, or pre-event gates.

## Read-only MCP evidence and limitations

- Event inspect of `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, with helper/lifecycle deferral and one workspace-scale blocking diagnostic. The lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eeb66681b9568658ee015638fba6e28360858104df2e5b19e03112a74699b51/4433437331be222dba4df3da25608c7855a59cab3a3e326e9abcee7ecf0d4d44/event-lint-4bccb6ec7fe1.json`.
- The matching event overview render returned `EVENT_RENDERED_PARTIAL` with layout hash `118888ec7d6771854b8f62f596ed4f25c9bbdcb117a9e47a91f177e7fec7a571`; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a42cd125593143fbef54a4925fe2580991103586ba01a7945280a55800838d14/bfd3fa80ef414b41fa3095794aad55d8c2a3b7baac121bea993634c761b4cd06/event-overview-4bccb6ec7fe1-manifest.json`.
- Focus inspect returned `FOCUS_INSPECTED` for `independence_wave_focus_tree` at revision `a62b4724125f17da1c1801a7fcd595310881a6be20383fe9eaa9933c0c0a5746`; the inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdc30f89331349afab947fb784e0e5777b3d31e16f0e5e2b11dc8486e669d372/945eede58d1851cc1d44c219062ca6ce63f30cc2eab1b36571f9b9fbb4ac06e5/focus-inspect.a62b4724125f17da.json`.
- Focus render returned `FOCUS_RENDERED` with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`; the read-only SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/febdb7cdc0279bc4bd153479733d6eb67210692dd0b3fda9a3e7c38faf0ada4d/independence_wave_focus_tree.focus.svg`.
- Map inspect of state `171` returned `MAP_INSPECTED` at revision `67b733118fb2f5e8692fc73ff7a8b34aaa0495877f770344b5d393ac78afbfe8`; selected-state membership, geometry, networks, and adjacencies passed, while workspace-wide position validation was false because unrelated aggregate diagnostics reported invalid buildings and floating-harbor positions. The map artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ee8d1e41172a2f2dbc61bde60688de486e9e433d9cd70a3ddf311a235801caa/26cecb4657f80fc07da4ae1144ffcb15edc445f9cf5d192fa321bde02fd0d8f2/map-inspect.67b733118fb2f5e8.json`.
- The read-only map state render returned `MAP_RENDERED` as an offline representation. No map rewrite was attempted and no state-specific map defect was proven.
- Direct probability inspection of `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with zero weighted candidates and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21227fdeebc145b9b78c80422abc82a2acc161571a002da3db3024fdeed057f3/213f9daa9f188da1a4840b62e8c400349175888388515ef51b37c656a6eedc4f/probability-inspect-b84ee2ca17f4.json`.
- Technology inspect/render for vanilla `infantry_weapons` each timed out after 180 seconds. No standalone Technology Tree Viewer was exposed, and no technology receipt is claimed.

These are read-only source-linked artifacts only. No live game, save/load, live country release, or user-consumer validation was performed or claimed.

## Validation

The following focused validators passed against the current worktree:

- `python -B .tools/audit_event6_allocator.py` passed and retained `IW015` in the adapter-only fail-closed set.
- `python -B .tools/audit_event6_country_api.py` passed with broad `242` unique tags, resolved `191` carriers, missing `0`, duplicates `0`, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` passed with `102` complete Event 006 flag families and `0` incomplete families.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and the recorded edge/publication checks.

No gameplay source patch, asset binary, tag, state id, leader id, party id, focus id, localisation key, formable id, admission flag, or attestation flag was changed by this audit. No commit or staging action was performed, and concurrent worktree edits were left intact.

## Blockers and promotion decision

1. GLC opening flag identity/period fit and redistribution rights remain a user-owned review gate even though the installed vanilla family is complete and identity-correct at carrier level.
2. Castelao portrait rights/provenance, provider receipt, independent review, and the `source_placeholder` versus older `styled_final` terminology conflict remain unresolved; Bóveda is not a valid substitute.
3. The mandatory `chaosx_ai_probability_auditor` route is unavailable, direct probability discovery found no weighted candidates, and no package-specific quantitative AI receipt is justified.
4. Technology MCP inspect/render timed out and no standalone Technology Tree Viewer was available; no technology acceptance claim is justified.
5. Event inspect/render and map inspect are workspace-partial or globally diagnostic-heavy, and no live/save-load proof exists.
6. Central content attestation, release capacity, deterministic Join, and FORM-07 identity/member promotion remain intentionally fail-closed.

Promotion receipt justified: **No**.

Source-correct local patch justified: **No**. The current package is source-wired for its bounded adapter role, and every remaining issue is an unresolved external evidence or central-gate decision rather than a safe GLC-owned source correction.
