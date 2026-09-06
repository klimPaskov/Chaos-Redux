# Event 012 priority surface and RSA cosmetic flag handoff

Status: implemented.

This handoff records the narrow Africa-scoped completion tranche for the Gods of Africa host priority presentation and the missing RSA cosmetic flag ladder. It does not change any other decision category and it does not promote a custom elephant asset.

## Host priority presentation

`common/decisions/012_africa_gods_decisions.txt` phases the visible host priority actions so the category presents the five core material lanes plus one advanced lane at a time. Emergency relief is the sixth lane before the provision focuses, support equipment replaces it after the arsenal-support focus, and aircraft reserves replace it after the logistics-support focus. The automatic demand-family selector remains capable of maintaining every supported family even when a family is not currently a visible manual row.

The phase gates are attached to the visible blocks for `gods_of_africa_prioritize_support` and `gods_of_africa_prioritize_emergency`, using the existing focus-unlock flags. The change is intentionally limited to the Event 012 category.

`common/ai_strategy_plans/012_africa_focus_plans.txt` now includes `africa_gods_of_africa_overlay_focus_plan`, which covers all twenty-four Gods overlay focus identifiers and is enabled only for an AI-controlled continental host with the Gods system active and activation committed. The plan also adds guarded factors for emergency need and vengeful wrath without changing non-Africa AI plans.

## RSA cosmetic flags

The runtime flag ladder now contains the nine TGA files required by the three RSA cosmetic branches:

* `gfx/flags/AFRICA_RSA_CONTINENTAL_COALITION.tga`
* `gfx/flags/medium/AFRICA_RSA_CONTINENTAL_COALITION.tga`
* `gfx/flags/small/AFRICA_RSA_CONTINENTAL_COALITION.tga`
* `gfx/flags/AFRICA_RSA_ALLIED_UNION_GOVERNMENT.tga`
* `gfx/flags/medium/AFRICA_RSA_ALLIED_UNION_GOVERNMENT.tga`
* `gfx/flags/small/AFRICA_RSA_ALLIED_UNION_GOVERNMENT.tga`
* `gfx/flags/AFRICA_RSA_REPUBLICAN_NATIONALIST.tga`
* `gfx/flags/medium/AFRICA_RSA_REPUBLICAN_NATIONALIST.tga`
* `gfx/flags/small/AFRICA_RSA_REPUBLICAN_NATIONALIST.tga`

The generated source and processing evidence is retained under `docs/assets/012_africa/flags/`. `manifest.json` records the three branch identities, source references, prompts, and hashes. `gfx_handoff.md` records the runtime paths and confirms that no new `.gfx` declaration is required because the country tags already resolve through the standard flag lookup. `qa/tga_validation.json` and `qa/AFRICA_RSA_cosmetic_flags_contact_sheet.png` provide the technical and visual QA evidence.

The validated dimensions and TGA descriptors are 82x52 normal with 32-bit type-2 data and descriptor `0x08`, 41x26 medium with 32-bit type-2 data and descriptor `0x08`, and 10x7 small with 32-bit type-2 data and descriptor `0x00`. Decoded pixel hashes match the processed PNG counterparts for all nine files.

## Elephant boundary

The `chaosx_elephant` unit intentionally reuses the vanilla `elephantry` sprite and entity actions. No custom elephant model, animation, sound definition, counter, or runtime override is required. The archived `docs/assets/012_africa/models_3d/elephant_shared_base/` material remains non-promoted reference/production history and is not part of the active runtime package.

## Validation limits and remaining work

The focus inspection and render are available, but the post-change focus refresh exceeded the MCP service's 180-second limit; this is recorded as an evidence limitation rather than treated as a source failure. A probability comparison request returned `PROBABILITY_SURFACE_EMPTY`, so dynamic scenario acceptance for the focus-plan weights remains incomplete. The user owns live HOI4 validation. Other Event 012 model, portrait, technology-viewer, and broad completion blockers remain documented in the event overview and are outside this narrow tranche.
