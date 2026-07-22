# Event 006 Scotland/Wales grounded source retry handoff

Date: 2026-07-22  
Scope: `IW-001` Scotland and `IW-002` Wales grounded leader/commander source
inputs only. No gameplay, GFX, localisation, spreadsheet, advisor, `_small`,
ImageGen, or DDS files were touched.

## Owned package

`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/sco_wls_grounded_retry_01/`

- `manifest.md` — source provenance, role fit, rights, dates, uncertainty,
  dimensions, hashes, ownership scan, and status.
- `gfx_handoff.md` — proposed parent-owned runtime paths and sprite names.
- `source_masters/SCO/SCO_cunninghame_graham_hathitrust_1907.jpg` — selected
  Scottish civic master, 813x1101, SHA-256
  `401cc30d278122a6cc99b691e913a63c568a2ef82e1e0ae0513dc93f303d4fbb`.
- `source_masters/WLS/WLS_saunders_lewis_ydrych_1916.jpg` — selected Welsh civic
  master, 1016x2239, SHA-256
  `d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3`.
- `source_masters/WLS/WLS_robert_knox_ross_erfgoed_1944.jpg` — selected Welsh
  commander master, 423x598, SHA-256
  `8673a1ddb9763b9d0f38367cc3063db964d5be38c27fc216abd5fb63f570061f`.
- `source_masters/WLS/WLS_gerard_bucknall_iwm_1944_alternate.jpg` — rights-clear
  but visually weaker Welsh commander alternate, 1012x951, SHA-256
  `727b7b551b3aae1c6240f6fd8f3ba8141d975153290bfc89914222b82fdef3f1`.
- `review_crops/` — explicit head-and-shoulders PNG crops only; crop boxes and
  hashes are in the manifest and hash list.
- `contact_sheet/sco_wls_grounded_retry_contact_sheet.png` — source/crop review
  sheet comparing the three selected rows and the Bucknall alternate.
- `source_hashes.sha256` — reproducibility list for all source and review files.
- `search_notes/ownership_and_rights.md` — bounded search and fail-closed notes.

## Role result

| Role | Result | Parent action |
|---|---|---|
| SCO civic convention | `source_ready` | Review Cunninghame Graham crop; if accepted, run the normal identity-preserving HOI4 portrait pass and record the DDS hash. |
| WLS national council | `source_ready` | Review Saunders Lewis crop; retain the newspaper provenance and caption removal note. |
| WLS mountain commandant | `needs_user_review` | Ross is the strongest single-subject source and the role is exact (GOC 53rd Welsh Division), but confirm the collection record's CC BY-SA 3.0 NL licence and attribution before runtime conversion. Bucknall is a public-domain alternate but a two-person profile crop. |
| SCO territorial commandant | `blocked` | Andrew Jameson McCulloch is the strongest identity/role lead (Edinburgh-born, GOC 52nd Lowland Division), but the available NPG portrait is licensable rather than redistribution-defensible. Do not substitute Ironside or Dowding (vanilla-owned), or generate a real person. |

## Source and rights evidence

- Cunninghame Graham: Commons/HathiTrust scan, no later than 1907, Commons
  public-domain/PD-US-expired basis.
- Saunders Lewis: `Y Drych`, 3 February 1916, National Library of Wales page;
  Commons Public Domain Mark / pre-1931 publication basis. The source master is
  byte-identical to the verified prior retry because Wikimedia returned HTTP 429
  on the repeat download.
- Robert Knox Ross: Erfgoed 's-Hertogenbosch biography and Brabant collection
  object report 53rd Welsh command and `CC BY-SA 3.0 NL`; object detail cache-missed
  during this retry, so parent must reconfirm metadata before shipping.
- Gerard Bucknall: IWM B 5468, No. 5 Army Film & Photographic Unit, Sgt Laing,
  1944; Commons UK Government/Crown copyright expiry/public-domain rationale.

## Ownership gate

The installed vanilla and project roots were searched across `common/characters`,
`history/countries`, `gfx/leaders`, `interface`, and `localisation` for exact
names, surname variants, title/name order, character IDs, and portrait consumers.
No character or portrait consumer was found for Cunninghame Graham, Saunders
Lewis, Robert Knox Ross, or Gerard Bucknall. Vanilla ownership was confirmed for
`ENG_hugh_dowding` and `ENG_edmund_ironside` in `common/characters/ENG.txt`, the
England history recruitment block, and interface/idea portrait definitions; those
people remain excluded from SCO.

## Validation performed

- PIL opened and verified every JPG/PNG in the package.
- Recorded dimensions and crop boxes match the source/crop files.
- Every line in `source_hashes.sha256` recomputed to the listed SHA-256.
- Contact sheet was visually reviewed; crops are mechanical only.
- No `.dds`, `.gfx`, gameplay, localisation, advisor, or `_small` output exists
  in the package.

## Remaining blockers and simplifications

- No defensible Scottish commander binary was found in this bounded retry; the
  SCO commander row is explicitly blocked.
- Ross remains `needs_user_review` until the collection record's licence is
  reconfirmed; no DDS is claimed.
- The parent agent owns any final processing, DDS conversion, GFX wiring,
  gameplay/localisation alignment, and final acceptance review.

