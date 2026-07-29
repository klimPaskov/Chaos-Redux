# Event 015 Utopia Manifesto Source of Truth and Resume Packet

Date: 2026-07-15  
Last reconciled: 2026-07-18

## Status

Event 15 is complete against its accepted specifications and plans in the frozen 2026-07-18 source snapshot.

Current focus-tree, country-package, decision-and-mission, English-localisation, spreadsheet/catalog, asset-package, improvement-loop, documentation, and whole-event gates pass. `completion_audit.md` is the current whole-event authority, SHA-256 `5a90b637478872d6f960c7e67630e0efd0fda3e17869bad2c094473596a12183`. Its 53-file runtime-text manifest SHA-256 is `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2`. The former FAIL snapshot previously stored at the same path, SHA-256 `be9d0be100eed6ccae223ed60db7ce36a07dc2f3eb38442b099799feab40a093`, is superseded historical evidence.

## Authority order

Use this order when sources disagree:

1. Live HOI4 source files are authoritative for implemented behavior and current identifiers.
2. `docs/events/015_utopia_manifesto/overview.md` is the canonical current mechanic description.
3. `docs/specs/015_utopia_manifesto_specs/specs/` is the accepted design authority, including the promoted implementation records in Parts 2, 4, 6, 7, and 8.
4. `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md` is the current implementation proof matrix, and `docs/plans/015_utopia_manifesto_plans/completion_audit.md` is the current whole-event completion verdict.
5. `docs/assets/015_utopia_manifesto/manifest.md` and `docs/assets/015_utopia_manifesto/gfx_handoff.md` are the visual index and wiring records. `subagent_handoffs/advisor_asset_final_audit_2026_07_18.md` is the current final asset audit authority.
6. The 2026-07-18 focus, decision, country, localisation, asset, spreadsheet, improvement-loop, and documentation records are evidence for their inspected snapshots.
7. Dated implementation handoffs are evidence and provenance, not continuing authority over later source.
8. Prompts, original planning handoffs, and old blockers are historical execution material.

## Exact current inventory

| Surface | Current count |
| --- | ---: |
| Event definitions | 106 |
| National focuses | 124 |
| Decisions | 121 |
| Main-system decisions | 105 |
| Evolution decisions | 15 |
| Prefire decisions | 1 |
| Missions | 44 |
| Main-system missions | 40 |
| Evolution missions | 1 |
| Prefire missions | 3 |
| Decision categories | 9 |
| Ideas | 50 |
| Characters | 24 |
| Institutional founder and successor entries | 8 |
| Institutional portraits | 4 |
| Advisors | 16 |
| Achievements | 14 |
| Cosmetic identities | 5 |
| AI strategy plans | 12 |

Twelve Event 15 definitions use documented `hidden = yes`: `.116`, `.150`, `.163`, `.164`, `.165`, `.205`, `.207`, `.212`, `.214`, `.216`, `.218`, and `.220`. Bridge `.165` validates Necessary Ground case-state, association-charter, settlement, supply, and island-lease founders after state-control changes. The event file contains zero `hide_window` uses.

## Implemented mechanic record

### Event entry and country transformation

- Event root is `chaosx.nr15.1`.
- Event type is Minor Fire-Once.
- An eligible weak country receives the manifesto through the current weighted selector.
- An AI recipient accepts.
- A human recipient can accept or reject.
- Acceptance initializes the Ledger, callings, ideas, actor pulse, event history, and replacement tree.
- Rejection performs the accepted cleanup and does not install the package.

### Living Ledger

The four displayed values are Need, Plenty, Concord, and Choice or Assignment. Each total is rebuilt as clamped base plus durable policy plus live contribution. Live contributions are replaced rather than accumulated, so an unchanged second refresh is idempotent. Refresh entry points are actor-scoped.

The decision category attaches `scripted_gui = utopia_manifesto_ledger_scripted_gui`. The GUI uses 46 audited sprite references and reports current value breakdowns, callings, active case, district state and role, reserve, route, and formation proof. The 10 case cards occupy the case presentation. The 7 district-role cards and 6 district-state overlays are paired on Stores and Settlements.

### Calling lifecycle

