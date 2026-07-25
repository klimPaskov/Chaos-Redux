# Event 006 focus-tree completion audit

Date: 2026-07-25

Scope: read-only audit of the Event 006 national-focus framework, imported shared branches, package overlays, focus localisation/icons, AI declarations, and focus-to-decision hooks. No gameplay files were edited.

## Verdict

**FAIL for completion.** The shared framework is structurally substantial and its source references are internally resolved, but the accepted design is not proven complete: the economy capstone has no continuing-decision consumer, package-specific focus coverage is narrower than the accepted package registry, the overlay only dynamically titles some lanes, and the authored focus layout still fails MCP validation with 14 blocking layout diagnostics.

The source admission gate is authoritative for current runtime scope. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:13-64` registers 18 adapters but currently attests exactly nine executable packages: IW-001, IW-004, IW-007, IW-008, IW-009, IW-010, IW-017, IW-019, and IW-184. The 206-row package registry and older completion handoffs describe a broader future surface; those older six/seven-package counts are stale and are not used as current runtime facts here.

## Evidence and validation

- `hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned 176 regular focuses, 214 connectors, 148 diagnostics, 49 crossings, 18 node intersections, and 26 long connectors. Validation failed on 14 blocking layout diagnostics; no parser, icon, localisation, or unresolved-reference blocker was reported. Artifact: [focus-inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3ffdd932241beb43437ca660516ad13ae55fdae83baa2ee62a65bb382b44906/425f5e8c7f9a6941b834d6bddbbee462f4844d9bb84cd751a0cd1e40091d92ce/focus-inspect.dfe1fff510afabd2.json).
- `hoi4.focus_render` returned a 17,200 by 2,440 render with the same 14 blocking diagnostics. Artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/887809e4c17f8082726cc4fd21cffde17a5362c1b1218c879d0be89b4c99d82b/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d74054c7a00db6d333e6ef6aa9747241fcac2c5d9e899a6e0e1fc1ce9b31938/independence_wave_focus_tree.focus.svg).
- A source-level parser counted 176 regular and 13 shared blocks in `006_independence_wave_focus.txt`, plus 48 IW-043/IW-058 shared blocks, 43 IW-093/IW-098 shared blocks, and 14 Pacific shared blocks: 294 focus/shared-focus blocks total. Every block has a localisation key and `_desc`; every icon reference resolves and has a matching `_shine` sprite. Every block also has an `ai_will_do` block.
- Required reference material was read before the audit: AGENTS.md, the focus/events/decisions/assets/improvement/subagent skills, offline national-focus and core wiki pages, and the relevant vanilla script/focus documentation.

## Route coverage table

