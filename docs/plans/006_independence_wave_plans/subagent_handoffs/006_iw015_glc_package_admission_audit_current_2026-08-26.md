# IW-015 GLC package admission audit — current

Date: 2026-08-26.

Scope: bounded audit of IW-015 Galicia (`GLC`) only, including the registered-carrier contract, state 171 anchor, vanilla and Event 006 leader consumers, portrait and flag surfaces, force mapping, shared focus and decisions, AI strategy, cleanup, central attestation/preflight, capacity, and deterministic Join consumers.

## Admissibility verdict

IW-015 GLC remains **HOLD / FAIL-CLOSED** and must not be promoted to central content attestation, automatic capacity, scenario preflight, or deterministic Join.

The decisive blocker is the unresolved duplicate real-person identity contract: vanilla GLC already owns Alfonso Daniel Castelao as a country leader, while Event 006 statically recruits `GLC_independence_wave_alfonso_daniel_castelao` as a second corps commander with a separate portrait. The role split is explicit, but no owner-approved transfer/ownership policy or source-backed replacement packet makes two live Castelao consumers safe.

The package also lacks an independent package/rights review and a quantitative AI/probability evidence pass. The latest portrait handoff records the supplied GLC Castelao texture as a valid `styled_final` runtime match, but retains `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` rights and explicitly leaves the duplicate-identity admission gate open.

No central admission patch is safe from the current evidence.

## Country package coverage checklist