Six calling families maintain structural pressure, raw and effective durable adjustment, temporary adjustment, present severity, uncovered severity, and hysteresis. Material conditions can restore pressure after temporary relief. Necessary Ground and island-variant gates read the live relevant deficit.

### Evolutions

Five tracks expose 15 paid choices. Every choice installs a shared obligation that reaches a second Event 15 system. Consumers include the Ledger, callings, reserves, stores, districts, charters, league and association duties, defense, sponsorship, island and refuge obligations, and Necessary Ground conduct. Setup is idempotent.

### Districts

The four ordinary role families are market garden, industrial housing, rail junction, and refugee municipality. Provision Ring remains the distinct fifth achievement role. Survey suitability comes from current state facts. A full project proves housing or settlement preparation, transport, and role-appropriate industry, reserve, or calling support. Partial and failed terminals do not grant full role proof. Charter completion records route-specific obligations.

### Penal Works and exact Deaths integration

Closed Island can attach Penal Works to a valid active district. The method consumes manpower, infantry equipment, support equipment, reserve, and exact civilian population. It gives construction and local-supply output while adding garrison, resistance, conduct, and foreign-reaction costs. Completion, halt, failure, revolt, ownership loss, route exit, and terminal cleanup are explicit.

The Event 15 helper calls state-scope `apply_exact_state_civilian_population_loss` from `common/scripted_effects/chaosx_dynamic_effects.txt`. That shared helper passes the exact applied loss into `chaos_meter_register_deaths`. The cause is `constant:chaos_meter_deaths_reason.gulag_repression`, localised as "From camps and forced labor". Penal Works requests 500 loss on activation and 1000 on successful completion, with the shared minimum-population clamp deciding the exact applied value.

### Necessary Ground case architecture

- A case requires a live relevant deficit.
- Selected country and state targets use persistent founder-side arrays and IDs.
- Selected countries record founders in `utopia_manifesto_case_founders`.
- Selected states record founders in `utopia_manifesto_case_state_founders`.
- Cleanup removes only the current founder and preserves a shared marker while another founder remains.
- State-transfer methods require the target country to survive the selected transfer.
- Long supply uses exact resource rights and cleans them with `remove_resource_rights`.
- Temporary market access was omitted.
- Settlement lasts 365 to 540 days.
- Long supply lasts 540 to 720 days.
- Association duties last 365 to 540 days.
- Island lease starts at 2190 days.
- Renewal adds 1095 days.
- Counteroffer adds 730 days.
- Ownership loss calls `utopia_manifesto_reconcile_integrated_commonwealth_state_ownership`, which removes the integrated-state flag, modifier, and array entry.

Island-lease renewal reserves the exact founder and lessor on both countries before `.213` opens. Cancellation or replanning invalidates that exact pair without releasing its delayed slot. Every `.213` option still returns through `.214`; `.214` applies only a live exact-pair answer and always clears the answer and reservation. Founder teardown, lessor teardown, and annexation follow the same reverse links. A different pair remains independent, and the same pair can schedule a fresh full-duration request only after the earlier slot resolves.

Wargoal creation uses `meta_effect` to inject the exact saved state ID into its static generator. The private wargoal's `take_states` block also requires ROOT membership in the selected state's founder array and ownership by the exact target in PREV.

The target country records each exact founder in a reverse array. The annexation hook snapshots that array before target cleanup. Hidden founder-rooted bridge events carry the annexer and annexed target through regular event targets so ROOT-dependent lifecycle helpers run from the founder. The intended dispositions are successor adoption during active stewardship, founder-extinction conduct and stewardship failure, or clean pre-steward invalidation.

The selected state has an independent reverse founder array. The one-shot state-control hook snapshots it and fires hidden founder-rooted `.165` after one hour to validate each affected case independently. The delay lets a full annexation's `.163` disposition settle before state validation. One founder's cleanup cannot clear another founder's state link or authorize its wargoal.

### Association-charter reverse indexes

A completed association charter records exact founder, host, and state reverse indexes. Active association-duty target annexation fails and clears the duty. Later host annexation, founder withdrawal, founder teardown, or state ownership transfer away from the recorded host removes only the affected founder's charter link and preserves another founder's valid charter on the same state. The last-link cleanup removes the state modifier and flag. Ownership loss records Need and Concord consequences and refreshes external-network and formation proof. The same narrow `.165` bridge handles case-state and charter-state validation without a recurring world scan.

