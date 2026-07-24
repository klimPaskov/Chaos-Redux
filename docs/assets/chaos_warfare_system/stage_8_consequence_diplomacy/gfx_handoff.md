# Stage 8 CBRN Consequence Diplomacy Decision Icon GFX Handoff

These three independent static decision icons are ready for wiring.

Suggested target definition: `interface/cbrn_diplomacy.gfx`.

No `.gfx` file was edited in this asset-only package.

Preserve every sprite name and texture path exactly as shown below.

## Ready-to-copy sprite definitions

```text
spriteType = {
	name = "GFX_decision_cbrn_demand_inspections"
	texturefile = "gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_demand_inspections.dds"
}

spriteType = {
	name = "GFX_decision_cbrn_share_forensic_evidence"
	texturefile = "gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_share_forensic_evidence.dds"
}

spriteType = {
	name = "GFX_decision_cbrn_sponsor_decontamination_mission"
	texturefile = "gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_sponsor_decontamination_mission.dds"
}
```

## Runtime mapping

| Sprite name | Stable decision id | Final DDS | Target | Visual cue |
| --- | --- | --- | ---: | --- |
| `GFX_decision_cbrn_demand_inspections` | `decision_cbrn_demand_inspections` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_demand_inspections.dds` | 32x32 | Sealed depot door, inspection lamp, clipboard/access papers. |
| `GFX_decision_cbrn_share_forensic_evidence` | `decision_cbrn_share_forensic_evidence` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_share_forensic_evidence.dds` | 32x32 | Tamper-sealed evidence case, specimen vial and shell fragment, dossier photographs and custody papers. |
| `GFX_decision_cbrn_sponsor_decontamination_mission` | `decision_cbrn_sponsor_decontamination_mission` | `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_sponsor_decontamination_mission.dds` | 32x32 | Foreign mobile wash rig, hose spray, protected worker, and relief-marked aid crate. |

The package manifest, prompt records, final review sheets, validation evidence, and hashes are under this package folder.

The wiring agent should attach each sprite to the matching stable decision id and keep localisation and gameplay changes outside this asset-only package.

Open wiring uncertainty: confirm whether the final project convention places Stage 8 diplomacy sprites in `interface/cbrn_diplomacy.gfx` or an already existing CBRN GFX definition before insertion.
