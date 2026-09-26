# Event 006 reclamation-doctrine connector follow-up — 2026-09-27

**Disposition:** unresolved; the reviewed coordinate trial was rejected and the focus source is restored.
**Scope:** this handoff covers the direct-tree military lane around `independence_wave_adopt_reclamation_doctrine` and its professional-defense convergence.
The accepted root-level shared-focus architecture, focus graph, rewards, prerequisites, AI, localisation, icons, and identifiers remain unchanged.
Event 006 remains **HOLD / PARTIAL**.

## Acceptance and source baseline

The user approved the complete Event 006 focus-tree design and explicitly retained imported `shared_focus` definitions without direct-focus fallback copies.
Part 4 assigns exact x/y positions to implementation while retaining the accepted focus routes and requires readable, short connectors.
The 2026-09-26 [connector handoff](006_event6_reclamation_doctrine_connector_repair_2026-09-26.md) remains the prior candidate history; this follow-up adds the current MCP evidence and records one additional rejected trial.

The restored source file `common/national_focus/006_independence_wave_focus.txt` has SHA-256 `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2`, matching the previously recorded pre-rewrite source hash.
The restored coordinates are parent `independence_wave_adopt_military_archetype_program` at (42,7), `independence_wave_adopt_reclamation_doctrine` at (32,8), `independence_wave_preserve_independent_command` at (50,8), and convergence focus `independence_wave_found_professional_defense_institution` at (40,9).

## Current restored MCP evidence

The read-only `hoi4.focus_inspect` result is `FOCUS_INSPECTED` at revision `3dbe39ecfad75054`, with 184 direct focuses, 196 connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, zero crossings, zero node intersections, and one long connector.
The only Event 006 layout diagnostic is `FOCUS_LAYOUT_LONG_CONNECTOR` from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`, spanning 10 horizontal columns and 1 row with thresholds 8 horizontal, 4 vertical, and 10 Manhattan units.
An unrelated vanilla continuous-focus localisation warning remains for `continuous_restrict_freedom_desc`.
The matching read-only `hoi4.focus_render` returned `FOCUS_RENDERED` with the same layout hash at 21,424 by 2,440 pixels; SVG hash `5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109`, HTML hash `c46038276d6f758dfb7fb380d96b1e220b6cc2ecb16e0a0147ac0a3473d277fd`, and JSON hash `04e2730212620f6e530626d1761c46db81a52369b99db0b53bcc38fc82654660`.
The artifact URIs are [inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd85b30d7d6a4863eb126cf4e1dd10cbc08a3e4cfd21f180de4376bf1a9899c2/7fe6fd24a5c27138b65af5ec4b4c3100285963622dca5c703fcc7d2edf1bce46/focus-inspect.3dbe39ecfad75054.json), [render SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/5a9cd4b76cff91a9802abc2bcfeaf78348cccfbabc0615fccb187b5fcee21fe2/independence_wave_focus_tree.focus.svg), and [render HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c46038276d6f758dfb7fb380d96b1e220b6cc2ecb16e0a0147ac0a3473d277fd/8b8e2a9b6cd51ec4b9117119104c30db2180c4be303a3d13d535e8e104044462/independence_wave_focus_tree.focus.html).

## Rejected coordinate trial and restoration

The temporary trial changed only four coordinates: the military parent from (42,7) to (40,7), reclamation from (32,8) to (40,9), independent command from (50,8) to (42,9), and professional-defense convergence from (40,9) to (40,10).
Read-only inspection at revision `6c16993d6e30aa91ef52e18e0622ecb4e69c52073282edc99cd29eee92869407` produced layout hash `deb452ab1204bd988aed0083cb5061caa85cbd437bee0c9a5436adf1b6341e0e`, 2 connector crossings, 9 node intersections, and 14 diagnostics.
The trial removed the long-connector diagnostic but added an unnecessary linear detour between `independence_wave_form_border_guard` and the military parent, retained two unsatisfied crossing pairs, and routed connectors through the professional-core, domestic-arsenal, reclamation, and independent-command focus boxes.
The matching `hoi4.focus_render` reported the same layout hash at 21,424 by 2,440 pixels; its SVG hash is `b8f6b38c4d5c339297cdc7c5caafc1ec2d6876658f5decc619451157aa24ca8f`, HTML hash `72e60d183b29520bb451233ce9537f644275b14cecafbe11ff6e9c11f8c1431d`, and JSON hash `53f3a6f8ee5125326425b7ddb25524c0622c7f39702508efba4c9344740a4e1a`.
The trial artifacts are [inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e59e6db58a610b94964cb52d5112a6b410dc117f1c0440752d23ca5d8a7c7d65/41516eaf8b58da6e56d0df9798d24b7907410c35c48cbb60b4f68ca2e2ad14d0/focus-inspect.6c16993d6e30aa91.json), [render SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8f6b38c4d5c339297cdc7c5caafc1ec2d6876658f5decc619451157aa24ca8f/f82394f8c80351338e82270bdd5a2d6a4dcc388edca17510d69d2a77f4185609/independence_wave_focus_tree.focus.svg), and [render HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72e60d183b29520bb451233ce9537f644275b14cecafbe11ff6e9c11f8c1431d/217545530a5ce9fc504814a7e4192232e5b027204cfee568b1d124299a005b51/independence_wave_focus_tree.focus.html).
The candidate was rejected, all four coordinate edits were restored, and a fresh inspect/render pair returned the original `a4d2d61f` layout hash.

## Remaining blocker

The existing direct-tree placement still violates the focus skill's short-connector goal, while the tested four-coordinate rearrangement creates visible connector crossings and focus intersections.
The full-tree high-fidelity `hoi4.focus_raster` attempt returned `RENDER_DIMENSIONS_BLOCKED`.
MCP resource reads of the focus inspect, plan, and SVG artifacts returned the exact error `Artifact provenance manifest is unavailable`; no decoded high-fidelity focus image was obtained.
The next repair needs a broader military-lane plan that clears the reclamation branch's parent edge and the capstone's multi-parent convergence without adding a direct-focus substitute or changing route logic.
No successful source edit is retained, no focus weight changed, no probability comparison was required, and no HOI4 launch or test was run.
This handoff records an unresolved layout repair and does not claim focus-tree or Event 006 completion.
