# Event 006 Reclamation Doctrine Connector Audit

Disposition: unresolved; no focus-source patch was retained because the tested coordinate-only alternatives introduce layout errors or intersect existing choice nodes.

## Scope and route coverage

This audit covers only the direct-tree connector from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine` in `common/national_focus/006_independence_wave_focus.txt`.

| Route segment | Source coordinates | Route relationship | Layout finding |
| --- | --- | --- | --- |
| `independence_wave_adopt_military_archetype_program` → `independence_wave_adopt_reclamation_doctrine` | Parent `(42,7)`; child `(32,8)` | Child requires the parent; it is mutually exclusive with `independence_wave_adopt_border_defense`. | Direct relationship is present, but the connector spans 10 columns and 1 row, exceeding the inspector thresholds of 8 horizontal columns and 10 Manhattan units. |
| `independence_wave_adopt_reclamation_doctrine` → `independence_wave_found_professional_defense_institution` | Child `(32,8)`; capstone `(40,9)` | The capstone has this focus in its third OR prerequisite group. | This downstream placement constrains moving reclamation to row 9 or lower: the capstone would no longer be below its prerequisite. |

The source relationship, prerequisite blocks, mutual exclusion, rewards, AI block, identifiers, and original coordinates remain unchanged. No complete Event 006 route-coverage audit or spec comparison was in scope.

## Why the connector remains unresolved

At row 8, the neighboring direct focuses occupy x positions 34, 36, 38, 40, 42, 44, 46, 48, and 50; x=32 is the free adjacent-row position for this route. Moving the focus to x=34,y=8 would collide with `independence_wave_confirm_civilian_control` at `(34,8)`, while x=33 would remain outside the MCP horizontal-span threshold and violate the reported two-column same-row spacing rule.

Moving the focus to row 7 would place it at or above its prerequisite. A temporary candidate at `(34,7)` produced `FOCUS_LAYOUT_PARENT_NOT_ABOVE`, `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`, `FOCUS_AVOIDABLE_CONNECTOR_CROSSING`, one crossing, and two node intersections; the related connector-through-node warnings named the `independence_wave_adopt_reclamation_doctrine` → `independence_wave_found_professional_defense_institution` connector crossing the `independence_wave_grant_military_autonomy` and `independence_wave_raise_mass_reserve` nodes.

A temporary candidate at `(36,9)` removed the long-connector warning but produced `FOCUS_LAYOUT_PARENT_NOT_ABOVE` for the reclamation-to-capstone relationship and two `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE` warnings where the incoming connector intersected `independence_wave_raise_mass_reserve` and `independence_wave_build_professional_core`.

Both candidate edits were reverted. A safe repair appears to require a wider local layout adjustment involving at least one neighboring row-8 focus or the existing capstone placement, which exceeds the authorized one-connector coordinate scope.

## MCP evidence

The before and final restored inspections both reported 184 focus nodes in the inspected tree scope, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, 196 connectors, zero crossings, zero node intersections, and one long connector. The before revision was `6f16e4a833724add10b09756d6cd33f8042d902d0821ca7e387ea716490f6a18`; the final restored revision was `5c39ef97d5f03174339f79664a3f4e475a539e33f9b3429d68948fc53e9b99eb`.

The final render has the same layout hash and HTML, SVG, and JSON artifact hashes as the before render. Useful artifacts: [before inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/130beae437ee611bebcc39e3f97e785fe055b18b7c5a0719e2acb33439954363/aa9c19bfc022aa41e96889d4c53edb32d2c208460ec19369c1238b72d1ce1b8e/focus-inspect.6f16e4a833724add.json), [final inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba9d51567cb460610d17c40847a155afe537ffb647ae46abd979d8552a9bc3ca/130e441a3ddd19e6b2ec7af6ca7be3df3051c92ed21fe9b6e2f811a4a431ca97/focus-inspect.5c39ef97d5f03174.json), [final rendered SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/8523858072b879b03f0a23fa502d4f8e47254cb2f3dcb457c91e4581aad90b8f/independence_wave_focus_tree.focus.svg), and [final rendered HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c46038276d6f758dfb7fb380d96b1e220b6cc2ecb16e0a0147ac0a3473d277fd/afd89269d87a8c47f558a41778791849c535a09d802ab3b010c1d6e8f03012dd/independence_wave_focus_tree.focus.html).

The candidate at `(34,7)` is evidenced by [its inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bd01de078e33b09f66e12ad09d557598c663c82a271b5740d943892a5423a3b/d2af7f1c6a8796c318c1f67336f73f1d8352b3182bb9336cb955ebafa6318df6/focus-inspect.7c139cbc81966f23.json), and the candidate at `(36,9)` by [its inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed8bbf4a5d91579dfcf6a16cec7b868ad1b2b2b0e266d05992c823d180e8a40a/ed7bd15fff223e6e0683ae8c29fa832914747f9f46499c62239149c4c63ab845/focus-inspect.07bd8808467d0aee.json).

The live `hoi4.focus_rewrite` schema rejected an authored rewrite without a plan with `MCP error -32602: ... plan is required unless layoutMode is compact at plan`; an empty authored plan was rejected with `MCP error -32602: ... Invalid input at plan`. The only exposed no-plan rewrite path is whole-tree `compact`, which was not run because it would arrange all 184 focus nodes in the inspected tree scope instead of preserving their accepted coordinates. No per-focus coordinate patch form was exposed by the live schema.

The inspector’s initial source inventory was truncated at 64 of 92 paths. The accepted imported shared-focus omission remains in effect: these artifacts do not establish layout evidence for imported shared focuses, including the DON set.

## Local reference evidence and route gaps

The offline National focus modding snapshot at `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, lines 254–280, describes focus x/y positions, relative positions, and prerequisite layout semantics; its SHA-256 is `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`.

