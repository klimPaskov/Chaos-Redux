# Super-event draft copyedit handoff

## Scope

This pass audited explicit player-facing draft strings embedded in `docs/plans/**`.

The pass did not edit gameplay, localisation, scripted localisation, GFX, GUI, event, focus, decision, audio, image, DDS, or spreadsheet files.

The pass did not rewrite ordinary planning, audit, implementation, or process prose.

The copy standard came from `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`.

## Source-of-truth map

| Surface | Authority and evidence | Current disposition |
| --- | --- | --- |
| Event 012 Africa super-events | `docs/specs/012_africa_specs/prompts/africa_super_event_prompt.md` and `docs/specs/012_africa_specs/specs/012_africa_spec_part_6_presentation_achievements_assets.md` define four public roles and require research before wiring. The plan handoffs contain candidate titles, remarks, and description contracts. `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_package_completion_audit_2026-07-29.md` records that display, localisation, triggers, dispatch, and audio setters remain absent. | Draft copy normalized in five plan and handoff files. Runtime remains untouched and the package remains queued for parent approval and wiring. |
| Event 014 Cannibalism super-events | `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_8_wendigo_and_world_end.md` and `docs/specs/014_cannibalism_specs/matrices/super_event_matrix.md` define the four slots. `docs/plans/014_cannibalism_plans/014_super_event_text_research.md` supplies proposed English strings. | Slot 49 and slot 52 draft descriptions were copyedited. Runtime localisation remains unchanged and needs an owner sync if the wording is accepted. |
| Event 011 Secret Alliance super-event | `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_text_research.md` states that slot 73 was accepted, promoted, and implemented. `localisation/english/011_secret_alliance_l_english.yml:277` is current implementation evidence. | Left unchanged because the handoff presents the text as implemented. The fractured description needs a parent decision before any runtime and documentation rewrite. |
| Event 016 Brilliant Scientist super-events | `docs/super_events/016_brilliant_scientist/text_research.md` is the controlling text research note. The plan handoff and `localisation/english/016_brilliant_scientist_super_events_l_english.yml` align with its selected buttons. | Left unchanged because changing either selected button would alter accepted canonical copy across the source note, plan handoff, and runtime localisation. |
| Event 006 Independence Wave super-event research | `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_text_verification.md` contains localization-ready recommendations without the targeted style defects. | Left unchanged. |
| Event 015 Utopia, Event 018 Resources Found, and Event 003 Holy Realm text handoffs | The reviewed files contain selected remarks, quotations, or research directions without a clear targeted style defect in the visible draft copy. | Left unchanged. |
| Event 020 Rat King global-defeat aftermath | `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_super_event_087_text_research_handoff.md` states that the title, quote, button, and description are promoted in runtime localisation. Its promoted description contains a contrast join in `The Royal Basin is silent, but hospitals, railways, archives, and emptied towns still bear the plague's mark.` | Left unchanged because runtime and handoff are already promoted. Parent decision required before a paired copyedit. |

## Files changed

- `docs/plans/012_africa_plans/012_africa_super_event_final_text_research_handoff.md`
- `docs/plans/012_africa_plans/012_africa_super_event_research_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_super_event_text_research_2026-07-29.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_super_event_text_research_final_2026-07-30.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_package_completion_audit_2026-07-29.md`
- `docs/plans/014_cannibalism_plans/014_super_event_text_research.md`

## Copy edits made

| Surface | Previous draft | Current draft | Reason |
| --- | --- | --- | --- |
| Event 012 Scramble response button | `This time, Africa answers.` | `Africa answers through its own institutions.` | Removes the staged time contrast and makes the public subject and institutional agency explicit. |
| Event 012 The World description contract | `Rival world orders have ended. Their peoples remain.` | `Rival world orders have ended, and their peoples remain.` | Removes a staccato two-sentence ending while preserving the distinction between ended political orders and surviving peoples. |
| Event 014 slot 49 description | `No government can prove whether he designed every cell or claimed the network when it had grown strong enough. The warlords no longer debate the distinction. Their armies, islands, and feeding territories are moving under one command.` | `No government can determine how much of the network Hannibal designed before claiming it as his own. The warlords have accepted his command, and their armies, islands, and feeding territories now move together.` | Preserves uncertainty, command, and movement while removing dialectical framing and short result chains. |
| Event 014 slot 52 description | `The coalition has won the war, but whole districts remain emptied.` | `The coalition has won the war, and whole districts remain emptied.` | Removes the contrast formula while preserving the victory and the continuing human cost. |

Identifiers, dynamic tokens, slots, audio IDs, titles, quotations, and gameplay claims were not changed.

## Unresolved plan and handoff disposition

