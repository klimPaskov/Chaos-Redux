# IW-017 Corsica post-wire country-package audit

Date: 2026-07-22  
Scope owner: `chaosx_country_package_auditor`  
Package: `IW-017` / `COR` / Corsica  
Reservation group: `RG-1`  
Inspected baseline: portrait wiring commit `787283cee`; latest tree observed before this handoff `7ecd76c6d`  
Audit mode: bounded static post-wire audit; no gameplay or map write

## Verdict

- **Country-package coverage: PASS.** The canonical Corsica package is internally coherent for the Event 006 admission and execution surfaces inspected below.
- **Portrait provenance and runtime wiring: PASS.** The two approved sourced portraits are the only portrait-bearing COR roles, are male-role compatible, and the runtime DDS payloads are pixel-identical to the approved processed PNGs.
- **Runtime/compile-time admission: CLOSED (not attested).** No live campaign, game compile, or MCP runtime attestation was run. Event 006 must remain fail-closed until the parent performs the authorized end-to-end admission check; this handoff is not a content attestation.

## Country-package coverage checklist

| Surface | Status | Evidence |
| --- | --- | --- |
| Tag, origin, and registry | PASS | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` and package bindings register `IW-017` as reusable tag `COR`, origin Corsica, automatic-pool-ready when not living. `common/scripted_triggers/006_independence_wave_package_triggers.txt:is_independence_wave_exact_package_iw_017_tag_available` requires `original_tag = COR` and the normal candidate/origin gates. |
| Anchor, host, and map reservation | PASS (static) | `RG-1` reserves anchor state `1` (Corsica) only; package bindings identify former host `FRA` and protect FRA capital state `16` while retaining a host remnant. `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt` enforce the reservation. No map write was made. |
| Setup and admission guards | PASS (static) | `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:can_initialize_independence_wave_iw_017_package` checks the exact package, generic-focus starting condition, state/host targets, capital `1`, region/depth/archetype and setup transaction. The prepared trigger requires the roster, baseline laws, full Event 006 focus assignment, route families, power struggle, force profile, AI/lifecycle, founding incident, and crisis/mature idea state. |
| Character roster and role ownership | PASS | `common/characters/006_independence_wave_mediterranean_characters.txt` contains the four current COR records: `COR_corsican_municipal_congress` (Landry civic leader), `COR_jean_chiappe` (Chiappe emergency/security leader and corps commander), `COR_paolo_pietri` advisor, and `COR_antone_rocchi` advisor. Recruit/promote/retire effects and the exact roster trigger use these same IDs. No live `COR_pasquale_venturi` record remains. |
| Portrait-bearing roles and assets | PASS | Only Landry and Chiappe have portraits. Both records are explicitly `gender = male`; Chiappe's civilian and army slots reuse one large portrait. Pietri and Rocchi have no portrait blocks. There are no COR `small` or advisor portrait consumers. `interface/006_independence_wave_mediterranean_portraits.gfx` defines exactly the two stable sprites. |
| Portrait source/provenance and DDS conversion | PASS | Approved processed PNGs: `COR_adolphe_landry.png` SHA256 `a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505`; `COR_jean_chiappe.png` SHA256 `ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45`. Runtime DDS SHA256s: Landry `42efd44de267e2802b697a2b98398fff0087985db5d0f5764efa58ddd305ea97`; Chiappe `561bc156566135f6ae27c010f63ec8952664ab637ec07d95cdcc44cb4c362c14`. Both are 156x210, legacy 32-bit BGRA DDS (`pitch 624`, masks `32/16711680/65280/255`, opaque alpha) and direct decoded payloads are pixel-identical to the approved PNGs. Sources and public-domain ownership are documented in `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/corsica_trial_01/`. |
| Politics, leaders, and parties | PASS (static) | COR's vanilla country shell remains the registered tag identity. Landry's civic/oligarchic records and Chiappe's despotism record are wired to current characters; baseline laws/popularity are set by the package setup, with route changes handled by package effects. No opposite-gender portrait/name pairing or invented live leader reference was found. |
| Focus tree | PASS (static) | `common/national_focus/006_independence_wave_focus.txt` loads `independence_wave_focus_tree` and contains the five COR extension focuses: `independence_wave_cor_reopen_ajaccio_customs_focus`, `...secure_mountain_post_road_focus`, `...register_coastal_communes_focus`, `...settle_french_maritime_accounts_focus`, and `...authorize_form05_delegation_focus`. Prerequisites, package gates, reward hooks, icons, localisations, and AI hooks resolve. |
| Decisions and mission | PASS (static) | `common/decisions/006_independence_wave_mediterranean_decisions.txt` and its category define the founding mission `independence_wave_cor_hold_island_supply_together` plus the eight COR administrative/security/maritime decisions. Exact package, capital, route, active-project, cancellation, timeout, cost, tooltip, and AI gates resolve. |
| Ideas and lifecycle | PASS (static) | `common/ideas/006_independence_wave_mediterranean_ideas.txt` defines `cor_exposed_island_supply`, `cor_civic_coastal_compact`, and the constitutional/mountain/guard/patron route ideas. Setup, route replacement, and cleanup effects remove/reapply the expected lifecycle ideas; corresponding icon definitions and textures exist. |
| Event/founding/route integration | PASS (static) | `events/006_independence_wave_mediterranean.txt` uses namespace `chaosx.nr6`; COR founding event `chaosx.nr6.21` and route event `chaosx.nr6.24` are scheduled by the Mediterranean package effects and guarded by exact package/setup/resolution flags. Localisation references resolve. |
| Form05 and diplomacy | PASS (static) | `common/scripted_triggers/006_independence_wave_form05_triggers.txt` and `common/scripted_effects/006_independence_wave_form05_effects.txt` use the exact COR/package/anchor/member gates. The Form05 effects preserve sovereign records without annexing countries, transferring states, granting cores, or replacing COR. |
| Military, technology, industry, supply | PASS (static) | The package's dynamic force mapping identifies `IW-017` as `coastal_maritime`, tradition `53`, navy inheritance enabled, air inheritance disabled, with mountain/coastal infantry reinforcement. Starting technologies, research slots, industry, ports, infrastructure, and naval baseline come from the registered vanilla COR shell; no unsupported custom technology surface was introduced. |
| AI and playability | PASS (static) | `common/ai_strategy/006_independence_wave_mediterranean.txt` provides exact-COR island survival, founding restraint, host threat, civic maritime policy, and island guard strategies. Focus and decision AI weights align with maritime instability, host pressure, and route progression. No broad world-iteration action was introduced. |
| Cleanup and release safety | PASS (static) | `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt` removes the mission, decisions, ideas, package variables/flags, focus assignment, and all four COR characters. Shared generation reset clears force/focus/decision/live registries; host release masks/restores cores and keeps protected host state rules. |
| Localisation and asset surfaces | PASS (static) | COR leader, advisor, idea, focus, decision, mission, AI and event keys resolve in `localisation/english/006_independence_wave_mediterranean_l_english.yml`; focus/decision/idea icon definitions and referenced textures exist. The asset manifest and per-trial handoff still describe the pre-audit pending state and should be promoted by the parent/source-of-truth update. |

## Validation evidence

Meaningful checks already run for this audit:

- `python .tools/audit_event6_allocator.py`: allocator and scenario bands passed (149 publishers, 126 automatic/high-chaos selectable, 138 SCN-008 ranked; automatic counts 3/4/5/7/10 and joint ordering valid).
- Focus, decision, event, and COR localisation reference parsing found no missing player-facing keys.
- Focus/decision/idea icon and texture existence checks passed.
- Direct DDS header, dimensions, masks, alpha, SHA256, and decoded-pixel comparison passed for both approved COR portraits.
- Focused live-source search found no active old COR leader ID, `_small` sprite, advisor portrait, or competing active portrait consumer.

Meaningful checks intentionally skipped:

- No live game/campaign execution, compile-time content attestation, or end-to-end allocator admission was performed. The parent must keep the runtime gate closed until that authorized check is completed.
- No map rewrite was performed; this audit only reviewed the declared state/host reservation and release surfaces.
- No technology-tree MCP viewer is installed/exposed in this environment; the registered vanilla COR technology baseline was reviewed from source instead.

## Remaining risks and blockers

1. Event 006 admission remains intentionally fail-closed pending the parent's authorized runtime/compile-time attestation. This handoff does not set `independence_wave_form05_readiness_attested` or any other readiness flag.
2. The shared Form05 readiness flag must be earned through the in-game route; it must not be manually asserted as part of package setup.
3. State-1 ownership/control, former-host transaction, protected FRA capital/remnant, current-generation, force-mapping, route, and cleanup checks still require runtime confirmation.
4. `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/corsica_trial_01/manifest.md` and `gfx_handoff.md` retain their pre-wire `approved_converted_pending_postwire_country_audit` wording. The parent/source-of-truth documentation pass should update those statuses and the aggregate asset manifest to reference this PASS handoff.

## Simplifications and omissions

No gameplay simplification, fallback country identity, new map reservation, new focus route, or unapproved asset was introduced by this audit. The only file changed by this subagent is this documentation handoff; no gameplay patch is required by the findings.

