# Localisation Cleanup Baseline, 2026-08-22

## Status and constraints

This is a read-only baseline audit of shared player-facing systems and Events 1 through 20. Event 21 and later content was inspected only where its keys participate in shared selectors, settings, event-log details, scenarios, registries, or shared documentation.

No localisation, scripted localisation, event, gameplay, GFX, spreadsheet, or GUI source file was changed. This report is the only file written by this pass.

The interface constraint is absolute for this cleanup. Event-log details, selectors, content strings, and scripted-localisation helpers remain valid localisation cleanup surfaces. No recommendation in this report requires edits to `interface/*.gui`, layout, coordinates, click regions, or other visual interface structure.

## Required references and method

The audit followed `AGENTS.md`, the repository cleanup master prompt, `chaos-redux-events`, and `chaos-redux-subagents`. It consulted the offline `Localisation - Hearts of Iron 4 Wiki.md` and `Data structures - Hearts of Iron 4 Wiki.md` pages, together with the installed vanilla `documentation/loc_formatter_documentation.md` and the relevant scope and localisation-object entries in `documentation/loc_objects_documentation.md`.

The English localisation scan covered 288 YAML files and 59,659 unique case-insensitive mod keys. It checked direct event title, description, option, tooltip, scripted-localisation, GFX token, GUI consumer, shared registry, documentation, and vanilla-localisation references before classifying a key as missing or potentially dead.

## MCP evidence and exact blockers

The shared event scan completed partially and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e05dcea8e484ae2361b840cdf538c0b1c90efbfc72f9195b0d1900b6f9350cf/f3bad11e08c76d03cba8d6d07e8ebbccb9003a3a84983e9e878e27aa8aeaf925/event-scan-bc0062fc8506.json` with result code `EVENT_INSPECTED_PARTIAL`.

A narrow namespace inspection using `{ kind = namespace, namespace = chaosx.nr1 }` failed with `timed out awaiting tools/call after 180s`. Per-event render evidence therefore remains unavailable for this baseline.

Read-only inspection of the shared `events_log_popup_window` failed with `ARTIFACT_STORAGE_LIMIT` after the server attempted the inspection and returned no artifact. Visual overflow and rendered missing-localisation validation are therefore blocked. Source review is not treated as equivalent rendered evidence. No GUI rewrite was requested, attempted, or recommended.

## Executive findings

1. One definite shared event-log wrapper key is missing. `fallout.event_log.clean_certificate.detail` is returned by the shared selector, while `GetFalloutEvent719EventLogDetail` and every branch it can return already exist.
2. Event 1 uses the raw option key `OK` eight times, but neither the mod nor installed vanilla English localisation defines uppercase `OK`.
3. There are 30 case-insensitive duplicate keys. Twenty-eight come from one fully redundant Event 5 localisation file. One is an Event 16 duplicate. One is the previously unresolved `ZIN` versus `zin` collision.
4. Shared settings and debug selectors contain three replicated event-name tables covering IDs 1 through 1000, while only 130 event-name keys exist. There are 864 unresolved selector destinations. This is structural selector debt, not a reason to create 864 empty or generic localisation keys.
5. All 288 English YAML files have a UTF-8 BOM, a valid `l_english:` header, no versioned `:0` keys, and no malformed localisation rows.
6. Several shared Event Details descriptions are mechanical implementation summaries rather than concise situation and premise text. Event 10 is the most severe example. This needs a coordinated localisation and spreadsheet wording tranche without any GUI layout work.
7. The CBRN event-log detail formats civilian and military death counts with two decimal places. Counts should use an integer display, while genuine contamination, outbreak, evidence, and pressure values should retain fractional precision.

## Missing key list

### Definite missing keys

| Key | Consumer | Evidence | Recommended repair |
| --- | --- | --- | --- |
| `fallout.event_log.clean_certificate.detail` | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5767` | `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt:600` defines `GetFalloutEvent719EventLogDetail`, and `localisation/english/fallout_consolidated_l_english.yml:1626` onward defines all branch keys, but no base wrapper exists | Add `fallout.event_log.clean_certificate.detail: "[GetFalloutEvent719EventLogDetail]"` beside the other Clean Certificate event-log keys |
| `OK` | `events/001_communism_spread.txt:884`, `893`, `904`, `915`, `926`, `937`, `948`, and `959` | No mod or installed vanilla English key named uppercase `OK` exists | Prefer an established generic vanilla option key if its exact displayed text is suitable. Otherwise add a scoped Event 1 option key and replace these eight consumers |

