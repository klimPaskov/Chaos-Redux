# Helper output lifetime skill handoff

Disposition: implemented within the explicitly requested generic skill-capture scope, with parent patch review pending.

## Changed files and ownership

- `.agents/skills/chaos-redux-events/SKILL.md`: only the nine added lines at 163–171 under `Helper output lifetime`, immediately after dynamic-localisation guidance.
- `docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-03_helper_lifetime_skill_rule.md`: this handoff.

The events skill already owns shared-helper and dynamic-localisation guidance, so it is the minimal fit.
The literal `localization_key` rule was already present and remains unchanged.
No new skill was created.
The fully read `chaos-redux-decisions-missions` and `chaos-redux-subagents` skills remain unchanged by this worker.
No routing or AGENTS.md update is needed.
No gameplay, localisation, spreadsheet, test, or other documentation file was edited, and no file was staged or committed.

## Findings and reference identity

Directly read `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 435–442 and 1069–1076.
Line 440 documents that helper-created temporary variables may disappear after return, while storage initialized before the call carries into the helper and retains its modifications.
Lines 1074–1076 describe temporary arrays and their elements using the same variable distinction.
The conservative output contract therefore covers scalar and temporary-array storage, each nested caller, `if.limit`, scripted-localisation `text.trigger`, public API obligations, and actual-source test frames with regular saved state kept separate.

Offline reference SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Pre-edit events skill SHA-256, including other workers' dirty guidance: `AAD544E7C1207F412B7A7E48C83A572D8C3BE926CCA4033680CD7D263AC717EE`.
Post-edit events skill SHA-256 at verification: `4B06BBCC69374923757FF07D9B3ED6273FD8BA6DE1F81D8F865B247924C3324F`.
Unchanged decisions skill SHA-256 at verification: `283033F95CBBB822A66242574EDDE98E425165715CDC5EF035B80F9A5267A745`.

## Exact owned hunk

Apply or isolate only this addition against the existing dirty skill, rather than taking its complete Git diff.

```diff
diff --git a/.agents/skills/chaos-redux-events/SKILL.md b/.agents/skills/chaos-redux-events/SKILL.md
--- a/.agents/skills/chaos-redux-events/SKILL.md
+++ b/.agents/skills/chaos-redux-events/SKILL.md
@@ -161,3 +161,12 @@
 Retain constant-backed temporary getters where the installed documentation supports the assignment, and do not introduce persistent globals solely for formatting.
 
+### Helper output lifetime
+
+Temporary variables first created inside a scripted effect or trigger may disappear after return, while caller-preinitialized storage retains the helper's modifications (`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, line 440).
+
+- Before each helper call, ensure every temporary scalar and temporary-array output consumed afterwards has caller-owned storage, including calls inside `if.limit` and scripted-localisation `text.trigger`. Initialize new output storage without resetting existing input or cursor values.
+- Apply this at every nested call boundary: each caller initializes the outputs it consumes, and outer callers also initialize forwarded outputs needed after return.
+- Public helper API docs must list caller-owned output storage and its required initial values.
+- Actual-source tests must model conservative call-frame cleanup by discarding temporary scalars and arrays first created in the returning helper, retaining modifications to caller-preinitialized storage, and keeping scoped regular saved state separate from temporary storage instead of using one flat global temporary dictionary.
+
 ## Event anatomy
```

## Validation and limits

Removing exactly the added section from the post-edit text reproduces the captured pre-edit text without any other difference, including existing mixed line endings and dirty probability guidance.
The decisions skill hash is unchanged.
Ran `python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-events`, which returned `Skill is valid!`.
Reviewed coverage against every requested generic obligation and the cited offline sections.

No MCP or game calls ran, as explicitly required by the bounded assignment.
No gameplay source tests or runtime validation ran because this patch changes instructions only.
Conservative helper-frame cleanup is a test-model requirement based on documented possible output loss, not proof of the engine's exact internal cleanup implementation in every context.
There are no simplifications or blockers in the requested capture, and parent review must isolate the owned hunk before integration.

Parent review refined the first bullet to distinguish creation of output storage from resetting inherited input or cursor values.
The instruction protects input/output limb arrays and nested traversal state, which must keep their current contents when passed into an in-place helper.

Skills used: `skill-creator`, `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-decisions-missions`.