| Route surface | Evidence | Verdict | Concrete gap or bounded fix |
|---|---|---|---|
| Framework assignment and additive overlay | `common/national_focus/006_independence_wave_focus.txt:25-55`; `common/scripted_effects/006_independence_wave_focus_effects.txt:29-56`; full/additive triggers in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-42` | PASS structurally | Full framework and additive mode are separated, and existing trees are not replaced by this focus tree. Runtime package/overlay reachability still needs scenario proof. |
| Survival and founding settlement | Main lane through `independence_wave_complete_founding_settlement` at `006_independence_wave_focus.txt:63-216`; gate in `006_independence_wave_focus_triggers.txt:57-63` | PASS | The capstone writes `independence_wave_founding_settlement_complete`, which the government lane consumes. Capital/mission/legitimacy/capacity scenarios were not run. |
| Government settlement | Seven route anchors from `006_independence_wave_focus.txt:818-1270`; route locks and `has_completed_independence_wave_government_settlement` in `006_independence_wave_focus_triggers.txt:86-209` | PASS with reachability caveat | Constitutional, popular, traditional, emergency, patron-client, radical sovereignty, and AJX municipal-neutral routes have locks and mutual exclusions. Package/region-specific institution naming is mostly static in shared localisation. |
| Economy and administration | Serial economy lane `006_independence_wave_focus.txt:281-389`; regional/economic helpers in `006_independence_wave_focus_effects.txt:443-560` | **FAIL at capstone contract** | `independence_wave_create_independent_treasury` sets only a tech bonus, `independence_wave_economy_capstone_complete`, and stabilization (`:377-389`). `rg` found no consumer of that capstone flag in `common/decisions`, `common/scripted_triggers`, or `common/scripted_effects`; unlike military/diplomacy, no treasury-specific continuing decision is unlocked. Part 4 explicitly requires each economy capstone to unlock continuing decisions (`spec_part_4:377-390`). Add or prove a bounded decision hook and make the treasury reward match its title/tooltip. |
| Military and force identity | Military lane `006_independence_wave_focus.txt:401-662`; five paired choices and institution at `:502-524`; professionalization decision consumer at `common/decisions/006_independence_wave_decisions.txt:1097-1103` | PASS | The five one-line prerequisite blocks are intentional OR semantics, and the institution focus writes `independence_wave_unlock_professional_army` plus the defense capstone. MCP layout crossings are concentrated around this lane and need authored endpoint cleanup. |
| Diplomacy, recognition, and patrons | Diplomacy lane `006_independence_wave_focus.txt:671-809`; foreign-service consumer at `common/decisions/006_independence_wave_decisions.txt:734-740` | PASS | The diplomatic capstone has a visible continuing decision hook. The neutral-or-patron prerequisite on `independence_wave_become_treaty_backed_state` is valid OR semantics because its two parents are mutually exclusive; do not rewrite it as AND. |
| Former-host settlement | Four living-host paths plus host-collapse path at `006_independence_wave_focus.txt:1274-1440`; living-host/collapse triggers at `006_independence_wave_focus_triggers.txt:211-249` | PASS structurally | Host survival and collapse are represented. Route-specific names/institutions remain shared/static, and no host/war/access reachability sweep was run. |
| Regional ambition and expansion | Regional survey and follow-on lane `006_independence_wave_focus.txt:1456-1520`; 14-region selectors in `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt:52-70` and effects `006_independence_wave_focus_effects.txt:600-627` | PASS for adaptation, PARTIAL for depth | Transport and ambition titles change across all 14 regions, with region-specific family flags. Government, patron, and former-host focus titles do not receive equivalent dynamic selectors. |
| League/network | Network/league chain `006_independence_wave_focus.txt:1528-1705`; decisions own votes/proclamation; league gate in `006_independence_wave_focus_triggers.txt:291-304` | PASS | Focuses improve network/league ledgers and unlock the decision surfaces. A complete multi-country AI/league scenario sweep is still missing. |
| Formable preparation | Generic preparation `006_independence_wave_focus.txt:1712-1762`; `can_open_independence_wave_formable_branch` at `006_independence_wave_focus_triggers.txt:285-289`; FORM-03-specific branch `:1765-1901` | PARTIAL | Generic discovery/congress/terms/integration focuses exist and decisions consume their flags, but bespoke focus depth is demonstrated only for FORM-03. The 48-family registry requires family-by-family reachability and post-formation integration proof; no such sweep is recorded. |
| Hidden high-chaos route | Hidden reveal and lane at `006_independence_wave_focus.txt:1904-2018`; gate in `006_independence_wave_focus_triggers.txt:263-277` | PASS structurally | `allow_branch` and `available` keep the lane hidden until ambition/open-sovereignty/world-collapse conditions. AI and invalidation behavior are not scenario-tested. |
| Signature/package focus modules | Package branches in `006_independence_wave_focus.txt:1971-2877`, COR extension `:3047-3115`, imported IW-043/IW-058, IW-093/IW-098, and Pacific shared files | **FAIL for package-wide completion** | Bespoke focus groups exist for a bounded set (SCO, WLS, AJX, BRI, AFX, RHI, BAY, ARX, ASX, COR, HBX, HAW, and imported signature branches), but no AGX/Frisia focus IDs exist. IW-007/AGX is in the current nine-package content gate and therefore reaches only the generic framework/overlay plus decisions. Most of the 206 accepted registry rows have no demonstrated focus-specific route module. |
| MCP layout and visual readability | `hoi4.focus_inspect`/`focus_render` artifacts above; crossings cluster at source `006_independence_wave_focus.txt:280-297`, `319-336`, `441-460`, and `501-524` | **FAIL** | Resolve the 14 blocking crossings with authored endpoint/coordinate changes while preserving prerequisite and mutual-exclusion semantics. |

## Missing, simplified, or unwired content

- Economy capstone continuation is the clearest unwired surface. The capstone flag is written and cleared but never consumed; the focus claims an independent treasury while granting only generic stabilization and an industry technology bonus.
- Package differentiation is incomplete relative to the accepted registry. AGX is currently admitted but has no AGX focus branch; IW-043/IW-058, IW-093/IW-098, and some Pacific branches are present in source but are not in the current nine-ID attestation gate, so their focus reachability is not a current runtime fact.
- The shared overlay has dynamic title selectors for transport, economic program, military program, ambition, and the two internal power centers. Government settlement, patron, and former-host focus names remain static, despite Part 5 requiring overlay-specific institutions, route naming, localisation tone, and AI behavior.
- Formable preparation is generic and FORM-03 is bespoke. The registry’s 48 families are not accompanied by a recorded focus reachability/post-formation sweep.
- MCP layout validation fails even though parser/icon/localisation/reference checks are clean. This is a release-blocking presentation problem, not a reason to alter the route graph.

## Icon coverage table

| Surface | Evidence | Verdict |
|---|---|---|
| Main and imported focus/shared-focus blocks | 294 blocks; 121 unique icon references; all sprite names and `_shine` counterparts resolve in `interface/006_independence_wave.gfx` and package `.gfx` files | PASS for asset existence/wiring |
| Route-family distinctness | Generic families repeat heavily (former-host, army integration, infrastructure, founding administration, league congress, high-chaos, and regional formable icons); ASSET-007..019 in `006_asset_family_registry.csv` call for distinct adapted route-family treatment | PARTIAL readability risk, not a missing-asset blocker |

## Localisation and reward mismatch list

- Localisation key coverage is a PASS: all 294 focus/shared-focus IDs have title and description keys, and the dynamic selectors resolve to existing keys.
- Dynamic route naming is incomplete: only transport/economy/military/ambition and internal power-center titles vary by metadata. Government, patron, and former-host route titles remain generic/static.
- `independence_wave_create_independent_treasury` (`006_independence_wave_focus.txt:377-389`) names and describes a treasury but has no treasury-specific flag, idea, decision unlock, ledger update, or visible treasury effect. Its current reward is a generic industry bonus plus stabilization and the inert capstone marker; this is a focus-name/reward mismatch against Part 4’s continuing-decision requirement.
- Military and diplomacy capstones do have explicit decision hooks (`unlock_professional_army` and `unlock_foreign_service`), so the economy gap should be fixed to the same standard rather than weakening those routes.
- Generic reward helpers in `006_independence_wave_focus_effects.txt:302-437` vary legitimacy, recognition, capacity, security, instability, network, and league ledgers; no repeated free-division reward or missing `_tt` key was found in this read-only pass.

## AI behavior gaps

- Every focus/shared-focus block has an `ai_will_do` block, so declaration coverage is a PASS.
- Dedicated strategy files provide route-aware policies for the bounded package tags (including current admitted SCO, BRI, AGX, RHI, BAY, AJX, ARX, ASX, and HBX, plus additional dormant package tags), and the source contains route/host/war-state modifiers.
- There is no recorded route-selection or invalidation sweep across the 206 registry identities, 14 regions, former-host states, patron/league states, or 48 formable families. Generic focus `ai_will_do` values therefore do not prove the Part 7 requirement that invalid routes are hidden/bypassed/zero-weight and valid routes are selected under resource safety.
- The economy capstone’s missing decision hook also leaves AI with no route-specific continuing economic action to evaluate after the focus completes.

## High-priority bounded fixes

1. Repair the 14 MCP blocking layout diagnostics by moving authored endpoints/coordinates in the crossing clusters; preserve all prerequisite, OR-block, and mutual-exclusion semantics.
2. Wire `independence_wave_create_independent_treasury` to a real continuing decision/mission or prove an existing consumer, and align its tooltip/reward with that hook.
3. Decide the admitted-package contract: add a narrow AGX focus module (and its AI/localisation/icon proof) or explicitly queue AGX as not focus-complete before claiming the current nine-package gate is complete. Do not silently broaden the whole registry in this patch.
4. Add or queue dynamic government, patron, and former-host overlay naming/institution surfaces so Part 5’s regional overlay contract is evidenced beyond transport/economy/military/ambition titles.
5. Run read-only focus reachability and weighted-AI scenario sweeps for each currently attested package, all 14 regions, living/collapsed hosts, league routes, and representative formable families before a completion claim.

## Remaining route risks and blockers

- No live Hearts of Iron IV session was launched; runtime consumer validation remains with the parent/user.
- The current gate admits nine package IDs, while the source registry and specs describe a much larger differentiated universe. Current source gate lines are the reliable scope; older handoffs must not be used to claim completion.
- MCP layout validation remains failed until the crossing clusters are authored out.
- The economy capstone’s marker-only implementation is an explicit acceptance failure, not merely an untested possibility.

## Simplifications and omissions

This audit intentionally made no gameplay edits and did not redesign route families. The completion verdict remains FAIL because the economy continuation hook, package-wide focus differentiation, overlay naming breadth, route/AI sweeps, and MCP layout validation are unresolved.
