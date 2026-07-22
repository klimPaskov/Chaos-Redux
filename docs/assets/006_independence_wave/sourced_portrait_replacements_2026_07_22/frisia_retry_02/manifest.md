# Event 006 Frisia sourced-portrait retry 02

Research date: 2026-07-22. Scope is source-mode research and unchanged original
master acquisition for the two grounded AGX real-male character identities. No
portrait treatment, crop, resize, PNG preview, DDS, `.gfx`, gameplay,
localisation, advisor, `_small`, generic, female, or flag asset was created.

The retry found stronger exact-person archival sources for both requested roles.
The source files below are source-ready, but the downstream identity-preserving
HOI4 treatment remains `needs_user_review`; the failed ImageGen refinishes are
not reused. The newly acquired 1919 Reenalda uniform portrait is both clearer
and more role-specific than the prior source; the 1915 garden photograph remains
an exact-person identity comparison.

## Source ledger

The selected commander master is the 1919 uniform source documented in the
`Selected commander source override` section below. The 1915 row is retained as
an exact-person comparison source, not as a second runtime consumer.

| Runtime role | Exact person / source status | Original source master | Source, date, rights basis | Dimensions / bytes / SHA-256 | Head-and-shoulders feasibility and role notes |
|---|---|---|---|---|---|
| AGX civic leader, `AGX_friesland_coastal_council` (`GFX_portrait_AGX_friesland_coastal_council`) | **Douwe Kalma (1896–1953)**; `source_ready`, downstream portrait `needs_user_review` | `source_masters/AGX_douwe_kalma_1917.jpg` | [Commons file page](https://commons.wikimedia.org/wiki/File:Portret_fan_Douwe_Kalma,_1917_ca._archiefnr_1990.jpg); [unchanged original](https://upload.wikimedia.org/wikipedia/commons/d/d6/Portret_fan_Douwe_Kalma%2C_1917_ca._archiefnr_1990.jpg); [Tresoar collection record](https://tresoar.nl/zoeken/collectie/cf64b17f-5d0c-46f9-9209-a7f60c185068). Tresoar catalogued portrait, F.O. Strüppert (Leeuwarden), circa 1917; archive field says `geen auteursrecht (publiek domein)` and Commons records Public domain with no attribution requirement. | `691x1013`, RGB, `87,040` bytes; `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf` | Clear centered frontal head, shoulders, tie and jacket; a vertical 156x210 crop is straightforward (review-only estimate around source x=70–620, y=70–850). Small dark pinhole/dust mark at upper-left forehead is source damage and must not be reconstructed into a different face. Real Frisian writer/nationalist, alive in 1936 (about 40), direct civic/municipal leadership fit. |
| AGX coastal commander, `AGX_friesland_coastal_commander` (`GFX_portrait_AGX_friesland_coastal_commander`) | **Pieter Reenalda (b. 1887)**; `source_ready`, downstream portrait `needs_user_review` | `source_masters/AGX_pieter_reenalda_1915_garden.jpg` | [Commons file page](https://commons.wikimedia.org/wiki/File:Portret_van_Pieter_Reenalda_in_de_tuin,_1915,_archiefnr_318-29.jpg); [unchanged original](https://upload.wikimedia.org/wikipedia/commons/5/55/Portret_van_Pieter_Reenalda_in_de_tuin%2C_1915%2C_archiefnr_318-29.jpg); [Tresoar collection record](https://tresoar.nl/zoeken/collectie/35b90c00-f265-44f3-a669-956995455c9e). Tresoar catalogued photograph by F.O. Strüppert, 1915; archive field says `geen auteursrecht (publiek domein)` and Commons records Public domain with no attribution requirement. | `1023x1619`, grayscale `L`, `91,591` bytes; `d97dc109f6d9e172b63004a0655fb8995c9bd7d7e3935dd6a85858083414aee2` | Clear three-quarter head-and-shoulders/torso with face, hair, moustache and age-appropriate 1915 civilian dress; a 156x210 crop is feasible (review-only estimate around source x=180–760, y=220–1010). Tresoar family-archive record identifies Pieter Reenalda; his KPM first-officer role is explicit in the companion 1911 uniform record below. Because this image is civilian/garden rather than uniformed, retain the role-caveat and have the parent choose between identity clarity and maritime-uniform context. |
| AGX coastal commander role-context candidate (not a second identity) | **Pieter Reenalda (b. 1887)**; retained unchanged prior source, `source_ready`, no new treatment | `source_masters/AGX_pieter_reenalda_1911_uniform_prior.jpg` | [Commons file page](https://commons.wikimedia.org/wiki/File:Eerste_officier_KPM_Pieter_Reenalda_in_uniform,_1911,_archiefnr_318-29.jpg); [unchanged original](https://upload.wikimedia.org/wikipedia/commons/8/8d/Eerste_officier_KPM_Pieter_Reenalda_in_uniform%2C_1911%2C_archiefnr_318-29.jpg); [Tresoar collection record](https://tresoar.nl/zoeken/collectie/2fec947d-31eb-4806-93cd-02510a98fc09). Tresoar family archive, photographer unknown, 1911; archive field says public domain and Commons records Public domain. This bitstream was already acquired in the preceding source package and is copied unchanged here for side-by-side role review. | `1243x1787`, grayscale `L`, `183,898` bytes; `2830fdc7d56040c2a3fa6a6f686bfd73126612786cc6eba80d428863190c488f` | Full figure in KPM first-officer uniform; head-and-shoulders crop is feasible, but the face is less clear than the 1915 garden source at native resolution. It is the strongest direct visual proof for a maritime/coastal command role. |

### Selected commander source override

The source ledger above retains the prior 1911 uniform master for provenance
comparison. The **selected** retry source for downstream processing is now
`source_masters/AGX_pieter_reenalda_1919_uniform.jpg`: 1206x1765 grayscale,
145,425 bytes, SHA-256
`8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`. It is a
Tresoar family-archive photograph (unknown maker, 1919; collection GUID
`4fddaece-1058-470b-be2a-29e4e9e236ac`) explicitly captioned as Pieter Reenalda
in uniform. The archive declares it public domain and Commons records the same.
The source has the clearest face and strongest direct maritime-command role fit
found in this retry. The 1915 garden source remains an exact-person alternate
for identity comparison only.

## Candidate comparison retained for review

The retry downloaded additional unchanged originals only for comparison; they
are not runtime assets and were not treated as substitutes:

| Candidate | Path | Source facts | Disposition |
|---|---|---|---|
| Reenalda, 1915 garden photograph | `source_masters/AGX_pieter_reenalda_1915_garden.jpg` | 1023x1619 grayscale, 91,591 bytes, SHA-256 `d97dc109f6d9e172b63004a0655fb8995c9bd7d7e3935dd6a85858083414aee2`; Tresoar `35b90c00-f265-44f3-a669-956995455c9e`, 1915, F.O. Strüppert, public-domain archive field. | Clear exact-person identity and excellent crop feasibility, but civilian garden dress is weaker role context than the selected 1919 uniform source. |
| Reenalda, 1919 uniform source (selected) | `source_masters/AGX_pieter_reenalda_1919_uniform.jpg` | 1206x1765 grayscale, 145,425 bytes, SHA-256 `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`; Tresoar `4fddaece-1058-470b-be2a-29e4e9e236ac`, 1919, unknown maker, public-domain archive field. | Promoted to selected source after visual review: the clearest face and direct maritime-uniform role evidence found in this retry. |
| Kalma, 1924 office photograph | `candidates/kalma/kalma_1924.jpg` | 1634x932 RGB, 173,070 bytes, SHA-256 `b5edfd9047fc6e61f2cefe00732135ae4925614c0bf36fc3b1388c6c87225057`; Tresoar `fc5b1c8e-dccf-45ff-9fde-fea32b3bb959`, circa 1 Mar 1924, unknown maker, public-domain archive field. | Exact person and good contextual civic image, but horizontal desk scene gives a smaller face and weaker portrait crop than the selected 1917 source. |
| Kalma, 1923 group photograph | `candidates/kalma/kalma_1923_group.jpg` | 931x1600 RGB, 268,488 bytes, SHA-256 `d34b938635be40fe7ecff54541e2b53d3806780c03e88128707e539d18d96e1b`; Tresoar `39fa5891-5d91-4fb4-9b5b-7f9cfc54409b`, circa 1923, unknown maker, public-domain archive field. | Exact person is in a multi-person group; not a defensible single-person portrait base. |
| Reenalda, 1911 square portrait | `candidates/reenalda/reenalda_1911_square_ipv4.jpg` | 659x653 RGB, 19,350 bytes, SHA-256 `c6087edd52d6b57c52f552e005131de025de2aca177e204ab8efe7714b6cb0e2`; Tresoar `2c33be44-930c-4846-a6e4-4478eac9a427`, 1911, unknown maker, public-domain archive field. | Face is overexposed and the crop is less reliable than the selected 1915 source. |
| Reenalda, 1911 Buyskes group | `candidates/reenalda/reenalda_buyskes_1911.jpg` | 674x961 RGB, 45,710 bytes, SHA-256 `001e13526bac84a9245759d5e254af0295412190b63e005023ac77d4c7dfdfda`; Tresoar `dce76980-a818-4901-9399-5cb24941ffcd`, 1911, unknown maker, public-domain archive field. | Exact KPM officer label, but face is small in a three-person shipboard group; retained only as role corroboration. |
| Reenalda, 1903 costume | `candidates/reenalda/reenalda_1903_costume_ipv4.jpg` | 650x1043 RGB, 85,543 bytes, SHA-256 `01d882c34c865bd9b423d8e8bbd12921d09ffae12e1d11e2cb25c89ebd238dbe`; Tresoar `7552ca06-74ae-4a34-8ace-b7475eb055f4`, 1903, unknown maker, public-domain archive field. | Face is clear, but the source depicts Reenalda at approximately age 16, too young to be the strongest 1936 command portrait base. |

Review sheet: `candidate_contact_sheet.png` (review-only; no game wiring).

## Identity and ownership gate

Search date: 2026-07-22. Exact and variant terms searched were `Douwe Kalma`,
`Kalma, Douwe`, `Douwe_Kalma`, `Pieter Reenalda`, `Reenalda, Pieter`,
`Pieter_Reenalda`, and `Reenalda`.

- **Vanilla:** no hits in `common/characters/`, `history/countries/`,
  `gfx/leaders/`, `interface/`, or `localisation/` for either person or any
  exact variant. No vanilla character, leader, commander, operative, portrait,
  or officeholder consumer resolves to either identity.
- **Chaos Redux:** no exact-person hit in the character/history/GFX/interface
  roots. The only full-name literals are the intended AGX display strings in
  `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:5-6`.
  The live owners are the package tokens
  `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-125`,
  recruited by `history/countries/AGX - Frisia.txt:17-18`; both are explicitly
  `gender = male`. The leader has only the large civilian portrait consumer;
  the commander has only the large army portrait consumer and is guarded as a
  corps commander. No advisor, dossier, `_small`, or alternate-country owner
  was found.
- No transfer/availability guard is needed because no origin roster owns either
  real person. The AGX package is the sole intended owner.

## Source-mode and processing disposition

AGX/Frisia is a grounded, plausibly historical regional polity. Both one-person
portraits therefore remain sourced real-person assets; no generated, generic,
female, advisor, `_small`, or invented-face substitute is allowed. The selected
masters clear the source identity/era/rights/ownership gates, but no downstream
identity-preserving HOI4 repaint was attempted in this source-only retry. The
parent may route the unchanged masters through the real-person processing review;
if identity drift recurs, mark that portrait `blocked` rather than substituting
another face.
