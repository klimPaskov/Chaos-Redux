# Event 006 focus final audit v70

Date: 2026-08-01.

Scope: read-only audit of the Event 006 shared framework, package overlays, additive-carrier boundaries, route wiring, icons, localisation, AI weights, and current MCP geometry.

Disposition: **PARTIAL / HOLD**. The source has broad route coverage and clean static ID/icon/localisation coverage, but the focus tree still fails the current MCP layout validation and the additive package boundary is only proven for Iceland. No focus source was patched in this audit.

## Evidence and source inventory

Required repository guidance, the six Event 006/HOI4 skills, the offline Paradox wiki national-focus page, the required core wiki pages, and the vanilla documentation files for effects, triggers, modifiers, localisation formatting, and script concepts were read before this audit.

| Source | Current static result |
| --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | 207 blocks: 184 regular focuses and 23 `shared_focus` blocks; 318 total Event 006 IDs after the overlay files are included. |
| `common/national_focus/006_independence_wave_pacific_focus.txt` | 20 `shared_focus` blocks. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | 48 `shared_focus` blocks. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | 43 `shared_focus` blocks. |
| All four Event 006 focus files | 318 unique IDs, zero duplicate IDs, every block has an icon, `completion_reward`, and `ai_will_do`; all 318 completion rewards use distinct normalized reward bodies. |

The central tree is explicitly documented as the full-framework owner at `common/national_focus/006_independence_wave_focus.txt:8-21`, and the shared overlay is declared after that tree at `common/national_focus/006_independence_wave_focus.txt:3167-3170`.

## Route coverage table

