# Historical scientist roster implementation handoff

Date: 2026-08-14.

## Outcome

The historical CBRN scientist roster now contains 67 static scientist identities across Australia, Canada, the United Kingdom, France, Germany, Japan, Poland, the Soviet Union, and the United States.

The implementation adds 46 new scientist identities and converts the nine formerly generated named scientists into static characters while retaining the twelve established dual-role scientist/advisor characters.

All 67 characters are recruited once by their country-scoped startup grant.

## Gameplay files

- `common/characters/cbrn_historical_specialists.txt` recalibrates the 12 established dual-role scientists without changing their advisor blocks or AI logic.
- `common/characters/cbrn_historical_scientists.txt` defines 55 scientist-only characters, including the nine static migrations and 46 new identities.
- `common/scripted_effects/chaosx_startup_history_effects.txt` replaces generated identity construction with static recruitment, adds the new country rosters, removes unreferenced helper effects, and preserves all 21 established `chaosx_scientist_*` flags.
- `localisation/english/chaosx_characters_l_english.yml` supplies one name and one factual description for every scientist.

## Profile calibration

The complete 67-row specialization, skill, and trait matrix is documented in `docs/systems/cbrn_historical_scientists.md`.

Ratings use file-scoped constants for skill 1 through 4, with no skill-5 profiles.

Skill 4 is limited to major authorities, program leaders, and decisive technical contributors; administrators and perpetrators without a strong direct scientific record remain at skill 1.

The implementation rebalances several conspicuous existing profiles: Shiro Ishii is skill 3 with Resourceful and Inhumane rather than a five-trait genius stack, Grigory Mairanovsky is a skill-2 chemical-warfare specialist with Inhumane CW, Ivan Velikanov is a skill-4 biological-warfare specialist with Brilliant Theorist and Resourceful, and the formerly generated Ernst Chain, Erich Traub, and Murray Sanders receive stable historically calibrated definitions.

## Portrait package

The user supplied 71 DDS files representing 70 unique images.

Sixty-six unique identities were installed: 20 existing runtime portraits were replaced and 46 new portrait sprites and textures were added.

Eleven established 65x67 advisor cards were regenerated from the accepted replacement portraits.

Four duplicate or alternate candidates were archived without creating duplicate identities.

The user identified `6925d2612b927.image_00001.dds` as Erich Traub, and it now replaces the existing Traub runtime DDS under the stable character and sprite contract. `s-l1200_00001.dds` is explicitly ignored and retained as `not_needed` evidence without an identity or runtime assignment.

The durable asset evidence is under `docs/assets/portraits/016_brilliant_scientist/`, with the full manifest at `docs/assets/portraits/016_brilliant_scientist/manifest.md` and the portrait-worker handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_scientist_portrait_install_2026-08-14.md`.

## Independent audits

The country-package audit found 67 unique definitions and 67 unique recruits, one specialization per scientist, zero matrix mismatches, zero generated duplicates, all 21 established identity flags preserved, all 12 advisor/AI blocks unchanged from `HEAD`, and complete portrait GFX/DDS resolution.

The audit caught Canadian recruits in the wrong country grant during review; the final source places Otto Maass, Frederick Banting, and Claude E. Dolman under `chaosx_startup_grant_can` and leaves Bulgaria unchanged.

The localisation audit confirmed all 134 roster keys exactly once and corrected 17 factual or clarity defects, including professions and wartime roles for Harold Hartley, Murray Sanders, Sergei Muromtsev, Karl Friedrich Meyer, Edwin Broun Fred, William Hagan, and several perpetrator descriptions.

The portrait parent review passed all 66 installed large portraits and 11 regenerated advisor cards at native and enlarged review scales.

No character/scientist renderer is exposed by the installed HOI4 MCP server.

The probability inspector found no supported weighted surface in the unchanged advisor `ai_will_do` blocks, and no probability-bearing gameplay value was changed.

## Portrait disposition

No portrait input remains blocked. The user-corrected Traub input is wired to the existing consumer, and the second anonymous file remains intentionally unwired under the explicit `not_needed` disposition.
