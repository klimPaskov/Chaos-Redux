# Event 006 localisation audit: decision, focus, DM-58, AFX, and treasury updates

Audit date: 2026-07-25.

Scope: read-only localisation audit after the current decision, focus, DM-58 reclamation-front, IW-006 AFX content-attestation, and independent-treasury changes. Gameplay files and the event spreadsheet were not patched by this subagent.

## Verdict

**FAIL for a clean Event 006 localisation closeout, with key coverage and encoding PASS.** Every checked Event 006 localisation reference resolves and all Event 006 English files retain the required BOM. The remaining failures are player-facing clarity and source-of-truth synchronisation: DM-58 gained claim-connected preflight and a finite success/failure transaction without result tooltip surfaces, the reclamation focus does not state that it authorises the paid mission, and the live IW-006 attestation set disagrees with current Event 006 documentation. The independent-treasury idea has complete localisation coverage, but its focus tooltip does not mention the idea's concrete industry modifiers.

## Missing key list

- **PASS — none found.** Decision `name` and `desc` keys, focus `id` and `_desc` keys, Event 006 event titles/descriptions/options, and all scanned custom effect and trigger tooltip references resolve to English localisation.
- **PASS — no missing custom-cost pair.** Every `custom_cost_text` in `common/decisions/006_*.txt` has the base key, `_tooltip`, and `_blocked` key in the English localisation set, including `independence_wave_cost_reclamation_front` at `localisation/english/006_independence_wave_decisions_l_english.yml:41,62-63`.
- **PASS — independent treasury coverage.** `independence_wave_independent_treasury` and `independence_wave_independent_treasury_desc` are present at `localisation/english/006_independence_wave_ideas_l_english.yml:10-11`.
- **PASS — AFX identity coverage.** `AFX_walloon_reserve_commander` is present at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and the emergency-command description uses the same display identity at line 91.

## Duplicate key list

- **PASS — none involving Event 006 keys.** A repository-wide scan found no Event 006 key defined more than once across `localisation/english/*.yml`.

## Scripted localisation issue list

- **PASS — no unresolved `localization_key` references.** All nine `common/scripted_localisation/006_*.txt` files resolve their `localization_key` values.
- **PASS — no undefined Event 006 scripted-localisation names found.** All `GetIndependenceWave...` names referenced by Event 006 source or localisation are defined in the Event 006 scripted-localisation files.
- **PASS — no raw trigger syntax in checked Event 006 English values.** The scan found no player-facing `has_`, `check_variable`, `NOT =`, `set_country_flag`, or equivalent script fragments.

## Dynamic text opportunities and player-facing clarity

