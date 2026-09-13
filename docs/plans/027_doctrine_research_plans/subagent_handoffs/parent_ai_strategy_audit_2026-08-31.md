# Event 027 AI strategy audit handoff

> **Superseded status notice (2026-09-01):** This dated AI strategy handoff is preserved as historical source evidence and is superseded as a current MCP status authority by ../documentation_state.md. Its Transport closed statement is stale after the fresh bounded Event 027 calls, and probability acceptance remains open.

## Scope

This parent-owned audit closes the source-level Event 027 AI strategy gap identified by the earlier probability handoff. It does not claim the mandatory MCP probability evidence, because the current HOI4 MCP transport returns `Transport closed` before analysis.

## Finding and disposition

The previous domain scorer added the strategy weight only when one of four country flags existed: `doctrine_research_ai_strategy_army`, `doctrine_research_ai_strategy_navy`, `doctrine_research_ai_strategy_air`, or `doctrine_research_ai_strategy_special_forces`. No source producer set those flags, and Chaos Warfare had no corresponding strategy signal. Those gates therefore contributed zero in ordinary play.

The current implementation removes those dead flag-only gates and uses explicit fail-closed scripted triggers in `common/scripted_triggers/027_doctrine_research_triggers.txt`:

- `doctrine_research_ai_has_army_strategy_signal` reads active land doctrine, native AI role templates, and current offensive or defensive war posture.
- `doctrine_research_ai_has_navy_strategy_signal` reads active naval doctrine, fleet and convoy presence, and naval production capacity.
- `doctrine_research_ai_has_air_strategy_signal` reads active air doctrine and deployed aircraft by supported role.
- `doctrine_research_ai_has_special_forces_strategy_signal` reads active Special Forces doctrine, native AI special-forces role templates, and supported special-forces template content.
- `doctrine_research_ai_has_chaos_warfare_strategy_signal` reads active Chaos Warfare doctrine or the owning CBRN AI viable-program signal.
- `doctrine_research_ai_has_selected_domain_strategy_signal` dispatches the selected domain to the corresponding signal for Grand Doctrine and track scoring.

The domain scorer applies the strategy weight only after the domain validity adapter succeeds. The Grand Doctrine and track scorers apply the same selected-domain strategy signal, while their existing force, production, war, geography, theater, completion, continuity, and owner-readiness factors remain independent. Subdoctrines inherit the selected track's strategy contribution and continue to receive their own force-fit and completion scoring.

## Source references

- `common/scripted_triggers/027_doctrine_research_triggers.txt`
- `common/scripted_effects/027_doctrine_research_effects.txt`
- `common/scripted_effects/027_doctrine_research_ai_effects.txt`
- `common/script_constants/027_doctrine_research_constants.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`

The installed vanilla documentation lists target-specific `ai_strategy_*` dynamic values but no generic targetless trigger for arbitrary internal AI strategy-plan entries. The implementation therefore uses documented native observable outputs and does not invent an undocumented readback path.

## Parent validation

- The four unproduced `doctrine_research_ai_strategy_*` flag references are absent from Event 027 gameplay sources.
- The Chaos strategy factor is now present through the owning `cbrn_chaos_warfare_ai_has_viable_program` signal.
- Strategy-factor call sites exist in the domain, Grand Doctrine, and track scorers.
- All changed Event 027 script files remain brace-balanced.
- The MCP runtime still needs a fresh baseline/final probability audit and same-scenario comparison after transport recovery.

## Remaining blocker

This handoff closes the source-level AI strategy defect only. It does not close runtime proof for strategy-sensitive probability scenarios, because the HOI4 MCP endpoint currently returns `Transport closed` for both Event and probability routes.
