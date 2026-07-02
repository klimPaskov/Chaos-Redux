# Event 17: implementation handoff, assets, localisation, and acceptance criteria

## Scripted system architecture

The implementation should not duplicate option selection and join logic across player options, AI events, evolutions, and decisions. Use shared helper effects and triggers.

### Required triggers

| Working trigger label | Scope | Purpose |
| --- | --- | --- |
| `is_random_faction_eligible_country` | country | validates selected minors |
| `is_random_faction_allowed_faction_leader` | country | validates faction leaders |
| `can_random_faction_join_faction` | selected country with leader target | validates joining at effect time |
| `is_random_faction_pressure_neighbor` | country | validates neighbor or region pressure target |
| `has_random_faction_active_pressure` | country | shows pressure decisions |
| `is_random_faction_wartime_candidate` | country | permits Evolution II war-adjacent selection |
| `random_faction_region_can_cascade` | global or country context | gates Evolution III cascades |

### Required effects

| Working effect label | Scope | Purpose |
| --- | --- | --- |
| `random_faction_prepare_runtime_context` | global or event root | chooses target and faction options |
| `random_faction_collect_faction_options` | selected country | saves one to four valid faction option targets |
| `random_faction_ai_choose_option` | selected AI country | chooses from saved option targets |
| `random_faction_join_selected_faction` | selected country | joins faction, applies memory, logs result |
| `random_faction_apply_alignment_shock` | selected country | applies temporary spirit and cooldown |
| `random_faction_apply_regional_pressure` | selected country | stores regional pressure and marks neighbors |
| `random_faction_schedule_neighbor_followup` | selected country | schedules Evolution I and higher follow-ups |
| `random_faction_run_evo2_pressure` | selected country or region | applies war-adjacent pressure effects |
| `random_faction_run_evo3_cascade` | region context | selects capped follow-up countries |
| `random_faction_cleanup_country_pressure` | country | clears stale flags, variables, missions, and decisions |
| `random_faction_cleanup_dead_faction_targets` | global or country context | handles dead faction leaders and invalid targets |

### Constants and tuning groups

All major values should be in script constants or documented file-scoped constants when duration fields reject `constant:` values.

Recommended tuning groups:

- option count caps
- recent alignment cooldown duration
- alignment shock duration bands
- neighbor pressure duration
- faction leader reaction cooldown
- Evolution I follow-up delay bands
- Evolution II mission duration bands
- Evolution III cascade count caps
- AI ideology, distance, threat, relation, and war-state weights
- faction cohesion or pressure gains if that value is implemented

### Event targets

Use regular event targets for option scopes when possible:

- `random_faction_target_country`
- `random_faction_option_1_leader`
- `random_faction_option_2_leader`
- `random_faction_option_3_leader`
- `random_faction_option_4_leader`
- `random_faction_selected_leader`
- `random_faction_pressure_source_country`

Global event targets should be avoided unless the implementation needs persistence beyond the event chain. If used, they must be cleared by a cleanup effect.

## Event chain map

The exact IDs can change during implementation, but keep the `chaosx.nr17.*` namespace stable.

| Working event | Role | Visibility |
| --- | --- | --- |
| `chaosx.nr17.1` | entry and runtime preparation | hidden or root event |
| `chaosx.nr17.10` | player selected minor choice event | visible to selected player |
| `chaosx.nr17.20` | AI selected minor choice resolver | hidden |
| `chaosx.nr17.30` | neighbor pressure follow-up | visible if player is affected |
| `chaosx.nr17.40` | faction leader reaction event | visible if player is faction leader |
| `chaosx.nr17.50` | Evolution I regional bloc race follow-up | mixed |
| `chaosx.nr17.60` | Evolution II pressured neutrality incident | mixed |
| `chaosx.nr17.70` | Evolution III cascade resolver | hidden with visible reports where relevant |
| `chaosx.nr17.80` | regional report event for large local cascades | visible report |

## Asset plan summary

The detailed asset prompt is in `prompts/017_random_faction_asset_prompt.md`.

Required visual assets are modest but real:

- decision category icon for bloc pressure
- decision icons for neutrality council, border posts, liaison mission, propaganda networks, guarantee corridor, public commitment, and stabilization
- idea icons for alignment shock, border pressure, bloc polarization, neutrality exhaustion, and liaison mission
- optional report image for Evolution III regional cascade reports
- animated bloc pressure seal with static fallback
- animated warning border or static-only warning frame if animation adds clutter in the existing UI pattern
- achievement icons for the achievement set

