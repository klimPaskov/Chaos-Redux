# Event 011 localisation tone audit handoff

## Result

The parent rewrite replaced the earlier bureaucratic report voice with distinct, concrete incidents.
The direct Event 011 reports, settlement events, public-reveal news event, five route-specific super-event descriptions, and compact GUI strings were audited together.
Five narrow wording fixes were applied, with no gameplay, route, secrecy, dynamic-scope, quote, or presentation changes.

## Files changed

- `localisation/english/011_secret_alliance_l_english.yml`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/event011_localisation_tone_audit_handoff.md`

`docs/super_events/011_secret_alliance/research.md` was inspected but not changed.

## Changed keys

- `chaosx.nr11.194.c`
- `secret_alliance_gui_lock_status`
- `secret_alliance_gui_select_card_tt`
- `secret_alliance_gui_clear_selection_tt`
- `secret_alliance_gui_toggle_animation_tt`

## Before and after

- `chaosx.nr11.194.c` changed from `Strike the innocent names.` to `Clear the innocent names.` so the option cannot be misread as an instruction to attack cleared suspects.
- `secret_alliance_gui_lock_status` changed from `Border conflict active: lead selection is locked until the crossing is settled.` to `Lead selection stays locked until the border conflict ends.` for directness and compact-panel fit.
- `secret_alliance_gui_select_card_tt` changed from `Select this developed lead for suspect-facing actions. Confidence and independent corroboration remain separate requirements.` to `Select this lead for actions against that country. Confidence and corroboration are checked separately.` to remove procedural jargon.
- `secret_alliance_gui_clear_selection_tt` changed from `Clear the selected lead without losing its accumulated evidence or confidence.` to `Clear the selected lead. Its evidence and confidence remain unchanged.` to remove the flagged `X without Y` mold while preserving behavior.
- `secret_alliance_gui_toggle_animation_tt` changed from `Set the confrontation emblem in motion or keep it still.` to `Turn the confrontation emblem's motion on or off.` for a shorter control tooltip.

No dynamic localisation was added or changed.

## Audit lists

- Missing keys: none found in the assigned direct event, super-event, or GUI set.
- Duplicate keys: none found in `011_secret_alliance_l_english.yml`.
- Scripted localisation issues: none found in the assigned GUI and super-event helpers.
- Dynamic text opportunities: no safe additional opportunity was needed because country names, state names, route descriptions, counts, faction names, phases, bands, and GUI lead state already use dynamic localisation.
- Cross-surface mismatches: none found.
- File encoding concerns: none found, and the localisation file retains UTF-8 BOM bytes `EF BB BF` after the patch.

## Prose-quality findings

- Vagueness: the old report abstraction is gone, and the current reports use concrete people, objects, places, and actions.
- Bloat: the direct event descriptions stay within compact scene-length paragraphs, and the five super-event descriptions remain one paragraph each.
- Obvious explanation: no event description restates its title or option, and the compact GUI tooltips now state only the control behavior and retained requirements.
- Repetition: no scoped text retains the flagged `without`, `while`, `not X but Y`, `rather than`, `can no longer`, `reports suggest`, or `the pattern` molds.
- Overcomplication: the ambiguous `Strike the innocent names` option and the GUI's `suspect-facing actions` wording were repaired.
- Style-rule repair: no em dash or sentence semicolon remains in the assigned text, and no staccato chain or generic list-then-explanation template required further rewriting.

## Super-event alignment and quote preservation

The following localisation lines match `docs/super_events/011_secret_alliance/research.md` exactly:

- `super_event_73_desc_hostile_war`
- `super_event_73_desc_pact_controlled`
- `super_event_73_desc_player_forced`
- `super_event_73_desc_fractured`
- `super_event_73_desc_weakened`

The locked title `THE PACT UNMASKED`, verified Sun Tzu quotation and Lionel Giles attribution, and button fragment `Look about you.` were preserved exactly.
All existing dynamic tokens and formatting codes in the assigned text were preserved.

## Validation and MCP evidence

- Targeted source checks confirmed the five super-event descriptions match the research note byte-for-byte at the localisation-line level.
- Targeted source checks found no duplicate key, scoped banned-mold, or missing inspected scripted-localisation helper.
- Event Chain Viewer scan revision `8ac996f680565cfe7d19f1fba4f12dc0c9c9bb81a0d620dfd20ace9b8a9ccd5a` produced source-linked options evidence at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eaaa2a03a5d59345f7d127ee5b80d2e80983cb0b275db4c61f80a0ea8d21171c/3ab9517825b409a282d605f8442b1c0d81bdf5a7023ee372423065d16a68c2e3/event-options-8ac996f68056.svg`.
- GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a3c27cfe8cb19133385ad253371961ae9a14229e967dda4cc34635f7a8d7d87/7374c660a492216fb4c882cf5ebd83e28845f97e8bda5e83134ff29e2afc12b1/gui-inspect.2bfe7ea43ae2034b.json`.
- Compact-panel render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4ee852ce09f603330f3cac65504ba9019e9aef444acf1d0d83eb3dec045b88a/e3f3ca604a26aeef642401eb65ea257e773b3ec05805167affde66d1818bd76d/secret_alliance_counter_network_container-full.svg`.

The GUI inspector hit its global source-graph diagnostic ceiling and reported `GUI_GRAPH_DIAGNOSTICS_TRUNCATED` plus `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`, so its workspace-wide overlap counts cannot be treated as Event 011-specific overflow proof.
The renderer produced the requested 500 by 250 panel artifact, but unresolved runtime country names and dynamic values prevent a conclusive worst-case long-name fit claim.
No in-game validation was performed or claimed.

## Unresolved wording decisions and skipped validation

No unresolved wording decision remains in the assigned set.
Live font metrics for unusually long dynamic country names were not available through the bounded render, so those names remain the only explicit presentation uncertainty.
No plan addendum was needed because the audit found no design-depth gap.
