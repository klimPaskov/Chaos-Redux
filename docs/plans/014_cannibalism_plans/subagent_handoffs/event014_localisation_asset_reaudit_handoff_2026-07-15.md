# Event 014 Localisation and Asset Reaudit Handoff

Date: 2026-07-15
Mode: narrow-fix audit

## Result

Final P0/P1/P2/P3 counts are 0/0/0/0. The audited Event 014 localisation, secrecy, runtime GFX, flags, portraits, animations, super-events, achievements, and audio are completion-ready.

The authoritative audit is:

`docs/plans/014_cannibalism_plans/audits/event014_localisation_asset_reaudit_2026-07-15.md`

## Edit made

`localisation/english/014_cannibalism_l_english.yml` had seven visible command-cost strings pointing to retired `*_command_trigger` constants. They now use the live `*_command_gate` constants. The zero-decimal localisation formatter rounds each `.99` affordability gate to the exact positive whole spend displayed to the player, matching the paired negative gameplay spend.

## Evidence summary

- Seven required YML files: UTF-8 BOM present, zero `:0`, 3,529 unique entries, 36 nested references with zero missing, 276 constant references with zero missing, and 33 Event 014 scripted-localisation selectors with zero missing.
- Secrecy: both creation paths set `cannibalism_reveal_complete` before public identity or art; ordinary and transformed GUI, all four super-events, Event Details terminal rows, Evolution III, and spoiler-bearing tracker entries remain gated.
- Runtime GFX: 812 references, 598 unique paths, zero missing, and 598 unique hashes.
- Flags: 195 files, exact three tiers, correct 32-bit bottom-left TGA headers, and 195 unique hashes.
- Warlord portraits: 56 source/processed/runtime portraits, 56 unique live hashes, 156x210, and no prison backgrounds.
- Animation: 12-frame ordinary and 16-frame transformed portraits plus 12 non-portrait real-frame packages; 142 unique source frames and 142 unique processed frames in total, with complete sheets, fallbacks, GIFs, manifests, contacts, and GFX handoffs.
- Super-events: four distinct action-heavy 457x328 scenes.
- Achievements: 18 registry entries and 54 unique runtime states using the exact required not-eligible overlay.
- Audio: IDs 49/50/52/53, four OGG and four WAV binaries, eight unique hashes, stereo 44100 Hz, complete sound wrappers, and retained license evidence.
- Retired content and cultural safety: zero Prison Host basenames or live matches; zero ancient-general disclaimer; zero player-facing living Indigenous sacred-authenticity claim.

## Changed files

- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/audits/event014_localisation_asset_reaudit_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localisation_asset_reaudit_handoff_2026-07-15.md`

## Simplifications, omissions, and blockers

None. No fallback was used. No commit was made.
