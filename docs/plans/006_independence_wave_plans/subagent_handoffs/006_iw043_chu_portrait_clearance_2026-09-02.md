# IW-043 CHU portrait clearance: Mirsaid Sultan-Galiev and Karim Tinchurin

Date: 2026-09-02 (Europe/Kyiv).
Owner: bounded `chaosx_portrait_creator` portrait clearance pass.
Scope: existing CHU portrait consumers for states 249/256 and `RG-MIDDLE-VOLGA-KAZAN` only.
No gameplay, character definitions, localisation, flags, central admission, `.gfx`, runtime DDS, RunPod, or ImageGen was changed.

## Executive result

Both consumers remain fail-closed for runtime admission.

The Mirsaid Sultan-Galiev row now has a stronger pre-baseline source candidate: a Commons record for a 1923 archival scan with an Internet Archive source and an annotated rightmost subject, plus a verified exact crop.

The Karim Tinchurin row now has a pre-baseline solo candidate dated 1934, which resolves the prior 1937-date problem, plus a verified exact crop.

Neither candidate clears the rights gate because the Commons records list the photographer/author as unknown and the `PD-old`/`PD-old-70-1923` templates have not received parent/legal acceptance for redistribution.

No source candidate was generated, repainted, relabelled, or substituted for another person.

## Consumer and wiring audit

The four CHU character consumers are the male civilian-large slots in `common/characters/006_independence_wave_characters_registry.txt:269-307`.

The two in this clearance pass are:

| Consumer | Existing character name | Existing GFX sprite | Existing runtime DDS | Existing DDS SHA-256 |
| --- | --- | --- | --- | --- |
| `CHU_independence_wave_middle_volga_congress` | Mirsaid Sultan-Galiev | `GFX_portrait_CHU_independence_wave_middle_volga_congress` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_middle_volga_congress.dds` | `2C4E5E0B00ECEC70D29901BF2938BD0695192B7AF0336E56E9B12CEBB0A2D8A3` |
| `CHU_independence_wave_bolgar_civic_presidium` | Bolgar Civic Presidium (institutional name; Karim is a representative candidate) | `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | `E031470617E94B88168155BB64826DB0BDC13B83A41B4E97245A2DC30BE26F67` |

Both existing DDS files decode as `156x210`, are `131168` bytes, and use the expected legacy uncompressed BGRA layout.

Both existing DDS files were decoded to temporary PNGs and visually inspected; they are painted male portraits, but this pass does not treat their pixels as source, identity, rights, or replacement evidence.

The existing portrait-specific wiring is in `interface/006_independence_wave_portraits_registry.gfx:163-180` and was left unchanged.

The existing recruitment references are in `history/general/006_independence_wave_character_recruitment_registry.txt:74-80` and were left unchanged.

No CHU DDS exists in the canonical `docs/assets/portraits/006_independence_wave/` archive; the two runtime hashes above are the only DDS hashes relevant to these consumers in this pass.

## Mirsaid Sultan-Galiev

### Identity, date, and role

