# Event 014 localisation and secrecy audit

Date: 2026-08-24

Mode: read-only audit. No gameplay, localisation, workbook, GUI, asset, or generated export was edited because concurrent Event 014 work is active.

## Outcome

Event 014 has complete implicit English key coverage across the audited gameplay families, and the dedicated localisation file satisfies the repository's UTF-8 BOM and key-syntax rules. The audit nevertheless found one critical runtime secrecy defect and one critical documentation secrecy defect:

- The public Event Details world-end catalog exposes `Lecter` before `cannibalism_reveal_complete`.
- The always-readable event catalog workbook exposes `Hannibal Lecter` in Evolution III and `Lecter` in both world-end descriptions.

These are completion blockers under the package's absolute pre-reveal secrecy requirement.

## References and evidence boundaries

The audit applied `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `xlsx`. It consulted the required offline wiki pages, including Localisation, Data structures, Triggers, Effects, Modifiers, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI Modding, National focus modding, Technology modding, and Achievement modding. It also consulted vanilla `documentation/loc_formatter_documentation.md` and `documentation/loc_objects_documentation.md` and compared vanilla localisation/scripted-localisation conventions.

The HOI4 MCP event trace completed partially for `chaosx.nr14.1` and linked the authoritative full artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc4b25e4ffd0de5768c2ebc44e081257f5ee890254fdf320ad73d813096a9c76/2c89cd441daf8589e0a482656bcd26f36f1e09bf535115a6d9d3ce3f3fde5958/event-trace-4de24027e9ca.json`. The response was `EVENT_INSPECTED_PARTIAL`, scanned 359 sources, and linked the complete evidence because the graph contained 9,513 events.

The following mandatory MCP routes were unavailable and source review is not treated as equivalent visual or engine evidence:

- `hoi4.focus_inspect` for the Event 014 focus file timed out after 180 seconds while awaiting `tools/call`; no focus render artifact was produced.
- `hoi4.tech_inspect` for `cannibalism_scavenger_warband_tech` did not return after 60 seconds and was terminated; no technology render artifact was produced. The installed package has no Technology Tree Viewer.
- `hoi4.gui_inspect` rejected each of `cannibalism_early_network_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window` with `windowName and scenario must be provided together`. A manifest-discovery call then failed to return and was terminated. No GUI render or overflow artifact was produced.

Consequently, source locations, key coverage, text length, and visibility gates were audited for those surfaces, but visual overflow remains unproven.

## Missing key list

No confirmed missing English key was found.

Automated implicit-pair coverage found:

- 264 Event 014 focus identifiers with both name and description keys.
- 127 decision or mission identifiers and 13 decision-category identifiers with both name and description keys.
- 37 idea identifiers with name and description keys.
- 9 custom unit identifiers with name and description keys.
- 9 activation-technology identifiers with name and description keys.
- 18 achievement identifiers with name and description keys.
- Complete base, `_DEF`, `_ADJ`, and ideology name/adjective variants for `CBA` through `CBH` and `CBL`.

Explicit Event 014 event, GUI, event-log, evolution, event-detail, super-event, scenario, country-selector, and achievement-tracker localisation references inspected in source resolve to defined keys. This result does not eliminate the MCP visual blockers above.

## Duplicate key list

No duplicate Event 014 or Hannibal-related English key definition was found across `localisation/english/`.

## Scripted localisation issues

### Critical: public Event Details world-end rows reveal Lecter

Consumers:

- `common/scripted_effects/chaosx_events_log_effects.txt:1180-1204` registers `world_is_the_larder` and `no_thaw_will_come` as public world-end rows without a `cannibalism_reveal_complete` visibility condition.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:12830-12831`, `:12886-12887`, and `:12944-12945` select their title and detail keys solely from the world-end registry identifiers.
- `localisation/english/chaosx_gui_l_english.yml:551` begins with `Lecter's host`.
- `localisation/english/chaosx_gui_l_english.yml:553` begins with `Lecter's winter host`.

Severity: critical. These catalog rows are available before the reveal flag even though their names and descriptions are terminal-route reference data.

Recommended fix: keep the public catalog useful but permanently anonymize its descriptions. The actual post-reveal super-events can continue naming Hannibal.

Recommended replacement for `chaosx.events_log.world_end.world_is_the_larder.details`:

> The unified Host has pulled the feeding territories and armed kitchens into one command. Roads, farms, prisons, and conquered cities are all treated as parts of the same larder. Surviving countries are reduced to prey, raiders, or small resistance enclaves.\n\nThe network has no reason to hide anymore. Every government still standing faces an expanding Host that intends to feed on the whole world.

