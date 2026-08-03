# IW-030 Montenegro current package-gate audit

Date: 2026-08-03 (Europe/Kyiv).

Authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v105_2026_08_03.md`, the current IW-030 re-audit at `006_iw030_montenegro_package_reaudit_current_2026_08_03.md`, and the current source-admission and Jovanović portrait handoffs. Obsolete pasted flag-log reports were not used.

Scope: static country-package audit after the current IW-030 visual portrait pass. The review covers MNT tag reuse, state 105, dispatch and attestation gates, setup/lifecycle, native roster, politics, leaders, portraits, flags, advisors, parties, focus loading, decisions, ideas, force mapping, technology, industry, supply, AI, localisation, cleanup, and documentation. No Hearts of Iron IV process or live scenario was launched.

## Disposition

IW-030 Montenegro remains **HOLD / fail-closed**. The package has a coherent dormant carrier and no independently proven gameplay defect. Portrait and identity gates remain open, so no attestation, runtime promotion, DDS, `.gfx`, generic portrait, relabel, copied history/OOB, flag replacement, advisor art, or fallback is authorized.

One narrow documentation drift was fully evidenced and corrected in `docs/events/006_independence_wave/montenegro_package.md`: the doc now reflects that vanilla MNT history recruits the three characters and that `chaosx.nr6.350` is only a shared checkpoint, and it no longer calls the closed shared-focus geometry a current MNT blocker. Runtime behavior is unchanged.

## Country-package coverage checklist

| Surface | Current evidence | Verdict |
| --- | --- | --- |
| Tag and identity | Vanilla `common/country_tags/00_countries.txt:99` maps `MNT` to `countries/Montenegro.txt`; the mod adds no MNT definition, custom history, or duplicate tag. Registry/constants keep MNT in the registered-reuse and Balkans/Danube sets. | PASS structurally; HOLD admission. |
| Anchor and map | Vanilla `history/states/105-Montenegro.txt` is the MNT/YUG state-105 anchor with cores, capital path, VPs `9809`/`9821`, two naval bases, infrastructure 2, one civilian factory, chromium 20, aluminium 70, manpower 895500, and local supplies 3.0. IW-030 reserves only state 105 under `RG-105`. | PASS static; ownership/control transfer, host survival, and save/load remain unobserved. |
| Dormant planner and preflight | `can_plan_independence_wave_package_iw_030` uses the exact MNT/state-105/`RG-105` proof. Normal and SCN-008 branches remain candidate-scoped and require `exists = no`. | PASS as a fail-closed candidate proof. |
| Runtime adapter and attestation | The adapter trigger includes `iw_030` (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:6-40`), while `has_independence_wave_runtime_package_content_attestation_for_execution_id` (`:73-90`) intentionally omits it. Both normal and scenario preflight call the outer attestation before the MNT candidate branch (`:95-159`, `:211-269`). | HOLD / blocking and correctly fail-closed. |
| Setup/lifecycle | `independence_wave_setup_iw_030_montenegro` (`common/scripted_effects/006_independence_wave_montenegro_package_effects.txt:279-316`) establishes laws, politics, ledgers, full shared focus assignment, routes, host/ambition/League state, dynamic force mapping, and AI profile. | PASS source contract; runtime timing and persistence unobserved. |
| Native roster | Vanilla `history/countries/MNT - Montenegro.txt:88-90` recruits `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic`; vanilla `common/characters/MNT.txt` defines all three as male, with Jovanović and Đukanović corps-command roles. Current `events/006_independence_wave.txt:166-187` has no MNT recruitment branch; `chaosx.nr6.350` is a shared TRA checkpoint. | PASS by vanilla reuse; no MNT gameplay patch needed. |
| Politics and parties | `independence_wave_initialize_mnt_politics` and the four route effects use central constants and package-local party names, laws, and popularity ladders. | PASS source coverage; route probabilities and live balance untested. |
| Leaders and portraits | Popović uses generic `GFX_portrait_europe_generic_land_19` and remains `BLOCKED_PROVENANCE`. Jovanović’s Znaci 8889 repaint passes visual identity/style but remains `NEEDS_USER_REVIEW` for rights/provenance. Đukanović remains rights/provenance review-pending. Martinović is a distinct role-correct identity candidate under `MNT_mitar_martinovic`, with v91 style/ownership/runtime review still open. All candidates are male; no opposite-gender metadata or name-pool pairing is present. | HOLD / blocking. Do not relabel a face or promote evidence-only candidates. |
| Flags and cosmetic identity | No mod-side MNT flag exists. Vanilla `MNT.tga`, `MNT_communism.tga`, `MNT_fascism.tga`, and `MNT_neutrality.tga` remain the intentional carrier flags. `MNT_AUS_danubian_state` in `common/countries/cosmetic.txt` is unrelated. | PASS by vanilla reuse. |
| Advisors and high command | No MNT-specific advisor/high-command role or icon is referenced by the package. | PASS by intentional absence; no advisor art is authorized. |
| Focus loading | Setup assigns `independence_wave_focus_assignment.full_framework` and `independence_wave_focus_tree`. v105’s current normal-spacing inspection reports 184 nodes and 192 connectors with zero Event 006 geometry failures; the isolated independent-command warning is intentional. | PASS source/geometry; no local MNT focus patch justified. |
| Decisions and mission | `common/decisions/006_independence_wave_montenegro_decisions.txt` provides the 420-day founding mission and ten costed projects with capital-control, one-active-project, cancellation, failure, and AI guards. | PASS source coverage; live timing, recovery, and balance untested. |
| Ideas and lifecycle | `common/ideas/006_independence_wave_montenegro_ideas.txt` defines the divided/mature compact and four route ideas; setup, route swaps, failure, and cleanup are package-owned. Shared Event 006 icons are the accepted asset boundary. | PASS source coverage. |
| Force and military identity | `006_force_package_mapping.csv:31` maps IW-030 to `mountain_frontier`, tradition 62, p30, five reinforcement paths, and no inherited navy/air. Constants resolve p30 to profile 4, tradition 62, reinforcement mask 647, inheritance mask 0, and research-sensitive flag 0. | PASS static mapping; dynamic force materialization, templates, stockpiles, manpower, and supply unobserved. |
| Technology and industry | Vanilla MNT history supplies three research slots, period-safe starting technology, and state-105 industry/resources. No mod-side MNT history or OOB is copied. The installed package exposes no Technology Tree Viewer. | PASS static reuse; technology-tree artifact unavailable as a tooling limitation. |
| AI and playability | `common/ai_strategy/006_independence_wave_montenegro.txt` supplies mountain-survival, former-host restraint, settled-frontier, and emergency-guard plans with central constants. | PASS source coverage; no live route, production, survival, or probability sweep. |
| Localisation | `localisation/english/006_independence_wave_montenegro_l_english.yml` has 61 package keys and begins with UTF-8 BOM bytes `239,187,191`; package party, idea, category, mission, decision, and tooltip keys are present. | PASS bounded source/encoding scan. |
| Cleanup and release | `independence_wave_cleanup_iw_030_montenegro` removes the mission, ten decisions, six ideas, ledgers, route/lifecycle flags, and AI state. The shared dispatcher calls setup, final validation, and cleanup. | PASS source cleanup; executable release and save/load unobserved. |

