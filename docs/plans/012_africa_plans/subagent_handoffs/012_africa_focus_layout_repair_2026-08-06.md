# Event 012 Africa Focus Layout Repair Handoff

Status: narrow layout patch complete, with residual MCP diagnostics handed to the parent agent for review.

Scope: `common/national_focus/012_africa_continental_focus_tree.txt` opening-lane coordinates only. Concurrent parent edits that translate the nine regional overlay lanes are visible in the same working file but are not attributed to this handoff. No route mechanics, rewards, icons, localisation, AI weights, decisions, or UI were changed here.

## Changed files and focus identifiers

Changed file: `common/national_focus/012_africa_continental_focus_tree.txt`.

Changed focus coordinates:

| Focus id | Before | After | Reason |
| --- | --- | --- | --- |
| `africa_repair_host_administration` | `x = 29, y = 1` | `x = 27, y = 1` | Align the repair-to-corridor chain with `africa_choose_first_corridor` and remove the opening detour. |
| `africa_build_host_coalition` | `x = 35, y = 1` | `x = 43, y = 1` | Align the coalition-to-partner chain with `africa_select_first_partner` and `africa_write_first_guarantee`. |
| `africa_prepare_host_security` | `x = 41, y = 1` | `x = 30, y = 1` | Keep the security prerequisite near `africa_secure_first_corridor` and reduce the long security connector. |
| `africa_protect_first_partner` | `x = 40, y = 4` | `x = 43, y = 4` | Align the partner proof chain with the guarantee lane. |

The temporary trial of `africa_secure_first_corridor` at `x = 35` was reverted because it increased node intersections and horizontal span. The final source retains its parent-baseline `x = 30` coordinate.

## Route behavior before and after

Before and after the patch, the four opening focuses retain the same prerequisites, availability gates, `cancel_if_invalid` behavior, completion rewards, and `ai_will_do` blocks. The patch changes only their visual coordinates, so the repair lane still feeds `africa_choose_first_corridor`, the coalition lane still feeds `africa_select_first_partner`, both lanes still converge at `africa_prove_the_first_obligation`, and the shared charter sequence still begins at `africa_publish_the_first_obligation`. The nine regional overlay lanes, six grounded constitutional routes, hidden Covenant lane, support lanes, and formation lanes are unchanged behaviorally.

## MCP evidence

Baseline parent layout evidence was inspect revision `91d9113e097ff3e315b02cdc2bcd5ee6f5d4765f43680eba4fde87781936542f`, artifact [focus-inspect.91d9113e097ff3e.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7093461efb4a7994bbf855382ffaddd0bf3c5ef274f49e6aa9b122e1f17de5ac/9301d52b9ef097691c0408e73a6de39cd1eb300bf8f8fa5ffee992d081d6e876/focus-inspect.91d9113e097ff3e.json).

Final focus inspection used workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `8f18248d78f6a40b02a171fbba295ede6524a45827eb62cf06b1640565ce34c3`, layout hash `1c6a4d7f2ba8282e534f979913dc6b3efb8f2dc7ca852ae9dde74704234950d3`, and artifact [focus-inspect.8f18248d78f6a40b.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f68afe4b3e8f91f7584afbd34e89dd794baa050f01eee2158aadca8022f6f8dd/4116c27a9eebeca7c8cb82c47eaf1853b2378e89086bb4ee87feb7dc2fd1bfa2/focus-inspect.8f18248d78f6a40b.json).

| MCP metric | Baseline | Final | Result |
| --- | ---: | ---: | --- |
| Focus nodes | 276 | 276 | Preserved. |
| Resolved titles | 276 | 276 | No localisation resolution loss. |
| Connectors | 348 | 348 | Route graph preserved. |
| Connector crossings | 61 | 61 | No change; residual fan crossings are described below. |
| Node intersections | 51 | 50 | One fewer intersection. |
| Long connectors | 36 | 35 | One fewer long connector. |
| Total horizontal span | 1696 | 1684 | Reduced by 12 columns. |
| Total vertical span | 568 | 568 | Preserved. |
| Same-row spacing conflicts | 1 | 1 | One West Atlantic/opening conflict remains. |
| Total diagnostics | 268 | 262 | Reduced, while validation still reports 14 blocking diagnostics. |

Final structural render succeeded at `reviewScale = 0.5`, dimensions `15400 x 2664`, with artifacts [focus HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb85e5e2129da17f98e5a0e6cbba733b7819d936274cf09ec1773c6be9a34925/ab2b512101a2a38690ebd0e32f3931e1f6a76dd468eda19c5c61387d7ec45e18/africa_continental_focus_tree.focus.html), [focus SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdb2f1fe77473f6f7bbb766c245d2f63ad136dfdaf033c2ea4575b0e9d801e4d/458e9c8f7ade88cd2ee0ee9128261035ea898687a54265716995ddaf25cedbb5/africa_continental_focus_tree.focus.svg), and [focus JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2cde29b0f316e1784eb967fafe9368cfc1918a2e0e951844465e4868f74745a1/2222e40026885117585f3f91a86faff47463906c7b1d2b78a55b862f12bb83f9/africa_continental_focus_tree.focus.json).

The required raster review also succeeded at `reviewScale = 0.25`, dimensions `7700 x 1332`, with PNG artifact [africa_continental_focus_tree.focus.png](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92bb5d980aaf6ebd935f8e6c1bc1b4b79ddf029050b5e98b9d37788b11acdd94/254cb9fb75683b78863d040609bef6857195802221c02a95b4446cb6a99b49a2/africa_continental_focus_tree.focus.png).

Skipped meaningful validation: no HOI4 process or save was launched, because live gameplay validation belongs to the parent/user; no probability audit was run, because no AI weight or probability-bearing value changed.

