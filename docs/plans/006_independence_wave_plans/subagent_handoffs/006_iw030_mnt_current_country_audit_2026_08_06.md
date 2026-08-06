# IW-030 Montenegro current country-package audit

Date: 2026-08-06.

Scope: read-only audit of the registered vanilla `MNT` carrier and Event 006 adapter for state `105` / reservation group `rg_105`. This tranche made no gameplay, portrait, flag, localisation, map, attestation, or runtime-asset changes.

## Verdict

`HOLD` / fail-closed. The MNT adapter is structurally coherent, but it cannot proceed to package admission after the portrait tranche alone. Portrait source and rights gates, runtime force/carrier evidence, decision balance defects, and typed AI evidence remain open. Central attestation intentionally omits `iw_030` and must not be changed by this audit.

## Coverage checklist

| Surface | Result | Evidence or remaining gate |
| --- | --- | --- |
| Tag and registry | PASS source-level | Vanilla `MNT` maps to `countries/Montenegro.txt`; registry row maps IW-030 to state `105` and `rg_105`. |
| State, capital, host, and origin | PASS source-level | State `105` is the native Montenegro anchor; the adapter preserves the former-host relation and requires state ownership/control and capital state `105`. Live release/host evidence is still absent. |
| History and carrier | HOLD | Vanilla `history/countries/MNT - Montenegro.txt:3` references `oob = "MNT_1936"`, but `history/units/MNT_1936.txt` is absent. The adapter deliberately uses its dynamic p30 force path instead of copying an OOB. Runtime force application must be evidenced; no invented OOB patch is authorized. |
| Roster and leaders | HOLD | Native `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic` are recruited by the vanilla carrier and are all male. Popovic remains generic; Jovanovic and Dukanovic source/provenance gates remain open. |
| Portraits | BLOCKED | Current v110 and source-placeholder handoffs retain `SAFE_PACKAGE_PROMOTION = NO`; no DDS, `.gfx`, or runtime consumer was promoted. Male-only original-source placeholder policy remains in force. |
| Politics and parties | PASS source-level | MNT baseline democratic setup and four named route parties are wired in `006_independence_wave_montenegro_package_effects.txt`. Runtime route execution is unobserved. |
| Focus tree | PASS for MNT assignment; shared warnings remain | MNT receives `independence_wave_focus_assignment.full_framework`. Current MCP focus inspect/render reports 184 nodes and 193 connectors, no crossings or node intersections, and only non-blocking Event 006 layout warnings. The same run reports 14 unrelated generic/vanilla missing-icon errors, so it is not a clean whole-tree validation. |
| Decisions and mission | BLOCKED | Source lifecycle is present, but the founding mission is mathematically unwinnable: 420-day timeout versus a 495-day minimum serialized critical path. Project decisions also lack a setup-complete gate, factory thresholds exceed their wording, and capital-loss failure can be applied twice. See the decision audit receipt. |
| Ideas and icons | PASS source-level | Six MNT ideas have MNT-only scope and resolve to existing shared icon pictures. Runtime lifecycle remains unobserved. |
| Map | PASS for state anchor; global MCP limitation | State 105 map inspection found the native anchor and connected state data; state render passed. Whole-map inspect remains false because the installed workspace reports unrelated global building-position and port-adjacency diagnostics. No MNT-specific map write was made. |
| AI and weighted logic | UNRESOLVED | `ai_strategy_factor` inspection returned `PROBABILITY_SURFACE_EMPTY`; decision/mission and allocator pools are incomplete or unresolved under empty-state evaluation. No quantitative balance or live-AI claim is justified. |
| Localisation and flags | PASS source-level | Existing MNT localisation is present and the package intentionally reuses vanilla MNT flags. No mod MNT flag or missing package key was found in this pass. |
| Cleanup and release | PASS source-level; runtime unobserved | MNT cleanup removes its mission, ten decisions, six ideas, ledgers, route flags, and package lifecycle values. Runtime release/cleanup/save-load behavior still needs parent-owned validation. |
| Technology | SOURCE-ONLY | Vanilla MNT history has three research slots and period-safe technology. The installed package exposes no Technology Tree Viewer, so no engine-rendered technology evidence is available. |

