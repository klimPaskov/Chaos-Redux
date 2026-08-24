# Event 006 IW-031 Kosovo current-boundary crosswalk audit

Date: 2026-08-24.

Status: **CROSSWALK ASSERTION IMPLEMENTED / NO ADMISSION CHANGE**.

This handoff audits the current Event 006 country/package boundary for IW-031 Kosovo (`KOS`). It does not promote a package, widen the 32-package boundary, invent identity or territory, write the map, or change gameplay files.

## Finding and safe next implementation

IW-031 is already centrally content-attested and its package-local source contract is complete under the accepted vanilla-carrier design. The only concrete package-boundary gap found is a source-of-truth crosswalk mismatch: the canonical 206-entry candidate registry leaves `baseline_anchor_state_ids` empty for IW-031, while the canonical installed-map binding records the exact current anchor as state `802`.

The candidate row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:32`. It says that Kosovo has no unique state in the public 763-state baseline and must use a current-map Kosovo state. The installed-map binding is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:32`, which records `anchor_state_ids=802`, `compact_state_ids=802`, `anchor_state_names=Kosovo`, `initial_owner_by_state=802=YUG`, `binding_reason=The installed map has a unique Kosovo state`, `rebind_status=new_current_state_binding`, and `installed_state_history_files=802-Kosovo.txt`.

The package runtime already agrees with the installed binding. Vanilla `history/countries/KOS - Kosovo.txt` sets `capital = 802`, vanilla `common/country_tags/00_countries.txt:275` maps `KOS` to `countries/Kosovo.txt`, and `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt:47-78,118-177` checks state 802 for ownership, control, capital, and setup. The package effects identify the same contract at `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:2-4,263-315`.

The safe reconciliation is now implemented in `.tools/audit_event6_country_api.py`: it asserts `IW-031 -> KOS -> current-map state 802`, the exact `Kosovo` binding, `new_current_state_binding`, and `802-Kosovo.txt` while preserving the candidate matrix's public-baseline caveat. The candidate CSV remains unchanged; `802` is not mislabelled as a public-763-state baseline anchor.

