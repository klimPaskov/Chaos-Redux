# IW-050/KOM portrait source audit — fail-closed handoff

Audit date: 2026-08-14.

Status: **BLOCKED — no defensible grounded portrait source located.** No portrait source, crop, processed candidate, DDS, `.gfx` entry, character edit, or gameplay wiring was created.

## Exact vanilla identity and consumer

The Event 006 research row for `IW-050` resolves to the registered vanilla `KOM` tag and explicitly requires a sourced real male period leader when valid, otherwise authentic archival material for the provisional institution; the row says to block until a defensible sourced leader or institution is assigned (`docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51`). The candidate registry also identifies `IW-050` as `Komi`, `KOM`, anchor state `397`/Syktyvkar (`docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:51`).

Installed vanilla defines:

- `common/characters/KOM.txt:3-13`: male `KOM_pavel_murashev`, display name **Pavel Murashev**, civilian country leader, `stalinism`, expiry `1950.1.1.1`, portrait token `GFX_portrait_Pavel_Murashev`.
- `history/countries/KOM - Komi Republic.txt:101`: `recruit_character = KOM_pavel_murashev` in the 1936 setup.
- `interface/_leader_portraits.gfx:5576-5579`: `GFX_portrait_Pavel_Murashev` currently resolves to `gfx/leaders/Europe/Portrait_Europe_Generic_3.dds`, a generic installed texture (156x210), not an attributed Pavel Murashev source portrait.

The vanilla files do not document a historical office for Murashev beyond the generic civilian country-leader role. I therefore do not infer “Komi first secretary,” “congress chair,” or another period office from the name alone. The only defensible Event 006 opening consumer is the existing registered vanilla civilian leader, pending a real source and a role note that does not claim an undocumented office.

## Ownership and collision search

The required exact/variant ownership search covered `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` in both the mod and the installed vanilla tree.

Search terms included `KOM_pavel_murashev`, `GFX_portrait_Pavel_Murashev`, `Pavel Murashev`, `Pavel Murashev`, `Павел Мурашев`, `Murashev`, `KOM`, and the existing Event 005 token `GFX_portrait_KOM_mine_river_committee`.

Matches are limited to the vanilla `KOM_pavel_murashev` character/history/token and the unrelated Event 005 institutional portrait `GFX_portrait_KOM_mine_river_committee` (`interface/005_soviet_collapse.gfx:1959`, consumed by Event 005 effects). No IW-050 character definition, portrait-specific runtime owner, or existing source package was found. The Event 005 institutional texture is not a person source and is not reusable.

## Vanilla reference evidence

The matching installed-vanilla role family was inspected before source research:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md` and `CATALOG.md`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` (eight full `156x210` country-leader references).
- Installed `GFX_portrait_Pavel_Murashev` texture path and dimensions from `_leader_portraits.gfx` above.

The references establish the full country-leader canvas and framing family only. They are not identity sources and were not copied or used as runtime art.

## Grounded-source search and rights verdict

No attributed period image of the exact Pavel Murashev was found in the bounded search. Searches were run for the English and Russian spellings and Komi/Syktyvkar/1936 context.

- Wikimedia Commons MediaSearch API exact and Russian queries returned zero file hits: `https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=Pavel%20Murashev&srnamespace=6&format=json` and equivalent `Павел Мурашев`, `Павел Алексеевич Мурашев`, and Komi/Syktyvkar variants.
- Russian Wikipedia API searches did not return an exact historical Pavel Murashev article; results were surname pages, unrelated Pavel Murashov biographies, and general Komi pages: `https://ru.wikipedia.org/w/api.php?action=query&list=search&srsearch=%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB%20%D0%9C%D1%83%D1%80%D0%B0%D1%88%D0%B5%D0%B2&format=json`.
- Brave web and image searches for `Pavel Murashev Komi`, `Павел Мурашев Коми СССР`, `Павел Мурашев Сыктывкар 1930`, and related role queries returned modern music/entertainment profiles and unrelated **Pavel Murashov** records (including a different WWII soldier), not the vanilla Komi leader. Search entry points: `https://search.brave.com/search?q=Pavel+Murashev+Komi` and `https://search.brave.com/search?q=%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB+%D0%9C%D1%83%D1%80%D0%B0%D1%88%D0%B5%D0%B2+%D0%9A%D0%BE%D0%BC%D0%B8`.

Because no exact identity image, source attribution, date, and rights status can be established, the portrait gate is **blocked**. Modern same-name images and wrong-spelling Murashov images are rejected as identity/era mismatches. I did not select a different Komi, Soviet, or regional officeholder and did not generate or repaint a face.

## Archive/runtime decision

No `source_placeholder` package was archived under `docs/assets/portraits/006_independence_wave/`. The current consolidated Event 006 layout (flat parent for source masters plus `processed/` for crop/metadata evidence) remains untouched because there is no unchanged source master from which to create the mandatory lossless crop, equality JSON, provenance contract, and `156x210` candidate. No runtime DDS or portrait-specific `.gfx` handoff is valid.

`replacement_pending` is **not** set: no styled-final request exists, and this portrait never reached a valid source-placeholder state. The user alone may supply an attributed exact source or a correction to the intended identity; only then can the portrait worker create a source package. RunPod was not opened or operated.

## Remaining blocker and next action

IW-050 cannot receive a grounded portrait until an exact Pavel Murashev archival image (or a user-approved, separately sourced exact institutional identity) is supplied with attribution/date/rights evidence. Do not substitute the generic vanilla Europe portrait as a new source, reuse the Event 005 Komi committee art, use a different Murashev/Murashov, invent a provisional chair, or invoke native ImageGen for this grounded identity.

Checks skipped because the source gate failed: crop extraction, crop/equality review, source hash package, PNG/DDS conversion, visual identity/framing review, `.gfx` registration, and runtime consumer wiring.