## Concrete package findings

### Formable discovery unlock is not paired with a formable family

`common/scripted_effects/006_independence_wave_montenegro_package_effects.txt:268-272` sets the generic `independence_wave_unlock_formable_discovery` flag when MNT completes the Balkan corridor focus helper. MNT setup explicitly requires `NOT = { has_country_flag = independence_wave_formable_family_registered }` at `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:135`, and does not select or register a formable family. The shared discovery trigger at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:63-78` additionally requires family registration, a valid selected family, readiness, and the discovery gate. This can expose an empty or misleading formable surface. The narrow safe recommendation is to remove or guard the generic unlock in the MNT helper; do not register a family or promote central attestation.

### Vanilla carrier has a dangling OOB reference

`history/countries/MNT - Montenegro.txt:3` references `MNT_1936`, while the installed vanilla `history/units` directory contains no `MNT_1936.txt`. The Event 006 adapter instead applies a dynamic `mountain_frontier` p30 force mapping with bounded manpower, stockpile, equipment, and technology. Copying a missing OOB or inventing a replacement would exceed this audit scope. The parent must obtain runtime evidence that the dynamic force path fully supersedes the dangling carrier reference before admission.

### Founding mission cannot succeed on its own timing

`common/decisions/006_independence_wave_montenegro_decisions.txt:15-48` gives `independence_wave_mnt_hold_mountain_compact_together` the constant `founding_crisis = 420` from `common/script_constants/006_independence_wave_montenegro_constants.txt:62`. Starting cohesion/crown are 34/31 and stable compact requires 60/60. The four serialized projects that raise both values require 75 + 120 + 120 + 180 = 495 days before reaction margin, so the mission times out even on an ideal path. The decision audit also identified missing setup-complete gates on project visibility/availability, civilian-factory thresholds stricter than the player-facing wording, and duplicate capital-loss failure application.

## MCP evidence and limitations

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

- Focus inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4504f2980e1d8dc62ac100d481be8aa4e631df66dfabd1bf57f2f00df84e4437/53899d001ad77be1322d8ff566fb718e339de79f10bb56619aedfa3a199d483e/focus-inspect.4b87b3c83762e6f.json`.
- Focus render artifacts: `603203fb.../independence_wave_focus_tree.focus.html`, `99315e3b.../independence_wave_focus_tree.focus.svg`, and `1625e421.../independence_wave_focus_tree.focus.json` under the same workspace artifact root. The render is partial only because generic/vanilla icon diagnostics remain.
- State 105 map inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/787e3e2cb62c6cd48f63e2f2b4f068f2a0d3b15bee37cc0f97192fcc36e3b742/2694f21396201aa66f78c0fa4d07a41ee99c944fa17c41694631514576b63f86/map-inspect.0a75f32382e56c01.json`.
- State map render passed with revision `0a75f32382e56c015849559b548278cdaca76f76576d38856d1b32aabd964115` and artifacts `93579ebb.../map-state.png`, `a3e4c01d.../map-state.json`, and `126fb871.../map-state.html`.
- Event inspect/render returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL` with zero selected nodes because the workspace-wide event graph is deferred and unresolved. Exact artifacts are retained under event scans `be8a459e7129` and entries render `be8a459e7129`; this is not engine proof for the MNT event path.
- Technology Tree Viewer is unavailable in the installed package, so technology validation remains source-only.

## Read-only outcome and parent actions

No gameplay or asset files were changed. The parent should keep IW-030 outside central attestation until all of the following are closed: native MNT portrait source/rights and runtime wiring; dynamic force/carrier runtime evidence; the 420/495-day mission design defect and related decision gates; the generic formable unlock guard; typed AI/probability evidence; release/cleanup/save-load checks; and a clean package-level event/focus/map review. Even a complete portrait tranche is insufficient for admission by itself.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_current_country_audit_2026_08_06.md` (this docs-only handoff).

