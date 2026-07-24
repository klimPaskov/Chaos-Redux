# Event 006 AFX Wallonia commander source retry handoff

Date: 2026-07-24  
Owner: `/root/event6_wallonia_commander_source`  
Scope: bounded sourced-portrait research for the AFX Wallonia reserve/industrial commander. No gameplay, interface, GFX, localisation, PNG/DDS processing, or runtime edits were made.

## Deliverables

- [Source manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/manifest.md)
- [Metadata](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/metadata.json)
- [Ownership scan](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/ownership_scan.md)
- [GFX handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/gfx_handoff.md)
- [Processing handoff](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/processing_handoff.md)
- [SHA-256 inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/source_hashes.sha256)
- Unchanged [archival master](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/henri_denis_revue02_master.jpg)
- Direct [head-and-shoulders crop](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/henri_denis_revue02_head_shoulders_crop.png)

## Outcome

| Role | Candidate | Result | Evidence / next decision |
|---|---|---|---|
| IW-006 AFX Wallonia reserve/industrial commander | Henri Denis | `blocked_current_owner` | Strong Wallonia linkage and role fit. Anonymous May 1940 public-domain original acquired at 1740 x 2480; direct crop is 780 x 1060. Approved Kaiserreich 1521695605 actively owns `BEL_henri_denis`, recruits it, marks it Walloon, and binds `GFX_portrait_BEL_henri_denis_army_small` to `gfx/interface/advisors/BEL/BEL_henri_denis.png`. No guarded transfer contract was supplied. |

The source master SHA-256 is `69BE092EC989B5640B66D9B787310FE27141864A5E50E37FC0F8B545B07C6AE3`. The crop SHA-256 is `50F6D976C74012B75F7F7DA15A99A0CB36F19446FD2D968022251B64EC254E76` and uses source rectangle `left=960, top=260, right=1740, bottom=1320`.

The current Event 006 stable consumer remains `AFX_walloon_reserve_commander`, with `GFX_portrait_AFX_walloon_reserve_commander` targeting `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`. This handoff does not create that DDS or modify the declaration.

## Parent action

Keep the AFX commander source surface blocked. Do not wire Henri Denis or clone his identity while the approved-reference owner is live. If a guarded transfer is explicitly approved, preserve the source/crop evidence and require the origin-owner invalidation, role caveat, and independent portrait audit before runtime wiring.

Jules Pire, Jules Bastin, and Jean-Baptiste Piron were considered as alternate Walloon/Belgian military identities but are already vanilla-owned or lacked a defensible clean source in the earlier retry evidence. Léon Degrelle was excluded by the parent constraint and is not an acceptable substitute for this role.

## Simplifications, omissions, and blockers

No fallback, invented real-person likeness, generated substitute, postwar-only proxy, DDS, GFX edit, gameplay edit, or localisation edit was used. The only blocker is the active approved-reference Henri Denis owner collision; source rights and crop evidence are preserved for a future transfer decision.
