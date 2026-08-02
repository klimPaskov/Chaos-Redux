# IW-030 Montenegro portrait source research handoff v107

Date: 2026-08-02

Subagent: `/root/event6_mnt_rights_source_research_v107`

Scope: sourced visual research and rights/ownership review only. No gameplay, character, localisation, GFX, runtime PNG, or DDS files were edited.

## Verdict

No current MNT portrait row is promoted. IW-030 remains fail-closed for portrait admission.

The strongest new lead is Danilo Aleksandar Petrović-Njegoš (1871–1939), Crown Prince of Montenegro. The source and attribution chain is substantially stronger than the unresolved Jovanović/Đukanović chains, but the candidate is `needs_user_review`, not runtime-ready: the parent must explicitly accept a distinct MNT identity and an independent grounded-portrait audit must pass before any generated or runtime asset is made.

This is not a silent replacement for `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, or `MNT_blazo_dukanovic`.

## Candidate and fit

| Field | Evidence | Outcome |
| --- | --- | --- |
| Candidate | Danilo Aleksandar Petrović-Njegoš, Crown Prince of Montenegro; briefly recognized as King Danilo II in 1921 and head of the royal-house government-in-exile | Explicit Montenegrin Petrović-Njegoš identity is plausible, subject to parent approval |
| Life/date fit | Born 29 June 1871, died 24 September 1939; alive at the 1936 scenario start (age 64) | Pass for adult-male 1936 roster eligibility; source photograph is 1911, not a claimed 1936 likeness |
| Role fit | Crown Prince; led the Royal Montenegrin Army with King Nicholas, Janko Vukotić, and Mitar Martinović during the Balkan Wars and World War I | Strong royal/military role evidence |
| Community distinction | Commons file names Danilo, Crown Prince of Montenegro; independent LOC plate reads `PRINCE DANILO, MONTENEGRO`; matching moustache, hairline, and facial structure across two archival references | Strong identity distinction; no generic Balkan-officer substitution |
| Admission state | `needs_user_review` | No DDS, sprite, character, or runtime wiring is authorized |

## Primary archival source and rights basis

- Commons file page: <https://commons.wikimedia.org/wiki/File:Danilo,_Crown_Prince_of_Montenegro_(1911).jpg>
- Original source URL: <https://upload.wikimedia.org/wikipedia/commons/8/81/Danilo%2C_Crown_Prince_of_Montenegro_%281911%29.jpg>
- Commons raw evidence: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v107_2026_08_02/research/commons_danilo_vandyk_1911.raw.txt`, SHA-256 `9117f1845243fb31925e8ec9502afd084d26e3e5b8e2f04029f8a1fcc633e664`.
- The raw record identifies the 1911 coronation photograph, names Carl Vandyk as photographer, names the source book `Memoari jedne njemacke princeze`, and applies Commons `PD-old-auto-expired|deathyear=1931`.
- Retained creator evidence: `research/wikidata_carl_vandyk_Q17627105.json`, SHA-256 `c823de300e9f74e00f47224acb5e1f8285ce408f6bc2853c76fb5f31585df0cb`; it records Carl Vandyk as 1851-01-17 to 1931-11-18.
- Downloaded source master: `source_masters/mnt_danilo_carl_vandyk_1911.jpg`, 1508x2336 RGB JPEG, SHA-256 `a22428a8229386e4c766473b3d402393b0a6c6b3a052af4fdd09d8e72cd116a`.

The named photographer and death-year-based public-domain claim are the best rights lead found in this pass. The source-book publication/edition chain is not independently established in the retained Commons record, so the status remains `needs_user_review` rather than an unconditional rights PASS.

## Independent corroboration

- Library of Congress item: <https://www.loc.gov/item/2014696620/> and resource <https://www.loc.gov/resource/ggbain.50089/>.
- Retained item metadata: `research/loc_ggbain_50089.json`, SHA-256 `d0fd33c6ac056841eba8108ddfa21265e928675f1232af9a0f2b8df8bc2c9ca`.
- The LOC record calls the image `Prince Danilo, Montenegro, in uniform`, dates the glass negative to 1900, credits Bain News Service as publisher, and states `No known restrictions on publication`.
- Review copy: `reference_sources/mnt_danilo_loc_bain_1900.jpg`, 739x1024 grayscale JPEG, SHA-256 `921a39aab4ec521109f22c3fbed86175ce7765483dbff7cdb0f3823a35b3d8fb`.
- Retained LOC rights page: `research/bain_rights_access.html`, SHA-256 `223bf93d78d72881cc2f1d01d6e50b9d192ddbec51834a72e1a608d7f1252223`.

The LOC rights page also says that the Library does not license the material and that researchers must assess possible third-party restrictions. That caveat is preserved; it is not converted into an invented blanket waiver. The LOC image is corroboration and should not silently replace the named Vandyk source.

## Exact crop evidence

- Crop prepared only for the next review gate: `source_masters/mnt_danilo_carl_vandyk_1911_head_shoulders.png`, 810x1060 RGB PNG, SHA-256 `cd03e7bc897a843cc8449a6b32f1220abc55145ff04afd3577039f962a011b2d`.
- Crop rectangle in the immutable master: `[left=350, top=60, right=1160, bottom=1120]`.
- Equality record: `research/mnt_danilo_carl_vandyk_1911_crop.json`, SHA-256 `cd81b4962ac8559f657371a100af9bd29f1406ac78c174ecb21f0aec38724b72`; generated with `extract_portrait_source_crop.py` v1.0 and reports `decoded_pixels_equal=true`.
- The crop is evidence only. It is not a final 156x210 portrait and must not be wired directly into a sprite definition.

## Ownership and identity gate

Search covered `MNT_danilo`, `MNT_prince_danilo`, `MNT_danilo_petro_njegos`, `Danilo Petrović`, and spelling variants in current Chaos Redux content plus installed vanilla MNT characters, history, GFX, interface, and localisation. No existing MNT Danilo owner was found. Vanilla's `YUG_danilo_kalafatovic` is unrelated and must not be reused.

If the parent accepts this identity, a new stable key such as `MNT_danilo_petro_njegos` may be proposed through the normal country-package process. Do not assign the face to `MNT_kristo_popovic`, either Blažo row, or the unrelated Yugoslav owner.

## Required next gate

1. Parent reviews and explicitly accepts the Danilo identity and retained source/rights chain.
2. Run the grounded real-person portrait sequence from the asset skill using the immutable exact crop as the source lock.
3. Produce a deterministic 156x210 candidate and obtain an independent likeness/style/provenance audit against the canonical vanilla leader/commander references.
4. Preserve a durable ComfyUI/source pair and provenance manifest.
5. Convert to repository-standard DDS only after the independent audit passes.
6. Parent owns all new sprite, character, localisation, GFX, and runtime wiring.

No fallback, relabel, or runtime shortcut is authorized.

## Existing MNT blockers carried forward

- Blažo Jovanović and Blažo Đukanović remain `needs_user_review` because their visual/source chains still rely on unresolved photographer or book-reproduction rights questions.
- Krsto Zrnov Popović remains blocked for lack of a defensible archival author/source/date/license chain.
- This v107 lead does not clear or replace those rows and does not establish full IW-030 content attestation.

## Package and handoff files

- Source-only package: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v107_2026_08_02/manifest.md`.
- Sprite boundary note: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v107_2026_08_02/gfx_handoff.md`.
- The source-only package is intentionally excluded from runtime and contains no processed runtime PNG or DDS.
