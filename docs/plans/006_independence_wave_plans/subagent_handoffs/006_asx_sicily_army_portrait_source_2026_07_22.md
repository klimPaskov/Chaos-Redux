# IW-019 ASX Sicily army portrait source handoff

Date: 2026-07-22  
Owner: sourced visual-asset subagent  
Package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/asx_grounded_command_retry_02/`

## Decision

The exact active-1936 Sicilian army-officer search did not produce a releasable
replacement that clears identity, role, licence, and ownership simultaneously.
Francesco Zingales and Ruggero Santini are the strongest uniformed, role-valid
sources but are active vanilla characters. Vito Scimeca, Rodolfo Corselli,
Enrico Maltese, Salvatore Pagano, and Francesco La Ferla are historically
plausible additional leads; their available photographs have unclear reuse
rights or no releasable bitstream (Maltese also has a weak “at disposal” 1936
role fit). No ambiguous-rights image was promoted.

Per parent decision, Vincenzo Di Benedetto is the selected identity for a
deliberate emergency-role adaptation. He was born in Enna, Sicily (1866), had a
substantial army career, was alive in 1936, and has a face-visible Senate source
whose Commons record gives PD Italy and PD-1996/US status. His career record
places him unemployed/at disposal in the 1930s; therefore the package must say
“retired Sicilian general recalled for the synchronized independence emergency,”
not claim a historical 1936 field command. The portrait remains his civilian
suit-and-tie appearance; no uniform or insignia may be invented.

## Source evidence

- Unchanged master: `source_masters/ASX_vincenzo_di_benedetto_senate_pd.gif`
- SHA-256: `EC033B2FCD0DC44441A57C93B12B8C9D64828CF72BD3DD2AD646D40480169553`
- Dimensions: `314x401`, grayscale GIF, 125,570 bytes
- Source page: https://commons.wikimedia.org/wiki/File:Senatore_Vincenzo_Di_Benedetto.gif
- Direct source: https://upload.wikimedia.org/wikipedia/commons/3/32/Senatore_Vincenzo_Di_Benedetto.gif
- Provenance: Senate of the Republic of Italy portrait; author unknown; date
  before 1942; Commons metadata records PD Italy (20 years after creation),
  PD-1996/US, and Italian Senate image collection.
- Proposed source crop: face-visible head-and-shoulders crop at the full leader
  ratio (`156:210 = 0.742857`), with suit lapels and tie retained. The exact
  crop and any derived PNG belong to the separate refinish package.

## Ownership evidence

Exact and variant `Di Benedetto`/`Vincenzo Di Benedetto` searches found no active
owner in current Chaos Redux `common/characters`, country-history recruitment,
leader/commander portrait roots, interface/GFX, or localisation, and no exact
owner in installed vanilla character/history/interface/localisation roots.
This is a scoped ownership check, not a claim that no unrelated reference mod
mentions the historical person.

## Parent handoff

The source package contains `manifest.md`, `gfx_handoff.md`,
`source_hashes.sha256`, three retained comparison masters, and a contact sheet.
The next package is
`docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_di_benedetto_trial_01/`.
Because this subagent is restricted to sourced visual work, it supplies the
unchanged source and crop evidence only; any identity-preserving painted finish
must be handled by an allowed generated-art workflow and independently audited.
No runtime DDS, `.gfx`, gameplay, character, history, or localisation edit was
made.

## Remaining risks

- Di Benedetto is a role adaptation and a civilian visual, not an active
  1936-command photograph; parent localisation and character history must keep
  that distinction explicit.
- The source is legally usable under the Commons record, but the author is
  unknown; retain the Senate/Commons attribution and source URL.
- The final portrait must remain male, full-size `156x210`, and source-anchored;
  no advisor, dossier, `_small`, generic, generated identity, or invented
  military detail is authorized.
