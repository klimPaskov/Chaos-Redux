# Event 014 modern model-source research handoff A

Date: 2026-08-22.

Owner: `chaosx_asset_source_researcher` scope, modern sourced visual-reference research only.

Status: one modern artwork reference has been acquired for each requested 3D job. All three are marked `needs_user_review` for parent approval of the exact ImageGen input and adaptation boundary. No ImageGen or Meshy call was made, and no gameplay, runtime, entity, GFX, event, localisation, processed, or DDS asset was edited or created.

## Selected modern references

| Job | Source and license | Untouched original | Dimensions | SHA-256 | Fit and review note |
| --- | --- | --- | --- | --- | --- |
| `cannibal_scavenger_warband` | [Justin Nichol, “Character concepts and Silhouettes”](https://opengameart.org/content/character-concepts-and-silhouettes), selected file `JustinOperable-Raider2.jpg`; CC BY-SA 3.0 | `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/refs/sourced/original/JustinOperable-Raider2.jpg` | 600 × 800 | `2DF37C7B800649B0E0E14DEC91285641319CF30D4B8EA6F8700792FDCCCECAE8` | Full-body modern post-apocalyptic raider with a long diagonal spear, rough wraps, hood or mask, and improvised pack logic. The source is static rather than running and carries CC BY-SA attribution/share-alike obligations, so the parent must adapt rather than trace it and review distribution terms. |
| `cannibal_feast_guard` | [Tiao Ferreira, “Gladius”](https://opengameart.org/content/gladius-0); CC0 1.0 | `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/refs/sourced/original/oga_gladius.JPG` | 814 × 1164 | `A05D6D2613A0DB92E27AA19C203A92A32D5A5DD9C63443D71643BB4BF97F99BA` | Full-body stocky shield-bearing fighter in a braced low melee stance with a clear opposite-hand weapon relationship. The source uses a rectangular shield and short sword, so the parent must independently adapt it to the requested round shield, hooded jaw-mask, rib-bone protection, and cleaver or axe. |
| `cannibal_feast_cohort` | [Engvee, “FREE Isometric Halberd Warrior”](https://engvee.itch.io/animated-isometric-halberd-warrior); explicit page permission for commercial and non-commercial projects, unlimited project quantity, and modification; no formal CC license stated | `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/refs/sourced/original/halberd_preview.gif` | 384 × 384, 92 frames | `D6094CB222D4D8DB4DB8C34945DA5B274D7B5077B11ECABDC8FF951713B45134` | Modern game unit preview with readable full-body isometric silhouette, long halberd-scale weapon, attack-ready combat stance, and textured armor/leather material logic. The source is an animated GIF and its custom permission should be retained with creator credit to Engvee and collaboration credit to Maksim Bugrimov; parent review is required before any redistribution of the untouched GIF. |

Access date for all sources: 2026-08-22 (Europe/Kiev).

Per-job provenance, source-page evidence paths, license evidence, direct URLs, creator/title/date fields, dimensions, hashes, fit notes, uncertainty, and adaptation prompts are recorded in each `refs/sourced/source_provenance.md` file:

- `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/refs/sourced/source_provenance.md`
- `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/refs/sourced/source_provenance.md`
- `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/refs/sourced/source_provenance.md`

Source-page evidence is archived untouched under each job's `refs/sourced/source_pages/` directory. The OpenGameArt page and CC BY-SA or CC0 license pages are preserved for the first two sources. The Engvee itch.io source page is preserved for the custom permission terms and collaboration credit.

## ImageGen adaptation direction

### `cannibal_scavenger_warband`

Create a substantially original full-body HOI4-style 3D model sheet of a lean, emaciated pale runner in a forward three-quarter sprint, with one foot lifted and a long crude spear or staff held low on a diagonal through both hands. Use only broad post-apocalyptic material logic from the source, such as rough wraps, ragged brown shoulder cloth, improvised straps, and a simple skull-like mask. Replace the source gas mask, exact hood, exact clothing arrangement, exact linework, exact pose, and source-specific accessories. Keep one unit centered on a neutral studio background with a clean silhouette and no extra characters. Do not reproduce any logo, protected character identity, or source costume, and do not introduce identifiable living Indigenous regalia, sacred motifs, or culture-specific body paint.

### `cannibal_feast_guard`

Create a substantially original stocky full-body melee guard in a braced, slightly crouched three-quarter stance, with a weathered round shield held forward and a compact crude cleaver or hand axe drawn back in the opposite hand. Add a hooded jaw-mask, dense rib-bone protection, dark ragged fabric, and scavenged iron or bone materials. Use the source only for broad body mass, shield blocking, and low guarded posture. Replace the Roman or gladiator helmet, classical armor, sword, exact blue-pen linework, and exact pose. Keep one unit centered on a neutral studio background with no extra figures, logos, or culture-specific motifs, and do not introduce identifiable living Indigenous regalia, sacred motifs, or culture-specific body paint.

### `cannibal_feast_cohort`

Create a substantially original aggressive full-body HOI4-style two-handed polearm infantry model sheet. Keep a forward-leaning, wide combat stance with both hands visibly controlling a long crude halberd or heavy spear, a strong diagonal weapon silhouette, and layered scavenged leather, dark cloth, bone, and rough iron materials. Use the source only for broad weapon scale, combat readability, and generic game-unit material logic. Replace the source armor, face, exact colors, exact animation frame, exact silhouette, and any source-specific ornament. Do not add a shield, recognizable game logo, protected character identity, or culture-specific motif. Keep one unit centered on a neutral studio background and do not introduce identifiable living Indigenous regalia, sacred motifs, or culture-specific body paint.

## Scope boundary, exclusions, and blockers

The user-provided images were treated as design-direction only and were not opened, copied, archived, or used as model inputs. The explicitly excluded path `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-59672c99-c6a5-4728-9ab5-71e311186bd4.png` was not used.

No archival, museum, historical, modern reenactment, identifiable living Indigenous regalia, sacred motif, or culture-specific body-paint reference is retained in this modern-only package.

No contact sheet was created because exactly one modern candidate was selected per requested job and no unresolved candidate comparison remains. Shared `sourced_reference_manifest.md`, `sourced_reference_contact_sheet.png`, and `gfx_handoff.md` were not overwritten.

This handoff does not claim that any generated adaptation is automatically covered by the source license. The Scavenger CC BY-SA source requires attribution and share-alike review, the Feast Guard CC0 source has no mandatory attribution but still requires substantial originality for the requested design, and the Feast Cohort custom permission should be reviewed before redistributing the untouched animated GIF. Parent-owned ImageGen adaptation, Meshy submission, model production, runtime wiring, GFX wiring, and final legal approval remain outstanding.