Recommended replacement for `chaosx.events_log.world_end.no_thaw_will_come.details`:

> The Winter Host has given itself to the Wendigo hunger. Feeding grounds spread with the cold, and conquered communities are dragged into a world where thaw, harvest, and mercy are treated as weaknesses.\n\nWinter advances with the Host. Every surviving country is hunted until human rule is consumed or driven into a handful of frozen refuges.

An alternative is to split each row into pre-reveal and post-reveal detail keys guarded by `cannibalism_reveal_complete`, but permanent anonymization is simpler and avoids a default-branch leak.

### Correct guarded selectors

No Hannibal leak was found in the following selectors:

- Event Details uses the concealed Event 014 detail before `cannibalism_reveal_complete` and the revealed detail after it in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6464-6475`.
- Evolution III title and body selectors require `cannibalism_reveal_complete`; Evolutions I and II remain generic.
- `CBA` through `CBH` country names and adjectives use `GetCannibalismWarlordCountryName` and `GetCannibalismWarlordAdjective`, not Hannibal's identity.
- Super-event title, body, quote, remark, image, and sound mappings are keyed to post-reveal Event 014 super-event IDs. No Event 014 text is used as an unguarded fallback.

## Dynamic text opportunities

- If the Event Details world-end descriptions are not permanently anonymized, add dedicated concealed/revealed scripted-localisation getters and make the concealed key the final fallback. Never put the named version in a default branch.
- Preserve the existing dynamic country, actor, timer, cost, pressure, and state tokens. The audit found no static actor or state name that should replace an already-available dynamic token.
- `cannibalism_achievement_tracker_read_only_tt` can describe availability dynamically rather than narrating automation. Recommended text: `Objectives appear here when their public conditions are known.`

## Cross-surface mismatches and secrecy notes

### Critical: workbook spoilers

Consumer: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events` row for Event 014.

- Cell `F15` exposes `Hannibal Lecter steps into public view...` even though a workbook has no runtime reveal flag.
- Cell `I15` repeats both public Event Details descriptions that begin with `Lecter's host` and `Lecter's winter host`.

Severity: critical for the requested spreadsheet-facing secrecy standard.

Recommended `F15` replacement:

> A concealed command steps into public view and begins drawing the mature network into one campaign.

Recommended `I15` replacement: retain the existing world-end titles and replace both descriptions with the anonymized Event Details text recommended above. After editing the workbook through the `xlsx` workflow, run `.tools/export_event_catalog_csv.py`; do not edit the generated CSV directly.

### Consistent surfaces

- The Event 014 row's starting detail and Evolutions I-II match the concealed in-game event-detail wording.
- Scenario `SCN-010`, `The Hunger Lines`, describes discipline collapse, ritual cells, silent islands, warlord states, and convergence without naming Hannibal.
- Pre-reveal focus trees and their localisation contain no Hannibal reference. The unified and Wendigo trees require `cannibalism_reveal_complete` at tree availability and root access.
- Direct GUI source gates the early/network/warlord windows to the concealed phase and the revealed/Wendigo command windows to `cannibalism_reveal_complete` or later state. Named titles and portraits occur only in the latter windows.
- All actual Event 014 achievements are `hidden = yes`. Tracker entries whose names or descriptions refer to Hannibal are gated to reveal or later progression; pre-reveal tracker copy remains generic.
- Units, activation technologies, ideas, country display names, focus names, decision names, scenario labels, and achievement names inspected before reveal do not identify Hannibal.
- Portrait and audio source filenames contain `hannibal`, but no pre-reveal player-facing key, tooltip, sprite label, sound label, scenario label, or GUI title exposes those filenames as metadata. Runtime visibility remains subject to the GUI MCP blocker above.

## File encoding concerns

No encoding concern was found in `localisation/english/014_cannibalism_l_english.yml`: it starts with UTF-8 BOM bytes `EF BB BF`, begins with `l_english:`, uses unversioned `key: "Text"` syntax, has no leading-space key definitions, and has no `:0` definitions. The audited Event 014 scripted-localisation files contain no direct `§` or `£` formatting characters.

## Prose-quality issues and replacement recommendations

The main Event 014 narrative text is concrete, route-specific, and readable. The weak passages are concentrated in late-route mechanical tooltips that read like implementation or anti-exploit notes.

### Vagueness

- `localisation/english/014_cannibalism_l_english.yml:1985`, `cannibalism_liberate_feeding_state_effect_tt`: `the established liberation-recovery sequence` is abstract and `exact active node` is implementation language. Recommended: `Retires the selected active node and begins the state's liberation recovery.`

