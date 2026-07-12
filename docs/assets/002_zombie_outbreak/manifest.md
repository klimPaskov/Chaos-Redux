# Event 002 Zombie Outbreak - decision icon cleanup manifest

## Package overview

- Event id: `002`
- Event slug: `zombie_outbreak`
- Source mode: Codex built-in `$imagegen`, one independent generation per final asset
- Transparency workflow: flat `#ff00ff` source field, official imagegen chroma-removal helper, exact-size RGBA processing
- Final DDS format: one-image-level uncompressed 32-bit BGRA/B8G8R8A8, canonical channel masks
- Sprite registry: `interface/chaosx_gfx_cleanup.gfx`
- Contact sheet: `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/contact_sheet_transparency.png`

The category icons were composed specifically for 52x40 presentation. The migration-restriction decision icon was generated separately for 32x32 presentation; it is not a resized category icon. Each final retains transparent unused canvas, a restrained dark edge, and a subtle dark shadow. No source link, third-party author, archive, date, licence, or public-domain claim applies because every source is generated.

## Reference review

The visual review used the existing `decision_category_zombies_cure.dds`, 52x40 vanilla decision-category icons including border conflict, fortification, resistance, paranoia, and economy examples, and the eight Event 002 weaponized zombie portraits as strain-theme references only. No reference image was copied, recoloured, or resized into a final.

After the skill example library was restored, the final contact sheet was compared again with `.agents/skills/chaos-redux-event-assets/assets/decisions/`. The restrained painterly silhouettes, sparse detail, native-size readability, and transparent framing match that reference family; no regeneration was required.

## Asset inventory

| Asset | Type and intended use | Source PNG | Processed PNG | Final DDS | Target | Sprite | Related id | Status | Notes |
|---|---|---|---|---|---:|---|---|---|---|
| `decision_category_zombie_outbreak_prevention` | decision category; outbreak cordon and checkpoint | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_zombie_outbreak_prevention.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_zombie_outbreak_prevention.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_zombie_outbreak_prevention.dds` | 52x40 | `GFX_decision_category_zombie_outbreak_prevention` | `decision_category_zombie_outbreak_prevention` | `handed_off` | Lowered quarantine boom, barricade, masked sentry. |
| `decision_category_weaponized_zombie_operations` | decision category; controlled bioweapon operations | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_operations.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_operations.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_operations.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_operations` | `decision_category_weaponized_zombie_operations` | `handed_off` | Sealed canister linked to restrained undead bust. |
| `decision_category_anti_zombie_league` | decision category; multinational defensive league | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_anti_zombie_league.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_anti_zombie_league.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_anti_zombie_league.dds` | 52x40 | `GFX_decision_category_anti_zombie_league` | `decision_category_anti_zombie_league` | `handed_off` | Reinforced shield and barricade resisting an undead hand. |
| `decision_category_weaponized_zombie_infected` | decision category; infected strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_infected.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_infected.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_infected.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_infected` | `decision_category_weaponized_zombie_infected` | `handed_off` | Clouded eye, three raised lesions, biohazard identity tag. |
| `decision_category_weaponized_zombie_rabid` | decision category; rabid strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_rabid.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_rabid.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_rabid.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_rabid` | `decision_category_weaponized_zombie_rabid` | `handed_off` | Feral fanged snarl with snapped restraint and broken links. |
| `decision_category_weaponized_zombie_parasitic` | decision category; parasitic strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_parasitic.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_parasitic.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_parasitic.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_parasitic` | `decision_category_weaponized_zombie_parasitic` | `handed_off` | Three pale parasite tendrils emerging from a shadowed host. |
| `decision_category_weaponized_zombie_mutant` | decision category; mutant strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_mutant.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_mutant.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_mutant.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_mutant` | `decision_category_weaponized_zombie_mutant` | `handed_off` | Asymmetric host with unstable broken DNA helix. |
| `decision_category_weaponized_zombie_undead` | decision category; undead strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_undead.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_undead.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_undead.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_undead` | `decision_category_weaponized_zombie_undead` | `handed_off` | Skeletal hand rising through broken grave earth. |
| `decision_category_weaponized_zombie_necrotic` | decision category; necrotic strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_necrotic.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_necrotic.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_necrotic.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_necrotic` | `decision_category_weaponized_zombie_necrotic` | `handed_off` | Blackened cracked tissue crumbling from a bandaged limb. |
| `decision_category_weaponized_zombie_demonic` | decision category; demonic strain identity | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_category_weaponized_zombie_demonic.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_category_weaponized_zombie_demonic.png` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_demonic.dds` | 52x40 | `GFX_decision_category_weaponized_zombie_demonic` | `decision_category_weaponized_zombie_demonic` | `handed_off` | Horned undead skull with broken iron seal; no glow or halo. |
| `decision_zombie_lift_migration_restrictions` | decision icon; reopen border after containment | `docs/assets/002_zombie_outbreak/source/gfx_cleanup/decision_zombie_lift_migration_restrictions.png` | `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/decision_zombie_lift_migration_restrictions.png` | `gfx/interface/decisions/002_zombie_outbreak/decision_zombie_lift_migration_restrictions.dds` | 32x32 | `GFX_decision_zombie_lift_migration_restrictions` | `decision_zombie_lift_migration_restrictions` | `handed_off` | Open gate doors, raised boom, slack broken quarantine chain. |

## Image-generation prompts

Every prompt specified richly hand-painted 1930s-1940s grand-strategy UI art, a perfectly uniform `#ff00ff` chroma field, crisp isolated subject, generous padding, final-size readability, no magenta in the subject, and no text, watermark, fake checkerboard, opaque square, circular medallion, halo, glow, white outline, sticker border, UI frame, cast shadow, or floor plane. The asset-specific requests were:

