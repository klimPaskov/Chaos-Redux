# IW-018 ARX sourced portrait audit v76

## Evidence reviewed

- The unchanged archival sources and their v15 attribution, rights, date, and role records.
- The exact head-and-shoulders crops and their decoded-pixel equality JSON files.
- The raw ImageGen repaints for Emilio Lussu, Luigi Mella di Sant'Elia, Vittorio Vernè, and Gioacchino Solinas.
- The reproducible 156x210 RGBA candidates for all four consumers.
- The enlarged comparison sheets with vanilla HOI4 leader and commander references.

## Findings

| Gate | Disposition | Evidence |
| --- | --- | --- |
| Historical identity | PASS for source candidates | The source ledger attributes Lussu, Mella, and Vernè; each repaint preserves the source face, pose, and period clothing. Vernè is recorded as Sardinia-linked, never Sardinian-born. |
| Source crop integrity | PASS | The v15 crop JSON records exact decoded-pixel equality against each immutable master. |
| HOI4 painted style | PASS, parent visual review | Restrained gouache/oil planes, subdued period palettes, readable faces, and quiet backgrounds match the vanilla reference families. |
| 156x210 readability | PASS, parent visual review | Native candidates retain identity-defining facial planes and shoulders without text, UI, or modern props. |
| Rights and attribution | PASS for promoted roster | Lussu and Mella carry CC BY 3.0 IT records; Verne carries PD-Italy + PD-1996; attribution is retained in the source ledger, metadata, and ARX package documentation. Solinas remains PD-Italy-only evidence under a rights hold. |
| Runtime promotion | PASS for three consumers | Lussu, Mella, and Verne have byte-matched 156x210 DDS files, corrected `.gfx` sprites, character consumers, and aligned localisation. Solinas has no runtime DDS. Exact Pala/Piras identities remain blocked and are not relabelled. |

Gioacchino Solinas is retained as a Sardinian-born commander evidence candidate, but its 1943 source carries only PD-Italy status and remains `needs_user_review`. The promoted ARX roster uses Lussu, Mella, and Verne; exact Vittorio Pala and Gavino Piras identities remain blocked and are not silently relabelled. IW-018 admission is governed by the post-wire country-package audit and exact content-attestation trigger.
