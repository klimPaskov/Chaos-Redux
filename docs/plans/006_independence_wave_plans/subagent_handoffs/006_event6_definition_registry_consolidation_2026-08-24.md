# Event 006 definition-registry consolidation

## Scope

This follow-on source-layout pass merges three definition-only Event 006 surfaces that had many small files but one shared container type per folder.

- The 49 Event 006 idea files are now `common/ideas/006_independence_wave_ideas_registry.txt`.
- The 17 Event 006 character files are now `common/characters/006_independence_wave_characters_registry.txt`.
- The 3 Event 006 country-leader-trait files are now `common/country_leader/006_independence_wave_leader_traits_registry.txt`.

Each registry keeps the original filename as a source marker and retains the original sorted section order. Unique idea, character, and trait identifiers are unchanged. Identical file-scoped constants are emitted once at the registry header; no conflicting constant values were found.

Package decisions, package effects, focus trees, localisation, country shells, and engine callback files remain separate because those surfaces carry package ownership, country-tag path semantics, or callback-composition risks.

## Preservation checks

The ideas registry preserves 413 unique idea definitions and the executable-definition SHA-256 is `902e7a1830977b222ed4a80c0b27af134974801c4487ca5521f8ddcc9fe8a3ec` before and after consolidation after comments and whitespace-only layout are normalized.

The characters registry preserves 68 unique character definitions and the executable-definition SHA-256 is `6433fde173c66c8adbb35ec31d7646559759fd4b0fe68c76bb040294e2ccfe13` before and after consolidation after comments and whitespace-only layout are normalized.

The leader-trait registry preserves 23 unique trait definitions and the executable-definition SHA-256 is `8cd34bd1f428f3cd33c178859b4ad576c015cfc0079adc242ff87d8066dcc647` before and after consolidation after comments and whitespace-only layout are normalized.

All three merged files have balanced braces, and no duplicate definition identifiers were introduced.

## Size and file-count result

The pass removes 69 old definition files and leaves three registries in their place, for a net reduction of 66 files.

Compared with the committed source snapshot, the ideas, character, and trait registries save 34,775 source bytes after repeated banners and duplicate identical constant declarations are removed.

Together with the earlier category/compatibility pass, Event 006 has removed 137 old parser files in exchange for six registries, a net reduction of 132 files and 79,010 committed source bytes.

## Validation boundary

The merge is a source-layout change only and does not claim live game loading, portrait promotion, tooltip observation, or runtime character recruitment. The Event 006 allocator, country API, strict flag-family, and SCN-008 static audits still pass with the same `3/4/5/7/10` ladder and 32/29/40/161 admission boundary.
