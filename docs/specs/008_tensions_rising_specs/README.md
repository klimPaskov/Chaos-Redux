# Event 008 Tensions Rising: Planning Package

## Authority and current navigation

Event 8 is implemented in source; the catalog status is `Needs Testing`, and runtime, GUI, probability, and provenance validation remain open.
The [owner decisions](../../plans/008_tensions_rising_plans/agent_decisions_2026-10-05.md) and [balance decisions](../../plans/008_tensions_rising_plans/balance_evidence_2026-10-06/owner_balance_decisions.md) record the corrections the parent accepted on 5 and 6 October 2026, and the specs describe them as current design.
The [owner state map](../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md) separates source design, implementation evidence, and blocked validation; `docs/events/008_tensions_rising/overview.md` is the implementation-facing record.
Broader design acceptance remains unresolved where no decision is cited, and new design lives only in Open questions.
Select remaining work from the [coding prompt](prompts/008_tensions_rising_coding_prompt.md).
Current workflows belong to [chaos-redux-events](../../../.claude/skills/chaos-redux-events/SKILL.md), [chaos-redux-event-assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [chaos-redux-subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Files

| Path | Role |
| --- | --- |
| `specs/008_tensions_rising_spec.md` | Main spec: identity, visible values, stages, pulse, relations, reports and incidents, connections, cluster, achievements, AI, limits |
| `specs/008_tensions_rising_evolutions_and_hidden_effects.md` | Stage availability, package table, pulse rules, selector, posture ideas, incident pools |
| `specs/008_tensions_rising_event_log_and_localisation.md` | Writing direction and localisation key map |
| `matrices/008_tensions_rising_constants_and_helpers.md` | Installed helpers, constant blocks, state lifecycle |
| `matrices/008_tensions_rising_ai_matrix.md` | AI posture layer and remaining AI directions |
| `matrices/008_tensions_rising_cluster_and_achievements.md` | Unresolved cluster record and achievement designs with tracking limits |
| `prompts/008_tensions_rising_coding_prompt.md` | Remaining source work and decision-gated work |
| `prompts/008_tensions_rising_goal_prompt.md` | Compact `/goal` prompt for the remaining work |
| `prompts/008_tensions_rising_asset_prompt.md` | Installed assets and the provenance item |
| `research/008_tensions_rising_catalog_row.md` | Read-only workbook facts and pending wording |
| `research/008_tensions_rising_context_digest.md` | Historical intake context |
| `package_manifest.md` | Package inventory |

## Core design summary

Event 8 stays a Minor Repeatable global pressure event.
Its baseline Calm World form requests `+2` world tension and fires only while world tension is below full.
Diplomatic Fever stages I-IV, unlocked by Chaos tier and their evolution checkboxes, request `+3/+5/+8/+12` world tension and add `+10/+15/+25/+50` Chaos, can fire at full tension, and add a capped timer pulse, timed relation shocks, AI posture ideas, and at most one delayed incident per report batch.
Stage III+ incidents can rarely start safe non-transfer border clashes, and Stage IV is the strongest non-terminal pressure.
Automatic shocks follow a 30-day cadence, and one report per recipient shows only the world tension and Chaos actually changed.
The event deliberately offers the player no decisions: its role is atmospheric pressure, and response belongs to ordinary diplomacy.

No super-event, world-end scenario, country package, focus tree, or formable is included.

## Open questions

Each item is `unresolved` until the user, parent, or named owner records a disposition.
Items marked "proposed (spec audit 2026-10-10)" are new design from the 10 October audit, not accepted design.

1. Cluster record.
   Current source registers `Diplomatic Panic` (Event 8 required Low, Event 17 optional Low), while the workbook lists four-member `Diplomacy` (8/17/36/59, Medium/Medium/High/High); the cluster owner must choose.
   Proposed (spec audit 2026-10-10): whichever record is chosen, list Event 8 at Low severity, because after the 6 October ladder a single firing adds at most 12 requested threat and the event no longer carries Medium pressure on its own.
2. Follow-up pool order.
   Proposed (spec audit 2026-10-10): replace the Stage II+ recent-relation-damage priority branch with a weight bonus for the same incidents inside each stage pool.
   Every Stage II+ root applies relation damage, so that branch currently wins almost always, hiding the insurance incident, Staff Cars After Midnight, and the Insurance Market achievement; the change needs a before-and-after comparison on the owner's declared scenarios.
3. Relation-selector fallbacks.
   Proposed (spec audit 2026-10-10): when the cooldown-respecting pass finds no valid pair, apply fewer pairs rather than falling back to recently hit actors.
   This keeps the same majors from absorbing every shock and makes Diplomatic Blackout reward spread rather than repetition.
4. Border clash outcomes.
   Proposed (spec audit 2026-10-10): replace the clash results' political-power swing with the stage's border-alarm opinion modifier between the two countries, kept alongside the existing war-support and stability effects, so a clash leaves a diplomatic scar instead of a generic resource change.

The incident world-tension rescale is not an open question: it repairs consistency with the accepted ladder and the accepted smaller-aftershock role, and it is listed in the coding prompt.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency: every document now uses the accepted 6 October 2/3/5/8/12 ladder and 30-day cadence instead of the superseded `+100` to `+1000` values, the in-game stage titles and Total Chaos tier name, the implemented opinion values, posture ideas, follow-up pools, and incident event IDs, and the current two-member source cluster beside the workbook record.
The localisation spec's pasteable drafts and the helper matrix's proposal tables were replaced by key and helper maps, the consumed achievement, scripted-system, and localisation-audit prompts and the stale goal-length receipt were removed, the coding, goal, and asset prompts now list only remaining work, and `.agents/skills` links point to `.claude/skills`.
Pass 2, design: the spec limits player-facing values to the batch's actual world-tension and Chaos change, records the real Chaos Meter, timer, and Event 011 connections, adds the incident aftershock-scale rule (incidents at 25-75 currently exceed the Stage IV root of 12), and adds four proposals on cluster severity, follow-up pool order, selector fallbacks, and clash outcomes.
Not edited here: `docs/events/008_tensions_rising/overview.md` still lists the superseded world-tension values.
