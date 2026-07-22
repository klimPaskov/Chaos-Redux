# Event 006 Scotland/Wales grounded portrait source retry

Research date: 2026-07-22. This is a source-and-review package only. The
unchanged source masters were downloaded from the cited archive or institutional
URL (the Saunders Lewis master is a bit-identical copy of the verified download in
the preceding `western_gap_retry` package because Wikimedia returned HTTP 429 on
the second request). The package contains mechanical head-and-shoulders review
crops and a contact sheet. It contains no ImageGen output, painted treatment,
runtime PNG/DDS, `.gfx` edit, advisor art, `_small` portrait, gameplay edit, or
localisation edit.

## Source-mode and review rules

- IW-001 Scotland and IW-002 Wales are grounded historical/regional identities;
  every named person below is therefore sourced rather than generated.
- All subjects are male and alive in 1936. The civic candidates are shown in
  civilian or service dress appropriate to their documented identity. The
  commander candidate is a real British Army officer associated with the 53rd
  (Welsh) Division.
- A crop is a literal rectangular crop of the unchanged master. It has no
  retouching, sharpening, recolouring, denoising, resizing, or painterly pass.
- The crop is a review input for the parent portrait pipeline, not a runtime
  portrait. No candidate here is a claim that a DDS is approved.
- The final runtime consumer requested by the existing ledger is the large
  `156x210` leader/commander portrait only. No advisor or `_small` surface is
  authorized by the Event 6 prompt.

## Role ledger

