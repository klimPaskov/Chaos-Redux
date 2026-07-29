# Event 015 Asset Completion Repaired-Snapshot Re-audit

Date: `2026-07-16`

Auditor scope: accepted visual manifest, repaired Choice/Assignment animation, route identities, portraits, super-event visuals/audio, and regression of the previous 100-record package

Verdict: **FAIL — four P2 blockers**

## Outcome

The repaired balance-shift asset is complete in both directions. Choice and Assignment each have eight distinct built-in ImageGen source objects, eight distinct processed frames, exact sheets, static fallbacks, GIF/contact review, exact uncompressed BGRA DDS output, registered static and animated sprites, live GUI consumers, route-sensitive threshold-crossing flags, first-refresh suppression, opposite-direction exclusion, and cleanup.

The fresh accepted-row crosswalk nevertheless invalidates the previous asset PASS. Four older accepted GUI families remain incomplete:

1. compact Need, Plenty, and Concord Value icons;
2. six Calling icons;
3. ten Case-card states;
4. seven District-role cards and six District-state presentations.

The first two have an unsliced ImageGen atlas but no final runtime family. The latter two have no accepted card package. None has the required registrations, live consumers, and state bindings. Existing text, decision icons, and background decoration are extra surfaces and do not substitute.

## Severity

All four findings are **P2 visual-completeness blockers**. No P0, P1, or P3 asset finding was identified.

## Repaired balance evidence

| Direction | Source frames | Processed frames | Native frame | Runtime | Binding |
| --- | ---: | ---: | --- | --- | --- |
| Toward Choice | 8 unique | 8 unique | `158x24` | 8 frames, 5 fps, non-looping | `utopia_manifesto_balance_shift_to_choice_recent` |
| Toward Assignment | 8 unique | 8 unique | `158x24` | 8 frames, 5 fps, non-looping | `utopia_manifesto_balance_shift_to_assignment_recent` |

Choice source-manifest SHA-256: `639d2e6e75f082b5a139b7e26222b061a41906005ac139f0685c3931cab74e4f`.

Assignment source-manifest SHA-256: `6fbc91cc8fe69d35c7d778c090ff29fd61fa59ca14b4f972a2e7a9cd13c072ce`.

Both packaged source sets are byte-identical to their recorded built-in ImageGen objects. Consecutive processed-frame RMS differences are nonzero and visually material. PNG sheets equal exact frame concatenations; static PNG/DDS files equal frame `007`; DDS headers, dimensions, lengths, channel masks, and pixel payloads match the processed PNGs. Contact sheets show physical rail/latch/branch change toward Choice and token sorting/grid formation toward Assignment; neither package is transform-only motion.

Runtime uses `GFX_utopia_balance_to_choice_animated` and `GFX_utopia_balance_to_assignment_animated` at `(516,70)`. `utopia_manifesto_refresh_balance_shift_animation` compares the recomputed band with `utopia_manifesto_previous_assignment_band`, requires a resolved route, suppresses initialization, sets one timed country flag, clears its opposite, and is called from state-change refresh paths rather than a recurring world scan. Terminal cleanup clears both flags and the stored previous band.

## Regression results

### Previous 100-record route-identity package

- `100/100` source hashes match.
- `100/100` processed hashes match.
- `100/100` runtime hashes match.
- `100/100` packaged-final files are byte-identical to runtime.
- `100/100` processed/runtime images are pixel-identical.
- `75/75` flags use required sizes, 32-bit TGA, and bottom-left origin.
- `4/4` institutional tableaux remain people-free.
- `16/16` advisors remain distinct dossier portraits.
- `5/5` League emblems remain registered and state-selected.

Package-record SHA-256: `828f18554094f6b214a07dde11f4fa61df290b881d8261cc3b6ee3677f54ea7`.

### Non-icon presentation package

- `22/22` source, processed, and final checksum records match.
- `22/22` dimensions match.
- `22/22` processed/runtime pixel comparisons match.
- `22` final hashes are unique.
- The family contains `14` reports, `3` news pictures, and `5` route-specific super-event pictures.

Package-record SHA-256: `5f12ace1db8b1ee59dd0530694cfbfaeec4d54a578c0ca773361a98b72047d3a`.

The five route pictures are registered and selected for slots `96`-`100`; visual review found five distinct route readings rather than aliases or legacy fallbacks.

### Audio

- Runtime WAV: SHA-256 `68ebdcb9a4d81ca9863e85344fc19ab1ad99ffb7e83c836691d7a92181bfd1b9`; Vorbis, 44.1 kHz, stereo, `116.000000 s`.
- Runtime WAV: SHA-256 `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`; PCM s16le, 44.1 kHz, stereo, `116.000000 s`.
- Each container hash is unique in its runtime folder (`55` OGG, `53` WAV).
- Six sound wrappers, localisation, audio ID `57`, and settings-aware playback remain registered.
- Frozen source, source page, metadata, CC0 deed, CC0 legal code, attribution, and processing evidence match the audio research record.

Audio research SHA-256: `2c87617e505064368af282bf885664e47e78494efca80f137d9a76ec6d54d655`.

## Exact blocker handoff

Stable sprite IDs, current data inputs, visibility precedence, and recommended Ledger positions/sizes are frozen in:

- `docs/assets/015_utopia_manifesto/gfx_handoff.md`;
- `docs/assets/015_utopia_manifesto/requirement_to_runtime_coverage_2026_07_16.md`.

The recommended repair uses three `32x32` compact Value icons, six `48x48` Calling icons, ten mutually exclusive `300x96` Case cards, seven `300x96` District role bases, and six `48x48` District state overlays. The handoff identifies the exact current case flags/variables, district phases/flags, the missing durable `planned` state, and the missing exact district-role mappings for port town and research town.

## Files edited

- `docs/assets/015_utopia_manifesto/manifest.md`
- `docs/assets/015_utopia_manifesto/gfx_handoff.md`
- `docs/assets/015_utopia_manifesto/icon_animation_handoff.md`
- `docs/assets/015_utopia_manifesto/requirement_to_runtime_coverage_2026_07_16.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/asset_completion_repaired_snapshot_reaudit_2026_07_16.md`

No gameplay, localisation, spec, spreadsheet, binary asset, source-image, interface, GFX, GUI, sound, or music file was edited. No commit was created.

## Validation boundary

This was a static, read-only audit of runtime files, provenance, decoded pixels, DDS/TGA structure, registrations, consumers, and script bindings. It did not launch HOI4 or perform in-engine audio playback. The four P2 findings are direct missing-file/registration/consumer facts and do not depend on engine execution.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications made by this audit: none.
- Omissions in the current asset package: four accepted UI families, as listed above.
- Fallbacks accepted: none.
- Blockers: four P2 asset-completeness blockers.
- Completion claim: not made; verdict is FAIL.
