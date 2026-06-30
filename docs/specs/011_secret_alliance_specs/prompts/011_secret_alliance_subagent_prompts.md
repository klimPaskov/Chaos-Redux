# Event 011 Secret Alliance Subagent Routing and Handoff Prompts

All project subagents must be invoked with fork_context=false. Each prompt below includes the event id, slug, paths, and scope so the subagent does not depend on inherited context.

## Scripted system architect prompt

Read AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-subagents, and the spec files under docs/specs/011_secret_alliance_specs. Design or patch reusable helpers for Event 011 Secret Alliance. Focus on candidate scoring, member arrays, reveal conversion, selected target cleanup, dynamic values, constants, and idempotent war conversion. Do not implement broad gameplay beyond helper architecture. Output helper map, constants plan, event target plan, cleanup plan, risks, and validation notes under docs/plans/011_secret_alliance_plans/subagent_handoffs/.

## Decision mission auditor prompt

Read AGENTS.md, hoi4-decisions-missions, chaos-redux-events, chaos-redux-subagents, and the Event 011 decision map. After implementation, audit the dossier category, selected target flow, missions, costs, tooltips, AI weights, cleanup, and exploit risks. Patch only small local issues. Write a handoff under docs/plans/011_secret_alliance_plans/subagent_handoffs/.

## Localisation auditor prompt

Read AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-super-events if the public reveal super-event is implemented, chaos-redux-subagents, and the Event 011 localisation directions. Audit missing keys, dynamic value formatting, event details, evolution text, decision tooltips, target names, and whether hidden members are revealed too early. Patch narrow text issues only. Write a key-level handoff.

## Icon artist prompt

Read the Event 011 asset prompt and relevant chaos-redux-event-assets sections. Produce decision icons, category icon, idea icons, achievement icons, faction emblem if treated as icon-scale art, and animated small UI pieces if assigned. Inspect reference folders first. Create source PNGs, processed PNGs, DDS files, contact sheets, manifest, and gfx_handoff.md. Do not edit gameplay or GFX files.

## Generated event art prompt

Read the Event 011 asset prompt and relevant chaos-redux-event-assets sections. Produce generated report images, super-event image, dossier panel art, member card art, and generated faction emblem if not handled by icon artist. Follow period documentary constraints and no readable generated text. Create manifest and gfx_handoff.md. Do not edit gameplay or GFX files.

## Super-event text researcher prompt

Read the Event 011 super-event prompt and quote or cultural remark sections of chaos-redux-super-events. Research real quote candidates and short button remark candidates for the public compact reveal. Verify wording and attribution. Avoid invented quotes and unsourced quote sites. Write the research note under docs/super_events/011_secret_alliance_super_event_research.md.

## Super-event audio researcher prompt

Read the Event 011 super-event prompt and audio sections of chaos-redux-super-events. Find a legally usable music track for the public compact reveal. Verify title, creator, performer if relevant, source, license, duration, and usage terms. Preserve source and create final .ogg if permitted. Write the audio handoff under docs/super_events/011_secret_alliance_super_event_research.md or a linked audio manifest.

## Completion auditor prompt

After implementation, read AGENTS.md, chaos-redux-events, chaos-redux-improvement-loop, chaos-redux-subagents, all Event 011 spec and prompt files, and the implementation files. Audit spec compliance across events, decisions, scripted helpers, evolutions, event details, assets, super-event, achievements, docs, AI, cleanup, and spreadsheet alignment. Write a read-only completion report under docs/plans/011_secret_alliance_plans/subagent_handoffs/.

## Documentation curator prompt

After implementation and audits, read AGENTS.md, chaos-redux-subagents, Event 011 specs, prompts, handoffs, docs, manifests, and completion report. Reconcile source-of-truth docs, mark queued or implemented handoffs, and write documentation_state.md or resume_packet.md under docs/plans/011_secret_alliance_plans/.
