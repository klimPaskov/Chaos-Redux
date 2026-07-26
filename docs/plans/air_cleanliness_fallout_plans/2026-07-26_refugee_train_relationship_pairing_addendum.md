# Refugee Train relationship pairing addendum

Status: implemented dormant pairing prerequisite. The later `2026-07-26_refugee_train_bilateral_consumer_addendum.md` supplies the opening and response consumer that this file originally left for a later tranche.

This tranche adds the first generation-bound reciprocal candidate payload to the Fallout scheduler. It remains dormant and does not activate the scheduler or issue an engine event.

## Accepted scope

The paired identity is Refugee Train with candidate id `415`, transaction key `710033`, route `7133`, human token `fallout_event_id.refugee_train_human`, AI token `fallout_event_id.refugee_train_ai`, and visible cost `fallout_event_415_transaction.visible_budget_cost`.

The producer scans the already reviewed candidate registries and selects the two lowest current registry indices that contain the exact Refugee Train row. It writes each index into the other row's `fallout_event_candidate_partner_registry_index_entries` slot.

The pass never creates a country, tag, native diplomacy relation, state target, or event. It writes no scheduler activation flag. Existing country rows and the existing bilateral ledger remain the only sources of identity and conflict state.

## Reciprocal proof

`fallout_event_candidate_relationship_payload_is_current` remains the release gate. It requires the partner index to be current, both candidate registries to be generation-bound, the exact candidate id and transaction key to match, the relationship class and bilateral opportunity flag to match, both human and AI tokens to be present and distinct, the visible cost to remain bounded, and the partner row to point back to the source registry index.

The general candidate eligibility trigger still requires the bilateral pair-family memory to be clear. The existing `fallout_event_reserve_bilateral_transaction` effect remains the only ledger writer, so pairing cannot allocate a ticket or mutate a participant row.

## Deliberate boundary

The current Refugee Train chain has authored ordinary opening, result, callback, and cleanup events under `chaosx.fallout.415` through `.421`. The separate bilateral consumer is now authored at events `1019` through `1022` and is documented in `FALLOUT_REFUGEE_TRAIN_BILATERAL_CONSUMER_PROOF.md`. The relationship pair remains dormant and outside the countable release floor because scheduler activation, host delivery, save recovery, multiplayer, and Event Log runtime proof remain open.

No new asset, sprite, audio path, tag, or localisation key is introduced by this addendum.
