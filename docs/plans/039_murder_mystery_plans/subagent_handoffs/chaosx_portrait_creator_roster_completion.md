# Chaos Redux portrait creator handoff: Event 039 compact roster completion

Status: `complete_with_parent_attachment_pending`.

This tranche completes the compact Event 039 Murder Mystery fictional portrait roster requested by the parent: the five existing country-leader portraits were individually audited, two full-size land commander portraits were installed, and one full-size operative-family portrait was installed for the foreign-cell organizer. The parent still owns character-token attachment because the concurrent `common/characters/039_murder_mystery_characters.txt` file was explicitly out of scope.

## Scope and safety

All eight subjects are fictional high-chaos identities, so the native ImageGen workflow was used throughout. No real-person source, web attribution, source-placeholder, provider-backed styled final, or RunPod operation was used. No character identity, traits, gameplay, localisation, country, focus, decision, event, or unrelated UI file was edited.

The three missing tokens are prepared for parent attachment: `murder_mystery_shadow_commander`, `murder_mystery_silent_guard_commander`, and `murder_mystery_foreign_cell_organizer`. The portrait package does not declare those tokens because the user prohibited edits to `common/characters`.

## Evidence and provenance

The required Event 039 Part 14 specification, asset prompt, Chaos Redux portrait workflow, event-assets workflow, and installed vanilla references were read before production. The matching canonical reference sheets were reviewed at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/operatives/contact_sheet.png`.

The installed vanilla consumers were verified against `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/ICE.txt` (`ICE_sveinn_bjornsson`, `civilian.large`), `common/characters/ENG.txt` (`ENG_alan_brooke`, `army.large`), `common/characters/FRA.txt` (`FRA_jacques_duclos`, full portrait stored in `army.large` with the explicit operative comment), `interface/_leader_portraits.gfx`, and `dlc/dlc028_la_resistance/interface/lar_portraits.gfx`. The canonical leader, land-commander, and operative families are opaque `156x210` textures.

The five existing source PNGs and prompt files were retained without replacement because they were already present in the shared worktree and passed the source, framing, and safety review. Their original native ImageGen outputs remain under `C:/Users/klimp/.codex/generated_images/01a04f14-ad5b-7750-9523-3cbe24871a9b/`.

The three missing-role prompts were retained at `docs/assets/039_murder_mystery/portraits/prompts/commander_039_shadow_commander.txt`, `commander_039_silent_guard_commander.txt`, and `operative_039_foreign_cell_organizer.txt`. Native ImageGen was also run directly in this turn with matching fictional prompts, and the corroborating outputs remain at the following default paths:

| Role | Direct native ImageGen output | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| Shadow Commander | `C:/Users/klimp/.codex/generated_images/01a05e2a-3d5c-7e73-960b-ef1c42f94ede/exec-cbc3db14-4d9d-44de-8df3-7817fc237d6b.png` | 1082x1453 | `e780f543cb173f3dc8ca03c4a35a5edd1194dd37aa8511f4659f72f60071353d` |
| Silent Guard Commander | `C:/Users/klimp/.codex/generated_images/01a05e2a-3d5c-7e73-960b-ef1c42f94ede/exec-38e3362c-4b6b-4fd6-a874-f0ce0dd52a72.png` | 1067x1474 | `c375988174d3c94671efc41f9aeb88be14011f80a0101b18a40fc72bebd47ae9` |
| Foreign Cell Organizer | `C:/Users/klimp/.codex/generated_images/01a05e2a-3d5c-7e73-960b-ef1c42f94ede/exec-02c43f22-f744-4757-8a74-e69b8a5dcba4.png` | 1080x1456 | `a17674c3a44a655769961e788c70264f28f0a6f66ff9673193232f1415dbe583` |

The direct in-turn outputs were reviewed but were not substituted for the already-reviewed shared production candidates, preserving concurrent work. The authoritative package source hashes are recorded in `docs/assets/039_murder_mystery/portraits/manifest.md` and `checksums.sha256`.

## Exact consumer forms

The five existing leader entries use only `civilian.large` because the live Event 039 character references use that full portrait slot. `murder_mystery_shadow_commander` and `murder_mystery_silent_guard_commander` use only `army.large` as land commanders. `murder_mystery_foreign_cell_organizer` uses only `army.large` as the installed vanilla operative character adapter; the semantic sprite and runtime basename identify it as the operative family.

No `army.small`, advisor, or high-command `65x67` dossier portrait was created. No alternate portrait form was inferred from the character roles.

## Installed files and wiring

The following three new runtime DDS files are installed under `gfx/leaders/039_murder_mystery/`:

| Token | Slot | Stable sprite | Runtime DDS |
| --- | --- | --- | --- |
| `murder_mystery_shadow_commander` | `army.large` | `GFX_portrait_039_shadow_commander` | `commander_039_shadow_commander.dds` |
| `murder_mystery_silent_guard_commander` | `army.large` | `GFX_portrait_039_silent_guard_commander` | `commander_039_silent_guard_commander.dds` |
| `murder_mystery_foreign_cell_organizer` | `army.large` operative adapter | `GFX_portrait_039_foreign_cell_organizer` | `operative_039_foreign_cell_organizer.dds` |

`interface/039_murder_mystery_portraits.gfx` now registers those three sprite keys and leaves the five existing sprite registrations unchanged. The parent attachment map is recorded in `docs/assets/039_murder_mystery/portraits/portrait_wiring.md`.

## Dimensions, hashes, and DDS round-trip

All eight retained source PNGs are opaque RGB/RGBA-equivalent source images and all processed PNGs are opaque `156x210`. Every runtime DDS is the converter’s one-level legacy BGRA layout with `DDS ` magic, `156x210` dimensions, 32-bit pixels, no mipmaps, and exactly `131168` bytes. Every decoded DDS matches its processed PNG pixel-for-pixel.

| Runtime basename | Source dimensions | Source SHA-256 | Processed SHA-256 | DDS SHA-256 | Round-trip |
| --- | ---: | --- | --- | --- | --- |
| `leader_039_emergency_constitutional_successor` | 1082x1454 | `95cd9f79d9d0cf98ec77add452534ae6b6745671881049fe609b060270ecaa11` | `dc267aa8cf69f3bdb5c0c8626a25ae6fd82e24089a0a20524da429c3d1c903a9` | `e8f9cc871767cd66504acd0ee7f0e8cb867b0c793997ac71dc89663886ab3f3a` | pass |
| `leader_039_first_knife` | 1081x1455 | `a9f9025f520f69dd48c6aa94954fc61eae6367578a28dd20f2d08577501e2d2e` | `9b475fc3d5e499ab0969510c997dedce232199105a27cff16dfc8fd1ec3fe823` | `da592e7440ac1ce9ec06b552edb82a7093c0e92888cda725c3ec731a20009930` | pass |
| `leader_039_hidden_hand` | 1083x1453 | `0943fb70cfcc5a02ed6390b99eb808bcf29aafd0466dcf77a4b055c08145b81b` | `90095a40f3c8b3c918d5c1b62deac08e4c9163f50313180952a5a1f87a8ac0ab` | `4c0b52cfc9f23eca6b1a972496a6ebd4b368a10d510168dcb328c9fbbe99ca0b` | pass |
| `leader_039_cells_without_masters` | 1082x1454 | `ce79cf0bfe62e4aad60619bc3f20623aca6fe1b268bdd3207c679efbf2dbe18d` | `268d17df0d5af2d16b34df12b4f1ea0fe2180221a1b06c28ae02b171d5e21730` | `78bf986a99cd1beaab9190e506e9db96aa8d5fe89df9d3f3c87ceea40495aa45` | pass |
| `leader_039_necessary_mask` | 1082x1454 | `1dd8566e970c5afee6ecd3e1fe00f6c9689fecfa8a321ca540c39bc4f5684b44` | `a137e1388e27e6092e717253f46425af647956c3edc15c770f59018aa6c7b26e` | `e887e806f746d6b73630ff28de9e92929e85fa9d6fb22f71aa7d520da6c7a64f` | pass |
| `commander_039_shadow_commander` | 1080x1456 | `78ffe8849cb423539704c030234983af3883478c73d45c8942df7ef8e26edf26` | `a579017511742eb5e3cbbb1b69e826380b2b7e5dfd8d6a1ddc552dae697eb96d` | `6464256d2ce88115a6427580b88d7683e53e83efba7f6c573acf34b65ffa191b` | pass |
| `commander_039_silent_guard_commander` | 1078x1459 | `8448f8e85b9a94a8d69980fd3b80ef686082ad4f01029553a0ce8304da9ff07e` | `0bd244248ba13197eabc6d03ad02684b85dd39814d887f494764d1ec8e911f81` | `fa33ce0eea4e0680c35ce2a01736d39b40e241da405afc26f83e8a4dd0079a26` | pass |
| `operative_039_foreign_cell_organizer` | 1080x1456 | `9b6561b1bc1673014d4990abe6ac95b8f84a82fdb1a1b54ea21b0d470d1fc0ae` | `d702ca1cfcbf81c12866e1773269404abce6c8865d407dc5b4921f723ffe867b` | `8b7d8e7e1ad4e8ca63b240e3612d2b8b37621091498b74a4fd99f77e3ee08e90` | pass |

The complete machine-readable checksum list is `docs/assets/039_murder_mystery/portraits/checksums.sha256`.

## Review evidence

The original five-portrait contact sheets remain preserved. The complete roster review artifacts are `docs/assets/039_murder_mystery/portraits/review/portrait_roster_contact_sheet.png`, `native_4x_nearest_roster_contact_sheet.png`, and `dds_roundtrip_roster_contact_sheet.png`.

The eight-portrait visual review passed at native size and enlarged size: faces are readable, crowns and chins are not clipped, shoulders remain visible, role clothing and settings separate the two commanders and organizer from the leader set, and no forbidden text, watermark, modern tactical equipment, fantasy treatment, gore, religious or ethnic coding, extremist insignia, generic ninja styling, or real-person likeness target was observed.

The existing five runtime DDS files were audited individually and all five passed the same header, dimensions, opacity, visual framing, and exact pixel round-trip checks. The three new DDS files passed the same checks after conversion.

## Emergency successor classification

`emergency_constitutional_successor` is `USED`, not orphaned, and was not deleted. `GFX_portrait_039_emergency_constitutional_successor` is consumed by the live Event 039 emergency-succession picture effects in `common/scripted_effects/039_murder_mystery_integration_effects.txt` at lines 410, 419, 428, and 436. The absence of a matching token in the concurrent character file does not make this runtime portrait orphaned.

## Replacement state and remaining handoff

All eight portraits are final fictional native-ImageGen outputs and none is `replacement_pending`. The parent should attach the three prepared tokens using the portrait map while preserving the exact `army.large`/operative-adapter distinction. No RunPod step is required or permitted for this fictional roster.

Skipped checks are live HOI4 launch, live in-game screenshot, and parent character attachment, because live validation belongs to the user and the character/localisation files were explicitly outside this tranche. No portrait-specific blocker remains.
