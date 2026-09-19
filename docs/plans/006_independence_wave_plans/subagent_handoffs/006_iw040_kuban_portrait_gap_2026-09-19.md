# IW-040 Kuban Ivanis portrait gap handoff

Date: 2026-09-19.

Owner: Chaos Redux portrait-production subagent.

Disposition: documentation-only audit; unresolved installed-build asset gap; no gameplay or central admission change.

## Scope and accepted contract

This handoff covers only the `KUB_ivanis_vasily_nikolaevich` portrait tokens used by IW-040 Kuban cleanup and route setup.

The accepted IW-040 package contract intentionally reuses the vanilla Ivanis character and portrait. `docs/events/006_independence_wave/kuban_package.md:3,27,31` describes the vanilla Ivanis roster and portrait as the package baseline. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw040_kuban_package_source_scaffold_handoff_2026_08_12.md:18,27,37` explicitly says that no Kuban-specific portraits or GFX are claimed and that vanilla identity reuse remains intentional until a separate asset/rights decision exists. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw040_current_audit_2026_08_13.md:15` records the same cleanup contract.

No accepted package decision authorizes a new grounded source-placeholder portrait or a Kuban-specific portrait override. The portrait worker therefore did not promote a source, create a crop, or add portrait wiring.

## Installed vanilla evidence

The installed build is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.

- `common/characters/KUB.txt:3-8` defines `KUB_ivanis_vasily_nikolaevich` and references `GFX_portrait_KUB_ivanis_vasily_nikolaevich` for the large army portrait and `GFX_idea_KUB_ivanis_vasily_nikolaevich` for the small portrait.
- `history/countries/KUB - Kuban Republic.txt:84` recruits the same vanilla character.
- `dlc/dlc034_no_step_back/interface/nsb_portraits.gfx:393-396` declares `GFX_portrait_KUB_ivanis_vasily_nikolaevich` with texture path `gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds`.
- `dlc/dlc034_no_step_back/interface/nsb_ideas_characters.gfx:110-113` declares `GFX_idea_KUB_ivanis_vasily_nikolaevich` with texture path `gfx/interface/ideas/idea_KUB_ivanis_vasily_nikolaevich.dds`.
- `dlc/dlc034_no_step_back/gfx/interface/ideas/idea_KUB_ivanis_vasily_nikolaevich.dds` exists, is 65x67 pixels, is 17,548 bytes, and has SHA-256 `c215128b588ffff5b03fc1885e0619dcc66cac31798b6cc3b514f48f31a26e93`.
- `dlc/dlc034_no_step_back/gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds` is absent from the complete installed vanilla tree. No alternate copy of that filename was found elsewhere under the installed game directory.

The result is narrower than a missing-token report: both GFX identifiers are declared by the installed No Step Back interface files, and the small idea sprite resolves to an existing DDS. The large portrait identifier resolves to a declaration whose referenced texture is missing, so the full 156x210 character portrait cannot be verified as renderable in this installed build.

## Current mod evidence

`common/scripted_effects/006_independence_wave_kuban_package_effects.txt:478-487` restores both civilian and army portrait scopes to the two vanilla Ivanis tokens during cleanup. No package-owned KUB character file is present, and no matching KUB/Ivanis portrait DDS or mod-side portrait sprite exists under `gfx/` or `interface/`.

The package-owned portrait registry is `interface/006_independence_wave_portraits_registry.gfx`. It has no Ivanis entry. Adding one, plus an IW-040 roster override and cleanup guard, would be a new package-specific portrait decision and is outside the accepted contract recorded above.

## Source, processing, and rights state

No external source was archived because the accepted IW-040 contract does not authorize a source-placeholder repair. No ImageGen call was made. RunPod was not opened or operated.

There is no new file under `docs/assets/portraits/006_independence_wave/` and no change to its flat shelf or single `processed/` child.

No crop, crop metadata, provenance record, review image, PNG, DDS, manifest, or portrait-specific `.gfx` entry was produced. Consequently, there are no new source or processed dimensions and hashes to report beyond the existing vanilla small-DDS evidence above.

## Review result and replacement state

Identity review: the installed character identity and package references agree on `KUB_ivanis_vasily_nikolaevich`; no substitute identity was introduced.

Framing review: not run because no source-placeholder candidate was authorized or produced.

Asset review: `needs_user_review` / unresolved. The parent decoded and opened the small vanilla idea texture at native 65x67; it is a readable vanilla character-card treatment with intact transparency and no visible matte or crop defect. The large vanilla portrait texture is missing from the installed tree, so no 156x210 consumer can be reviewed.

Replacement state: no replacement is installed. The package remains on its existing vanilla token references, with the large token pending an explicit scope and rights decision. This is not a live-completion claim.

## Required next decision and gates

An authorized follow-up must first amend the IW-040 package contract to permit a dedicated, exact-identity grounded source placeholder and define its rights basis. Only after that acceptance may the portrait worker archive an attributed source on the flat Event 006 shelf, create the deterministic 156x210 crop, run the required PNG/DDS processing, add the portrait registry entry, and add package-scoped setup/cleanup wiring.

The eventual source package would still require independent identity/framing review, rights review, converter output inspection, and user live-game validation. The user remains responsible for supplying any HOI4-style final through RunPod; this handoff does not authorize the worker to operate RunPod.

## Validation and files changed

The installed vanilla character, GFX declarations, texture paths, and DDS header/dimensions were inspected from the paths listed above. No gameplay, character identity, localisation, interface, or asset file was edited.

Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw040_kuban_portrait_gap_2026-09-19.md`.

Skipped by design: source-placeholder production, crop and framing review, PNG/DDS conversion, mod portrait wiring, MCP/live-game validation, RunPod, commit, and staging. The remaining blocker is the missing accepted source/rights decision for an IW-040-specific portrait repair.
