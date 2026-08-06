# Event 006 country API all-carrier repair

Date: 2026-08-06

Scope: narrow repair of the reusable `chaosx_country_all` registry surface. No
package admission, origin ownership, focus assignment, history, state, flag,
portrait, advisor, or runtime release behavior was changed.

## Finding

Before this repair, `common/script_constants/chaosx_country_registry_constants.txt`
declared the broad `all_chaosx_country_tags` array, but it omitted 38 registered
Event 006 carriers that were already present in
`independence_wave_country_groups.all_resolved_carrier_tags`. The
event-specific `chaosx_country_independence_wave` collection therefore worked,
but a later cross-event consumer using `chaosx_country_all` could not discover
those existing carriers through the public API.

## Repair

The missing registered carriers were added to `all_chaosx_country_tags`:

`AFA ALT ANU ARM ASY ATJ AZR BAN BAR BAY BIA BLC BLI BOS BRD BRI BSK BYA CAT CHM CHU CIN COR CRI DAG DAH DON EVE FER FIJ FSM GAL GAR GEO GLC HAR HAW HYD ICE IMO KAR KAS KHA KHL KOM KOS KUB KUR LAO LEB MAC MAD MAY MEL MEN MIS MNT MPU MYS NAV NEN OCC OKN ORO PAL PNG POK PSH QUE RAS RHI RIF RUT RWA SAM SCO SIN SKK SOK SOM TAT TIG TRA UDM UGA WLS WPG YAK YUC`

The public API documentation now lists `collection:chaosx_country_all` and
states that it contains the complete 191-carrier Event 006 surface. Collection
membership remains a lookup only; callers must still prove origin, package
readiness, map binding, collision safety, and meaningful-tree preservation.

## Validation

The parsed array comparison reports 242 unique tags in `all_chaosx_country_tags`,
191 unique tags in `all_resolved_carrier_tags`, and an empty resolved-carrier
set difference. The reusable check is now `.tools/audit_event6_country_api.py`
and reports `missing=0; duplicates=0`. The unrelated Soviet and other Chaos
Redux entries remain in the broad array. No Event 006 package attestation or
scenario allowlist was expanded by this repair.

## Files

- `common/script_constants/chaosx_country_registry_constants.txt`
- `docs/events/006_independence_wave/country_api.md`
- `.tools/audit_event6_country_api.py`

The whole Event 006 goal remains active and incomplete; this handoff closes
only the broad reusable country-API omission.
