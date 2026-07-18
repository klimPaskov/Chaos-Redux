# FORM-48 Pacific GFX handoff

Date: 2026-07-17
Owner after handoff: parent implementation agent

## Parent-owned registration

The final 128x128 texture is installed. Register it without renaming, preferably
in a dedicated `interface/006_independence_wave_form48.gfx` registry alongside
the existing FORM-03 and FORM-05 pattern:

```text
spriteTypes = {
	spriteType = {
		name = "GFX_independence_wave_formable_form_48"
		texturefile = "gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds"
	}
}
```

The parent must point the stable FORM-48 decision/category/detail-window
consumer at `GFX_independence_wave_formable_form_48` and validate that the
consumer uses the complete 128x128 texture. This package deliberately does not
edit `.gfx`, gameplay, localisation, registry rows, or scripted GUI.

## Flag lookup

Country flags do not need `.gfx` sprite entries. HOI4 resolves the complete
families by tag and ideology filename:

- `HBX`, `HBX_democratic`, `HBX_communism`, `HBX_fascism`, `HBX_neutrality`;
- `PFX`, `PFX_democratic`, `PFX_communism`, `PFX_fascism`, `PFX_neutrality`;
- the same names under `gfx/flags/medium/` and `gfx/flags/small/`.

Parent wiring actions:

1. Keep `HBX` as the California carrier tag locked by the accepted FORM-48 plan.
2. Apply `PFX` as the Pacific Federation cosmetic/formable identity.
3. Register the emblem sprite above and use it in the stable FORM-48 UI consumer.
4. Do not create ideology recolours: the five names per tag intentionally share
   one constitutional/civic design.

## Protected boundary

No portrait or advisor-icon registration belongs in this FORM-48 handoff.
BAY/RHI portraits and all Event 006 advisor-icon decisions remain untouched.
