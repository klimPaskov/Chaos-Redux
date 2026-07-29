# Event 006 focus framework and overlay audit — 2026-07-29

## Scope and verdict

This is a read-only audit of the Event 006 full focus framework, shared-focus sources, regional/package overlays, route locks, rewards, icons, localisation, AI weights, existing-tree preservation, and current focus-carrier evidence. No gameplay, focus, icon, localisation, AI, or scripted-effect source file was patched; this handoff is documentation-only.

**Verdict: HOLD / PARTIAL.** The authored source contains the required lane families and package/shared branches, but the central layout remains validator-blocked and the additive carrier contract is only statically proven for the Event 006 full tree and the reviewed Iceland carrier. Route-family reachability, package admission, focus-order AI, and post-formation live behavior remain unproved.

Authoritative design references were `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`, `...part_5_country_packages_and_regional_overlays.md`, `...part_6_formables_league_and_scenario.md`, and `...part_7_ai_balance_assets_and_acceptance.md`. The current completion boundary remains the 2026-07-28 whole-event re-audit and the current resume/source-of-truth packets; this handoff does not promote any package or runtime result.

## Current source inventory

| Source | Regular `focus` blocks | `shared_focus` blocks | Focus/shared IDs | Current use |
| --- | ---: | ---: | ---: | --- |
| `common/national_focus/006_independence_wave_focus.txt` | 184 | 17 | 201 | Full Event 006 tree, generic overlay, ICE consumers, COR extension, and package modules. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | 0 | 48 | 48 | IW-043 Volga/Ural and IW-058 Mesopotamian signature branches. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | 0 | 43 | 43 | IW-093 Asante and IW-098 Sokoto signature branches. |
| `common/national_focus/006_independence_wave_pacific_focus.txt` | 0 | 20 | 20 | HBX, HAW, and FIJ Pacific branches. |
| **Total** | **184** | **128** | **312** | All IDs were unique in the balanced-block scan. |

The full tree has 16 top-level shared-focus imports at `common/national_focus/006_independence_wave_focus.txt:40-60`. They cover the generic overlay root, COR, HBX, HAW, FIJ, IW-043, IW-058, IW-093, and IW-098 roots, including the explicitly imported disconnected IW-043 economy/emergency spurs and IW-058 civilian-command spur. A prerequisite/descendant graph over the four Event 006 focus sources reaches all 128 shared definitions from those roots; this is static source evidence, not live UI evidence.

The reviewed meaningful-tree carrier is `common/national_focus/iceland.txt:28-44`. It keeps the vanilla `iceland_tree` and imports the eight generic overlay focuses plus four ICE route consumers. Repository search finds no other current owning-tree import of `independence_wave_overlay_take_stock_of_independence`.

## Required route coverage

