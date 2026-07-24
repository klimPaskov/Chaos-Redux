# Stage 7 Biological Countermeasure Icon GFX Handoff

This handoff is for the main agent that will register the later Stage 7 biowarfare sprites.

No `.gfx` file was edited because the bounded request supplied sprite names and final DDS paths but no target registration file.

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

The later wiring pass should connect these sprites to the already registered Stage 7 ids without renaming or changing the asset type.

No localisation, gameplay, GUI, existing icon, military-raid asset, or protected reference file was changed by this package.
