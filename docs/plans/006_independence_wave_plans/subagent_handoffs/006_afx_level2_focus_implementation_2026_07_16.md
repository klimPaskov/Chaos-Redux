# Event 006 AFX Level 2 implementation handoff

Date: 2026-07-16

Scope: exact package `IW-006`, Wallonia (`AFX`)

Design authority: `docs/specs/006_independence_wave_specs/`

## Outcome

Wallonia has a package-specific Level 2 lane layered over the shared full Independence Wave tree. The lane connects the Sambre-Meuse continuity crisis to government selection, defense, former-host succession, the informal network, a paid Meuse conference, and `FORM-03` preparation. The package also has three generation-local country incidents: one at founding, one after government installation, and one after the paid Meuse conference.

No package attestation, automatic-release wrapper, scenario preflight, tag reservation, country identity, force mapping, free unit, equipment award, or Political Power store was added by this tranche. `IW-006` remains fail-closed until its unique visual package and a fresh independent package audit pass.

## Files changed

- `common/script_constants/006_independence_wave_wallonia_frisia_constants.txt`
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt`
- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `events/006_independence_wave_wallonia_frisia.txt`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`
- this handoff

No AGX package gameplay was changed.

## Focus lane

The exact AFX branch occupies authored column 93 and rows 1 through 8:

1. `independence_wave_afx_charter_sambre_meuse_authority_focus`
2. `independence_wave_afx_bind_mines_rails_furnaces_focus`
3. `independence_wave_afx_codify_basin_government_focus`
4. `independence_wave_afx_integrate_industrial_reserve_focus`
5. `independence_wave_afx_settle_industrial_succession_focus`
6. `independence_wave_afx_open_meuse_network_office_focus`
7. `independence_wave_afx_mandate_meuse_conference_focus`
8. `independence_wave_afx_prepare_low_countries_dossier_focus`

The root uses `allow_branch = { is_independence_wave_afx_package = yes }`; every node has an exact package-aware `available` block, a centralized duration, a final name, description and effect tooltip, and state-aware AI weighting.

The lane deliberately retains the existing paid decision layer. The network office requires live network membership. The conference mandate authorizes but does not complete `independence_wave_afx_convene_meuse_industrial_conference`; that project still consumes the shared strategic payment and its full duration. The Low Countries dossier requires the conference to have completed and opens discovery without replacing `FORM-03` consent, route, territory, charter, or mutation checks.

## Rewards and costs

- The authority and industrial-integration steps raise the visible Industrial Continuity value and the shared country ledgers through existing centralized helpers.
- Mines, rails, and furnaces add one anchor-state Infrastructure and one 50 percent Industry research bonus.
- The Industrial Reserve grants 15 Army Experience and 15 Command Power, but no formations or stockpiles.
- Government codification applies a real route-dependent cost: constitutional and popular settlements lose 5 percent War Support; emergency and patron settlements lose 5 percent Stability. Their country-ledger gains differ by route.
- Industrial succession requires the paid former-host ledger settlement while a former host survives. Ratification costs 5 percent War Support; an extinct host takes the separate orphaned-ledger resolution.
- Network and formable preparation alter the visible network, league, ambition, and country ledgers through shared helpers rather than static checklist flags alone.

The new AFX tuning fields are centralized in `independence_wave_nwe_package_duration.afx_incident_delay` and `independence_wave_nwe_package_focus`.

## Country incidents

| Event | Schedule point | Player-facing choice |
| --- | --- | --- |
| `chaosx.nr6.18` | prepared founding setup | municipal warrant review or binding dispatch authority |
| `chaosx.nr6.19` | installation of any accepted AFX government | published quotas and appeals or government quota command |
| `chaosx.nr6.20` | completion of the paid Meuse conference | confederal mandate or binding industrial directorate |

Each scheduler sets a generation-local scheduled flag, loads the one-day delay constant into a temporary variable, and passes that variable to `country_event days`. Each event trigger requires the exact package plus its own scheduled and unresolved state. Every option sets a distinct outcome flag and all six visible ledger deltas before calling `independence_wave_apply_afx_incident_deltas`.

The prepared setup proof now requires the founding incident to be scheduled. Cleanup clears every new focus, authorization, delegation, scheduled, resolved, and outcome flag. No incident uses `fire_only_once`, creates forces, supplies equipment, or bypasses a paid package/formable transaction.

## Decision integration

`independence_wave_afx_convene_meuse_industrial_conference` now becomes visible only after the Level 2 mandate and the existing full conference foundation both hold. Its complete path schedules `chaosx.nr6.20`. Its existing strategic payment, 300-day duration, capital-control cancellation, and project-failure consequences remain authoritative.

## AI behavior

- Continuity recovery is urgent below the stable threshold.
- Severe former-host threat increases reserve and security priorities.
- Constitutional and popular governments prefer public review and the confederal mandate.
- Emergency and patron governments prefer quota command and the binding-directorate mandate.
- Development Compact membership favors the Meuse/Low Countries diplomatic lane.
- AI faces the same route, host, network, project-cost, conference, and formable gates as the player.

## Visual handoff

The focus file reserves eight package-specific base sprites:

- `GFX_goal_independence_wave_afx_sambre_meuse_authority`
- `GFX_goal_independence_wave_afx_mines_rails_furnaces`
- `GFX_goal_independence_wave_afx_basin_government`
- `GFX_goal_independence_wave_afx_industrial_reserve`
- `GFX_goal_independence_wave_afx_industrial_succession`
- `GFX_goal_independence_wave_afx_meuse_network_office`
- `GFX_goal_independence_wave_afx_meuse_conference`
- `GFX_goal_independence_wave_afx_low_countries_delegation`

The incidents reserve three report sprites:

- `GFX_report_event_006_afx_industrial_authority`
- `GFX_report_event_006_afx_basin_government`
- `GFX_report_event_006_afx_meuse_ambition`

The required source, processed, DDS, contact-sheet, prompt, manifest, validation, and handoff package is owned under `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/`. The main agent owns `interface/006_independence_wave_wallonia_frisia_assets.gfx` and final consumer wiring.

## Validation and completion boundary

Static implementation review found:

- balanced blocks across all seven gameplay/localisation files;
- eight unique AFX focus IDs;
- one definition and one scheduler for each of `.18`, `.19`, and `.20`;
- English localisation with a UTF-8 BOM and no duplicate keys;
- no direct script constant passed to `country_event days`;
- no new free-unit, stockpile, or Political Power reward; and
- no new package-readiness, registry, scenario, or allocation mutation.

Read-only HOI4 focus and event inspection was attempted but returned `ARTIFACT_STORAGE_LIMIT`; no MCP artifact is claimed. Fresh independent focus, decision, incident, setup, cleanup, AI, asset, identity, host-survival, Event 5 collision, and admission review remains mandatory before `IW-006` can enter automatic or SCN-008 selection.

## Simplifications, omissions, and blockers

- The gameplay lane, incidents, localisation, AI weighting, lifecycle cleanup, and paid conference integration are implemented without a fallback.
- Final visual assets and sprite registration were still in production when this handoff was written.
- Automatic and scenario admission intentionally remain closed pending the visual handoff and fresh independent audit.
