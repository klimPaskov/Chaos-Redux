# Event 006 generic focus surface audit

Date: 2026-08-03.

Scope: read-only audit of the accepted one-tree Event 006 focus framework after the parent-owned geometry reflow. The audit covers route coverage, prerequisites, mutual exclusions, icons, localisation, rewards, AI hooks, and current `hoi4.focus_inspect`/`hoi4.focus_render` evidence.

Disposition: **AUDIT COMPLETE / NO SAFE LOCAL PATCH**.

The source is unchanged. The only Event 006 diagnostic is the intentional isolated warning on `independence_wave_preserve_independent_command`; adding a visible prerequisite would alter the accepted hidden-gate geometry and must be handled by a coordinated parent reflow if it is ever desired.

## Current MCP evidence

The fresh `hoi4.focus_inspect` call resolved `independence_wave_focus_tree` from `common/national_focus/006_independence_wave_focus.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02c53b898c2194f15af26b64269d0ee67edeb7f3d1b516219ddb5729c2d415fa/7bc5076975c1a05b4be2dad202ff79c4b1c901fbec9ae8d3f47d9e796a95a2c8/focus-inspect.72f3e7922c9e4b4a.json`.

The tree resolves 184 direct focus nodes and 192 connectors with layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2`. MCP reports zero Event 006 crossings, node intersections, long connectors, or same-row spacing violations. Bounds are `x=1..121`, `y=0..19`; the maximum horizontal connector span is seven columns.

The fresh `hoi4.focus_render` call produced these review artifacts.

| Artifact | URI |
| --- | --- |
| HTML | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a3bd831786e84784b2ba2bc02e0ccea6e05e7ca0ba53d226283e07ecafe142f/0056aaa7cb5087e1656a9febe28c368ef1964f29e2334a3d5d1a1d80a4eef0e7/independence_wave_focus_tree.focus.html` |
| SVG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a556ee61cca5f3861b9b6e7474b4d5bf973f414fb5cedffb6024550cbdbfc026/34cc0580c87baeb1cf6e0387f5ea7c6d25353d597e22ac8661856ccead1711a6/independence_wave_focus_tree.focus.svg` |
| JSON | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ca461ac81d6b56fa4adf3ab065da1aba5fc8e2b3b0838d8b827a24cca855426/b34c729c8f90e6077e67a352bd416f6bef097a0b7187f1f27e888db16c2edf0b/independence_wave_focus_tree.focus.json` |
| Source map | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cadd1e58ed0a0c32895099288fd06a4c21f0685724082a1b4c38d5b8c9f2319f/5eb117bb2f5f4121f890e5cf0311f8114b4e994e055a5b0935e43755346759df/independence_wave_focus_tree.focus.source-map.json` |
| Plan metadata | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68e486a1002af710814092ced63c7fec1dcdd7e447029ed1df4176d8929a35a9/eeea8cbb3a7d095c23ef51a9b5013a737bad6bedbf96c5ff04552b53b89562d5/independence_wave_focus_tree.focus.plan.json` |

The render and inspect still report 14 blocking diagnostics from unrelated vanilla continuous focuses in `game:common/continuous_focus/generic.txt`, plus the Event 006 warning `FOCUS_ISOLATED` for `independence_wave_preserve_independent_command` at `common/national_focus/006_independence_wave_focus.txt:734-751`. No Event 006 icon or localisation diagnostic was emitted.

## Route coverage

