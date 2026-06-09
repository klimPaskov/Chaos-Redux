# Event 006 Congress Volunteer Cadre Decision Audit

## Scope

Audited the New States Congress volunteer-cadre decision tranche:

- `independence_wave_send_congress_volunteer_cadre`
- `can_independence_wave_send_congress_volunteer_cadre`
- `independence_wave_send_congress_volunteer_cadre_effect`
- `independence_wave_decision.congress_volunteer_cadre_*`

Files reviewed were limited to the requested Event 006 decision, constants, scripted trigger, scripted effect, localisation, and documentation files.

## Findings by severity

- Medium: `independence_wave_send_congress_volunteer_cadre` allowed subject Event 006 releases to send or receive cadres once they had Congress delegate flags. That diverged from `independence_wave_sign_mutual_guarantee`, which requires independent sender and target countries, and could let patron-controlled releases participate in Congress aid as if they still had full sovereign corridor control.
- Low: The custom cost text is static localisation. It currently matches the constants (`10` command power, `1,000` manpower, `80` infantry equipment), but future balance changes must keep the localisation in sync.
- Low: The decision remains repeatable by sender across different eligible targets after the re-enable window. This appears intentional for a corridor network because each target can only receive the cadre once and the sender pays political power, command power, manpower, and infantry equipment each time.

## Patch Made

Changed files:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`

Changed identifiers:

- `independence_wave_send_congress_volunteer_cadre`
- `can_independence_wave_send_congress_volunteer_cadre`

Before:

- Any Event 006 release with New States Congress and delegate flags could target the decision, even if it had become a subject.
- Eligible targets could receive the cadre while subject, as long as they were Event 006 releases with delegate flags and were vulnerable by war state or militia strength.

After:

- Sender must be independent in the decision `target_root_trigger` and in the shared scripted trigger.
- Target must be independent inside `FROM` in `can_independence_wave_send_congress_volunteer_cadre`.
- Mutual guarantee and volunteer-cadre Congress sovereignty rules now match.

## Category Lifecycle Notes

The decision belongs to `independence_wave_new_states_congress_category`. It is a targeted decision over `global.independence_wave_released_countries`, gated by Congress and delegate flags, and re-enables after `@independence_wave_congress_decision_days`. No hidden decision without reveal logic was found in this tranche.

## Mission Quality Notes

No mission was added or changed by this tranche.

## Cost and Requirement Clarity

The custom cost has a real `custom_cost_trigger` and the effect subtracts command power, manpower, and infantry equipment in `independence_wave_send_congress_volunteer_cadre_effect`. The target requirement is hidden from raw trigger display because invalid targets are filtered by `target_trigger`; the visible cost line remains concise.

## AI Validity and Route-Lock Notes

AI has a nonzero `ai_will_do`, with route and target-war modifiers. The target array is limited to the Event 006 release ledger and the scripted trigger rejects non-existing targets, self-targeting, repeated target receipt, and non-independent sender/target countries after this patch.

## Localisation and Tooltip Gaps

Localisation exists for the decision name, description, effect tooltip, and custom cost. No localisation keys were changed. Remaining risk is static numeric cost text drifting if constants are retuned.

## Cleanup and Exploit Risk

The target receives `independence_wave_received_congress_volunteers`, preventing repeated cadre receipt. Sender repeatability across different targets remains bounded by the re-enable window and real costs. No cleanup hook is needed for the target receipt flag because it is a persistent corridor-history marker.

## Validation

Performed static validation by reading:

- Offline Paradox wiki pages for decisions, scopes, triggers, effects, localisation, modifiers, on actions, events, ideas, AI, and data structures.
- Vanilla documentation for script constants, triggers, effects, and modifiers.
- Vanilla decision/scripted trigger/effect precedents for targeted `FROM` semantics, custom costs, and AI weights.
- `rg -n "<=|>="` across the bounded Event 006 gameplay, localisation, and event-doc files returned no unsupported comparison operators.
- Line checks confirmed the sender and target independence gates are present on the patched identifiers.

## Remaining Risks

- Static localisation numbers can drift from constants.
- This audit did not validate in-game UI rendering or runtime AI choice frequency.