### Excluded event-specific missing keys

The following are visible from shared files but belong to Event 79 or 80 standalone content and are outside this baseline patch scope: `chaosx.news.79.a`, `chaosx.news.80.t`, `chaosx.news.80.d`, and `chaosx.news.80.a`. In addition, `chaosx.news.79.t` and `chaosx.news.79.d` exist as empty values. Route these to the owner of those later events rather than repairing them in an Events 1 through 20 cleanup.

`POLITICS_NEVILLE_CHAMBERLAIN_DESC` appears as a quoted value in `_chaosx_easter_eggs.txt`. Its status is uncertain because the quoted token can be a literal or an engine database lookup rather than a direct localisation-key consumer. Do not add or remove a key without tracing the live consumer.

## Duplicate key list

### Safe duplicate-file retirement candidate

`localisation/english/005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml` contains exactly 28 definitions after its header, and all 28 collide with definitions in `localisation/english/005_soviet_collapse_l_english.yml`. The affected base keys are:

- `UWR_blacksite_command`
- `UWR_cold_chain_foundries`
- `UWR_registry_of_containment`
- `UWR_release_authority_commissions`
- `UWR_quarantine_corridor_protocols`
- `UWR_field_release_supply_chain`
- `UWR_directorate_of_last_resort`
- `KMB_subsoil_deepening_commission`
- `KMB_furnace_procurement_board`
- `KMB_treaty_corridor_guards`
- `KMB_oil_shale_convoy_pool`
- `KMB_golem_foundry_council`
- `KMB_basin_concession_court`
- `KMB_orefront_mobilization`

Each base key also has a duplicated `_desc` key, for 28 collisions total. Most display names are identical, but the descriptions differ. `UWR_blacksite_command` also differs as `Blacksite Command Charter` in the small file and `Blacksite Command` in the consolidated Event 5 file. Confirm the consolidated Event 5 wording as canonical, then retire the entire smaller file. Deleting individual duplicate rows would leave only a header and provides no benefit.

### Other duplicates

| Key | Locations | Classification |
| --- | --- | --- |
| `KRG_XENOBIOLOGICAL_ASCENDANCY` | `localisation/english/016_brilliant_scientist_country_l_english.yml:68` and `localisation/english/016_brilliant_scientist_focus_l_english.yml:87` | Identical text. Remove one definition after assigning the idea or country package a canonical localisation owner |
| `ZIN` and `zin` | `localisation/english/chaosx_countries_l_english.yml:29` and `localisation/english/chaosx_ideas_l_english.yml:101` | Case-insensitive collision. Defer because the lowercase idea ID is referenced by Event 68 gameplay and the uppercase country tag participates in shared classifications and Event 2 documentation |

## Scripted-localisation issue list

There are 2,983 `defined_text` names across the 50 in-scope scripted-localisation files and no duplicate helper names.

The definite broken chain is the missing `fallout.event_log.clean_certificate.detail` wrapper described above. Its helper and branch keys are internally complete.

Many unquoted `localization_key = GFX_*` results in Event 16, Event 19, and shared selector files are sprite tokens rather than visible localisation keys. They require matching `.gfx` consumer checks and must not be bulk-created as YAML keys.

Quoted `localization_key = "literal text"` values and dynamic expressions such as `[?variable]` are deliberate literal output. They must not be treated as unresolved key names by mechanical missing-key scans.

## Obsolete selectors and helper-consolidation opportunities

