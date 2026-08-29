# Conditional Subagent Prompt: Event 021 Skill Maintainer

Use this prompt only when Event 021 implementation reveals a reusable workflow, repeated mistake, or project-wide rule not already covered by the current skills.

Spawn `chaosx_skill_maintainer` with `fork_context=false`.

Read:

- repository `AGENTS.md`
- the owning existing skill
- the Event 021 implementation evidence that revealed the reusable rule
- related helper documentation and audit findings

Update an existing skill when the workflow belongs there. Create a new skill only when the workflow is distinct and broadly reusable.

Do not put Event 021-specific design, country names, route names, constants, or implementation history into a skill.

Record:

- reusable rule
- source paths
- exact reason it prevents future rediscovery
- examples
- validation or handoff requirement
- routing impact
- files changed

Do not edit gameplay files.

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/skill_maintainer_handoff.md`
