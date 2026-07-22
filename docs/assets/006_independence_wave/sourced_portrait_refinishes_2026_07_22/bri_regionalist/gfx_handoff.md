# Event 006 BRI regionalist portrait - parent wiring handoff

This package does not edit `.gfx`, gameplay, localisation, country history, or
the runtime texture folder. It supplies a source-preserving portrait candidate
for the existing BRI civic-delegate leader.

## Existing sprite to preserve

```text
spriteType = {
	name = "GFX_portrait_BRI_independence_wave_civic_commission"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds"
}
```

Definition: `interface/006_independence_wave_brittany_portraits.gfx`  
Character token: `BRI_independence_wave_civic_delegate`  
Role branches: traditional regionalist compact; protected-ports patron  
Subject: Régis de l'Estourbeillon, grounded male Breton regionalist civic figure

## Selected art

- raw ImageGen master: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png` (`1024x1536`, RGB, SHA-256 `CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7`)
- processed review PNG: `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png` (`156x210`, opaque RGB, SHA-256 `BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8`)
- visual comparison: `contact_sheets/bri_regionalist_identity_review.png`
- final runtime DDS: deferred to parent; expected path `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`

The parent should independently review the selected face against the unchanged
John Wickens source before conversion. If identity drift is judged material,
fail closed: reject this candidate and keep the civic slot blocked. Do not wire
the retained v1 alternative without review, the Dulac illustration, a generated
or generic face, a female identity, an advisor, or an operative.

## Suggested parent actions

1. Review `contact_sheets/bri_regionalist_identity_review.png` and the source
   master against the selected processed portrait.
2. If likeness and costume are accepted, convert the processed RGB PNG with
   `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to the
   existing runtime texture path.
3. Preserve the existing sprite name and `.gfx` declaration; no duplicate
   declaration is needed.

