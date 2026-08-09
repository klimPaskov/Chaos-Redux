# Toxic Armored Warfare compatibility note

## Source of truth

This file documents the legacy `chemical_suppression` compatibility identifier. The complete accepted doctrine design and current implementation are documented in `docs/systems/chaos_warfare_doctrine.md`.

The player-facing track is Toxic Armored Warfare. Its implementation is in `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt`, with shared gates and state changes in the CBRN doctrine trigger and effect files.

## Current mastery progression

The five mastery rewards are:

1. Sealed Crew Compartments
2. Armored Agent Delivery
3. Gas-Chamber Saturation Drills
4. Protected Breakthrough Logistics
5. Catastrophic Shock Breakthrough

The track separates generic Chemical support from armored Chemical delivery by applying its formation modifiers only to `category_chemical_tank_support_companies`. Its mastery units are the light, medium, and heavy CBRN armored delivery detachments plus the independently gated nerve-suppression detachment.

Gas-Chamber Saturation Drills authorizes nerve-agent methods in existing extermination camps. Once Tabun, Sarin, or Soman has been researched, the camp can select the strongest matching stocked agent without a separate occupation law, readiness gate, mobile detachment, or special-project prerequisite. The method still consumes real cylinders through the shared chemical pipeline and records deaths, contamination, medical pressure, resistance trauma, evidence, attribution, and Condemnation.

The mastery multiplies nerve-agent killing efficiency by 2.25, reduces activation and monthly payload consumption to 45 percent of standard, reduces generated evidence to 55 percent of standard, and adds agent-scaled resistance suppression. It does not create camp infrastructure.

## Explicitly absent infrastructure

Toxic Armored Warfare grants no Concentration occupation law, camp, extermination site, experiment site, genocide system, restricted Chemical site, or concealment mechanism. The migration effects clear the obsolete `concentration_occupation_law_unlocked` flag rather than restoring it. Existing extermination camps receive the Gas-Chamber Saturation Drills method only after the mastery and a nerve-agent technology are present; doctrine never creates or reveals those systems.

## Runtime art

`GFX_doctrine_chemical_suppression_medium` is registered in `interface/cbrn_doctrine.gfx` and uses the final dedicated Toxic Armored Warfare icon at `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds`.

The full doctrine and officer-corps asset package, source PNGs, processed PNGs, contact sheets, validation inventory, and manifests are under `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/`. No placeholder or cross-type substitute is retained for this track.

## Relevant files

- Doctrine track: `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt`
- Doctrine gates: `common/scripted_triggers/cbrn_doctrine_triggers.txt`
- Doctrine state and migration: `common/scripted_effects/cbrn_doctrine_effects.txt`
- Nerve-suppression authorization: `common/scripted_triggers/cbrn_occupation_triggers.txt`
- Nerve-suppression operation: `common/scripted_effects/cbrn_occupation_effects.txt`
- Player-facing doctrine text: `localisation/english/chaosx_doctrines_l_english.yml`
- Final doctrine art wiring: `interface/cbrn_doctrine.gfx`

## Engine limit

The legacy mobile occupation operation remains fail-closed because the current confirmed hook does not provide exact target-loss, weather, and terrain receipts. It is not the gameplay implementation of nerve suppression. The supported route is the Gas-Chamber Saturation Drills mastery, which uses the existing selected-camp transaction as its exact target and release receipt and therefore needs no estimator or proxy casualty formula.
