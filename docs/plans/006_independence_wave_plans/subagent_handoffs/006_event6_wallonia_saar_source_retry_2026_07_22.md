# Event 006 Wallonia/Saar sourced-portrait retry handoff

Date: 2026-07-22  
Owner: `/root/event6_wallonia_saar_source_retry`  
Scope: bounded source research and unchanged archival master acquisition for
the AFX Wallonia and AJX Saar portrait gaps. No gameplay, interface, GFX,
localisation, PNG/DDS processing, or runtime edits were made.

## Deliverables

- [Bounded source manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/manifest.md)
- [Ownership and candidate log](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/search_notes/ownership_and_candidate_log.md)
- [SHA-256 inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/source_hashes.sha256)
- [GFX handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/gfx_handoff.md)
- [AJX commander source comparison sheet](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/contact_sheets/ajx_commander_source_candidates.png)
- Two unchanged original JPEG masters under `source_masters/AJX/`.

## Role outcomes

| Role | Result | Evidence / next decision |
|---|---|---|
| IW-006 AFX Wallonia civic leader | `blocked` | Jules Destrée is already the current live owner of `AFX_walloon_provisional_assembly`; no guarded transfer contract was supplied. Georges Truffaut is role-accurate but the source page says `Droits SOFAM` while the Commons copy claims CC BY-SA 4.0. No independent rights proof. |
| IW-006 AFX Wallonia reserve/industrial commander | `blocked` | Jules Bastin and Jules-Joseph Pire are strong 1936 Walloon/Belgian Army fits, but available image references expose no defensible reuse licence/original. |
| IW-010 AJX Saar civic/municipal leader | `needs_user_review` | Johannes Hoffmann remains the best role identity but his 1941 Brazilian/family-estate image has a URAA/licence conflict. Josef Bürckel has a public-domain NAC lead but is a political commissioner rather than a neutral municipal leader; no local source was acquired. |
| IW-010 AJX industrial/security commander | `source_ready` primary / `needs_user_review` alternate | **Willy Schmelcher**: 1938 archival portrait, exact Saarbrücken Polizeipräsident role, 539x703, SHA-256 `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7`. **Anton Dunckern**: circa-1937 Berlin Document Centre portrait, exact Saarbrücken Gestapo role, 315x405, SHA-256 `109e048050666b1f7029eb32c26e4692aba3a1ee6b484c2eb3c36bd3658f9bd0`; lower-resolution and rights-territory review remain. |

## Parent action

The parent may send only the Schmelcher master through the approved
identity-preserving portrait processing/visual-approval pipeline. Dunckern is
an alternate for human review, not an automatic substitution. The AFX civic,
AFX commander, and AJX civic surfaces remain blocked or review-gated; do not
close them with generated faces, generic stand-ins, postwar-only substitutes,
paid-rights proxies, or re-encoded derivatives.

If Schmelcher is approved, the existing role-key runtime path to review is
`gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`.
This source retry does not create that DDS or edit the existing
`interface/006_independence_wave_region_01_portraits.gfx` declaration.

## Checks performed

- Verified both retained files are non-empty JPEGs at the dimensions and byte
  counts listed in the manifest; hashes are independently recorded in
  `source_hashes.sha256`.
- Inspected the comparison sheet to confirm both subjects are face-visible and
  period-appropriate; the sheet is explicitly review-only.
- Searched exact names and transliterations in current character/history,
  country-leader, interface/GFX, and English localisation roots. Jules Destrée
  was the only live owner hit and was not copied.
- Preserved direct Wikimedia upload bytes; no thumbnail, proxy, screenshot,
  PNG repaint, DDS, or gameplay change was made.

## Simplifications, omissions, and blockers

No source-ready AFX or AJX civic replacement was found. This is an intentional
fail-closed result caused by current-owner collision, unresolved SOFAM/Commons
rights conflict, absent face-visible free sources, and unresolved
Brazilian/family-estate rights. The only accepted source tranche is the AJX
security/industrial commander primary (Schmelcher), with Dunckern retained as a
review-gated alternate.
