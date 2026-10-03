# Script constant schema skill rule handoff

Disposition: implemented for the bounded reusable skill rule; parent review and isolated commit remain pending by assignment.
Acceptance basis: the explicit follow-up authorizes one concise rule in the existing constants section, this handoff, and an owned patch outside the workspace.

## Change and ownership

Updated `.agents/skills/chaos-redux-events/SKILL.md` under `### 7. Duration fields and constants` with one three-sentence paragraph.
It requires reading the installed schema and concept documentation and inspecting the existing group before authoring, placing a matching schema first in every new group, and respecting the inherited schema when adding keys to an existing group.
It explicitly distinguishes a basic brace parse from schema validation.
The rule contains no event IDs, project-private constant names, error history, or source-fix context.
No other skill or guidance was edited, including the committed participant-scope paragraph, frozen transaction frames, parameter prohibition, parchment text, probability workflow, and existing duration guidance.
All original skill bytes and line endings were preserved outside the insertion.
No new skill or routing/AGENTS.md change is needed.

Owned outputs:

- `.agents/skills/chaos-redux-events/SKILL.md`: only the three rule lines and a paragraph-separating blank line.
- `docs/plans/012_africa_plans/subagent_handoffs/012_script_constant_schema_skill_rule_2026-10-03.md`: this new handoff.
- `C:\Users\klimp\AppData\Local\Temp\gods_script_constant_schema_skill_owned_20261003.patch`: the skill-only owned patch; excludes this handoff and every other owner's hunk.

## Exact source authority and lesson

Primary installed schema authority: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md`, lines 1-32, SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
Lines 15-17 require schema as the first entry; lines 18-21 distinguish named `key` from `any_key`; lines 23-30 define `int`, `fixed_point`, or a complex data schema and require matching entries.
The displayed alternatives are explanatory schema options, not instructions to combine mutually exclusive fields.

Installed concept authority and native example: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md`, Script Constants lines 216-245, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
Lines 231-238 demonstrate a category starting with `schema = { any_key = yes data = fixed_point }` before numeric values.
These exact installed files were read directly as requested; this maintenance task does not edit engine-facing source or claim any native execution evidence.
No MCP GUI/tasks or HOI4 launch was used.

Current repository precedent: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\012_africa_gods_constants.txt`, all groups read across lines 1-541, SHA-256 `2bc9b49758513d35a8187ed119b30efa130fccb0b57be6cb374903622b3b5d16` at inspection.
All 24 current groups start with schema and use `any_key = yes`.
Integer namespaces use `data = int`; fractional tuning namespaces use `data = fixed_point`.
The corrected mobile-type group is at lines 514-522, schema 515-518 with `int`; mobile tuning is at lines 524-541, schema 525-528 with `fixed_point`, matching its fractional values.
Representative pre-existing integer and fractional groups are timing at lines 9-37 and armor at lines 126-140.
This read verifies the source pattern; it is not an engine-load or schema-validator result.

The actual source fix was independently verified from commit `16664b3a47988a099ca23e7b7d6779dad454d1ec` and its parent.
The commit inserts the two schema blocks without changing the surrounding constant values.
Before the fix, `gods_of_africa_mobile_type` began at line 514 with `trucks = 1` as its first entry, while `gods_of_africa_mobile` began at line 519 with `units_per_thousand = 1000`; neither group declared a schema.
After the fix, the groups begin at lines 514 and 524 with the matching schema blocks as their first entries.
Parent-version file SHA-256: `6764fda6b785a0b21c18bee4ceef1b490c80238457d2bb3b10ae9cb051e881b6`.
Fix-commit file SHA-256: `45a20b91ef85c0ac3e197ad87505e050259cffcbd66f42874a0ff7c9d12df9dd`.
These historical file hashes differ from the current shared file; no attempt was made to replace or reconcile other owners' source edits.
The earlier authoring attribution to parent commit `42bb46` comes from the assignment; this worker verified the missing-schema source state and the actual correction in `16664b3a4`, without claiming an audit of the earlier commit's full contents.

The factual missing-schema defect is established by the source and installed schema requirement.
The fix commit's message reports a pre-menu crash; that symptom is commit-author testimony, not a native log supplied to or independently observed by this worker.
No native error line or exact engine error text was provided, and none is invented here.
A brace-only parse can accept these missing-schema blocks structurally, so brace success does not establish their schema validity; no claim is made that a particular native parser was executed.

## Owned patch evidence

HEAD at patch generation: `9065313c7c564c219afcc22b1607993dcfd0872b`.
HEAD skill SHA-256: `96a93a51bebf77aa6a255d16ef56b5bd467e4aa65e449c74d65202f4b93673b2`.
Working skill before insertion SHA-256: `0c66c344dad0ef00093ea42f4054c9f797fe2c7861717574e303246cc022f7a6`.
Working skill after insertion SHA-256: `6d2aa61d668e542ccd88fddc2bb572d48e2d9c48fe1348d907a284a47b4975dc`.
Untouched prefix SHA-256: `faa659c15e017f3e5468e5e637aa1fd304ab5c8b518348926f07f27523bd5c09`.
Untouched suffix SHA-256: `78c8040146caff8c8dec170669ed6f45f337c32700c8cdb5009519fe74c5c321`.
Rule lines at edit time: `655-657`.
Owned patch SHA-256: `c8a3a7fda3eb75754c0c96e6697e9687b7997eccc177d0062978decb46085d10`.
Single patch hunk: `@@ -641,6 +641,10 @@`.

The patch adds only the rule paragraph and its separator to the recorded HEAD, with explicit old/new hunk ranges and preserved leading context spaces.
It was manually reviewed and reconstructed against the recorded HEAD in memory; the result matched HEAD plus this owned insertion exactly.
The shared working-tree insertion was separately checked to recover every original byte when removed.
The parent owns review, application to an isolated checkout, and commit.
Do not apply the insertion patch to the shared skill, which already includes the rule.
If the parent's base advances, review/rebase this insertion without taking unrelated changes.

Read-only Git object queries were used solely to verify the expressly named source fix and build the requested owned HEAD-relative patch.
No gameplay edits, Git mutations, index access/update, staging, commit, reset, checkout, or worktree operations were performed.

## Validation and status

The rule was reviewed against the installed first-entry, key-rule, and data-kind requirements and every current source group before patching.
The official skill-creator quick validator accepted the updated events skill; that packaging result does not prove engine schema behavior.
No simplifications, omitted requested output, or remaining source-reference blocker.
Parent review and isolated commit remain pending; no parent-feature completion claim is made.

Skills used: official `skill-creator`, `chaos-redux-events`, and `chaos-redux-subagents`, in the canonical `chaosx_skill_maintainer` role.
Updated: `chaos-redux-events` only.
Created: no new skill.
Left unchanged: all other skills and AGENTS.md.
User review needed: none for the authorized bounded rule; parent review of the owned patch is the requested handoff.
