# Event 015 Focus Tree Layout Repair Handoff

## Verdict

**PASS for the coordinate-only layout assignment.**

The 122-focus tree now reads as a compact centered opening, a single five-route commitment band, interlocked shared-institution rows, and a centered formation tail. The layout-only pass materially reduced every audited layout metric, removed all connector-through-node cases involving the opening/commitment band, and removed all connector-through-node cases incident to the five route openers. Focus IDs, prerequisites, rewards, triggers, AI, localisation references, and other gameplay semantics were not changed.

## Owned files

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
  - Replaced the fixed `x`/`y` coordinates for all 122 focuses.
  - Updated `initial_show_position` and `continuous_focus_position` to match the repacked tree.
  - No focus ID, prerequisite, reward, trigger, AI weight, localisation key, cost, icon, or gameplay field was changed.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_tree_layout_repair.md`
  - Added this evidence and ownership handoff.

No other file was edited by this layout assignment. No file was staged or committed.

## Layout structure

- Recovery and survey remain the centered top trunk.
- The two founding-institution branches and Interpretive Congress remain compact immediately below it.
- The five political readings occupy one ordered commitment row:
  - Consent: `x = 22`
  - Common Provision: `x = 24`
  - Guardianship: `x = 26`
  - Closed Store: `x = 28`
  - Open Humanism: `x = 30`
- `utopia_manifesto_the_country_as_a_question` is at `x = 28`, so every political opener is within six columns of the hub.
- Stores and Garden support enter from the left; Necessary Ground, Callings, and Defense enter from the right; shared route institutions occupy the center instead of five isolated columns.
- External Need, association, regional-order, crisis-correction, and stewardship nodes converge into the lower proof band.
- Proof, proclamation, identity, and post-formation focuses form the centered tail at rows 13-16.

This preserves the accepted six-stage top-to-bottom reading while allowing bands four and five to visibly interlock, as required by the architecture specification.

## Before/after metrics

Baseline is the fresh re-audit render recorded in `focus_tree_reaudit.md`. Final values are from the fresh final `hoi4.focus_inspect` artifact listed below.

| Metric | Before | After | Reduction |
| --- | ---: | ---: | ---: |
| Focuses | 122 | 122 | unchanged |
| Connectors | 170 | 170 | unchanged |
| Connector crossings | 86 | 50 | 41.9% |
| Connector-through-node intersections | 41 | 7 | 82.9% |
| Long connectors | 26 | 20 | 23.1% |
| Width | 80 columns | 55 columns | 31.3% |
| Height | 30 rows | 17 rows | 43.3% |
| Maximum horizontal span | 43 | 20 | 53.5% |
| Maximum vertical span | 14 | 4 | 71.4% |
| Maximum Manhattan span | 45 | 21 | 53.3% |
| Total horizontal span | 746 | 653 | 12.5% |

The final tree has the required same-row spacing of two columns and no parent-order, coordinate-conflict, visible-overlap, or same-row-spacing diagnostics.

## Opening and route-band proof

- Connector-through-node cases whose unrelated node lies in rows 0-6: **0**.
- Connector-through-node cases incident to any of the five route openers: **0**.
- Re-audit concrete case `count_houses_and_hands -> homes_near_work`: **0** through-node diagnostics.
- Re-audit concrete case `agriculture_for_all -> every_hand_knows_the_soil`: **0** through-node diagnostics.
- The earlier `every_hand_knows_the_soil` intersections with `cooperative_land_trusts`, `constitution_of_provision`, and `voluntary_commonwealth_league`: **0**.

## Semantic integrity proof

The baseline and final inspector plans were normalized by removing only focus positions, tree viewport positions, provenance, and source-location offsets. The normalized plans are byte-identical:

- Baseline semantic SHA-256: `DA69C3371FD0B0F5DA72308204EC770D259DFA4304DCA4753DA43B83FD0A667E`
- Final semantic SHA-256: `DA69C3371FD0B0F5DA72308204EC770D259DFA4304DCA4753DA43B83FD0A667E`
- Focus-ID order and set: identical, 122/122.
- Final focus source SHA-256: `460B233727B02136E26FBDF796DBE97246E6C3EA5D3445A2EBB3B69EF36F3B69`

## Fresh artifacts

### Baseline

- Inspect JSON: `hoi4-agent://workspace/chaos_redux/artifact/cebaf534a0779709a489f4ab6f4973a7b787094d27c9554087620d76df57e7c0/5593adaf1a74ef630765a8123ef8e31ebeb1bbfd0298ef856be93dbcc04371eb/focus-inspect.d89c516652e29a8b.json`
- Rendered PNG: `hoi4-agent://workspace/chaos_redux/artifact/01d6b1ba7803c7eb6d5718de6ad204cff341540c7481a86ba570e3896f58f9ec/7e3ec6936a0ebcd91d78e87481078257d5ac63c7247925bb7b3cbf224b557c11/utopia_manifesto_tree.focus.png`
- Baseline focus source SHA-256: `BAD7F93468CDEC937324C711F835145C30A000CB3714585BA64A62F847F12BE2`
- Baseline layout hash: `4DC9D30A7C5A153BB448531D9AEF4B1DC7150D2CE332DF940C3A58574FF484B3`

