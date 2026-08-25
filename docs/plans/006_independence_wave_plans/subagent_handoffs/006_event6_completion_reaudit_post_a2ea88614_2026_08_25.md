# Event 006 completion re-audit after `a2ea88614`

Date: 2026-08-25

## Disposition

**HOLD / PARTIAL.** Event 006 remains at the admitted authority boundary of **32 attested packages, 29 attested groups, 40 registered adapters, and 161 unattested packages out of 193**. Nothing in this pass supports promoting an evidence-blocked package.

The current source-of-truth map and resume packet remain authoritative for package admission, the 3/4/5/7/10 ladder, the ten-package World Collapse witness, and the neutralized pre-event crisis. Their older MCP-availability note is partially superseded by this pass: event and focus inspection/rendering now return artifacts; map inspection still does not complete; the GUI route returns workspace-wide blocking diagnostics; and probability inspection lacks the scenario inputs required for quantitative balance evidence.

## Repository snapshot and concurrency boundary

- `git rev-parse --short=9 HEAD` returned `a2ea88614` (`Consolidate small Event 006 definition registries`).
- `git diff --name-only a2ea88614..HEAD` returned no paths.
- The shared worktree contains extensive concurrent changes, including Event 006 scripted triggers, localisation, package documentation, and handoffs. This audit did not alter, stage, revert, or promote any of them.
- The only path added by this pass is this handoff.

## Fresh source validators

Run from the mod root with Python bytecode disabled:

| Command | Result |
| --- | --- |
| `python -B .tools/audit_event6_allocator.py` | PASS: 149 publishers; 126 automatic/high-chaos publishers; 138 SCN-008-ranked publishers; 40 adapters; 32 attestations; 29 groups; frozen twenty-package witness; exact 3/4/5/7/10 ladder; retired pre-event crisis. |
| `python -B .tools/audit_event6_country_api.py` | PASS: 242 broad candidates; 191 resolved candidates; 34 Soviet and 45 African candidates; zero missing and zero duplicates; IW031 crosswalk passed. |
| `python -B .tools/audit_event6_scenario_matrix.py` | PASS: all 32 matrix cells and eight edge cases. |
| `python -B .tools/audit_event6_flags.py --strict` | PASS: 102 registered flag identities, 102 complete, zero incomplete. |
| `python -B .tools/audit_event6_form16.py` | PASS: exact ARM/GEO/AZR contract. |
| `python -B .tools/audit_event6_gui_matrix.py` | PASS for the semantic source matrix only; this is not runtime rendering or save/load evidence. |

These checks preserve the current authority counts and establish that the flag atlas variant repair is complete for every registered identity covered by the strict validator. They do not attest any of the remaining 161 packages.

## Fresh MCP evidence

### Event root

`hoi4.event_inspect`, lint mode, selected `chaosx.nr6.1`, downstream depth 4 and 240-node limit, returned `EVENT_INSPECTED_PARTIAL` at revision `730a452a72e0a477b59c5cc2a817aa8781cdd5cb89f9ca3272636a23c3f9d31a`: 9,513 events, 14,705 options, 1,073 entries, 37,134 edges, 8,301 unresolved nodes, 2,130 diagnostics, and **zero blocking diagnostics**. Large-workspace helper and lifecycle projections were deferred, so this is not complete acceptance evidence.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0290b0e784e58870811c6b0796667f738182fa6ee00fea9074825ce8f9e8b2ab/ec281688be102801b79e206281fce1e366eba00aab20f82b2df914b602668760/event-lint-730a452a72e0.json`

`hoi4.event_render`, state view, returned `EVENT_RENDERED_PARTIAL` at the same revision: three selected nodes, 41,241 omitted nodes, zero blocking diagnostics, and the same deferred projections.

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c8ea23c198ac2e7b93416dfa12f20054c71e6de0547367f2bad7144a9866ec3/5961db1dca8a3095c01511095a8944466bdd2ef51406c787d353b701d453a65c/event-state-730a452a72e0-manifest.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07f1e8d475a0f9323af0a377074cb1c272ea44ccf13c89c613ba16eb3d5cdc6c/bec62d4515edcd401c2b3d6ac5f6703d6f11a7ec779e21859de44b0b20c039ae/event-state-730a452a72e0.svg`

No cached changed revision was available for a meaningful event comparison. Source-only review is not substituted for the deferred helper/lifecycle projections.

### Shared focus tree

`hoi4.focus_inspect` returned `FOCUS_INSPECTED`, validation passed, revision `f6db4ebb5d39919bd4f6c2f666e2a5066823e04bfe631b1a5466ea1ebda213ca`, layout hash `35895a6791b1770c91501cb14c2151b62534260b4601b5ed2314d164f1f4a068`: **184 focuses, 195 connectors, zero crossings, zero node intersections, two long connectors, and five authored layout diagnostics**.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc3e13fcfc425c174d234a3186d2b8de7b661ee5629315af64b74c3e5830d1ee/ab9db25c269384f394e6af1f5578084cefa267b56d0ca52970d4f286492dd5e5/focus-inspect.f6db4ebb5d39919b.json`

`hoi4.focus_render` returned `FOCUS_RENDERED`, validation passed, with the same layout hash.

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/087fa87d5b57b93e10156a6e4e2bed5d39967cb2088ad1cb3e43a7054ffd3e5a/3684deac5304c0b06ae8554094989c6cbf0ccd5cb5f993bfb932628732a2e2b5/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d4017b525b544c9fd667dbffe833a0f30a80d6191a5809b7a3283853498259b/ee1174c19f322ab61a092ae5b5b537f1634e30ce1e58b3202489e1a3461015d5/independence_wave_focus_tree.focus.svg`

