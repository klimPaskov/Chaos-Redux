# Event 006 localisation audit, round 2

Date: 2026-08-24

## Scope and authority

This audit compares the current Event 006 English localisation and scripted-localisation sources with the seven accepted specification parts, the current source-of-truth map, current gameplay identifiers, and the shared Event Log selectors that consume Event 006 text.

The accepted specs explicitly classify their names as working labels rather than final localisation. Current YAML and current script identifiers therefore take precedence when checking implemented display coverage. Historical handoffs are evidence of earlier work, not current parser paths.

No gameplay, GUI layout, scripted-localisation logic, spreadsheet, or broad prose set was changed. One Event Log evolution-summary key received a bounded clarity rewrite.

## Current-source audit results

### Missing key list

None found in the audited current-source surfaces.

- Seventy-three `006_independence_wave*_l_english.yml` files contain 8,756 parsed keys, including 675 existing keys with leading indentation.
- The current Event 006 event, decision, focus, idea, character, achievement, and scripted-GUI files supplied 2,509 likely player-facing `title`, `desc`, `name`, `custom_effect_tooltip`, `custom_trigger_tooltip`, and `tooltip` references. All resolved to localisation keys present somewhere in the current localisation tree.
- All `localization_key` targets in the nine current Event 006 scripted-localisation files resolve to current YAML keys.

This is a static identifier and source-location result. It is not runtime parser or rendered GUI evidence.

### Duplicate key list

None found among the 8,756 Event 006 YAML keys.

No Event 006 YAML key uses a `:0` version suffix.

### Scripted-localisation issue list

No live identifier defect was found.

