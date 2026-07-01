# Event 013 Natural Disasters Subagent Routing Plan

The environment for this planning task exposed subagent instruction files rather than a runtime tool to spawn independent agents. Use this routing plan during implementation with `fork_context=false` and explicit prompts.

## Recommended order

1. `chaosx_scripted_system_architect`
   - Design and patch reusable disaster helpers, trigger structure, script constants, event targets, cleanup, and direct API call sites.
   - Required handoff: helper map, inputs, outputs, side effects, constants, target lifecycle, call sites, validation.

2. `chaosx_decision_mission_auditor`
   - Audit and patch the Disaster Response and Reconstruction category after the first implementation tranche.
   - Required handoff: costs, mission objectives, clutter control, AI behavior, cleanup, exploit risk.

3. `chaosx_localisation_auditor`
   - Audit event details, report text, decision text, GUI labels, dynamic family and area text, and catalog-facing strings.
   - Required handoff: missing keys, duplicate keys, dynamic text, encoding, mismatches.

4. `chaosx_generated_event_art`
   - Produce generated report, news, super-event, and GUI background assets that depict fictional or abnormal disaster scenes.

5. `chaosx_icon_artist`
   - Produce decision category icons, decision icons, idea icons, achievement icons, and animated small UI markers where appropriate.

6. `chaosx_super_event_text_researcher`
   - Research quotes and cultural remarks for meteor shower, global rupture, massive eruption, and storm corridor super-events.

7. `chaosx_super_event_audio_researcher`
   - Research, verify, download, convert, and document final licensed music for super-events.

8. `chaosx_event_completion_auditor`
   - Compare implementation with the spec after all surfaces are wired.

9. `chaosx_spreadsheet_doc_worker`
   - Update the final event catalog workbook after final in-game localisation exists.

10. `chaosx_documentation_curator`
   - Use if many handoffs, audits, asset manifests, and implementation notes need reconciliation before completion.

## Bounded prompts

Each subagent prompt must include the event id, slug, paths to the relevant spec files, the exact surface in scope, and the user rule that individual disaster pulses do not create Event Log entries. Do not rely on inherited conversation context.
