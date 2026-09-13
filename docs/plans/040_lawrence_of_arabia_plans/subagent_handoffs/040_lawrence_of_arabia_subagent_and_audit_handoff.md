# Event 40 Subagent and Audit Handoff

## Tool status for this planning pass

All supplied subagent definitions were extracted and read in full. The current conversation tool registry did not expose a project-subagent spawn action or the HOI4 MCP actions. No subagent or MCP audit was run during specification writing.

The prompts below are context-complete future handoffs. Spawn each named project subagent without inherited conversation context. In Codex use `fork_context=false`. Each prompt must include the current repository root, final implementation status, accepted plan dispositions, and any user correction received after this specification.

## Shared context for every Event 40 subagent

Project: Chaos Redux

Event:

- ID `40`
- name Lawrence of Arabia
- type Minor Fire-Once
- Chaos level `1`
- no cluster

Accepted specification root:

`docs/specs/040_lawrence_of_arabia_specs/`

Working plan and handoff root:

`docs/plans/040_lawrence_of_arabia_plans/`

Core constraints:

- one random entry and internal regional follow-up stages
- one public intervention value, Lawrence's Influence
- no custom scripted GUI
- no triggerable scenario
- no custom 3D unit
- one canonical grounded Lawrence character
- three evolutions at 200, 400, and 600 Chaos
- federation outcomes are British Arabia, Independent Arab Federation, and rare Lawrence's Kingdom
- evolution activation gives zero Chaos
- current catalog type is stale and must later become Minor Fire-Once through the workbook

## `chaosx_improvement_loop_planner`

Mode: plan-only

Prompt:

Read `AGENTS.md`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-super-events`, and every accepted Event 40 spec file. Inspect the current Event 40 implementation, docs, localisation, plans, assets, and previous addenda. Compare the implemented feature with the playable promise: one British intervention contest that can grow into revolt networks, a client system, or a federation without losing local agency. Write one bounded improvement addendum only if implementation created a substantial new gap not covered by the specs. Do not patch gameplay. If the design is already deep and aligned, write a closure handoff that recommends no broad expansion. Place the result under `docs/plans/040_lawrence_of_arabia_plans/`. Do not repeat this planner while an earlier Event 40 addendum remains unresolved.

## `chaosx_scripted_system_architect`

Mode: active narrow architecture and patch

Prompt:

Read the shared context, `AGENTS.md`, relevant system skills, the shared dynamic helper documentation, all Event 40 specs, and the current implementation. Inspect the event-owned generation, active-target, Influence, settlement, character-state, evolution, regional-node, delayed-job, federation-readiness, and formation-transaction logic. Design or patch reusable Event 40 helpers only where the behavior is already accepted. Do not move Event 40 lifecycle into shared classifiers. Use generation proof, one-shot receipts, bounded arrays, event-driven refresh, fail-closed validation, and rollback. Do not add whole-world daily or monthly iteration. List changed files, helper IDs, inputs, outputs, call sites, and remaining parent work in a handoff under `subagent_handoffs/`.

## `chaosx_decision_mission_auditor`

Mode: active audit and small patch

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-decisions-missions`, all Event 40 specs, final decisions, missions, scripted effects, tooltips, AI calls, and localisation. Audit phase visibility, action count, mission count, costs, texticons, map objectives, target validity, success, partial success, failure, cooldowns, receipts, AI, no-DLC intelligence behavior, and cleanup. The normal phase should show three to five actions, six maximum, and one or two active missions. Patch narrow defects only. Do not redesign the event or add a GUI. Weighted changes require a separate baseline and comparison pass by the probability auditor. Write a patch handoff listing every affected ID and meaningful test.

## `chaosx_ai_probability_auditor`

