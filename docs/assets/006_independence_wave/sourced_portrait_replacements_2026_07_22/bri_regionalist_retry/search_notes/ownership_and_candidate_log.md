# BRI regionalist source retry - search, role, and ownership log

Date: 2026-07-22  
Scope: Event 006 BRI civic-delegate portrait only. This is a source-research
log; it does not authorize portrait processing, `.gfx` edits, or gameplay edits.

## Role gate

The requested character is the existing `BRI_independence_wave_civic_delegate`.
The traditional regionalist compact and protected-ports patron branches both
promote the token as an oligarchic civic leader. A valid replacement therefore
needs to be a grounded male Breton/regionalist civic figure alive at the 1936
start, not a generic Breton face, a female identity, an advisor, or a labor/
socialist figure.

Régis-Marie-Joseph de l'Estourbeillon de La Garnache (1858-1946) clears this
role gate. The evidence chain is:

- [BnF authority record](https://catalogue.bnf.fr/ark:/12148/cb12157019r):
  identifies him as publiciste, historian, and politician; born in Nantes in
  1858 and deceased in Avessac in 1946; deputy of Morbihan in 1898-1919 and a
  founder/member of the Union regionaliste bretonne.
- [Assemblee nationale Sycomore record](https://www2.assemblee-nationale.fr/sycomore/fiche/%28num_dept%29/4166/%28legislature%29/33):
  confirms the 1898-1919 Morbihan deputy terms, his lifelong Breton regional
  attachment, and his direction of regional publications.
- [CRBC/PRELIB record](https://crbc.huma-num.fr/prelib/personne/450/):
  records him as president of the Union regionaliste bretonne from 1902 to
  1942, with earlier delegation and vice-presidential roles.
- [Union regionaliste bretonne overview](https://fr.wikipedia.org/wiki/Union_r%C3%A9gionaliste_bretonne):
  supplies the historical context that the URB was founded in 1898 as a
  conservative Breton regionalist organization. This secondary source is used
  only to characterize the route fit; the identity and office dates rely on the
  institutional records above.

He was alive on 1936-01-01 (age 77). His retained sources are earlier than the
scenario date: the Wickens photograph is from 1904 (approximately age 46) and
the Dulac illustration is from 1898 (approximately age 40). The age difference
must be recorded in the parent's visual approval; it does not justify inventing
or substituting another face.

## Bounded ownership scan

The scan was run on 2026-07-22 against the active runtime roots in both the
Chaos Redux project and the vanilla installation:

- current project: `common/characters`, `common/country_leader`,
  `history/countries`, `gfx/leaders`, `interface`, and `localisation`;
- vanilla: the corresponding `common/characters`, `common/country_leader`,
  `history/countries`, `gfx/leaders`, `interface`, and `localisation` roots.

Exact and variant terms searched case-insensitively in the runtime file types
(`*.txt`, `*.yml`, `*.gfx`, `*.gui`, `*.asset`, `*.dds`, `*.tga`) were:

```text
Regis de l'Estourbeillon
Régis de l'Estourbeillon
L'Estourbeillon
Estourbeillon
L_Estourbeillon
Regis_Marie_Joseph
Hoel Broerec
Hoël Broërec
Hoel_Broerec
```

No active character, country leader, commander, operative, officeholder, or
portrait owner was found for Régis de l'Estourbeillon or these spelling
variants. Documentation-only references were excluded from the ownership
result. The current `Tangi Kerbrat` localisation is a fictional placeholder
for the same BRI token, not an owner of the sourced identity. No vanilla
portrait or leader sprite may be reused by guessing at a name collision.

## Candidate and provenance log

### 1. John Wickens photograph (retained, `source_ready`)

- Commons page: [File:Estourbeillon.jpg](https://commons.wikimedia.org/wiki/File:Estourbeillon.jpg)
- Direct original: `https://upload.wikimedia.org/wikipedia/commons/b/b5/Estourbeillon.jpg`
- Description: Marquis de Estourbeillon in Breton national costume at the
  Pan-Celtic Congress.
- Source credit: John Wickens, *A Book of Mad Celts*, 1904.
- Photographer provenance: [Storiel John Wickens record](https://www.storiel.cymru/whats-on/john-wickens/)
  records his 1904 Celtic Congress photography in Caernarfon; the [National
  Portrait Gallery record](https://www.npg.org.uk/collections/search/person/mp105135/john-wickens)
  identifies John Wickens (1864-1936) as a photographer.
- Master path: `source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`.
- Dimensions/size: `1145x1707`, 487,769 bytes, JPEG.
- API SHA-1: `22eb568fb74b75331a4304bdbb77f12053586fd5`.
- Local SHA-1 matched the API value; local SHA-256 is
  `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`.
- Rights: Commons labels it Public domain/PD. Wickens died in 1936, so the
  UK life-plus-70 term ended in 2006. The 1904 publication is far outside the
  US publication term; any possible URAA restoration would have ended by 2000.
  The Commons page's missing structured-data copyright status is noted, and
  attribution, source title, author, and dates are preserved as provenance.
- Visual disposition: unchanged full-body photograph, face visible and upper
  torso crop-capable. Early halftone texture and 1904-to-1936 age gap remain
  parent review risks. No crop or repaint has been made.

### 2. Maurice Dulac illustration (retained, `needs_user_review`)

- Commons page: [File:Estourbeillon, Regis.jpg](https://commons.wikimedia.org/wiki/File:Estourbeillon,_Regis.jpg)
- Direct original: `https://upload.wikimedia.org/wikipedia/commons/7/7b/Estourbeillon%2C_Regis.jpg`
- Description: `La Nouvelle Chambre: De l'Estourbeillon`, *Le Monde moderne*,
  December 1898.
- Artist/source context: Maurice Dulac, French illustrator; the periodical's
  publication context is corroborated by [OpenEdition](https://books.openedition.org/enseditions/33590?lang=en)
  and [the magazine history page](https://fr.wikipedia.org/wiki/Le_Monde_moderne).
- Master path: `source_masters/BRI/BRI_regis_de_l_estourbeillon_maurice_dulac_1898.jpg`.
- Dimensions/size: `389x469`, 42,959 bytes, JPEG.
- API SHA-1: `dd546711317223bdf29b2ad2e5acdd4f72f77519`.
- Local SHA-1 matched the API value; local SHA-256 is
  `AC0F77BB97F159264F7FE2E09B9A0EDE2A40B1BAB209FE6DE55CF3A8914A2317`.
- Rights: Commons labels the file Public domain/PD-Art. The 1898 publication
  predates the US 1929 cutoff, but the complete source-country/URAA chain and
  the artist's life dates were not independently established. The page also
  notes missing structured copyright status.
- Visual disposition: archival black-and-white line illustration, not a
  photograph. The event-assets skill permits archival illustrations, but the
  parent brief requires explicit review before this can replace a grounded
  leader portrait. No crop, repaint, PNG, DDS, or GFX output exists.

## Acquisition and integrity notes

The two named Commons originals were downloaded through the Commons
`Special:FilePath` endpoint with a descriptive user-agent after a direct upload
host request returned HTTP 429. The local SHA-1 values match the Wikimedia API
metadata, and the source JPEGs were preserved byte-for-byte. The contact sheet
`contact_sheets/bri_regionalist_source_candidates_review.png` is a review-only
comparison made from those unchanged masters; it is not a runtime asset.

No ImageGen call, generated portrait, generic fallback, portrait processor,
PNG output, DDS conversion, or `.gfx` edit was performed in this source-only
retry.

## Decision

Retain the Wickens 1904 photograph as the only `source_ready` candidate for
parent crop/finish review. Retain the Dulac 1898 illustration solely as a
review-gated archival alternative. If the parent rejects both after visual and
rights review, the BRI civic slot remains blocked; no fallback is authorized by
this package.
