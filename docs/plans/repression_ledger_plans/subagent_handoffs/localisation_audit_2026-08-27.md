# Repression Ledger localisation audit handoff

## Scope and outcome

Audited the current Repression Ledger player-facing text, dynamic branches, and five-tab GUI consumers in `localisation/english/camp_repression_rework_l_english.yml`, `localisation/english/camp_repression_country_kits_l_english.yml`, `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`, `interface/camp_repression_ledger.gui`, and `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`.

The patch removes the remaining text-simulated telemetry style from the audited localisation, replaces implementation-facing language with direct in-world prose, aligns the five visible tabs with their separate panels, and prevents cached Japanese action identifiers from selecting Japanese names or descriptions outside Japan.

## Changed files and keys

- `localisation/english/camp_repression_rework_l_english.yml`
  - `camp_repression_network_desc_germany`
  - `camp_repression_network_desc_japan`
  - `camp_repression_network_desc_soviet`
  - `camp_repression_network_desc_generic`
  - `repression_ledger_category_summary`
  - `repression_ledger_gui_phase`
  - `repression_ledger_gui_summary`
  - `repression_ledger_tab_sites`
  - `repression_ledger_tab_sites_tt`
  - `repression_ledger_tab_country`
  - `repression_ledger_tab_country_tt`
  - `repression_ledger_tab_discovery`
  - `repression_ledger_tab_discovery_tt`
  - `repression_ledger_overview_reach`
  - `repression_ledger_overview_output`
  - `repression_ledger_overview_burden`
  - `repression_ledger_overview_evidence`
  - `repression_ledger_country_values_germany`
  - `repression_ledger_country_values_japan`
  - `repression_ledger_country_values_soviet`
  - `repression_ledger_country_values_generic`
  - `repression_ledger_selected_state`
  - `camp_selected_state_detail`
  - `camp_gui_chemical_method_tt`
- `localisation/english/camp_repression_country_kits_l_english.yml`
  - `germany_mengele_cloning_unlock_requirements_tt`
  - `germany_mengele_cloning_unlock_pending_tt`
  - `camp_ledger_country_values_germany`
  - `camp_auschwitz_status_dormant`
  - `camp_ledger_country_values_japan`
  - `camp_ledger_country_values_soviet`
- `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`
  - Added `original_tag = JAP` guards to all four Japanese action-name branches and all four Japanese action-description branches in `GetCampCountryAction1Name` through `GetCampCountryAction4Description`.
- `docs/plans/repression_ledger_plans/subagent_handoffs/localisation_audit_2026-08-27.md`
  - This handoff.

The concurrent parent-owned five-tab edits in `interface/camp_repression_ledger.gui` and `common/scripted_guis/camp_repression_ledger_scripted_gui.txt` were inspected but not authored or reverted by this subagent.

## Audit lists

- Missing keys: none among the 90 GUI localisation references and 232 static scripted-localisation references.
- Duplicate keys: none among references consumed by this GUI and scripted-localisation surface.
- Scripted localisation issues: the Japanese action branches previously trusted only cached numeric action ids. They now also require `original_tag = JAP`. Country panel names, country summaries, and network descriptions already use explicit country branches with neutral generic fallbacks.
- Dynamic text opportunities: NKVD authority, gulag reach, archive control, transfer pressure, occupation records, and army-review pressure still lack dedicated band-name helpers. Their numeric values are preserved because removing existing dynamic tokens for concision would alter the information contract. A future GUI-owner pass could move secondary values into card tooltips and retain no more than four visible country-system values.
- Cross-surface mismatch notes: the current five-tab contract is aligned as Overview, State Pools, Active Sites, Country System, and Evidence & Reform. Each visible tab has a matching click entry, selection mark, and panel-visibility entry. The exact remaining overflow diagnostic is unresolved below.
- File encoding concerns: both edited English localisation files remain UTF-8 with BOM.
- Sourced quotations: no sourced or attributed quotation appears on the inspected category, tab, card, action, or scripted-localisation surface. No quotation text was changed.

## Before and after display

- Before: overview and selected-state text used pipe-like or semicolon-separated telemetry patterns and read as a debug ledger. After: cards and summaries use short sentences tied to the actual panel purpose.
- Before: major-country summaries were label/value dumps. After: the same dynamic values and band calls are expressed as country-specific prose; no Japanese summary branch can serve the Soviet Union or a generic country.
- Before: `hidden project progress`, a recurring `monitor`, `registered`, `unregistered`, `slot`, and similar implementation-facing terms appeared in player text. After: these read as project preparation, current conditions, active administration, and available directives.
- Before: the combined wording used Locations, Actions, and Discovery & Reform. After: localisation matches the five real panels as Active Sites, Country System, and Evidence & Reform.
- Before: the chemical-method tooltip described an already-scaled baseline in tuning language. After: it states the action, consequences, and preserved dynamic multipliers directly.

