# Event 006 reusable country collection API handoff

Date: 2026-08-03.

## Scope

Named every existing Event 006 and shared `chaosx_country_*` collection in:

- `common/collections/006_independence_wave_country_collections.txt`
- `common/collections/chaosx_country_collections.txt`

The new `name = CHAOSX_COLLECTION_*` fields give later callers stable, discoverable collection identifiers while preserving the existing static-array inputs and collection keys. No tag, country history, origin marker, package dispatcher, focus assignment, or content gate was changed.

## API coverage

The named views cover the full resolved Event 006 carrier pool, owned X tags, registered-tag reuse, bound and unbound selectors, overlay route carriers, Africa overlap/current-map groups, all fourteen regions, the broad Chaos Redux country pool, and Soviet Collapse carriers. The existing registry documentation remains the usage authority and continues to distinguish active collections from dormant reservation arrays.

## Validation

- Compared both collection files against their current diffs. Changes are limited to collection names and comments already present in the files.
- Confirmed each collection retains its original `input = constant:` source.
- Confirmed the protected-tag audit remains the authority for external collisions and is unchanged by this naming-only patch.

## Remaining risks

Collection names do not create countries or grant package readiness. Callers must still resolve package identity, origin, state anchors, tag collisions, content attestation, and the event-specific focus/AI/decision contract before loading content.
