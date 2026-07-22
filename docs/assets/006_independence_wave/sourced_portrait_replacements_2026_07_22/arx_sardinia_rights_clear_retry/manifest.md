# Event 006 ARX Sardinia rights-clear retry manifest

Date: 2026-07-22
Scope: source-only retry for the unresolved ARX Sardinia real-person
portrait roles. This package contains unchanged source masters only. No
cropping, resizing, colour treatment, portrait processing, review sheet,
PNG/DDS conversion, GFX edit, gameplay edit, or localisation edit was made.

The status in this file is a research disposition, not runtime approval. A
`needs_user_review` row must not be wired until a separate rights/visual review
and the parent ownership scan are complete. A `blocked` row has no acceptable
source master in this pass and must not receive a generated or generic face.

## Role ledger

| Role / current fictional consumer | Candidate | Status | Role and era fit | Source-master path | Dimensions | SHA-256 | Rights / uncertainty |
|---|---|---|---|---|---:|---|---|
| `ARX_sardinian_crown_consultative_council` (`Vittorio Pala` replacement) | Prince Adalberto di Savoia-Genova, Duke of Bergamo (1898–1982) | `needs_user_review` | House of Savoy-Genova dynastic figure and Italian general. Treccani records brigadier-general rank in 1934, vice-command of the mobilised Gran Sasso infantry division from September 1935, and division-general rank in 1936. A dynastic/council interpretation is plausible, but parent design must confirm that this branch may use a Savoy-Genova duke rather than the direct royal household. | [source master](source_masters/sardinia/arx_adalberto_savoia_genova_1935_original.png) | 391×564 | `fb822de0d5c19d0f72e371fdbebf15a44108e07df7c9c8a21c3156d1605add3b` | Wikimedia Commons marks the Italian simple photograph public domain under the 20-year term; page does **not** add an explicit US `PD-1996` determination. Treat as rights review required. Source page names photographer Fotografia Ravagnan and gives source catalogue PDF; see URLs below. Side-profile military portrait is face-visible but visual approval remains separate. Parent must check active owner collisions before any reuse. |
| `ARX_gavino_piras` (army/coastal commander replacement) | Prince Adalberto di Savoia-Genova, Duke of Bergamo | `needs_user_review` | The same 1935–36 record makes him an active general and division commander at the scenario date. Reusing this person for both a dynastic council seat and a command office is a design choice for the parent, not an assumption made here. | [same unchanged source master](source_masters/sardinia/arx_adalberto_savoia_genova_1935_original.png) | 391×564 | `fb822de0d5c19d0f72e371fdbebf15a44108e07df7c9c8a21c3156d1605add3b` | Same PD-Italy / US-status uncertainty and parent ownership gate as above. Do not create a second copy or new identity unless the parent accepts this dual-role use. |
| `ARX_gavino_piras` (naval/coastal alternative only) | Giovanni Sechi (1871–1948) | `needs_user_review` | Born in Sassari; Regia Marina admiral, senator, and Kingdom of Italy Navy minister. Treccani records reserve vice-admiral status in 1923, squadron-admiral rank in 1926, and ministry service 1919–21. He was alive in 1936 but already a senior reserve/retired institutional figure; this is a coastal/council alternative, not a strong army-corps match. | [unchanged Commons original](source_masters/sardinia/arx_giovanni_sechi_original.jpg) | 250×207 | `063de6d462dda2524479b40e3ee31ad697aac3a653b67fbff28032b2161cc5ec` | Commons labels the anonymous early-20th-century image `PD-anon-70-EU`; no explicit US `PD-1996` record and no named photographer. The 250×207 source is low-resolution and landscape; no local crop or upscale was made. Parent must decide whether this framing can satisfy the role and must run owner scan. |

The Commons extracted derivative `source_masters/sardinia/arx_giovanni_sechi_cropped_original.jpg` (167×202, SHA-256
`329fbec43bf0c34c210653f70f0aa35da60bc15a3884ef1dfebdba1d953a0573`) is
retained only as an untouched downloaded reference variant. It is not a
processed game asset and is not a recommendation over the full 250×207 source.

## Source records

### Prince Adalberto di Savoia-Genova, Duke of Bergamo

- Commons file page: <https://commons.wikimedia.org/wiki/File:Adalberto_di_Savoia-Genova.png>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/c/c5/Adalberto_di_Savoia-Genova.png>
- Catalogue/source named on Commons: <https://www.limantiqua.com/img/cms/155-_.pdf>
- Commons record: photographic portrait of S.A.R. Adalberto di Savoia-Genova;
  date `16 settembre 1935-`; author `Fotografia Ravagnan`; original PNG
  391×564, 306,177 bytes.
- Commons rights note: `PD-Italy` for a simple photograph after the Italian
  20-year term, with a warning that US status requires a separate `PD-1996`
  determination. This package therefore does not call it source-ready.
- Era/role note: Treccani identifies Adalberto as a House of Savoy-Genova
  prince and records general-of-brigade rank in 1934, vice-command of the
  Gran Sasso infantry division from 20 September 1935, and general-of-division
  rank in 1936. See <https://www.treccani.it/enciclopedia/savoia-adalberto-di-duca-di-bergamo/>.

