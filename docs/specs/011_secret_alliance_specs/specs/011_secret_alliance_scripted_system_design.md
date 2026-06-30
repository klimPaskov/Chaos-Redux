# Event 011 Secret Alliance Scripted System Design

This file maps reusable scripted helpers, variables, flags, and cleanup responsibilities for implementation. Names are proposed working names and can be adapted to existing repository naming conventions.

## Main scopes

| Scope | Responsibility |
| --- | --- |
| Global | Stores the compact membership arrays, active state, stage, public reveal state, and selected target country pointer if needed |
| Target country | Stores player suspicion, preparedness, evidence, dossier category state, selected dossier target, and response route flags |
| Pact leader or convenor | Stores pact cohesion, aggression, war readiness, and leadership role state if global storage is not preferred |
| Member country | Stores membership, role, commitment, identified state, public state, isolation, defection, and incident cooldown flags |
| State scopes | Stores sabotage targets, guarded rail hubs, border incident states, and temporary damage markers |

## Proposed variables

| Variable | Scope | Meaning |
| --- | --- | --- |
| secret_alliance_stage | Global or target | 0 baseline, 1 Evolution I, 2 Evolution II, 3 Evolution III |
| secret_alliance_secrecy | Global or target | Hidden proof difficulty |
| secret_alliance_cohesion | Global or convenor | Internal unity |
| secret_alliance_aggression | Global or convenor | Incident pressure and war appetite |
| secret_alliance_war_readiness | Global or convenor | Public faction war preparation |
| secret_alliance_member_count | Global | Current valid member count |
| secret_alliance_major_count | Global | Valid major member count |
| secret_alliance_suspicion | Target | Player-facing suspicion after dossier opens |
| secret_alliance_evidence | Target | Quality of proof |
| secret_alliance_preparedness | Target | Defensive readiness |
| secret_alliance_selected_target_id | Target | Human UI selected country id if the repo uses id storage |
| secret_alliance_recent_incident_score | Target | Used for pacing and tooltips |

Use integer formatting for values shown to the player. If percentages are used, show whole percentages unless fractional precision changes decisions.

## Proposed flags

| Flag | Scope | Meaning |
| --- | --- | --- |
| secret_alliance_active | Global | Event 011 compact is active |
| secret_alliance_public | Global | Compact is publicly revealed |
| secret_alliance_dossier_open | Target | Player can see dossier category |
| secret_alliance_target | Country | Country targeted by the compact |
| secret_alliance_member | Country | Country is a compact member |
| secret_alliance_founder | Country | Country is a founding member |
| secret_alliance_convenor | Country | Country hosted the first compact |
| secret_alliance_purse_holder | Country | Country funds operations |
| secret_alliance_knife_hand | Country | Country handles hard operations |
| secret_alliance_patron | Country | Major patron role |
| secret_alliance_identified_by_target | Country | Target has proof of this member |
| secret_alliance_public_member | Country | Country has joined the public faction |
| secret_alliance_defector | Country | Country defected from compact |
| secret_alliance_isolated_from_war_call | Country | Rare outcome from player diplomacy |
| secret_alliance_recently_invited | Country | Invitation cooldown |
| secret_alliance_recently_sabotaged | State or country | Prevents repeated damage on same place |

## Proposed scripted triggers

| Trigger | Scope | Inputs | Purpose |
| --- | --- | --- | --- |
| can_be_secret_alliance_founder | Country | Target event target or variable | Hard eligibility for baseline founders |
| can_be_secret_alliance_minor_invitee | Country | Target, stage | Eligibility for Evolution I and later minor invitations |
| can_be_secret_alliance_major_patron | Country | Target, stage | Eligibility for major entry |
| is_valid_secret_alliance_member | Country | None | Removes dead, capitulated, invalid, or already cleared members |
| is_secret_alliance_neighbor_pressure_target | Country | Target | Checks border incident validity |
| target_has_secret_alliance_dossier_tools | Target | None | Category visibility |
| selected_secret_alliance_target_valid | Target | Selected target data | Human selected target cleanup |
| secret_alliance_can_publicly_expose | Target | Evidence and suspicion | Exposure availability |
| secret_alliance_can_start_border_war | Target | Selected member | Border war availability |
| secret_alliance_should_force_reveal_from_war | Country or global | War participants | Detects member war with target |

## Proposed scripted effects