### Final

- Inspect JSON: `hoi4-agent://workspace/chaos_redux/artifact/f234baaf51ae2f8da6217643d6c14ef999eef70a0f4b06e1c2638d774d164cc2/9cc09378241c3c62b1f24973eedde3de8ba8d93bc84e24728581737428d05b71/focus-inspect.bff80712ea9fb68a.json`
- Rendered HTML: `hoi4-agent://workspace/chaos_redux/artifact/b57e31b6b128219e58923e823122e2e064edf320402bdcf8088f64daf3bf5569/b496c5eaea50f651020526b5dc558733c3ac4c614cb35c6133e8df28b6389a5b/utopia_manifesto_tree.focus.html`
- Rendered SVG: `hoi4-agent://workspace/chaos_redux/artifact/b33b8502afb7e48f40987227075cd473f7b42a8ac03d57b26326fb444720fc05/0cec5d0411cae97cdf9bca5b0fc886088feb231ff5b779559dbd6982e5ebf395/utopia_manifesto_tree.focus.svg`
- Rendered PNG: `hoi4-agent://workspace/chaos_redux/artifact/eeae071bef34284deb69ec79a8159e2f2d26107ff849ec6a58f005775237d430/315b43920debfec56e7eb48d5a9641a9ffe85fc77bbd9ce1de0ab0f246c76b89/utopia_manifesto_tree.focus.png`
- Render JSON: `hoi4-agent://workspace/chaos_redux/artifact/8ac584fa0a67f8b5fb4898225490a3eb1be6ae293d0112c53822add080865c85/22068e09bb7f3b260924b4955883b45d54e0bb05ae6a9264cc00b5cb2a057c52/utopia_manifesto_tree.focus.json`
- Final layout hash: `248B31C1CBDCE685AF214EC1665BD6F38037306C59FAE3805B9E6876A27C6DFF`
- Final PNG SHA-256: `EEAE071BEF34284DEB69EC79A8159E2F2D26107FF849EC6A58F005775237D430`
- Final render size at review scale 0.5: `4904 x 1046`.

The final PNG was reviewed directly at normal review scale after the last coordinate change. The opening trunk is centered, the five route openers are contiguous and ordered, shared branches visibly interlock, and the formation tail returns to the center.

## References and skills used

- Skills: `hoi4-focus-trees`, `chaos-redux-subagents`.
- Offline wiki core pages required by `AGENTS.md`, plus `National focus modding - Hearts of Iron 4 Wiki.md`.
- Vanilla documentation under `Hearts of Iron IV/documentation`, including script concepts and focus-tree load/trigger references.
- Vanilla generic and Spain focus-tree coordinate/prerequisite precedents.
- Accepted Event 015 focus architecture specification and the fresh focus-tree re-audit.

## Residual warnings and boundaries

- Seven connector-through-node warnings remain in the lower shared-institution/formation convergence area. None is in the opening or route-commitment band and none is incident to a route opener. This is an 82.9% reduction from the audited 41.
- Fifty connector crossings and twenty long connectors remain in the 170-edge interlocked graph. They are materially reduced from 86 and 26, respectively; removing them entirely would require weakening the required interlock or changing prerequisite topology, which was outside this coordinate-only ownership grant.
- The inspector still reports 14 partial icon-reference diagnostics and one localisation-reference diagnostic. Those predate this coordinate pass, are not layout fields, and were not edited.
- The optional automatic compact rewrite was tested first and returned `FOCUS_COMPACT_QUALITY_BLOCKED` with no changed files. The final layout is the manually authored, inspected, and rendered coordinate solution.
- Event 15 lifecycle and route-AI findings in `focus_tree_reaudit.md` remain parent-owned and were deliberately not touched.

## Simplifications, omissions, and blockers

No requested layout route, focus, band, or coordinate surface was omitted. No gameplay fallback or prerequisite simplification was used. There is no blocker within the coordinate-only assignment.