| Surface | Current result | Evidence and identifiers |
| --- | --- | --- |
| Carrier/tag | Source PASS, admission HOLD | IW-015 resolves to registered vanilla `GLC`; no mod country definition or history shell is expected. `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:16` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:16` bind `GLC`, state 171, and `RG-171`. |
| Vanilla country history | PASS as carrier source, identity gate open | Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\GLC - Galicia.txt:1,65-102` uses capital 171, democratic politics, and country leaders Fuco Gómez, Alfonso Daniel Castelao, Vicente Martínez Risco, and Santiago Casares Quiroga. |
| State/anchor | Source PASS, fresh targeted MCP receipt unresolved | Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\171-Galicia.txt:3,10-27` has state 171 owned by `SPR`, core `GLC`, capital candidate context, VPs, two dockyards, one arms factory, air base, and naval base. Package predicates require state 171 to be owned and controlled by the selected carrier and retain a protected former host. |
| Initialization | Source PASS, gated | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:52-69` requires exact IW-015 package/region/depth/archetype, event targets, state 171 ownership/control, protected former host, capital, and vanilla Fuco Gómez. |
| Politics/parties | Source PASS | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:484-492` sets democratic elections, GLC popularity constants, four GLC party names, and the council/port ledgers. Direct localisation is present at `localisation/english/006_independence_wave_iberian_l_english.yml:146-152`. |
| Leader and corps roster | **HOLD / blocking** | `history/general/006_independence_wave_character_recruitment_registry.txt:183-185` recruits `GLC_independence_wave_alfonso_daniel_castelao`; `common/characters/006_independence_wave_characters_registry.txt:262-279` defines it as male, `corps_commander`, with `GFX_portrait_GLC_alfonso_daniel_castelao`; `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:80-87` requires it alongside Fuco Gómez. Vanilla GLC independently creates Castelao at `GLC - Galicia.txt:84-89`. |
| Portrait | Runtime wiring PASS, rights/identity HOLD | `interface/006_independence_wave_portraits_registry.gfx:141-152` wires the stable GLC DDS sprite. `006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md:31-35,45-47,57,67-75,94-98` records byte-identical supplied/runtime DDS and valid framing, but unresolved source-rights caveat, no independent rights reviewer, and the duplicate Castelao consumer. |
| Flag | Vanilla reuse only; independent admission review open | The carrier reuses vanilla GLC flag assets (`GLC.tga`, ideology variants, medium, and small variants) under the installed game. No mod `GLC` flag override exists. Research requires proof that the registered base flag matches the released identity/origin before attestation; no separate current GLC flag/source admission packet was found. |
| Force/start setup | Source present, blocked by roster gate | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:16` maps IW-015 to p15 `territorial_defense`, 50 starting-force weight, territorial infantry/coastal guards, and institutional fallback if biographies remain unresolved. `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:511-512` loads/applies p15 only after `has_independence_wave_glc_command_roster`. |
| Technology | Vanilla inheritance only; evidence limitation | Vanilla GLC history supplies infantry, recon, support, engineers, mountaineers, artillery, anti-air, aircraft/naval tech, electronics/industry, and grand battleplan. No custom Event 006 technology tree exists. The installed MCP route reported no Technology Tree Viewer capability; a scan attempt timed out, so no technology acceptance claim is made. |
| Ideas/ledgers | Source PASS | `common/ideas/006_independence_wave_ideas_registry.txt:1606-1655` contains `glc_contested_council`, `glc_atlantic_compact`, `glc_constitutional_charter`, `glc_workers_port_council`, `glc_municipal_atlantic_covenant`, `glc_coastal_security_command`, and `glc_protected_customs_mandate`; direct names/descriptions are at `localisation/english/006_independence_wave_iberian_l_english.yml:179-192`. |
| Focus | Source/framework present; package admission still blocked | GLC setup assigns `independence_wave_focus_tree` through the full shared framework and enables constitutional, popular-council, traditional, emergency, patron, host, League, power-struggle, and formable hooks at `006_independence_wave_iberian_package_effects.txt:493-510`. Current focus geometry evidence is the shared-tree closure handoff, not GLC admission proof. |
| Decisions/mission | Source PASS, shared GUI only | `common/decisions/006_independence_wave_iberian_decisions.txt:205-397` defines the GLC founding category, mission `independence_wave_glc_hold_council_together`, and eleven project IDs through `independence_wave_glc_open_iberian_network`; direct names, descriptions, effect tooltips, and category text are present at `localisation/english/006_independence_wave_iberian_l_english.yml:97-131`. No dedicated GLC-owned scripted GUI exists. |
| AI | Source present, quantitative result unresolved | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:823-901` defines GLC territorial-survival, host-restraint, settled-port, and emergency-command profiles with exact `original_tag = GLC` and package/setup flags. The required probability inspection and named auditor pass did not complete; no weight change or balance conclusion is claimed. |
| Cleanup | Source PASS, not an admission waiver | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:594-628` removes the GLC mission/projects and ideas, clears ledgers/flags, and retires the additive Castelao character. Vanilla GLC history and its ruling roster remain intact. |
| Central adapter | Present | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` includes `iw_015` in the runtime adapter allowlist. |
| Central content attestation | **Absent by design** | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` lists the current attested package IDs and does not include `iw_015`. |
| Runtime/scenario preflight | Branch exists but is unreachable without attestation | Runtime preflight requires content attestation at `006_independence_wave_package_dispatch_triggers.txt:207-210`; the exact `iw_015`/`GLC` branch is only at `:388-390`. Scenario preflight likewise requires attestation at `:411-413` and has the exact IW-015 availability branch at `:558-560`. |
| Capacity/Join | **Not admitted** | `common/scripted_effects/006_independence_wave_join_effects.txt:213-247` probes the fixed attested Join order and contains no `iw_015`. The current allocator audit reports 40 adapters, 32 attested packages, 29 compatible groups, and IW-015 among the eight adapter-only fail-closed IDs. |

## Identity blocker and safe owner choices

The existing prior audit `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw015_glc_duplicate_identity_audit_2026-08-14.md` remains current in substance. Removing the additive recruitment leaves `has_independence_wave_glc_command_roster` unsatisfied, removing it from the trigger weakens the accepted force gate, retiring vanilla Castelao mutates authored carrier history, and inventing or renaming a replacement requires a new source/role/date/rights/portrait packet.

Before admission, the owner must select and document one of three bounded designs: guarded reuse/transfer of the vanilla Castelao identity with explicit country-leader-to-corps-command ownership and cleanup; a distinct source-backed Galician corps commander with independent date/role/rights/portrait evidence; or an intentional no-additive-commander design that rewrites the GLC roster and force-readiness contract together.

The latest portrait audit does not choose among these designs and does not authorize central attestation.