### Paid focus and dynamic-cost atomicity

The tree has 34 paid focus callers: 26 institutional and 8 military. Each caller uses the matching live affordability trigger, sets `cancel_if_invalid = yes`, refreshes and rechecks its current foundation, network, or capstone price at completion, deducts before generating proof or a formation, and keeps every later reward inside a payment-success guard. A last-tick affordability change fails closed: it takes no payment and grants no package reward, although the focus engine may already have marked the focus complete.

`on_state_control_changed` refreshes dynamic costs for accepted ROOT and FROM actors outside the Fallout-only callback guards. Exact founder snapshotting plus Ledger, island, and history-sensitive reconciliation remain guarded where intended. The frozen focus hash is `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` and the frozen on-actions hash is `73a06f68cc6ba23e61c51ba1c9610ff35586fee129623bea5f53478c09cf4037`.

## Formal improvement-loop promotion

`docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md` is accepted and implemented. Its original plan remains as provenance. The design has been promoted as follows:

| Finding | Implemented disposition | Canonical promotion |
| --- | --- | --- |
| Calling entry gate | actor-scoped structural seeding from current conditions | Part 2 and Part 7 |
| Living Ledger and calling lifecycle | durable and live layers, idempotent rebuild, hysteresis | Part 2 and Part 7 |
| Evolution choice consumption | 15 paid actions plus shared second-system obligations | Part 6 and Part 7 |
| District suitability and proof | four suitability roles, three obligations, partial and failed terminals, route charters | Part 2, Part 4, and Part 7 |
| Penal Works | paid Closed Island district method with exact state population loss and Deaths registration | Part 4 and Part 7 |

`docs/plans/015_utopia_manifesto_plans/subagent_handoffs/improvement_loop_closure_audit_2026_07_15.md` closes the formal improvement-loop gate with PASS and no open P0 through P3 finding. Promotion and closure remain separately recorded so the dated plan does not masquerade as its own validation.

## Working-plan dispositions

| Working record | Disposition | Current authority or reason |
| --- | --- | --- |
| `015_utopia_manifesto_formal_improvement_loop_addendum_2026-07-15.md` | implemented, promoted, and closed | accepted findings are in Parts 2, 4, 6, and 7. Closure audit PASS |
| `015_utopia_manifesto_final_improvement_loop_closure_2026-07-18.md` | STOP and closed | no broad gap remains and no further Event 15 addendum is authorized |
| `research/manual_improvement_loop_closure.md` | superseded as the active improvement plan, retained as provenance | formal addendum and closure audit replace the manual planning-stage substitute |
| `catalog/event_15_catalog_replacement_plan.md` | implemented and promoted | live catalog/workbook row and spreadsheet completion audit are current |
| `handoffs/implementation_sequence.md` | superseded execution plan, retained as historical order | live source, proof matrix, and this packet describe current state |
| `handoffs/subagent_orchestration.md` | superseded planning handoff, retained for reproducibility | the listed specialist roles later ran and their dated reports are indexed here |
| `handoffs/unresolved_verification_blockers.md` | superseded and resolved | its unmounted-repository and unavailable-reference conditions do not describe the current workspace |
| `matrices/asset_manifest_plan.md` | implemented and promoted | current asset manifest, GFX handoff, and focused validators are authoritative |
| `prompts/subagents/` and the other Event 15 execution prompts | historical/reproducible recipes, not open tasks | current report files record what actually ran |
| `completion_audit.md` | current whole-event PASS | SHA-256 `5a90b637478872d6f960c7e67630e0efd0fda3e17869bad2c094473596a12183`; the former FAIL at the same path, SHA-256 `be9d0be100eed6ccae223ed60db7ce36a07dc2f3eb38442b099799feab40a093`, is superseded historical evidence |
| This source-of-truth and resume packet | active | current authority order, gate state, limitations, and resume sequence |

No accepted working plan remains silently queued, and no Event 15 completion workflow gate remains open.

