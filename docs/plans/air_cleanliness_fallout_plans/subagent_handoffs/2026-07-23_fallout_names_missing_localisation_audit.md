# Fallout Names for the Missing localisation audit

## Changed files

- `localisation/english/fallout_consolidated_l_english.yml`
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`

## Changed key

- `chaosx.fallout.274.success.d` changed from a discouraged `did not ... but ...` contrast frame to direct in-world wording: `Their work left the losses intact and made the living legible enough for food, medicine, and a name to meet again.`
- Added name and description keys for all six Names for the Missing dynamic modifiers. The keys match the modifier ids exactly.

## Before and after behavior

The event result, Event Log detail, branch meaning, and gameplay effects are unchanged. The local clerks success report now states the surviving losses and the usable record directly.

## Validation

- Confirmed UTF-8 BOM on the YAML after the patch.
- Confirmed all title, description, option, and custom tooltip keys referenced by event ids 269 through 281 resolve in the scoped YAML.
- Confirmed all fifteen `fallout_event_269_log` payload detail keys resolve through the scoped scripted localisation and YAML.
- Confirmed no duplicate keys inside the YAML or across English localisation files for this tranche.
- Confirmed all six dynamic modifier ids have matching name and description keys.
- Confirmed the scoped localisation and scripted localisation contain no em dashes or semicolons.

## Skipped meaningful validation

No live HOI4 runtime or scheduler activation test was run because the Names for the Missing candidate is documented as dormant and the parent scope is a static localisation audit.

## Remaining risks and wording decisions

- The chain intentionally has no state target, so regional specificity remains country-level through districts, shelter rooms, outer roads, and market spaces rather than dynamic state names.
- Government-aware wording is present through `GetAirWinterGovernmentAuthority` and `GetAirWinterGovernmentOfficial`.
- Central Event Log name and detail selectors remain aligned to history id 9118 and `GetFalloutEvent269EventLogDetail`.
