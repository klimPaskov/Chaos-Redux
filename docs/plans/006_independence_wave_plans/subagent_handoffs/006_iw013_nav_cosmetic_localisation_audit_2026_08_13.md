# IW-013 NAV Cosmetic Localisation Audit

Date: 2026-08-13

## Scope and result

Read-only audit of the four IW-013 NAV cosmetic identities added to `localisation/english/006_independence_wave_iberian_l_english.yml`.

The 60-key country-name ladder is complete, uniquely defined across the English localisation set, syntactically regular, and encoded in UTF-8 with BOM. The four names are concise, concrete, and distinguish the constitutional, traditional, socialist, and emergency identities without exposing implementation details. No localisation patch was required.

One cross-surface decision remains for the owning agent: the patron-client installer uses `NAV_INDEPENDENCE_WAVE_CIVICX`, so a patron-client NAV displays `Basque Civic Republic` while its party and national spirit are `Protected Pyrenean Compact`. This is mechanically valid and consistent with the documented four-identity design, but the visible country name does not express the patron route as clearly as its other surfaces.

## Source references checked

- `common/countries/cosmetic.txt:1812-1831` defines `NAV_INDEPENDENCE_WAVE_CIVICX`, `NAV_INDEPENDENCE_WAVE_AGRARIANX`, `NAV_INDEPENDENCE_WAVE_SOCIALISTX`, and `NAV_INDEPENDENCE_WAVE_EMERGENCYX`.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:169,186,203,221,239,444` applies the four tags. The constitutional route and initial setup use CIVICX, workers use SOCIALISTX, municipal/traditional uses AGRARIANX, emergency uses EMERGENCYX, and patron-client also uses CIVICX.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:578-584` recognizes and removes all four tags during cleanup.
- `docs/events/006_independence_wave/iberian_registered_packages.md` documents the same four generated route identities and says vanilla NAV is preserved before setup and after cleanup.
- `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/manifest.md` uses the same four identifiers and describes matching civic, agrarian, socialist, and emergency flag roles.

## Key coverage

Each cosmetic identity has the complete 15-key ladder:

- unqualified name, `_DEF`, and `_ADJ`
- `democratic`, `communism`, `neutrality`, and `fascism` names
- `_DEF` and `_ADJ` for each ideology

Covered key families:

- `NAV_INDEPENDENCE_WAVE_CIVICX*`: 15 of 15
- `NAV_INDEPENDENCE_WAVE_AGRARIANX*`: 15 of 15
- `NAV_INDEPENDENCE_WAVE_SOCIALISTX*`: 15 of 15
- `NAV_INDEPENDENCE_WAVE_EMERGENCYX*`: 15 of 15

Missing key list: none.

Wrong-namespace list: none. The identifiers exactly match the cosmetic definitions, effect consumers, flag filenames, and documented route identifiers.

## Duplicate keys

Duplicate key list: none. Every one of the 60 audited keys has exactly one definition across `localisation/english/`, and no key repeats inside the assigned file.

## Scripted localisation and dynamic text

Scripted localisation issue list: none. The audited values contain no scripted-localisation calls, scope tokens, bound variables, colour codes, or formatting tokens.

Dynamic text opportunities: none. Country-name and adjective ladders should remain static. Their only runtime variation is already supplied by the engine's ideology-specific lookup.

## Cross-surface mismatch notes

- Review requested: `independence_wave_install_nav_patron_government` assigns the CIVICX cosmetic identity while setting the democratic party to `Protected Pyrenean Compact` and adding `nav_protected_pyrenean_compact`. The map and diplomacy name therefore remain `Basque Civic Republic`. The owner should explicitly accept this shared civic identity or create a distinct patron cosmetic package with matching flag assets and full localisation. A localisation-only rename is not safe because CIVICX also belongs to initial setup and the constitutional route.
- The other mappings are coherent: CIVICX / `Basque Civic Republic`, AGRARIANX / `Basque Agrarian Compact`, SOCIALISTX / `Basque Workers' Republic`, and EMERGENCYX / `Basque Frontier Directorate` match their effect routes and flag manifest roles.
- All ideology variants deliberately retain the selected route identity. This prevents an ideology suffix lookup from falling back to vanilla NAV after popularity or politics changes.