## Prose-quality repairs

- Vagueness: network descriptions now identify the acting institution and the concrete costs in sites, deaths, resistance, famine, evidence, and reform pressure.
- Bloat: the chemical-method explanation and cloning-pending explanation were shortened without removing their dynamic values or requirements.
- Obvious explanation: close/open and current-directive text no longer narrates implementation slots or monitoring behavior.
- Repetition: category, overview, country, and evidence surfaces now divide their responsibilities instead of repeating a generic ledger inventory.
- Overcomplication: long noun stacks and tuning phrases such as `agent-scaled baseline` and `hidden project progress` were replaced with direct consequences and preparation stages.
- Style-rule repair: no spaced pipe delimiter, box-drawing separator, em dash, or sentence semicolon remains in the two audited localisation files.

All existing dynamic tokens, formatting codes, costs, requirements, names, and consequences were preserved. The only removed material was redundant or implementation-facing prose. No sourced quotation was altered.

## Validation and MCP evidence

- Source audit found zero missing consumed localisation keys, zero duplicate consumed keys, and zero unresolved `GetCamp...` calls across the two localisation files.
- The five GUI tab element names match their scripted click, selection-mark, and panel-visibility entries.
- The final `hoi4.gui_inspect` used scenario `repression_ledger_final_five_tab_audit`, inspected 94 elements, and returned revision `e9ec19a454d1e6f363fd0a69e02c6973ecb6fc6379e7e07772b53ccd33998a79`.
- Final inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87f7b8ac7bb98e3a9e1ad4a1e66491d904a724c468f0612a8178571b28cf7a9f/51247949fbf712590389b1d339771ad0d586affaea2bc5b4c02b0abe5f7fb42b/gui-inspect.e9ec19a454d1e6f3.json`.
- Full-window render artifact at 1920x1080: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0179a2e4c0df19f733c338fc2bdf7d696c1236dd7cad8fa8ea08fc1d146f48b/f3a24e5038e566ea6eadf7a086a5d03096f3cde855f96e2a4ae9f1c26eb8371a/repression_ledger_window-full.svg`.

## Skipped or blocked meaningful validation

The final MCP inspection reports exactly one `GUI_TEXT_OVERFLOW`, but the server's global graph and validation diagnostic ceilings omitted the element and location from the inline response. The linked 56 MB inspect artifact is byte-ranged, and the available route did not expose a focused diagnostic filter. Source dimensions make the 90-pixel `Country System` tab label the leading candidate, but that is an inference, not verified attribution. The parent GUI owner should widen that label region or confirm the exact element through its GUI comparison pass, then rerun the render. Source review is not treated as equivalent to that missing visual evidence.

No in-game validation was performed because live consumer validation belongs to the user. No gameplay effects, costs, AI, or balance were changed.

## Remaining risks and unresolved wording decisions

- The single MCP text-overflow diagnostic remains unresolved until the GUI owner identifies and fixes its exact element.
- The Germany, Japan, and Soviet country-system summaries preserve more than four pre-existing dynamic values. Their prose is cleaner, but the underlying value budget remains too large for the skill's preferred country-card hierarchy. Reducing it safely requires a GUI-owner decision about which secondary values move into tooltips.
- No plan handoff beyond this required patch handoff was written. The remaining issues are presentation follow-up, not a missing mechanic.

## Final restricted-payload addendum

This final pass was read-only for gameplay, GUI, localisation, and scripted localisation. Only this handoff was updated.

### Cost branch and key coverage

- `GetCampChemicalPayloadCost` has 21 ordered branches. Every referenced key is defined exactly once: seven ordinary chemical payloads, three nerve-mastery variants, the corresponding technology-only fallbacks, and `camp_cost_payload_unavailable`.
- `GetCampBiologicalPayloadCost` has nine ordered branches. Every referenced key is defined exactly once: four capacity branches, four technology-only fallbacks, and `camp_cost_payload_unavailable`.
- `GetCampRestrictedPayloadCost` has three ordered branches. `camp_cost_payload_restricted_chemical` resolves to `GetCampChemicalPayloadCost`, `camp_cost_payload_restricted_biological` resolves to `GetCampBiologicalPayloadCost`, and the fallback resolves to `camp_cost_payload_unavailable`.
- All payload strings are icon-first. The two action costs also lead with `£pol_power` and the shared `camp_rework_cost.restricted_method_pp` value of 60, matching both GUI availability and the political-power debit in `common/scripted_effects/camp_repression_rework_effects.txt`.
- Ordinary chemical quantities match the action source: chlorine 70, phosgene 60, mustard 50, lewisite 45, tabun 40, sarin 35, and soman 28 cylinders.
- Biological quantities and equipment names match the action source: tularemia 20, anthrax 16, plague 12, and smallpox 6 bombs.