### Giovanni Sechi

- Commons file page: <https://commons.wikimedia.org/wiki/File:Giovanni_Sechi.jpg>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/d/de/Giovanni_Sechi.jpg>
- Original source credited by Commons: <http://www.ordinidinasticisavoia-sardegna.net/?cat=3&p=16>
- Commons record: `Beginning of the 20. century`; author not supplied; original
  JPEG 250×207, 20,417 bytes. Commons applies `PD-anon-70-EU` and says the
  author is anonymous; no US `PD-1996` determination is supplied.
- Cropped derivative page (not processed by this subagent):
  <https://commons.wikimedia.org/wiki/File:Giovanni_Sechi_(cropped).jpg>.
- Identity/role evidence: Commons category records birth in Sassari on 7
  January 1871 and death in Rome on 1 May 1948, plus admiral, Navy-minister,
  and senator classifications. Treccani confirms the Regia Marina career and
  1919–21 Navy ministry. See <https://www.treccani.it/enciclopedia/giovanni-sechi/>.

## Blocked high-fit command leads (no local bitstream copied)

These candidates were investigated because they fit Sardinian military/coastal
continuity, but their available image paths did not satisfy the rights-clear
source gate. They remain evidence only; no substitute portrait was invented.

| Candidate | Why it fits | Why blocked |
|---|---|---|
| Nino Salvatore Villa Santa (1884–1960) | Born in Cagliari. Generals.dk records command of the 19th Infantry Division `Gavinana` from 1935-09-01 through 1938-06-30, covering 1936. | Generals.dk portrait is credited to `Generali Dell’Impero` / Vinicio Araldi but the site states `Copyright © Steen Ammentorp`; no reuse grant was found. The Regio Esercito page exposes only a 90×110 thumbnail without a usable licence chain. Candidate is blocked pending a rights-clear archival scan. Sources: <https://generals.dk/general/Villa_Santa/Nino_Salvatore/Italy.html>, <https://www.regioesercito.it/pages/et35comand.html>. |
| Gavino Pizzolato (1884–1943) | Born in Sorso, Sassari province. Generals.dk records command of the 1st Celere Artillery Regiment `Eugenio di Savoia` from 1934 to 1937, alive and active in 1936. | The available Generals.dk portrait is credited as courtesy of Franco Tarnassi and the site is copyright-controlled; the Noialpini page image has no reuse grant or source-author statement. No rights-clear original bitstream was copied. Sources: <https://generals.dk/general/Pizzolato/Gavino/Italy.html>, <https://www.noialpini.it/pizzolato-gavino.html>. |
| Luigi Efisio Marras (1888–1991) | Cagliari-born senior Italian general; previously investigated in the earlier ARX package. | Existing source is explicitly a 1950s portrait (255×346) and outside the requested 1936-era evidence; the prior handoff marks it blocked. Not duplicated here. |
| Gioacchino Solinas (1892–1987) | Bonorva-born Sardinian general and strongest existing local command candidate. | Already held in `sardinia_crown_command_retry`; previous photographic trial remains `needs_user_review` and was intentionally not duplicated. Parent must resolve that package independently. |

## Ownership gate

This subagent did not read runtime gameplay files, vanilla files, or other-mod
implementation roots. A non-runtime documentation scan found no existing
`Adalberto`, `Eugenio`, or `Duca di Bergamo` references, but that is not an
ownership clearance. The parent must scan the active vanilla character/history,
current Chaos Redux character/GFX roots, and installed other-mod roots for
exact and variant names before accepting either master. Known Savoy collisions
from the preceding ARX handoff include Aimone, Amedeo, Filiberto, and
Ferdinando variants; do not infer that Adalberto or Sechi are collision-free.

## Parent handoff

1. Keep the ARX crown route fail-closed until the owner scan and separate
   rights/visual review approve Adalberto (or another defensible dynastic
   person). Do not wire the source merely because Commons says `PD-Italy`.
2. For `ARX_gavino_piras`, Adalberto is the only local source master in this
   retry with both a 1935-era bitstream and a documented active general role;
   Sechi is an explicitly weaker naval/council alternative. The parent may
   instead keep the command role blocked and pursue a rights-clear Solinas or
   other Sardinian commander review.
3. Emilio Lussu remains the existing civic candidate and is not changed by
   this package. No portrait was copied for Lussu, Marras, or Solinas.
4. If a separate review accepts a master, process it only through the approved
   native leader-portrait pipeline. This package intentionally has no processed
   PNG, DDS, review sheet, or GFX handoff.

## Simplifications / blockers

- No fully source-ready ARX command or crown replacement is claimed. Adalberto
  and Sechi remain `needs_user_review` because of US-rights, visual-framing,
  and ownership gates.
- Villa Santa and Pizzolato are historically excellent Sardinian command leads
  but are blocked by copyright/unclear reuse and were not copied.
- No generated, generic, modern, female, invented, or fictional replacement was
  introduced.
