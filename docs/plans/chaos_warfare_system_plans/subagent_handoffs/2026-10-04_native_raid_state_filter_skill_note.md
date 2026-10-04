# Native raid target-filter scope skill handoff

Disposition: implemented skill guidance, pending parent review and shared commit.
Acceptance basis: the parent explicitly authorized one narrow paragraph in the existing native-raid skill to capture a recurring scope error exposed by user live QA.

## Changed files and ownership

- `.agents/skills/chaos-redux-native-raids/SKILL.md`: one added paragraph under Scope and dispatch.
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-04_native_raid_state_filter_skill_note.md`: this evidence and review handoff.

The owned paths had no staged or unstaged changes before this edit.
All pre-existing skill rules remain intact.
No gameplay, scripts, generated mirrors, agent definitions, or AGENTS.md changes are part of this handoff.
The parent owns final review and the shared commit.

## Exact added rule

> - Keep physical `target_type` state/province filters actor-neutral unless an explicit actor binding is documented.
>   A native `target_type = { state = { ... } }` filter can evaluate with state `ROOT` (observed engine behavior); do not assume `ROOT` is the actor or infer the province filter's root from this state result.
>   Put actor/victim diplomacy and policy checks in known country preflight (`show_target`, `available`, `launchable`, and `ai_will_do`), using the documented `FROM` target-country binding and explicitly scoped country helpers.
>   Keep AI authorization gates before target desirability boosts.

## Sources and evidence limits

| Source | Read span | Revision | What it establishes |
| --- | --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\_documentation.md` | 63-78 and 95-135 | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` | `ai_will_do`, `show_target`, `available`, and `launchable` use `FROM` for the target country; target state/province variables are available where applicable; `launchable_from` has its own explicitly documented starting-point controller scope. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 253-267 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | `ROOT` and `FROM` depend on the block's context; entering a nested scope does not redefine the root. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\air_raids.txt`, `facility_strike` | 50-67 | SHA256 `4bc5ced6afb625b65dcf01e45cfb6583b555bd8a045b53064675ccfe0ddbc657` | Vanilla puts faction exclusion in `show_target`, war permission in `launchable`, and the physical facility selector in `target_type`. |

The reference context, search, read, and source lookup routes were confirmed exposed and called with their live schemas.
The initial general context omitted Scopes because of its result limit; targeted search and revision-bound reading covered the relevant Scopes table instead.
The installed raid documentation was found through a targeted `show_target` search and read through the reference route.
Source lookup returned no `facility_strike` definition for kind `raid`, so the exact installed vanilla file was read directly and its SHA256 retained.
This lookup limitation does not invalidate the directly read precedent.

The parent reports that actual native state-target evaluation supplied state `ROOT`, causing country-only `is_in_faction_with`, `is_subject_of`, and `has_war_with` calls in an actor-assuming state profile to fail.
That observation is supplied live-QA evidence, not a new engine observation by this worker and not a rule documented by the cited raid section.
The province-filter recommendation is a conservative scope rule inferred from the context-dependent root contract; this handoff makes no claim that province filters share the observed state-root behavior.
Keeping physical filters separate from diplomacy/policy prevents reuse of a helper that silently assumes actor-country `ROOT` when the engine invokes it as a standalone state filter.
Keeping authorization gates ahead of AI desirability boosts preserves the parent-owned permission contract while moving only the physical filter boundary.

## Validation and remaining work

The existing skill already owns native raid scope and dispatch, so no new skill or routing change is needed.
The edit was checked against its previous content to ensure it adds only the authorized paragraph and preserves all other rules.
`python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-native-raids` passed.
That validator checks package structure only; it does not establish engine behavior.
The parent reports 88 source cases passing for its separate gameplay repair; this worker did not run or claim those cases independently.
Absence of the actual engine warnings after the repair remains pending user live QA.
No game launch occurred, and no fallback or simplification was introduced.