Mode: read-only audit

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-subagents`, relevant event, decision, and focus skills, Event 40 weighted source files, and `quality/040_lawrence_of_arabia_probability_scenarios.md`. Start with `hoi4.probability_inspect`. Audit initial and later target selection, British and target decisions, incident pools, Evolution I cells and rupture, Evolution II client and counter-bloc behavior, Evolution III core and outcome selection, Lawrence defection, Lawrence's Kingdom, focus AI, and mission priority. Use the named scenarios. State candidate-pool completeness and classify evidence as exact, bounded, sampled, score-only, or unresolved. Remain read-only. After the owner patch, run `hoi4.probability_compare` with the same scenarios and revisions.

## `chaosx_focus_tree_auditor`

Mode: active audit and small patch

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, the federation specs, the focus prompt, current focus source, localisation, assets, ideas, decisions, and AI. Use mandatory `hoi4.focus_inspect`, full-tree `hoi4.focus_render`, lint, and comparison evidence. Audit first-glance branch clarity, route depth, origin validity, hidden Lawrence route, prerequisites, mutual exclusions, bypasses, search filters, Focus Navigation, idea lifecycles, decisions, map rewards, postwar handling, AI, and icon coverage. Patch narrow issues. Broad route gaps become a plan. Return route coverage and changed IDs.

## `chaosx_country_package_auditor`

Mode: active audit and small patch

Prompt:

Read the shared context, `AGENTS.md`, event and focus skills, the federation package spec, and the full federation implementation. Audit tag or carrier collision evidence, country history, capital, states, cores, claims, control, government, parties, flags, names, leaders, portrait ownership, advisers, ideas, army, templates, equipment, manpower, technology, production, fuel, convoys, trains, supply, focus assignment, decisions, AI, wars, subjects, player switching, accession, defeat, release, and cleanup. Confirm that the formation transaction cannot duplicate or delete forces and stockpiles. Patch narrow package defects only. A new country redesign becomes a plan.

## `chaosx_localisation_auditor`

Mode: active audit and small patch

Prompt:

Read the shared context, `AGENTS.md`, Event 40 specs, the localisation prompt, and every implemented player-facing Event 40 surface. Audit missing and duplicate keys, UTF-8 BOM, scripted-localisation branches, dynamic actors, costs, tooltips, Event Details, evolution rows, country names, focuses, achievements, and super-events. Preserve the writing direction: active local actors, one public Influence value, concealed survival premise, no lone-savior framing, no film imitation, no em dashes, no semicolons, no staccato, and no hidden-route spoilers. Patch narrow text defects and list every changed key.

## `chaosx_event_completion_auditor`

Mode: read-only completion audit

Prompt:

Read the shared context, `AGENTS.md`, every Event 40 spec and plan, all implementation files, localisation, assets, super-event research, audio, achievements, federation package, Event Log wiring, docs, workbook export, and subagent handoffs. Compare every accepted requirement against implementation. Audit both pre-fire and active-event evolution entries, every baseline outcome, Lawrence state, AI, no-DLC behavior, formation rollback, save persistence, cleanup, assets, audits, and named acceptance scenarios. Report missing, simplified, fallback, blocked, stale, or unverified work. Do not patch source and do not claim completion.

## `chaosx_asset_source_researcher`

Mode: asset production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-event-assets`, the Event 40 historical research, asset prompt, and current asset manifest. Research non-portrait archival images for Lawrence with Faisal and other leaders, Lawrence with Arab and Allied officers at Aqaba, and the Hejaz Railway or related route operations. Prefer official archives and clear rights. Preserve source bytes when permitted, provenance, dates, archive data, and licenses. Produce approved source files, processed previews, DDS outputs for locked consumers, contact sheets, manifests, and GFX handoff. Do not use film stills, actors, reenactors, or lone romantic imagery as the main event scene. Do not wire gameplay.

## `chaosx_portrait_creator`

