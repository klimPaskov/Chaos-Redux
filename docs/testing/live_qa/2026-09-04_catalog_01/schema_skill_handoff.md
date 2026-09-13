# Startup schema skill handoff

Disposition: implemented within the parent-authorized skill-only scope.

Updated `.agents/skills/chaos-redux-debug-playtest/SKILL.md`, section 7, with exactly seven sentences immediately before the existing `check_variable` triage note.
The exact addition is:

```diff
+For a repeated pre-menu crash with an empty fresh `error.log`, check `common/script_constants/` category schemas early; the empty log does not prove successful startup.
+Read installed vanilla `common/script_constants/documentation.md` and the Script Constants section of `documentation/script_concept_documentation.md`: each category requires `schema` as its first entry, and scalar declarations use `data = int` or `data = fixed_point`, not `any_value`.
+Preserve valid array declarations using the installed `common/script_constants/country_groups.txt` (`array = country`) and `state_groups.txt` (`array = state`) precedents; absence of scalar `data` alone is not an array-schema defect.
+Repair confirmed declaration defects without changing tuning values, constant names, or consumers.
+A parsed-object key recovered from a crash dump is an investigative lead, not proof that the named entry alone caused the crash; shortening or removing it does not establish a cause without a successful controlled retest.
+Resolving an early parse crash can expose a large downstream error batch that earlier launches never reached, so distinguish newly observable errors from demonstrated patch regressions using the recorded evidence.
+Keep the clean-start gate pending until the required main-menu and country-map observations and fresh-log checks pass.
```

Authoritative references read under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`: `common\script_constants\documentation.md` lines 16–27 require the schema first and document scalar `data`; `documentation\script_concept_documentation.md` lines 216–245 document constant injection and a scalar schema; `common\script_constants\country_groups.txt` lines 1–5 and `state_groups.txt` lines 1–5 establish the valid array schemas separately.
The required offline wiki core pages were opened, and `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` constants guidance was consulted alongside vanilla.
The crash progression and unsuccessful isolated-entry experiments are parent-supplied observations, not independently reproduced by this subagent.

Used `skill-creator` and read the target debug-playtest skill for maintenance only; its existing triage was the appropriate owner, so no new skill was created and all other skills were left unchanged.
The skill validator passed, and the added schema guidance was checked against the installed scalar and array references.
Preserved the existing generic-skill-reference removal and comparison-syntax addition, along with launch limits, authorization, routing, and MCP instructions.
No gameplay, AGENTS.md, configuration, desktop, process, staging, or commit actions were performed.
No simplifications or blockers for this bounded documentation task; gameplay repair and successful startup remain outside this handoff's validation claim.