This reconciliation must not alter `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, the 32-ID attestation OR-list, normal/scenario preflight, or any package effect. It does not justify adding an unattested package or changing reservation capacity.

A read-only CSV crosswalk check returned `{"package_id":"IW-031","tag":"KOS","candidate_baseline_anchor":"","installed_anchor":"802","installed_compact":"802","host":"802=YUG","binding":"new_current_state_binding","history":"802-Kosovo.txt"}`. This is the concrete mismatch to reconcile.

## Boundary authority

The current Event 006 boundary remains **HOLD / PARTIAL**: 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. The eight adapter-only fail-closed IDs remain IW-013/NAV, IW-015/GLC, IW-043/CHU, IW-058/ASY, IW-093/DOX, IW-098/SOK, IW-177/FIJ, and IW-179/FSM.

The admitted set remains IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184.

The source-of-truth rule is explicit: `docs/specs/006_independence_wave_specs/README.md:100` treats `006_candidate_country_registry.csv` as canonical for identity/tag representation and `006_current_installed_map_package_bindings.csv` as canonical for current anchors, hosts, and bindings. The mismatch is consequently metadata drift between two intentionally different authorities, not evidence that KOS needs a new country shell or a new state.

## Country-package coverage checklist

| Surface | IW-031 result | Evidence and remaining risk |
| --- | --- | --- |
| Tag registration | PASS | Vanilla `KOS` is reused. No mod `KOS` country or history overwrite exists, and `common/country_tags/006_independence_wave_countries.txt` does not duplicate the vanilla registration. |
| Current state and capital | PASS source-level / MCP revalidation blocked | Current binding and vanilla history agree on state/capital 802. A narrow current MCP allocation probe reported that state 802 exists in `game:history/states/802-Kosovo.txt`; a full state inspect timed out after 180 seconds, so no fresh ownership, province, supply, railway, port, resource, or adjacency receipt is claimed. |
| Host and collision safety | PASS source-level | The binding records `802=YUG`; exact package triggers require a dormant KOS carrier, a distinct living host, state-802 ownership/control, no active Event 006/Soviet origin, and no reservation collision. |
| Package setup/final/cleanup | PASS source-level | `independence_wave_setup_iw_031_kosovo`, exact IW-031 readiness, final validation, and generation-safe cleanup are wired in `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:263-371` and `common/scripted_triggers/006_independence_wave_kosovo_package_triggers.txt:118-185`. Central setup/final/cleanup dispatch is present at `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:26,58,104`. |
| Politics and parties | PASS source-level | Four guarded government routes set route-specific party names, popularity, leader, cosmetic tag, route idea, and lifecycle flags in `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt:136-202`. |
| Leaders and portraits | PASS with accepted source-placeholder policy | The three male character consumers are `KOS_independence_wave_ferhat_draga`, `KOS_independence_wave_miladin_popovic`, and `KOS_independence_wave_shaban_polluzha` in `common/characters/006_independence_wave_characters_registry.txt:432-478`. Dedicated GFX and DDS wiring is in `interface/006_independence_wave_iw031_kosovo_portraits.gfx:1-16` and `gfx/leaders/006_independence_wave/portrait_KOS_independence_wave_*.dds`. The source-placeholder workflow, provenance caveats, and absence of advisor/high-command/dossier/small portraits are documented in `docs/events/006_independence_wave/kosovo_package.md`. User-supplied HOI4-style finals and live portrait review remain separate gates. |
| Flags and cosmetics | PASS source-level | Vanilla KOS flags remain untouched. Route cosmetic tags and native TGA ladders are documented in `docs/events/006_independence_wave/kosovo_package.md`; the strict Event 006 flag audit found 102 registered tags and 102 complete families. No new flag or identity is justified by this crosswalk gap. |
| Shared focus | PASS source-level / MCP revalidation blocked | The shared `independence_wave_focus_tree` is defined at `common/national_focus/006_independence_wave_focus.txt:34-93`; KOS hook calls are present at `:114`, `:167`, `:201`, `:1444`, and `:1715`. The package intentionally has no separate KOS tree. Current focus inspect/render calls could not complete because the MCP transport closed after the earlier map timeout; the prior KOS audit's source-linked artifacts remain dated evidence only. |
| Decisions and mission | PASS source-level | `common/decisions/006_independence_wave_kosovo_decisions.txt:10-146` defines the founding mission and ten paid projects with visibility, cost, lock, cancellation, failure, and route consumers. |
| Ideas and lifecycle | PASS source-level | Six KOS-only ideas are registered at `common/ideas/006_independence_wave_ideas_registry.txt:2946-3009` and are removed/reapplied by the package lifecycle effects. |
| Force and starting setup | PASS source-level / live map unclaimed | IW-031 uses p31 `mountain_frontier`, military tradition 55, reinforcement mask 1047, five guarded reinforcement paths, and no navy/air inheritance. The current package authority is `docs/events/006_independence_wave/kosovo_package.md`; no force or equipment change is proposed. |
| Technology | Vanilla inheritance only | IW-031 uses vanilla KOS starting technology and has no custom technology tree. The installed package exposes no Technology Tree Viewer, so no technology-tree MCP proof is available. |
| AI and playability | PASS source-level / quantitative balance unclaimed | Four KOS strategy blocks are in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1625-1672`. The required named `chaosx_ai_probability_auditor` route is not callable in the installed tools; the direct probability route also lost MCP transport, so no quantitative AI balance claim is made. |
| Localisation | PASS source-level | Party, route, idea, decision, mission, and cosmetic keys are in `localisation/english/006_independence_wave_kosovo_l_english.yml:2-109`; character keys are in `006_independence_wave_kosovo_portraits_l_english.yml`. The prior package audit records 129 scoped keys with no missing/duplicate result. |
| Advisors and high command | Intentionally absent | No Event 006 advisor icon or unresearched advisor consumer is authorized for IW-031. The military consumer is the sourced male Polluzha corps-command role, not an advisor fallback. |

## Central loader and boundary checklist

The adapter registry includes IW-031 at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:40`. The content-attestation OR-list includes it at `:176`. Normal preflight and scenario preflight use exact KOS/state-802 branches at `:274-278` and `:493-495`. Shared setup/final/cleanup dispatch calls the Kosovo package at `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:26,58,104`.

The central final-validation barrier also requires the shared generic focus contract and `independence_wave_generic_ai_profile` before a selected package can pass. IW-031's package setup sets its KOS AI profile and focus framework flags through the package effects and triggers, so no loader omission was found.

No package-local implementation is missing at the gameplay boundary. The one actionable gap is the stale/ambiguous candidate-to-installed-map anchor crosswalk described above. Do not promote any of the 161 unattested rows on the strength of this finding.

## MCP inspection and rendering evidence

The required read-only map route was attempted for the exact KOS anchor. `hoi4.map_inspect` with `allocationRequests=[{kind=state,requestedId=802}]` returned `MAP_STATE_ID_COLLISION` and named `game:history/states/802-Kosovo.txt` as the scanned source, confirming presence but not supplying a full artifact. A direct `stateIds=[802]` inspect timed out awaiting the tool after 180 seconds. A state-layer `hoi4.map_render` attempt with coastlines, ports, and victory points also timed out after 180 seconds. No map write was attempted.

The required shared-focus inspect/render route was attempted for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree`. Both calls failed after the map timeout with `Transport closed`. The event inspect route for `events/006_independence_wave.txt`, the technology inspect route, and the direct probability inspect route for `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` then returned the same exact `Transport closed` blocker. These failures are recorded as MCP limitations, not replaced by source-only claims.

