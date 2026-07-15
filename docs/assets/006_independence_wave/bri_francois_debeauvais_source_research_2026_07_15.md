# Francois Debeauvais portrait source research — 2026-07-15

## Required acceptance rule

A final real-person portrait requires both:

1. an attributed source whose face is strong enough to preserve identity; and
2. a defensible reuse basis in the source country and the United States.

No candidate met both conditions. BRI portrait content-readiness therefore
remains unset. No low-fidelity runtime fallback is retained and no face was
invented or reconstructed.

## Rights-cleared source rejected for identity weakness

### 2 September 1928 Breiz Atao group photograph

- Source page: <https://commons.wikimedia.org/wiki/File:Breiz_Atao_-_2_septembre_1928_-_le_comit%C3%A9_directeur_et_les_d%C3%A9l%C3%A9gu%C3%A9s_alsaciens_et_corses.jpg>
- Publication: *Breiz Atao*, 2 September 1928.
- Creator: anonymous/unspecified on the source record.
- Identification: the source annotation names the people in the group,
  including Francois Debeauvais.
- Rights: the Commons record treats the anonymous 1928 publication as public
  domain in the United States and in source countries whose anonymous-work
  term has expired.
- Local evidence: `source_png/portraits/bri_francois_debeauvais_group_source.jpg`.
- Rejection: the complete local image is 1210x831, but the identified face
  occupies only about 100x147 pixels and contains severe newspaper screening,
  blur, and compression. It cannot support an identity-preserving 156x210
  painted portrait. ImageGen was not used.

## Sharper candidates rejected for rights

### 10 August 1932 Ouest-Eclair portrait

- Source page: <https://commons.wikimedia.org/wiki/File:Debeauvais.png>
- Publication: *L'Ouest-Eclair*, 10 August 1932.
- Creator: not identified on the source record.
- Local evidence:
  `source_png/portraits/candidates/bri_francois_debeauvais_1932_ouest_eclair_rejected_us_rights.png`.
- Image quality: substantially stronger face and usable identity evidence.
- Source-country status: the Commons record presents an anonymous/collective
  French public-domain rationale.
- United States problem: the page does not provide a defensible US
  public-domain basis. A 1932 foreign publication can remain within the
  95-year US term through 2027. No publication-without-notice or other
  independently verified US exception was established.
- Disposition: rejected; not used for ImageGen or a runtime asset.

### 17 September 1933 Breiz Atao injured portrait

- Source page: <https://commons.wikimedia.org/wiki/File:19330917_Fran%C3%A7ois_Debeauvais_bless%C3%A9_par_les_Camelots_du_Roi_lors_du_rassemblement_de_Saint-Goazec_dans_Breiz_Atao.png>
- Publication: *Breiz Atao*, 17 September 1933.
- Creator: not identified on the source record.
- Local evidence:
  `source_png/portraits/candidates/bri_francois_debeauvais_1933_breiz_atao_rejected_rights_record.png`.
- Rights problem: the page describes a 1933 publication while its US license
  rationale says the work was published before 1 January 1931. That internal
  contradiction cannot support reuse.
- Disposition: rejected; not used for ImageGen or a runtime asset.

### 30 July 1939 Olier Mordrel / Francois Debeauvais photograph

- Source page: <https://commons.wikimedia.org/wiki/File:Breiz_Atao_-_30_juillet_1939_-_Olier_Mordrel_%26_Fran%C3%A7ois_Debeauvais.jpg>
- Publication: *Breiz Atao*, 30 July 1939.
- Creator: not identified on the source record.
- Rights problem: the Commons record explicitly lacks a sufficient United
  States public-domain tag. A 1939 publication is not independently cleared.
- Disposition: rejected. The Wikimedia download was rate-limited during this
  tranche, so the source page—not an incomplete local file—is the retained
  evidence.

## Search coverage

The final pass checked the Wikimedia Commons person category, exact-title and
variant-spelling searches (`Francois Debeauvais`, `Fransez Debauvais`,
`Fransez Debeauvais`), Gallica/BnF results, and pre-1931 date constraints.
No sharper attributable pre-1931 portrait with defensible dual-jurisdiction
rights was found. Unattributed modern reposts were excluded.

## Runtime disposition

- Reserved sprite id: `GFX_portrait_BRI_francois_debeauvais`.
- Registered sprite: none.
- Runtime DDS: none.
- Processed final PNG: none.
- Content-readiness: blocked/unset pending a stronger attributable and
  dual-jurisdiction source.
