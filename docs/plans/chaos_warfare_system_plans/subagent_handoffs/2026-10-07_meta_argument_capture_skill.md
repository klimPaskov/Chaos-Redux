# Meta argument capture skill handoff

Disposition: implemented as a documentation-only skill addition, with parent review and isolated commit pending.
Acceptance basis: the parent explicitly assigned this four-sentence reusable rule and this handoff on 2026-10-07.
Owner scope: `.agents\skills\chaos-redux-events\SKILL.md` and this handoff.
No gameplay files, other skills, index entries, or commits were changed.

## Change

The existing literal-only meta-field guidance already covers this workflow, so no new skill was created.
Four sentences immediately after its literal-field paragraph explain construction-time capture, compute-before-consume ordering, helper invocation inside a dynamic guard, preservation of eligibility/RNG/records/duplicate checks, and effect-specific delay evidence.
The addition contains no event IDs, event names, or task-specific implementation paths.
No routing change to `AGENTS.md` or `chaos-redux-subagents` is needed.

## Evidence and limits

Direct local reading covered installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:4833-4852` (`meta_effect`) and `:8096-8128` (`state_event`).
Its SHA256 revision is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
The installed examples support building effects from strings and literal state-event delay fields; they do not establish universal variable-delay support or explicitly document every capture-order detail.

Direct local reading covered offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:4617-4682` (construction/replacements) and `:3350` (state-event variable-delay warning).
Its SHA256 revision is `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.
The offline example computes its variables before invoking the meta block.
The variable-delay warning is retained as uncertainty rather than converted into a universal prohibition.

The vanilla substitution precedent read was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\CZE_scripted_effects.txt:438-447`.
Its SHA256 revision is `CB5EE5136B5759EFE4CAAAACE23189964FCE57AF18558D0AC535336EA93319C6`.
This precedent demonstrates a guarded meta invocation using a previously available variable; it is not evidence for state-event variable delays.

The parent supplied the timing finding and reports 20 source cases in a bounded model.
Those cases were not independently rerun by this skill worker and are not engine validation.
This documentation-only edit follows the assigned local-reading route and does not claim MCP or live-game evidence.
No skill-scope blocker or simplification remains; parent implementation validation and final review remain outside this handoff's completion claim.

## Exact isolated insertion

The skill had pre-existing edits by other actors.
Removing the insertion from the resulting bytes reproduces the exact working-before bytes.
Do not stage the entire dirty skill file.

Snapshot directory: `C:\Users\klimp\AppData\Local\Temp\chaos-redux-meta-capture-33b704faa1c44699a7aff9fa1b48355c`.
Working-before bytes: `skill.before.bin`, SHA256 `FF298DDAACCD5E1127A3B99C28FAB7F138168B0FFA30EC05EF95234ED5251E4E`.
Exact insertion bytes: `skill.insertion.bin`, SHA256 `B181A58414662A161CB6BFE6A201BCE929B0E456A8CCDE3B3EC44B7B1A251365`.
Resulting bytes: `skill.after.bin`, SHA256 `8899B0CC3648F8F35EDFEF19D3287312CAB77410D85D5F97AB38A9DE65E57640`.
Zero-based insertion byte offset: `79225`.
Insertion byte length: `714`.
The insertion includes two leading line endings, uses the skill's existing line endings, and has no trailing line ending; all original bytes are preserved.

Parent commit ownership: use the before/insertion artifacts to isolate this addition, review it together with the current index, and commit only the authorized hunk plus this handoff as appropriate.
The worker is frozen after validation.
