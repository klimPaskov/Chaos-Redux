# Event 006 - BRI regionalist portrait source retry

Date: 2026-07-22  
Producer: `/root/event6_bri_regionalist_source`  
Mode: sourced real-person portrait research (unchanged source masters only)  
Status: primary `source_ready`; secondary `needs_user_review`

This package supplies a grounded male Breton regionalist for the existing BRI
civic-delegate leader token. It does not edit gameplay, localisation, `.gfx`,
or the parent portrait processor. No generated, generic, female, advisor, or
operative asset is used. Processed PNG and runtime DDS output are intentionally
absent because final crop, native HOI4 finishing, visual approval, conversion,
and wiring belong to the parent agent.

## Requested role and runtime mapping

The current token is `BRI_independence_wave_civic_delegate`. The traditional
regionalist compact and protected-ports patron routes both promote it as an
oligarchic civic leader. The existing sprite name is
`GFX_portrait_BRI_independence_wave_civic_commission`, defined in
`interface/006_independence_wave_brittany_portraits.gfx`, with deferred runtime
path `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`.

Régis de l'Estourbeillon is a direct role fit: he founded the Union
régionaliste bretonne, served as its president from 1902 to 1942, and was a
Morbihan deputy from 1898 to 1919. He was a conservative/regionalist civic
figure, male, alive on 1936-01-01, and is not an advisor or operative identity.

## Candidate ledger

### Primary - Régis de l'Estourbeillon, John Wickens photograph, 1904

Status: `source_ready` (parent visual review and processing still required).

- Full identity: Régis-Marie-Joseph de l'Estourbeillon de La Garnache, usually
  Régis de l'Estourbeillon; born 1858-02-10 in Nantes, died 1946-09-04 in
  Avessac. He was alive at the 1936 scenario start and was male.
- Role evidence: [BnF authority record](https://catalogue.bnf.fr/ark:/12148/cb12157019r),
  [Assemblée nationale Sycomore biography](https://www2.assemblee-nationale.fr/sycomore/fiche/%28num_dept%29/4166/%28legislature%29/33),
  and [CRBC/PRELIB role record](https://crbc.huma-num.fr/prelib/personne/450/).
  The CRBC record gives Union régionaliste bretonne president, 1902-1942;
  the Assemblée record gives the Morbihan deputy terms and regionalist work.
- Source page: [Commons File:Estourbeillon.jpg](https://commons.wikimedia.org/wiki/File:Estourbeillon.jpg).
  Direct original: [upload.wikimedia.org/.../Estourbeillon.jpg](https://upload.wikimedia.org/wikipedia/commons/b/b5/Estourbeillon.jpg).
- Original provenance: John Wickens, *A Book of Mad Celts*, 1904; the image
  depicts the Marquis de Estourbeillon in Breton national costume at the
  Pan-Celtic Congress. Wickens's photographer identity and the 1904 Congress
  context are corroborated by [Storiel's John Wickens record](https://www.storiel.cymru/whats-on/john-wickens/)
  and the [National Portrait Gallery authority entry](https://www.npg.org.uk/collections/search/person/mp105135/john-wickens).
- Source master: `source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`.
  Dimensions `1145x1707`, MIME `image/jpeg`, 487,769 bytes. Source SHA-1
  `22eb568fb74b75331a4304bdbb77f12053586fd5`; local SHA-256 is recorded in
  `source_hashes.sha256`.
- Rights basis: Commons records `Public domain`/`PD`. Wickens is documented as
  1864-1936; UK life-plus-70 expired at the end of 2006. The photograph was
  published in 1904, so no US publication term remains in 2026; any possible
  URAA restoration would have expired by 2000. The Commons page notes missing
  structured copyright status, so attribution and the independent provenance
  chain are retained rather than treating the tag as the sole evidence.
- Visual fit: an unchanged full-body period photograph with a visible face and
  crop-capable upper torso. It has noticeable early-photo/halftone texture and
  dates from 1904 (subject approximately 46, compared with approximately 77 in
  1936). The age and texture difference are review risks, not an invented-face
  substitution. Parent must make the explicit head-and-shoulders crop and
  identity-preserving native HOI4 leader finish before acceptance.
- Ownership: the bounded current-project and vanilla scan found no active
  character, portrait, leader, commander, operative, or officeholder owner for
  this identity or the searched spelling variants (see ownership log).
- Processed PNG: `not_created_by_parent_scope`.
- Final DDS: `not_created_by_parent_scope`.

### Secondary - Régis de l'Estourbeillon, Maurice Dulac illustration, 1898

Status: `needs_user_review`; never wire without an explicit decision to accept
an archival illustration as the real-person portrait source.

- Source page: [Commons File:Estourbeillon, Regis.jpg](https://commons.wikimedia.org/wiki/File:Estourbeillon,_Regis.jpg).
  Direct original: [upload.wikimedia.org/.../Estourbeillon,_Regis.jpg](https://upload.wikimedia.org/wikipedia/commons/7/7b/Estourbeillon%2C_Regis.jpg).
- Original provenance: Maurice Dulac, *Le Monde moderne*, December 1898,
  series captioned “La Nouvelle Chambre: De l'Estourbeillon.” The periodical
  context is corroborated by [OpenEdition's *Le Monde moderne* record](https://books.openedition.org/enseditions/33590?lang=en)
  and the [magazine history record](https://fr.wikipedia.org/wiki/Le_Monde_moderne).
- Source master: `source_masters/BRI/BRI_regis_de_l_estourbeillon_maurice_dulac_1898.jpg`.
  Dimensions `389x469`, MIME `image/jpeg`, 42,959 bytes. Source SHA-1
  `dd546711317223bdf29b2ad2e5acdd4f72f77519`; local SHA-256 is recorded in
  `source_hashes.sha256`.
- Rights basis: Commons records `Public domain`/`PD-Art` for the 1898
  publication. Publication predates the US 1929 cutoff, so no current US term
  remains; a complete URAA/source-country chain was not independently
  established. The artist's birth/death dates are unavailable in the retained
  authority evidence, and the Commons page also notes missing structured
  copyright status. Keep this candidate review-gated.
- Format caveat: this is a black-and-white line illustration, not a photograph.
  The event-assets skill permits archival illustrations as a source class, but
  the parent brief's grounded portrait gate still requires explicit review
  before it can replace the live leader token. No crop, repaint, PNG, or DDS was
  made.
- Ownership: no active owner was found in the bounded scan.
- Processed PNG: `not_created_by_parent_scope`.
- Final DDS: `not_created_by_parent_scope`.

## Source and review files

- Unchanged masters: `source_masters/BRI/`.
- Candidate comparison sheet (review evidence only):
  `contact_sheets/bri_regionalist_source_candidates_review.png`.
- SHA-256 ledger: `source_hashes.sha256`.
- Search, role, ownership, and rights notes:
  `search_notes/ownership_and_candidate_log.md`.
- Parent wiring notes: `gfx_handoff.md`.

## Non-wiring and unresolved items

No fallback identity is supplied. Do not wire the 1898 illustration, use a
generated/generic/female/advisor portrait, or point a live sprite at either
JPEG. The primary 1904 photograph is the only source-ready candidate; it still
needs parent-owned crop/finish review because of the source's age gap and
halftone texture. The secondary remains `needs_user_review` because it is an
illustration and its complete territorial rights chain is not documented.
