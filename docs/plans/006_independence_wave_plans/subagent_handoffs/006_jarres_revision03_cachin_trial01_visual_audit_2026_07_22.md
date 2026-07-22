# Event 006 sourced portrait visual audit — Jarres revision 03, Cachin trial 01, Devin trial 01

Date: `2026-07-22`
Reviewer scope: independent visual/source admission only. No source master,
ImageGen master, processed PNG, DDS, GFX, gameplay, source manifest, or skill
file was changed. This handoff is the only changed file in this review.

## Review basis and source gate

All three requested identities are grounded real male people for Event 006.
The source-only gate therefore applies: a generated image may repaint/recompose
the unchanged attributed source, but it may not invent a replacement face. I
read the complete `chaos-redux-event-assets` skill, the retired
`assets/leader_portraits/README.md` (which routes current work to the canonical
root), the canonical root README/CATALOG and portrait contact sheets, the
relevant source manifests, the prior Jarres rejection handoff, every retained
source photograph, every retained full ImageGen master, and every native
`156x210` review PNG.

Canonical comparisons:

- Jarres and Cachin: `assets/vanilla_reference/portraits/leaders/contact_sheet.png`
  and the cataloged `den_thorvald_stauning`, `fin_carl_mannerheim`,
  `ice_sveinn_bjornsson`, and `ire_eamon_de_valera` references.
- Devin's command role: `assets/vanilla_reference/portraits/commanders/contact_sheet.png`
  for role framing, with the leader family for the common painted finish and
  quiet background/value treatment.

The bounded ownership scan found no active vanilla or project character/portrait
owner for `Karl Jarres`, `Marcel Cachin`, or `Henri-Léon Devin`. The current
Karl Jarres localisation entry is a name/description consumer, not an active
character-owner match. No female, fictional, advisor, generic, or fallback
identity is authorized.

## Decision summary

| Candidate | Runtime target | Visual decision | Runtime action |
|---|---|---|---|
| Karl Jarres revision 03 | `GFX_portrait_RHI_independence_wave_provisional_directorate` | **`needs_revision` — reject for admission**; the face remains insufficiently identity-specific and the hat still carries too much of the likeness burden | Do not convert or wire |
| Marcel Cachin trial 01 | `GFX_portrait_BRI_independence_wave_civic_commission` | **Visual gate approved**; recognisable at full and native scale, with only a minor style/metadata note | Parent may run normal native processing/DDS after correcting the master-dimension record |
| Henri-Léon Devin trial 01 | `GFX_portrait_BRI_independence_wave_coastal_commandant` | **`needs_revision` — reject for admission**; likeness is strong, but cap/rank/ribbon treatment adds unverified decoration and the finish is too dark/olive for the canonical commander family | Do not convert or wire |

Approval here is visual/source approval only. It is not a claim that any DDS or
runtime sprite exists.

## 1. RHI Karl Jarres — revision 03

### Provenance and dimensional verification

| Item | Path | Actual dimensions/mode | SHA-256 |
|---|---|---:|---|
| Primary source | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg` | `562x800`, grayscale indexed JPEG | `72c952b0f1a1e3c08a16b20c123466b4bfc737d7c03ae63594cf7e6332c2c8d6` |
| Identity cross-check | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/RHI/RHI_karl_jarres_loc_undated.jpg` | `1024x734`, grayscale indexed JPEG | `d07eb103f4c5fdf13ca06c9d58fdea2f626c14f82060d2b2d92b740df633b36e` |
| ImageGen master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/imagegen_sources/RHI/RHI_karl_jarres_hoi4_revision_03.png` | **`1081x1455`, RGB** (manifest says `1080x1456`) | `4276f09d7218c6ad09c6d2c91576d0f95521c06b897cd4d537a282c7249f4cff` |
| Native review | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/processed_png/RHI/RHI_karl_jarres_hoi4_revision_03.png` | `156x210`, RGB/opaque | `90f395c882ba42f577a44228713125ff2d278698c970dce152348d90d80fe3c9` |

The source hashes and rights/provenance agree with the active-vanilla-conflict
retry manifest. The processed PNG is the expected native canvas. The ImageGen
master is not the documented `1080x1456`; the stated centered `1080x1454`
crop at `x=0,y=1` is not self-proving against the actual `1081x1455` input.
Correct the refinish manifest and record the exact crop before any future DDS.

