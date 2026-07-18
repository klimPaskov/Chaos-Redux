# Event 019 Localisation Specialist Final Re-audit

> Its former two-branch claimant creation description is superseded on 2026-07-16 by `019_male_claimant_identity_correction_handoff_2026_07_16.md`. Technical `portrait` tokens remain correct, but their fixed Event 019 sprites now display regional army/muster identity scenes rather than people; current visual evidence is `019_full_portrait_regeneration_handoff_2026_07_16.md`. The body below remains historical localisation/interface audit evidence and is not current claimant creation or visual metadata.

Date: 2026-07-16

Mode: current-source, audit-only re-audit. This subagent did not edit gameplay,
localisation, scripted localisation, GUI, GFX, assets, registries, skills, or
spreadsheets. The only file created by this subagent is this handoff. No files
were staged and no commit was created.

## Final verdict

The final Event 019 English player-facing contract passes the requested
re-audit. The current open severity counts are exact:

| Priority | Open count |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

Two defects were found against the live source during the audit. The parent
agent corrected both while this audit was active, and both fixes passed the
end-state sweep:

| ID | Priority | Finding | Final state |
| --- | --- | --- | --- |
| `L10N-FINAL-019-01` | P1 | Visible report `chaosx.nr19.917` used undefined structural sprite token `GFX_report_event_infantry_spawn_claimant`. The claimant DDS was registered under `GFX_report_event_infantry_spawn_evolution_iii`. | Closed. `events/019_infantry_spawn.txt:682` now uses the registered claimant-report sprite. All 11 unique Event 019 event-picture references resolve. |
| `L10N-FINAL-019-02` | P2 | `infantry_spawn_derivative_become_the_regional_predator_tt` contained two em dashes, contrary to the Event 019 writing contract. | Closed. `localisation/english/019_infrantry_spawn_l_english.yml:941` now uses a parenthetical while preserving all requirements. The final main file contains zero em dashes and zero semicolons. |

Observed findings were P0: 0, P1: 1, and P2: 1. Both observed findings are
closed, which yields the final open counts of zero at every priority.

## Latest claimant identity contract

### Exact selectors and neutral invalid state

