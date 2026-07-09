# Current implementation map

This map records what the uploaded current-implementation notes say exists. The coding agent must verify each item against the actual repository files before patching.

## Chain identity

The path is a Germany gameplay chain, not a normal random-event pool entry. The namespace is `germany_mengele.*` and the primary event file is documented as `events/germany_mengele.txt`.

The chain starts when fascist Germany controls Auschwitz after 1940.06.13. The Auschwitz node is Kielce state `88`, province `9412`.

## Core layers

| Layer | Current-source description | Completion concern |
| --- | --- | --- |
| Auschwitz Experiments authorization | `germany_mengele.1` offers full authorization, restriction, or shutdown. | Verify trigger, option effects, timer expiry, closure effects, and localisation. |
| Report chain | `germany_mengele.10` through `.14` handle reports, autonomy, SS archive control, deaths, chaos, and condemnation memory. | Verify pacing, event visibility, death calls, flags, and no placeholder text. |
| Facility demands | `germany_mengele.17` can add `biowarfare_facility` in controlled priority states. | Verify state preference order, cooldown, cost, AI, and special-project unlock behavior. |
| Coup monitor | `germany_mengele.20` recalculates coup pressure and can start the Angel of Death civil war. | Verify pressure formula, 1943 and Soviet-war gates, facility count, fascist support, and hidden cleanup. |
| Emergency laboratory revolt | `germany_mengele.22` can trigger from enemy capture of Auschwitz-linked or biofacility states. | Verify state-control hook, invader war flow, loyalist war delay through `.38`, and duplicate prevention. |
| Cloning project | `sp_mengele_cloning` can unlock through proposal or registry and trigger `.24` if completed during the active program. | Verify project visibility, project completion effects, dynamic manpower, and coup handoff. |
| Final Solution decisions | `germany_final_solution_category` tracks racial policy, SS archive control, Ahnenerbe influence, foreign awareness, and aryan-origin preparation. | Verify category visibility, phase cleanup, AI, costs, and player tooltips. |
| Tibet Expedition | `prepare_tibet_mission` starts `.40` with scientific, covert SS, or Holy Realm contact routes. | Verify expedition cancellation, result flags, Holy Realm integration, and no text treating Nazi claims as true. |
| Clone army tree | `mengele_clone_army_focus_tree` supports the Directorate after consolidation, conventional expansion, and world-order network branch. | Verify focus load, branch locks, non-linear depth, AI, assets, localisation, and tests. |
| Hidden clone network | `.120` and `.121` create foreign host offers and hidden facility markers. | Verify target selection, acceptance weights, refusal paths, cleanup, client creation, and final reveal. |
| World-end path | `MCL_the_numbered_world` launches `Angelic World Order`, with `Aryan Supremacy` title variant. | Verify world-end threshold, ranking checks, network requirements, super-event, client regimes, and wars. |

## Permission scale

`mengele_permission_level` links the chain to the genocide crisis system.

| Value | Meaning |
| ---: | --- |
| 0 | Rejected or closed program. |
| 1 | Restricted camp administration. |
| 2 | Limited experimental authority from record classification. |
| 3 | Full Auschwitz Experiments authorization. |
| 4 | SS laboratories bypassing state and military oversight. |

Higher permission must increase deaths, hidden atrocity score, discovery condemnation, coup pressure, and Directorate laboratory-unit scale where applicable.

## Deaths, condemnation, and chaos

The path records experiment deaths through `chaos_meter_register_deaths` in Auschwitz state scope. Report deaths use hidden autonomy, facility count, permission level, and an Auschwitz bonus, then clamp to a cap. Coup deaths use `chaos_meter_register_state_civilian_deaths_percent` in Auschwitz and facility states.

The path has dedicated chaos history reasons for authorization, reports, coup, purge, truce, victory, world order, Tibet claim, and Tibet scandal.

Condemnation uses the chemical and biological condemnation variable and diplomatic consequence effect. It must follow the genocide-crisis rule that hidden internal damage can accumulate before foreign condemnation becomes public through discovery or other concrete evidence.

## Super-event and asset status from current source

The current notes name these presentation assets:

- `GFX_super_event_angel_directorate` in `interface/chaosx_super_events.gfx`.
- `gfx/super_events/003_holy_realm/super_event_angel_directorate.dds`.
- Super-event slot and audio ID `12`.
- `music/003_holy_realm/super_event_12_angel_directorate.ogg`.
- `chaosx_super_event_angel_directorate_track`.
- `sound/003_holy_realm/super_event_12_angel_directorate.wav`.
- Audio source notes in `docs/super_events/super_event_audio_packages.md`.

The current notes also say the registered Angel Directorate super-event image currently contains default super-event art. The finish pass must replace it with final art or document that a new final file already exists in the repo.

The later world-order assets include `GFX_super_event_angelic_world_order` and generated symbolic art documented under `docs/assets/mengele_clone_world_order/manifest.md`. Verify this package separately from the Angel Directorate reveal.