| Required lane or overlay | Source evidence | Result and remaining risk |
| --- | --- | --- |
| Survival/state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, `006_independence_wave_focus.txt:65-219` (8 focuses). | Present with a real trunk and founding capstone. Runtime completion conditions are not scenario-proven. |
| Internal power struggle | `independence_wave_map_internal_power_centers`, `:224-272`. | Present as an optional registered two-center branch with three mutually exclusive outcomes; package registration and AI selection remain unproven. |
| Government settlements | Constitutional `:821-899` (5), popular council `:901-954` (4), traditional restoration `:956-1022` (5), emergency military `:1024-1077` (4), patron/client `:1079-1146` (5), radical sovereignty `:1148-1211` (4), and Saar municipal neutral commission `:1218-1266` (4). | All seven required settlement families are represented. Route availability/locks use package flags and shared route effects; live invalid-route and mutual-exclusion cases remain open. |
| Economy/administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`, `:283-399` (6). | Present. Rewards call dynamic administration/transport/economy effects and the treasury idea/technology capstone, not only flat numbers. |
| Army/security/military identity | `independence_wave_integrate_militia_commands` through `independence_wave_found_professional_defense_institution`, `:404-665` (16). | Present. The professional-defence capstone uses five separate prerequisite blocks, each an OR pair, and the ten choice focuses have pairwise mutual exclusions. Scenario balance is untested. |
| Diplomacy/recognition/patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service`, `:674-815` (7). | Present with foreign-office, recognition, neutrality, patron, treaty, and service hooks. Patron validity and AI reachability are unproved. |
| Former host/borders | `independence_wave_define_former_host_policy` and five policy families through `independence_wave_settle_empty_claim`, `:1277-1451` (13). | Present with negotiated, guarded, association, reclamation, and collapse paths. Host-state and map-state cases remain parent-owned runtime gaps. |
| Regional ambition/expansion | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension`, `:1459-1521` (5). | Present with registered ambition family, regional congress, integration authority, and signature anchor. Region-specific family reachability is unproved. |
| Network/League | `independence_wave_recognize_fellow_new_states` through five charter proposals, `:1532-1710` (12). | Present with standing, aid, arbitration, congress preparation, and mutually exclusive charter choices. The accepted four-member/three-willing-member League contract is not live-tested here. |
| Formable preparation and FORM-03 | Generic preparation `:1716-1766` (4) and FORM-03 post-charter sequence `:1773-1883` (6). | Present. Decisions own map validation and formation; post-charter language/industrial progression is gated. Formable-family reachability and staged cores remain unproved. |
| Hidden/high-chaos | `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders`, `:1914-1965` (4). | Present and hidden behind high-chaos/world-collapse triggers. No probability sweep proves safe suppression outside accepted conditions. |
| Package modules | SCO/WLS/AJX/BRI/AFX/AGX/RHI/BAY/ARX/ASX at `:1974-3120` (67 focuses), plus shared IW-043/IW-058/IW-093/IW-098/Pacific/COR branches. | Static branches have package gates, rewards, AI, icons, and localisation. Current content attestation admits only the parent-owned eleven-package set; unadmitted rows remain fail-closed. |
| Generic additive overlay | Eight `independence_wave_overlay_*` shared focuses at `:3149-3277`. | Full-tree definition is present and ICE imports all eight. Other meaningful vanilla trees still lack a reviewed carrier import. |
| Post-formation overlay | Producer at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1497-1501` sets `post_formation_overlay` only when an active Event 006 country already owns the full framework. | Bounded static producer is present. It does not solve meaningful-tree insertion, and formation/save/load/visibility evidence is absent. |

## Prerequisite, bypass, and route-lock audit

The bounded parser found 396 focus prerequisite references with no unknown IDs. Multiple prerequisite blocks are used where the design requires AND-of-OR-pairs, most visibly at `006_independence_wave_focus.txt:509-513` for `independence_wave_found_professional_defense_institution` and at the route capstones such as `independence_wave_consolidate_constitutional_state`, `independence_wave_proclaim_council_commonwealth`, `independence_wave_crown_the_restored_state`, and `independence_wave_entrench_emergency_state`.

The internal-power, military-choice, patron-neutrality, former-host, League-charter, RHI/BAY/ASX, ICE, IW-043, IW-058, IW-093, and IW-098 mutual-exclusion sets are structurally present. The AJX neutral-commission opener at `:1221-1230` lists the six ordinary government openers unilaterally; its own `can_lock_independence_wave_ajx_neutral_commission_route` trigger at `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt:80-86` requires the AJX package flag, founding settlement, undecided government route, and unlocked route, so the asymmetry is guarded rather than proven broken. A live “ordinary route first versus AJX route first” check is still required.

Package `allow_branch`/`available` checks are present, and `common/scripted_triggers/006_independence_wave_focus_triggers.txt:28-61` keeps full-framework, additive, and post-formation visibility gates fail-closed. A flag does not dynamically attach a shared focus to an owning tree; only a reviewed `shared_focus` import does that under the accepted design.

## Missing or simplified content

