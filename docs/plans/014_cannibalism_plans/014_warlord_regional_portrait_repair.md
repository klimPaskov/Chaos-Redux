# Event 014 Regional Warlord Portrait Refresh

Status: completed and closed by the 2026-07-15 asset and country-package evidence.

## Corrected runtime contract

- `CBA` through `CBH` are eight origin-agnostic reusable country slots. A slot may receive Island Host, Siege Commune, or March Host gameplay according to its selected state.
- Every slot has seven regional portrait variants: Europe, Asia, Africa, Middle East, North America, South America, and Oceania.
- Portrait selection uses the stored `cannibalism_warlord_region` and `cannibalism_warlord_slot_index`. A submitted warlord keeps the same face and regional name after unification.
- No portrait depicts a prison, detention facility, barred corridor, cell, guard station, prisoner uniform, or penal formation.
- Every portrait is an independently generated 1930s-1940s HOI4-style painted leader bust rather than a full action scene or environmental illustration.
- Every subject is a distinct fictional bald adult male warlord, visibly feral and less conventionally human through expression, posture, scars, pallor, bloodshot eyes, damaged teeth, blood, or grounded physical deterioration. Clothing is invented rough fabric and scavenged period gear.
- At least one warlord holds a skull and visibly licks it. Other portraits use different aggressive behaviors and props so the set does not repeat one composition.
- Regional appearance may be represented, but no portrait copies living ceremonial, sacred, tribal, Indigenous, African, or Pacific regalia. No portrait resembles Hannibal Lecter or an actor likeness.

## Frozen 56-file runtime ledger

For each slot `S` in `CBA`, `CBB`, `CBC`, `CBD`, `CBE`, `CBF`, `CBG`, and `CBH`:

- Europe: `gfx/leaders/014_cannibalism/leader_S_warlord.dds`, sprite `GFX_portrait_S_warlord_europe`.
- Asia: `gfx/leaders/014_cannibalism/leader_S_warlord_asia.dds`, sprite `GFX_portrait_S_warlord_asia`.
- Africa: `gfx/leaders/014_cannibalism/leader_S_warlord_africa.dds`, sprite `GFX_portrait_S_warlord_africa`.
- Middle East: `gfx/leaders/014_cannibalism/leader_S_warlord_middle_east.dds`, sprite `GFX_portrait_S_warlord_middle_east`.
- North America: `gfx/leaders/014_cannibalism/leader_S_warlord_north_america.dds`, sprite `GFX_portrait_S_warlord_north_america`.
- South America: `gfx/leaders/014_cannibalism/leader_S_warlord_south_america.dds`, sprite `GFX_portrait_S_warlord_south_america`.
- Oceania: `gfx/leaders/014_cannibalism/leader_S_warlord_oceania.dds`, sprite `GFX_portrait_S_warlord_oceania`.

Each runtime portrait is 156 by 210, uncompressed one-mip 32-bit BGRA DDS. Its generated source, processed PNG, prompt evidence, hash, crop record, and decoded comparison belong under `docs/assets/014_cannibalism/leader_portraits_refresh/`.

## Animated leader refresh

- Ordinary Hannibal: the canonical `gfx/leaders/014_cannibalism/hannibal.dds` static is frame `000` of a 12-frame source package. Eleven separately image-generated fork, lick, bite, chew, and reset states complete the 1872 by 210 BGRA sheet, preview GIF, contact sheet, manifest, and GFX handoff.
- Transformed Hannibal: the canonical `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` static is frame `000` of a 16-frame source package. Fifteen separately image-generated jaw, tongue, crush, chew, swallow, and reset states complete the 2496 by 210 BGRA sheet, preview GIF, contact sheet, manifest, and GFX handoff.
- Both portrait sheets play at 12 FPS through `gfx/FX/buttonstate_blendframes.lua`. Neither animation relies on transform-only motion.
- Neither animation or static fallback is exposed before `cannibalism_reveal_complete`.

## Acceptance proof

- 56 unique generated source images and 56 exact-size runtime DDS files.
- 28 genuine source frames across the two animations: two canonical static frame `000` images plus 26 separately image-generated action states. Matching sheets, static fallbacks, previews, contact sheets, manifests, and runtime sprite handoffs are present.
- Pixel-decoded comparison proving every DDS matches its processed PNG.
- Manual visual review for HOI4 portrait framing, distinct faces, regional compatibility, feral presentation, period compatibility, requested skull action, and absence of prohibited settings or motifs.

## Closure evidence

- `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/manifest.md` and `cbe_cbh/manifest.md` account for all 56 independently generated warlord sources and final 156 by 210 DDS files.
- Their matching `gfx_handoff.md` files record the stable CBA-CBH regional sprite and runtime paths.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/portrait_regen_a_handoff.md` and `portrait_regen_b_handoff.md` record the two completed production tranches.
- `docs/assets/014_cannibalism/leader_portraits_refresh/hannibal/manifest.md` closes the ordinary 12-frame package, and `wendigo_hannibal/manifest.md` closes the transformed 16-frame package. Both have matching GFX handoffs, static fallbacks, sheets, previews, contact sheets, canonical frame `000` sources, and separately generated action states.
- `audits/event014_country_package_consolidation_reaudit_2026-07-15.md` reports 56 live portrait files, 56 valid dimensions, 56 unique hashes, correct regional selection, the required skull-lick composition, and no prison setting in CBG or CBH.

No fallback, reused portrait, transform-only animation, missing regional variant, or unwired runtime path remains in this repair scope.