## MCP evidence and limits

- Fresh `hoi4.event_inspect` and `hoi4.event_render` attempts for selector `{ kind: event, eventId: chaosx.nr6.350 }` used bounded state-flow/state views and both timed out awaiting `tools/call` after 180 seconds. No fresh event artifact is claimed. The prior structural receipt remains useful: `006_iw015_glc_duplicate_identity_audit_2026-08-14.md` records the earlier partial trace/render artifacts for the same synchronous roster event, with zero selected blocking diagnostics but deferred helper/lifecycle projection.
- Fresh `hoi4.focus_inspect` and `hoi4.focus_render` attempts for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, stalled beyond the bounded wait and were terminated; no fresh artifact is claimed. The current shared-tree closure handoff records 184 focuses, 195 connectors, zero Event 006 crossings/intersections/long connectors/close-row pairs, and artifact-backed geometry evidence; this is not package admission evidence.
- The GLC consumer uses the shared `independence_wave_status_window`; it does not introduce a GLC-owned GUI. The current shared GUI audit records 48 inspected elements and a rendered artifact but workspace-wide blocking diagnostics/selected-scenario overlap warnings, so no GLC GUI acceptance claim is made.
- A targeted state-171 map inspection was not completed in this pass after the initial batched call was rejected because `refresh` is not accepted by the map schema. Vanilla state source evidence is recorded above; no current MCP map artifact or map-write claim is made.
- `hoi4.tech_inspect` scan timed out after 180 seconds. The installed package exposes no Technology Tree Viewer, so technology-tree acceptance remains unresolved rather than inferred from vanilla source.
- `hoi4.probability_inspect` first rejected `source.relativePath` as an invalid schema field; the corrected `source.path` attempt against `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` timed out after 180 seconds. The callable inventory exposes no `chaosx_ai_probability_auditor` route, so no scenario evaluation, sweep, compare, or balance conclusion is claimed.

## Static validation

The following current repository checks passed without changing source:

- `python -B .tools/audit_event6_country_api.py`: 242 broad unique tags, 191 resolved carriers, zero missing, zero duplicates.
- `python -B .tools/audit_event6_flags.py --strict`: 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attestations, 29 groups, eight adapter-only IDs including IW-015, and the 3/4/5/7/10 ladder.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and eight edge-case receipts passed.
- `python -B .tools/audit_event6_form16.py`: shared FORM-16 contract passed with fail-closed readiness predicates preserved; this is supporting shared evidence, not GLC admission proof.

These checks confirm the current boundary and do not waive the GLC identity, rights, independent package, AI/probability, or MCP evidence gates.

## Files changed and patch disposition

Only this handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw015_glc_package_admission_audit_current_2026-08-26.md`

No country, history, character, portrait, flag, force, idea, decision, focus, AI, event, attestation, preflight, capacity, Join, map, technology, localisation, or central-dispatch source file was changed.

No staging or commit was performed, per parent scope.

## Documentation drift to reconcile later

`docs/events/006_independence_wave/iberian_registered_packages.md:46-48` and the top of `docs/events/006_independence_wave/overview.md` retain older source-placeholder portrait wording, while `006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md` records only the NAV and GLC Castelao runtime outputs as supplied `styled_final` matches. This is documentation drift, not evidence for admission; the Castelao rights caveat and duplicate identity gate remain open.

## Remaining blockers and next discriminator

1. Approve one explicit Castelao identity/ownership design and provide its source-backed transfer or replacement packet.
2. Complete independent GLC country, flag, portrait-rights, and package review, retaining the current `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` rights status until resolved.
3. Supply named GLC AI scenarios and route the mandatory probability pass through `chaosx_ai_probability_auditor`; compare only after an owner-applied admission patch.
4. Obtain a bounded state-171 map receipt and any needed GUI/focus/event rerenders after the transport blockers clear.
5. Only after all gates pass, make one owner-controlled central change adding GLC to content attestation, scenario/runtime preflight parity, capacity, and deterministic Join, followed by same-scenario comparison and post-validation.

No fallback, identity invention, central admission widening, map write, live HOI4 run, save/load claim, or balance simplification was made.
