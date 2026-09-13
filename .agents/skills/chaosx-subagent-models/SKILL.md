---
name: chaosx-subagent-models
description: Use when spawning a Chaos Redux subagent in DSH and the child model or reasoning effort matters, including choosing max reasoning for a premium or top-tier model, deciding whether a role should run on the default model, or checking why a subagent ignores a model named in its Codex TOML.
---

# Chaos Redux Subagent Model Policy

Use this skill when a Chaos Redux subagent is spawned on DSH and the child's model or reasoning effort is part of the decision.

The role, ownership, and routing rules for those subagents live in `chaos-redux-subagents`. This skill covers only which model the child runs on.

## The default

DSH subagents default to **DeepSeek 4.1 Flash with high reasoning effort**.

| Setting | Value | Meaning |
| --- | --- | --- |
| provider | `deepseek-official` | The route owned by `dsh-llm-deepseek` |
| model | `deepseek-flash` | Published in the adapter catalog as `DeepSeek-V41-Flash` |
| reasoning effort | `high` | One of `off`, `low`, `high`, `max` |

That default is configured outside this repository, in the active DSH profile's `cordis.patch.yml`, on the `tool-subagent` row's `agentOptions`.
It applies to every role, so the ordinary case needs no model decision at all: spawn the subagent and say nothing about models.

## Max reasoning for premium models

When a role is deliberately routed to a premium or top-tier model rather than the default, raise the reasoning effort to **max**.

Treat a model as premium when it is not the default Flash model, for example a Pro-class or a project-named top-tier model such as `sol` or `astra`.
For those children, request `max` rather than accepting the inherited `high`.

## What this policy cannot do

These are engine constraints, not preferences, and they must not be worked around by inventing a capability.

- **The Codex TOML model names do not apply.** DSH does not read `.codex/agents/*.toml`, so a named role does not arrive with the model its TOML names. `model = "gpt-5.6-sol"` in a TOML is a Codex setting and has no effect on a DSH child.
- **`subagent_fork` cannot select a child model.** The shipped fork tool inherits the parent's provider and model so the copied conversation prefix stays eligible for KV Cache reuse. Use the ordinary `subagent` tool when the model matters.
- **Per-call model and effort fields need a per-session opt-in.** The tool exposes `provider`, `model`, and `reasoning_effort` only when a session carries an enabled model-selection policy recorded at session composition. A running session cannot gain that policy retroactively, and a restored session without a recorded policy stays disabled.
- **A model id can be unlisted and still work.** Catalog membership is advisory: the adapter validates the effective route, and an unlisted id is accepted when its adapter supports it. Do not report a model as unavailable only because it is missing from a discovery listing.

If a required route is genuinely unavailable, report the exact blocker instead of silently running the work on the default model and presenting it as the requested route.