1. **Central geometry is still validator-blocked.** `hoi4.focus_inspect` reports 14 blocking diagnostics, 49 connector crossings, 18 node intersections, 27 long connectors, six too-close same-row pairs, bounds `x=1..101`, `y=0..19`, maximum horizontal span 80, maximum vertical span 6, and maximum Manhattan span 81. The four coupled repair clusters are the opening oath/economy crossing (`:284-301`), the founding-settlement fan over food/transport (`:323-340`), the same fan over depots/officer recall (`:446-465`), and the professional-defence merge (`:506-529`). A prior coordinate candidate was reverted after worsening crossings and long connectors; no isolated focus move is safe.
2. **Meaningful-tree carrier coverage is incomplete.** `common/national_focus/iceland.txt:28-44` is the only current reviewed vanilla-tree carrier for the generic overlay. `common/scripted_triggers/006_independence_wave_focus_triggers.txt:56-61` recognizes only ICE’s lifecycle flag and `iceland_tree` as an attachable carrier. The twelve other reviewed meaningful-tree adapters in the source map remain decisions/adapter contracts or unproven shared-focus insertions; they must not be called visible focus overlays.
3. **Post-formation visibility is bounded, not accepted runtime.** The formable registry producer now exists, but it is limited to active full-framework countries and leaves meaningful existing trees outside the design. No formation, carrier visibility, save/load, or cleanup scenario matrix is complete.
4. **Regional overlay depth is uneven by admission status.** The full tree has package-specific SCO/WLS/AJX/BRI/AFX/AGX/RHI/BAY/ARX/ASX modules and the shared IW-043/IW-058/IW-093/IW-098/Pacific/COR branches. IW-005 Flanders is intentionally decisions-only (`006_iw005_flanders_overlay_implementation_2026_07_16.md:13-15,46`) and therefore does not satisfy a visible focus-overlay lane without an explicit architecture exception. IW-022, IW-025, IW-035, IW-059, IW-085, IW-101/IW-102/IW-105, and IW-156/IW-196/IW-197/IW-204 remain bounded adapter/overlay work, not admitted full focus packages.
5. **Family-level reachability is unproven.** Static IDs do not prove that every patron, League, former-host, formable, high-chaos, post-formation, or package route is selectable under its accepted origin, state, sponsor, ideology, map, and capacity conditions.

No fallback tree, placeholder focus, generic country replacement, or route family was introduced by this audit.

## Icon coverage

| Surface | Result | Evidence |
| --- | --- | --- |
| Focus/shared blocks | 312/312 specify an icon. | Balanced parser over the four Event 006 focus sources. |
| Distinct icon IDs used | 121. | All references are `GFX_goal_*` IDs. |
| Regular sprites | 121/121 resolve. | `interface/006_independence_wave*.gfx` focus-icon files. |
| Shine sprites | 121/121 matching `_shine` IDs resolve. | Same `.gfx` surfaces; no missing shine pair. |
| Texture paths | 121/121 base paths resolve to registered Event 006 goal assets. | Static `.gfx` path inventory. |
| Reuse risk | Review item only. | Highest-use families are former-host settlement (21), army integration (19), infrastructure authority (18), founding administration (17), League congress (14), regional formable (13), high-chaos sovereignty (12), and recognition diplomacy (11). Package-specific AFX/AGX/RHI/BAY/ARX/ASX icon families are separately registered. |

No icon repair is justified by the current static inventory.

## Localisation and reward mismatch list

The 42 Event 006 English localisation files under `localisation/english/006_independence_wave*.yml` are UTF-8 with BOM. All 312 focus/shared IDs have title and `_desc` keys, and every `custom_effect_tooltip` token resolves. The three intentional tooltip-key normalisations are `independence_wave_focus_build_permanent_foreign_service`, `independence_wave_focus_discover_regional_identity`, and `independence_wave_focus_coordinate_reclamation_fronts`; their resolved keys are `independence_wave_build_permanent_foreign_service_tt`, `independence_wave_discover_regional_identity_tt`, and `independence_wave_coordinate_reclamation_fronts_tt` in `localisation/english/006_independence_wave_focus_l_english.yml`.

Every block has a nonempty `completion_reward`, and reward implementations call dynamic shared effects, route flags, ideas, technology/doctrine bonuses, missions, or staged formable/League hooks. No direct focus-name/reward contradiction was proven in the bounded static scan. A full prose review of all 312 descriptions and effect tooltips, and live tooltip truncation, remain outside this audit.

## AI behavior gaps

All 184 regular focuses and all 128 shared focuses declare `ai_will_do`. In the 184 regular focuses, 80 contain inline modifiers and 104 use only a base constant. The shared/package blocks together contain 133 modifier-bearing AI blocks and 179 base-only blocks. Government, military, patron, former-host, League, high-chaos, ICE, IW-043, IW-058, IW-093, IW-098, and package focus blocks contain route-aware gates where the source design requires them.

