# Fallout shared helper triggers

This note records the shared gate helpers in `common/scripted_triggers/fallout_consolidated_triggers.txt` that several Fallout event chains and orientation proofs reuse.

## Delayed-result and callback gate

Each ordinary Fallout chain with a delayed result and a callback exposes two admission triggers, `fallout_event_<N>_delayed_result_can_enter` and `fallout_event_<N>_callback_can_enter`.

For chains whose callback enters under the same gate as the delayed result, the callback trigger delegates to the delayed-result trigger:

```
fallout_event_908_callback_can_enter = {
	fallout_event_908_delayed_result_can_enter = yes
}
```

- Scope: COUNTRY.
- Input: the issued dispatch envelope (`fallout_event_dispatch_issued_*` variables) and the chain registry, exactly as the delayed-result trigger reads them.
- Output: a boolean, identical to the delayed-result trigger.
- Side effects: none.
- A chain whose callback needs a different gate (chains 649, 656, 663, 670 and 677) keeps a standalone body; change a delegating chain's gate in the delayed-result trigger only.

## Pilot roster

`fallout_orientation_country_memory_is_pilot_roster` lists the twelve country memories of the reviewed orientation pilot. The resource, government, and candidate mapping gates in the orientation registry builders call it directly (the government mapping trigger `fallout_orientation_country_memory_has_pilot_government_mapping` is a one-line wrapper over it), and each keeps its own receipt contract (resource identity row, candidate payload). Add a memory to the roster in one place.

- Scope: COUNTRY, reading `fallout_country_memory_id`.
- Side effects: none.

## Example

```
limit = { NOT = { fallout_orientation_country_memory_is_pilot_roster = yes } }
```
