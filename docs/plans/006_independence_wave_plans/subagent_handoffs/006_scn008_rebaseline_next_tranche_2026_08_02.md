# Repo Explorer Handoff

## Scope read

- Parent task: re-baseline Event 006 against `docs/specs/006_independence_wave_specs` and the current source/audit authority, then identify one feasible, high-impact next tranche without live HOI4 testing or bespoke country focus trees.
- Explicit constraints: read-only exploration; no package admission, fallback, gameplay redesign, or live/in-game test; preserve the committed generic-focus contract; record exact files, identifiers, precedents, risks, and validation.
- Files and IDs reviewed: `SCN-008` / `Every Banner Rises`, `chaosx.triggerable_scenarios.8`, `chaosx.triggerable_scenarios.80`, scenario type/intensity/rule constants and triggers, the shared allocator, current focus and whole-event audits, source-of-truth map, and resume packet.
- Skills/docs read: `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, the Event 006 specification parts and scenario documentation, required offline Paradox wiki pages, and relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.

## Primary findings

1. The generic focus contract is no longer the next tranche. It is a static PASS and is committed as `212e37662` (`independence_wave_focus_tree`, full assignment for the fourteen admitted packages, and the reviewed additive ICE carrier). Bespoke country trees remain out of scope.
2. The whole event remains `PARTIAL / HOLD`. The v98 authority records the shared focus geometry diagnostic artifact as unavailable (`SCAN_BYTE_LIMIT`), 14 admitted packages out of 193 non-overlay rows, 14/20 capacity unresolved, formables/assets/GUI/achievement gaps, and `6001` rights/runtime blocked.
3. The highest-impact safe next tranche is a non-live SCN-008 acceptance-matrix artifact. The source already enumerates six numeric families, eight player-facing modes (three separate Universal Belligerence rules), four intensities, 138 ranked bound attempts, 55 disabled unbound rows, and 13 route-only overlays. What is missing is an automated/static case artifact proving the required edge-case rows and ledger alignment. This closes a declared acceptance gap without admitting packages, changing focus trees, or requiring live HOI4.
4. Do not speculative-reflow the focus tree in this tranche. Current `hoi4.focus_inspect` and `hoi4.focus_render` both return `SCAN_BYTE_LIMIT`, so the post-v82 geometry blocker count and layout hash are unavailable. The current static model retains 53 crossings, 2 through-node hits, 28 long connectors, and 5 close same-row pairs.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/events/006_independence_wave/systems/triggerable_scenario.md` | Canonical SCN-008 contract and acceptance targets. | Defines Every Banner Rises, the single Liberation transaction, 138 attempts, 55 disabled rows, 13 overlays, eight selectable modes, four intensities, and the required case matrix at lines 5-12, 18-24, 32-50, and 80-82. |
| `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` | Controlling static-acceptance authority. | Scenario criteria require source/MCP coverage for all eight modes at Low/Medium/High/Maximum (32 cells), separate Universal Belligerence target/result rows, blocked-candidate reporting, and host/overlap safety. |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current source-of-truth and queued work order. | Explicitly keeps the 32-cell SCN-008 evidence open and says live playback is optional; distinguishes current 14-package authority from the wider registry. |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Resume boundary and no-reopen rules. | Says shared allocator/core is source-closed, the 32 SCN-008 cells still need source/MCP evidence, and 14/20 capacity remains fail-closed. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_narrowed_generic_focus_completion_audit_v98_2026_08_02.md` | Current whole-event matrix and recommended order. | Row 30 is `STATIC STRUCTURE PASS; ACCEPTANCE EVIDENCE HOLD`; row 113 recommends a non-live 32-cell artifact covering zero-ready, mixed readiness, collision, protected-host, Event 005, repeated launch, and ledger alignment. |
| `common/script_constants/006_independence_wave_scenario_constants.txt` | Shared scenario tuning and registry cardinalities. | `independence_wave_scenario_belligerence_rule` (former_hosts=1, neighboring_releases=2, nearby_nonleague=3); registry constants at lines 9-31 (`bound_package_count=138`, `disabled_unbound_package_count=55`, `total_registry_package_count=206`). |
| `common/scripted_triggers/006_independence_wave_scenario_triggers.txt` | Selector and transaction gates. | `independence_wave_scenario_type_is_valid`, `...belligerence_rule_is_valid`, `...intensity_is_valid`, `...queued_selection_is_valid`, `...transaction_barrier_is_open`, `...can_launch`, and `...can_execute_queued` are the static branch coverage surface. |
| `common/scripted_effects/006_independence_wave_scenario_effects.txt` | Scenario allocation and type-specific semantics. | `...initialize_settings`, `...set_intensity_tuning` (lines 94-159), `...rebuild_ranked_registry` (line 161 onward), `...load_dispatch_package` (306), `...reserve_dispatch_package` (341), `...attempt_ranked_packages` (379), and `...allocate_scenario_packages` (420 onward). Former Hosts target uniqueness is guarded later in this file; Wars of Separation intentionally keeps one viable host war per release. |
| `events/006_independence_wave_scenario.txt` | Delayed launch barrier and result event. | `chaosx.triggerable_scenarios.8` revalidates the queued selection and transaction barrier before calling `independence_wave_trigger_scenario`; `.80` publishes the frozen summary and opens the scenario ledger. |
| `common/decisions/categories/006_independence_wave_scenario_categories.txt` | Decision-category registration and ledger surface. | Registers `independence_wave_scenario_ledger_category`, the player-facing inspection surface for blocked rows and summary alignment. |
| `common/decisions/006_independence_wave_scenario_decisions.txt` | Player selector and row-level ledger controls. | Contains the mode/intensity/rule selectors and zero-reward Previous/Next/Close ledger controls referenced by the canonical scenario doc. |
| `.tools/audit_event6_allocator.py` | Existing static source audit to reuse/extend. | Already checks 149 publishers, the exact 14 attested set, 138 ranked IDs excluding overlays, all four intensity mappings, type effects, Great Partition tuning, Universal Former Hosts cleanup, Wars-of-Separation policy, and Event 005-first ordering. It does not emit a 32-cell edge-case artifact. |
| `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` | Context only; not a recommended edit surface for this tranche. | The generic tree contract is already committed and audited; focus geometry remains blocked by `SCAN_BYTE_LIMIT`. |

## Existing patterns

- The allocator is deliberately deterministic: `independence_wave_scenario_rebuild_ranked_registry` pushes a fixed ranked array, `...attempt_ranked_packages` loads every candidate, records `package_unready`, and delegates other failures to the shared reservation API. A matrix validator should report this source contract rather than duplicate or replace the allocator.
- Intensity changes territory/force/value levels but never candidate count. `...set_intensity_tuning` starts from `bound_package_count` and maps Low/Medium/High/Maximum to anchor/compact/extended/extended-high-chaos levels. Great Partition consumes one extra territory tier only when the bounded condition permits it.
- Type is orthogonal to intensity. Six numeric families are exposed as eight selectable modes because Universal Belligerence has three independently selected rules. The validator must retain three separate Universal rows; do not collapse to the historical six-by-four shorthand.
- SCN-008 reuses the ordinary Liberation transaction. The result summary (`.80`) and ledger arrays are the same source of truth for blocked candidate rows; no parallel country-release path is allowed.
- Existing source audits use fail-closed wording and preserve package admission as a separate authority. A passing matrix artifact must not be treated as 14- or 20-country runtime capacity proof.

## Vanilla or reference precedents

- No vanilla triggerable-scenario system was found. Use the Chaos Redux scenario contract as the source of truth.
- Vanilla deterministic array construction is visible in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/DOD_Yugoslavia.txt` around its `add_to_array` blocks (approximately lines 410 and 565). This is a precedent for explicit ordered candidate arrays, not proof of SCN-008 semantics.
- Vanilla delayed hidden-event sequencing appears in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/BFTB_Bulgaria.txt` and similar event files (`country_event = { id = ... days = ... }`). This supports the existing `.8` queued-launch revalidation pattern.
- Required vanilla documentation consulted: `documentation/effects_documentation.md` and `documentation/script_concept_documentation.md`. No installed Technology Tree Viewer is available; no technology evidence should be invented for this tranche.

## Likely edit order for the parent

1. Freeze the current source authority and read the SCN-008 canonical doc, Part 7 acceptance criteria, source map, resume packet, and v98 audit together.
2. Build a bounded non-live validator/artifact (prefer extending `.tools/audit_event6_allocator.py` only if its existing contract remains clear; otherwise use a dedicated `.tools/audit_event6_scenario_matrix.py`) that enumerates the 8×4 selectable matrix and emits machine-readable rows plus a concise markdown receipt.
3. For each cell, record static witnesses for: zero-ready failure; mixed ready/unready candidates; anchor collision; protected host-capital/remnant; Event 005 reserved tag/state collision; repeated launch after barrier reset; summary/ledger array alignment; and, for Universal Belligerence, former-host distinct-target reservation, neighboring-release targeting, and nearby-nonleague targeting. Record Wars of Separation as a separate control where one viable host war is allowed per release.
4. Reuse the source constants and identifiers above rather than hardcoding a second registry or silently treating 206 rows as selectable. Keep 138 bound attempts, 55 unbound disabled rows, and 13 overlays explicit in the receipt.
5. Run the existing allocator audit plus the new matrix validator and preserve outputs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`. Update the SCN-008 catalog status only if the new evidence actually satisfies the source/MCP acceptance authority; the explorer does not authorize workbook edits.
6. If the validator finds a real source defect, patch only the narrow scenario branch and re-run the static audits. Do not admit a package, add a fallback, change the focus contract, or claim runtime completion.