## Resolved architecture questions

### Temporary access

The package does not simulate a long-supply agreement through temporary market access. It grants exact resource rights and removes those rights at expiry or cleanup.

### Disappearing target

The accepted design uses exact country and state reverse founder records plus narrow annexation and state-control callbacks. It does not use a recurring world scan, arbitrary replacement search, or silent integration. Country disposition depends on stage and annexer relationship. State validation remains isolated by exact founder membership and saved state ID. Its one-hour delay gives a full annexation's country disposition priority. The final decision and mission re-audit passes the three founder-rooted bridges and multiplayer state-link contract with no open P0 through P3 finding.

### Agreement terms

All current term bands and lease extensions are centralized in Event 15 constants. The exact durations are listed above.

### Integrated state after ownership loss

The reconciliation helper removes state integration records when the actor no longer owns the state. A lost state cannot remain counted as integrated commonwealth territory.

## Country and idea package

The five cosmetic identities are:

- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH`
- `UTOPIA_MANIFESTO_COUNCIL_UNION`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND`
- `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH`

The 24 characters comprise eight institutional founder and successor entries plus sixteen advisors. Four people-free built-in ImageGen, vanilla-HOI4-style 156x210 institutional tableaux are shared by the eight institutional entries. Empty chambers, council tables, ledgers, apparatus, stores, seals, and route emblems represent the durable governing bodies without depicting people. The sixteen distinct 65x67 advisor dossier cards use independent fictional ImageGen portrait masters beneath the unchanged canonical `advisor_template.png`. Each complete source is resized to the native advisor canvas and uniformly fitted without warping before the template is applied once as the top layer. Focused provenance validation requires exact byte equality with the recorded built-in ImageGen objects for all sixteen advisor masters. The idea package contains 50 definitions across 12 pictures and keeps administration, social order, and institution lifecycles in separate concurrent slots.

The eight paid military templates and every matching `create_unit` payload resolve their player-facing names through `GetUtopiaManifestoMilitaryFormationName`. All eight localisation outcomes exist, so the former direct-string translation limitation is closed.

## Current visual authority

The current final asset audit passes with no P0 through P2 finding. The July 16 requirement-first crosswalk continues to cover all 24 accepted rows:

- 124 focus usages and 74 unique focus sprites
- 174 decision-map rows, composed of 9 categories, 121 decisions, and 44 missions
- 165 gameplay decision and mission assignments
- 50 idea assignments and 12 unique idea sprites
- 14 achievements and 42 active, complete, and failed variants
- 8 Ledger-seal, 8 Need, 8 Choice, 8 Assignment, and 10 formation source frames across the five required animation families
- 8 reserve-fill source frames as an additional runtime family outside the required-family count
- 46 unique scripted-GUI sprite references
- 33 static Ledger assets: 4 value icons, 6 Calling icons, 10 case cards, 7 district-role cards, and 6 district-state overlays
- 459 base sprite definitions plus 5 route-super-event definitions, with no duplicate names across all 464 registrations

Every active flag has a genuine built-in ImageGen source design and a flat heraldic runtime design. Twenty-one independent source designs plus four intentional engine-lookup aliases produce 75 TGAs. These are ImageGen-authored designs, not simple-shape substitutes. The finishing pipeline preserves generated geometry and tonal detail and does not quantize, trace, redraw, substitute motifs, impose a palette ceiling, or replace the generated work with simple shapes. The current final asset audit SHA-256 is `d2f659ac4e968a9d48ae3f346c1a7d9d5e1cb6b09b67f3be16a789662b583693`. The requirement crosswalk SHA-256 is `8cf869a2f6f53ee9119a2bf2148c6eff4efae8c70ceae6c6d0e052f7dcae19bd`. The current decision mapping CSV SHA-256 is `757ec0c51edca25b5453899f28816a3d34e8a5b330be268bed6ff4d27e0abcc0`.

`docs/assets/015_utopia_manifesto/final_icon_frame_audit.json` remains useful for the current animation and Ledger-binding records. Its decision-mapping subsection is frozen at 173 rows, 43 missions, and 164 gameplay assignments and is superseded for those three counts by the current mapping CSV plus the final decision audit.

