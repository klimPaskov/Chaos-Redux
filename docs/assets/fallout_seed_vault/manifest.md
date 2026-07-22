# Fallout Seed Vault Custody - asset manifest

## Requirement-to-runtime crosswalk

| Requirement | Artifact | Status |
|---|---|---|
| Fictional post-Fallout report image | `gfx/event_pictures/fallout_seed_vault/seed_vault_report.dds` | Complete and wired |
| Retained generated source PNG | `docs/assets/fallout_seed_vault/source/seed_vault_report_source.png` | Complete |
| Processed 210x176 preview PNG | `docs/assets/fallout_seed_vault/processed/seed_vault_report_preview.png` | Complete |
| Generation provenance | `docs/assets/fallout_seed_vault/prompt_provenance.md` | Complete |
| Sprite handoff | `docs/assets/fallout_seed_vault/gfx_handoff.md` | Complete and wired |

## Asset facts

- Asset id: `seed_vault_report`.
- Surface: report event picture.
- Source classification: fictional / alternate-history post-Fallout scene.
- Source mode: generated with official built-in ImageGen, generation fits because the Seed Vault Custody chain is fictional and needs a unique documentary-staged scene rather than a real historical photograph.
- Subject: two non-zombie custodians securing a concrete underground seed archive, steel vault cabinet, keys, ledger without legible writing, glass seed jars, and a dim emergency lamp.
- Visual family: sepia archival report photography, report-family reference inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png`.
- Constraints checked: no zombies, no gore, no corpses, no monsters, no readable text, no logos, no watermark, no modern props, no maps, no UI artifacts, no reused asset paths.
- Source dimensions: 1370x1148 pixels.
- Processed preview dimensions: 210x176 pixels, RGBA PNG, feathered report-paper perimeter (alpha minimum 0, maximum 255).
- Final DDS dimensions: 210x176 pixels.
- Final DDS format: legacy one-level uncompressed BGRA, 32-bit, `DDS ` magic, header size 124, pixel-format size 32, flags 65, fourCC 0, masks `0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000`, texture caps `0x1000`, exact length 147968 bytes, alpha-byte range 0-255.

## SHA-256

| File | SHA-256 |
|---|---|
| `docs/assets/fallout_seed_vault/source/seed_vault_report_source.png` | `9e40f4848fd33c17942a4d503d4be0aba2668a4c4709df5ddfbdb067540554da` |
| `docs/assets/fallout_seed_vault/processed/seed_vault_report_preview.png` | `b723a2a3f09cb22a71fc452a7969bfda04fa63a5c12cf5e73aaf1ed04a303920` |
| `gfx/event_pictures/fallout_seed_vault/seed_vault_report.dds` | `5b9697437d7b8c3428391a8fe8f0348caa19f4c1a543bc352473a402a778164d` |

## Ownership and review

- Generation and conversion are complete.
- The parent wired `GFX_fallout_seed_vault_report` in `interface/fallout_world_end.gfx`.
- Human events `188`, `190`, `191`, `192`, `193`, and `198` use the sprite. Hidden AI events use the same chain without a picture.
- The parent owns gameplay, localisation, interface, and event wiring.
- No fallback or placeholder was used. Static sprite registration is complete. Runtime visual observation remains unproved because HOI4 was not launched.
