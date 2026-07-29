# Toxic Armored Warfare compatibility note

## Source of truth

This file documents the legacy `chemical_suppression` compatibility identifier. The complete accepted doctrine design and current implementation are documented in `docs/systems/chaos_warfare_doctrine.md`.

The player-facing track is Toxic Armored Warfare. Its implementation is in `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt`, with shared gates and state changes in the CBRN doctrine trigger and effect files.

## Current mastery progression

The five mastery rewards are:

1. Sealed Crew Compartments
2. Armored Agent Delivery
3. Mobile Nerve Suppression
4. Protected Breakthrough Logistics
5. Catastrophic Shock Breakthrough

The track separates generic Chemical support from armored Chemical delivery by applying its formation modifiers only to `category_chemical_tank_support_companies`. Its mastery units are the light, medium, and heavy CBRN armored delivery detachments plus the independently gated nerve-suppression detachment.

Mobile Nerve Suppression grants only a doctrine eligibility flag. It does not release an agent and does not waive the separate project, protection, occupation-policy, readiness, stock, state, condition, or consequence requirements. A valid later suppression operation must consume equipment and record deaths, contamination, resistance trauma, evidence, attribution, and severe diplomatic consequences.

## Explicitly absent infrastructure

Toxic Armored Warfare grants no Concentration occupation law, camp, extermination site, experiment site, genocide system, restricted Chemical site, or concealment mechanism. The migration effects clear the obsolete `concentration_occupation_law_unlocked` flag rather than restoring it. Independent camp mechanics can receive the accepted Terminal Hazard killing-efficiency multiplier only after their own infrastructure, ownership, and authorization already exist; doctrine never creates or reveals those systems.

## Runtime art

`GFX_doctrine_chemical_suppression_medium` is registered in `interface/cbrn_doctrine.gfx` and uses the final dedicated Toxic Armored Warfare icon at `gfx/interface/doctrines/icons/stage_5_chaos_warfare/doctrine_toxic_armored_warfare.dds`.

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

The exact state transaction for nerve-agent suppression remains fail-closed because the current confirmed hook does not provide the required target-loss, weather, and terrain receipts. No decision-click approximation, proxy casualty formula, or hidden periodic fallback is retained.
