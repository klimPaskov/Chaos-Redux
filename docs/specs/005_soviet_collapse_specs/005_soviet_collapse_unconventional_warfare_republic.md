# Unconventional Warfare Republic

## Overview

The Unconventional Warfare Republic is a high-chaos Soviet Collapse successor centered on the Tver biological warfare facility. It appears only through the high-chaos successor path, when Soviet collapse pressure is deep enough and the Tver facility state is still held by the Soviet Union, or when a force-all high-chaos scenario explicitly requests every high-chaos successor.

The country is led by Ivan Mikhailovich Velikanov and is built around forbidden biological, chemical, and zombie special-project warfare. It starts with an extreme high-chaos force package, a biowarfare/chemical national spirit, broad payload access, blacksite facilities, and an aggressive AI posture against the Soviet Union and nearby countries.

## Runtime Flow

1. `can_soviet_collapse_spawn_uwr` checks the high-chaos successor gate, tag existence, collapse pressure, depot vulnerability, and state 247 biowarfare facility ownership/control.
2. `soviet_collapse_spawn_uwr_if_enabled` cores and transfers state 247 to `UWR`.
3. `soviet_collapse_setup_uwr_successor` loads `UWR_soviet_collapse_focus_tree`, grants the experimental warfare idea, initial manpower, biowarfare and chemical facilities, an experiment camp, heavy biological and chemical payload stockpiles, advanced gas technology, starting breakthroughs, and random chaos special-project unlocks.
4. The high-chaos evolution log records stage `unconventional_warfare_stage` and fires `chaosx.nr5_custom.43`.

## Focus Tree

The UWR focus tree is a fourteen-focus compact specialist tree. It has:

- a founding research focus that grants the country identity idea, biowarfare and chemical breakthrough progress, and random chaos special-project unlocks
- a biological facility branch
- a chemical facility branch
- an experimentation camp merge point
- a zombie-weapon branch
- a field-release doctrine branch that expands stockpiles, prepares deliberate CBRN operations, and supports expansion
- a containment and quarantine branch that unlocks exact-state prisoner intake and captured-blacksite aftermath policy
- a last-resort command branch that strengthens deliberate native release preparation without fabricating a release
- a final chaos warfare focus that combines special-project rolls, assault columns, reserves, claims, and neighbor conflict pressure without automatically releasing a biological agent

## Reusable Special-Project Helper

`grant_random_chaos_special_project_available_tech` is the central registry for experimental CBRN project rewards. It rolls one not-yet-owned biological, chemical, Black Plague weaponization, or zombie project and applies that project's native completion output. Every future Chaos Redux special project must be reviewed when added: eligible CBRN projects enter this helper with their exact project/output mapping, while intentional exclusions are documented in `common/scripted_effects/cbrn_scripted_effects.md`. Shared output technologies do not replace project-specific completion gates.

Documented helper file:

- `common/scripted_effects/cbrn_scripted_effects.md`

## Assets

Registered idea sprite:

- sprite name: `GFX_idea_uwr_experimental_warfare_republic`
- gfx file: `interface/005_soviet_collapse_uwr_kmb_icons.gfx`
- final texture: `gfx/interface/ideas/005_soviet_collapse/005_uwr_experimental_warfare_republic.dds`

Country flags:

- `gfx/flags/UWR.tga`
- `gfx/flags/UWR_communism.tga`
- `gfx/flags/UWR_democratic.tga`
- `gfx/flags/UWR_fascism.tga`
- `gfx/flags/UWR_neutrality.tga`
- matching `medium/` and `small/` files

The five final ideology-aware UWR flag designs are installed at normal, medium, and small sizes. Their source PNGs, processed previews, contact sheet, hashes, and exact handoff are recorded under `docs/assets/005_soviet_collapse/uwr_final_flags/`.

## Completed Follow-Up Package (2026-08-09)

- `uwr_overclock_blacksite_network` and `uwr_expand_experiment_camp_registry` provide the facility-overclocking surface.
- `uwr_authorize_field_release_raids` prepares deliberate native exact-state CBRN operations but cannot fabricate an actor, victim, payload, route, result, or target state.
- `uwr_intake_prisoner_transports` is a state-targeted intake action restricted to valid UWR-controlled blacksite states.
- Successful native biological raid, battlefield, or sabotage release paths mark the exact UWR actor and exact target state for the Event 005 aftermath ledger.
- A foreign controller of a captured UWR aftermath site chooses exactly one of dismantlement, secure containment, or exploitation. The Event 005 marker clears after the choice while any active native biological episode remains owned by the native CBRN system.
- Route-aware AI priorities cover the research, facility, camp, field-release, containment, and chaos-warfare milestones.
- Final UWR flags, focus icons, decision icons, and the identity-idea icon have dedicated registered assets and manifests.

## Implemented shared-crisis hooks (2026-07-11)

UWR now has route AI overlays without adding focus nodes. After the Tver directorate, CW facility, or experiment-camp milestones, it prioritizes army, infantry, and support production; Field Release Doctrine or Chaos Warfare raises army commitment and force concentration. These overlays use the successor decision surface so terminal collapse does not switch the route off.

The retired `soviet_collapse_uwr_contaminate_neighbor_front` hook is not part of the accepted CBRN design. Focus completion cannot choose a random neighboring state, fabricate a biological release, or bypass exact payload, actor, victim, route, result, and target-state authority. UWR battlefield and strategic releases use the native exact-state raid routes and the shared ordinary-pathogen lifecycle. Older implementation handoffs that describe automatic focus contamination are superseded by this source-of-truth rule.
- Review `grant_random_chaos_special_project_available_tech` whenever any Chaos Redux special project is implemented; add eligible CBRN projects and document intentional exclusions.
