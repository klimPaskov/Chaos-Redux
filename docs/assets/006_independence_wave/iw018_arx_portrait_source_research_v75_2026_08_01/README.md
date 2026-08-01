# IW-018 ARX grounded Sardinian male portrait source research v75

Research date: 2026-08-01.

Scope: source and provenance research for the three already-authored ARX full-size leader consumers: Emilio Lussu for the civilian/labor route, the current name-only token Vittorio Pala for the crown consultative route, and the current name-only token Gavino Piras for the mountain-guard directorate.

ARX is a grounded historical/regional polity classification, so every one-person portrait must use an attributed real-person source and the source-locked portrait pipeline. Generated faces, generic Sardinian faces, relabelled people, and reuse of an unrelated person are not admissible.

## Executive disposition

| Consumer | Current display name | Best grounded identity evidence | Source disposition | Roster disposition |
|---|---|---|---|---|
| `ARX_sardinian_provisional_assembly` | Emilio Lussu | Emilio Lussu, Sardinian politician, soldier, writer, and Partito Sardo d'Azione/Partito d'Azione figure born in Armungia, Cagliari province, 1890. | Senate headshot, 180x253, CC BY 3.0 IT via `senato.it`, dated only `before 1958`; unchanged master retained here. | `source_ready_for_parent_review`; exact 1936 capture date and downstream likeness/style audit remain open. |
| `ARX_sardinian_crown_consultative_council` | Vittorio Pala | No attributable historical person or archival portrait matching the exact name `Vittorio Pala` was found. Luigi Arborio Mella di Sant'Elia is the strongest role-fit substitute, not the same identity. | Mella Senate portrait, 153x193, CC BY 3.0 IT via `senato.it`, dated before 26 June 1955; unchanged master retained here. | Current `Vittorio Pala` token is `blocked_name_only`; Mella is `needs_user_review` only if the parent explicitly accepts a role/name change. |
| `ARX_gavino_piras` | Gavino Piras | No attributable historical person or archival portrait matching the exact name `Gavino Piras` and a 1936 mountain-command role was found. Gioacchino Solinas is the strongest Sardinian-born command substitute, not the same identity. | Solinas source photograph, 181x278, dated 1943, anonymous, PD-Italy only; unchanged master retained here. | Current `Gavino Piras` token is `blocked_name_only`; Solinas is `needs_user_review` because US rights and the prior photographic finish remain unresolved. |

## Candidate summary

The complete researched candidate set is in [`source_ledger.csv`](source_ledger.csv), including role-fit alternatives that are blocked by rights, ownership, quality, timing, or identity mismatch.

The strongest crown-route source is Mella because he was born in Sassari, served as Grand Master of Court Ceremonies for Vittorio Emanuele III from age twenty-five, was a royal confidant, and was alive in 1936; the source date is late-bounded and the image is small, so it is not runtime-ready.

The strongest Sardinian-born mountain-command source is Solinas because he was born in Bonorva, Sassari province, was a decorated Bersaglieri general, and was alive and professionally active in 1936; his available photograph is from 1943 and carries PD-Italy without an explicit PD-1996 determination.

Vittorio Vernè is a rights-strong command alternative because Commons records PD-Italy plus PD-1996 and Generals.dk records 1936 East African divisional command, but he was born in Rome and is only Sardinia-linked through a formation connection.

Giuseppe Valle is a strong Sardinian-born 1936 aviation/state-command fit with a period `Grande enciclopedia aeronautica 1936` image and PD-Italy plus PD-1996, but the exact person is owned by Kaiserreich as `SRD_giuseppe_valle` with a live character, history recruitment, localisation, and portrait consumers.

Giuseppe Pizzorno is Sardinian-born and commanded the Sassari Brigade, but the only attributed source is a 145x160 side-profile thumbnail with insufficient detail for a defensible identity-preserving repaint.

Savoy-Genova alternatives Eugenio and Adalberto are role-plausible crown figures, but the retained Commons sources are PD-Italy only without independent United States publication/registration evidence; they remain rights-review candidates, not cleared sources.

Giovanni Sechi is Sardinian-born and a senior naval/public figure, but Kaiserreich owns `SRD_giovanni_sechi`; he is rejected by the subject-ownership gate.

No processed PNG, source crop, generated repaint, advisor icon, final DDS, `.gfx` edit, localisation edit, or gameplay edit was made in this research package. The copied files in `source_masters/` are unchanged archival/source binaries retained for evidence only.

No new contact sheet was generated because this package preserves source masters already compared in the cited v15 and earlier ARX evidence packages; the new ledger is a roster/rights/identity audit, not a visual-processing pass.

## Parent decision boundary

Do not wire the current `Vittorio Pala` or `Gavino Piras` names to Mella or Solinas by relabelling the source person. If the parent accepts either substitute, the parent must make the identity/name change in the gameplay package and then route the unchanged source through the exact crop, source-locked repaint, independent likeness/style/provenance audit, deterministic 156x210 processing, DDS conversion, and `.gfx` wiring workflow.

If the design requires the exact existing names, the crown and mountain-guard portraits are blocked and no generated or generic fallback is allowed.