## File-surface checklist

- `common/script_constants/006_independence_wave_montenegro_constants.txt`: MNT politics, pressure, duration, and AI tuning tables.
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`: MNT identity, roster, setup, force, focus, AI, and runtime-readiness proofs.
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`: setup, politics/routes, decisions/focus rewards, final validation, and cleanup.
- `common/decisions/categories/006_independence_wave_montenegro_categories.txt`: MNT decision category registration.
- `common/decisions/006_independence_wave_montenegro_decisions.txt`: founding mission and ten project IDs.
- `common/ideas/006_independence_wave_montenegro_ideas.txt`: six MNT lifecycle/route ideas.
- `common/ai_strategy/006_independence_wave_montenegro.txt`: four MNT AI strategy IDs.
- `localisation/english/006_independence_wave_montenegro_l_english.yml`: 61 package-localisation keys.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`: central adapter, preflight, attestation, final-validation, and cleanup gates.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt`: planner, state-105 reservation, former-host pointer, and `RG-105` binding.
- Vanilla references: `common/country_tags/00_countries.txt`, `common/countries/Montenegro.txt`, `history/countries/MNT - Montenegro.txt`, `history/states/105-Montenegro.txt`, and `common/characters/MNT.txt`.
- Documentation authority: `docs/events/006_independence_wave/montenegro_package.md`, current v105 evidence, current package re-audit, source-admission handoff, and Jovanović repaint handoff.

