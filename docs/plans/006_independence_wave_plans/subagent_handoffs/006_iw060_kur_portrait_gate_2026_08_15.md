# IW-060 KUR country-leader portrait source gate

Date: 2026-08-15

Status: SOURCE-ONLY EVIDENCE; RUNTIME PORTRAIT GATE FAIL-CLOSED PENDING RIGHTS REVIEW.

Scope: audit the installed vanilla KUR country-leader roster for the 1936 opening, inspect the matching vanilla leader portrait references, research one period-compatible attributable source, and retain only source/crop evidence under the Event 006 flat portrait archive. No character override, gameplay, localisation, central admission, Join, DDS, GFX, RunPod, generated face, or 156x210 archive file was created.

## Vanilla KUR opening roster

The installed source is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/KUR.txt`, with recruitment in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/KUR - Kurdistan.txt`.

| Recruit order | Character token | Localised name | Country-leader ideology | Ideology group | Large portrait token in `KUR.txt` | Vanilla opening status |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `KUR_qazi_muhamad` | Qazi Muhammad | `marxism` | communism | `GFX_portrait_PER_qazi_muhammad` | First communist-party leader and later succession candidate; not the 1936 country leader. |
| 2 | `KUR_mahmud_barzanji` | Sheikh Mahmud Barzanji | `despotism` | neutrality | `GFX_portrait_Sheikh_Mahmud_Barzanji` | First non-aligned-party leader and later succession candidate; not the 1936 country leader. |
| 3 | `KUR_ishan_nuri` | Îhsan Nûrî Paşa | `fascism_ideology` | fascism | `GFX_portrait_kur_ihsan_nuri` | First fascist-party leader and later succession candidate; also has a field-marshal role. |
| 4 | `KUR_seyid_riza` | Seyid Riza | `conservatism` | democratic | `GFX_portrait_kur_seyid_riza` | **Opening country leader.** `set_politics = { ruling_party = democratic }` selects the first recruited democratic leader. |

The country history recruits these four country leaders in the order above before `set_politics`, and the offline country-creation/character references state that the first recruited character in each ideology group becomes that party's leader while `set_politics` forces the requested ruling ideology. Therefore the exact vanilla KUR 1936 opening leader is `KUR_seyid_riza` (Seyid Riza); the other three are live country-leader succession candidates, not missing identities to be replaced.

The rest of `KUR.txt` is not part of the country-leader roster: `KUR_ferzende_bege_haseni` is a corps commander, `KUR_ihsan_nuri` is a separate advisor token, and the remaining `KUR_*` entries are advisors or high-command roles.

## Vanilla portrait wiring audit

The exact installed KUR large texture is `gfx/leaders/KUR/portrait_kur_seyid_riza.dds`, registered as `GFX_portrait_kur_seyid_riza` in `interface/_leader_portraits.gfx`; its small dossier sprite is `GFX_portrait_kur_seyid_riza_small` using `gfx/interface/ideas/idea_KUR_seyid_riza.dds`.

The Qazi character references `GFX_portrait_PER_qazi_muhammad`, but the installed leader GFX file defines `GFX_portrait_Qazi_Muhammad` instead, pointing to shared `gfx/leaders/SYR/Portrait_Arabia_Generic_1.dds`; no exact `GFX_portrait_PER_qazi_muhammad` definition was found in vanilla during this audit.

The Mahmud character references the defined `GFX_portrait_Sheikh_Mahmud_Barzanji`, which points to shared `gfx/leaders/SYR/Portrait_Arabia_Generic_land_1.dds`.

The Ihsan character references `GFX_portrait_kur_ihsan_nuri`, but the installed leader GFX file defines `GFX_portrait_Ihsan_Nuri_Pasa` instead, and that sprite points to `gfx/leaders/KUR/portrait_kur_ihsan_nuri.dds`, which is absent from the installed KUR leader folder; this is recorded as vanilla wiring evidence only and was not patched here.

The exact installed Seyid DDS was decoded to a temporary inspection PNG outside the repository and compared with the canonical leader reference shelf; no vanilla art was copied, modified, or used as a face source.

## Source candidate: Seyid Riza