## Route coverage table

| Surface | Source range or identifiers | Coverage result |
| --- | --- | --- |
| Shared protection-first opening | `012_africa_continental_focus_tree.txt:42-317`, from `africa_identify_host_problem` through `africa_choose_constitutional_principle` | 16-focus opening remains connected; only four coordinates changed. |
| Regional overlays | `:322-1422`, nine six-focus lanes for Maghreb-Sahara, West Atlantic, Sahel-Lake Chad, Nile-Horn, Congo Basin, Great Lakes, Swahili-Indian Ocean, Southern Africa, and Madagascar-Islands | 54 focuses remain present; each lane retains its `allow_branch` gate, prerequisites, six-step rewards, and capstone. |
| Host origin signatures | `:1428-1560`, `africa_host_signature_*` and `africa_compact_signature_*` | Full, promoted, and compact signature slots remain present and connected. |
| Grounded constitutional routes | `:1565-5675`, roots `africa_federal_representation_before_merger`, `africa_republic_civic_status_and_accession`, `africa_crowns_recognise_living_crowns`, `africa_union_coalition_of_revolution`, `africa_command_define_the_mandate`, and `africa_confederation_reserve_sovereignty` | Six route families remain present with route-specific prerequisites, mutual exclusions, rewards, and AI blocks. |
| Hidden Covenant route | `:5705-6270`, beginning `africa_covenant_recognise_the_impossible` | Covenant transformation lane remains present; no changes were made. |
| Shared support and post-formation lanes | `:6274-7251` and `:7252-end` | Route-sensitive support, Charter League formation, ratification, and final settlement surfaces remain in the source graph. |

## Missing or simplified content

- No focus route, focus identifier, prerequisite, mutual exclusion, reward hook, decision hook, formable hook, or route gate was removed or simplified by this patch.
- The MCP planner reports `branchCount = 0` because it evaluates all mutually exclusive overlay edges as one static graph. The source still contains the runtime `allow_branch` predicates; this is an evidence limitation, not a gameplay route deletion.
- The final inspect still reports 14 blocking diagnostics. These are residual static layout and repeated-reward diagnostics, not missing route nodes.
- Full-scale raster was not attempted after the final patch because the known 30,864-by-5,392 dimension ceiling blocks it; the scaled raster above is the successful visual evidence.

## Icon coverage table

| Coverage check | Evidence | Result |
| --- | --- | --- |
| Focus icon references | `012_africa_continental_focus_tree.txt` and `interface/012_africa.gfx` | No missing-icon diagnostic in inspect, render, or raster. |
| Loaded icon families | MCP scanned 13 DDS families: `aid_and_relief`, `army_common_reserve`, `charter_law`, `continental_representation`, `host_legitimacy`, `host_proclamation`, `protection_guarantee`, `rail_corridor`, `regional_congress`, `resource_sovereignty`, `rival_bloc`, `road_corridor`, and `volunteer_intervention` | 13/13 icon families resolved. |
| Changed icon ids | None | No asset or `.gfx` edits required. |

## Localisation and reward mismatch list

- Localisation: MCP resolved all 276 focus titles, and the scanned files include `localisation/english/012_africa_focus_l_english.yml` and `localisation/english/012_african_union_l_english.yml`. The coordinate-only patch changed no localisation key.
- Reward analyzer warnings: `FOCUS_REPEATED_GENERIC_REWARD` appears for six milestone patterns across the nine overlay lanes (`settle_authority`, `build_corridor`, `bind_partner`, `settle_local_terms`, `convene_council`, and `prove_mandate`). This is a static-pattern false positive for the current implementation, not a reward mismatch: `common/scripted_effects/012_africa_effects.txt:1625-1714` receives the temporary overlay step, applies region-specific flags for all nine overlays, and then calls `africa_apply_constitutional_overlay_payoff`; `common/scripted_effects/012_africa_focus_route_effects.txt:111-192` maps each milestone to distinct major/minor constitutional axes for every grounded route and Covenant replay path.
- No dummy reward, generic political power, or reward dust was added to suppress the analyzer. The existing region and constitution helpers are the correct differentiation surface.

## AI behavior gaps

- No AI behavior gap was found in the touched opening focuses. A source census finds 276 focus `ai_will_do` blocks for the 276 focus nodes, and MCP reported no missing-AI diagnostic.
- No AI weight or probability-bearing modifier was edited, so the mandatory probability-auditor compare was not applicable to this coordinate-only patch. Parent review should reroute probability inspection if later layout work changes any `ai_will_do` factor.

## High-priority fixes and remaining risks

1. P0 parent decision: accept or redesign the static opening fan. MCP still reports connector-through-node warnings from `africa_identify_host_problem` to the nine mutually exclusive overlay roots and to signature branches, plus the long connector to `africa_maghreb_sahara_face_divided_sovereignty` (`:321-340`). A broader redesign would need to move the shared root or introduce a deliberate visual staging lane and is outside this narrow patch.
2. P1 parent visual review: the West Atlantic lane still crosses the security-to-corridor connector and leaves `africa_build_first_corridor` one column from `africa_west_atlantic_open_port_and_inland_route` on row 3. MCP marks the endpoints fixed and gives no movable focus ids. Moving `africa_secure_first_corridor` to `x = 35` was tested and reverted because it increased node intersections and horizontal span; no safe one-focus alternative was found.
3. P2 reward diagnostics: retain the existing helper-backed region and constitution differentiation. Do not add cosmetic rewards solely to silence the repeated-pattern warning unless the helper is actually shown to collapse at runtime.

No route, icon, localisation, reward, or AI simplification was made. Parent integration remains required because the MCP validation check is still false for the residual diagnostics above.
