# Event 012 Africa Created-Country Naval/Air OOB Audit Handoff

Date: 2026-06-17
Mode: country package subagent, audit with tiny safe patch permission

This is an audit handoff only. It is not a completion claim for Event 012 Africa, the created-country package suite, or the wider Africa implementation.

## Scope Audited

- Country history registrations for MAG, EAC, IOC, TDM, CRR, WAC, CBC, ANW, OVN, NHR, and SLC.
- Naval OOBs for MAG, EAC, IOC, TDM, CRR, WAC, CBC, ANW, and OVN:
  - `*_1936_naval_mtg.txt`
  - `*_1936_naval_legacy.txt`
- Air OOBs for MAG, IOC, OVN, NHR, and SLC:
  - `*_1936_air_bba.txt`
  - `*_1936_air_legacy.txt`

## References Used

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Unit modding, Equipment modding, Technology modding, State modding, and Map modding.
- Vanilla documentation:
  - `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Vanilla examples:
  - `~/projects/Hearts of Iron IV/history/units/ITA_1936_naval_mtg.txt`
  - `~/projects/Hearts of Iron IV/history/units/FRA_1936_air_bba.txt`
  - `~/projects/Hearts of Iron IV/history/countries/ENG - Britain.txt`
  - `~/projects/Hearts of Iron IV/history/units/SAF_1936_air_bba.txt`
  - `~/projects/Hearts of Iron IV/history/units/IRQ_1936_air_bba.txt`

## Patch Made

Changed file:

- `history/countries/NHR - Nile-Horn League.txt`

Changed identifier:

- Replaced invalid technology token `mountain_infantry = 1` with vanilla technology id `tech_mountaineers = 1`.

Before behavior:

- NHR history attempted to set `mountain_infantry`, which does not exist as a technology id in current vanilla or mod technology files.

After behavior:

- NHR starts with the valid mountaineer technology unlock used by vanilla country histories and the local mod pattern.

Why this was safe and bounded:

- It is a one-token correction in a listed file.
- The intended behavior was already clear from the Nile-Horn geography/theme and the stale token name.
- Vanilla `common/technologies/infantry.txt` defines `tech_mountaineers`; vanilla country histories use that id.

## Country Package Coverage Checklist

- MAG: naval registration present; air registration present; MTG variant present; legacy naval OOB present; BBA/legacy air OOB present.
- EAC: naval registration present; MTG variant present; legacy naval OOB present.
- IOC: naval registration present; air registration present; MTG variant present; legacy naval OOB present; BBA/legacy air OOB present.
- TDM: naval registration present; MTG variant present; legacy naval OOB present.
- CRR: naval registration present; MTG variant present; legacy naval OOB present.
- WAC: naval registration present; MTG variant present; legacy naval OOB present.
- CBC: naval registration present; MTG variant present; legacy naval OOB present.
- ANW: naval registration present; MTG variant present; legacy naval OOB present.
- OVN: naval registration present; air registration present; MTG variant present; legacy naval OOB present; BBA/legacy air OOB present.
- NHR: air registration present; BBA/legacy air OOB present; invalid mountaineer technology token patched.
- SLC: air registration present; BBA/legacy air OOB present.

Full country package surfaces outside navy/air OOB registration and directly adjacent history tokens were not audited in this tranche.

## File Surface Checklist

- All 11 listed country history files exist.
- All 18 listed naval OOB files exist for MAG/EAC/IOC/TDM/CRR/WAC/CBC/ANW/OVN.
- All 10 listed air OOB files exist for MAG/IOC/OVN/NHR/SLC.
- No scoped file has nonzero brace balance.
- No scoped file contains unsupported comparison-operator tokens.
- No scoped country history has unresolved technology ids after the NHR patch.
- No scoped MTG naval OOB references a missing country-created ship variant.
- No scoped ship variant module token failed resolution against vanilla module ids.

## Missing Or Stale Country Package Surfaces

No missing scoped OOB files or stale scoped OOB registrations were found.

Out of scope for this tranche and not completion-certified here:

- Tag registration, flags, localisation, advisors, focus-tree assignment, AI strategy, release logic, state ownership, production, and broader country-package playability.

## Map And State Setup Issues

No naval-base placement issue found in the scoped OOBs.

Validated naval placements:

- MAG: province 7132, state 459 Western Algeria, naval base level 6, 2 destroyer/cutter ships.
- EAC: province 2196, state 546 Tanganyika, naval base level 2, 1 destroyer/cutter ship.
- IOC: province 5222, state 543 Madagascar, naval base level 1, 1 destroyer/cutter ship.
- TDM: province 5210, state 905 Mombasa, naval base level 2, 1 destroyer/cutter ship.
- CRR: province 12975, state 772 Middle Congo, naval base level 1, 1 destroyer/cutter ship.
- WAC: province 2050, state 558 Nigeria, naval base level 3, 1 destroyer/cutter ship.
- CBC: province 10968, state 295 Congo, naval base level 1, 1 destroyer/cutter ship.
- ANW: province 10803, state 779 Ivory Coast, naval base level 1, 1 destroyer/cutter ship.
- OVN: province 6039, state 773 Cameroon, naval base level 1, 1 destroyer/cutter ship.

No airbase placement issue found in the scoped OOBs.

Validated air placements:

- MAG: state 459 Western Algeria has an airbase; 24 BBA/legacy fighters.
- IOC: state 543 Madagascar has an airbase; 12 BBA/legacy fighters.
- OVN: state 773 Cameroon has an airbase; 12 BBA/legacy fighters.
- NHR: state 271 Ethiopia has an airbase; 18 BBA/legacy fighters.
- SLC: state 275 South Africa has an airbase; 20 BBA/legacy fighters.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

No tranche-specific politics, leader, portrait, flag, advisor, or party issue was found while auditing the listed history files for OOB registration and directly adjacent load tokens.

This was not a full politics/leader/asset audit.

## Focus, Decision, Idea, And Asset Issues

No focus, decision, idea, or asset issue was found in the scoped OOB files.

This tranche did not audit focus trees, decisions, ideas, sprite manifests, or localisation coverage beyond checking that the OOB and history tokens needed for naval/air loading resolve.

## Starting Military, Technology, Industry, Supply, And Production Issues

Patched:

- `history/countries/NHR - Nile-Horn League.txt`: stale `mountain_infantry` technology id corrected to `tech_mountaineers`.

No remaining scoped naval/air OOB token issue found:

- MTG naval OOBs use `ship_hull_light_1` and per-country `version_name` values defined in the same country history under the MTG branch.
- Legacy naval OOBs use `destroyer_1`, which resolves in vanilla equipment.
- BBA air OOBs use `small_plane_airframe_0`, `creator = "ENG"`, and `version_name = "Hawker Fury"`, matching vanilla patterns for Commonwealth/minor inherited aircraft such as SAF/IRQ and ENG's created `Hawker Fury` variant.
- Legacy air OOBs use `fighter_equipment_0`, which resolves in vanilla equipment.

Industry, supply, and production were not broadly audited in this tranche.

## AI And Playability Issues

No OOB-specific AI blocker found.

Balance/theme read:

- Naval packages are intentionally light coastal patrols: one destroyer/cutter for most tags, two for MAG.
- Air packages are small inherited interwar fighter groups: 12 to 24 aircraft.
- This fits minor created-country/littoral-authority identity and does not appear to create a major balance spike.

Route AI, focus AI, reinforcement behavior, and long-term playability were not audited here.

## Meaningful Validation Evidence

One-off parser checks over the 39 scoped files reported:

- `missing []`
- `brace_nonzero []`
- `unsupported_compare []`
- `bad_tech []` after patching NHR
- `variant_match` empty for MAG, EAC, IOC, TDM, CRR, WAC, CBC, ANW, and OVN
- `bad_modules []`
- `bad_naval_places []`
- `bad_air_places []`
- Naval ship counts: MAG 2; EAC/IOC/TDM/CRR/WAC/CBC/ANW/OVN 1 each.
- BBA air counts: MAG 24; IOC 12; OVN 12; NHR 18; SLC 20.

Manual reference checks:

- `set_naval_oob` and `set_air_oob` are valid country-history effects per vanilla documentation.
- Offline Country creation wiki confirms MTG/BBA split OOB pattern.
- Offline Country creation and Division modding wiki confirm `creator` selects the creator country for equipment variants and defaults to owner only when omitted.
- Vanilla ENG creates `Hawker Fury`; vanilla SAF/IRQ/NZL/GRE-style air OOBs use `creator = "ENG"` for inherited aircraft.

## Skipped Meaningful Validation

- No full game launch or error-log validation was run; this was a bounded repository audit and patch pass.
- No broad country-package audit was performed beyond the listed files and OOB-adjacent token checks.

## Remaining Risks

- The OOBs assume the created tags receive or retain control of the referenced state/province at runtime. This audit verified the vanilla map/state placements, not every Event 012 release/control path.
- The BBA inherited-aircraft pattern depends on ENG's `Hawker Fury` variant being available in the loaded game setup. Vanilla supports this pattern, but a total-conversion or later override of ENG history could affect it.
- Wider country package surfaces remain outside this handoff: localisation, flags, portraits, advisors, AI strategy, focus loading, production, reinforcement paths, and release cleanup.