| Required route | Source coverage | Status and evidence |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, `common/national_focus/006_independence_wave_focus.txt:100-243` | PASS. The chain gates the founding settlement and writes the shared survival/state values. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` through `independence_wave_ajx_entrench_neutral_commission_focus`, `common/national_focus/006_independence_wave_focus.txt:257-1382` | PASS. Constitutional, popular-council, traditional, emergency-military, patron-client, radical-sovereignty, and AJX neutral-commission openings are present with route locks and reciprocal exclusions. |
| Economy, infrastructure, and administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`, `common/national_focus/006_independence_wave_focus.txt:322-443` | PASS. Economy branches feed capacity, treasury, transport, and package-program effects. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command`, `common/national_focus/006_independence_wave_focus.txt:448-751` | PASS. The professional-defense capstone at `:555-597` uses five AND-of-OR prerequisite groups; all ten y=8 choices are present and mutually exclusive in pairs. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service`, `common/national_focus/006_independence_wave_focus.txt:757-903` | PASS. Recognition, neutrality, patron balancing, treaty backing, and permanent foreign service are wired to shared ledgers. |
| Former-host settlement | `independence_wave_define_former_host_policy` through `independence_wave_settle_empty_claim`, `common/national_focus/006_independence_wave_focus.txt:1389-1579` | PASS. Living-host settlement choices are exclusive and the collapsed-host ledger branch is separately gated. |
| Regional ambition and signature extensions | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension`, `common/national_focus/006_independence_wave_focus.txt:1581-1654` | PASS. Registered ambition families and mandate state gate the lane. |
| Network and League | `independence_wave_recognize_fellow_new_states` through `independence_wave_propose_revisionist_charter`, `common/national_focus/006_independence_wave_focus.txt:1659-1842` | PASS. Network aid, arbitration, charter, congress, and proposal focuses remain focus-owned while votes and proclamation remain decision-owned. |
| Formable preparation and FORM-03 chain | `independence_wave_focus_discover_regional_identity` through `independence_wave_form03_submit_low_countries_compact`, `common/national_focus/006_independence_wave_focus.txt:1848-2040` | PASS at source level. Focuses prepare identity, congress, terms, integration, and the FORM-03 post-charter chain; discovery, claims, consent, and formation stay in the formable decision/adaptor surfaces. |
| High-chaos sovereignty | `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders`, `common/national_focus/006_independence_wave_focus.txt:2046-2103` | PASS. World Collapse, radical/open-sovereignty, danger-milestone, and revisionist-pressure gates are present. |
| Package and signature modules | Main-tree package blocks `common/national_focus/006_independence_wave_focus.txt:2111-3320`, plus `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, and `006_independence_wave_pacific_focus.txt` | PASS for source presence and exact package gates. Admission, identity, and formable readiness remain separate package evidence surfaces. |
| Durable-state capstone | `independence_wave_secure_durable_sovereignty`, `common/national_focus/006_independence_wave_focus.txt:3321-3339` | PASS. Economy, military, foreign-service, host-policy, and durable-state trigger requirements are explicit. |
| Additive carrier boundary | `independence_wave_overlay_take_stock_of_independence` and its overlay chain, `common/national_focus/006_independence_wave_focus.txt:3347-3474` | PASS as an intentional boundary. The overlay is opt-in and does not load or replace a carrier's meaningful tree. |

The four Event 006 focus source files contain 184 direct definitions, 134 shared-focus definitions, and 27 main-tree import roots, for 318 unique focus IDs. This is one `independence_wave_focus_tree`, not a collection of country trees.

## Missing or simplified content

- No accepted route family is missing, and no fallback or bespoke country tree was introduced.
- The source graph does not prove runtime package admission, formable transactions, save/load persistence, or live focus selection after ledgers change.
- No probability sweep was run for government, patron, League, formable, high-chaos, package, or CAT opener ordering.
- Package branches are source-present but remain fail-closed until their separate identity, carrier, and readiness evidence is accepted.
- The additive carrier remains deliberately narrow; broadening it would bypass the accepted ownership barrier.
- The 14 MCP blocking diagnostics are vanilla continuous-focus references and are outside this Event 006 focus source. They should not be “fixed” by changing Event 006 assets.

## Icon coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Unique focus icon references | 121 | Four `common/national_focus/006_independence_wave*.txt` sources. |
| Base `.gfx` registration | 121/121 | `interface/006_independence_wave*.gfx`. |
| Shine sprites | 121/121 | Matching `_shine` registrations in the same `.gfx` files. |
| Focus image files | Resolved by MCP | The current inspect/render inventory resolves the Event 006 icon assets; no Event 006 icon diagnostic is present. |
| Missing/repeated icon issue | None found | No icon patch is justified. |

## Localisation and reward mismatch list

