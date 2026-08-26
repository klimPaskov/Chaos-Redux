# Event 006 country-registry effects

This file contains only the two lifecycle wrappers needed by the canonical
Independence Wave origin ledger. The static carrier data lives in
`common/script_constants/006_independence_wave_country_registry_constants.txt`;
the exact country-scope predicates live in the country-registry section of
`common/scripted_triggers/006_independence_wave_package_triggers.txt`.

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

## Static carrier status API

The country-group constants in
`common/script_constants/006_independence_wave_country_registry_constants.txt`
now expose package-row status projections for later callers:

- `selectable_bound_tags` is the current-map-bound selectable pool (138 rows,
  137 unique carrier scopes).
- `selectable_unbound_tags` is the explicit fail-closed selectable pool (55
  rows, 55 unique carrier scopes). Missing geography is preserved; no nearby
  state or substitute tag is implied.
- `event6_owned_bound_tags` and `event6_owned_unbound_tags` split custom `X`
  registrations by current-map status.
- `registered_reuse_bound_tags` and `registered_reuse_unbound_tags` split
  vanilla-tag reuse rows by current-map status.
- `overlay_route_carrier_tags` and its route-specific subsets expose the
  original carriers for all thirteen non-selectable overlays. Overlay
  carriers may also appear in a selectable pool when the same vanilla country
  has a separate Event 006 row; route triggers remain the identity gate.

Country groups de-duplicate tags, so BIA appears in both bound and unbound
status projections: IW-107 is bound while IW-096 is unbound. Exact package
identity, anchor, host, reservation group, readiness, scenario rank, and
package status remain row-level facts in the canonical candidate registry,
package-id constants, and current-map binding CSV. Use those sources and the
existing region load/reserve dispatchers when a caller needs a specific row;
do not infer a row from a carrier tag alone.

The public `chaosx_country_independence_wave_*` collections mirror these
status and overlay views. Collections are active views and naturally omit
dormant reserved tags; static country-group constants remain the source for
registration audits and fail-closed admission checks.
