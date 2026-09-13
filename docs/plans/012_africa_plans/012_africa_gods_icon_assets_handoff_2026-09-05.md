# Event 012 Gods of Africa icon asset handoff

Status: source art, target-size PNGs, and final DDS files are complete for the accepted 27-icon inventory, and current working-tree GFX and consumer wiring is evidenced; live visual review and promotion remain pending.

Reconciliation note, 2026-09-05: the asset package itself changed no GFX, gameplay, localisation, or spreadsheet files, but the current parent working tree now contains the proposed aliases and the Event 012 decision, idea, focus, and category consumers described below. This source evidence supersedes the narrower pending-wiring wording without constituting parent or user approval.

## Scope and references

This package follows the accepted Gods of Africa asset prompt and the current consumers in `common/ideas/012_africa_gods_ideas.txt`, `common/decisions/012_africa_gods_decisions.txt`, and `common/national_focus/012_africa_continental_focus_tree.txt`.

The matching canonical contact sheets were inspected before generation at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/missions/contact_sheet.png`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/contact_sheet.png`.

The official ImageGen skill was used for every source PNG with genuine transparent-background instructions in the initial call, and no background-removal fallback was used.

## Files and processing

Native source PNGs are preserved under `docs/assets/012_africa_gods_icons/source/` and processed review PNGs are under `docs/assets/012_africa_gods_icons/processed/`.

The review contact sheet is `docs/assets/012_africa_gods_icons/contact_sheet.png`.

The complete per-asset manifest with source, processed, and final DDS SHA-256 hashes, prompts, dimensions, proposed sprite aliases, and consumer notes is `docs/plans/012_africa_plans/012_africa_gods_icon_manifest.json`.

The concise GFX-only companion is `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_of_africa_gfx_handoff.md`.

Every processed PNG is RGBA with all four corners alpha zero and a non-empty subject, and every DDS decodes strictly through Pillow as RGBA at the requested size.

DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` on the processed PNGs, and decoded DDS pixels match their processed PNG pixel-for-pixel, including alpha.

Fully transparent processed pixels have RGB zeroed after resize so no invisible matte spill can reach the runtime texture.

The mechanic and idea targets are 64x64, decision targets are 32x32, and focus targets are 94x86, matching the current Chaos Redux consumers and repository precedent.

## Final DDS inventory

### Strength and Wrath mechanic icons

| Asset | Final DDS | Proposed sprite |
| --- | --- | --- |
| Gods of Africa Strength | `gfx/interface/012_africa/gods_of_africa/gods_of_africa_strength.dds` | `GFX_012_africa_gods_strength` |
| Wrath of the Gods | `gfx/interface/012_africa/gods_of_africa/gods_of_africa_wrath.dds` | `GFX_012_africa_gods_wrath` |

### Participant response decision icons

| Accepted asset | Final DDS | Proposed sprite | Current consumer mapping |
| --- | --- | --- | --- |
| fulfill | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_fulfill_demand.dds` | `GFX_decision_012_africa_gods_fulfill_demand` | `gods_of_africa_comply_demand` |
| substitute | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_offer_substitute.dds` | `GFX_decision_012_africa_gods_offer_substitute` | `gods_of_africa_substitute_demand` |
| extension | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_request_extension.dds` | `GFX_decision_012_africa_gods_request_extension` | `gods_of_africa_negotiate_demand` |
| refuse | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_refuse_demand.dds` | `GFX_decision_012_africa_gods_refuse_demand` | `gods_of_africa_refuse_demand` |
| defy | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_defy.dds` | `GFX_decision_012_africa_gods_defy` | `gods_of_africa_permanent_defiance` |

### Africa-side action icons

| Accepted asset | Final DDS | Proposed sprite | Consumer state |
| --- | --- | --- | --- |
| priority | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_set_priority.dds` | `GFX_decision_012_africa_gods_set_priority` | `gods_of_africa_prioritize_land`, `gods_of_africa_prioritize_fuel`, `gods_of_africa_prioritize_manpower`, `gods_of_africa_prioritize_industry` |
| leniency | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_grant_leniency.dds` | `GFX_decision_012_africa_gods_grant_leniency` | `gods_of_africa_grant_leniency` |
| offender | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_mark_offender.dds` | `GFX_decision_012_africa_gods_mark_offender` | `gods_of_africa_mark_offender` |
| protection | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_protect_partner.dds` | `GFX_decision_012_africa_gods_protect_partner` | `gods_of_africa_protect_partner` |
| pardon | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_public_pardon.dds` | `GFX_decision_012_africa_gods_public_pardon` | `gods_of_africa_seek_reconciliation` and settlement/reconciliation consumers |
| escalation | `gfx/interface/decisions/012_africa/gods_of_africa/decision_012_africa_gods_escalate_offense.dds` | `GFX_decision_012_africa_gods_escalate_offense` | `gods_of_africa_prepare_defensive_defiance`, `gods_of_africa_harden_stockpiles`, `gods_of_africa_secure_transport`, and `gods_of_africa_prepare_countermeasures` |

### Doctrine idea icons

| Idea id | Final DDS | Proposed sprite |
| --- | --- | --- |
| `gods_of_africa_idea_proclamation` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_proclamation.dds` | `GFX_idea_gods_of_africa_idea_proclamation` |
| `gods_of_africa_idea_voices` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_voices.dds` | `GFX_idea_gods_of_africa_idea_voices` |
| `gods_of_africa_idea_reciprocal_covenant` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_reciprocal_covenant.dds` | `GFX_idea_gods_of_africa_idea_reciprocal_covenant` |
| `gods_of_africa_idea_sovereign_exaction` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_sovereign_exaction.dds` | `GFX_idea_gods_of_africa_idea_sovereign_exaction` |
| `gods_of_africa_idea_reserve` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_reserve.dds` | `GFX_idea_gods_of_africa_idea_reserve` |
| `gods_of_africa_idea_judgment` | `gfx/interface/ideas/012_africa/gods_of_africa/idea_gods_of_africa_idea_judgment.dds` | `GFX_idea_gods_of_africa_idea_judgment` |

