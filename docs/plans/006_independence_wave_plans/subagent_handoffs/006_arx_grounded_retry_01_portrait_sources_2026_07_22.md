# Event 006 ARX grounded portrait-source retry 01 handoff

Date: 2026-07-22  
Owner: sourced visual-asset subagent  
Scope: source research and mechanical crop previews for the two unresolved
real-person ARX portrait roles. No gameplay, localisation, GFX, runtime DDS,
or existing asset package was edited.

## Deliverables

- [Retry README](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/README.md)
- [Manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/manifest.md)
- [Source hash inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/source_hashes.sha256)
- [Unchanged source masters](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/source_masters/sardinia/)
- [Mechanical crop previews](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/crop_previews/sardinia/)
- [Candidate contact sheet](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/contact_sheet_arx_grounded_retry_01.png)
- [Documentation-only GFX handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/gfx_handoff.md)
- [Ownership/candidate log](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/arx_grounded_retry_01/search_notes/ownership_and_candidate_log.md)

## Result

| ARX role | Candidate | Disposition |
|---|---|---|
| `ARX_sardinian_crown_consultative_council` | Prince Eugenio di Savoia-Genova, Duke of Ancona / fifth Duke of Genoa | `needs_user_review`: period 1936 Treccani entry confirms an active House of Savoy-Genova naval officer; Commons 1920s original is face-usable. Commons `PD-Italy` leaves US publication/URAA evidence unresolved, so this is not source-ready. No active owner found in current Chaos Redux or vanilla. |
| `ARX_gavino_piras` | Taddeo Orlando | `needs_user_review`: active in Tripolitania as artillery commander in 1936 and later commander of the 21st `Granatieri di Sardegna`. Main 173x234 image is a Generals.dk-derived `Regio Esercito` portrait with unclear creation/publication and US status; 1942 Slovenia field photo is a degraded alternate only. Parent must decide whether a non-Sardinian-born Italian officer satisfies the ARX command role. |
| `ARX_gavino_piras` blocked leads | Ubaldo Soddu; Carlo Geloso; Carlo Sanna; Luigi Efisio Marras; Villa Santa; Pizzolato; Solinas | `blocked` or existing-review dispositions are recorded in the manifest/log. Ubaldo and Geloso are vanilla-owned active identities; Carlo Sanna died in 1928; Marras is an existing wrong-era retry; Villa Santa/Pizzolato have no defensible bitstream; Solinas remains in the prior package. |

## Handoff actions for parent

1. Treat both package candidates as review-only. Do not wire a fictional
   identity to a real person or overwrite existing ARX `.gfx` paths from this
   handoff alone.
2. For Eugenio, resolve the Commons US publication/URAA question and confirm
   that a Savoy-Genova duke is acceptable for the crown consultative role.
3. For Taddeo, resolve both rights and role fit. If the parent requires a
   Sardinian-born commander, keep `ARX_gavino_piras` blocked and pursue a new
   rights-clear source rather than using a generic or generated face.
4. If either candidate is approved, run the repository-native grounded portrait
   processing pipeline against the unchanged master. The 156x210 previews are
   only mechanical crop comparisons; they are not final style output or DDS
   inputs.

## Source integrity and checks

- All source masters are unchanged downloads from the direct URLs recorded in
  `manifest.md`.
- All previews are mechanical crops/resizes only; no ImageGen, denoising,
  recolouring, painterly repaint, or identity synthesis was used.
- SHA-256 values and dimensions are recorded in `source_hashes.sha256` and the
  manifest.
- The final contact sheet is 660x300 with SHA-256
  `d09e17b92ebccd76b45308e72416f6ee36cfccfab216fbbc8bfc2869bf9299f6`.
- No final DDS, `.gfx` change, gameplay edit, localisation, advisor sprite,
  small portrait, or fallback was produced.

## Commit

The parent should record the exact commit containing only this new package and
this handoff after review. Any concurrent worktree changes outside these paths
belong to other agents and must not be staged with this handoff.
