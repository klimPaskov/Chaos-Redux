# Event 006 ARX Sardinia rights-clear portrait-source retry

Date: 2026-07-22  
Owner: sourced visual-asset subagent  
Scope: source-only research for the unresolved ARX Sardinia crown/council and
army/coastal-command portrait roles. No runtime GFX, gameplay, localisation,
crop, resize, processing, PNG/DDS conversion, or portrait wiring was done.

## Deliverables

- [ARX retry manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/manifest.md)
- [SHA-256 inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/source_hashes.sha256)
- [Unchanged source masters](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/source_masters/sardinia/)
- [Documentation-only GFX handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/gfx_handoff.md)
- [Ownership and candidate log](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/search_notes/ownership_and_candidate_log.md)

## Result

| ARX role | Candidate | Disposition |
|---|---|---|
| `ARX_sardinian_crown_consultative_council` | Prince Adalberto di Savoia-Genova, Duke of Bergamo | `needs_user_review`: 1935 photographic master, House of Savoy-Genova dynastic identity, and 1935–36 general/division-command record. Parent exact/variant scan found no owner across Chaos Redux, vanilla, Kaiserreich, or approved mods `2265420196`/`1458561226`. Commons `PD-Italy` lacks publication evidence needed to establish the US condition independently; rights and visual review remain required. |
| `ARX_gavino_piras` | Prince Adalberto di Savoia-Genova, Duke of Bergamo | `needs_user_review`: strong 1935–36 active-general role fit; using one dynastic general for both crown/council and command is a parent design decision, not an automatic replacement. |
| `ARX_gavino_piras` naval/coastal alternative | Giovanni Sechi | `rejected_external_mod_owner`: parent ownership scan found the active Kaiserreich Sardinia character `SRD_giovanni_sechi`. The retained low-resolution Commons files are provenance evidence only and must not be processed or wired. |
| `ARX_gavino_piras` Sardinian army lead | Nino Salvatore Villa Santa | `blocked`: Cagliari-born and 1935–38 commander of 19th Infantry Division, but available Generals.dk image is copyright-controlled and the Regio Esercito page only exposes an unlicensed 90×110 thumbnail. |
| `ARX_gavino_piras` Sardinian army lead | Gavino Pizzolato | `blocked`: Sassari-born and 1934–37 artillery-regiment commander, but available portraits carry unclear/copyright-controlled reuse terms and no rights-clear original was found. |

Emilio Lussu remains the existing ARX civic source-ready candidate from the
earlier package and was not copied or changed. Luigi Efisio Marras remains
blocked (1950s source) and Gioacchino Solinas remains in the prior
`sardinia_crown_command_retry` package as `needs_user_review`; neither was
duplicated here.

## Source evidence

### Adalberto di Savoia-Genova

- Commons file: <https://commons.wikimedia.org/wiki/File:Adalberto_di_Savoia-Genova.png>
- Direct source: <https://upload.wikimedia.org/wikipedia/commons/c/c5/Adalberto_di_Savoia-Genova.png>
- Catalogue named by Commons: <https://www.limantiqua.com/img/cms/155-_.pdf>
- Author/date: Fotografia Ravagnan; 16 September 1935 onward.
- Local master: `source_masters/sardinia/arx_adalberto_savoia_genova_1935_original.png`
- Dimensions/size: 391×564, 306,177 bytes.
- SHA-256: `fb822de0d5c19d0f72e371fdbebf15a44108e07df7c9c8a21c3156d1605add3b`.
- Role evidence: Treccani identifies the House of Savoy-Genova prince as
  brigadier general in 1934, vice-commander of the Gran Sasso division from
  September 1935, and general of division in 1936:
  <https://www.treccani.it/enciclopedia/savoia-adalberto-di-duca-di-bergamo/>.
- Rights note: Commons provides an Italian simple-photograph PD-Italy claim
  but does not supply publication evidence needed to establish the US
  condition independently. Do not call this source-ready without that review.
- Ownership note: the parent exact/variant scan found no Adalberto owner in
  current Chaos Redux, vanilla, Kaiserreich `1521695605`, or approved mods
  `2265420196` and `1458561226`.

### Giovanni Sechi

- Commons file: <https://commons.wikimedia.org/wiki/File:Giovanni_Sechi.jpg>
- Direct source: <https://upload.wikimedia.org/wikipedia/commons/d/de/Giovanni_Sechi.jpg>
- Credited source page: <http://www.ordinidinasticisavoia-sardegna.net/?cat=3&p=16>
- Date/author: beginning of the 20th century; author not supplied.
- Local master: `source_masters/sardinia/arx_giovanni_sechi_original.jpg`
- Dimensions/size: 250×207, 20,417 bytes.
- SHA-256: `063de6d462dda2524479b40e3ee31ad697aac3a653b67fbff28032b2161cc5ec`.
- Role evidence: Commons identifies birth in Sassari and admiral/Navy-minister
  status; Treccani records the Regia Marina and 1919–21 ministry career:
  <https://www.treccani.it/enciclopedia/giovanni-sechi/>.
- Rights/framing note: Commons uses `PD-anon-70-EU`; no US PD-1996 statement
  is supplied. The image is low-resolution and landscape. An untouched Commons
  extracted derivative (167×202, SHA-256
  `329fbec43bf0c34c210653f70f0aa35da60bc15a3884ef1dfebdba1d953a0573`) is
  retained only as provenance evidence, not as a processed game asset.
- Ownership rejection: active Kaiserreich Sardinia character
  `SRD_giovanni_sechi`; disposition `rejected_external_mod_owner`.

## Ownership gate and parent actions

The parent completed exact/variant scans across current Chaos Redux, vanilla,
Kaiserreich workshop mod `1521695605`, and approved workshop mods
`2265420196` and `1458561226`. Adalberto has no active owner match. Giovanni
Sechi matches active Kaiserreich Sardinia character `SRD_giovanni_sechi` and is
rejected. The full terms, roots, collision exclusions, and candidate log are in
the package [ownership evidence](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/search_notes/ownership_and_candidate_log.md).

If the parent accepts Adalberto after separate rights and visual review, use
only the exact unchanged master listed in the manifest and then run the
repository’s approved portrait pipeline. Sechi must not be processed or wired.
The package [GFX handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_sardinia_rights_clear_retry/gfx_handoff.md)
records every DDS, sprite, `.gfx`, and runtime path as deferred; no final path
or sprite snippet is supplied before approval.

## Simplifications, blockers, and non-claims

- No source-ready ARX command or crown portrait is claimed in this retry.
- Adalberto remains `needs_user_review`; its owner scan is clear, but its US
  rights evidence and visual approval are unresolved.
- Sechi is `rejected_external_mod_owner`, not an alternative awaiting review.
- Villa Santa and Pizzolato are blocked by rights/bitstream uncertainty; no
  copyrighted site image was copied.
- No generated, generic, modern, female, fictional, or invented identity was
  used. No fallback was introduced.
