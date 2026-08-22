# Event 006 localisation surface audit and patch

## Scope and source authority

This pass audited the current English Event 006 localisation against the accepted Independence Wave specification, achievement matrix, decision and mission matrix, super-event text research, current event, decision, scripted-localisation, scripted-GUI, event-log, scenario, achievement, cluster, and super-event consumers.

The audit covered 73 dedicated `006*_l_english.yml` files with 8,714 localisation keys.

The source-reference scan covered 545 event, common, and interface files that mention `independence_wave` or `chaosx.nr006`. It found 2,361 filtered localisation references and 2,342 unique referenced keys in title, description, text, tooltip, and button fields.

## Audit results

### Missing keys

None in the scanned Event 006 source-linked title, description, text, tooltip, and button consumers.

### Duplicate keys

None among the 8,714 dedicated Event 006 keys, and none for those keys across the complete English localisation folder.

### Scripted localisation

The 11 dedicated Event 006 scripted-localisation files contain 352 `localization_key` targets. Every non-GFX target resolves to English localisation.

No duplicate `defined_text` names were found inside the dedicated Event 006 scripted-localisation set.

No direct `§` or `£` format characters were found in those scripted-localisation files.

The shared event-log scripted localisation resolves the five Event 006 evolution titles and bodies, the danger milestone, Join history, release-record history, and Event Details key. The shared scenario scripted localisation resolves every Event 006 type, intensity, and launch-status key reviewed.

One unused-key candidate remains: `independence_wave_form03_member_language_cost_tooltip` has no current source consumer outside its localisation definition. Its values were not changed because no live consumer proves the intended cost surface.

### Dynamic text opportunities

Eleven visible requirements used raw numeric state labels or the working phrase `selected FER anchor`. They now use the existing state localisation tokens for states 234, 249, 291, 408, 409, 421, 507, 512, 538, 663, 668, and 950.

The Event Details text already formats Join thresholds dynamically through `constant:independence_wave_join.reduction_percent` and `constant:independence_wave_join.minimum_states_lost`.

No new scripted-localisation function was required.

### Cross-surface consistency

The 16 accepted achievement-matrix rows have 16 `_NAME` keys, 16 `_DESC` keys, and 16 achievement-specific tooltip keys. The additional generic eligibility tooltip is intentional.

The Event Details key `chaosx.events_log.window.event_details.independence_wave` exactly matches workbook `Events!C7` according to `006_event6_catalog_reconcile_2026-08-22.md`. That reconciliation also refreshed the export-only catalog CSVs.

The Liberations cluster description consistently presents the shared liberation crisis without exposing Event 006 route internals.

The scenario surface consistently uses `Every Banner Rises`, scenario entry `#008`, the eight accepted scenario-type names, four intensity descriptions, and the current blocked-movement ledger terms.

The two super-event titles, descriptions, buttons, and quotations remain aligned with the accepted text research.

### Encoding and namespace concerns

All 73 dedicated Event 006 localisation files have UTF-8 BOM encoding.

No forbidden localisation version suffixes were found.

There are 707 key lines with leading indentation across the Event 006 files. This is a repository-style concern, not a runtime key-resolution failure, and was not mechanically normalized during a prose patch in a heavily shared worktree.

No wrong Event 006 localisation namespace was found in the scanned live consumers.

### Prose-quality findings

Vagueness: raw labels such as `state 291` and `selected FER anchor` concealed the actual locations. These were replaced by localised state names.

Bloat: no broad bloat rewrite was justified on the accepted event-log, evolution, scenario, achievement, or super-event prose.

Obvious explanation: `independence_wave_status_gui_refresh_tt` and `independence_wave_status_gui_toggle_animation_tt` still describe their visible button actions. They were not removed because the current GUI inspection and render routes did not return bounded visual evidence.

Repetition: seven regional overlay descriptions repeated the formula `without pretending that a foreign or distant sponsor has solved local logistics`. The repeated disclaimer was replaced by a concrete locally controlled supply schedule.

Overcomplication: no additional live consumer required a safe bounded rewrite after state labels and the repeated logistics formula were repaired.

Style-rule repair: the Kuban and Tatarstan project-failure tooltips used semicolons. Each consequence now has its own complete sentence.

Potential policy mismatch: Event Details includes exact Join thresholds even though the event-writing guidance normally reserves mechanical requirements for action and tooltip surfaces. The workbook deliberately mirrors this current text. It was left unchanged because resolving the accepted cross-surface wording requires a parent decision, not a localisation-only rewrite.

### Sourced quotations

The Wilson excerpt and attribution in `chaosx_super_event.23.q` were not changed.

The Hosea 8:7 King James Version excerpt and attribution in `chaosx_super_event.24.q` were not changed.

No attributed quotation appeared in any patched key.

## Patch

### Changed files

