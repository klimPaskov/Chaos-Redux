# Reusable scope-frame skill maintenance

Disposition: implemented within the explicitly authorized two-file documentation scope.
No gameplay, source, assets, workbook, staging, or commit work was performed.

## Changed files and exact ownership

- `.agents\skills\chaos-redux-events\SKILL.md`: two insertion-only hunks, totaling eight instruction sentences and two separating blank lines.
- `docs\plans\035_great_depression_plans\subagent_handoffs\skill_scope_frame_maintenance_2026-10-03.md`: this handoff, created for the parent.

The selector hunk is at skill lines 366 to 369 immediately before `### 1. Classify the event first`:

```text
For deterministic max-score selectors, track explicit first-valid-candidate presence and accept that first candidate regardless of its score.
A numeric best-score sentinel must not reject an otherwise valid negative score.
After the first candidate, retain the exact score comparison and existing ID tie-break without changing weights or eligibility.
```

The transaction hunk is at skill lines 506 to 511 inside `Country activation and ROOT`, immediately before the existing matching actor/state nonce paragraph:

```text
For synchronous country transactions that can launch nested helper work, `ROOT` remains the original sender, temporary loop indexes are unscoped, and regular event-target names are shared throughout the effect chain.
Nested transaction setup can overwrite both indexes and named targets, so a regular event target alone is not a frozen transaction input.
Before any helper that can launch nested work, capture the proven source and origin pointers, actor/episode/receipt identity, and outer row indexes into recipient-owned normal private input fields.
At durable context commit, read those frozen fields and validate real object existence plus exact actor, episode, and receipt identity, rather than trusting overwritten aliases or `scope_exists` on a variable scope.
Restore outer row indexes only from that frozen frame, and clear the private fields on every success or rejection return while preserving the public immediate outputs.
```

## Findings and source basis

Read `AGENTS.md`, the entire events skill, and the official `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md` before editing.
The existing ROOT, nonce, asynchronous pointer, and helper-output-lifetime guidance did not cover synchronous nested alias overwrite or recipient-owned frozen private input frames.
The existing probability guidance did not cover valid negative-score rejection by a numeric selector sentinel.
Both gaps belong in the existing events skill, so no new skill was created.

The explicit parent task supplies the proven synchronous transaction findings and required input-freezing, identity validation, index restoration, and cleanup contract.
`transaction_order_and_duration_repair_2026-10-03.md`, Transaction order, provides supporting context for exact outgoing-row receipt restoration and deferred transaction commit.
It does not independently establish every nested alias finding.
`center_owner_probability_v2_supplement_2026-10-03.md`, Additional source finding on the before-source, records an eligible candidate scoring -7 rejected against a -1 sentinel, and the narrow first-valid-candidate correction preserving weights and the ID tie-break.
That report explicitly limits its conclusion to source arithmetic and leaves mandatory MCP probability evidence unresolved.
No event IDs, paths, variable names, dates, or task reports were added to the skill's owned hunks.

Direct local corroboration read:

- `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 263 to 266, 303 to 316, and 433 to 445, covers single-pointer event targets, effect-chain lifetime, and unscoped temporary versus scoped regular variables.
  SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 6496 to 6503, confirms the event-target effect's supported scope.
  SHA-256: `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, lines 7450 to 7474, distinguishes scope validity from country existence and states that variable scopes are always valid.
  SHA-256: `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

## Shared-workspace preservation and validation

The starting skill already had seven added lines owned by other work: the event-option audit paragraph and the participant-country ROOT paragraph.
Both were preserved exactly.
The starting file SHA-256 was `839570E0B5D2A4E7360C863E92DC1C5A392C973BA166239ECE185D2D1052A501`.
The full skill was re-read immediately before patching and matched the retained baseline.
After patching, a normalized full-text comparison matched that baseline plus only the two owned insertions.
The official skill validator returned `Skill is valid!`.
The verified post-edit skill SHA-256 was `9FC79849CBDCFD8AEA8BEAE63CF6D4AE2985B8B1E03463E802B25A2FD7AEC12D`.

Other agents have extensive active changes in this shared tree, including the underlying transaction source.
Line numbers and hashes are point-in-time evidence, and later edits can change them.
The parent must retain the earlier seven-line additions and these two owned hunks when reviewing or committing the combined file.
No overlapping edit prevented this patch.

## Completion boundary and handoff

Completed: both missing reusable rules captured, existing guidance preserved, and this handoff written.
No simplifications or omissions were made within the requested skill-maintenance scope.
No routing contract changed, so no `AGENTS.md` or subagent-skill update is needed.
Other skills were left unchanged.
No unresolved skill-content choice requires user review.
Parent review remains responsible for integration and any eventual commit under its own authorization.
This pass did not run native transaction or probability validation and does not close the parent implementation or its existing MCP evidence gaps.
