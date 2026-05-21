# Soviet Collapse Faction Goal Audit

## Scope

This audit covers the Part 4 requirement that Event 005 local leagues, blocs, and compacts have purpose, membership rules, joining conditions, refusal logic, removal logic where relevant, shared decisions, war goals, AI behavior, victory conditions, failure conditions, rewards, and consequences.

## Source Findings

| Requirement | Source evidence | Status |
| --- | --- | --- |
| Purpose | `docs/events/005_soviet_union_collapse_local_leagues.md` defines the Baltic League, Caucasus League, Central Asian League, and Free Republics' League as the regional layer between isolated republics and broad anti-Moscow coordination. | source_pass |
| Membership rules | `is_soviet_collapse_regional_faction_candidate`, `can_found_soviet_collapse_baltic_league`, `can_found_soviet_collapse_caucasus_league`, and `can_found_soviet_collapse_central_asian_league` restrict candidates by breakaway/high-chaos status, subject status, existing faction membership, region, pressure gates, and quorum. | source_pass |
| Joining conditions | `soviet_collapse_invite_baltic_regional_partners`, `soviet_collapse_invite_caucasus_regional_partners`, `soviet_collapse_invite_central_asian_regional_partners`, and `soviet_collapse_invite_free_republics_league_partners` only add eligible existing breakaways or eligible high-chaos successors that are not already in a faction. | source_pass |
| Refusal logic | Invitation effects skip subjects, non-breakaways, ineligible regional tags, existing faction members, and countries that recently left a regional faction. Foreign dependency logic also treats faction membership as protection from client-state pressure. | source_pass |
| Removal logic | `soviet_collapse_withdraw_from_regional_faction` clears regional member flags, removes regional commitments, makes the country leave the faction, and applies a 180-day recently-left block. | source_pass |
| Shared decisions | `soviet_collapse_regional_faction_category` exposes founding, invitation, coordination, defensive, recognition, logistics, tension, war-call, withdrawal, and goal-resolution decisions. | source_pass |
| War goals | `soviet_collapse_call_regional_league_defensive_war` declares or joins the anti-Soviet war, arms members, clears the progressive-release cooldown, and triggers a release check. | source_pass |
| AI behavior | Regional decisions include `ai_will_do` blocks that respond to league pressure, Soviet threat, war with Moscow, depot vulnerability, foreign appetite, and southern breakaway pressure. | source_pass |
| Victory conditions | `has_soviet_collapse_regional_faction_goal_success` resolves active defense, recognition, and logistics goals when the defensive war is active, recognition progress is high enough, or depot control is high enough. `soviet_collapse_apply_regional_faction_goal_success` clears the active goal, records success, rewards members, and reports `chaosx.nr5.41`. | source_pass |
| Failure conditions | `has_soviet_collapse_regional_faction_goal_failure` detects high tension, collapsed cohesion, an invalid low-threat defense program, patron-dominated recognition failure, or logistics failure under depot vulnerability. `soviet_collapse_apply_regional_faction_goal_failure` clears the active goal, records failure, applies penalties, recalculates Soviet pressure, and reports `chaosx.nr5.42`. | source_pass |
| Rewards and consequences | Successful goals raise cohesion, resilience, war support, recognition, depot control, manpower, equipment, and member League support depending on active goal. Failed goals lower cohesion, recognition, and depot control while raising tension and Soviet-facing pressure. | source_pass |
| Super-event scope | Local league formations fire normal news events `chaosx.nr5.30`, `.31`, and `.32`; Free Republics' League and Steppe Federation announcements use news/report channels. No ordinary local league formation uses a super-event helper. | source_pass |

## Resolution Behavior

Active goals now have explicit source-level resolution instead of relying only on implicit pressure changes. League leaders can ratify a successful common program or mediate a failed one through the regional faction category. Existing invite, coordination, tension-settlement, and defensive-war effects also call the same resolution helper after they change the relevant variables.

## Validation Notes

This is a source-level audit. It verifies scripted coverage, not live-session pacing. The broader Event 005 goal remains incomplete until the remaining partial ledger rows are resolved.