No real leader portraits or country flags are required because the event does not create new countries or change public country identities.

## Localisation handoff

Do not paste final wording from this spec. Implementation must write final localisation from these directions.

### Event name and event detail

The event name is `Random faction` as supplied by the user. Event detail text should describe a small country being forced into a faction choice by diplomatic pressure. It should mention that existing factions are used dynamically. It should not describe hidden weights or exact mechanical effects.

### Player country event

Tone direction: anxious, concrete, and country-specific. Mention the selected country and the offered factions. Avoid generic crisis-office prose. Avoid text that says the event is a warning.

Option direction: each option should feel like a distinct forced commitment. The option should name the faction or faction leader through dynamic localisation. One option can sound pragmatic, one ideological, one fearful, and one opportunistic when four options exist, but the final wording must still be tied to actual factions rather than generic moods.

### Neighbor pressure events

Tone direction: civic pressure, military readiness, newspaper talk, party pressure, and border concern. Show that neutrality is becoming expensive without saying that neutrality is doomed.

### Faction leader reaction events

Tone direction: opportunistic and strategic. The faction leader sees a chance to gain a foothold or deny one to a rival. Avoid making every leader sound identical.

### Decision text

Decision names and descriptions should describe visible state action: convening councils, sending staff missions, guarding borders, publishing declarations, funding networks, guaranteeing corridors, and demanding commitments. Tooltips should show concrete costs and named requirements.

### Evolution log direction

Evolution I should read as a regional bloc race. Evolution II should read as pressure on neutral countries becoming militarized. Evolution III should read as a broader collapse of neutrality in parts of the world.

## Achievement set summary

The detailed achievement prompt is in `prompts/017_random_faction_achievement_prompt.md`.

The set should reward:

- surviving a forced faction choice as a minor
- resisting regional bloc pressure as a neutral neighbor
- creating a multi-faction regional border situation
- using faction leader support decisions without breaking the target country
- triggering and surviving Evolution II war-adjacent alignment
- reaching Evolution III while still leaving at least one eligible neutral country outside all factions

Achievements should not unlock just because Event 17 fires.

## Spreadsheet and documentation handoff

After implementation, the spreadsheet worker should update ID 17 with the final in-game event detail, evolution detail, cluster assignment, member severity, and status. The worker must mirror in-game wording rather than paraphrasing when the field is meant to match UI text.

The event doc should live at `docs/events/017_random_faction.md`. It should explain:

- core flow
- player and AI choices
- eligibility rules
- faction option generation
- bloc pressure decisions
- evolutions
- event log behavior
- cluster behavior
- assets and achievement hooks
- known limitations and tuning notes

## Validation expectations for implementation

The implementation completion report should include:

- evidence that Event 17 is registered as Minor Repeatable
- evidence that unreworked default enable behavior is correct for the current project standard
- a check that event name and event detail selectors resolve ID 17
- a check that the event shows unavailable when no eligible country or no valid faction exists
- a check that a human selected country receives one to four valid options and cannot decline all factions
- a check that AI uses the same saved option targets as player options
- a check that Evolution I creates no more than the intended follow-up count
- a check that Evolution II validates wartime and enemy faction cases
- a check that Evolution III uses cascade caps
- a check that pressure decisions hide when their country, faction leader, or region becomes invalid
- a check that scripted localisation does not expose raw triggers
- a check that decision, idea, and achievement asset paths exist after asset production
- a check that the event catalog spreadsheet matches final in-game wording

## Acceptance criteria

The event spec is satisfied only when:

- an eligible minor joins one valid existing faction on each successful baseline firing
- a human selected minor receives one to four faction choices based on the current world faction pool
- the player has no neutral refusal option when directly selected
- AI countries use dynamic faction choice logic
- selected countries, nearby neutrals, and faction leaders receive the planned pressure memory
- Evolution I creates regional bloc race follow-ups
- Evolution II introduces pressured neutrality, wartime eligibility, and border missions
- Evolution III creates capped regional cascades without forcing every eligible country into a faction
- decisions use concrete costs and objectives instead of only political power or command power
- event logs, details, evolutions, docs, assets, achievements, and spreadsheet rows are aligned
- no fallback, simplification, placeholder asset, missing AI behavior, or unwired visible surface is hidden from the completion report
