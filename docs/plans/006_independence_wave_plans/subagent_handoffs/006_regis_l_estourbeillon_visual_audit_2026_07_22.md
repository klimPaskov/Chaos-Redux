# Event 006 Régis de l'Estourbeillon portrait visual audit

Date: 2026-07-22  
Scope: read-only visual/provenance audit of the BRI civic-delegate portrait candidate.  
Auditor: generated-event-art subagent  
Source-mode rule: `grounded_identity` requires an attributed sourced real male identity. ImageGen is acceptable only as an identity-preserving HOI4 painted edit of that source; it may not reconstruct or substitute a different face.

## Verdict

**Conditional visual PASS for the selected v2 candidate; not runtime-complete.**

The selected v2 master and its processed native PNG visually retain the same
Régis de l'Estourbeillon shown in the unchanged John Wickens 1904 photograph.
At review scale, the facial silhouette, brow/eyes and leftward gaze, nose,
cheeks/jaw, moustache, ear, apparent age, head angle, hat, and source-supported
Breton costume remain coherent. I found no material face substitution or
material identity drift. The edit reads as a restrained HOI4 leader finish,
not a newly invented officeholder.

This is a visual candidate verdict only. The refinish package remains
`needs_user_review`; it has no final DDS and no runtime wiring. If a parent
review at larger display size finds the nose, eye spacing/gaze, moustache, jaw,
or head angle materially changed from the unchanged source, fail closed and
reject the candidate rather than rationalizing the difference. Do not use the
1898 illustration, a generated replacement face, or a generic/female/advisor/
operative substitute.

## Requirement checks

| Check | Result | Evidence / residual risk |
| --- | --- | --- |
| Exact same-person likeness | **Pass (conditional visual)** | The contact sheet puts the unchanged source crop, ImageGen v1/v2, and processed output together. Selected v2 keeps the source man's moustache, broad facial shape, leftward three-quarter view, eyes/gaze, nose, ear, hat, and upper costume. No material drift is visible at the native 156x210 review size. ImageGen edits cannot prove pixel identity; fail closed if larger-scale inspection finds material feature changes. |
| Male-only compliance | **Pass** | The sourced subject is Régis-Marie-Joseph de l'Estourbeillon (1858–1946), a male Breton regionalist civic figure; the selected output remains visibly male. Manifest and prompt explicitly require the grounded male role. |
| Grounded source gate | **Pass** | BRI is a grounded regional polity and the candidate uses the attributed John Wickens 1904 real-person photograph. No generated identity was used as the source. |
| Source / era fit | **Pass with age note** | John Wickens photograph, *A Book of Mad Celts* (1904), depicts the subject in Breton national costume. Subject was approximately 46 in the source and 77 at the 1936 start; the earlier portrait is period-authentic and the age gap is documented, but remains a presentation risk. |
| Head-and-shoulders crop | **Pass** | Selected master is cropped to preserve full hat, head, shoulders, and source-supported upper-torso costume; processed PNG is exactly 156x210. Crop record is `(0,79,1024,1457)` from the 1024x1536 selected master, then Lanczos resized to 156x210. |
| HOI4 painted style, full/native | **Pass** | Processed RGB PNG is native 156x210. Quiet pale neutral backdrop, muted warm values, restrained brush texture, controlled contrast, and readable silhouette match the inspected vanilla leader family (Stauning/Mannerheim and leaders contact sheet). No raw-photo-only resize or generic oil filter is evident in the supplied review. |
| Invented stereotype / fantasy features | **Pass** | Hat, moustache, clothing, and visible decorative costume elements are source-supported. Prompt explicitly forbids medals, insignia, tartan, pseudo-Celtic motifs, sacred/cultural symbols, flags, text, modern props, caricature, and fantasy details; none are visible in v2/processed output. |
| Rights / source traceability | **Pass with documented caveat** | Commons source page, direct original, John Wickens attribution, 1904 publication context, photographer authority context, public-domain basis, rights caveats, source path, and SHA-256 are recorded. The package honestly retains the Commons missing structured copyright-status caveat and does not present that tag as sole proof. |
| Runtime readiness | **Not complete** | No DDS exists in either named package. Existing sprite mapping remains deferred to `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`; parent must run the repository converter and make the final wiring decision after accepting this visual audit. |

## Source and package evidence inspected

The two named packages were inspected in full. The following are the exact
files and current SHA-256 hashes:

### Sourced replacement package (`bri_regionalist_retry`)

```text
C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg
AC0F77BB97F159264F7FE2E09B9A0EDE2A40B1BAB209FE6DE55CF3A8914A2317  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_masters/BRI/BRI_regis_de_l_estourbeillon_maurice_dulac_1898.jpg
1BA112E1D0B5FC99CF952EBBCADB19B962FD56DD083B80517791E77031C7B229  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_hashes.sha256
48461A09E9184C44FE4483F2124A59F1237CD1F700BB9FF65719882063AB16E7  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/gfx_handoff.md
6CB0035D0A5299D0AA428726804C8B0D958635E8E71CE7386B35563EFD4130DF  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/manifest.md
154FBA4C6F66464713227F873C956FF12D27494CE41728B07128263A7E2D71AF  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/contact_sheets/bri_regionalist_source_candidates_review.png
06453767D157B76340D634EC328758373B24827CE231375D65C926BF1FD83033  docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/search_notes/ownership_and_candidate_log.md
```

