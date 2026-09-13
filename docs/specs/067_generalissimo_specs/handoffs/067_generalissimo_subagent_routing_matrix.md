# Event 067 Subagent Routing Matrix

## Purpose

This matrix assigns every Event 067 implementation surface to the narrow project subagent that owns it. Each invocation must use a complete self-contained prompt with no inherited parent context. The main agent keeps final integration, validation, and completion authority.

## Planning-stage status

All 20 supplied subagent definitions were read in full before this specification pack was written.

The active planning environment did not expose a working custom-subagent invocation route. Two connector discovery attempts failed with HTTP 429 and HTTP 404 responses. No subagent output is claimed in this pack.

The parent-authored review in `quality/067_generalissimo_parent_improvement_review.md` is a design check. It does not replace the required independent improvement-loop pass during implementation.

## Routing table

| Surface | Required subagent | Mode | Required timing | Main handoff |
| --- | --- | --- | --- | --- |
| Unclear repository locations or dependencies | `chaosx_repo_explorer` | Read-only | Only when direct inspection cannot resolve the file map | Exact files, precedents, risks, edit order, MCP routes |
| Event-owned constants, variables, targets, effects, and triggers | `chaosx_scripted_system_architect` | Narrow patch | Before broad event and decision wiring | Helpers, call sites, lifecycle, cleanup, remaining parent work |
| Crisis, junta, integration, and world-end decisions | `chaosx_decision_mission_auditor` | Active audit and small patch | After the first complete decision tranche and before completion | Decision IDs, costs, objectives, AI, cleanup, exploit findings |
| Generalissimo focus tree | `chaosx_focus_tree_auditor` | Active audit and small patch | After route implementation and after final layout changes | Route coverage, render evidence, AI, icons, localisation, gaps |
| Dynamic civil-war and military-government country package | `chaosx_country_package_auditor` | Active audit and small patch | After civil-war and peaceful-takeover setup | Identity, capital, forces, laws, focus loading, AI, cleanup |
| Event-owned compact display and focus inlay | `chaosx_event_ui_worker` | Bounded implementation | After gameplay state and layout brief are locked | GUI files, identifiers, resolutions, states, render comparisons |
| AI weights and random selection | `chaosx_ai_probability_auditor` | Read-only | Before every weight patch and after it | Named scenarios, inspect evidence, comparison, unresolved factors |
| Generalissimo portrait | `chaosx_portrait_creator` | Asset production | After character token and runtime basename are locked | Fictional ImageGen source, DDS, portrait wiring, manifest |
| Report, news, category, super-event, flag, and emblem art | `chaosx_generated_event_art` | Asset production | After final consumer names and dimensions are locked | Source art, processed assets, DDS, contact sheets, manifest |
| Focus, idea, trait, decision, mission, and achievement icons | `chaosx_icon_artist` | Asset production | After identifiers and consumers are locked | Separate icon-family art, DDS, alignment QA, handoff |
| Super-event quotes and cultural remarks | `chaosx_super_event_text_researcher` | Research | Before final super-event localisation | Candidates, exact sources, confidence, selected recommendation |
| Super-event music | `chaosx_super_event_audio_researcher` | Research and audio preparation | Before sound wiring | Licensed source, rights, original, final WAV, checksums, handoff |
| Broad Event 067 localisation | `chaosx_localisation_auditor` | Active audit and small patch | After complete English text exists and before completion | Keys, wording, dynamic text, encoding, cross-surface mismatches |
| Catalog workbook | `chaosx_spreadsheet_doc_worker` | Workbook patch | After implementation wording and facts are stable | XLSX fields, preserved structure, export result |
| Documentation reconciliation | `chaosx_documentation_curator` | Documentation patch | After several handoffs or before final resume and completion | Source map, plan dispositions, superseded and unresolved docs |
| Design depth review | `chaosx_improvement_loop_planner` | Plan-only | After a meaningful implementation tranche | Expansion or closure addendum under Event 067 plans |
| Final spec-versus-implementation review | `chaosx_event_completion_auditor` | Read-only | After all accepted addenda are resolved | Missing mechanics, assets, AI, docs, validation, and fallbacks |
| Event 067 custom 3D geometry | `chaosx_3d_model_pipeline` | Not routed | No accepted 3D consumer exists | Do not invoke unless the accepted specification changes |
| Historical non-portrait source art | `chaosx_asset_source_researcher` | Conditional research | Only if implementation replaces an accepted fictional asset with a real historical requirement | Source, provenance, rights, processing handoff |
| Skill maintenance | `chaosx_skill_maintainer` | Conditional documentation | Only if implementation reveals a reusable workflow defect | Skill files changed and consistency checks |

## Mandatory probability cycle

Every change to an AI weight, MTTH modifier, random-list weight, target score, focus choice, decision score, scenario outcome, or world-end outcome follows this sequence:

1. `chaosx_ai_probability_auditor` runs `hoi4.probability_inspect`.
2. The auditor records the named baseline scenarios and the completeness of each candidate pool.
3. The owning patch-capable agent or parent applies the accepted change.
4. The probability auditor runs `hoi4.probability_compare` over the same scenarios.
5. The parent accepts, revises, or rejects the change from the evidence.

The auditor does not choose the desired balance and does not edit source.

## Improvement-loop cycle

After the first complete implementation tranche:

1. Run `chaosx_improvement_loop_planner` against the actual repository state.
2. Record every proposed addition as accepted, queued, rejected, or blocked.
3. Fold accepted design into the Event 067 specifications or implement it.
4. Do not request another broad planning pass while an earlier addendum remains unresolved.
5. Run a final closure review after all accepted additions are resolved.

## Final parent gate

The parent agent must confirm that:

- each patch handoff stayed inside its role
- every accepted plan has a disposition
- probability comparisons use the same named scenarios as their baselines
- asset handoffs have runtime consumers
- the temporary Event 067 asset workspace is retained while blocked and removed only after durable evidence is promoted
- documentation and the authoritative workbook match final player-facing wording
- no subagent output is treated as proof of full event completion by itself