### Bloat

- `:2065`, `cannibalism_wendigo_press_terminal_hunt_desc`, buries the effect under six exclusions. Recommended: `Spend another field package against [cannibalism_wendigo_terminal_hunt_target.GetName] to add [?constant:cannibalism_wendigo_terminal_hunt.press_pressure|0] Hunt Pressure.`
- `:2080`, `cannibalism_activate_inherited_winter_cell_desc`, carries a seven-item exclusion list. Recommended: `Activate an inherited foreign cell inside [FROM.GetName] for [?constant:cannibalism_wendigo_inherited_cell.duration_days|0] days. The cell disrupts planning, organization, and supply. If [FROM.GetName] is the active terminal-hunt target, it also adds [?constant:cannibalism_wendigo_inherited_cell.hunt_pressure|0] Hunt Pressure once.`

### Obvious explanation

- `:145`, `cannibalism_achievement_tracker_read_only_tt`, explains that a read-only tracker is read-only and automatic. Recommended: `Objectives appear here when their public conditions are known.`
- `:2062`, `cannibalism_wendigo_terminal_hunt_mission_effect_tt`, ends with `Neither outcome creates free formations.` The mission's two numeric consequences are already complete. Recommended: `Success adds [?constant:cannibalism_wendigo_terminal_hunt.success_progress|0] transformation progress. Failure removes [?constant:cannibalism_wendigo_terminal_hunt.failure_progress|0] transformation progress.`

### Repetition

- `:2057`, `cannibalism_wendigo_launch_terminal_hunt_effect_tt`, repeats the package-wide `no free` assurance. Recommended: `Begins a [?constant:cannibalism_wendigo_terminal_hunt.mission_days|0]-day terminal hunt against [FROM.GetName] with [?constant:cannibalism_wendigo_terminal_hunt.starting_pressure|0] Hunt Pressure.`
- `:619`, `cannibalism_synchronize_warlord_attack_effect_tt`, repeats the partner availability condition after stating that both warlords pay. Recommended: `Both warlords pay the full cost, gain Network Alignment, and receive Synchronized Warlord Attack for at least [?constant:cannibalism_warlord_decision.synchronized_operation_days|0] days. Courier, commune, road, and convergence contracts can extend the operation.`

### Overcomplication

- The inherited-cell and terminal-hunt passages above combine their actual consequence with lists of systems they do not touch. Split the actual timed effect and conditional pressure consequence into direct sentences; omit unrelated exclusions unless a specific nearby control would otherwise mislead the player.

### Writing-style violations

- `exact`, `established sequence`, `complete cost`, and repeated `does not create` lists expose implementation and tuning concerns in player-facing prose. The replacements above preserve every actor, dynamic value, timer, cost, target, and gameplay consequence that the player needs.
- No em dash, sentence semicolon, staged contrast formula, prompt fragment, or attributed-quote normalization issue was found in the Event 014 localisation set.

## Sourced-quotation preservation notes

The following super-event quote strings are sourced, public-domain quotations and must remain verbatim, including their historical capitalization and punctuation:

- `chaosx_super_event.49.q`: Thomas Hobbes, *Leviathan*.
- `chaosx_super_event.50.q`: William Shakespeare, *King Lear*.
- `chaosx_super_event.52.q`: Walt Whitman, *Specimen Days*.
- `chaosx_super_event.53.q`: Lord Byron, *Darkness*.

The wording and source confidence are documented in `docs/plans/014_cannibalism_plans/014_super_event_text_research.md`. None of the recommended fixes changes a quote, attribution, formatting code, or dynamic token.

## Recommended fix order

1. Remove the two named Event Details world-end leaks in `localisation/english/chaosx_gui_l_english.yml` or implement concealed/revealed selectors in the registry and scripted localisation.
2. Replace the Event 014 workbook spoilers in `F15` and `I15`, then regenerate the three catalog CSV exports from the workbook.
3. Apply the bounded tooltip rewrites above in `localisation/english/014_cannibalism_l_english.yml` while preserving all dynamic tokens.
4. Re-run GUI inspect/render with an accepted Event 014 scenario manifest, focus inspect/render, and technology inspect/render. Review normal, long-text, and missing-localisation states at supported resolutions before claiming visual completion.

## Simplifications, omissions, and blockers

No audit surface was intentionally omitted. Visual overflow and engine-backed focus/technology/GUI evidence remain blocked by the exact MCP failures recorded above. No fallback was used and no source file was changed.
