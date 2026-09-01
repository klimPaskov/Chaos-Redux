# Event 016 final-closure baselines, 2026-09-01

## Purpose

This handoff freezes the structural baseline captured immediately after the accepted final-completion contract was promoted into the Event 016 specification package. It is not completion evidence. Every changed technology, event, focus, probability, map, or GUI surface still requires the matching post-change MCP inspection and comparison.

## Source baseline

- Repository base before the closure-contract tranche: `159e6b2ac2caf5f571292fd88ab9a114dad570af`.
- Binding contract: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
- The worktree contains unrelated user and parallel-task changes. Closure commits must stage only reviewed Event 016 or explicitly shared-API paths owned by the relevant tranche.

## Event chain

`hoi4.event_inspect` traced `chaosx.nr16.1` downstream with helper expansion, depth eight, and a 500-node ceiling.

- Result: `EVENT_INSPECTED_PARTIAL`.
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Revision: `10aaa15b0c3924aba7f2bf65b7208a6901098605534c8007ee1dd8e307ff57d6`.
- Blockers: none.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8dc4a5c5da303145d39f149f29726696a0d786afcdb29c2b85d4dc933008e35/5946aeb0ef26b2e2081b1091df8ec1dbd3d3b4879037e6abb5e67f678dcd3bcc/event-trace-10aaa15b0c39.json`.

The partial status reflects the bounded trace, not a claimed event defect. Targeted traces and state-flow comparisons remain required for the opening, transfer, four evolutions, `.49`, incidents, containment, KRG formation, D'Rhondan `.40` through `.47`, Event 019 provider 508, and both terminal routes.

## Technology graph

The initial full-graph technology lint returned `TECH_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0` at revision `e9eb567a04fefa82bea15f25b9bef580e653e79649208c195e33a15ba29546df`, graph hash `c43aa3f2b623802250c57bca092d80a5dd523518f39da3474dfecd6e8892a8f5`. It also returned 1,427 blocking diagnostics across the combined vanilla and mod graph, so it is not accepted as a clean Event 016 baseline.

- Full-graph artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75ea3dc60f8b862c2fbe49606c7896ec430cb46ed3d98502c87d797ee1402852/a9248a9e5fbac555dd177c3b35e3921f2d51efc182a2832510918e9122c144bd/technology-lint-e9eb567a04fe.json`.
- Disposition: the technology/API tranche must establish targeted baselines and post-change renders for all Event 016 hidden operational, weaponization, control, and shared clone technologies. Workspace-wide inherited diagnostics may not be presented as Event 016 acceptance evidence.

## KRG focus tree

Current inspection found exactly 100 focuses and 108 connectors with zero crossings, intersections, long connectors, or blocking diagnostics.

- Tree: `brilliant_scientist_kruger_state_focus_tree`.
- Inspection revision: `400fc6311c10de69ef9a9362f09818f549a5ea9e3c605077604936bf5fcde03e`.
- Layout hash: `7a0f5017eea9a6d0a7131d07075d2bd848eeb092f5e870f3dc4bda605ec5ea39`.
- Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccb413a332d96f13ffbcaa245ebfbe6f4e7dd2ee33b97486910a520993b2d422/959aa2e727feb52e33b255068337ccc73e443c21b22fe3cb8b8352b06905f873/focus-inspect.400fc6311c10de69.json`.
- Current render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47ce06cd96e1426329b76afeda9aab2f9b7d3a3355239a976ebbf9490f2cb3d9/4744f9e3d2d2b3f55fbf5340713bfdbd7005ebc3958affbac93547b5dc102113/brilliant_scientist_kruger_state_focus_tree.focus.svg`.

The only reported warning is the inherited vanilla `continuous_restrict_freedom_desc` localisation reference, outside Event 016.

## DHR focus tree

Current inspection found exactly 88 focuses and 102 connectors with zero crossings, intersections, long connectors, or blocking diagnostics.

- Tree: `dhrondan_focus_tree`.
- Inspection revision: `55caf3e871144620dbe2a952a28a5497e6f28ab75de3647ac7fd3201b0b050b5`.
- Layout hash: `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`.
- Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f5db6df58409a015ff93792a670a90dc5bf3360b04a1fdf968a41e228e90ecb/d9edfc5e58d1545fbbc9d1c30ba11ac57bb93f72abe191fd7c54003aa574c703/focus-inspect.55caf3e871144620.json`.
- Current render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/72438626cbc4c8bebaad456b9aa2da0983755c808db5b098ce881bc0b8898056/dhrondan_focus_tree.focus.svg`.

The only reported warning is the same inherited vanilla localisation reference.

## Directorate scripted GUI

`hoi4.gui_inspect` inspected `kruger_directorate_container` with scenario `event016_directorate_compact_current`.

- Result: `GUI_INSPECTED`.
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/649e2a6d8fd0b7cb89c6a57e2a3da60a2a91c36ca677bf6f881e9bfdbcde4256/3f1a5519f38d0928cf24966f9789acb646faad2ccaf6181e714d06e3e7025c9b/gui-inspect.e7568116812bf35b.json`.
- Blocking source defect: the open and close buttons occupy the same click region in the generated compact scenario.
- Additional design risks: compact and full panels are simultaneously modelled as visible, the full background can cover the open control by z-order, and compact/full titles and backgrounds overlap in the generated state.

These findings are accepted baseline defects for the event-owned GUI tranche. They must be resolved through the dedicated GUI workflow and verified in compact and expanded states at 1366 by 768, 1920 by 1080, and 2560 by 1440. Intentional text-over-background composition does not excuse the conflicting control regions or state-visibility defects.

## Baseline disposition

The exact focus counts and clean structural layouts are invariants. The event trace is bounded and must be replaced by targeted state-flow evidence as each chain is changed. The full technology lint is only a discovery artifact and must be replaced by targeted Event 016 inspections. The Directorate overlap and click-region findings are active defects, not renderer exceptions.
