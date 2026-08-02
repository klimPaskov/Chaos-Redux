# Event 006 focus geometry reflow handoff

Date: 2026-08-02
Owner: parent agent
Scope: `common/national_focus/006_independence_wave_focus.txt`

## Result

The shared generic Independence Wave tree retains 184 direct focus definitions and all focus identifiers, localisation keys, rewards, route flags, and package effects. The authored layout was reflowed so that the rendered Event 006 graph has 186 visible prerequisite connectors with zero crossings, zero node intersections, zero long connectors, and zero too-close node pairs. The rendered bounds are x=1..121 and y=0..19.

The deterministic focus render receipt is:

- layout hash: `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/323bd0cf24f496e10110bd80a39fb87fc9003d8a74e7d056924ab6550932e290/61c9fe2440f18873880f1d08f49f6d0a233bccfaca4a91f1d0ca81ae3b1ab097/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad05162d760dac733ab2bd5f1621b0162121dde1a3e3062367a755bac03de3f5/bf6048fc092755c1e69e517954bbe0190b8ceee52d35291d06d06c2817adaa72/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de3265bd27665de9f3e54b86916914f8b5b742575036f42110da1cae0205a9c9/43548c9865fc24eceed3faf9b4b2e6ced9e44114f39f56f546283a3fa90d58ac/independence_wave_focus_tree.focus.json`
- source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d4bd36c7ca89e309eae9aba9ba58521c809030e153abec10767638196d22177/b1759a9c82de2ba00c3a3139703cf4e619c56c62296a85e387b74ef8988db04c/independence_wave_focus_tree.focus.source-map.json`
- plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d7e069f494f19f31027f6c935fa0e89ecdd95fd52634260aef5a20e925c0264/fca5633972772c76e0b0ad28747142647bd1c24e6729022a945403e0a412a330/independence_wave_focus_tree.focus.plan.json`

## Gating preservation

The original visible prerequisite edges that created the previous crossings were not deleted mechanically. They were moved into `available` as `has_completed_focus` gates for the founding branches, the emergency revenue, militia command, foreign office, former-host settlement, regional ambition, package roots, military archetype choices, durable sovereignty, the ASX dossier, and the BAY sibling branch. The capstone keeps both original military OR groups in `available`, while its three readable visible prerequisite groups remain intact. This preserves the authored route semantics while keeping the rendered graph legible.

The package lanes were separated without changing package IDs or rewards. ARX, ASX, SCO, WLS, AJX, BRI, RHI, AFX, BAY, and AGX retain their internal branch order and package-specific `allow_branch`, `available`, effects, AI, and localisation.

## Diagnostics and scope

The focus renderer reports only two `FOCUS_ISOLATED` design warnings for `independence_wave_standardize_with_league` and `independence_wave_preserve_independent_command`. Both choices retain the hidden `adopt_military_archetype_program` gate and remain connected mechanically through the capstone OR gate; their visible fan was intentionally removed because restoring it creates long or crossing connectors.

The national-tree inventory also reports fourteen missing continuous-focus sprites and one vanilla localisation warning. Those entries belong to the installed vanilla continuous-focus palette (DEN/ETH/SWI and generic continuous production/research icons), not the Event 006 tree. No unrelated vanilla assets were added to mask that inventory noise.

No live game test was run. Runtime package admission, allocator, scenario matrix, GUI matrix, flag ladders, and external-tag scans remain separate audits.