Mode: complete portrait production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-comfyui`, `chaos-redux-event-assets`, the asset prompt, and current character files. Search installed vanilla and Chaos Redux for Lawrence identity ownership. Classify him as grounded source only. Find an attributed archival photograph of T. E. Lawrence, preserve the unchanged original, create the exact head-and-shoulders crop and equality evidence, produce the deterministic `156x210` source-placeholder PNG and DDS, wire portrait-specific GFX and existing character portrait references, and write the durable manifest and handoff. Never generate, reconstruct, beautify, repaint, or substitute Lawrence's identity. Never use an actor, reenactor, illustration, or statue as the identity master.

## `chaosx_icon_artist`

Mode: asset production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-event-assets`, the asset prompt, locked runtime IDs, and canonical vanilla reference contact sheets. Produce only authorized Event 40 decision-category, decision, idea, focus, achievement, faction, and formable-seal icons. Treat every UI family separately. Request native transparent ImageGen output for alpha-backed families and preserve alpha. Create source evidence, processed PNGs, final DDS files for locked consumers, contact sheets, manifests, and GFX handoff. Do not create primitive local drawings, resize one icon family into another, or use opaque square backgrounds. Defer focus icons until stable focus IDs exist.

## `chaosx_generated_event_art`

Mode: asset production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-super-events`, the asset and super-event prompts, and approved grounded source constraints. Produce generated non-icon alternate-history scenes for the decision category or the three federation super-events only when the consumer is authorized and the scene does not fabricate a real person's identity. British Arabia must show local actors inside an uneasy British-sponsored settlement. Independent Arab Federation must center a sovereign congress. Lawrence's Kingdom must use an approved grounded Lawrence identity when he appears. Preserve source prompts, PNGs, DDS outputs, contact sheets, manifests, and handoff. Do not use film composition or readable generated text.

## `chaosx_super_event_text_researcher`

Mode: read-only research and note production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-super-events`, the Event 40 historical research, and the super-event prompt. Research several verified quote and button-reaction candidates for British Arabia, Independent Arab Federation, and Lawrence's Kingdom. Prefer public-domain, historical, political, constitutional, literary, or Lawrence primary sources. Verify exact wording, author, work, year, translation, source, and confidence. Do not invent or silently alter a quote. Keep copyrighted cultural fragments within project limits. Write recommendations and rejected candidates to the Event 40 super-event research note. Do not edit localisation.

## `chaosx_super_event_audio_researcher`

Mode: audio research and production

Prompt:

Read the shared context, `AGENTS.md`, `chaos-redux-super-events`, and the Event 40 super-event prompt. Check approved repository audio first. Research one unique structured musical recording for each federation outcome. Verify composition rights and recording rights separately. Reject film scores, unclear uploads, generated audio, drones, test tones, and placeholder ambience. Preserve original downloads, URLs, creators, performers, licenses, checksums, and conversion notes. Produce game-ready WAV files under `sound/040_lawrence_of_arabia/` and an audio handoff. Do not wire sound definitions or gameplay.

## `chaosx_spreadsheet_doc_worker`

Mode: workbook update

Prompt:

Read the shared context, the active spreadsheet skill, the catalog alignment spec, final Event Details and evolution wording, and the authoritative workbook. Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Set Event 40 to Minor Fire-Once, Chaos level 1, no cluster, and the final implemented detail and evolution summaries. Preserve workbook formatting and structure. Run `python .tools/export_event_catalog_csv.py`. Do not add a triggerable scenario or cluster row. Report the workbook and export results.

## `chaosx_documentation_curator`

Mode: documentation-only patch

Prompt:

Read the shared context, all Event 40 specs, plans, handoffs, reports, manifests, and permanent docs. Reconcile source-of-truth order, accepted and rejected addenda, current implementation status, asset and audio provenance, route coverage, and unresolved blockers. Mark stale planning notes and promote durable facts from temporary workspaces before cleanup. Do not edit gameplay, localisation, assets, or spreadsheets. Write a resume packet and source map when the implementation is long enough to benefit.

## Parent review requirements

Before relying on any handoff, the parent must verify:

- the subagent stayed inside scope
- changed files and IDs are listed
- probability source changes have baseline and comparison evidence
- broad design proposals are placed in plans and given a disposition
- assets have real consumers or are reported pending
- Event 40 temporary asset workspaces remain while blocked and are deleted only after durable evidence and runtime wiring are complete
- final docs, Event Details, localisation, and workbook agree
- the completion auditor reviews the final repository state