- Nine current Event 006 scripted-localisation files define 58 unique `defined_text` names.
- No duplicate Event 006 `defined_text` name was found.
- No Event 006 YAML call matching `[GetIndependenceWave*]` lacks a definition.
- No current scripted-localisation branch points to a missing YAML target.
- `GetEventsLogSelectedEvolutionSummary` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` still selects `independence_wave.evolution.summary` for `constant:independence_wave_evolution.evolution_type`.

The four paths removed by the 2026-08-24 scripted-localisation merge are referenced only by its historical merge handoff. Current sources and current event documentation do not still load or cite those removed parser files:

- `common/scripted_localisation/006_independence_wave_crisis_localisation.txt`
- `common/scripted_localisation/006_independence_wave_decision_cost_localisation.txt`
- `common/scripted_localisation/006_independence_wave_decision_scripted_localisation.txt`
- `common/scripted_localisation/006_independence_wave_rival_bloc_scripted_localisation.txt`

Their ten selectors now live in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

### Dynamic text opportunities

No missing dynamic value justified a safe patch in this round.

- The public `chaosx.nr6.2.d` report already reads the committed country count, region count, armed-country count, host concentration, and pre-existing network through variables and scripted localisation.
- The Event Details text uses script constants for the Join threshold and minimum state loss.
- The patched evolution summary contains no numeric, actor, state, timer, route, or cost value that should become dynamic.
- Several repeated package descriptions could become more country-specific, but doing so safely requires package-by-package identity review and is outside this bounded patch.

### Cross-surface mismatch notes

Current implemented wording agrees on the principal Event 006 premise:

- `chaosx.nr6.2.d` presents a committed wave of governments taking capitals, ministries, and borders.
- `chaosx.events_log.window.event_details.independence_wave` presents the same statehood, former-host, recognition, administration, defense, patron, and Join conditions.
- The current exported Event 006 catalog row mirrors that Event Details text.
- The accepted Part 2 and catalog-alignment direction require the public report to be the first visible Event 006 indication. No current Event 006 YAML contains working-label, placeholder, implementation-history, rework-history, package-ID, adapter, or fail-closed wording.

Current event documentation still contains stale parser paths created by later registry merges. These are current documentation defects, not live localisation or gameplay references:

- `docs/events/006_independence_wave/altai_package.md:49` cites the removed Altai category file.
- `docs/events/006_independence_wave/form39_melanesian_federation.md:25` cites the removed FORM-39 category file.
- `docs/events/006_independence_wave/systems/iw005_flanders_overlay.md:120` cites the removed IW-005 category file.
- `docs/events/006_independence_wave/karelia_crimea_packages.md:46` cites the removed Karelia/Crimea category file.
- `docs/events/006_independence_wave/northern_western_europe_packages.md:1022` cites the removed Saar category file.
- `docs/events/006_independence_wave/systems/triggerable_scenario.md:68` cites the removed scenario category file.
- `docs/events/006_independence_wave/transcaucasus_packages_and_form16.md:25` cites the removed Transcaucasus category file.

Those category identifiers now live in `common/decisions/categories/006_independence_wave_categories.txt`.

`docs/events/006_independence_wave/systems/iw005_flanders_overlay.md:38` and `:119` also cite the removed `common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt`; its unique callback is now in `common/on_actions/006_independence_wave_on_actions_registry.txt`.

Wildcard documentation references and missing vanilla/reference paths were not classified as registry-merge defects.

### File encoding concerns

All 73 Event 006 English YAML files have an `EF BB BF` UTF-8 BOM and an `l_english:` header. The patched file retained its BOM.

The eight ownership-sensitive Event 006 scripted-localisation `.txt` files left outside the new consolidated registry remain plain UTF-8 without BOM, as recorded by the merge handoff. The consolidated registry has a BOM. Scripted-localisation parser files are Clausewitz script rather than YAML language databases, so no encoding-only rewrite was made without a demonstrated parser need.

There are 675 leading-indented Event 006 YAML key lines, concentrated in existing files such as `006_independence_wave_gui_l_english.yml`. This conflicts with the repository's no-leading-space localisation style, although the static key parser still found and resolved them. It is a broad pre-existing formatting surface and was not mass-normalized in this bounded round.

## Prose-quality issue list

### Vagueness

`independence_wave.evolution.summary` used an abstract process construction, “A stage ... has taken hold, reshaping,” instead of stating what changed. This was the one bounded patch.

Several shared status texts remain abstract but mechanically meaningful, including “Founding phase,” “Network standing,” and “Patron capture.” Their adjacent dynamic values and panels provide context, so they were not changed without a GUI render.

### Bloat

`chaosx.nr6.2.d` is 774 source characters and combines the opening report, five dynamic clauses, the governance problem, and an interpretive closing sentence. It still matches the accepted public-summary direction, so shortening it would be a larger narrative choice than this task authorizes.

Two hundred forty-two Event 006 localisation values exceed 420 source characters. Most are dynamic decision-category ledgers or exact effect disclosures rather than prose alone. Representative review candidates include `independence_wave_ice_north_atlantic_category_desc`, `independence_wave_rut_network_effect_tt`, and `independence_wave_mnt_host_ledgers_effect_tt`. They should be reviewed with their rendered consumers before any shortening because they carry variables, constants, costs, or consequences.

### Obvious explanation

Several GUI button tooltips narrate the visible action without adding much context, including `independence_wave_status_gui_refresh_tt` and the five `independence_wave_status_gui_tab_*_tt` keys. A GUI render is required before deciding whether to shorten or remove them, and the required MCP route timed out.

### Repetition

The package set contains widespread exact prose reuse that weakens route identity even though the keys are mechanically valid. Examples include:

- identical emergency-command descriptions across BSK, BYA, KHA, and KUR
- the same Danube emergency-command description across AXX, BOS, BBX, MAC, BAX, and TRA
- repeated former-host ledger descriptions across several Balkan packages
- repeated compact, depot, municipal-charter, and network-effect text across distinct packages

This is a package-localisation depth issue. It should be handled only with package ownership and accepted identity material, not by a blind bulk rewrite.

### Overcomplication

Several effect tooltips combine four or more mechanical sections into one value. `independence_wave_rut_network_effect_tt`, `independence_wave_mnt_host_ledgers_effect_tt`, and similar package-local keys are accurate but difficult to scan. Their constants and dynamic tokens must be preserved during any future restructuring.

### Style-rule repair and remaining violations

The Event 006 YAML set contains no em dash and no semicolon sentence. The automated scan found no literal working-label, placeholder, implementation-history, rework-history, package-ID, adapter, hardcoded, or runtime wording.

Two `while the government` clauses were found in `independence_wave_fragmented_command_desc` and `independence_wave_balanced_patronage_desc`. They describe simultaneous mechanics rather than staged official denial, so they were not treated as prohibited escalation contrast.

No dialectical `not just`, `not only`, or `not ... but ...` template was detected. No safe claim is made that all 8,756 values are free of subtle staccato or generic-tone problems; the exact-repetition findings above demonstrate that broader prose review is still needed.

## Sourced-quotation preservation notes

The quote-bearing super-event keys `chaosx_super_event.23.q` and `chaosx_super_event.24.q` were inspected and left byte-untouched. Their Wilson and Hosea wording and attributions were not modernized, shortened, or repunctuated.

No sourced quotation exists in the patched evolution-summary file.

## Patch

### Changed files

- `localisation/english/006_independence_wave_evolutions_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_localisation_audit_round2_2026-08-24.md`

### Changed keys

- `independence_wave.evolution.summary`

### Before and after display

Before:

> A stage of the worldwide sovereignty cascade has taken hold, reshaping which states may emerge and what institutions, forces, and ambitions they carry into independence.

After:

> The sovereignty cascade has changed which states can emerge and the institutions, forces, and ambitions they bring to independence.

The Event Log evolution details summary now leads with the visible change and removes passive throat-clearing. The event identity and gameplay meaning are unchanged.

### Dynamic localisation added or fixed

None. The edited key contains no dynamic tokens. Its existing scripted selector remains unchanged.

### Prose before-and-after summary

- Vagueness: replaced “a stage ... has taken hold, reshaping” with a direct statement of what changed.
- Bloat: reduced the sentence from 27 words to 20 words.
- Obvious explanation: removed the announcement that a stage “has taken hold.”
- Repetition: removed one redundant stage/cascade framing phrase.
- Overcomplication: simplified the main verb while preserving the three affected dimensions: institutions, forces, and ambitions.
- Style-rule repair: changed passive process language to a direct active construction.

All dynamic tokens and formatting codes were preserved because the key contains none. Sourced quotations were preserved without exception.

## Meaningful validation

- Re-ran the Event 006 key/reference audit after the patch: no duplicate Event 006 YAML key, missing current-source display reference, missing scripted-localisation target, duplicate Event 006 `defined_text`, or unresolved Event 006 scripted-localisation call was found.
- Confirmed the patched YAML retained its UTF-8 BOM.
- Confirmed `GetEventsLogSelectedEvolutionSummary` still selects the changed key and that the shared GUI binds evolution summary controls in both normal and wide evolution-detail windows.
- Compared the current Event Details key with the current exported catalog row and accepted premise direction; no wording contradiction was found.

## Skipped meaningful validation and exact blockers

The required read-only Event MCP trace was attempted with `hoi4.event_inspect` for selector `{ kind = event, eventId = chaosx.nr6.1 }`. The valid request timed out after 180 seconds with `timed out awaiting tools/call after 180s` and returned no artifact URI.

The linked shared Event Log GUI was then submitted to `hoi4.gui_inspect` with `windowName = events_log_popup_window` and scenario `event6_localisation_evolution_summary_round2`. That valid request also timed out after 180 seconds with the same error and returned no artifact URI.

No `hoi4.gui_render` was attempted after the prerequisite inspect failed. Overflow, long-text behavior, and visual fit of the new summary remain unverified. Source inspection is not treated as equivalent MCP or rendered evidence.

## Unresolved wording decisions and parent follow-up

- Decide whether the 675 leading-indented YAML keys warrant a separate mechanical style-normalization pass.
- Route the repeated generic package descriptions to package owners if bespoke identity prose is desired. Do not bulk-rewrite them without package context.
- Retry the Event MCP and Event Log GUI inspect/render routes before any whole-event localisation completion claim.
- Update the nine stale current documentation citations to the category and on-action registries. They do not block current localisation loading but do misdirect maintainers.
- Review the long dynamic ledger and effect tooltips with rendered consumers before shortening them.

No separate design-depth plan was written. The repeated package prose is an implementation-quality backlog, not evidence for a new mechanic.