1. **DM-58 result and failure surfaces are incomplete.** The source now requires `independence_wave_focus_reclamation_fronts_authorized` and `has_independence_wave_reclamation_front_preflight = yes` at `common/decisions/006_independence_wave_decisions.txt:3481-3491`. The preflight requires the minimum member count and one claim-connected external-state candidate per member at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:426-437`, and the resolver creates a finite take-state war goal only for a valid target at `common/scripted_effects/006_independence_wave_decision_effects.txt:661-708`. The current description at `localisation/english/006_independence_wave_decisions_l_english.yml:213-214` only says that synchronized fronts may succeed or break the league. The success branch, finite-count failure branch, and timeout branch at `common/decisions/006_independence_wave_decisions.txt:3505-3560` have no `custom_effect_tooltip` calls, unlike the other Event 006 mission families. The gameplay owner should add success, finite-target failure, and timeout tooltip calls and corresponding keys after deciding how much target detail is public; localisation alone cannot expose those outcomes.

2. **The reclamation focus does not name the mission it unlocks.** `independence_wave_focus_coordinate_reclamation_fronts` sets the authorisation flag at `common/national_focus/006_independence_wave_focus.txt:1925-1927`, while its title, description, and tooltip at `localisation/english/006_independence_wave_focus_l_english.yml:382-384` describe common matériel, experience, and revisionist pressure but do not say that the paid `Coordinate Reclamation Fronts` mission becomes available. Add that visible unlock wording when the parent decides the intended reveal level.

3. **The treasury focus tooltip under-describes its concrete reward.** The focus adds `independence_wave_independent_treasury` and the shared stabilisation bundle at `common/national_focus/006_independence_wave_focus.txt:384-392`. The idea supplies `consumer_goods_factor`, production-efficiency, and building-construction modifiers at `common/ideas/006_independence_wave_ideas.txt:156-164`, while the focus tooltip at `localisation/english/006_independence_wave_focus_l_english.yml:116-118` only says that capacity and stability improve. The idea description at `localisation/english/006_independence_wave_ideas_l_english.yml:11` is thematically accurate, so this is an opportunity to make the focus result legible rather than a missing-key defect.

4. **New category values use one-decimal formatting for integer-valued state metrics.** The changed descriptions at `localisation/english/006_independence_wave_decisions_l_english.yml:3` and `:5` print Legitimacy, Recognition, Government Capacity, Security, and Instability with `|1`. The underlying `independence_wave_country_value` constants are fixed-point schema values with integer current tuning at `common/script_constants/006_independence_wave_constants.txt:112-124`, so the parent should decide whether `|0` is the intended player display or whether one decimal is deliberate. This is a formatting review item, not an unresolved key.

## Cross-surface mismatch notes

- **Runtime attestation versus Event 006 implementation documentation.** The live gate at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-66` admits IW-001, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-019, and IW-184. `docs/events/006_independence_wave.md:13,17,85` still reports a seven-package set and says the ten-country bands fail below that capacity. `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:11,84,153,173` reports a nine-package set and still marks IW-006 as pending. The parent or documentation curator must choose the current attestation authority and reconcile those counts before making a completion claim.
- **Duplicated IW-006 admission comment.** The runtime trigger comment lists IW-006 among admitted packages at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:37-38` and repeats the IW-006 admission at lines 50-52. This is not a localisation key issue, but it is a stale/duplicated player-facing-source explanation that should be cleaned with the attestation documentation.
- **IW-006 live identity is current; old identity references are historical only.** Live localisation consistently uses Louis Hubert baron Ruquoy at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4,91`, and no `Marcel Delcourt`, `Rucquoy`, or alternate `AFX_independence_wave_*` key remains in `localisation/english/006_*.yml`. Older source-blocked portrait manifests and handoffs still mention Marcel Delcourt, for example `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/afx_jules_pire_source_blocked/manifest.md:20,25,44`; those files are historical evidence, but a documentation cleanup should mark them superseded rather than letting a workspace-wide search look like a live identity mismatch.
- **AFX attestation is intentionally absent from player-facing localisation.** No Event 006 English value mentions `attestation`, portrait audits, package admission, or runtime wiring, which is correct for hidden implementation gates. The public AFX text remains the Wallonia/Ruquoy alternate-history role wording at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:46-154`.

## File encoding concerns

- **PASS — all 33 `localisation/english/006_*.yml` files begin with UTF-8 BOM bytes `EF BB BF`.** Python `utf-8-sig` reads succeeded for every file and no Event 006 file had a malformed leading key or `:0` key suffix.

## Recommended fixes with file paths and keys

1. Parent gameplay owner: add DM-58 success, finite-target failure, and timeout `custom_effect_tooltip` calls in `common/decisions/006_independence_wave_decisions.txt:3521-3560`, then add the matching keys beside `independence_wave_coordinate_reclamation_fronts_desc` in `localisation/english/006_independence_wave_decisions_l_english.yml`.
2. Parent focus owner: update `independence_wave_coordinate_reclamation_fronts_tt` at `localisation/english/006_independence_wave_focus_l_english.yml:384` to state that the focus authorises the paid reclamation-front mission, without exposing hidden target-selection details.
3. Parent focus/localisation owner: decide whether `independence_wave_create_independent_treasury_tt` at `localisation/english/006_independence_wave_focus_l_english.yml:118` should mention reduced consumer-goods use, factory-efficiency gain, and building-speed gain in addition to the shared capacity/stability bundle.
4. Parent localisation owner: decide whether the changed category metrics at `localisation/english/006_independence_wave_decisions_l_english.yml:3,5` should use `|0`.
5. Documentation owner: reconcile the ten-entry runtime gate with `docs/events/006_independence_wave.md:13,17,85` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:11,84,153,173`, and remove the duplicate IW-006 admission sentence in the trigger comment.

## Patch and handoff record

- Changed files by this subagent: only this handoff file.
- Changed localisation keys: none.
- Dynamic localisation added or fixed: none; this was a read-only audit as requested.
- Before/after gameplay or display behaviour: unchanged by this subagent. The audit records current source behaviour and recommends follow-up text hooks, but does not add them.
- Fallbacks or simplifications introduced: none.
- Separate plan handoff: none; the actionable findings are recorded here for the parent-owned gameplay and documentation follow-up.

## Validation run

- Compared all Event 006 decision `name`/`desc` keys, focus IDs and descriptions, event titles/descriptions/options, and custom tooltip references against the complete English localisation set; no missing references were reported.
- Compared every Event 006 `custom_cost_text` against base, `_tooltip`, and `_blocked` keys; no missing cost pair was reported.
- Scanned all nine Event 006 scripted-localisation files for unresolved `localization_key` references and all Event 006 scripted-localisation names for undefined consumers; no issue was reported.
- Scanned all 33 Event 006 English YMLs for duplicate keys, BOM presence, malformed leading keys, `:0` key suffixes, and stale process labels; no Event 006 duplicate, BOM, key-shape, or stale-process-label defect was found.
- Read-only validation did not launch Hearts of Iron IV, alter the spreadsheet, or write gameplay files.

## Skipped meaningful validation and why

- No live game or consumer-session validation was run because repository instructions assign in-game validation to the user and this handoff was explicitly read-only.
- No GUI render was needed because the audit had complete source-level key coverage and no linked GUI artifact was supplied for the changed surfaces.
- No technology-tree viewer was available in the installed tool set; the treasury focus's industry bonus reference was checked statically against its source idea and focus reward.

## Unresolved wording decisions

- Whether DM-58 should reveal claim-connected target requirements and finite objective count in its description, or keep those as blocked-state detail while exposing only the public league-crisis consequence.
- Whether the focus tooltip should enumerate the treasury idea's three industrial modifiers or leave them in the idea panel.
- Whether one decimal place for the fixed-point state metrics is intentional.
- Which documentation surface is the authoritative IW-006/IW-010/IW-184 attestation count.