A dated prior IW-031 audit contains useful source-linked MCP artifacts but is not a fresh 2026-08-24 acceptance receipt. Its map inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/286ee35dbe3ec95070a7eea2401af12b3702b3d35100c12bde1c767bee071fdc/8af525193b54595d2a93cbf4d7e14b4bff63dd5f3b3c79d2c7d66f1f21fe2981/map-inspect.8314b98d43d3319f.json`, and its map render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd8b53eb2549add50b207cbe2fd618aafa44f6729a7363de31f02dba24b7b466/d8f3f68dad06593fd6e38b631d7b7f488ea3febc56f96e3126b684197e58df86/map-state.png`. The focus inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29586b3c82fa6f54b6e0fb8bc7eb39c7bd69a129727d373a052c6385fdcb340b/5434ac8eaf22514fe9687c0c0dd9ddec03b4c9b4904aff0ce63066a14afae014/focus-inspect.2a7873965b683aa3.json`, and its focus render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb40f2bfb9a1333fa26ada4991a5b0b787d21d4fe3ea999e62e0b7cdbd3c5ec6/3072be04a409bc053ab660cc363c81a2085da53433407019780d5f573dd13f09/independence_wave_focus_tree.focus.html`. The event inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0eaaeb3f297daa31e0be0bb1eaedecf798e7bf52b113a2cc0a4f2ce6dd4e3f86/f71ea9f99c4552d11deac1120127efa4a5f8ee174057309285ad2bca3fe84853/event-lint-7e8e9a563058.json`. Prior decision, mission, and focus probability source-inspect artifacts are recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw031_kosovo_country_package_final_audit_2026_08_10.md`. These artifacts support the existing package handoff only and do not close the current MCP revalidation failure.

No Technology Tree Viewer is installed. No technology viewer evidence was substituted.

## Maintained validation

The current maintained validators were run read-only from the repository root:

- `python -B .tools/audit_event6_allocator.py` — PASS: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attestations, 29 compatible groups, 20-package static witness, automatic ladder 3/4/5/7/10, and no retired pre-event crisis surface.
- `python -B .tools/audit_event6_country_api.py` — PASS: 242 broad rows, 191 resolved carriers, 34 Soviet rows, 45 Africa rows, zero missing and zero duplicate rows.
- `python -B .tools/audit_event6_flags.py --strict` — PASS: 102 registered Event 006 tags, 102 complete flag families, zero incomplete families.
- `python -B .tools/audit_event6_scenario_matrix.py` — PASS: all 32 SCN-008 mode/intensity cells and eight edge cases.
- `python -B .tools/audit_event6_form16.py` — PASS: ARM/GEO/AZR exact anchors 230/231/229, consent/refusal, identity/territory/integration/generation gates, rollback, cleanup, and readiness witnesses.
- `python -B .tools/audit_event6_gui_matrix.py` — PASS: five Statehood Ledger tabs, recognition/dependency/league/formable frame groups, generation cleanup, and four static/animated sprite pairs. This is a semantic source matrix, not runtime render/click/save-load proof.

The country API validator now tests the candidate-registry-to-current-map crosswalk and reports `IW-031-crosswalk=pass`. The remaining safe validation is to rerun all six maintained commands and retry a narrow `hoi4.map_inspect` for state 802 when the MCP transport is available. No map rewrite or live HOI4 run is authorized by this handoff.

## Uncertainty, omissions, and remaining risks

- The KOS package gameplay surface is source-complete under the existing accepted contract; the current finding is a metadata crosswalk gap, not a missing runtime adapter or country implementation.
- The candidate registry's blank anchor remains intentional under its public-763-state wording; the validator now ties it to the exact current-map binding without changing the matrix semantics.
- Current map ownership, controller, province, supply, railway, port, resource, building, and adjacency evidence is not freshly closed because the MCP inspect/render calls timed out.
- Current focus, event, technology, and probability MCP routes are not freshly closed because the installed MCP transport closed. The named `chaosx_ai_probability_auditor` route is unavailable, and no probability comparison is claimed.
- Grounded portraits remain source placeholders under the accepted workflow, with final user-supplied HOI4-style replacement and rights review remaining separate gates.
- The whole Event 006 system remains HOLD/PARTIAL. No package promotion, identity redesign, rights inference, formable promotion, map write, or balance change follows from this audit.

## Files changed by this audit

This handoff and the country API validator were changed:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw031_kosovo_current_boundary_crosswalk_audit_2026-08-24.md`

`.tools/audit_event6_country_api.py`

No gameplay, localisation, country, history, map, focus, decision, idea, AI, portrait, flag, dispatch, loader, reservation, or admission registry file was changed by this reconciliation. The previous handoff commit was `fd5ffc3ec`; this follow-up is intentionally kept as a separate parent-owned validator tranche because all agents share this branch.

## Parent action

Keep IW-031 admitted as `KOS`/state `802` and keep all other admission gates unchanged. The parent-owned validator assertion is complete; rerun the six maintained validators and obtain a fresh MCP map inspect/render before making any package-boundary or live-runtime claim.
