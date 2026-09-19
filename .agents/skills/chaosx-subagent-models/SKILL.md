---
name: chaosx-subagent-models
description: Use when spawning a Chaos Redux subagent in DSH and the child model or reasoning effort matters, including applying the standing rules that every subagent defaults to deepseek-flash, that the 3D model pipeline worker runs sol at high effort, that astra needs explicit permission, deciding whether a role should run on the default model, or checking why a subagent ignores a model named in its Codex TOML.
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

## Routes

Every Chaos Redux subagent on DSH runs on `deepseek-official/deepseek-flash`, except the 3D model pipeline worker, which runs on `sol` by default.

| Route | Status |
| --- | --- |
| `deepseek-official/deepseek-flash` | The default route for every subagent |
| `openai/gpt-5.6-sol` | The 3D model pipeline worker's default route |
| `openai/gpt-6-astra` | Permission-gated. Never spawned without explicit user permission for that run |
| `deepseek-official/deepseek-v4-pro` | Forbidden. Never spawn a subagent on it, not even for a role that looks like it needs stronger reasoning |
| any other provider or model | Forbidden without a fresh explicit user instruction |

Naming `provider` and `model` on a `subagent` call is still allowed, but the only value pair that may be supplied for an ordinary subagent is `deepseek-official` with `deepseek-flash`. The ordinary case is simpler: say nothing about the model and let the configured Flash default apply. If a task seems to need a stronger model than the route allows, split it into narrower bounded subagents instead of escalating the model.

The 3D model pipeline worker is the one exception, and it is a route decision rather than a different role. Spawn `chaosx_3d_model_pipeline` on **`sol` at `high` reasoning effort by default**. `sol` is the `openai` catalog route published as `gpt-5.6-sol`.

Do not spawn that worker on `astra`, published as `gpt-6-astra`, unless the user grants permission for that specific run. A standing instruction to use manual Blender rigging, animation, or repair authorizes the Blender work itself and never authorizes the `astra` model route. When permission has not been granted, `sol` high is the route; ask once if `astra` looks warranted, and never treat the request as granted by default.

`gpt-6-astra` still appears throughout the 3D pipeline, event-planning, improvement-loop, event-assets, and subagents skills as the authoring identity recorded in handoffs, checkpoints, and provenance evidence. Keep writing it there. It describes who authored the Blender work, not which model spawns the child.

## Selecting a model or effort per call

Model selection is enabled in this deployment, so the `subagent` tool accepts `provider`, `model`, and `reasoning_effort` on a call and a `list_subagent_models` tool reports the allowed routes.

Two engine rules govern those fields.

- **Provider and model are one route and must be supplied together.** Supplying only one is rejected. Effort may be supplied alone, because the configured default already fixes the route.
- **Changing the route without an explicit effort clears the configured effort**, so the newly selected run falls back to its own default. This matters only if the route itself ever changes; under these route rules, leave the route alone and pass `reasoning_effort` explicitly whenever the effort needs to be stated.

The authorized routes are the ones in the table above. An unauthorized route is rejected before the child starts.

### What takes effect when

The opt-in is sampled **when a session is composed**, and the resulting route list is then recorded in that session.

A session that started before the opt-in was enabled does not gain these fields, and a restored session without a recorded policy stays disabled. Do not report a missing `reasoning_effort` field as a broken configuration: it means that session predates the opt-in, and a newly composed session will expose the fields.

## What this policy cannot do

These are engine constraints, not preferences, and they must not be worked around by inventing a capability.

- **The Codex TOML model names do not apply.** DSH does not read `.codex/agents/*.toml`, so a named role does not arrive with the model its TOML names. `model = "gpt-5.6-sol"` in a TOML is a Codex setting and has no effect on a DSH child.
- **`subagent_fork` cannot select a child model.** The shipped fork tool inherits the parent's provider and model so the copied conversation prefix stays eligible for KV Cache reuse. Use the ordinary `subagent` tool when the model matters.
- **A model id can be unlisted and still work.** Catalog membership is advisory: the adapter validates the effective route, and an unlisted id is accepted when its adapter supports it. Do not report a model as unavailable only because it is missing from a discovery listing.

If a required route is genuinely unavailable, report the exact blocker instead of silently running the work on the default model and presenting it as the requested route.