`common/scripted_localisation/chaosx_scripted_localisation_debug.txt` contains 1,000 event-name branches. `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` repeats nearly the same range in `GetSettingsEventName` and `GetLastEventName`, while `GetSelectedEventName` delegates to those helpers. Together these surfaces contain 2,998 branches for the 1 through 1000 range.

Only 130 `chaosx.event_name.*` keys exist. The current replicated selectors can resolve to 864 undefined destinations, including ID 100, 98 IDs from 101 through 199, 764 IDs from 200 through 999, and ID 1000.

Do not repair this by adding 864 generic names. The safe architecture is one canonical event-name selector contract with an explicit unknown fallback, plus only the registered numbered events and documented shared system IDs. This requires the scripted-system owner because settings variables, manual debug entry, event-log callers, and fallbacks must be migrated together.

`chaosx.event_name.635` through `.641` and `.991` are shared system log IDs rather than normal numbered events. They are intentional and must survive any consolidation.

## Dynamic text and integer-formatting opportunities

`localisation/english/chaosx_gui_l_english.yml:526` displays `cbrn_action_record_civilian_deaths_entries` and `cbrn_action_record_military_deaths_entries` with `|.2`. These are death counts and should display as whole numbers with `|0`, or through the repository's established human-readable death-count helper if large values need compact formatting.

The same string's contamination change, outbreak change, evidence quality, and repeat-use pressure values appear to be continuous values and should retain fractional precision. Attribution, retaliation, and first-use state values already use integer formatting. Do not mechanically change every `.2` formatter in the file.

The Event 19 request-cost profiles correctly use dynamic script constants. Their prose repeats the same administration calculation and settlement sentence across provider families. A future cleanup can keep the dynamic values while consolidating the shared administration clause into one helper and leaving only provider-specific settlement text in each branch.

## Dead-localisation candidates and uncertainty

The Event 5 custom splinter file is the only high-confidence whole-file retirement candidate because every definition collides with a consolidated definition and the file has no unique key.

No other key should be deleted from this baseline solely because a direct event-script reference was absent. Dynamic scripted localisation, GFX sprite tokens, GUI string references, meta text, saved event-log history, settings selectors, documentation, and spreadsheet consumers all create indirect references that a direct grep can miss.

The following empty values appear intentional and should be retained unless their callers are retired in the same change: `death_custodial_category_status_hidden`, `secret_alliance_objective_blank`, `africa_selected_action_no_additional_cost`, `natural_disaster.report.clause.empty`, Event 16 empty detail clauses, `infantry_spawn_claimant_traits_none`, chaos-meter `.none` values, `chaosx.scenarios.launch_status.ready`, event-log empty and enabled values, `chaosx.settings.export.empty`, and the Fallout no-deaths clause.

`chaosx_debug_loc` is empty and may be deliberate debug output. Confirm its live caller before deletion. The empty Event 79 news keys are later-event debt and are not intentionally approved by this audit.

## Events 21 and later shared references

Shared event-name localisation contains visible names for later numbered events, and shared debug and settings helpers select those names. Those keys are in scope only as registry destinations. Their standalone event prose, options, mechanics, and private localisation were not reviewed or approved.


Shared system IDs 635 through 641 and 991 are intentionally retained even though they are greater than 20 because the event log consumes them as nonstandard system records.

## Cross-surface and naming mismatches

The visible canonical names for Events 1 through 20 come from `localisation/english/chaosx_event_names_l_english.yml`. Several internal filenames and documentation slugs differ:

| Event | Visible name | Internal drift | Recommendation |
| --- | --- | --- | --- |
| 17 | A Faction Comes Calling | `017_join_faction_l_english.yml` and `017_random_faction` documentation | Preserve legacy namespaces for now. Use the visible name in shared player-facing labels |
| 18 | Resources Found | `018_random_resource_l_english.yml` | Preserve legacy filename. Use the visible name in shared labels |
| 19 | Soldiers from Nowhere | `019_infrantry_spawn_l_english.yml` contains the typo `infrantry`, while docs use `019_infantry_spawn` | Defer file and namespace rename because of broad reference risk. Do not propagate the typo into new keys or docs |
| 20 | The Black Plague | `020_black_death_l_english.yml` | Preserve the legacy namespace. Use The Black Plague for the numbered event and reserve Black Death for mechanic-specific text only where intended |