### Focus icon families

| Family | Final DDS | Proposed sprite | Current focus ids covered |
| --- | --- | --- | --- |
| proclamation and institution | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_proclamation_institution.dds` | `GFX_goal_012_africa_gods_proclamation_institution` | `gods_of_africa_focus_prepare_proclamation`, `gods_of_africa_focus_office_voices`, `gods_of_africa_focus_continental_proclamation`, `gods_of_africa_focus_recognize_voice`, `gods_of_africa_focus_africa_speaks_for_itself` |
| reciprocal doctrine | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_reciprocal_doctrine.dds` | `GFX_goal_012_africa_gods_reciprocal_doctrine` | `gods_of_africa_focus_reciprocal_covenant` |
| extractive doctrine | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_extractive_doctrine.dds` | `GFX_goal_012_africa_gods_extractive_doctrine` | `gods_of_africa_focus_sovereign_exaction` |
| provision and logistics | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_provision_logistics.dds` | `GFX_goal_012_africa_gods_provision_logistics` | `gods_of_africa_focus_measure_needs`, `gods_of_africa_focus_continental_arsenals`, `gods_of_africa_focus_rails_ports_fuel`, `gods_of_africa_focus_continental_reserve`, `gods_of_africa_focus_relief_beyond` |
| oaths and diplomacy | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_oaths_diplomacy.dds` | `GFX_goal_012_africa_gods_oaths_diplomacy` | `gods_of_africa_focus_return_soil`, `gods_of_africa_focus_end_sponsorship`, `gods_of_africa_focus_security_oaths` |
| protection | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_protection.dds` | `GFX_goal_012_africa_gods_protection` | `gods_of_africa_focus_shelter_faithful`, `gods_of_africa_focus_expedition`, `gods_of_africa_focus_no_sanctuary` |
| judgment | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_judgment.dds` | `GFX_goal_012_africa_gods_judgment` | `gods_of_africa_focus_record_refusal`, `gods_of_africa_focus_reach_beyond_coast`, `gods_of_africa_focus_let_world_answer`, `gods_of_africa_focus_hand_judgment`, `gods_of_africa_focus_last_sentence` |
| continental settlement | `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_continental_settlement.dds` | `GFX_goal_012_africa_gods_continental_settlement` | `gods_of_africa_focus_final_council` |

## Parent-owned wiring and open review

No GFX, gameplay, GUI, focus, decision, idea, localisation, or spreadsheet files were edited by this package.

The current working tree contains the proposed sprite aliases in `interface/012_africa.gfx`, and the listed decision, idea, and focus consumers now reference the generated aliases; the parent should still review the contact sheet and native-size PNGs before accepting the wiring.

The six existing `gods_of_africa` idea pictures now have matching aliases in `interface/012_africa.gfx`, with consumers in `common/ideas/012_africa_gods_ideas.txt`; live visual review remains open.

The current participant decision file retains generic or Charter-family sprites for demand-mission, reconciliation, and defensive paths that were outside the accepted five-response/six-action inventory; those paths remain explicitly unchanged, while the listed generated consumers use their corresponding aliases.

The current focus overlay now references the eight Gods-specific family aliases in `common/national_focus/012_africa_continental_focus_tree.txt`; the asset package did not edit that gameplay file, and the latest focus MCP inspect/render reports no blocking diagnostics while layout warnings and live review remain open.

Strength and Wrath have no current GFX or scripted-GUI consumer in the inspected source; their proposed aliases and DDS files are ready for the parent-owned consumer decision.

No custom elephant asset was produced because `common/units/012_africa_elephant_forces.txt` intentionally binds `sprite = elephantry`, the installed vanilla sprite, and the accepted scope forbids creating a replacement elephant binary.

No animation was created because the accepted package has no dedicated state-driven animated consumer.