`common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
contains exact, gap-free mappings for all twenty profiles:

| Selector | Exact rows | Mismatches | Invalid-context result |
| --- | ---: | ---: | --- |
| `GetInfantrySpawnClaimantPortraitSprite` | 20 | 0 | `GFX_portrait_unknown` |
| `GetInfantrySpawnSelectedClaimantPortraitSprite` | 20 | 0 | `GFX_portrait_unknown` |
| `GetInfantrySpawnSelectedClaimantProfileTitle` | 20 | 0 | `infantry_spawn_claimant_profile_unrecorded` |
| `GetInfantrySpawnSelectedClaimantProfileDescription` | 20 | 0 | `infantry_spawn_claimant_profile_unrecorded_desc` |

The two name selectors each retain all eighty profile and name-variant pairs.
Their invalid result is `infantry_spawn_claimant_name_unrecorded`. The trait
selector's invalid result is the empty `infantry_spawn_claimant_traits_none`
value. No invalid context resolves to profile 01, a Quartermaster trait, or any
other live claimant identity.

The neutral player-facing defaults are:

- `infantry_spawn_claimant_name_unrecorded`: `Unnamed Muster Claimant`
- `infantry_spawn_claimant_profile_unrecorded`: `No Claimant File`
- `infantry_spawn_claimant_profile_unrecorded_desc`: `No verified private command identity is selected.`
- `GFX_portrait_unknown`, which is registered by vanilla in
  `interface/_leader_portraits.gfx`

These are defensive invalid-context display values, not substitutes for missing
claimant content. Every valid profile has its own exact title, description,
name set, and portrait.

### Runtime consumption

`infantry_spawn_load_claimant_localisation_context` clears all visible claimant
variables before loading a row and only loads a row when the claimant ledgers
are aligned and the selected index is in range. This prevents a stale claimant
identity from leaking into reports or the Muster Board.

The Muster Board consumes the exact profile text through
`infantry_spawn_muster_gui_claimant_identity`:

```text
[This.GetInfantrySpawnSelectedClaimantProfileTitle]
[This.GetInfantrySpawnSelectedClaimantProfileDescription]
```

The claimant portrait object has three matching pieces:

- `interface/019_infantry_spawn_muster_board.gui:196` declares
  `infantry_spawn_muster_claimant_portrait` with neutral
  `GFX_portrait_unknown` initialization.
- `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:162-166`
  shows it only for a valid selected claimant with a profile in the supported
  range.
- The same scripted GUI's `properties` block at line 231 assigns image
  `[GetInfantrySpawnSelectedClaimantPortraitSprite]` to that exact GUI object.

The object name, visibility trigger, and dynamic property identifier are
structural GUI identifiers. They are not English localisation keys.

### Commander portrait injection

`infantry_spawn_create_current_claimant_commander` copies the selected profile
and name variant to normal meta variables, then injects
`[This.GetInfantrySpawnClaimantPortraitSprite]` as `PORTRAIT` in both the female
and male `meta_effect` branches. Each generated `create_corps_commander` block
uses `picture = [PORTRAIT]`, and the meta variables are cleared after creation.

The offline Effects reference lists `picture`, `portrait_path`, and `gfx` as
accepted commander portrait inputs. The meta-effect form follows existing
Chaos Redux dynamic commander creation and vanilla meta-effect token injection
structure. All twenty returned claimant GFX tokens are registered in
`interface/019_infantry_spawn.gfx`, every referenced DDS exists, and the neutral
unknown token resolves in vanilla.

### Regional and diaspora wording

The corrected profile wording matches the live regional gates and source matrix:

- profile 04 describes a South or Southeast Asian commander also found among
  Australasian diaspora communities
- profile 12 describes an East or Southeast Asian commander including the
  Australasian diaspora
- profile 20 describes an Australasian commander and remains Australia-only in
  the regional trigger

The titles, descriptions, selectors, portrait rows, name pools, and regional
matrix therefore describe the same valid identity set.

## Localisation and display coverage

### File integrity

| File | Keys | Unique | Duplicate or malformed rows | UTF-8 BOM |
| --- | ---: | ---: | ---: | --- |
| `localisation/english/019_infrantry_spawn_l_english.yml` | 2,726 | 2,726 | 0 | present |
| `localisation/english/chaosx_achievements_l_english.yml` | 574 | 574 | 0 | present |
| `localisation/english/chaosx_gui_l_english.yml` | 883 | 883 | 0 | present |
| `localisation/english/chaosx_chaos_meter_l_english.yml` | 368 | 368 | 0 | present |
| `localisation/english/chaosx_event_names_l_english.yml` | 101 | 101 | 0 | present |

The main file also has zero `:0` keys and zero leading key indentation. Across
the five audited files, 380 unique `$KEY$` aliases resolve with zero missing.

### Scripted localisation

| File | `defined_text` blocks | Valid `localization_key` fields | Invalid `localisation_key` fields | Unique targets | Missing English targets |
| --- | ---: | ---: | ---: | ---: | ---: |
| `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt` | 16 | 315 | 0 | 209 | 0 |
| `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt` | 6 | 24 | 0 | 16 | 0 |

The main selector file has 21 unique `GFX_*` targets. Those are structural sprite
tokens deliberately returned to meta effects and GUI image properties, not YML
keys. The remaining 188 targets are genuine localisation keys and all resolve.
Neither Event 019 scripted-localisation file contains direct section or icon
formatting characters.

### Explicit and implicit references

A field-aware sweep across 62 Event 019 and shared integration files found 635
unique player-facing references from event titles, descriptions, options,
tooltips, custom effect and trigger tooltips, cost text, GUI text, button text,
and GUI tooltips. Missing references: 0.

The final implicit display-pair audit is:

| Surface | Identifiers | Required display keys | Missing |
| --- | ---: | ---: | ---: |
| Decisions and missions | 77 | 154 | 0 |
| Decision categories | 3 | 6 | 0 |
| Derivative focuses | 45 | 90 | 0 |
| Ideas | 67 | 134 | 0 |
| Achievements | 11 | 22 | 0 |

The 77 decision-category children remain exactly 64 decisions and 13 missions.
All explicit decision, mission, focus, event, and achievement condition or
effect tooltips used by the source resolve. Each Event 019 achievement also has
its condition tooltip and shared eligibility text.

### Events, Event Log, and Event Details

- `events/019_infantry_spawn.txt` contains 30 visible and 4 hidden events.
- `events/019_infantry_spawn_scenario.txt` contains 3 visible and 3 hidden
  events.
- Every visible event has a title, description, at least one named option, and
  resolved localisation.
- Event 019 contributes 40 unique localisation targets to the shared Event Log
  and Event Details selectors, with zero missing.
- The four evolution titles are `Organized Muster`, `Arsenal Lottery`, `Command
  Fracture`, and `Anomalous Muster`. Each title is selected in all four shared
  title contexts, and each body is selected in the evolution detail context.
- All 14 Event 019 history payloads have title and description selectors.
- `chaosx.event_name.19` and
  `chaosx.events_log.window.event_details.infantry_spawn` resolve.
- The debug, settings, and Event Log name selectors all route Event ID 19 to
  `chaosx.event_name.19`.

### Muster Board

The interface contains 125 unique player-facing text, button, and tooltip
references, with zero missing. The same file contains 98 structural GUI object
names and 10 structural sprite references. Structural names were not counted as
missing localisation. The five tabs, selection states, empty states, accounting
rows, claimant identity, family names, action buttons, costs, lock reasons, and
animation controls all resolve.

### SCN-013

- `triggerable_scenario_id.infantry_spawn` is exactly `13`.
- `chaosx.scenarios.entry.id.infantry_spawn` is exactly `#013`.
- The shared scenario selectors use 18 unique Event 019 targets, with zero
  missing.