- All 318 focus IDs have title keys and all 318 `_desc` keys across the 45 Event 006 English localisation files under `localisation/english/006_independence_wave*_l_english.yml`.
- All 318 `custom_effect_tooltip` keys used by focus rewards resolve.
- All 45 scanned Event 006 English localisation files carry UTF-8 BOM encoding.
- No duplicate focus ID, title/description key, or custom-tooltip key was found in the bounded scan.
- No exact normalised completion-reward body repeats across the 318 definitions.
- No player-facing title, description, or reward-key mismatch was found by the bounded key scan.
- A semantic prose-to-effect review was not repeated for every package sentence in this geometry tranche, so claims are limited to key and reward-body evidence.

## AI behavior gaps

| Surface | Current evidence | Gap/risk |
| --- | --- | --- |
| Focus AI blocks | Every one of the 318 parsed focus definitions has `ai_will_do`; 26 hidden prerequisite gates all include `independence_wave_focus_ai.prerequisite_boost` | Source coverage is complete; relative runtime selection order is untested. |
| Shared constants | `common/script_constants/006_independence_wave_focus_constants.txt:62-78` defines none/cautious/standard/high/urgent, preference, avoidance, war-avoidance, and hidden-gate boost factors | No tuning change is justified without scenario evidence. |
| Generic profiles | `common/ai_strategy/006_independence_wave_generic.txt:42-143` provides survival, recovery, and consolidation profiles keyed by `independence_wave_generic_ai_profile` | Runtime activation and starvation across route families remain untested. |
| Route-aware focus modifiers | `common/national_focus/006_independence_wave_focus.txt` reads government, package, host, patron, network, military, and chaos state in route modifiers | No probability sweep or live AI run proves route preference or completion timing. |

## High-priority follow-up

1. Preserve the current geometry and hidden-gate treatment until a parent-owned reflow can review `independence_wave_preserve_independent_command` together with `independence_wave_standardize_with_league`, the professional-defense capstone, and the surrounding diplomacy lane. A one-line visible prerequisite is not a safe local patch because it changes the coupled layout and the intentional route presentation.
2. Run the parent-owned probability/AI evidence pass for government, patron, League, formable, high-chaos, package, and CAT opener scenarios. The relevant focus IDs and generic profiles are listed above; no source edit is recommended before that evidence.
3. Keep package admission and formable readiness validation separate from this focus-source audit. Source presence is PASS, but runtime contract closure is not implied by the focus graph.
4. Ignore the unrelated vanilla continuous-focus icon/localisation diagnostics when assessing Event 006 focus assets.

## Validation and limits

Meaningful checks completed were the fresh `hoi4.focus_inspect`, fresh `hoi4.focus_render`, four-file focus block/duplicate-ID scan, prerequisite and mutual-exclusion reference scan, reciprocal mutual-exclusion scan, five military capstone AND-of-OR inspection, hidden-gate AI compensation scan, icon-to-`.gfx` and shine scan, focus title/description/custom-tooltip key scan, reward-body uniqueness scan, and UTF-8 BOM scan.

Skipped `hoi4.focus_rewrite` because the source is already reflowed, the remaining Event 006 warning is intentional, and a rewrite would exceed this narrow audit scope.

Skipped live game launch, save/load, pixel raster review, and in-game AI validation because they are parent/user-owned surfaces and outside the accepted one-tree focus contract.

## Changed files and identifiers

No gameplay, focus, localisation, icon, AI, or plan source file was changed by this audit.

This handoff file is the only new artifact: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_generic_focus_surface_audit_2026_08_03.md`.

Changed focus IDs: none.

Changed localisation keys: none.

Changed icon IDs: none.

No improvement-loop plan was written because the accepted generic tree already has broad route depth; the remaining work is coordinated geometry/runtime evidence, not a missing route family.

## Remaining route risks

- `independence_wave_preserve_independent_command` remains intentionally isolated in the MCP design diagnostic because its prerequisite is represented in `available` and mutual exclusion rather than a visible connector (`common/national_focus/006_independence_wave_focus.txt:734-751`).
- The MCP render is validation-partial because of 14 unrelated vanilla continuous-focus diagnostics, although Event 006 layout metrics are clean.
- Source checks do not prove runtime focus selection, package admission, formable formation, save/load persistence, or AI completion order.
- CAT and other non-attested package branches must remain fail-closed until their separate package evidence closes.

Parent handoff: retain the current source and geometry, use the artifact links above for review, and queue only parent-owned probability/runtime evidence or a coordinated reflow if the intentional isolated warning must be removed.