| Required lane | Current implementation and evidence | Verdict |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` at `common/national_focus/006_independence_wave_focus.txt:85-243`; the capstone requires ministries, regional communications, and provincial integration, while `can_complete_independence_wave_survival_capstone` additionally checks capital control, legitimacy, and functioning capacity at `common/scripted_triggers/006_independence_wave_focus_triggers.txt:79-85`. | PASS at source level. |
| Government settlements | Constitutional, popular-council, traditional, emergency-military, patron-client, radical-sovereignty, and the IW-010 municipal-neutral-commission branch are all present at `common/national_focus/006_independence_wave_focus.txt:839-1290`. The seven opening commitments are mutually exclusive at focus IDs on lines 865, 925, 994, 1048, 1117, 1172, and 1241, and route readiness/locks are centralized in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:108-229`. | PASS at source level; runtime reachability still needs parent-owned scenario sweeps. |
| Economy, infrastructure, and administration | Emergency revenue, food/fuel, regional transport, customs, package economic activation, and treasury capstone are the lane at `common/national_focus/006_independence_wave_focus.txt:302-421`; rewards include fuel, stockpile/economic flags, technology bonus, and the independent-treasury idea. | PASS at source level. |
| Army, security, and military identity | Militia integration, national depots, officer vetting, border guard, force archetype, professional defence, civilian/military choice, reserve/core choice, arsenal/foreign-arms choice, border/reclamation choice, and league/independent command choice are at `common/national_focus/006_independence_wave_focus.txt:423-693`. `independence_wave_found_professional_defense_institution` uses five separate prerequisite blocks, each containing a paired alternative, so the intended AND-of-five-OR semantics are preserved. | PASS at source level. |
| Diplomacy, recognition, and patrons | Foreign-office, missions, recognition, guarantor, patron, treaty, and foreign-service route content is at `common/national_focus/006_independence_wave_focus.txt:694-839`; route modifiers and patron thresholds are provided by `006_independence_wave_focus_triggers.txt:153-229`. | PASS at source level; no probability/timing sweep was run. |
| Former-host settlement | Negotiated separation, guarded frontier, association, reclamation, and collapsed-host settlement are at `common/national_focus/006_independence_wave_focus.txt:1296-1474`. The four living-host openers are mutually exclusive at lines 1314, 1355, 1383, and 1411, while the collapsed-host branch uses `can_settle_independence_wave_host_collapse` at `006_independence_wave_focus_triggers.txt:233-270`. | PASS at source level. |
| Regional ambition and signature extensions | `independence_wave_survey_regional_ambition` begins the package-owned extension lane at line 1483 and is gated by `can_open_independence_wave_regional_ambition` at `006_independence_wave_focus_triggers.txt:273-283`. | PASS at source level; package admission remains separate. |
| Network and league | Recognition, civil-service exchange, aid corridor, arbitration, charter, founding members, congress, and five mutually exclusive proposals run from `common/national_focus/006_independence_wave_focus.txt:1550-1733`. Decisions own votes and proclamation as documented in the source comment at line 1551. | PASS at source level. |
| Formable preparation | Identity discovery, union congress, formation terms, and integration commission run at `common/national_focus/006_independence_wave_focus.txt:1735-1790`; FORM-03 post-charter focuses continue at lines 1792 onward. Discovery is gated by `can_open_independence_wave_formable_branch`, while formable transactions and claims remain decision-owned. | PASS at source level; individual formable/carrier admission remains open. |
| High-chaos sovereignty | `independence_wave_sponsor_further_ruptures`, reclamation fronts, open sovereignty, and border-charter rewrite run at `common/national_focus/006_independence_wave_focus.txt:1931-1988`. The lane is gated by `can_open_independence_wave_high_chaos_lane` and can open from World Collapse/ambition without requiring the radical government settlement, as documented in the source comment at line 1933. | PASS at source level; no high-chaos AI probability sweep was run. |
| Package overlays | Scotland, Wales, Saar, Brittany, Wallonia, Frisia, Rhineland, Bavaria, Sardinia, Sicily, COR, Pacific, IW-043/IW-058, and IW-093/IW-098 blocks are present in the central/shared package files at `common/national_focus/006_independence_wave_focus.txt:1991-3146` and the three overlay files. | PASS for source presence; package admission/identity evidence is outside this audit. |
| Post-formation overlay | `independence_wave_formable_commit_selected_family` assigns `post_formation_overlay` only when the active country already carries `independence_wave_full_focus_framework` at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1508-1515`; the assignment preserves the full-tree flag and sets both additive/post-formation flags in `common/scripted_effects/006_independence_wave_focus_effects.txt:39-72`. | PASS for full-framework formables; no non-full meaningful-tree post-formation carrier is proven. |
| CAT/IW-014 boundary | CAT roots are imported at `common/national_focus/006_independence_wave_focus.txt:75-82`, and CAT package focuses are declared at lines 3527-3650. However, the draft calls itself additive while its first root requires `can_use_independence_wave_full_focus_framework` at line 3540, and the CAT setup assigns `full_framework` at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:316-317`, which calls `load_focus_tree`. The current source-of-truth map still marks IW-014 CAT as fail-closed outside attestation because the Iberian X identity, flag package, identity review, and NAV/GLC adapters are incomplete. | PARTIAL / BLOCKED. The wording and code disagree, and the current additive carrier contract does not admit CAT. |
| Africa boundary | `common/national_focus/012_africa_continental_focus_tree.txt:24` owns `africa_continental_focus_tree`, with separate priority/world trees in `012_africa_priority_member_focus.txt:21` and `012_africa_world_europe_focus.txt:19`; these files contain no Event 006 focus imports, and the Event 006 focus/effect/trigger files contain no Africa carrier or import. | PASS as a deliberate boundary; no unified Event 006 additive overlay exists for Africa. |

## Prerequisites, mutual exclusions, and reward wiring

- The route-opening focuses use one prerequisite block for a single parent and separate prerequisite blocks when all parents are required, matching the wiki semantics that one block is OR and separate blocks are AND.
- The professional-defence capstone at `common/national_focus/006_independence_wave_focus.txt:529-531` has five separate prerequisite blocks containing paired alternatives, which is the intended AND-of-five-OR shape rather than an accidental all-six requirement.
- Government opener mutual exclusions cover all seven settlement families, including the AJX neutral commission, and route-specific `allow_branch`/`available` checks are backed by the centralized triggers rather than only by localisation.
- Former-host and league proposal routes also use reciprocal mutual-exclusion sets, with source references at `common/national_focus/006_independence_wave_focus.txt:1314-1428` and `1665-1733`.
- Static reward coverage is complete for the 318 parsed blocks: every block has `completion_reward`, every block has a distinct normalized completion body, and every `custom_effect_tooltip` key has a localisation entry.
- No direct focus-title, focus-description, completion-tooltip, or reward-key mismatch was found by the bounded key scan; semantic prose-to-effect review remains limited and should not be treated as a full balance audit.