| Effect | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| initialize_secret_alliance | Target | None | Selects founders, assigns roles, seeds values, records root event state |
| score_secret_alliance_candidate | Candidate | Target | Writes temporary score for selection |
| add_secret_alliance_member | Candidate | Role and target | Sets member flags, increments counts, applies hidden idea if needed |
| remove_secret_alliance_member | Member | Reason | Clears flags, decrements counts, removes hidden idea, handles defector or exit |
| refresh_secret_alliance_members | Global or target | None | Sanitizes member list and recalculates counts |
| run_secret_alliance_invitation_round | Convenor or global | Stage | Selects invitee candidates and resolves acceptance |
| apply_secret_alliance_incident | Target | Incident family and actor | Applies damage, evidence chance, suspicion, pact value changes |
| identify_secret_alliance_member | Target | Member | Sets identified flag and opens target actions |
| open_secret_alliance_dossier | Target | None | Opens category, initializes visible values, writes first detail entry |
| force_secret_alliance_reveal | Target | Reason | Converts hidden compact to public faction and logs reveal |
| create_secret_alliance_public_faction | Target or convenor | None | Creates Anti-[target] Pact and adds valid public members |
| call_secret_alliance_members_to_war | Target | War reason | Ensures all valid public members join war |
| apply_secret_alliance_preparedness_reward | Target | War or incident context | Reduces damage or grants opening defense based on preparedness |
| dissolve_secret_alliance | Target | Reason | Clears compact, removes ideas, closes decisions, logs outcome |
| cleanup_secret_alliance_selected_target | Target | None | Clears selected UI target and active target decisions |
| cleanup_secret_alliance_state | Global or target | None | Final cleanup after defeat, collapse, or invalid target |

## Constants and tuning groups

Use script constants for shared tuning.

| Constant group | Examples |
| --- | --- |
| secret_alliance_stage_thresholds | suspicion values, evidence values, minimum cohesion for evolutions |
| secret_alliance_candidate_weights | minor preference, factionless preference, opinion penalty, ideology bonus |
| secret_alliance_incident_pacing | baseline, Evolution I, Evolution II, Evolution III timing bands |
| secret_alliance_costs | support equipment, army XP, command power caps, civilian burden values |
| secret_alliance_ai_weights | peaceful AI, hardline AI, patron AI, weak member AI |
| secret_alliance_damage_caps | factory damage caps, sabotage cooldowns, max repeated pressure per state |
| secret_alliance_war_readiness | public war timer floors, modifiers, ultimatum thresholds |

## Event targets and arrays

The implementation should use arrays for member lists when the existing codebase supports them cleanly. Use event targets for short-lived current actor, current suspected country, incident state, and reveal reason. Use global event targets only for persistent pointers that must survive across scheduled events, and clear them during cleanup.

Important saved pointers:

| Pointer | Lifetime | Notes |
| --- | --- | --- |
| secret_alliance_target | Full system | Target country. Must be cleaned if target no longer exists or tag migrates |
| secret_alliance_convenor_target | Full hidden system | Can be regular or stored through member flags if global target is risky |
| secret_alliance_current_actor | One incident chain | Country causing current incident |
| secret_alliance_current_state | One incident chain | State hit by sabotage, border mission, or guard objective |
| secret_alliance_selected_member | UI action chain | Selected dossier target for human player |

## Public faction name

The public faction name should be dynamic and based on the target country display name. Use a scripted localisation helper for the faction name if the engine field supports it. If faction creation needs a static token, create a stable generic faction key and show the dynamic Anti-[target] name through faction localisation where possible.

The public name direction is a direct hostile pact name. Avoid joke names. Avoid exposing hidden implementation values in the faction name.

## Cleanup plan

Cleanup must remove:

- hidden member flags on all members
- public pact ideas and temporary war ideas
- selected dossier target data
- active target decisions
- stale incident state flags
- temporary sabotage cooldowns where safe
- compact arrays or member variables
- public compact war timers if the pact dissolved
- member AI strategies tied only to Event 011

Cleanup should preserve durable outcome flags needed for achievements, event history, and aftermath. For example, preserving that the player dismantled the compact peacefully is useful. Preserving a dead selected target pointer is not useful.

## Risk notes

The hardest implementation risks are dynamic faction naming, random-country selection without expensive world polling, selected-target UI cleanup, and the instant war-reveal rule. These should be implemented through shared helpers before content files duplicate logic.