1. `decision_category_zombie_outbreak_prevention`: "Emergency outbreak-prevention cordon with sturdy military checkpoint barricade, lowered quarantine boom gate, and small gas-masked sentry silhouette."
2. `decision_category_weaponized_zombie_operations`: "Squat sealed pathogen canister beside a controlled fantasy undead bust wearing a heavy restraint collar and short chain anchored to the canister."
3. `decision_category_anti_zombie_league`: "Battered steel defensive shield reinforced by crossed wooden barricade beams, stopping one clawed undead hand, with restrained multinational ribbon accents."
4. `decision_category_weaponized_zombie_infected`: "Stylized infected host bust with three raised dark lesions, one clouded eye, and a metal biohazard identity tag at the collar; non-graphic."
5. `decision_category_weaponized_zombie_rabid`: "Feral fantasy undead head in profile with pronounced fanged snarl, snapped restraint collar, and broken chain links; no victim or biting contact."
6. `decision_category_weaponized_zombie_parasitic`: "Shadowed host bust with three thick pale parasite tendrils emerging from the crown and curling outward; no exposed anatomy."
7. `decision_category_weaponized_zombie_mutant`: "Unstable asymmetrical mutant host with oversized armored shoulder, crossed behind by one broken DNA double helix."
8. `decision_category_weaponized_zombie_undead`: "Skeletal undead hand thrusting upward from broken grave earth, fingers spread, with a torn military identification chain at the wrist."
9. `decision_category_weaponized_zombie_necrotic`: "Dry blackened fantasy undead forearm and hand with cracked tissue crumbling into large flakes and a wilted medical bandage; no wet gore."
10. `decision_category_weaponized_zombie_demonic`: "Horned demonic undead skull with short asymmetric swept-back horns, cracked brow, heavy fangs, and a broken iron seal; matte and without glow."
11. `decision_zombie_lift_migration_restrictions`: "Quarantine border gate reopening after containment, central doors swung outward, striped boom raised, and quarantine chain lying slack and broken."

## Validation and review

- All ten category PNG/DDS pairs are exactly 52x40; the decision PNG/DDS pair is exactly 32x32.
- All eleven PNGs contain both fully transparent and fully opaque pixels. Every corner pixel is transparent.
- No visible chroma-magenta pixels remain in any final PNG.
- Every DDS decodes pixel-identically to its processed PNG and uses 32-bit BGRA masks `00FF0000/0000FF00/000000FF/FF000000` with one stored image level.
- The checker contact sheet was manually reviewed for silhouette, subject identity, square matte, bright fringe, white outline, and glow/halo artifacts.
- Review risk: the parasitic icon can read as a tendril-crowned host at first glance, but the three large organic tendrils remain distinct at 52x40. The infected tag is secondary at native size; the lesion pattern and clouded eye carry the strain identity.
- Fallbacks or simplifications: none. Every requested asset has an independent generated source, exact-size processed PNG, and final DDS.
- Localisation key: `not_needed` for this asset-only handoff. Wiring remains with the main agent.
