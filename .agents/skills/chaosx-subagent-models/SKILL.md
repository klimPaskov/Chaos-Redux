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

## Selecting a model or effort per call

Model selection is enabled in this deployment, so the `subagent` tool accepts `provider`, `model`, and `reasoning_effort` on a call and a `list_subagent_models` tool reports the allowed routes.

Two engine rules govern those fields.

- **Provider and model are one route and must be supplied together.** Supplying only one is rejected. Effort may be supplied alone, because the configured default already fixes the route.
- **Changing the route without an explicit effort clears the configured effort**, so the newly selected model falls back to its own default. Always pass `reasoning_effort` explicitly when you switch models, or a premium model will silently run below `max`.

The authorized routes are `deepseek-official/deepseek-flash` and `deepseek-official/deepseek-v4-pro`. An unauthorized route is rejected before the child starts, so do not attempt an unlisted provider.

### What takes effect when

The opt-in is sampled **when a session is composed**, and the resulting route list is then recorded in that session.

A session that started before the opt-in was enabled does not gain these fields, and a restored session without a recorded policy stays disabled. Do not report a missing `reasoning_effort` field as a broken configuration: it means that session predates the opt-in, and a newly composed session will expose the fields.

## What this policy cannot do

These are engine constraints, not preferences, and they must not be worked around by inventing a capability.

- **The Codex TOML model names do not apply.** DSH does not read `.codex/agents/*.toml`, so a named role does not arrive with the model its TOML names. `model = "gpt-5.6-sol"` in a TOML is a Codex setting and has no effect on a DSH child.
- **`subagent_fork` cannot select a child model.** The shipped fork tool inherits the parent's provider and model so the copied conversation prefix stays eligible for KV Cache reuse. Use the ordinary `subagent` tool when the model matters.
- **A model id can be unlisted and still work.** Catalog membership is advisory: the adapter validates the effective route, and an unlisted id is accepted when its adapter supports it. Do not report a model as unavailable only because it is missing from a discovery listing.

If a required route is genuinely unavailable, report the exact blocker instead of silently running the work on the default model and presenting it as the requested route.