### Visual findings

| Check | Result | Evidence |
|---|---|---|
| Source identity/role | Pass | The Bundesarchiv 1925 subject and LOC face cross-check are the same Karl Jarres; both are period-appropriate and the source manifest records the grounded Rhenish civic role and no active owner. |
| Full-size likeness | **Fail for admission** | Revision 03 improves the eyes and mouth over the rejected family, but the face is still broad, smooth, and near-symmetrical against both photographs. The long/narrow facial structure, receding/high forehead under the hat, source asymmetry, hooded eyes, and guarded thin mouth are not specific enough to make the result more than a generic middle-aged German civic portrait. |
| Native likeness | **Fail for admission** | At `156x210`, the hat is the strongest identity cue; once it is mentally discounted, the face does not remain unmistakably Jarres. The eyes, nose, cheek width, and jaw read as an interchangeable face. |
| Age/expression continuity | Partial | The apparent age is broadly compatible with the 1925 source and a 1936 start, but the direct neutral gaze is cleaner and more composed than the guarded/slightly downward source expression. Do not solve this with de-aging or beautification. |
| Hat continuity | **Revise** | The crown remains too tall/peaked and the brim too wide and curled compared with the lower crown, restrained crease, and narrower brim in the Bundesarchiv image. The hat is doing too much of the identity work. |
| Clothing continuity | Mostly pass | Dark overcoat, white collar, and tie are appropriate and no forbidden insignia, text, prop, facial hair, or second person was introduced. Lapels remain a little broader/more dramatic than the source. |
| HOI4 painted finish | Partial | This is a genuine painted repaint rather than a raw photograph, but the conspicuous cross-hatch modelling and high local contrast are heavier than the quiet vanilla leader family. |
| Background/value family | Pass with caution | Revision 03 is much closer to the pale warm-grey/cream family than the rejected first family. The pale background is not the blocker; reduce the remaining yellow/olive cast only as part of the face/finish revision. |
| Composition/readability | Pass conditionally | Clean full head-and-shoulders silhouette, uncropped hat, and readable eyes/mouth at native scale. Preserve this framing while fixing the likeness; do not crop tighter around the generic face. |
| Invented detail | Partial fail | No forbidden symbol or object was added, but the overbuilt hat and widened lapels are invented visual details that materially change the identity read. |

### Required revision before another review

1. Repaint from the unchanged Bundesarchiv master, using the LOC image only to
   lock the same person's facial geometry. Restore Jarres's longer rectangular
   face, narrower jaw/chin, high/receding forehead and temples, hooded/asymmetric
   eyes, straight nose, and thin guarded mouth. The face must remain recognisable
   without the hat.
2. Match the archival hat: lower crown, restrained centre crease, and narrower,
   less curled brim. Keep the dark civic overcoat, white collar, and tie with
   restrained lapels; do not add insignia or decorative costume.
3. Keep the restrained painted treatment and pale warm-grey background, but
   reduce conspicuous cross-hatch and harsh facial modelling.
4. Produce a new native `156x210` review PNG and repeat full-size/native likeness
   review before any DDS or GFX work.
5. Correct the manifest's master dimensions/crop record (`1081x1455` actual)
   before the next audit.

## 2. BRI Marcel Cachin — trial 01

### Provenance and dimensional verification

