# CXT country name pool handoff

Status: implemented and reviewed by the parent.

Acceptance basis: the parent assigned a package-specific name-pool repair for the reported character manager errors affecting Chaos Redux Test Directorate, tag `CXT`.

## Changed files

- `common/names/chaosx_test_country_names.txt` adds the only new runtime name-definition file.
- `docs/testing/runtime_repairs/20260913_cxt_followup/country_name_handoff.md` records the schema evidence, validation, and handoff boundaries.

The final SHA-256 of the new name-definition file is `14dfd28824c680ec7f89644cbb52594966dadcd13ef95cdf8e3487694e50776c`.

No existing country name file was edited, so the pools for every other tag remain unchanged.

## Schema and coverage

Before this patch, the mod `common/names/` directory contained no `CXT` block, and a scan of the installed vanilla `common/names/` directory found no `CXT` block or duplicate `chaosx_test_country_names.txt` filename.

The final `CXT` block supplies 32 male names, 32 female names, 64 shared surnames, and 24 callsigns using the country keyed structure accepted by the game.

Parent review expanded the specialist's initial six-name and six-surname pools because the retained 261-division roster generates many commanders and the country also supports generated scientists and other leaders.
The final pools provide 2,048 first-name/surname combinations per gender, or 4,096 total, rather than the initial 72 combinations.
Vanilla name-file documentation explicitly states that full combinations are not reused, so ample capacity matters for this test package.

The final pool has no duplicate entries within either gender, the surname pool, or the callsign pool.
Ordinary names shared with other countries are allowed by the country keyed schema.

The offline `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md` Character names section documents country keyed `male`, `female`, `surnames`, and `callsigns` blocks for random generated characters.

The installed vanilla `common/names/00_names.txt` uses the same structure for country pools and does not define role-specific `general` or `scientist` blocks.

The installed vanilla `documentation/effects_documentation.md` documents `generate_character` and `generate_scientist_character` as country-scoped effects that accept an optional explicit name, so generated general and scientist roles consume the country name pool when no explicit name is supplied.

The role names `general` and `scientist` therefore describe the consumers of this pool, not nested schema keys to add to the name file.

## Parent bootstrap review

The parent candidate in `common/scripted_effects/chaosx_test_country_effects.txt` queues `chaosx_test_country.1` from a valid `CXT` scope with a one-hour delay before the final `change_tag_from` effect in the generated `CXT` block.

That ordering addresses the reported `country_event supported Country provided None` failure that occurred when the receiver was evaluated immediately after the player country had already changed.

The one-hour `hours` field is supported by the offline event modding reference and matches vanilla country-event delay precedents.

The existing `chaosx_test_country.1` receiver remains triggered-only and tag-gated to `CXT`, where it initializes or refreshes the CXT setup after the transfer.

The parent candidate preserves the existing setup helpers and their responsibilities, including initialization, refresh, registered content synchronization, the static roster, equipment stockpiles, special projects, facilities, technology, and CBRN or camp setup.

The reviewed helper definitions remain `chaosx_test_country_initial_setup`, `chaosx_test_country_refresh`, `chaosx_test_country_sync_registered_content`, and `chaosx_test_country_sync_dynamic_content`, with their subordinate facility, occupation, warfare, camp, registration, and resource helpers intact.

At review time, the parent candidate hashes were `C3AE1DB56E3E03CD4E67EA96CF16986E7B1E99C205AB2BC7AEBBB12CBBAD0293` for `common/scripted_effects/chaosx_test_country_effects.txt` and `EAC04DF731E00B2591EEBD7B576C7438EB838574E254B6E28696961C6EEA3DDE` for `events/chaosx_test_country.txt`.

This handoff does not edit the parent-owned effect or event files.

## Validation and limits

The name-file structure was checked against the offline Country creation schema, the installed vanilla `00_names.txt` precedent, and the installed effects documentation.

The new file has one `CXT` definition, both gender pools, a top-level surname pool, and a top-level callsign pool.

The parent event and bootstrap source were reviewed read-only for ordering. The current parent effect candidate keeps `change_tag_from` last in the generated CXT block and keeps the direct existing-CXT receiver branch intact.

Live game validation was skipped because live game testing and consumer validation belong to the user.

The name repair should remove the two missing generated-name errors after the file is loaded, but the roster, equipment, and project symptoms still depend on the parent bootstrap and event changes.

No simplification or fallback was used. Omitting role-specific `general` and `scientist` blocks is intentional because that syntax is absent from the installed schema and vanilla precedent.

Parent source review confirmed the recorded effect and event hashes, preserved setup coverage, and receiver-before-transfer scheduling.
Source and MCP evidence do not prove live receiver execution.