## Final super-event package

Slots 96 through 100 select five distinct route images:

| Slot | Image |
| ---: | --- |
| 96 | `GFX_super_event_015_consent_of_households` |
| 97 | `GFX_super_event_015_common_table` |
| 98 | `GFX_super_event_015_guardians_of_measure` |
| 99 | `GFX_super_event_015_closed_island` |
| 100 | `GFX_super_event_015_joke_understood` |

The five entries use the title `UTOPIA HAS NEIGHBORS`, the accepted Thomas More quotation, route-specific descriptions, and `Nowhere has a timetable.`

Audio ID 57 uses `super_event_57_utopia_has_neighbors`. The source is the CC0 Musopen performance of Brahms, *Symphony No. 3 in F major, Op. 90*, third movement. Source evidence, license evidence, hashes, edit details, registries, and uniqueness proof are preserved under `docs/super_events/`.

The two older Event 15 super-event images are historical assets from the superseded two-image presentation. Their obsolete sprite registrations were removed and they are not route fallbacks. World Tension Subsides and placeholder language are historical catalog provenance only.

## Audit register

| Audit | Current result | Notes |
| --- | --- | --- |
| Direct integrated source validation | PASS for its dated inspected source, not a completion substitute | recipient gate, evolution paths, formation and proclamation gates, identity timing, no annex/core/claim formation effects, paid military growth, public parity, charter lifecycle, and asset registrations |
| Final focus-tree audit | PASS after one narrow P2 token correction, no open P0 through P3 finding | 124 reachable focuses and 388/388 focus-adjacent script-constant references resolve. Report SHA-256 `29ffa7c45d601bde8c90a4a717a4b19f4bcccab2ba92f0a832f232a499a043fa` |
| Final English-localisation audit | PASS after two idea-ID collision corrections and six prose-definition normalizations, no open P0 through P2 finding | 2,480 Event-owned definitions, all exact and case-folded unique, with no missing or unaccounted orphan key. Report SHA-256 `8d6e12652670782aef40259c263e18d306989d9134e7059b4e732dc4bc4a0e17` |
| Final country-package audit | PASS, no open P0 through P2 finding | Stress-matrix rows 40 and 45 and island renewal `.213`/`.214` pass. Report SHA-256 `ada264c49b233b0fb287693a5e685d57c0ee81eb91924b9c5b03bc86a3f72b1f`; its frozen 53-file runtime-text manifest is `F8E5F75FF910C753A8D1F2357933CA58931BE200E8CD6A03841FFD85B1A301E9` |
| Final decision-and-mission audit | PASS, no open P0 through P3 finding | 121 decisions and 44 missions, including 105/40 main, 15/1 evolution, and 1/3 prefire. Report SHA-256 `a5bb24e63977f5185872b1b11e0c054524a50816d1096a29a34cbaf20661826f` |
| Final asset audit | PASS, no open asset blocker | Choice and Assignment eight-frame packages, route presentation, and current bindings pass under the July 18 audit. Current advisor-card workflow and hashes are recorded separately in `docs/plans/gfx_icon_flag_mapmode_cleanup_plans/advisor_template_runtime_migration_2026_07_29.md`. |
| Current spreadsheet and catalog follow-up | PASS, no Event 15 workbook change required | `Events!A16:M16` matches 13/13 with normalized row SHA-256 `e330489603bd739e64fc356b8bb79498c4a34d54433f28cda4c2ba459dadab1e`. Current workbook SHA-256 `ed52b1f3ee3f0e602b3cc6a4b5fd7bc0d340445a3c085c6c8531fbcd2c0430f4`; follow-up SHA-256 `e0ba36c5805e0aca01b6bf74fec4f6dc29a24aecf4a3ec36382c334e5c741bd1`. The earlier `729e48a3135094d210b70e74ce3694ff0b66dbd5d2bc448051db931a41f4bd80` spreadsheet and localisation snapshots are pre-drift but Event 15-row-equivalent |
| Final improvement-loop closure | STOP and closed | No broad gap remains and no further Event 15 addendum is authorized. Closure SHA-256 `deaef9e886974048fa05c61c6cb2ca377bf4f0b43637a6476bf544a371c9a268` |
| Final documentation reconciliation | PASS for the pre-final documentation gate | `subagent_handoffs/documentation_final_audit_2026_07_18.md`; this is not the whole-event verdict |
| Former whole-event completion snapshot | superseded FAIL | Former path content SHA-256 `be9d0be100eed6ccae223ed60db7ce36a07dc2f3eb38442b099799feab40a093`; its 43-mission inventory and missing Choice/Assignment finding remain dated history |
| Final event-completion audit | PASS, zero open P0 through P3 finding | `completion_audit.md`, SHA-256 `5a90b637478872d6f960c7e67630e0efd0fda3e17869bad2c094473596a12183`; 53-file runtime-text manifest SHA-256 `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2` |