| Requested role / consumer | Status | Subject and role evidence | Source / provenance / rights | Unchanged master | Mechanical crop | Notes |
|---|---|---|---|---|---|---|
| SCO civic leader / `portrait_SCO_independence_wave_civic_convention.dds` | `source_ready` for parent review | Robert Bontine Cunninghame Graham (1852-1936), Scottish politician, writer, and first president of the Scottish National Party (1934); exact regional civic identity and alive on the 1936 boundary | [Commons file page](https://commons.wikimedia.org/wiki/File%3APhoto_of_R._B._Cunninghame_Graham.jpg); [HathiTrust source scan](https://babel.hathitrust.org/cgi/pt?id=coo1.ark:/13960/t6xw50w29;view=1up;seq=191;size=150). Portrait published no later than 1907, artist/photographer not stated. Commons records `PD-US-expired` / public domain; pre-1931 publication gives the recorded US basis. Territorial public-domain status is an archive/legal review note, not an invented license grant. | `source_masters/SCO/SCO_cunninghame_graham_hathitrust_1907.jpg` — 813x1101, 395,863 bytes, SHA-256 `401cc30d278122a6cc99b691e913a63c568a2ef82e1e0ae0513dc93f303d4fbb` | `review_crops/SCO/SCO_cunninghame_graham_hathitrust_1907_head_shoulders.png` — crop box `(120,120)-(700,900)`, 580x780, SHA-256 `bc30ee3ccf31d8e31656678bf8b703658189e83cb300889e3461bfba9a73b56a` | Cleaner face-visible alternative to the earlier Rijksmuseum album-page source. No transfer or ownership conflict found in the bounded scan below. |
| WLS civic leader / `portrait_WLS_independence_wave_national_council.dds` | `source_ready` for parent review | Saunders Lewis (1893-1985), Welsh nationalist, writer, and Great War veteran; direct Welsh self-government identity and alive in 1936 | [Commons file page](https://commons.wikimedia.org/wiki/File%3ASaunders-lewis-y-drych-1916.jpg); [National Library of Wales newspaper page](https://papuraunewydd.llyfrgell.cymru/view/3776384/3776392/60/). `Y Drych`, 3 February 1916, author not stated. Commons records a Public Domain Mark / pre-1931 publication basis. The master was downloaded unchanged in `western_gap_retry`; the copy here has the same SHA-256. | `source_masters/WLS/WLS_saunders_lewis_ydrych_1916.jpg` — 1016x2239, 1,499,841 bytes, SHA-256 `d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3` | `review_crops/WLS/WLS_saunders_lewis_ydrych_1916_head_shoulders.png` — crop box `(210,200)-(800,994)`, 590x794, SHA-256 `eb0f03982a3d2b6b2c06dd766c21489b447d8488db9f28645c666ca3c1a672aa` | The original page includes a newspaper caption and border. The crop excludes the text and retains the face, uniform collar, and shoulders; it is still only a mechanical review crop. |
| WLS mountain/territorial commander / `portrait_WLS_independence_wave_mountain_commandant.dds` | `needs_user_review` (rights metadata confirmation before runtime) | Robert Knox Ross (1893-1951), Major-General, GOC 53rd (Welsh) Division from September 1942 through 1945; direct formation-command fit, though not Welsh-born | [Erfgoed 's-Hertogenbosch biography](https://www.erfgoedshertogenbosch.nl/verhalen/de-bevrijder-van-s-hertogenbosch-genraal-robert-ross); [collection record](https://www.brabantserfgoed.nl/collectie/object/erfgoed-s-hertogenbosch/f6d5746da8eeae68c39b52ff02bc9f1682fa650b). Collection record reports CC BY-SA 3.0 NL; the biography identifies the subject, uniform, and 53rd Welsh command. The image is treated as c. 1944 from the wartime uniform/context; the exact capture date is not stated. The collection page was cache-missed during this retry, so attribution and the exact record licence must be reconfirmed before DDS release. | `source_masters/WLS/WLS_robert_knox_ross_erfgoed_1944.jpg` — 423x598, 76,232 bytes, SHA-256 `8673a1ddb9763b9d0f38367cc3063db964d5be38c27fc216abd5fb63f570061f` | `review_crops/WLS/WLS_robert_knox_ross_erfgoed_1944_head_shoulders.png` — crop box `(8,5)-(414,550)`, 406x545, SHA-256 `f34c283324c67e8261786db60c02ef198158401fca5b9fd5c7a299fdbe98a1f4` | Strong single-subject fit for the Welsh command surface; source is a low-resolution institutional image. Apply `CC BY-SA 3.0 NL` attribution/share-alike only if the collection record still carries that licence. |
| WLS commander alternate (not selected) | `alternate_source_ready`, not selected | Gerard Corfield Bucknall (1894-1980), GOC 53rd (Welsh) Division 29 July 1941–12 September 1942; exact formation association | [Commons file page](https://commons.wikimedia.org/wiki/File%3ALt_General_Bucknall_1944_IWM_B_5468.jpg); [IWM B 5468 search record](https://www.iwm.org.uk/collections/search?query=B%205468). No. 5 Army Film & Photographic Unit, Sgt Laing, 1944. Commons records UK Government/Crown copyright expiry and public-domain reuse rationale. | `source_masters/WLS/WLS_gerard_bucknall_iwm_1944_alternate.jpg` — 1012x951, 361,691 bytes, SHA-256 `727b7b551b3aae1c6240f6fd8f3ba8141d975153290bfc89914222b82fdef3f1` | `review_crops/WLS/WLS_gerard_bucknall_iwm_1944_alternate_head_shoulders.png` — crop box `(548,30)-(1000,637)`, 452x607, SHA-256 `f8934725d8f9bc28644b6cc03ada92b7916171cf0840e0ee1b6c50cd81c50126` | The original is a two-person walking photograph; the crop isolates Bucknall in profile but is weaker as a portrait than Ross. Retained only as a documented alternative, not a runtime handoff. |
| SCO territorial commander / `portrait_SCO_independence_wave_territorial_commandant.dds` | `blocked` | Best role lead found: Andrew Jameson McCulloch (1876-1960), Edinburgh-born Major-General and GOC 52nd (Lowland) Division in 1934-35 and 1936-38; exact Scottish territorial command. | [WFA biography](https://www.westernfrontassociation.com/generals-biographies/andrew-jameson-mcculloch/); [biographical summary](https://en.wikipedia.org/wiki/Andrew_McCulloch_(British_Army_officer)); [52nd Division research](https://www.britishmilitaryhistory.co.uk/wp-content/uploads/sites/124/2024/11/52-Division-1930-38-V2_1.pdf). The clearest face-visible portrait lead is the National Portrait Gallery record (`NPG x124937` / three portraits), which is licensable but not redistribution-defensible without permission. No original binary with a free/CC/public-domain licence was acquired in this bounded retry. | none | none | Existing alternatives were fail-closed: William Edmund Ironside is already an installed vanilla `ENG_edmund_ironside` character/portrait consumer; Hugh Dowding is installed as `ENG_hugh_dowding`; neither may be cloned. No generated or generic substitute is supplied. |

## Ownership scan

The bounded ownership check searched these roots and surfaces for exact names,
surname variants, title/name-order variants, character ids, portrait consumers,
and localisation references:

- Installed vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- Current project: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`
- Surfaces: `common/characters`, `history/countries`, `gfx/leaders`, `interface`,
  and `localisation`.

Terms included `Cunninghame Graham`, `Cunninghame`, `Saunders Lewis`, `Lewis`,
`Robert Knox Ross`, `Ross`, `Gerard Bucknall`, `Bucknall`, `Andrew Jameson
McCulloch`, `McCulloch`, `Ironside`, and `Dowding`.

Results:

- No installed vanilla or project character/portrait consumer was found for
  Cunninghame Graham, Saunders Lewis, Robert Knox Ross, or Gerard Bucknall.
  The project has intentional Event 6 localisation strings for the two civic
  names, but no corresponding character definition was returned by the scan.
- Vanilla ownership was confirmed for `ENG_hugh_dowding` in
  `common/characters/ENG.txt`, `history/countries/ENG - Britain.txt`, and
  `interface/ideas.gfx`; `ENG_edmund_ironside` is likewise defined and recruited
  in the vanilla England roster. Both are excluded from the Scotland package.
- The McCulloch search returned generic surname-name-pool occurrences and no
  character or portrait consumer; the blocker is source rights, not ownership.

## Canonical visual references inspected

The canonical reference root was used directly:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- `portraits/leaders/contact_sheet.png`
- `portraits/commanders/contact_sheet.png`

The crops in this package intentionally stop before the HOI4 painted treatment;
the parent agent owns identity-preserving processing and DDS conversion after
review.

## Package paths

- Contact sheet: `contact_sheet/sco_wls_grounded_retry_contact_sheet.png`
- Hash list: `source_hashes.sha256`
- Source-search and rights notes: `search_notes/ownership_and_rights.md`
- Proposed sprite/path handoff: sibling `gfx_handoff.md`
