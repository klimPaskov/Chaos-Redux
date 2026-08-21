# Event 020 Black Plague response dashboard localisation audit

## Scope

Audited only the dedicated response dashboard and its direct category consumer:

- `interface/020_black_plague_response.gui`
- `common/scripted_guis/020_black_plague_response_scripted_guis.txt`
- `common/decisions/categories/020_black_plague_response_categories.txt`
- the dashboard and directly consumed category/status keys at the top of `localisation/english/020_black_plague_response_l_english.yml`
- the two directly referenced `defined_text` blocks in `common/scripted_localisation/020_black_plague_response_scripted_localisation.txt`, read only to verify the dashboard calls

The shared Disease Containment UI, gameplay decisions, and other Event 020 localisation were not audited or changed.

## Outcome

The dedicated window presents the intended live hierarchy: Countermeasure Progress is the primary value, and Medical Reserve plus Response Capacity are the two supporting live values. Country/world deaths and international response are supporting status lines rather than additional managed values. The cure-programme line is a categorical status for the same countermeasure progression, not a separate numeric mechanic.

The completion wording does not promise an instant cure. `black_plague_countermeasure_status_complete` says that cure-capable cleanup is unlocked, while `black_plague_countermeasure_progress_tt` explicitly says progress does not remove an outbreak by itself.

## Audit lists

### Missing keys

None in the scoped GUI/category surface. Every `text` and `pdx_tooltip` key referenced by `black_plague_response_category_window` is present, as are `black_plague_response_category` and `black_plague_response_category_desc`.

### Duplicate keys

None among the scoped keys in `020_black_plague_response_l_english.yml`.

### Scripted localisation issues

None found. `GetBlackPlagueCountermeasureStatus` and `GetBlackPlagueInternationalResponseStatus` exist, use country-scoped flags, reference present localisation keys, and provide unconditional fallback text.

### Dynamic text opportunities

No missing dynamic value was identified. The three managed values use live variables, the progress denominator uses the configured completion constant, deaths use country/global variables, the country name is dynamic, and both categorical status lines use scripted localisation.

### Cross-surface mismatches

None requiring a patch. The category description sends selected-state operations to the Disease Containment board, matching the dedicated dashboard's read-only national role. `Cure programme` and `Countermeasure Progress` describe the same primary mechanic at status and numeric-detail levels; this is intentional but should remain paired if either label changes later.

### File encoding concerns

None. `localisation/english/020_black_plague_response_l_english.yml` retains UTF-8 BOM (`EF BB BF`) after the edit.

### Prose-quality issues and fixes

- Vagueness: the Medical Reserve tooltip previously said production and operations merely “change” the stock. It now states that production raises it and active operations consume it.
- Bloat: the category description, identity tooltip, Response Capacity tooltip, outbreak-ledger tooltip, and international-status tooltip were shortened without removing mechanics or destinations.
- Obvious explanation: no title-restating tooltip remained after the pass. Tooltips focus on cause, use, or routing.
- Repetition: repeated references to the shared board and response bureaucracy were compressed while preserving the boundary between national and selected-state actions.
- Overcomplication: “mortality transaction” implementation language was replaced with direct player-facing wording about deaths already caused by the plague.
- Style-rule repair: passive and administrative constructions were replaced with direct verbs. The Countermeasure Progress tooltip uses the repository's British `programme` context indirectly and keeps three concrete sentences rather than a staged contrast formula.

### Sourced quotations

No sourced or attributed quotation appears on the scoped surface, so no quotation text required preservation.

## Patch details

### Changed files

- `localisation/english/020_black_plague_response_l_english.yml`
- this handoff

### Changed keys

- `black_plague_response_category_desc`
- `black_plague_response_gui_identity_tt`
- `black_plague_response_gui_medical_reserve_tt`
- `black_plague_response_gui_response_capacity_tt`
- `black_plague_response_gui_outbreak_ledger_tt`
- `black_plague_response_gui_international_status_tt`
- `black_plague_countermeasure_progress_tt`

### Dynamic localisation added or fixed

None. All existing dynamic tokens, variable references, formatting codes, constants, and scripted-localisation calls were preserved unchanged.

### Before and after display behavior

The window's values, visibility, labels, status selection, and gameplay behavior are unchanged. Only category/tooltip prose became shorter and more explicit. The Progress tooltip still states that completion unlocks cure-capable local cleanup and never removes an outbreak by itself.

## Meaningful validation

- `hoi4.gui_inspect` completed for `black_plague_response_category_window` under scenario `event020_black_plague_response_dashboard`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d7beb146e4141d75221521fac34366736c2267128c1f010aece6af847c5c888/bb4134a9df9a48efcb552bc256d3e54e3ade1710be5fcd1604e53060b2a37ab0/gui-inspect.3f116c4bf76362b8.json`.
- One bounded 1920x1080, UI-scale-1 long-text render completed for the exact window. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b64b40b804208457dd979c1eadc570b6fbee3255be88721f46439a9453a494d6/fcb7d850fa74da63e2aecf1c169d0123973b2ba1cf36f4fb69e36570dd37fd35/black_plague_response_category_window-full.svg`.
- The render places the warning, death ledger, and international status within their assigned 426-pixel rows, and keeps Medical Reserve and Response Capacity in separate 202-pixel columns.
- Direct source checks confirmed every GUI text/tooltip reference, both scripted-localisation definitions and fallbacks, duplicate-key absence in the scoped file, and retained UTF-8 BOM.

## Skipped or limited validation

- No live game render was run; in-game consumer validation belongs to the user.
- The MCP synthetic scenario did not resolve the country/global numeric variables or scripted-localisation calls into representative maximum-length values. It rendered placeholders, so exact overflow behavior for exceptionally long country names or very large death/reserve totals remains uncertain.
- The MCP inspect reported repository-wide graph diagnostic truncation and unrelated symbol collisions. Those global diagnostics were outside this bounded localisation task and prevent treating the inspect's repository-wide validation flag as a clean task-specific pass.
- No post-edit GUI render was necessary because the patch changed tooltips/category prose only and did not change visible dashboard rows, coordinates, or window dimensions.

## Remaining risk and unresolved wording decisions

- The 202-pixel live-value columns are safe for ordinary values in the bounded render, but extremely large Medical Reserve or Response Capacity totals could outgrow them because the renderer could not substitute numeric maxima.
- The supporting death ledger may be vulnerable to an exceptionally long dynamic country name combined with unusually large death totals. Its 426-pixel row is generous, but the bounded synthetic render could not prove the worst case.
- No wording decision remains blocked. If the parent later renames `Cure programme`, the categorical status line and Countermeasure Progress terminology should be reviewed together so they continue to read as one mechanic.

## Parent disposition

The parent shortened the two visible support labels to `Reserve` and `Capacity` after this audit and replaced the dynamic country name in the ledger with `National deaths`. This removes the identified country-name overflow path and leaves more room for large support values without changing their tooltips or mechanics.

## Simplifications, omissions, and blockers

No gameplay or GUI-layout simplification was made. The only evidence limitation is unresolved maximum-length dynamic substitution in the offline render. No plan addendum was needed.
