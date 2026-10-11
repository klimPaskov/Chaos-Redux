# Achievement engine lookup bindings — shard 5 (2026-10-11)

Status: 4 achievement triplets bound (12 DDS files); 3 active 038 triplets skipped because no accepted source triplet and receipt exist.

The HOI4 achievement consumer loads root-level DDS states by the exact registered achievement ID. These copies add the missing active 030 names while preserving all source pixels and source files. No `.gfx`, gameplay, localisation, or achievement registry files were changed.

## Accepted source evidence

The source package is `docs/assets/030_time_traveler/`. Its manifest records parent visual acceptance of the achievement sheet on 2026-10-10 and documents the 64x64 runtime triplets. `docs/assets/030_time_traveler/notes/achievement_source_validation.json` records the source-layer acceptance and state derivation; `docs/assets/030_time_traveler/notes/dds_roundtrip_validation.json` records strict 64x64 DDS round-trip validation. The existing root-level source DDS triplets below were byte-copied without conversion.

| Source DDS stem | Active registered ID | Output paths |
| --- | --- | --- |
| `030_time_traveler_future_refused` | `chaos_redux_030_the_future_refused` | `gfx/achievements/chaos_redux_030_the_future_refused{,_grey,_not_eligible}.dds` |
| `030_time_traveler_i_have_seen_this_office_before` | `chaos_redux_030_i_have_seen_this_office_before` | `gfx/achievements/chaos_redux_030_i_have_seen_this_office_before{,_grey,_not_eligible}.dds` |
| `030_time_traveler_nine_lives_of_history` | `chaos_redux_030_nine_lives_of_history` | `gfx/achievements/chaos_redux_030_nine_lives_of_history{,_grey,_not_eligible}.dds` |
| `030_time_traveler_no_one_owns_tomorrow` | `chaos_redux_030_no_one_owns_tomorrow` | `gfx/achievements/chaos_redux_030_no_one_owns_tomorrow{,_grey,_not_eligible}.dds` |

All 12 outputs match their corresponding source SHA-256 values. Strict header checks confirmed DDS magic, a 124-byte classic header, 64x64 dimensions, 32-bit BGRA masks, and 16,512-byte files. Each target ID is present in the current `common/achievements/` registry.

## Skipped active IDs

| Active registered ID | Result |
| --- | --- |
| `chaos_redux_038_deus_vult_logistically` | Skipped: no complete accepted source triplet/runtime DDS receipt was found in the bounded 038 achievement package. A source PNG exists, but no accepted state triplet exists to copy. |
| `chaos_redux_038_the_eleventh_time_is_the_charm` | Skipped: no complete accepted source triplet/runtime DDS receipt was found in the bounded 038 achievement package. A source PNG exists, but no accepted state triplet exists to copy. |
| `chaos_redux_038_malta_stands_alone` | Skipped: no achievement source triplet or receipt was found in the bounded 038 achievement package. |

No artwork was generated or derived, and no existing asset was overwritten. The 038 entries remain incomplete pending accepted color/grey/not-eligible triplets and their production evidence. No live HOI4 validation was performed.