## File encoding concerns

None. The target file begins with bytes `EF BB BF`, declares `l_english:`, and the added keys use the repository's unversioned `key: "value"` format.

## Prose-quality audit

- Vagueness: none. Each country name identifies both the Basque polity and its governing form.
- Bloat: none. The longest visible name, `Basque Frontier Directorate`, is 27 characters and contains no redundant qualifier.
- Obvious explanation: none. These are labels, not tooltips, and they do not narrate their own display behavior.
- Repetition: the ideology ladders repeat the selected route name and adjective by design. This is required fallback coverage rather than avoidable prose repetition.
- Overcomplication: none. All terms are familiar within the route context and the names avoid stacked administrative clauses.
- Style-rule violations: none. No em dash, semicolon, fragment, staged contrast, implementation history, tuning note, or AI-style filler appears.

Recommended wording fixes: none within the current four-family key set.

## Sourced quotations

No sourced or attributed quotation appears in the audited keys. No quotation preservation action was needed.

## MCP evidence and display uncertainty

The required focus inspection and render routes succeeded for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97f6f9189d5eed9e051f94ec9dc70e084659408139b5f5d5889258e0ad5948be/f85f88bda8732b7adf98f857f096c3da24773f923fddd152936b70e4bb477a3b/focus-inspect.1178cf22a2daf3b8.json`
- Rendered HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c29dfe6b234078818639cb0ccb4b9d5bf390573ea8855d634a794d53747cdaf6/de9b19cd89d29c77b826fac1843787f165446c182dafba82229e53a20bcff7ee/independence_wave_focus_tree.focus.html`
- Rendered SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/0726879ab997d06da921c51d1dcf937fb4d3c07d716553ed88ec0f41c5cb7627/independence_wave_focus_tree.focus.svg`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14516e03405b7df3a0bdd2b48a0ec13f2db444d74bb86f72b7f3d1aa80e97c32/8b1ea34213200c8219904d1872c37a200077cea19f1224161f7602780490fdd5/independence_wave_focus_tree.focus.source-map.json`

The shared focus tree has no direct references to these cosmetic-name keys, so the focus render cannot exercise their runtime map, diplomacy, or country-header presentation. No country-name or flag presentation renderer is available through the installed HOI4 MCP routes. Visual overflow is therefore not directly rendered; confidence rests on the short label lengths and standard country-name key structure. This limitation is not treated as equivalent to live display evidence.

## Meaningful validation

- Compared the 60 expected name-ladder keys with every English localisation definition and confirmed exact one-to-one coverage.
- Traced every cosmetic identifier from definition through installation and cleanup effects, then compared it with the route documentation and asset manifest.
- Checked the complete added block for malformed keys, missing closing quotes, and unexpected dynamic tokens.
- Confirmed the file's BOM bytes directly.

## Skipped meaningful validation

- Runtime map, diplomacy, country-header, and tooltip-width presentation were not rendered because the installed MCP package exposes focus rendering but no country-name/cosmetic-tag presentation renderer.
- No live-game validation was performed; that consumer validation belongs to the user.

## Changed files and keys

- Audit report added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_nav_cosmetic_localisation_audit_2026_08_13.md`.
- Gameplay/localisation files changed: none.
- Localisation keys changed: none.
- Dynamic localisation added or fixed: none.

## Unresolved wording decision

Decide whether patron-client NAV should intentionally retain the civic country name or receive a fifth, route-specific cosmetic identity such as the already established `Protected Pyrenean Compact`. This requires owner coordination across cosmetic definition, three flag sizes, localisation ladder, installer/cleanup logic, and documentation; it is not a safe localisation-only edit.

## Simplifications, omissions, and blockers

No localisation simplification was made. The sole evidence limitation is the absence of a country-name/cosmetic-tag presentation renderer, and the sole content decision is the patron-client/CIVICX naming overlap described above.