This route is currently available and makes the focus geometry closure an implementable parent-owned tranche.

### Weighted decisions and missions

`hoi4.probability_inspect` used the `mission_ai_will_do` adapter on `common/decisions/006_independence_wave_decisions.txt`. It returned `PROBABILITY_SOURCE_INSPECTED`, validation passed, source revision `f65dd84a86089d949179b73de841a9a27cfc7163473d2ba5fd9c8ff6fc097473`: 54 candidates, zero currently available candidates, 49 required inputs, an incomplete pool, and zero unresolved references.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04d8827ae42b30607144093fb836ab31d27a32707bde657c756ed2952079d1ad/a03cc025a6a6a4e2da46ff19523648029b089599c94cba5fe8bccdb26cf97218/probability-inspect-9450608eb3c7.json`

This is source discovery, not quantitative balance evidence. No weighted patch or balance conclusion is admissible without the named scenario inputs and a probability-auditor pass.

### Scripted GUI and map

`hoi4.gui_inspect` completed at revision `9e77e5f850be0113eee87a29b3bd79fda9aea2071fd80c13eea1e965f7f35b1d` with 48 inspected elements, but validation failed on 2,000 workspace blocking diagnostics and 64 visible overlaps in the selected scenario.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76de7020b22a982a78ab14316ffd32c9b3916a51ecaa1b1cd5e0e4836c1bf84c/2a69d0c7e3aaec3dfaf39b80b92947fce0eea015152bc010ef514dd2906a3475/gui-inspect.9e77e5f850be0113.json`
- Rendered SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cf000756ada11a3f72b77c58099ed8eb2f376d67cd52aa69bf75f77a8e2a31f/4d504e527278de22c350ed15cd5724cbaab1d908b4464d31deb4b16942f507e4/independence_wave_status_window-full.svg`

`hoi4.map_inspect` for states 229, 230, 231, 397, 408, 409, and 563 did not return after more than 60 seconds and was terminated. No fresh map artifact or acceptance evidence exists from this pass.

## Highest admissible next tranche

The safest bounded implementation is the **shared focus geometry closure tranche**. It must be coordinates-only and must not change eligibility, effects, AI, focus IDs, connector count, package admission, or attestation.

Treat these five current diagnostics as one route-cohort reflow:

1. `independence_wave_activate_package_economic_program` (`x = 32`, `y = 6`) to `independence_wave_create_independent_treasury` (`x = 28`, `y = 8`).
2. `independence_wave_form_border_guard` (`x = 38`, `y = 5`) to `independence_wave_adopt_military_archetype_program` (`x = 40`, `y = 7`).
3. `independence_wave_adopt_military_archetype_program` (`x = 40`, `y = 7`) to `independence_wave_preserve_independent_command` (`x = 50`, `y = 8`).
4. `independence_wave_define_former_host_policy` (`x = 50`, `y = 4`) to `independence_wave_inherit_successor_ledger` (`x = 59`, `y = 5`).
5. `independence_wave_build_postwar_integration_authority` (`x = 50`, `y = 11`) to `independence_wave_focus_discover_regional_identity` (`x = 52`, `y = 12`).

Do not repeat the rejected single-node trials that moved `create_independent_treasury` to `x = 32, y = 7` or `discover_regional_identity` to `x = 50, y = 12`; they created or merely displaced geometry defects.

Acceptance requires:

- preservation of all 184 focus IDs and 195 connectors;
- source equivalence outside `x` and `y` assignments;
- zero crossings, zero node intersections, and removal of all five current authored warnings;
- fresh `focus_inspect`, `focus_render`, and before/after focus comparison evidence;
- reconciliation of the warning count in the acceptance checklist, simplifications ledger, source-of-truth map, resume packet, and Event 006 overview after the layout is accepted.

IW050/KOM remains the nearest package breadth candidate, but it is evidence-blocked and is not an admissible implementation tranche. The eight adapter-only packages IW013/NAV, IW015/GLC, IW043/CHU, IW058/ASY, IW093/DOX, IW098/SOK, IW177/FIJ, and IW179/FSM likewise remain fail-closed.

## Remaining blockers

- 161 packages remain unattested; eight of them have adapters but intentionally remain fail-closed.
- Event MCP evidence is partial because helper and lifecycle projections were deferred, and no cached comparison baseline was available.
- Probability inspection lacks 49 required scenario inputs; no quantitative AI/mission balance conclusion is supported.
- GUI evidence fails on workspace-wide blocking diagnostics and selected-scenario overlaps; source semantic checks are not a substitute.
- Fresh map inspection timed out and produced no artifact.
- Current authority documents disagree on whether the focus warning count is five or six. Fresh focus MCP evidence establishes five before the geometry tranche.
- The catalog statuses remain `Needs Testing` for Event 006 and SCN-008 and `Partially Available` for Liberations; this pass supplies no basis to advance them.

## Changed paths

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_completion_reaudit_post_a2ea88614_2026_08_25.md`

No gameplay, asset, localisation, workbook, source-of-truth, or resume-packet file was changed. Nothing was staged or committed.