| Item | Path | Actual dimensions/mode | SHA-256 |
|---|---|---:|---|
| Source | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_masters/BRI/BRI_marcel_cachin_gallica_meurisse_1918.jpg` | `5063x7000`, grayscale indexed JPEG | `85fa2c4d485bddde3e5fee903f52a3dc8f91f53f22159b38e1a62164f024e2a9` |
| ImageGen master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/imagegen_sources/BRI/BRI_marcel_cachin_hoi4_trial_01.png` | **`1080x1457`, RGB** (manifest says `1080x1456`) | `b623484563b1efb19fdf466cd4f6bc7eaf2f3fab7ca8396eff7dd294be34dd24` |
| Native review | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/processed_png/BRI/BRI_marcel_cachin_hoi4_trial_01.png` | `156x210`, RGB/opaque | `225ce2f8eaf8092ba63a481e200f70d0dad20df67bf1a5b4fc56c8e8bc02bf7f` |

The Gallica/Agence Meurisse source path, `5063x7000` dimensions, hash, and
documented public-domain/PD-US-expired basis agree with the BRI source manifest.
The ImageGen master is actually `1080x1457`, not the documented `1080x1456`;
the processed native hash and dimensions are correct. Correct that metadata and
record the exact `1080x1454` crop before conversion, but this dimensional issue
does not undermine the source identity or the visual approval below.

### Visual findings

| Check | Result | Evidence |
|---|---|---|
| Source identity/role | Pass | Marcel Cachin is a grounded male French politician born in Paimpol, alive in 1936, with no active vanilla/project character or portrait owner in the bounded scan. The Gallica face-visible head-and-shoulders source is adequate for the BRI civic role. |
| Full-size likeness | **Pass** | The repaint preserves the unusually high forehead and swept-back hair, arched brows, wide eyes, long rounded nose, large curled moustache, long jaw, and serious direct expression. It reads as the same photographed man, not a generic moustached substitute. |
| Native likeness | **Pass** | At `156x210`, the moustache silhouette, high forehead, eye spacing, nose, jaw, and centered head remain readable and identity-specific. |
| Age/expression continuity | Pass | The repaint stays near the source's late-1910s apparent age and serious expression; it does not visibly beautify, de-age, or change the subject's gender presentation. The source date is 1918, so this is a period-source portrait rather than a claim that the man appears exactly at age 67 in 1936. |
| Clothing continuity | Pass | Dark suit, white collar, and tie are retained. The broader lapel and tie texture are minor painterly reinterpretations, not a uniform, insignia, prop, or replacement role. |
| Invented detail | Pass with minor note | Hair mass and moustache tips are slightly fuller/cleaner than the source and the tie has painterly patterning, but no identity-changing object or decoration was invented. |
| HOI4 painted finish | Pass | It is a coherent painted portrait with readable planes, clean silhouette, no photographic artefacts, and no face-replacement seams. Texture is a little more visible than the canonical family but remains compatible with the existing Chaos Redux painted portrait targets. |
| Background/value family | Pass with minor note | The muted warm-grey/olive background (`top corners` approximately RGB `184/182/162` and `182/174/153`) is somewhat darker/greener than the palest canonical leaders but remains quiet, uncluttered, and behind the face. |
| Composition/readability | Pass | Centered head-and-shoulders composition, no clipping, no text, no frame, no second person, and a clean opaque `156x210` canvas. |

### Visual approval boundary

This candidate is **approved for the visual/source gate only**. The parent may
run the normal native portrait processor and standard DDS conversion after
correcting the ImageGen-master dimension/crop record. The approval does not
authorize a fallback, a runtime path into `docs/assets/`, or a new GFX entry by
this subagent.

## 3. BRI Henri-Léon Devin — trial 01

### Provenance and dimensional verification

| Item | Path | Actual dimensions/mode | SHA-256 |
|---|---|---:|---|
| Source | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_masters/BRI/BRI_leon_henri_devin_brest_prefet_1930.jpg` | `6318x8587`, grayscale indexed JPEG | `ab7d69e6f485be51bfc02823bf94187a9239b54f56525ff97223c9e7b2f7e4c0` |
| ImageGen master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/imagegen_sources/BRI/BRI_henri_leon_devin_hoi4_trial_01.png` | **`1081x1455`, RGB** (manifest says `1080x1456`) | `b30ffff5a4bcb82d66f2ac4b8c06421ada4b51b505bc575aa805b609beb0f542` |
| Native review | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/processed_png/BRI/BRI_henri_leon_devin_hoi4_trial_01.png` | `156x210`, RGB/opaque | `7b9e9bf849dd8deeb45c7de9044b31af5429053aa501a18813700038b93cca2c` |

The BRI source manifest records the 1930 Gallica/Agence Rol source, its
PD-1996/PD-France basis, source hash, and the accepted 1936-valid École navale
at Brest command fit. The ImageGen master is actually `1081x1455`, not the
documented `1080x1456`; the native PNG hash and canvas match the requested
review output. Correct the master dimension/crop record before any new render.

### Visual findings

