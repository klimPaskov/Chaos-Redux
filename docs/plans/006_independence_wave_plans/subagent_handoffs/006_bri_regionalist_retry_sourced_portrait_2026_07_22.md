# Event 006 BRI regionalist sourced-portrait retry handoff

Date: 2026-07-22  
Producer: `/root/event6_bri_regionalist_source`  
Scope: bounded real-person source research for the BRI civic-delegate token.
No gameplay, localisation, `.gfx`, portrait processing, PNG, or DDS edits.

## Package

- Source package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/`
- Manifest: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/manifest.md`
- GFX handoff: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/gfx_handoff.md`
- Hash ledger: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_hashes.sha256`
- Search and ownership notes: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/search_notes/ownership_and_candidate_log.md`
- Review contact sheet: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/contact_sheets/bri_regionalist_source_candidates_review.png`

## Result

| Requested token | Result | Candidate |
|---|---|---|
| `BRI_independence_wave_civic_delegate` / `GFX_portrait_BRI_independence_wave_civic_commission` | `source_ready` pending parent crop/finish review | Régis de l'Estourbeillon (1858-1946), male Breton regionalist; John Wickens photograph, 1904 |
| Same token | `needs_user_review`; do not wire without explicit approval | Régis de l'Estourbeillon; Maurice Dulac archival illustration, 1898 |

Régis de l'Estourbeillon is a defensible role match for both the traditional
regionalist compact and protected-ports patron oligarchic branches. Institutional
evidence records his Union régionaliste bretonne presidency from 1902 to 1942,
his Morbihan deputy terms from 1898 to 1919, and his regionalist civic work. He
was alive at the 1936 scenario start and no active current-project or vanilla
identity/portrait owner was found in the bounded scan.

## Source integrity

- `BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`: `1145x1707`,
  487,769 bytes, source SHA-1
  `22eb568fb74b75331a4304bdbb77f12053586fd5`, local SHA-256
  `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`.
- `BRI_regis_de_l_estourbeillon_maurice_dulac_1898.jpg`: `389x469`,
  42,959 bytes, source SHA-1
  `dd546711317223bdf29b2ad2e5acdd4f72f77519`, local SHA-256
  `AC0F77BB97F159264F7FE2E09B9A0EDE2A40B1BAB209FE6DE55CF3A8914A2317`.

Both local SHA-1 values match the Wikimedia API metadata. The JPEG masters are
unchanged. The Wickens photograph carries a public-domain basis supported by
the 1904 publication, photographer death date, and Commons provenance; the
Dulac illustration is Commons PD-Art but remains review-gated because its full
artist/territorial rights chain is not independently complete.

## Parent actions

1. Review the unchanged Wickens master, make the explicit identity-preserving
   head-and-shoulders crop, finish a full `156x210` native leader portrait, and
   compare it with the canonical vanilla leader references.
2. If accepted, convert through the repository-standard DDS pipeline and keep
   the existing `GFX_portrait_BRI_independence_wave_civic_commission` name and
   target path. Do not add a duplicate sprite.
3. Do not process the Dulac illustration unless an explicit user review accepts
   the archival illustration format and its remaining rights uncertainty.
4. If both are rejected, leave the BRI civic slot blocked and run a later
   source retry. No generated or generic fallback is supplied here.

## Residual risks and simplifications

- The primary image predates the scenario by 32 years; subject age is roughly
  46 in 1904 versus 77 in 1936, and the photograph has early halftone texture.
- The secondary candidate is an illustration, not a photograph, and its artist
  life dates/complete territorial rights chain remain unresolved.
- No processed PNG, DDS, `.gfx` edit, or gameplay wiring is included by design;
  these are parent-owned after explicit source acceptance.

There is no silent fallback or generated substitute in this handoff.