## Icon coverage table

| Check | Result |
| --- | --- |
| Focus icon references | 121 unique base `GFX_goal_independence_wave_*` references across the 318 blocks. |
| `.gfx` registration | 121/121 references resolve to a `name` in `interface/*.gfx`; the scan found zero missing names. |
| Shine sprites | 121/121 base references have a matching `_shine` sprite definition. |
| Missing icon diagnostics | None found in the bounded source scan or the MCP focus inspection output. |

The principal registration files are `interface/006_independence_wave.gfx` and the package-specific `interface/006_independence_wave_*_assets.gfx` files.

## Localisation and reward mismatch list

- Static key coverage is complete for all 318 focus IDs and all 318 `_desc` keys across `localisation/english/006_independence_wave*` and the other Event 006 localisation files.
- All 318 custom effect tooltip keys used by the focus blocks resolve to localisation keys.
- Event 006 English localisation files inspected for this audit carry UTF-8 BOM bytes (`EF-BB-BF`).
- No missing or duplicate focus localisation key was found by the bounded scan.
- No exact normalized completion-reward body is repeated across the 318 blocks, so the audit found no mechanically duplicated reward body.
- A full human semantic review of every title/description against every hidden effect was not repeated in this final geometry-focused pass; parent review should retain the whole-event HOLD/PARTIAL disposition.

## AI behavior gaps

- Every parsed focus block has an `ai_will_do` block, and the route openers use route/war/instability/patron/host/chaos conditions rather than only a naked base value.
- Package branches carry package-specific `allow_branch` and/or `available` gates, and the ICE route consumers include route-aware AI modifiers in `common/national_focus/006_independence_wave_focus.txt:3301-3447`.
- The source does not provide a complete scenario probability sweep for patron, league, formable, high-chaos, CAT, or the unadmitted additive carriers; this is an evidence gap, not a claimed runtime failure.
- The additive carrier trigger is intentionally fail-closed but currently admits only the reviewed Iceland carrier: `can_attach_independence_wave_additive_focus_carrier` at `common/scripted_triggers/006_independence_wave_focus_triggers.txt:52-64` requires the carrier flag plus `iceland_tree`, while the only setter is `common/scripted_effects/006_independence_wave_ice_package_effects.txt:354`.
- FSM requests `additive_overlay` at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:765-766`, but no FSM carrier registration exists, so the assignment fails closed by design.
- CAT currently requests `full_framework`, not additive, at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:316-317`; this is inconsistent with the CAT overlay comment and the current source-of-truth wording.

## Current MCP geometry diagnostics

Fresh `hoi4.focus_inspect` result for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`:

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e308c0959a006f6aa351a2cc02cb7407236d14d047aaffa99812ba73247af36/80e6fa97461319c1ea1939e8b81888b10fce841b559f882b57f2570c863b4ff3/focus-inspect.2593b45037e97f42.json`.
- Layout hash: `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.
- Metrics: 184 regular nodes, 223 connectors, 45 crossings, 7 node intersections, 28 long connectors, total horizontal span 1228, total vertical span 242, bounds x=1..101 and y=0..19.
- Same-row spacing: 164 checked pairs and 5 too-close pairs.
- Validation remains false because 14 blocking focus diagnostics are present.
- The blocking diagnostics are long connectors, fixed-endpoint connector crossings, and one through-node intersection involving the founding-settlement, inventory/emergency-revenue, bind-oath/integrate-militia, AJX/former-host/recognition, survey-ambition, professional-defence, reclamation, league-standardisation, and durable-sovereignty edges.
- The unsatisfied crossing diagnostics report `movableFocusIds: []`, so a safe local node move is not available; a coordinated reflow is required.

Fresh `hoi4.focus_render` artifacts:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/851338a874752aab23cb217f917a6b59a0594e39460b7c8e9f698c05c9c09cdc/3071b0b13ce632bb018f993afbbb86e7eb0d30f406be2c8239fb633402e7ce50/independence_wave_focus_tree.focus.html`.
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db058a79681af4beadd7012b103961104222162d8df430e7e294a1c47cbc39dd/bbf69bc37b27c651e35c5562b12298ff22a42d6fb0c53f095c95b2096915d61b/independence_wave_focus_tree.focus.svg`.
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9987bc22eed2ddcd71c28c705169b9dbfc5a14fa683952abf57ae6a5b739570/e62a4ab3495c03eabf9dc6ff75f07e8af5236120cb409152bebbe5c95f4b3c11/independence_wave_focus_tree.focus.json`.
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15a35fe1acdd6c5b89997e726ff64ce5083fa19b3a196e2ab1f73d66144cd13d/accd949ad9f87407d5e666485add94dffe976775c5086a88d861b5227afd1e23/independence_wave_focus_tree.focus.source-map.json`.
- The default raster request was blocked by the fixed 16384-pixel ceiling because the full render is 17904x2440; the reduced review raster succeeded at 4152x1163.
- Reduced raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdbd4e90d7103eef984e361bb0fb8fb2596538ec35ca7aef1ee3f2c2a0be6778/4fc42db30f96d251023ec4d1f77fb86a25843ec8c2b98f7c7d494cba7178a0fb/independence_wave_focus_tree.focus.png`.

