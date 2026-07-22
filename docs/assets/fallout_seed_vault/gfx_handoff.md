# Seed Vault Custody report-picture `.gfx` handoff

- Final DDS: `gfx/event_pictures/fallout_seed_vault/seed_vault_report.dds`
- Final dimensions: `210x176`
- Proposed sprite name: `GFX_fallout_seed_vault_report`
- Registered target `.gfx`: `interface/fallout_world_end.gfx`.
- Intended use: report event picture for the dormant global "Seed Vault Custody" chain.
- The processed PNG/DDS preserves a feathered transparent perimeter consistent with the inspected vanilla report-picture family, the central image is fully opaque.
- Ready-to-copy texture path: `gfx/event_pictures/fallout_seed_vault/seed_vault_report.dds`
- Suggested sprite skeleton for the parent-owned registry:

```text
spriteType = {
	name = "GFX_fallout_seed_vault_report"
	texturefile = "gfx/event_pictures/fallout_seed_vault/seed_vault_report.dds"
}
```

Final `.gfx` wiring is complete. The parent owns the event, localisation, interface, and gameplay references.