The selected opening-leader source is Wikimedia Commons [File:Seyid Rıza 3.jpg](https://commons.wikimedia.org/wiki/File:Seyid_R%C4%B1za_3.jpg), with the [direct original](https://upload.wikimedia.org/wikipedia/commons/f/f4/Seyid_R%C4%B1za_3.jpg). Commons describes the single visible subject as Seyid Rıza, gives an image date of `before 1938`, identifies the author as unknown, and displays `Public domain`, `Copyrighted=False`, `AttributionRequired=False`, and the `PD Tr` category.

The captured [Seyid Riza identity reference](https://en.wikipedia.org/wiki/Seyid_Riza) dates him to circa 1863–15 November 1937 and identifies him as an Alevi Kurdish political leader of Dersim, a religious figure, and leader of the Dersim rebellion; it also records his Hesenan leadership and opposition to Turkish authorities before the March 1937 rebellion.

This is a strong role/date fit for the 1936 democratic opening leader, but rights do not clear independently: the Commons record's author is unknown and its source credit is an Instagram repost URL rather than a verifiable archive or first-publication chain. The source is therefore retained as `source_only_needs_user_review`, not as an admitted runtime `source_placeholder`.

## Retained evidence

The untouched source master is `docs/assets/portraits/006_independence_wave/iw060_kur_seyid_riza__portrait_kur_seyid_riza_original.jpg`, 674x1024 RGB JPEG, 52,502 bytes, SHA-256 `e31dc8a06fa9a90bbf40a8156774143dcb21727bd121b28948aa7916919db4f5`.

The lossless head-and-shoulders crop is `docs/assets/portraits/006_independence_wave/processed/iw060_kur_seyid_riza__portrait_kur_seyid_riza_source_crop.png`, 500x675 RGB PNG, 319,770 bytes, SHA-256 `882dcf3479f815222b2d007ee59927d9ca61966ddce10367c6b2c2404bdf227f`, using source rectangle `(left=85, top=74, right=585, bottom=749)`.

The crop proof is `docs/assets/portraits/006_independence_wave/processed/iw060_kur_seyid_riza__portrait_kur_seyid_riza_source_crop.json`; the provided crop tool reports decoded RGBA equality and matching RGBA SHA-256 `a220983438d74645bde753e6846477ddf89058e44d4c179755082e76b0afe13a`.

The review-only nearest-neighbour enlargement is `docs/assets/portraits/006_independence_wave/processed/iw060_kur_seyid_riza__portrait_kur_seyid_riza_source_review_4x_nearest.png`, 2000x2700 RGB PNG, SHA-256 `6af249ce2005abd6ea23a070c10c3499b8850abfedb40efd7fa18c56d13ff7f7`; native and 4x review preserve the single face, hat, beard, upper torso, and source-specific clothing without repainting or substitution.

The co-located provenance contract is `docs/assets/portraits/006_independence_wave/processed/iw060_kur_seyid_riza__portrait_kur_seyid_riza_provenance.txt`; captured source pages are `iw060_kur_seyid_riza__commons_page.html` and `iw060_kur_seyid_riza__identity_page.html` in that same `processed/` directory.

## Gate and handoff

Identity verdict is `PASS_BOUNDED` for source evidence, framing verdict is `PASS_BOUNDED` for source evidence, and provenance/rights verdict is `FAIL_CLOSED_PENDING_RIGHTS_REVIEW`.

No `156x210` PNG was retained in the Event 006 archive, no DDS was produced, no `.gfx` entry was added, no character portrait reference was overridden, and the existing vanilla `KUR_seyid_riza` wiring remains untouched.

`styled_final` was not requested, `replacement_pending` is false, and RunPod was not opened, operated, configured, queued, or monitored.

Parent action if this identity is desired: obtain an independently attributable archive/publication and rights basis for the unchanged Seyid Riza source, then route the source through the complete portrait pipeline without changing the runtime basename; otherwise keep IW-060's KUR portrait surface blocked and do not substitute a generated face, generic portrait, or another KUR leader.

No central admission, Join, gameplay, country setup, character identity, trait, localisation, or unrelated UI files were edited.