The Wickens source is 1145x1707 JPEG; the Dulac alternative is 389x469 JPEG.
The Dulac drawing is visibly a different presentation (line illustration,
different hair/face framing, no source hat/costume) and remains review-gated;
it was not used or accepted.

### Complete refinish package (`bri_regionalist`)

```text
E5F909E046AF3B735A1019A842C2BFE5AC7C9D326D7EEFA57908E77D7E88032C  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/manifest.md
2356149C98BE97FB7092889F3DB30C6ACBFFA996A72F4C4239D2F4B183AE7BB2  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/gfx_handoff.md
CC100E042DB64DB4854FB44901C54C77E9580A137E34EB73D1BCDF5A595CBC54  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/sha256sums.txt
75B0CEB397D92285EB2E502F3D1AA9459DF3CB48B354A6AE21EDFEBF1F5F9891  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/prompt.md
CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png
8BE51C6A25E14BB93CE1996483F0E76CAB76B708118723091C998B49E454418B  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png
BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png
01069C9BA6750562F909222115C071052F84D1C285B7B84BBA0FC3F6D8A00329  docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/contact_sheets/bri_regionalist_identity_review.png
```

Image metadata confirmed by `ffprobe`:

```text
John Wickens source JPEG                 1145x1707, yuvj420p
Maurice Dulac alternative JPEG              389x469, yuvj420p
selected ImageGen master PNG              1024x1536, rgb24
retained ImageGen v1 PNG                  1080x1456, rgb24
selected processed/native PNG                156x210, rgb24
identity review contact sheet              1032x980, rgb24
```

The selected v2 is the file named `imagegen_master.png`; `candidate_v1.png`
was retained only for comparison. The selected prompt explicitly says the
Wickens photograph is the identity-bearing Image 1, canonical refs are
style-only, and only crop/background/subtle finish may change.

## Canonical HOI4 leader references inspected

The canonical library rules (`README.md`) and catalog (`CATALOG.md`) were
read, then the complete `portraits/leaders/` family and contact sheet were
inspected. The relevant style references named by the package and their hashes
are:

```text
08732002182BDCB2BFF3D78B142CC2B3D75DBDB29D4115F9E89CA5BDC6A21B6  .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png
7E78E33E0B691B96B584393F2D363C07A302320F7E6300BDA0FFF261AA98D49E  .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png
8966AE351D1FE8FC13D47CA1C59EC3D8A34DA9101CE5FD65F7ACFF3421BD0401  .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png
```

For completeness, the other six leader refs in that same inspected family
were `afg_mohammed_zahir_shah.png` (SHA-256
`F606BC3C6204E0DBD35D8EDCEB21F87AE6F93A0AE7AD657382C7E9043E8907A0`),
`africa_generic_1.png` (`F37A9AB2CA9460B86DF5E5DB7491B0BA80A405A8E402AE2C0FFB0CB087B03F1D`),
`eth_haile_selassie.png` (`E06BC1BD67CE70E1FB22E39D4C6D2732327D23A58EFEB74B096B456318B7EB4B`),
`ice_sveinn_bjornsson.png` (`860726D268873F21AE0DBD6FB170482F50FAD6393882B97B2B7B7A1814189D14`),
`ire_eamon_de_valera.png` (`FF5F8689F1E8EA75EB88BEA4C4A87DCF60518B1E062EA53BE4A9CEFF3509DCB0`),
and `lux_charlotte.png` (`4947273BE4A501CA67DB37FDB5F4623DDD30791B5156393D26254BB150DE1BF7`)
as listed in the leader-family contact sheet/catalog. All canonical leader
textures are 156x210; the BRI processed PNG matches that native canvas.

Reference-library file hashes:

```text
E6A2F4A4CFDCE04D4C0682103B6C5D38A98557D40E7491CB9F3A9A869EB59C52  .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md
72FDD8110BDFC42CCE194AFAE44D45E6373501342B5DCA5049594BE4FDD1AA37  .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md
```

## Runtime handoff and residual risks

- Preserve the existing `GFX_portrait_BRI_independence_wave_civic_commission`
  sprite and `BRI_independence_wave_civic_delegate` token.
- Final expected texture remains
  `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`.
- No `.gfx`, gameplay, localisation, manifest, or asset file was changed by
  this audit; this handoff is the only new file.
- Parent still must perform the repository-standard DDS conversion and the
  final runtime-path/header validation.
- The principal residual risk is the unavoidable possibility of subtle
  ImageGen face drift outside the native-size review. Under the controlling
  rule, any material drift is a hard reject, not a reason to ship a fallback.
- Rights evidence is well traced but retains the package's honest Commons
  structured-status caveat; do not remove that caveat when promoting durable
  provenance.