## Validation checks

- `python -B .tools/audit_event6_allocator.py` (must retain the current 149-publisher, 138-ranked, 14-attested, ladder, Event 005-first, and Former Hosts/Wars-of-Separation checks).
- `rg -n "independence_wave_scenario_type_(sovereign_scatter|common_congress|wars_of_separation|universal_belligerence|patron_worlds|great_partition)" common/scripted_triggers/006_independence_wave_scenario_triggers.txt common/script_constants/006_independence_wave_scenario_constants.txt`.
- `rg -n "triggerable_scenario_intensity\.(low|medium|high|maximum)" common/scripted_triggers/006_independence_wave_scenario_triggers.txt common/scripted_effects/006_independence_wave_scenario_effects.txt`.
- `rg -n "former_hosts|neighboring_releases|nearby_nonleague|package_unready|unbound_current_map|independence_wave_scenario_ledger_category|chaosx\.triggerable_scenarios\.(8|80)" common events localisation docs/events/006_independence_wave/systems/triggerable_scenario.md`.
- Assert the generated receipt has exactly 32 selectable mode/intensity rows, three distinct Universal Belligerence rule rows per applicable mode, 138 bound attempts per intensity, 55 disabled rows, and 13 excluded overlays; assert no candidate count change across intensities.
- Assert every row has a rejection/commit outcome witness and ledger-array alignment fields, and that zero-ready, collision, protected-host, Event 005, repeated-launch, and former-host uniqueness cases are represented.
- Keep the current MCP evidence boundary explicit: `hoi4.focus_inspect`/`hoi4.focus_render` returned `SCAN_BYTE_LIMIT`; the supplemental event roots inspection was only partial structural evidence (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b62fbb78263084c7664a71ef79164649f65d3997d70d9a5fc5507363b465d0b5/8201ea15dc20509a0a06d074a99b51ca23fd975b00b9a8222d50e58a1b9fbd96/event-roots-8cb7d9f366af.json`).

## Risks and blockers

### Confirmed blockers

- No current 32-case static/MCP scenario artifact exists; the catalog remains `Needs Testing` under the source authority even though source enumeration is present.
- The current admitted set is fourteen packages; 20-country capacity is unreachable and 14-country compatible-capacity evidence is not closed. A matrix receipt cannot promote packages or prove simultaneous runtime allocation.
- Focus diagnostics/rendering remain unavailable because of `SCAN_BYTE_LIMIT`; geometry edits should wait for a successful focused inspect/render.
- Formables, shared asset/crosswalk evidence, Statehood Ledger GUI evidence, achievement row-level evidence, and super-event `6001` remain separate blockers. `6001` is rights/runtime blocked and has no authorized fallback.

### Ordinary risks

- Static source witnesses cannot prove Clausewitz runtime scope, target reservation, array mutation, or host survival. Keep all claims bounded to source/static evidence and do not claim live execution.
- The three Universal Belligerence rules are easy to collapse accidentally. Preserve separate Former Hosts, neighboring releases, and nearby nonleague rows, and keep Wars of Separation as its own control.
- A validator that duplicates the 138-ID registry or treats all 206 rows as candidates can drift from the constants. Read the existing ranked array and constant values as the authority.
- A tooling-only change is not gameplay completion. If no branch defect is found, report the tranche as acceptance evidence only and leave the whole-event status `PARTIAL / HOLD`.

## Recommended next action

Implement the bounded, non-live SCN-008 8×4 acceptance-matrix artifact now, reusing the existing allocator audit and source constants. It is the safest high-impact tranche because the source paths are already wired, the missing evidence is explicitly named by v98 and Part 7, and it does not require live HOI4, package admission, new assets, or bespoke country focus trees. Keep the generic focus contract, capacity boundaries, formables, GUI, assets, and `6001` blockers unchanged until their owning audits close them.
