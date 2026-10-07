# Idea lookup skill maintenance handoff — 2026-10-07

Disposition: `implemented` for the bounded skill addition, subject to parent review.
Acceptance basis: the explicit maintenance request authorizes one generic addition inside the asset skill's Idea and national spirit section plus this handoff.

## Context and ownership

The parent reported a proven native idea-picture lookup defect during Event 029 Riches Found work and requested reusable consumer lookup guidance.
This worker verified the generic offline and installed-native references; it did not inspect or repair Event 029 consumers or assess its asset package.
Event-specific context remains in this handoff only.

Changed files:

- `.agents\skills\chaos-redux-event-assets\SKILL.md`: four instruction lines and one blank line added at lines 378–382, solely inside `### Idea and national spirit icons`.
- `docs\plans\029_riches_found_plans\subagent_handoffs\idea_lookup_skill_2026_10_07.md`: this maintenance receipt.

The target skill had no staged or unstaged diff before the edit, and the handoff path did not exist.
The reviewed skill diff contains only the owned addition below; concurrent work elsewhere was left untouched.
No gameplay, assets, XLSX, GFX, index, commits, or generated runtime definitions were changed, and no children were spawned.

## Exact owned hunk

Insert immediately after the existing compact-art paragraph and before the visual-components background paragraph:

```diff
+Trace the consumer's actual prefix contract and default override before wiring: idea `picture = my_icon` resolves to `GFX_idea_my_icon`, while an existing `GFX_idea_<idea_id>` takes precedence even over explicit `picture`.
+Do not pass `GFX_idea_my_icon` as the picture value; it requests `GFX_idea_GFX_idea_my_icon`.
+Verify the exact expected alias, any automatic idea-id override, and its texture path across mod and vanilla definitions, and record the resolved consumer-to-alias mapping in the handoff while preserving stable identifiers unless a lookup correction requires a change.
+Check each consumer independently: decision and category `icon` fields accept both suffixes and full `GFX_decision_`/`GFX_decision_category_` names, so never apply blanket `GFX_` stripping.
+
```

The existing skill already owns asset naming, icon type separation, and stable wiring, so no broader instructions were duplicated or rewritten.
Before this addition, the Idea and national spirit section described visual production without stating the native picture lookup contract.
The addition requires resolving the expected alias and automatic override before wiring, preserving stable identifiers, and treating decision icon lookup separately.
No runtime identifiers were changed.

## Reference evidence

Connected `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` routes were exposed and returned `status = ok` for the relevant calls in workspace `mod_chaos_redux_ea3b2d67c2c0`.
The exact sections and native blocks were also read directly from their Windows paths before the patch.

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Idea modding - Hearts of Iron 4 Wiki.md`, Picture, lines 65–101; revision/SHA-256 `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac`; MCP section `f59bc90828b19ec433a26f04e65ba449e46d6d68ea63eedaccc4f90ce06e9c83`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, Icon, lines 111–127; revision/SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; MCP section `897da3425dcc6c64071f5b44e614cca80dfc0bba596d11e3db0a008f6b0e61de`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\ideas\afghanistan.txt`, lines 222–235: `AFG_democratic_influence` uses `picture = generic_democratic_drift_bonus`; physical SHA-256 `6552a3a0f024e52b941426e5b02cc2aec3129306139ccf31b6d75f7697cf6d30`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\ideas.gfx`, lines 594–597: `GFX_idea_generic_democratic_drift_bonus` points to `gfx/interface/ideas/generic_democratic_drift_bonus.dds`; physical SHA-256 `73b5be871c2e1d1df14b4bf8b6456c5231f5305742dcd41051074b56c330544f`.

Both focused native `source_lookup` results used workspace-index revision `9c62af0e1935d4a63c52c9fefe6befbd40acec0a2d809486c06703f834a3f57f`, returned one complete, unshadowed definition without truncation, and deliberately excluded references.
The idea context bundle had no missing or omitted required sources; its installed-documentation selection was the general Modifiers introduction, which does not establish picture lookup semantics.
The exact `GFX_idea_` search across offline and installed documentation returned only the cited wiki Picture section; a direct bounded search of installed `documentation` and idea documentation for picture/prefix terms found no matching picture-contract documentation.
The optional `script_doc` corpus was reported unavailable with zero files; no unavailable corpus is claimed as read.
The prefix and automatic override rule is supported by the offline Picture section, while the installed native pair corroborates the suffix-to-alias convention rather than independently proving override precedence.

## Validation and limits

Read `AGENTS.md`, official `skill-creator`, `chaos-redux-event-assets`, and `chaos-redux-subagents` in full.
Ran `python -X utf8 -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-event-assets`; result: `Skill is valid!`.
Reviewed the exact final skill diff against both lookup sections and the native suffix/alias pair.
The owned addition contains generic examples only and preserves the decision/category full-name exception.
The validator covers skill structure, not native rendering or runtime correctness.
No live HOI4 launch, visual asset acceptance, or package coverage audit was performed or claimed.

Skills used: `skill-creator`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
Updated: `chaos-redux-event-assets` only.
Created skills: none.
Other skills and `AGENTS.md` remain unchanged; no routing or subagent-definition update is needed.

No simplifications, omissions, or blockers within the requested maintenance scope.
Parent review remains required; Event 029 gameplay repairs, consumer-specific evidence, asset acceptance, and package completion remain with the parent.
