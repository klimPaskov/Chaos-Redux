## Event 012 Africa Bestiary Flag Variant Handoff

Date: `2026-06-17`

Scope completed: fictional ideology variant flag package for the five bestiary tags that previously only had base no-suffix flags.

Tags covered:

- `CTL` = Chimpanzee Telegraph League
- `OKP` = Okapi Court
- `TRM` = Termite Citadel Engineers
- `HGD` = Honeyguide Commons
- `GHC` = Great Herds Compact

Ideology suffixes created for every tag:

- `_communism`
- `_democratic`
- `_fascism`
- `_neutrality`

Files changed:

- `gfx/flags/<TAG>_<ideology>.tga` for all 20 normal-size variants
- `gfx/flags/medium/<TAG>_<ideology>.tga` for all 20 medium-size variants
- `gfx/flags/small/<TAG>_<ideology>.tga` for all 20 small-size variants
- `docs/assets/012_africa/generated_flags/source_png/variants/*`
- `docs/assets/012_africa/generated_flags/processed_png/variants/*`
- `docs/assets/012_africa/generated_flags/contact_sheets/012_africa_bestiary_variant_flags_contact_sheet.png`
- `docs/assets/012_africa/generated_flags/manifest.md`

Important preservation note:

- Existing base no-suffix flags were left untouched for `CTL`, `OKP`, `TRM`, `HGD`, and `GHC` in normal, medium, and small sizes.

Source mode:

- Generated symbolic package.
- I used the built-in `$imagegen` workflow for concept prompting per family, then built the final flat source masters locally so the end result matched the established Event 012 generated-flag style and remained readable at HOI4 flag sizes.

Exact generated variant families:

- `CTL_communism`, `CTL_democratic`, `CTL_fascism`, `CTL_neutrality`
- `OKP_communism`, `OKP_democratic`, `OKP_fascism`, `OKP_neutrality`
- `TRM_communism`, `TRM_democratic`, `TRM_fascism`, `TRM_neutrality`
- `HGD_communism`, `HGD_democratic`, `HGD_fascism`, `HGD_neutrality`
- `GHC_communism`, `GHC_democratic`, `GHC_fascism`, `GHC_neutrality`

Design notes by family:

- `CTL`: kept the chimp-hand and telegraph-network motif, but varied the field structure, node treatment, and central authority symbol by ideology.
- `OKP`: kept the okapi tribunal medallion logic, but shifted between court standards, river-law bands, and more rigid command framing.
- `TRM`: kept the termite citadel mound as the anchor symbol, but reworked the surrounding geometry into workers' braces, survey circles, or hard authoritarian framing.
- `HGD`: kept the honeyguide bird and comb language, but varied between commons-ring, civic-band, directional war-sigil, and guidance-banner treatments.
- `GHC`: kept the herd-horn / waterhole identity, but changed the surrounding seal and field layout so the four ideologies are not recolor copies.

Validation performed:

- `file` on all 60 newly created TGA files.
  Expected and observed sizes:
  `82x52`, `41x26`, and `10x7`.
- Verified that `file` output did not include `- top` on the new TGA files.
- Count check:
  `20` normal + `20` medium + `20` small = `60` new TGA files.
- Duplicate check across the new variant TGAs:
  no duplicate hashes were reported.
- Visual QA on a full-family contact sheet and on the small-flag board to confirm orientation and family distinctness.
- QA pass corrected an intermediate transparency-hole issue in some ring motifs before final export.

Skipped validation:

- No in-game wiring or `.gfx` checks were run because that was explicitly out of scope for this subagent task.

Remaining risks:

- The `10x7` tier is readable by palette and silhouette, but some interior emblem detail necessarily compresses into abstract forms at that size. The normal and medium flags preserve the intended distinctions more strongly.

Parent follow-up:

- Review the contact sheet and the five family designs for tone fit.
- If any one ideology family needs a stronger route-specific symbolism pass, the source masters already exist under `docs/assets/012_africa/generated_flags/source_png/variants/` for targeted revision without touching the base flags.