## Missing or stale surfaces

- IW-030 is intentionally absent from the compile-time content-attestation list and therefore from normal and SCN-008 admission. This is a deliberate blocker, not a repair target.
- The current `events/006_independence_wave.txt` has no MNT recruitment branch because vanilla MNT history already recruits the native roster. Older handoff prose that called `chaosx.nr6.350` an MNT recruitment branch was stale; the MNT package doc is corrected by this tranche.
- `docs/events/006_independence_wave/overview.md` still uses broad “synchronous vanilla roster handoff” wording in historical/current overview paragraphs; parent documentation ownership should reconcile that wording if a single-event overview is being refreshed. It does not change runtime behavior or admission.
- No MNT portrait DDS, `.gfx` sprite, character amendment, advisor asset, flag edit, or runtime archive reference is missing from the current fail-closed state; creating any of these before rights/identity admission would be unsafe.
- The installed package has no Technology Tree Viewer, so a technology render remains unresolved.

## Map/state, politics, leaders, assets, and playability findings

No static state-105 map defect was found in the current authority artifact. Remaining map risks are runtime release ownership/control, capital reassignment, former-host protected-state relation, and save/load persistence.

Politics, parties, route ideas, and cleanup are internally coherent and use central constants. The package does not add a new tag, formable family, flag, advisor, or history/OOB copy.

Portrait gates remain fail-closed: Jovanović visual/style PASS with rights review, Đukanović rights review, Popović provenance block, and Martinović distinct-identity candidate pending human style/ownership/runtime review. No generic or opposite-gender pairing is introduced.

Starting-force static mapping is complete, but installed vanilla lacks `history/units/MNT_1936.txt`; dynamic p30 force application is therefore the only bounded Event 006 path and still needs parent-owned runtime evidence for templates, equipment, manpower, supply, industry, and research effects.

AI strategy source is present but cannot support a playability or balance claim without the parent-owned scenario pass across all four governments, founding mission, project failures/recovery, former-host restraint, and corridor route.

## Changed files and behavior

- Changed `docs/events/006_independence_wave/montenegro_package.md` only: corrected the roster source from an alleged MNT event branch to vanilla MNT history and removed the stale shared-focus admission blocker. No runtime identifiers changed.
- Added this handoff at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_current_package_gate_audit_2026_08_03.md`.
- Changed tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, gameplay effects, portraits, flags, sprites, or attestation lists: none.
- Before/after behavior: no gameplay behavior changes; documentation now matches the current source and v105 focus/portrait gate status.

## Meaningful validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 14 attested packages, and 13 compatible reservation groups.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 mode/intensity cells and eight edge cases.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- Static source scans confirmed the MNT adapter/final-validation/cleanup identifiers, native vanilla roster recruitment lines, no MNT branch in the shared checkpoint event, intentional IW-030 omission from content attestation, and no mod-side MNT portrait/flag runtime files.
- The MNT localisation source scan confirmed 61 keys and UTF-8 BOM bytes `239,187,191`.

Skipped meaningful validation: no game launch, live release, AI run, force materialization, production/supply observation, route probability sweep, save/load, portrait promotion, DDS/GFX conversion, attestation promotion, map write, or technology-tree render. The repository boundary assigns live consumer validation to the parent/user, the current visual handoffs keep rights and identity review open, and no Technology Tree Viewer is installed.

## Remaining admission risks and next gates

1. Resolve rights/ownership for Jovanović and Đukanović and complete the full non-generic male roster.
2. Admit a role-correct replacement for Popović only under an explicit identity such as `MNT_mitar_martinovic`; never relabel another face as `MNT_kristo_popovic`.
3. For every admitted portrait, complete source attribution, crop proof, independent identity/style/provenance review, rights sign-off, DDS conversion, and parent-owned `.gfx`/character wiring.
4. Only after those gates, add `constant:independence_wave_package_id.iw_030` to the content-attestation list and rerun normal/SCN-008 preflight and capacity evidence.
5. Exercise the MNT event branch, p30 force loader, state/host relation, cleanup, save/load, AI, and balance in a bounded parent-owned runtime scenario.

No simplification or fallback was introduced. IW-030 remains incomplete and fail-closed.