- The direct confirmation, setup-complete, and setup-failed reports resolve.
- Four type names and descriptions, four intensity names and descriptions,
  launch status text, and the two generated leader names resolve.
- Event 006's scenario identity was not edited or treated as an Event 019 key.

### Cosmetic identities and visible assets

The cosmetic matrix remains complete:

- 13 identity stems by 7 regions equals 91 regional cosmetic tags
- 1,365 required regional country-name keys, zero missing
- 13 unsuffixed compatibility identities and 195 required keys, zero missing
- 273 regional flag TGAs across large, medium, and small sizes, zero missing

Structural visible-asset checks also pass:

| Surface | Unique references or required files | Missing |
| --- | ---: | ---: |
| Event report pictures | 11 | 0 |
| Decision and category icons | 51 | 0 |
| Focus icons | 45 | 0 |
| Idea icons | 9 | 0 |
| Achievement icon states | 33 | 0 |
| Unique textures referenced by `interface/019_infantry_spawn.gfx` | 154 | 0 |
| Claimant portrait sprites | 20 | 0 |

GFX names, texture paths, GUI object names, property names, animation names,
cosmetic tag tokens, and raw meta-effect tokens are structural identifiers.
They were checked against GFX definitions, files, or consuming script instead of
being misclassified as missing English keys.

## Registry ownership invariant

The final filename sweep found exactly one dedicated Event 019 registry file:

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

Its current SHA-256 during this audit was
`F5582496605395431EF38AF798D6C56D05DD2CF91B7CF8C89D57A42F87C3D90A`.
The file was inspected only and was not modified by this subagent. Shared
`chaos_unit_family_registry_*` integration files are shared providers, not
additional dedicated Event 019 registry files.

## Representative commands and evidence

The audit used direct `rg`, PowerShell source parsing, and file-existence checks.
Representative checks included:

```powershell
rg -n "GetInfantrySpawnClaimantPortraitSprite|GetInfantrySpawnSelectedClaimantPortraitSprite|GetInfantrySpawnSelectedClaimantProfile" common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt
rg -n "meta_effect|PORTRAIT|create_corps_commander" common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt
rg -n "claimant_portrait_visible|properties|GetInfantrySpawnSelectedClaimantPortraitSprite" common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt
rg -n "profile_(04|12|20)|Australasia|diaspora" localisation/english/019_infrantry_spawn_l_english.yml docs/specs/019_infantry_spawn_specs
rg --files common | rg -i "(019_infantry_spawn.*registry|event19_registry)"
```