The installed vanilla precedent `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/argentina.txt`, lines 107–116, shows a focus whose prerequisite is positioned using `relative_position_id`; its SHA-256 is `E7B06A02BFE938AE96C455FB13923C23A160178E74A1733CF92A7C1A38ED2A7E`. It supports placing dependent focuses relative to route anchors but does not establish that a same-row or intersecting alternative is safe.

The installed `documentation` directory contains no dedicated national-focus coordinate/layout document. The inspected `documentation/effects_documentation.md` section `load_focus_tree` at lines 4770–4788 covers tree loading and shared-focus completion, not focus geometry; its SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

The connected tool list did not expose `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup`; local offline wiki and installed-game files were therefore read directly. No Paradox wiki web access was used.

## Icons, localisation, rewards, and AI

| Focus | Source icon reference | Coverage result |
| --- | --- | --- |
| `independence_wave_adopt_military_archetype_program` | `GFX_goal_independence_wave_army_integration` | Source reference unchanged; asset registration was outside this connector-only audit. |
| `independence_wave_adopt_reclamation_doctrine` | `GFX_goal_independence_wave_high_chaos_sovereignty` | Source reference unchanged; asset registration was outside this connector-only audit. |

Localisation and reward consistency were not audited because neither was in scope, and no keys or rewards changed. AI route behavior was not evaluated; both focuses’ `ai_will_do` blocks remained unchanged, no focus weights were edited, and no probability analysis was required for this coordinate-only attempt.

The only other diagnostic in the restored direct-tree inspection is the unrelated game-source warning `FOCUS_LOCALISATION_REFERENCE_MISSING` for `continuous_restrict_freedom_desc` at `game:common/continuous_focus/generic.txt:498–525`.

## Parent compact-rewrite attempt and restoration — 2026-09-26

The parent tried `hoi4.focus_rewrite(layoutMode = compact)` as a whole-tree cleanup after the isolated coordinate attempts failed. It rewrote coordinate values across the 184 direct focus definitions, created `common/national_focus/006_independence_wave_focus.focus-plan.json`, retained the reclamation long connector, and added sibling-anchor-deviation and asymmetry diagnostics (compact layout hash `69a59e16210cd8f863ea1a640d4b2261c39660bc1fabaca70eadbc17ad48de38`, diagnostic count 7). The parent rejected this broad layout result.

The parent restored only the rewrite-generated coordinate hunks with a reverse zero-context patch, preserved the pre-existing IW-039 import and three KAR/CRI/KUB prerequisite edits, then removed the untracked tool-generated focus plan whose source hash no longer matched the restored tree. The full source SHA-256 returned exactly to the pre-rewrite value `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2`; `git diff` again contains only those pre-existing import/prerequisite changes.

Post-restoration `hoi4.focus_inspect` revision `2431d009b7838ba05b99c2ba9c7c27f49d8e3c5f827bc525b24f7793f65f321f` and matching `hoi4.focus_render` return the original layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, 184 direct nodes, 196 connectors, zero crossings/intersections, and one long connector. The original source was restored; no focus source change is retained from this parent attempt. A future repair requires a complete nearby lane-layout plan that checks all affected prerequisite order and connector crossings before any source write.

## Files and final source review

Only this handoff was authored by this subagent. The focus source SHA-256 was `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2` both before the candidate edits and after restoration. Its existing working-tree diff still contains concurrent DON shared-focus imports and three prerequisite-expression edits; these were preserved. The final diff contains no change to either audited focus’s coordinates, prerequisite, reward, AI block, icon, or identifier.

Meaningful validation consisted of before/candidate/final `hoi4.focus_inspect` and `hoi4.focus_render` runs. The final state reproduces the original long-connector warning and layout hash. No game launch or broad route, localisation, AI-balance, or imported-focus validation was performed.

## Parent follow-up

Disposition: unresolved. To remove the warning, the parent must authorize a broader nearby coordinate change and review all affected connectors, nodes, and the reclamation-to-capstone relationship through matching MCP inspect/render evidence. No route, focus id, reward, prerequisite, AI weight, localisation, or icon change was made by this handoff.