`chaosx.events_log.window.event_details.event_011_unavailable: "Event 011 is currently unavailable."` is implementation-status wording and conflicts with Event 11's dynamic visible identity as Secret Alliance. Replace it only after confirming whether the details surface can expose the event name and premise without revealing secret alliance participants early.

Spreadsheet and documentation mirrors must be updated in the same later prose tranche as Event Details. The workbook remains the only editable spreadsheet source, and the export-only CSV files must not be edited directly.

## File-encoding concerns

No current encoding defect was found. All 288 English YAML files begin with a UTF-8 BOM, use `l_english:` as the first meaningful line, avoid `:0`, and contain no malformed parsed rows.

The primary risk is regression during cleanup. Any file retirement, duplicate repair, or prose rewrite must preserve UTF-8 with BOM. Scripted-localisation `.txt` files do not use the YAML header rule.

## Prose-quality issue list

### Vagueness

`chaosx.events_log.window.event_details.evolution_entry_body_generic` says only that a milestone marks a shift in story or consequences. It gives the player no concrete event, action, or result. Prefer an event-specific body or a factual fallback explaining that no further record was captured.

`event_011_unavailable` reports implementation availability rather than the in-world situation. Its replacement must preserve the route's secrecy and must not reveal the alliance counterpart before the gameplay surface does.

### Bloat and hidden-mechanic explanation

`chaosx.events_log.window.event_details.death` is the strongest cleanup candidate. It is five dense paragraphs that enumerate population deletion, Deaths System recording, ownership, cores, buildings, modifiers, unit damage, soul-power conversion, spending categories, decisions, and victory conditions. Event Details should establish the island disappearance, the Black Ledger threat, and the living world's response. Exact costs and state effects belong in tooltips and mechanic-specific detail rows.

`chaosx.events_log.window.event_details.communism_spread` exposes exact daily ideology drift and internal state-tier behavior. The premise can describe organizers taking local control and the risk of uprising, while exact drift and intervention coverage remain in their tooltips.

`chaosx.events_log.window.event_details.zombie_outbreak` reads like strategy advice and engine explanation, including manpower-only divisions, immediate coring, outbreak weighting, and a checklist beginning with `If you want to keep the event under control`. Rewrite it as a concrete outbreak premise and move advice or exact mechanics to relevant tooltips.

`chaosx.events_log.window.event_details.fury` explains exclusion pools and target rules. It should describe the rogue war state and its escalating attacks, leaving eligibility filters to debug or tooltip surfaces.

`chaosx.events_log.window.event_details.white_peace` explains selection weight and repeated-firing suppression. Replace this with the diplomatic situation and the kind of wars that may close.

### Obvious explanation and repetition

Event 19's sustainment and request-cost keys repeat `ledger-backed` and `no separate stockpile debit` across sixteen player-facing strings. Consolidate the common sentence through one scripted helper or a shared clause while retaining provider identity and all dynamic cost tokens.

Several shared button tooltips repeat visible actions, such as opening a detail panel. These are low priority unless the tooltip can add a requirement or consequence. Do not change the button layout or consumer.

### Overcomplication

The CBRN action detail is a ten-line raw receipt with internal phrases such as `Military-death receipt`, `Attribution state`, and `Repeat-use pressure`. Preserve the recorded data, but use direct player-facing labels and whole-number formatting for deaths. If status integers map to meaningful states, route them through scripted localisation instead of exposing numeric codes.

Event 5 contains long administrative noun stacks such as commissions, authorities, ledgers, corridors, and procurement boards. Much of this register is route-appropriate. Review only passages where the action and consequence become unclear. Do not flatten Soviet-collapse factions into generic modern prose.

### Style-rule violations

No em dash was found in the selected player-facing corpus.