The PowerShell audits parsed YML keys, all five BOM byte prefixes, scripted
localisation targets, explicit localisation-bearing fields, implicit display
pairs, GUI text fields, GFX definitions, texture paths, achievement icon states,
country-name matrices, and flag files. Their end-state results are recorded in
the tables above.

The read-only HOI4 MCP event lint was also attempted. It could not create its
artifact because the server returned `ARTIFACT_STORAGE_LIMIT`. This did not
change source and did not block the direct source, wiki, vanilla-reference, or
file-resolution audits.

## Files inspected

### Repository guidance and source-of-truth documents

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Event 019 specs and review documents under
  `docs/specs/019_infantry_spawn_specs/`
- prior Event 019 localisation, claimant, asset-remediation, registry, and
  decision audit handoffs under
  `docs/plans/019_infantry_spawn_plans/subagent_handoffs/`

### Runtime sources

- both `events/019_infantry_spawn*.txt` files
- all `common/decisions/019_infantry_spawn*.txt` files and their three category
  files
- `common/national_focus/019_infantry_spawn_derivative_focus.txt`
- both `common/ideas/019_infantry_spawn*.txt` files
- the Event 019 section of `common/achievements/chaos_redux_achievements.txt`
- all Event 019 scripted effects, scripted triggers, script constants,
  on-actions, and AI strategy files used by the explicit-reference sweep
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
- `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt`
- `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt`
- `interface/019_infantry_spawn_muster_board.gui`
- `interface/019_infantry_spawn.gfx`
- the shared Event Log, Event Details, debug-name, settings-name, and triggerable
  scenario effects, triggers, scripted localisation, GUI, constants, and event
  files that contain Event 019 branches
- the five English localisation files listed in the integrity table
- claimant DDS files, achievement DDS files, and regional flag TGAs through
  exact path-resolution checks

### Offline engine references and vanilla precedents

The required offline wiki pages consulted were Data structures, Triggers,
Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision
modding, Idea modding, AI modding, Interface Modding, Scripted GUI Modding,
National focus modding, Country creation, Achievement modding, and Portrait
modding.

Vanilla documentation consulted included
`documentation/script_concept_documentation.md`,
`documentation/loc_formatter_documentation.md`,
`documentation/loc_objects_documentation.md`, and the relevant
`effects_documentation.md` and `triggers_documentation.md` sections. Vanilla
precedents included dynamic scripted-GUI image properties, scripted
localisation returning GFX tokens, meta-effect token injection, commander
portrait fields, and the registered unknown portrait.

## Remaining blockers and risks

Two global Event 019 completion blockers remain. They are not localisation
severity findings:

- `B-019-001`: the engine exposes no documented exact division-scoped ownership
  transfer for a natural loyal-formation derivative release. The unapproved
  recreate-prove-delete substitute remains unimplemented.
- `B-019-002`: the available callbacks do not atomically prove the exact Event
  019 division, same-battle victory, duration, enemy-strength ratio, and
  casualty tuple. The four affected achievements remain hidden and fail closed.

The four hidden achievements are `One Battalion Wonder`, `Combined-Arms
Accident`, `Borrowed Future`, and `Barracks of Babel`. Their names,
descriptions, condition tooltips, and icon states are complete despite the
gameplay blocker.

The only validation limitation was the MCP artifact-storage condition described
above. No unresolved player-facing English, scripted-localisation, GUI-property,
GFX, icon, cosmetic-identity, Event Log, Event Details, or SCN-013 defect remains
in the audited current source.

## Simplifications, omissions, skills, and Git

No localisation surface in the assigned runtime contract was simplified or
omitted. No placeholder identity, profile-01 invalid default, global portrait
substitute, missing icon substitute, gameplay fallback, or weaker text contract
was accepted.

Skills used:

- `chaos-redux-subagents`
- `chaos-redux-events`

No reusable skill gap was discovered, so no skill was created or updated. No
files were staged and no commit was created. The parent owns final integration,
diff review, staging, and the meaningful plan commit.