`hoi4.focus_rewrite` was intentionally skipped because this was a read-only audit and the MCP marks every unsatisfied crossing as having no movable focus IDs.

## Missing, simplified, and blocked content

1. The central tree is not MCP-valid because 14 coupled layout diagnostics remain, so the tree cannot be treated as geometry-complete.
2. Additive carrier admission is currently proven only for Iceland; the generic flag is not an engine insertion mechanism, and all other additive requests fail closed unless a reviewed owner-tree carrier is added.
3. CAT's source comment and source-of-truth entry describe an additive vanilla-carrier overlay, but the current setup calls the full framework and the root branch requires the full-framework trigger, which would replace the owning tree if CAT ever passed its admission gates.
4. The CAT package remains outside attestation because the source-approved Iberian X identity, complete flag package, identity review, and complete NAV/IW-013 and GLC/IW-015 adapters are missing; this is a package admission blocker rather than a missing focus-ID blocker.
5. Africa intentionally remains a separate focus-tree system; no Event 006 additive graft or shared carrier is implemented for Africa, so cross-system integration is not demonstrated.
6. Static source does not prove route timing, AI selection probabilities, save/load persistence, or live consumer visibility; those are parent-owned evidence gaps under the current source-of-truth map.

## High-priority fixes

1. Perform one coordinated geometry reflow of the fixed-endpoint crossings and long connectors, then rerun `hoi4.focus_inspect`, `hoi4.focus_render`, and a reduced raster review until the 14 blockers are cleared or a reviewed geometry exception is documented.
2. Resolve the CAT contract before admission by either implementing a reviewed vanilla CAT carrier/additive path or changing the package design and documentation to explicitly authorize a full-tree load; do not leave the current additive wording/full-load behavior mismatch.
3. Add reviewed owner-tree carrier contracts for any future meaningful-tree additive package, with an explicit setter and post-validation evidence; keep unreviewed packages fail closed.
4. Run parent-owned route and AI probability sweeps for each government settlement, patron/league proposal, formable, high-chaos, and admitted package branch.
5. Reconcile the CAT and Africa package boundaries with the current source-of-truth map before any whole-event completion claim.

## Validation and limits

Meaningful checks completed: required wiki/vanilla documentation review, nested-focus static parser, duplicate-ID scan, icon-to-`.gfx` and `_shine` scan, focus-title/description/tooltip localisation scan, BOM scan of Event 006 English localisation files, fresh MCP inspect/render, and reduced raster review.

Skipped: no focus rewrite, no source patch, no game launch, no live-save/save-load observation, and no scenario probability simulation because the parent requested a read-only bounded audit and the current MCP diagnostics have no movable IDs.

No fallback content was introduced.

No improvement-loop plan was written because route depth is present and the immediate blockers are geometry, carrier admission, package identity, and evidence rather than a shallow missing route family.

## Parent handoff

The parent should treat this handoff as the current focus-specific disposition: broad route coverage and static asset/localisation checks PASS, CAT/additive carrier integration is PARTIAL, Africa remains a separate boundary, and the shared-tree geometry remains BLOCKED by the 14 fresh MCP diagnostics.
