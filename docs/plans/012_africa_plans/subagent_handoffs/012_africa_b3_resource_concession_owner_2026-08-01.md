# Event 012 B3 resource-concession owner tranche

Status: implemented as a narrow owner patch; the achievement remains incomplete until its other matrix disqualifiers have authoritative writers.

## Gameplay changes

- Added `africa_achievement_ratio.resource_review_settlement_foreign_concession_share = 20` in `common/script_constants/012_africa_achievement_constants.txt`.
- Added `africa_achievement_record_measured_foreign_concession_share` in `common/scripted_effects/012_africa_achievement_effects.txt`.
- The helper is called only from `africa_achievement_record_action_outcome` when the resolved action is a full `resource_sovereignty_review` result, whose player-facing contract is “Contracts renegotiated or nationalised with local benefit.”
- The helper writes the global measured share and `africa_achievement_ore_leaves_as_machines_owner_ready` in the host scope. It does not clear a prior concession-breach flag or erase an earlier failure.
- The helper refreshes the survival windows after the write, while the five-year resource timer now requires the owner-ready marker; reaching the zone and processing counts before a review cannot start the clock from an unknown share.
- `africa_ore_leaves_as_machines_is_complete` now requires the owner-ready marker, so the startup `invalid` share cannot satisfy the achievement.
- A failed surveyed `create_local_processing_chain` now records `africa_achievement_raw_export_dependency_crisis`, and the action validation requires the documented resource-survey prerequisite before that failure can occur.

## Acceptance alignment

This closes the missing exact owner for the live foreign-concession share and adds the direct raw-export failure owner without using a generic action-success proxy. The measured value is deliberately below `foreign_concession_cap` and is centralised beside the achievement thresholds. Both failure flags remain sticky through their dedicated helpers.

The achievement is not completion-ready yet. The forced-resource-seizure disqualifier still lacks an authoritative owner and was not inferred from an unrelated action outcome in this tranche.

## Validation and remaining risk

Static source review should confirm one helper definition, one exact full-review callsite, one owner-ready trigger gate, and no additional tag or model changes. A live campaign must still prove that the full review is reachable after resource and processing work and that the existing five-year timer starts only after the measured write. No in-game session was launched by the agent.
