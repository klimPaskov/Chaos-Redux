# Event 006 active-vanilla conflict retry — sourced portrait handoff

Date: `2026-07-22`

Status: `source_research_complete_processing_deferred`

## Scope and result

I researched exactly the three parent-requested grounded male roles whose
former people conflict with active vanilla characters:

| Package / role | Source-ready primary | Alternate | Remaining caveat |
|---|---|---|---|
| `IW-008 RHI` civic/constitutional/patron | Karl Jarres, 1925 Bundesarchiv Bild 102-01175, CC BY-SA 3.0 DE | Wilhelm Marx, Bain/LOC public-domain source | Jarres archive upload notes a small historical uploader crop; the local file is unchanged. Marx’s LOC caption date is unrecorded (Commons metadata says 1920). |
| `IW-009 BAY` military/emergency mountain command | Eugen Ritter von Schobert, July 1940 NAC 2-12702, public-domain/free-use basis asserted by NAC/Commons | Ludwig Kübler, c.1941 Polish-book scan, exact mountain fit | Schobert is a Bavarian infantry/army commander rather than a Gebirgstruppe specialist. Kübler’s anonymous 1979-book publication/right chain needs review. |
| `IW-001 SCO` territorial/military command | Victor Morven Fortune, 1940 IWM RML 342, UK-government public-domain scan | Archibald Rice Cameron, 1929 Bassano/NPG negative | Fortune primary is only 200×250 but face-visible. Cameron’s NPG page displays a copyright notice while Commons marks PD, so Cameron is `needs_review`. |

The complete source ledger, direct URLs, archive/author/licence notes, era and
role fit, exact local dimensions/bytes/SHA-256, bounded collision scan, and
deferred output paths are in
[`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/manifest.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/manifest.md).

The deferred runtime-name map is in that package’s
[`gfx_handoff.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/gfx_handoff.md), and the exact source
hash list is in [`source_hashes.sha256`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_hashes.sha256).

## Ownership and source gates

- The bounded scan searched both installed vanilla and current Chaos Redux in
  `common/characters`, `history/countries`, `common/country_leader`,
  `interface`, `gfx/leaders`, and `localisation/english`.
- Exact and variant tokens for Jarres, Marx, Schobert, Kübler, Fortune, and
  Cameron returned no textual hits in those roots.
- Existing parent-owned admission audits remain authoritative for the active
  vanilla conflicts: Adenauer/GER, von Epp/GER, and Ironside/ENG. No old
  identity is silently renamed or reused here.
- Every acquired binary is an unchanged source master. No PNG, DDS, crop,
  resize, visual-processing metadata, contact sheet, `.gfx`, gameplay, or
  localisation edit was made.
- No generated, fictional, generic, female, advisor, ImageGen, or fallback
  face was supplied.

## Parent follow-up

1. Independently review Jarres, Schobert, and Fortune as the proposed primaries
   and decide whether any alternate is preferable.
2. Resolve the Kübler publication/right chain and Cameron’s NPG/Commons rights
   conflict before processing either alternate.
3. Process only the selected source through the approved leader-portrait
   pipeline, obtain separate visual/rights approval, and create the exact
   runtime DDS. This package intentionally does not do those steps.
4. Re-run the parent-owned candidate/character/recruitment audit before any
   `.gfx` or gameplay admission. Keep the role unresolved if a reviewer
   rejects a source; no fallback is authorized.

## Files changed by this handoff

Only the new package and this dated handoff were added:

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_hashes.sha256`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/gfx_handoff.md`
- unchanged downloaded source masters under that package’s `source_masters/`
- this dated handoff file

No existing manifests, specs, gameplay, localisation, interface, GFX, or skill
files were changed.