- `localisation/english/006_independence_wave_far_eastern_l_english.yml`
- `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`
- `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`
- `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml`
- `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`
- `localisation/english/006_independence_wave_kuban_l_english.yml`
- `localisation/english/006_independence_wave_kurdistan_l_english.yml`
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`

### Changed keys

- `independence_wave_fer_hold_railway_council_desc`
- `independence_wave_iw059_hold_baghdad_river_guard_desc`
- `independence_wave_iw085_secure_oasis_depots_desc`
- `independence_wave_iw085_hold_cyrenaica_coastal_guard_desc`
- `independence_wave_iw101_secure_kongo_river_depots_desc`
- `independence_wave_iw101_hold_kongo_river_corridor_desc`
- `independence_wave_iw102_secure_kuba_forest_depots_desc`
- `independence_wave_iw102_hold_kuba_forest_anchor_desc`
- `independence_wave_iw105_secure_loango_port_depots_desc`
- `independence_wave_iw105_hold_loango_port_guard_desc`
- `independence_wave_iw156_secure_moluccan_interisland_depots_desc`
- `independence_wave_iw156_hold_moluccan_sea_lanes_desc`
- `independence_wave_iw196_secure_antilles_member_depots_desc`
- `independence_wave_iw197_secure_araucania_depots_desc`
- `independence_wave_iw197_hold_araucania_anchor_desc`
- `independence_wave_iw204_secure_patagonia_depots_desc`
- `independence_wave_kub_hold_mounted_compact_together_desc`
- `independence_wave_kub_project_failure_effect_tt`
- `independence_wave_kur_hold_mountain_council_desc`
- `independence_wave_tat_hold_river_compact_together_desc`
- `independence_wave_tat_project_failure_effect_tt`

### Display before and after

Before, several missions displayed raw internal labels such as `state 538`, `state 950`, or `selected FER anchor`. After, those surfaces resolve the installed state names through `$STATE_n$` tokens, including Coquilhatville, Araucanía, Vladivostok, and Khabarovsk.

Before, seven overlay depot descriptions ended with the same explanatory disclaimer about a sponsor not solving local logistics. After, they state that the route establishes a locally controlled supply schedule.

Before, the Kuban and Tatarstan failure tooltips joined separate consequences with semicolons. After, the loss and instability consequences are separate sentences.

All existing constants, variable formatters, colour codes, text icons, country scope tokens, and gameplay consequences were preserved.

## Validation

The post-patch source scan found no remaining raw `state <number>` strings in dedicated Event 006 English localisation and no remaining copy of the repeated sponsor disclaimer.

Every added `$STATE_n$` token resolves in the installed vanilla `state_names_l_english.yml`.

All eight changed localisation files retain UTF-8 BOM encoding.

The dedicated Event 006 key and scripted-localisation target counts remain stable, with no missing or duplicate key introduced by the patch.

The read-only event inspection returned partial current-source evidence with revision `2af1fa63424ef325ab938b49e0183b19d58d881a678db801d72f40e94ec2701c` and graph hash `565a46665a869a32a3345249b71191686a4725ae679476fa7f864e3a33afacb2`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8b4bbda2f91fd30b4b5ce5b9a1203bf9249738a19d8e79cdc4a1b926e950a08/09930825fc66400cdf696ea7e8c435a8281ce4172c57a88ed6e66a732b50155c/event-trace-2af1fa63424e.json`.

## Skipped or blocked meaningful validation

`hoi4.event_render` for `chaosx.nr006.1` did not return within a bounded 60-second attempt and was terminated. Event-popup overflow and rendered option presentation therefore remain unresolved.

`hoi4.gui_inspect` and `hoi4.gui_render` for `independence_wave_status_window` did not return within bounded attempts and were terminated. GUI overflow, long-text behavior, missing-localisation rendering, and the value of the two button tooltips remain unresolved.

Read-only focus inspection for the four Event 006 focus files did not return within a bounded parallel attempt and was terminated. Focus-card overflow and rendered focus localisation coverage remain unresolved rather than treated as source-verified.

No Technology Tree Viewer was available in the installed package. Event 006 technology-tree localisation rendering was therefore unavailable, and source-only review is not presented as equivalent visual evidence.

No live game validation was performed because live consumer testing belongs to the user.

## Unresolved wording decisions and parent follow-up

- Decide whether exact Join thresholds remain in Event Details or move to an action or tooltip surface, then keep the workbook mirror aligned.
- Revisit the two status-window button tooltips after GUI inspection and rendering become available.
- Decide whether the orphan `independence_wave_form03_member_language_cost_tooltip` should be wired to a consumer or removed.
- Consider a separate mechanical indentation normalization pass for the 707 indented key lines. It should not be mixed into prose review.

No new design-gap plan was written. This file is the required bounded patch handoff.
