# Stage 7 Biological Countermeasure Icon GFX Handoff

The Stage 7 biological-countermeasure sprites are registered in `interface/biological_countermeasures.gfx`.

The definitions below are the exact registered runtime contract.

Preserve every sprite name and texture path exactly as shown below.

## Decision sprites

```text
spriteType = {
    name = GFX_decision_bio_activate_surveillance_network
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_activate_surveillance_network.dds"
}

spriteType = {
    name = GFX_decision_bio_quarantine_state
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_quarantine_state.dds"
}

spriteType = {
    name = GFX_decision_bio_border_control
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_border_control.dds"
}

spriteType = {
    name = GFX_decision_bio_anthrax_antibiotics
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_anthrax_antibiotics.dds"
}

spriteType = {
    name = GFX_decision_bio_plague_antibiotics
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_plague_antibiotics.dds"
}

spriteType = {
    name = GFX_decision_bio_tularemia_antibiotics
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_tularemia_antibiotics.dds"
}

spriteType = {
    name = GFX_decision_bio_international_medical_mission
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_international_medical_mission.dds"
}

spriteType = {
    name = GFX_decision_bio_sustain_containment
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_sustain_containment.dds"
}

spriteType = {
    name = GFX_decision_bio_expand_medical_capacity
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_medical_capacity.dds"
}

spriteType = {
    name = GFX_decision_bio_expand_biosecurity_capacity
    texturefile = "gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_biosecurity_capacity.dds"
}
```

## Idea sprites

```text
spriteType = {
    name = GFX_idea_bio_surveillance_network
    texturefile = "gfx/interface/ideas/biowarfare/countermeasures/idea_bio_surveillance_network.dds"
}

spriteType = {
    name = GFX_idea_smallpox_vaccination
    texturefile = "gfx/interface/ideas/biowarfare/countermeasures/idea_smallpox_vaccination.dds"
}
```

The decisions are exact 32x32 runtime compositions and the ideas are exact 64x64 runtime compositions.

The decision sprites are wired to their matching biological response decisions, and the two idea sprites are wired to `bio_surveillance_network_idea` and `smallpox_vaccination_program_idea`.

No existing icon or military-raid asset was removed, renamed, resized into another asset type, or overwritten.
