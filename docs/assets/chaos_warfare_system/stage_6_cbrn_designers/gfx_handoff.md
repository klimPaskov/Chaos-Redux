# GFX handoff: Stage 6 CBRN designer icons

The asset package does not edit `.gfx` files. The following sprite names are proposed because the parent supplied stable identifiers and runtime DDS paths but no sprite names. They follow the existing Stage 6 CBRN designer naming pattern.

Suggested target file: `interface/cbrn_designers.gfx`

```text
spriteType = {
	name = "GFX_cbrn_protective_equipment_consortium"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_protective_equipment_consortium.dds"
}

spriteType = {
	name = "GFX_cbrn_mobile_decontamination_works"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_mobile_decontamination_works.dds"
}

spriteType = {
	name = "GFX_cbrn_biological_security_directorate"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_biological_security_directorate.dds"
}

spriteType = {
	name = "GFX_cbrn_medical_countermeasure_directorate"
	texturefile = "gfx/interface/ideas/cbrn_designers/cbrn_medical_countermeasure_directorate.dds"
}
```

| Stable identifier | Proposed sprite | Runtime DDS | Size / format | Archive SHA-256 | Alpha evidence | Visual distinction |
| --- | --- | --- | --- | --- | --- | --- |
| `cbrn_protective_equipment_consortium` | `GFX_cbrn_protective_equipment_consortium` | `gfx/interface/ideas/cbrn_designers/cbrn_protective_equipment_consortium.dds` | 64x64, 16,512-byte legacy uncompressed BGRA | `48049c0a1c236f815748ab3c26c6b11e93f1aeace90d20213388fa5380f487a8` | alpha 0..255; 1723 transparent, 621 partial, 1752 opaque; opaque magenta 0 | front-facing respirator, twin filters, industrial canister |
| `cbrn_mobile_decontamination_works` | `GFX_cbrn_mobile_decontamination_works` | `gfx/interface/ideas/cbrn_designers/cbrn_mobile_decontamination_works.dds` | 64x64, 16,512-byte legacy uncompressed BGRA | `8d1078531f28444f3b93c475db39144e5f68c266d7d346730459f56d9ed3ef39` | alpha 0..255; 2358 transparent, 583 partial, 1155 opaque; opaque magenta 0 | tank truck, hose, pale cyan wash fan |
| `cbrn_biological_security_directorate` | `GFX_cbrn_biological_security_directorate` | `gfx/interface/ideas/cbrn_designers/cbrn_biological_security_directorate.dds` | 64x64, 16,512-byte legacy uncompressed BGRA | `45b0e426148962508a3f598d7cbf9c984c679e9f3e3e79f0ae2ecacc5b8f1384` | alpha 0..255; 2232 transparent, 638 partial, 1226 opaque; opaque magenta 0 | sealed teal vial, containment sleeve, tamper lock, inspection lens |
| `cbrn_medical_countermeasure_directorate` | `GFX_cbrn_medical_countermeasure_directorate` | `gfx/interface/ideas/cbrn_designers/cbrn_medical_countermeasure_directorate.dds` | 64x64, 16,512-byte legacy uncompressed BGRA | `3dde4dffe6b210a087b5c4f285da791597f41bf2659fd685439d939060f75da5` | alpha 0..255; 1680 transparent, 733 partial, 1683 opaque; opaque magenta 0 | oxygen mask, medical case, amber vials, triage marker |

Archive/runtime pairs are byte-identical for all four icons. Runtime registration remains parent-owned. No localisation key was changed; the parent should connect each proposed sprite to its corresponding MIO/designer definition.

## Handoff uncertainty and risks

- Sprite names are proposed, not parent-supplied; preserve them if they match the parent’s intended `.gfx` identifiers, or rename only before wiring if an existing registration requires different names.
- Runtime DDS paths and stable identifiers are fixed by the parent prompt and must not be renamed.
- No gameplay, localisation, `.gfx`, or unrelated documentation was changed in this sidecar.
