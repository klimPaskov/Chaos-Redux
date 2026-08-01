# IW-018 ARX portrait eligibility and crop review

This is a research-only eligibility record. No row is runtime-approved, no crop was created in this package, and no person may be relabelled to the existing `Vittorio Pala` or `Gavino Piras` tokens without an explicit parent design decision.

## Source-mode gate

ARX is a grounded Sardinian/regional polity. The source mode is therefore `grounded_source_only` for all three one-person consumers. The two authored names `Vittorio Pala` and `Gavino Piras` have no attributable historical identity evidence in the checked archival, Commons, Wikidata, and historical-reference searches. They are blocked as names, not invitations to generate or substitute a face.

## Eligibility table

| Candidate | Role | Identity and era | Source / rights | Crop feasibility | Eligibility |
|---|---|---|---|---|---|
| Emilio Lussu | Civilian/labor | Sardinian-born, alive and politically active in 1936. | 180x253 Senate source, CC BY 3.0 IT, photographer unknown, date only before 1958. | Clean full-frame crop is feasible; prior exact crop evidence exists. | `source_ready_for_parent_review`. |
| Luigi Arborio Mella di Sant'Elia | Crown consultative | Sardinian-born Sassari court official and royal confidant, alive in 1936. | 153x193 Senate source, CC BY 3.0 IT, photographer unknown, before 26 June 1955. | Clean full-frame crop is feasible but small. | `needs_user_review`; candidate is not Vittorio Pala and cannot be silently relabelled. |
| Prince Eugenio di Savoia-Genova | Crown consultative | Savoy-Genova dynastic figure, active naval officer in the 1936 entry, not Sardinian-born. | Commons PD-Italy only; US publication/registration condition unresolved. | Clear face and upper torso; crop feasible after rights review. | `blocked_needs_rights_review`. |
| Prince Adalberto di Savoia-Genova | Crown consultative | Savoy-Genova prince and active general in 1935-1936, not Sardinian-born. | Commons PD-Italy only; US condition unresolved. | Side-profile source can be cropped, but visual approval is separate. | `blocked_needs_rights_review`. |
| Gioacchino Solinas | Mountain guard | Born Bonorva, Sassari province; Sardinian-born general, alive and active in 1936. | 181x278 anonymous 1943 photograph, PD-Italy only. | Head-and-shoulders crop is feasible; prior photo finish was rejected as not HOI4-painted. | `needs_user_review`; candidate is not Gavino Piras. |
| Vittorio Vernè | Mountain guard | 1936 divisional command fit; born Rome, not Sardinian-born. | 200x250 anonymous 1930s photograph, PD-Italy plus PD-1996. | Crop feasible; low resolution. | `blocked_strict_sardinian_birth_requirement` unless parent accepts a Sardinia-linked commander. |
| Giuseppe Valle | Mountain guard | Born Sassari and active as Aeronautica Chief of Staff in 1936. | 417x488 1936 encyclopedia portrait, PD-Italy plus PD-1996. | Excellent front-facing crop. | `blocked_owner_collision` because Kaiserreich owns the person. |
| Giuseppe Pizzorno | Mountain guard | Born Cagliari, commanded Brigata Sassari, alive in 1936. | 145x160 L'Unione Sarda thumbnail, PD-Italy plus PD-1996. | Full-frame crop exists but the side-profile source is too small for identity preservation. | `blocked_source_quality`. |
| Giovanni Sechi | Mountain guard/coastal | Born Sassari, but naval elder rather than mountain commander. | 250x207 anonymous early-20th-century source, PD-anon-70-EU. | No clean 156x210 crop. | `blocked_owner_collision`. |
| Vittorio Pala | Crown consultative | No verified historical identity or era role. | No attributable source or rights evidence. | Not applicable. | `blocked_name_only`. |
| Gavino Piras | Mountain guard | No verified historical identity or era role. | No attributable source or rights evidence. | Not applicable. | `blocked_name_only`. |

## Crop and downstream gate

The repository requires an unchanged attributed master, an exact decoded-pixel crop produced with `extract_portrait_source_crop.py`, a source-locked identity-preserving repaint, a deterministic 156x210 finish, and an independent likeness/style/provenance audit before DDS or runtime wiring.

The existing Lussu and Mella crops in the 2026-07-29 v15 package are exact-frame evidence, but this package intentionally does not duplicate or promote them. The existing Solinas trial crop was produced by a retired processor and is not exact-crop utility evidence; downstream work must make a new exact crop.

Commons also hosts [`Portrait of Luigi Arborio Mella.png`](https://commons.wikimedia.org/wiki/File:Portrait_of_Luigi_Arborio_Mella.png), a 343x612 public-domain photographic reproduction of a two-dimensional artwork sourced to the Kazakh consulate. It is useful role/context corroboration but is not an unchanged archival photograph, so it cannot replace the Senate photograph as the grounded identity master.

No candidate here has a processed PNG or DDS output. A source-ready row means only that the source identity, visible crop, and rights evidence are sufficient to ask the parent for the next gated step.

## Search negative evidence

Commons title search for `Vittorio Pala` returned zero exact-title hits, and Wikidata exact-name search returned zero entities. Commons title search for `Gavino Piras` returned no attributable 1936 portrait; the three broad hits were modern funerals or unrelated heraldic material. Wikidata exact-name search returned zero entities for `Gavino Piras`.