### Concrete remaining defect

The three nerve-mastery quantities displayed by `camp_cost_payload_tabun_mastery`, `camp_cost_payload_sarin_mastery`, and `camp_cost_payload_soman_mastery` do not match the amount debited by the action.

- The localisation displays `camp_rework_chemical_mastery_cost`: 24 tabun, 21 sarin, and 16.8 soman cylinders.
- `camp_rework_prepare_chemical_method_outcome` instead starts from the ordinary costs 40, 35, and 28, then multiplies `camp_method_stockpile_cost` by `camp_rework_chemical_factor.nerve_mastery_payload_cost = 0.45` before passing it to `cbrn_try_debit_action_payload`.
- The resulting debits are 18 tabun, 15.75 sarin, and 12.6 soman cylinders.
- The mastery-capacity triggers also test the separate 24/21/16.8 constants, so the displayed number currently describes the availability threshold rather than the actual action debit. The gameplay owner must choose one source of truth and align the trigger, debit, and localisation together. This read-only audit did not make that balance decision.

### Final localisation hygiene

- 335 unique keys are consumed by `interface/camp_repression_ledger.gui` and `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`. None are missing and none resolve to duplicate English definitions.
- No spaced pipe delimiter, box-drawing separator, fake text-layout line, telemetry wording, placeholder wording, debug wording, implementation-history wording, hardcoded wording, or raw-variable wording remains in the audited GUI, scripted-localisation, or two camp localisation files.
- All Japanese country panel, value, network-description, action-name, and action-description branches require `original_tag = JAP`. No Japanese key is reachable from an unguarded action branch, so the Soviet and generic fallbacks cannot inherit Japanese prose.
- `localisation/english/camp_repression_rework_l_english.yml` and `localisation/english/camp_repression_country_kits_l_english.yml` both retain their UTF-8 BOM. No `:0` key style or leading-space key was found.
- No sourced or attributed quotation appears on this restricted-payload or tab surface. Dynamic tokens, icons, formatting codes, equipment names, costs, and quantities were inspected but not edited.

### Five-tab overflow assessment

- Current labels are Overview, State Pools, Active Sites, Country System, and Evidence & Reform.
- Overview, State Pools, and Active Sites use 90 by 18 text boxes. Country System uses the widened 100 by 36 box, and Evidence & Reform uses 90 by 36. The two longer labels therefore have two-line height available.
- The successful `hoi4.gui_render` covered normal, long-text, and missing-localisation states at 1920 by 1080 and 1366 by 768. The complete 3,367,417-byte SVG artifact was byte-range scanned and contains no `GUI_TEXT_OVERFLOW` or `text_overflow` marker. On current source and render evidence, none of the five English tab labels is likely to overflow.
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/125c3b778d52bee555772509f03a11c3fe23da527cd883fde7a3ee338475afbc/19699af0348c55d53cdc6ebad95a7c742e4321a61b37d6d66fbad033e6800d0d/repression_ledger_window-full.svg`.
- Two `hoi4.gui_inspect` calls for `repression_ledger_window` timed out at the MCP server boundary after 180 seconds and produced no new inspect artifact. The render response itself was wire-truncated and its offline font paths are approximations. The source and render artifact therefore resolve the likely English-label overflow question, but they do not replace an engine-native inspection or live consumer check.

### Final change and validation record

- Changed file: `docs/plans/repression_ledger_plans/subagent_handoffs/localisation_audit_2026-08-27.md` only.
- No gameplay, GUI, localisation, scripted-localisation, cost, balance, or behavior file was edited.
- No commit was created. Parent review owns any repair of the mastery cost mismatch.

## Final nerve-mastery cost clearance

The earlier mastery-cost defect is cleared and superseded by the current source.

- Activation display, requirement, and debit now agree exactly: tabun 18.00, sarin 15.75, and soman 12.60 cylinders. The three mastery localisation keys use `|2`, so no precision is lost in the player-facing cost.
- Monthly requirement and debit also agree exactly: tabun 2.70, sarin 2.25, and soman 1.80 cylinders.
- `GetCampChemicalPayloadCost` selects the matching mastery key whenever nerve mastery and the corresponding activation-capacity trigger apply. Equipment names remain aligned with the consumed tabun, sarin, and soman cylinder types.
- No remaining concrete defect was found in the displayed, required, or consumed nerve-mastery quantities.

This clearance changed only this handoff. No gameplay, GUI, localisation, scripted-localisation, trigger, effect, or constant source was edited, and no commit was created.
