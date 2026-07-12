# Event 002 Zombie Outbreak - decision sprite handoff

## Target registry

Implemented registry: `interface/chaosx_gfx_cleanup.gfx`.

No `.gfx`, `.gui`, gameplay, localisation, spreadsheet, or flag file was edited by the asset worker. The main implementation registered the exact sprite names and final texture paths below.

| Related id | Sprite name | Final texture path | Size | State |
|---|---|---|---:|---|
| `decision_category_zombie_outbreak_prevention` | `GFX_decision_category_zombie_outbreak_prevention` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_zombie_outbreak_prevention.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_operations` | `GFX_decision_category_weaponized_zombie_operations` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_operations.dds` | 52x40 | ready |
| `decision_category_anti_zombie_league` | `GFX_decision_category_anti_zombie_league` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_anti_zombie_league.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_infected` | `GFX_decision_category_weaponized_zombie_infected` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_infected.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_rabid` | `GFX_decision_category_weaponized_zombie_rabid` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_rabid.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_parasitic` | `GFX_decision_category_weaponized_zombie_parasitic` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_parasitic.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_mutant` | `GFX_decision_category_weaponized_zombie_mutant` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_mutant.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_undead` | `GFX_decision_category_weaponized_zombie_undead` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_undead.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_necrotic` | `GFX_decision_category_weaponized_zombie_necrotic` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_necrotic.dds` | 52x40 | ready |
| `decision_category_weaponized_zombie_demonic` | `GFX_decision_category_weaponized_zombie_demonic` | `gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_demonic.dds` | 52x40 | ready |
| `decision_zombie_lift_migration_restrictions` | `GFX_decision_zombie_lift_migration_restrictions` | `gfx/interface/decisions/002_zombie_outbreak/decision_zombie_lift_migration_restrictions.dds` | 32x32 | ready |

## Ready-to-copy sprite definitions

```text
spriteType = {
	name = "GFX_decision_category_zombie_outbreak_prevention"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_zombie_outbreak_prevention.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_operations"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_operations.dds"
}
spriteType = {
	name = "GFX_decision_category_anti_zombie_league"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_anti_zombie_league.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_infected"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_infected.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_rabid"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_rabid.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_parasitic"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_parasitic.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_mutant"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_mutant.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_undead"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_undead.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_necrotic"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_necrotic.dds"
}
spriteType = {
	name = "GFX_decision_category_weaponized_zombie_demonic"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/categories/decision_category_weaponized_zombie_demonic.dds"
}
spriteType = {
	name = "GFX_decision_zombie_lift_migration_restrictions"
	texturefile = "gfx/interface/decisions/002_zombie_outbreak/decision_zombie_lift_migration_restrictions.dds"
}
```

## Review notes

- The category sprites are separate 52x40 sources, not derived from focus, idea, portrait, or decision icons.
- The 32x32 decision sprite has its own independently generated source.
- The checker review sheet is `docs/assets/002_zombie_outbreak/processed/gfx_cleanup/contact_sheet_transparency.png`.
- No naming or path uncertainty remains. The main agent only needs to add the definitions and point the category/decision entries at these sprites.
