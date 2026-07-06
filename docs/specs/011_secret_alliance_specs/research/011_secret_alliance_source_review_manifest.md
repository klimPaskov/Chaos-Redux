# Event 011 Source Review Manifest

This manifest records the references used before creating the Secret Alliance source spec package. It is not a completion report for gameplay implementation.

## Repo Instructions And Skills

Required project instructions:

- `AGENTS.md` repository instructions supplied in the task

Skills read and applied:

- `chaos-redux-event-planning`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `hoi4-decisions-missions`
- `hoi4-mtth`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`

## Offline Paradox Wiki Snapshot

The required offline wiki snapshot under `paradox_wiki/` was consulted. Web Paradox wiki pages were not used.

Core pages:

- `Data structures - Hearts of Iron 4 Wiki.md`
- `Triggers - Hearts of Iron 4 Wiki.md`
- `Effects - Hearts of Iron 4 Wiki.md`
- `Modifiers - Hearts of Iron 4 Wiki.md`
- `Localisation - Hearts of Iron 4 Wiki.md`
- `Scopes - Hearts of Iron 4 Wiki.md`
- `On actions - Hearts of Iron 4 Wiki.md`
- `Event modding - Hearts of Iron 4 Wiki.md`
- `Decision modding - Hearts of Iron 4 Wiki.md`
- `Idea modding - Hearts of Iron 4 Wiki.md`
- `AI modding - Hearts of Iron 4 Wiki.md`

Event-specific adjacent pages:

- `Faction modding - Hearts of Iron 4 Wiki.md`
- `Interface modding - Hearts of Iron 4 Wiki.md`
- `Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `Intelligence agency modding - Hearts of Iron 4 Wiki.md`
- `Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `Sound modding - Hearts of Iron 4 Wiki.md`

Key reference implications:

- Persistent long-lived scope pointers need global event targets and explicit cleanup.
- Regular event targets are suitable inside short event chains.
- Decisions and missions need clear `visible`, `available`, `target_root_trigger`, target cleanup, and AI weights.
- On-action use must stay narrow. This package does not approve recurring `on_daily`, `on_weekly`, or `on_monthly` world iteration.
- Localisation and scripted localisation must be planned with UI support and final encoding constraints.

## Vanilla Documentation And Examples

Vanilla docs consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`:

- `effects_documentation.md`
- `triggers_documentation.md`
- `modifiers_documentation.md`
- `script_concept_documentation.md`
- script constants documentation under `common/script_constants/documentation.md`

Vanilla precedents:

- `common/factions/_documentation.md`
- `common/factions/templates/generic_factions.txt`
- `common/decisions/WTT_border_conflicts.txt`
- vanilla decision examples using targeted decision patterns and faction creation flows

Key reference implications:

- Use `create_faction_from_template`; raw `create_faction` is documented as deprecated.
- Border-war actions should mirror WTT-style paired-state setup, timeout, cleanup, and `change_state_after_war = no` unless a later design explicitly adds territorial stakes.
- Faction reveal should use a template and must verify dynamic faction name display before implementation.
- Script constants are preferred for shared tuning, but unsupported fields need variable assignment, file-scoped constants, or meta effects.

## Chaos Redux Precedents

Relevant existing package:

- `docs/specs/017_random_faction_specs/`

Useful patterns:

- Dynamic country selection and validation.
- Event-owned systems that persist after the opening event.
- Decision category values that represent live pressure rather than static flavour.
- Event log actor mapping and event detail mapping.
- Architecture matrices and follow-up prompts as source package companions.

Existing Event 011 references found:

- `common/scripted_effects/chaosx_logic_effects.txt` includes Event 011 in fire-once arrays as unavailable.
- `localisation/english/chaosx_event_names_l_english.yml` maps Event 011 to an unavailable placeholder.
- Existing scripted localisation mapping files already resolve Event 011 through `chaosx.event_name.11`.

No existing source spec or implemented Event 011 script package was found before this spec was created.

## Subagent Handoffs

The following bounded subagents were used with `fork_context=false`:

- `chaosx_improvement_loop_planner`: wrote `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_addendum.md`
- `chaosx_scripted_system_architect`: wrote `docs/plans/011_secret_alliance_plans/011_secret_alliance_scripted_system_architecture.md`
- `chaosx_decision_mission_auditor`: wrote `docs/plans/011_secret_alliance_plans/011_secret_alliance_decision_mission_handoff.md`
- `chaosx_super_event_text_researcher`: wrote `docs/plans/011_secret_alliance_plans/011_secret_alliance_super_event_text_research.md`

The source spec promotes their accepted recommendations and leaves their original files as working evidence.