Twenty-four player-facing semicolons were found. Sixteen occur in Event 19 request and sustainment cost profiles. Others occur in Event 6 failure tooltips, Event 15 ledger or focus text, Event 16 outcome and Directorate strings, and one sourced Event 5 quotation attribution. The nonsourced strings are safe punctuation cleanup candidates when their wording tranche is opened. The sourced Event 5 quotation must not be changed.

## Sourced-quotation preservation notes

Quote-bearing super-event surfaces for Events 2, 3, 5, 6, 7, 10, 11, 12, and 13 were treated as attributed quotations. Their wording, spelling, punctuation, line breaks, and attribution are outside prose normalization.

In particular, `chaosx_super_event.11.q` contains a sourced contrast construction that would otherwise trigger the style scan. Preserve it verbatim. `chaosx_super_event.17.q` contains the attribution `International Working Men's Association, General Rules (1864; revised 1871)`. Preserve the semicolon and the rest of that quotation verbatim.

No quotation is proposed for deletion or stylistic rewriting.

## Safe bounded patches

These repairs are narrow enough for an owner-applied cleanup tranche after this baseline:

1. Add the missing `fallout.event_log.clean_certificate.detail` wrapper beside the existing Clean Certificate event-log strings.
2. Replace the eight raw Event 1 `OK` consumers with one confirmed existing generic key or one scoped Event 1 option key.
3. Confirm the consolidated Event 5 definitions as canonical and retire `005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml` as a whole.
4. Remove one identical `KRG_XENOBIOLOGICAL_ASCENDANCY` definition after selecting a canonical owner file.
5. Change only the two CBRN death-count formatters from two decimals to integer display. Leave genuinely fractional values unchanged.
6. Replace nonsourced semicolons in the opened Event 6, 15, 16, and 19 wording sets while preserving meaning and all dynamic tokens.

Each patch must be followed by reference-aware localisation validation. Event and shared GUI consumers should also receive the mandatory read-only MCP inspection when the artifact storage blocker is cleared. No patch requires or authorizes interface layout edits.

## Dynamic-reference uncertainty

Do not delete unresolved-looking keys that can be reached by a `defined_text` result, a variable-composed selector, a `GFX_*` token, meta text, a saved event-log record, a shared scenario registry, or a spreadsheet/documentation mirror.

The manual event-name selectors accept IDs that are not presently registered. Some may be developer placeholders and some may be obsolete. Their status cannot be decided from direct key references alone.

The failure of per-event and GUI MCP evidence leaves rendered overflow, fallback order, and some live selection paths unverified. This uncertainty must carry into the cleanup tranche.

## Deferred migrations

1. Consolidate the three replicated event-name tables into one canonical selector and fallback contract with the scripted-system owner.
2. Resolve `ZIN` versus `zin` through an idea-ID migration or an explicitly supported ownership decision. This crosses Event 68 and is not a bounded Events 1 through 20 repair.
3. Rename legacy Event 17 through 20 files or namespaces only through a reference-complete migration. The Event 19 `infrantry` typo is real, but a filename-only correction would break consumers.
4. Rewrite the shared Event Details premise text and mirror the accepted wording into the event-catalog workbook and exports. Keep all interface files read-only.
5. Convert numeric CBRN status codes to meaningful scripted-localisation labels if the underlying values and fallback semantics are confirmed.
6. Route Event 79 and 80 missing or empty news keys to their event owners.

## Validation limitations and unresolved decisions

The baseline provides source, key, encoding, dynamic-reference, GFX-token, documentation, and partial MCP event evidence. It does not provide successful per-event renders or GUI overflow screenshots because the event query timed out and GUI artifact creation reached the server storage limit.

The canonical wording choice for the 28 Event 5 duplicates remains an owner decision because the descriptions differ even when most names match.

The correct generic replacement for Event 1's `OK` remains an owner decision until the intended option tone is checked against its eight event contexts.

No gameplay or display behavior was changed. No simplification or fallback was implemented. No source quotation or dynamic token was altered.