| Check | Result | Evidence |
|---|---|---|
| Source identity/role | Pass | The subject remains Henri-Léon Devin, a grounded male naval officer, and the role/source/ownership gates are satisfied. No replacement face or unrelated officer appears. |
| Full-size likeness | Pass | The long narrow face, low/hooded eyes under the visor, straight nose, thin moustache, narrow mouth, ears, and stern neutral expression track the source closely. This is substantially stronger than the rejected Jarres likeness. |
| Native likeness | Pass conditionally | The face is smaller because the source's cap, shoulders, ribbons, and upper torso are retained, but the eyes, moustache, nose, and cap silhouette remain readable at `156x210`. A tighter head-and-shoulders crop could improve read without discarding the cap or source ribbon row. |
| Age/expression continuity | Pass | The 1930 source and repaint read as the same approximately early-50s officer with the same reserved gaze. |
| Cap fidelity | Partial / revise | The naval cap, anchor-in-laurel device, visor, and stacked bands are preserved structurally, but the generated badge/trim is brighter and more ornate than the source. Keep the source crown, visor, anchor device, and band count/spacing one-to-one. |
| Uniform fidelity | Partial / revise | The dark double-breasted coat, buttons, shoulder boards, and chest bar are recognisable, but the generated shoulder trim and button highlights are embellished rather than strictly traced from the grayscale source. |
| Ribbon fidelity and invented details | **Fail for admission** | The repaint introduces a bright coloured upper ribbon/accent and a more explicit multi-colour lower ribbon presentation that the retained grayscale photograph does not establish. It also brightens rank/shoulder details. Do not invent awards, colours, or insignia semantics for a real officer. Preserve only the visible source arrangement and neutral value relationships. |
| HOI4 painted finish | Partial | It is genuinely painted and has a clean silhouette, but the directional texture is conspicuous and the coat/face modelling is harsher than the quiet canonical commander family. |
| Background/value family | **Revise** | The native background is a dark olive vignette, with top-corner samples around RGB `193/183/156` and `137/129/105`; it is materially darker/greener than the warm pale-grey commander/leader references and competes with the uniform. |
| Composition/readability | Pass conditionally | No clipping, text, frame, or second person; cap and chest remain inside the `156x210` canvas. Preserve the source's commandant framing but consider a modestly tighter crop so the face does not become a tiny detail. |

### Required revision before another review

1. Keep the face geometry, age, gaze, thin moustache, and cap silhouette from the
   source. Do not replace or genericise the officer.
2. Trace the cap crown/visor/anchor-in-laurel device, band count, shoulder
   boards, button spacing, chest bar count, and visible ribbon arrangement from
   the unchanged grayscale source. Remove the unverified coloured upper ribbon,
   extra/brightened trim, or any invented medal semantics; use only source-
   supported neutral values unless an independent historical uniform record is
   added by the parent.
3. Repaint with a quieter HOI4 commander finish: reduce conspicuous cross-hatch,
   soften harsh modelling, and move the background toward the canonical pale
   warm-grey/cream family while keeping a readable dark naval coat.
4. Re-export a native `156x210` review PNG, retaining the cap and source ribbon
   row, and repeat full-size/native identity plus uniform-detail review before
   any DDS or GFX work.
5. Correct the refinish manifest's actual master dimensions (`1081x1455`) and
   exact crop record.

## Runtime and documentation boundary

- No candidate in this audit has an approved DDS path. Cachin is visually
  approved only; Jarres and Devin remain blocked pending the revisions above.
- No `.gfx`, localisation, gameplay, source manifest, or skill edit is included.
- The parent remains responsible for the standard native portrait processor,
  repository DDS converter, runtime path under `gfx/leaders/006_independence_wave/`,
  sprite wiring, and final package admission.
- Any later source/manifest dimensional correction must preserve the unchanged
  original source masters and these verified hashes. No fallback portrait is
  authorized if a revision fails.

## Validation evidence

- `System.Drawing` decode verified the three source masters, three ImageGen
  masters, and three native review PNGs; all native outputs are exactly
  `156x210` opaque RGB PNGs.
- SHA-256 values above were recomputed locally and match the supplied manifests
  or parent handoff values. The three master dimension mismatches are recorded
  explicitly rather than silently accepting the stale claims.
- Canonical leader/commander contact sheets and native family references were
  inspected visually at full and native scale. No DDS conversion, GFX wiring,
  or live-game admission test was run in this bounded visual audit.

Simplifications, omissions, and blockers: Jarres and Devin are deliberately
not admitted; no visual fallback or generic replacement was used. Cachin is the
only candidate receiving visual/source approval in this handoff, and still
requires the parent-owned metadata correction and normal runtime pipeline.