Package-level strategy files exist under `common/ai_strategy/006_independence_wave_*.txt` for Brittany, ICE, IW-043/IW-058, IW-093/IW-098, Mediterranean, Pacific, Rhineland/Bavaria, rival bloc, Saar, Scotland/Wales, and Wallonia/Frisia. They are not focus-order proofs. The generic overlay uses common `high`/`urgent` constants, and no Event 006 focus strategy-plan file was found under `common/ai_strategy_plans` or `common/ai_focuses`.

No `hoi4.probability_inspect` sweep was run for valid/invalid patrons, League membership, formable map checks, host-collapse/reclamation, high-chaos suppression, ICE carrier selection, or post-formation visibility. These are parent-owned completion gaps, not missing `ai_will_do` syntax.

## High-priority fixes first

1. Reflow the four geometry clusters as one coordinated layout change, preserving every focus ID, prerequisite block, mutual exclusion, reward, icon, localisation key, and AI weight, then rerun `hoi4.focus_inspect` and `hoi4.focus_render` after each coherent tranche.
2. Expand the meaningful-tree carrier contract only through reviewed static imports and explicit cleanup. Begin with ICE evidence and document a disposition for each other existing meaningful tree; do not call `load_focus_tree` for those trees.
3. Run route reachability and AI probability validation across full framework, meaningful-tree overlay, patron, former-host, League, formable, high-chaos, package, and post-formation cases, including ordinary-route/AJX ordering and carrier failure-closed behavior.
4. Re-audit package-specific shared-focus geometry and runtime admission after the parent’s eleven-package attestation gate changes; do not promote the 206-row registry, 149 publishers, or static adapter presence as focus completion.
5. Treat IW-005 Flanders as a documented decisions-only exception or obtain an accepted preservation-safe focus carrier before claiming regional-overlay focus coverage for that package.

## MCP evidence

`hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` returned `FOCUS_INSPECTED` with validation false and the 14 blockers above. Inspect artifact: [focus inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f7ae651c7aa82e44462cfd2f41a0cad21529ea3cd6de0dcf3de0d46827b8eef/3430d32917ef7a0fa83d26dd58ff682e3d18e511b5077fd1126fdc50e8a8276e/focus-inspect.fa5c997ad511d012.json).

`hoi4.focus_render` reproduced layout hash `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`, width 13428, height 1830, and the same blockers. Review artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f956357238e8b464c69d8f62847450c11e1e62f8d5c58307ff3dad7cd5ec2ca/4cd4046cf22234c4de442c75c3c1c3e69a173bf8cb94517190ea779f0d43fb3d/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7d02695294c4518c0b17f1f439891a59f78d31c7b706d5e75a0d381e7ac0d92/9f4c0e8eca8d85c8e0510f746e453de47958989fc461540793aefd7678e2b83e/independence_wave_focus_tree.focus.svg), and [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c675ecfdb3c8779aba3083242064448c25a2db5118609e9ab4a7f91f9842a15/24ede85d513ec07c8ecf913285933df5597f8eefc088b04dcaf2fe78ee2df811/independence_wave_focus_tree.focus.json).

The MCP inline inventory was truncated, so static icon/localisation scans above remain the authoritative coverage evidence. Standalone inspection of shared-only files is not applicable because they contain definitions but no `focus_tree` block.

## Validation performed and skipped

Performed: required offline Paradox wiki and vanilla documentation review; balanced-block parsing of all four Event 006 focus sources; duplicate-ID and unknown-prerequisite checks; title/description/tooltip localisation checks; BOM checks; icon regular/shine/path checks; repository carrier search; source review of focus assignment triggers/effects and formable post-formation producer; `hoi4.focus_inspect`; and `hoi4.focus_render`.

Skipped: `hoi4.focus_rewrite` because the diagnostics are coupled and no safe local rewrite was authorized; game execution, save/load, live package admission, and probability simulation because those belong to the parent/user validation surface; full player-facing prose review because the bounded static key/reward checks did not identify a local mismatch.

## Changed files, identifiers, and remaining risks

Changed gameplay files: none. Changed focus IDs: none. Changed localisation keys: none. Changed icon IDs: none. No improvement-loop plan was written because no whole route family is absent; the remaining work is coordinated geometry repair, carrier design/evidence, and parent-owned runtime validation.

Remaining risks are the 14 blocking geometry diagnostics, incomplete meaningful-tree carrier coverage beyond ICE, post-formation visibility evidence, unproven family-level reachability, package admission/overlay depth, focus-order AI selection, and live balance. No simplification or fallback was introduced.
