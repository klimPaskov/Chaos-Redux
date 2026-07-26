# Refugee Train relationship pairing addendum

This tranche adds the first generation-bound reciprocal candidate payload to the Fallout scheduler. It remains dormant and does not activate the scheduler or issue an engine event.

## Accepted scope

The paired identity is Refugee Train with candidate id `415`, transaction key `710033`, route `7133`, human token `fallout_event_id.refugee_train_human`, AI token `fallout_event_id.refugee_train_ai`, and visible cost `fallout_event_415_transaction.visible_budget_cost`.

The producer scans the already reviewed candidate registries and selects the two lowest current registry indices that contain the exact Refugee Train row. It writes each index into the other row's `fallout_event_candidate_partner_registry_index_entries` slot.

The pass never creates a country, tag, native diplomacy relation, state target, or event. It writes no scheduler activation flag. Existing country rows and the existing bilateral ledger remain the only sources of identity and conflict state.

## Reciprocal proof

`fallout_event_candidate_relationship_payload_is_current` remains the release gate. It requires the partner index to be current, both candidate registries to be generation-bound, the exact candidate id and transaction key to match, the relationship class and bilateral opportunity flag to match, both human and AI tokens to be present and distinct, the visible cost to remain bounded, and the partner row to point back to the source registry index.

The general candidate eligibility trigger still requires the bilateral pair-family memory to be clear. The existing `fallout_event_reserve_bilateral_transaction` effect remains the only ledger writer, so pairing cannot allocate a ticket or mutate a participant row.

## Deliberate boundary

The current Refugee Train chain has authored ordinary opening, result, callback, and cleanup events under `chaosx.fallout.415` through `.421`. Those consumers authenticate ordinary receipts and are not yet bilateral response consumers. The relationship pair therefore remains non-countable until a later tranche supplies the bilateral opening and response stage consumer, host delivery proof, save recovery proof, multiplayer proof, and Event Log proof.

No new asset, sprite, audio path, tag, or localisation key is introduced by this addendum.