## Historical P2 waves and resolutions

The audit history remains part of the evidence record. Passing current reports do not erase earlier finding waves.

1. The 2026-07-15 focus completion audit recorded two P2 findings. Two focus textures were `95x85` instead of `94x86`, and one decision texture was `64x64` instead of `32x32`. The focus re-audit verified both focus textures at `94x86` and the decision texture at `32x32`, leaving zero focus-owned P2 findings.
2. The 2026-07-16 repaired asset snapshot recorded four P2 visual-completeness blockers. Compact value icons, six Calling icons, ten case cards, and seven district-role plus six district-state presentations were absent. The Ledger tranche supplied all 33 static assets and the Ledger architecture re-audit verified exact script, GFX, GUI, path, and dimension parity.
3. The former whole-event snapshot at `completion_audit.md`, SHA-256 `be9d0be100eed6ccae223ed60db7ce36a07dc2f3eb38442b099799feab40a093`, recorded the missing Choice and Assignment animation family. The separate eight-frame Choice and Assignment packages and current final asset audit close that defect. The fresh report now stored at that path is an independent current PASS rather than a reinterpretation of the old FAIL.
4. The 2026-07-18 focus audit found an undeclared `constant:utopia_manifesto_case_method.none` reset. The one-token `.none` to `.unset` correction closes that P2 and leaves 388/388 focus-adjacent script-constant references resolved.

## Resume order

1. Preserve `completion_audit.md` and runtime-text manifest `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2` as the frozen completion anchor.
2. The parent performs final diff review and creates the required plan commit.

## Completion result and evidence boundaries

- No fallback tree, fallback route, placeholder art, route-image substitute, generic country package, missing AI surface, or silent target integration is accepted by the canonical design.
- The two older super-event images remain historical files, are unregistered, and are not used as substitutes.
- The final whole-event completion audit passes with no open fallback, simplification, omission, blocker, or queued accepted plan.
- The current focus, country, decision, and localisation audits are source audits. They do not claim an exact-snapshot engine trace, rendered tooltip/layout inspection, AI distribution observation, or multiplayer interleaving observation.
- A final-tick paid-focus affordability race deliberately fails closed and can leave the engine focus completed without its package reward. It cannot grant a free proof, unit, or downstream reward.
- Exact original-leader restoration requires the recorded character to remain alive and eligible. The package does not fabricate a substitute.
- English is the audited language. The eight formation/template presentations now resolve through `GetUtopiaManifestoMilitaryFormationName`; the former direct-string translation limit is closed.
- The country audit documents an engine-level diplomacy-provenance limit: after Event 15 creates a boolean access or guarantee relation, script cannot distinguish a later non-Event-15 co-owner of that same engine relation.
- The country audit's earlier 53-file manifest predates the final localisation patch. The final whole-event audit supersedes it for combined current-state identity with runtime-text manifest SHA-256 `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2`.
- `final_icon_frame_audit.json` has a stale decision-mapping subsection. Current counts come from `decision_icon_mapping.csv` and the final decision audit. No asset file was edited during documentation reconciliation.
- Fresh HOI4 MCP focus, event, and GUI inspection attempts each stopped with `ARTIFACT_STORAGE_LIMIT` before producing diagnostics or artifacts. This is a tooling storage-retention limitation, not evidence of a source failure. Direct source evidence and current specialist reports remain available.

Event 15 is complete in the frozen source-level snapshot identified by the final audit and runtime-text manifest above.
