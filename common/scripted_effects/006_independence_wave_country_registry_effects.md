# Event 006 country-registry effects

This file contains only the two lifecycle wrappers needed by the canonical
Independence Wave origin ledger. The static carrier data lives in
`common/script_constants/006_independence_wave_country_registry_constants.txt`;
the exact country-scope predicates live in
`common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`.

## `independence_wave_registry_record_event6_origin`

- Scope: country.
- Inputs: none; the caller has already validated the Event 006 setup package.
- Outputs: sets `independence_wave_active_origin`, clears the ended marker, and
  writes `liberation_origin = constant:liberation_origin.independence_wave`.
- Side effects: only the normal Event 006 origin markers. It does not create a
  tag, change ownership, add cores, load a focus tree, or touch Event 012 flags.
- Call site: `independence_wave_prepare_country_origin` in
  `common/scripted_effects/006_independence_wave_effects.txt`.

## `independence_wave_registry_clear_event6_origin`

- Scope: country.
- Inputs: none; called after the Event 006 package and ledger cleanup chain.
- Outputs: clears the live Event 006 origin, preserves
  `independence_wave_origin_ended`, and resets `liberation_origin` to `none`.
- Side effects: no tag, focus, state, or Event 012 mutation.
- Call site: `independence_wave_end_active_origin` in the same Event 006 effect
  file.

## Provenance and cleanup contract

Event 012 records its own `africa_priority_origin_*` and package flags. It must
never call either helper, so an Africa promotion cannot acquire Event 006
origin provenance by sharing a carrier tag. Event 006's existing package,
network, event-target, and focus cleanup still runs before the clear wrapper.
The registry itself owns no event targets: the short-lived setup targets remain
the existing `independence_wave_setup_former_host` and
`independence_wave_setup_anchor_state` targets, and the existing Event 006
cleanup chain remains responsible for clearing them and global targets.