The source is [Commons `File:Mirsaid Sultan-Galiev and Narkomnats Commissars, 1923.jpg`](https://commons.wikimedia.org/wiki/File:Mirsaid_Sultan-Galiev_and_Narkomnats_Commissars,_1923.jpg) with the [Internet Archive scan source](https://archive.org/stream/zhiznnatsionalno01russ#page/32).

The fetched Commons raw record identifies four named men from left to right and explicitly annotates Mirsaid Sultan-Galiev as the rightmost subject at `x=3071, y=286, w=952, h=2327` in a `4095x2619` source.

The Commons description dates the photograph to 1923, while the structured Commons date is the 2015-09-29 upload date.

The Internet Archive metadata record for `zhiznnatsionalno01russ` reports `date=1918` for the scanned serial volume, so the archival publication context is pre-1936 under either the Commons description or the item-level archive date.

Mirsaid Sultan-Galiev is a documented male Tatar revolutionary and Volga political figure, and the existing CHU localisation describes the Middle Volga Congress as chaired by him.

The identity and direct Middle Volga political role fit pass for this consumer; the 1923 image itself is a historical source, not a claim that Sultan-Galiev historically held the fictional CHU office.

### Rights and source status

The raw Commons record lists `author={{unknown|author}}` and applies `{{PD-old-70-1923}}`.

That template is a reported public-domain basis, not an independent redistribution clearance, and the source chain still needs parent/legal acceptance.

The previous `SultanGaliyev0011.jpg` source remains broad-date `before 1940` evidence with a separate rights/source hold; this 1923 archive-backed record is the stronger date candidate but does not remove the legal hold.

Verdict: identity PASS; male PASS; pre-1936 date PASS; role fit PASS; source attribution PASS; crop/framing PASS; rights HOLD; runtime admission HOLD.

### Archived source and crop evidence

The immutable source master is `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons.jpg`.

It is a `4095x2619` RGB JPEG, `3926173` bytes, SHA-256 `00F80D301D89D56148EE2965F7A50327C72994835D8F1806679DF48DAD5AA1A8`.

The same unchanged bytes are retained as `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons_original.jpg` with the same dimensions, byte count, and SHA-256.

The exact source crop is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons_crop.png`.

It is a `995x1340` RGB PNG, `1611539` bytes, SHA-256 `8B03443D7C3D7A2F676A0246E3C80B5FB492A11341AA9C55FA861C25EE52BF70`.

The manual half-open crop rectangle is `[3100, 250, 4095, 1590]`, selected to isolate the rightmost annotated subject without the neighboring seated men.

Crop metadata is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons_crop.json`, `4314` bytes, SHA-256 `71EF5155C020346CFA43AE8F5F72A11768BF60DD5DD238B7DB06C88F4442C5C6`.

The crop metadata records `decoded_pixels_equal=true` in RGBA comparison mode with matching decoded RGBA hash `d1db84c879fe44324c1803ba59f6efc6c9d8e2b13dbe294ba19c763d9b8776b5` and `1333300` compared pixels.

The co-located provenance record is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons.txt`, `4393` bytes, SHA-256 `0F33C633E07A709510C896F571847B9F629C847F863C5C2F0B69B8E2F34C8B8C`.

The 156x210 deterministic review output was reconstructed in memory with Pillow LANCZOS and had SHA-256 `4BE5CD3F98B8A170A51E97CD49A049A9B773883C2D878A0A84C4E7B6CDF93952`, but it was not retained after the parent restored the consolidated archive contract that forbids `156x210` files in this archive.

The source master, exact crop, and temporary 156x210 review were opened and visually inspected.

### Mirsaid replacement state

No approved HOI4-style final was supplied by the user for this row.

The agent did not operate RunPod and did not invoke ImageGen.

No DDS conversion was run because the rights gate and parent admission gate remain open.

The existing runtime DDS remains unchanged and evidence-only.

## Karim Tinchurin

### Identity, date, and role

The new source is [Commons `File:Karim Tinchurin (1934).jpg`](https://commons.wikimedia.org/wiki/File:Karim_Tinchurin_(1934).jpg) with the National Library of the Republic of Tatarstan source page at `https://kitaphane.tatarstan.ru/tinch/pixf.htm`.

The fetched Commons raw record identifies a solo male Karim Tinchurin photograph, uses `date=1934`, names the National Library source, and lists the author as unknown.

Karim Tinchurin (1887-1938) is a documented male Tatar dramatist, actor, director, and theatre organiser.

The existing Tinchurin State Theatre biography evidence supports his theatre leadership and civic-cultural organiser role, which is a defensible regional representative fit for the fictional Bolgar Civic Presidium route.

The 1934 date is within the 1936-centered scenario baseline and removes the prior v90/v95 candidate's one-year-post-baseline 1937 problem.

The source is an identity and role candidate for the institutional consumer, not a claim that Tinchurin historically held the fictional Bolgar office.

### Rights and source status

The raw Commons record lists `author={{author|unknown}}` and applies `{{PD-old}}`.

The unknown photographer and absent first-publication chain leave the public-domain label pending parent/legal acceptance.

The existing 1937 NKVD mug-shot package remains visually and provenance-audited but rights/date-held because its source is outside the accepted baseline.

An additional direct-parent alternate, `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1930_commons.jpg`, is a `580x774` RGB JPEG, `108779` bytes, SHA-256 `BBDE80247CC1C91AF50AD28E6909F4E7BF3E5E41E9DC9D1D2F7E14B24669E405`; its Commons record is circa 1930 with unknown author and `PD-old`, so it is also rights-held evidence rather than a cleared replacement.

Verdict for the 1934 candidate: identity PASS; male PASS; baseline date PASS; role fit PASS; source attribution PASS; crop/framing PASS; rights HOLD; runtime admission HOLD.

### Archived source and crop evidence

The immutable source master is `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons.jpg`.

It is a `342x450` RGB JPEG, `15008` bytes, SHA-256 `F06A8F33505149107E76FF0B3021AA1E235A530693A330BB5BFC147B740B74F7`.

The same unchanged bytes are retained as `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons_original.jpg` with the same dimensions, byte count, and SHA-256.

The exact source crop is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons_crop.png`.

It is a `342x450` RGB PNG, `113876` bytes, SHA-256 `5A64FD1E09861F8FD547CEDFDDA1CD692E20E0A18D041BD4CF5924BA4457762F`.

The manual half-open crop rectangle is `[0, 0, 342, 450]`, retaining the complete solo source without geometric alteration.

Crop metadata is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons_crop.json`, `4304` bytes, SHA-256 `62576AC1D7ACA829DFAF9A103A3047C296AF62A16133026AEE030BC4BAF05A40`.

The crop metadata records `decoded_pixels_equal=true` in RGBA comparison mode with matching decoded RGBA hash `51eb6d9134953c71671eb87e66631b30c43f29bc27a93c8f8c3b92ee4851dc1a` and `153900` compared pixels.

The co-located provenance record is `docs/assets/portraits/006_independence_wave/processed/portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons.txt`, `4289` bytes, SHA-256 `EED397C8B2361C9D364F057D357CEACEBFD981FA55D5A914475ED5342397AE84`.

The 156x210 deterministic review output was reconstructed in memory with Pillow LANCZOS and had SHA-256 `37F6A3E64319AFFCBB65CD5A96877F63DB4286268F43730F199EBADC94570B61`, but it was not retained after the parent restored the consolidated archive contract that forbids `156x210` files in this archive.

The source master, exact crop, and temporary 156x210 review were opened and visually inspected.

### Karim replacement state

No approved HOI4-style final was supplied by the user for this row.

The agent did not operate RunPod and did not invoke ImageGen.

No DDS conversion was run because the rights gate and parent admission gate remain open.

The existing runtime DDS remains unchanged and evidence-only.

## Ownership and collision findings

Exact and variant searches across the current Chaos Redux character, history, GFX, interface, localisation, vanilla, and checked Kaiserreich surfaces found no separate Karim Tinchurin owner.

Mirsaid Sultan-Galiev is the existing CHU identity for the Middle Volga Congress and was not conflated with Sahib-Garey Said-Galiev or any other similarly named person.

No opposite-gender substitute, generic portrait, external-owner transfer, relabelled DDS, or duplicate character was introduced.

## Checks performed and intentionally skipped

The required offline Paradox wiki core pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The installed vanilla character documentation, `common/characters/CHU.txt`, vanilla portrait registry, vanilla leader portrait GFX examples, and the installed leader contact sheet/reference PNGs were consulted.

The matching Event 006 archive-layout, consumer-gate, CHU package-audit, Mirsaid v83, Karim v90, and Karim v95 handoffs were reviewed.

The source crop tool `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v2.0 was used with explicit manual rectangles, and both JSON records prove lossless decoded-pixel equality.

Source and processed PNG dimensions, modes, byte counts, SHA-256 hashes, and both existing runtime DDS headers/dimensions were checked.

No rights/legal parent signoff was available, so rights were not promoted from HOLD.

No independent second admission reviewer was available in this bounded pass, so runtime admission was not promoted.

No `convert_to_dds.py` invocation was made because a rights-held source must not produce a promoted runtime DDS.

No `.gfx`, character, localisation, gameplay, central-admission, or runtime file was edited.

No RunPod operation, ImageGen call, HOI4 launch, or live consumer validation was performed.

## Handoff decision

Keep both CHU consumers outside accepted runtime admission.

Mirsaid's 1923 source is the preferred next legal-review candidate, but the unknown-author `PD-old-70-1923` record still requires explicit acceptance.

Karim's 1934 source is the preferred next date-review candidate, but the unknown-author `PD-old` record still requires explicit acceptance.

If parent/legal review clears either source, a separate owner-controlled pass may create the user-supplied HOI4-style final, rerun identity/role/rights/framing review, convert through `convert_to_dds.py`, and then request parent-owned runtime wiring.

Until those gates clear, the existing runtime DDS files and portrait wiring must remain unchanged and must not be treated as accepted replacements.