| Document group | Disposition | Reason and next owner |
| --- | --- | --- |
| Event 012 Africa text handoffs and the 2026-07-29 world-package audit | Queued after draft normalization | The four role packages remain research candidates or blocked runtime work. Parent must approve the revised button and contract, then the implementation owner must sync any future localisation and dispatcher work. |
| Event 014 Cannibalism text research | Queued after draft normalization | The file is a proposed final localisation package, not an implementation file. The localisation owner must decide whether to promote the revised slot 49 and slot 52 bodies. |
| Event 011 Secret Alliance text handoff | Left unchanged as accepted and implemented | The fractured description is already represented in runtime localisation. Parent must approve any wording change before a paired runtime and docs patch. |
| Event 016 Brilliant Scientist text research and plan handoff | Left unchanged as accepted canonical research | `No one has won.` and `Inspection begins where victory ends.` may be stylistically debatable, but changing them would alter accepted source text and runtime localisation together. Parent decision required. |
| Event 006, 015, 018, and 003 text documents | Left unchanged | No clear targeted player-facing style defect was found in the reviewed draft surfaces. |
| Event 020 Rat King super-event text handoff | Left unchanged as promoted runtime text | The handoff and `localisation/english/020_black_plague_super_events_l_english.yml` are already promoted. Parent must decide whether the contrast join warrants a paired runtime and docs rewrite. |

No plan was marked rejected because no reviewed source supplied a rejection disposition.

No plan was marked superseded because the overlapping Event 012 handoffs are dated research evidence and no parent disposition identifies a canonical replacement.

## Contradictions and sync risks

1. `docs/plans/014_cannibalism_plans/014_super_event_text_research.md:50` and `:161` now hold revised draft strings, while `localisation/english/014_cannibalism_l_english.yml:2025` and `:2033` still hold the previous runtime strings. This is an intentional documentation-only mismatch until the localisation owner promotes or rejects the draft.

2. `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_text_research.md` describes slot 73 as implemented, while `localisation/english/011_secret_alliance_l_english.yml:277` retains the fractured description's short sentences and unsettled final clause. The runtime status makes this a parent decision, not a documentation-only rewrite.

3. `docs/super_events/016_brilliant_scientist/text_research.md`, `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_super_event_text_research_handoff.md`, and `localisation/english/016_brilliant_scientist_super_events_l_english.yml:20` and `:24` agree on `No one has won.` and `Inspection begins where victory ends.`. Those lines remain accepted canonical copy even though they may read as generic filler or a contrast formula under the current style rules.

4. `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_super_event_087_text_research_handoff.md` says the slot 87 description is promoted, while its visible sentence still uses `but` to join the silent basin and surviving infrastructure. A rewrite would require a paired runtime localisation decision.

5. Event 012 has four overlapping dated research handoffs plus a package audit. They now share the revised Scramble response button, but the documents remain separate and are not marked superseded. Parent should select one current research handoff and retain the dated copies as evidence or add an explicit superseded notice.

## Duplicate and superseded document list

- Event 012 duplicates: `012_africa_super_event_research_handoff.md`, `012_africa_super_event_final_text_research_handoff.md`, `subagent_handoffs/012_africa_super_event_text_research_2026-07-29.md`, and `subagent_handoffs/012_africa_super_event_text_research_final_2026-07-30.md` overlap on the four title and remark selections. They remain dated evidence and were not deleted or silently superseded.
- Event 012 audit: `subagent_handoffs/012_africa_world_package_completion_audit_2026-07-29.md` repeats selected text inside a runtime-status table. It was aligned with the revised button but remains an audit record, not a source spec.
- Event 016 split authority: `docs/super_events/016_brilliant_scientist/text_research.md` and the Event 016 plan handoff are intentionally separate canonical research and implementation-status surfaces. No merge was attempted.
- No other reviewed candidate file required a superseded notice.

## Stale prompt and instruction audit

The named Event 012, Event 014, and Event 016 super-event prompts still point to their current spec areas and do not use the old Africa button phrase, obsolete slots, or superseded event identifiers.

No stale prompt filename or obsolete event id was found in the reviewed plan surfaces.

The dated Event 012 handoffs contain old research timestamps, but those dates are provenance and were not rewritten as current implementation claims.

## Validation performed

- Searched `docs/plans` for the removed `This time, Africa answers.` phrase. No match remains.
- Searched `docs/plans` for the removed `Rival world orders have ended. Their peoples remain.` ending. No match remains.
- Re-read every changed block and confirmed that slot numbers, event keys, dynamic placeholders, titles, quotations, and audio IDs are unchanged.
- Compared the revised Event 014 draft strings against runtime localisation to record the required owner sync instead of editing forbidden gameplay surfaces.
- Checked the reviewed 011 and 016 canonical surfaces for accepted copy that requires parent approval before any paired change.

## Skipped validation and why

- No localisation, workbook, spreadsheet, GFX, audio, or gameplay validation was run because those surfaces are outside this subtask's ownership.
- No Hearts of Iron IV launch or live-session test was run because runtime validation belongs to the parent and user.
- No binary asset or spreadsheet inspection was performed.

## Remaining risks and parent decisions

- Decide whether to promote the revised Event 014 bodies into runtime localisation and then update any event catalog wording through the spreadsheet owner.
- Decide whether to preserve or rewrite the accepted Event 011 fractured description and the Event 016 two selected button remarks. Any change needs paired runtime and documentation updates.
- Decide whether to preserve or rewrite the promoted Event 020 slot 87 description. Any change needs paired runtime and documentation updates.
- Select one Event 012 research handoff as current, then mark dated duplicates as retained evidence or superseded documentation.
- Keep Event 012 runtime status blocked until the four-role research, source, asset, audio, localisation, and dispatcher gates are complete.

No gameplay completion claim is made by this handoff.
