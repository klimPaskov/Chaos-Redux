# IW-039/DON Country Package Audit — 2026-09-26

**Disposition:** blocked for package admission. Static inspection is complete; required probability, technology, and campaign-state evidence remains blocked, so the current tree must remain HOLD / PARTIAL.

**Workspace:** C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

**Scope:** read-only audit of the supplied IW-039/DON specifications, addendum, package source, shared package dependencies, mechanic reference, and three named handoffs. Narrow direct dependencies were read only where needed to verify the actual-host pointer, p39 force path, DHC interlock, vanilla DON OOB, and the four affected vanilla state records. No game was launched, no map rewrite was performed, and no source or content-attestation file was changed.

**Accepted basis:** state 245/Millerovo is the required anchor and capital; state 238/Volgodonsk is optional; state 218 is excluded; SOV must retain state 219; Event 005 DHC and IW-039 are mutually exclusive in both orders; the alternate-history council grants host and non-host petition rights; the three settlements are elected host assembly, constitutional district compact with civilian oversight, and time-limited emergency host staff with civilian review; the vanilla DON_cossack_host opening divisions are suppressed and p39 mounted_mobile is applied once per generation after a valid muster; FORM-11 remains separate with no carrier selected; Sidorin reuse is blocked; the vanilla DON flag ladder is reused; and the five root-level shared focuses remain without direct-focus duplicates.

**Parent affordability basis:** the charter mission lasts 420 days; the serialized railhead project costs 25 PP and lasts 75 days; the petition project costs 20 PP and lasts 45 days; one government settlement costs 30 PP immediately; the constitutional compact adds 10 CP; and emergency civilian review costs 10 PP within 90 days. No factory cost or repeatable 500-infantry/100-support/5,000-manpower purchase is accepted. No event incidents were accepted or added.

## Gate recommendation

Do not admit IW-039 or add its package to compile-time content attestation from this static review. The implementation has coherent source gates for the accepted tag, footprint, force, and charter contract, but attestation is withheld, the mandatory probability pass did not return, imported focus layout remains unproved, the technology routes timed out, and campaign-state scenarios for the DHC order interlock, rollback, and force muster remain unexecuted.

The package may advance as a source-audit packet for parent review. That does not pass the admission or attestation gate.

## Findings by severity

### Blockers

1. **The runtime adapter is registered but IW-039 is absent from compile-time content attestation.** The adapter whitelist includes package ID iw_039 at common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:42. The attestation whitelist at the same file, lines 160–202, omits iw_039, while preflight at lines 208–211 requires both the adapter and attestation checks. The automatic readiness predicate and Region-04 candidate gate depend on that preflight at common\scripted_triggers\006_independence_wave_triggers.txt:899–907 and common\scripted_triggers\006_independence_wave_package_region_triggers_registry.txt:345–353. This is a fail-closed admission boundary, not an authorization to edit attestation.

2. **The mandatory AI probability audit produced no evidence.** Weighted surfaces in the named package include the Region-04 weighted candidate pool at common\scripted_effects\006_independence_wave_package_region_effects_registry.txt:946 and 974–984, five focus ai_will_do blocks at common\national_focus\006_independence_wave_don_focus.txt:32, 55, 78, 104, and 127, and decision/mission ai_will_do blocks at common\decisions\006_independence_wave_don_decisions.txt:53, 95, 131, 167, 190, 214–218, 240–244, and 267. The required chaosx_ai_probability_auditor subagent was spawned read-only with fork_context=false, but errored before returning its scenario analysis because the account hit its usage limit; the tool reported retry at October 2, 2026, 10:53 AM. No probability inspection, evaluation, sweep, comparison, or rendered artifact was delivered to this handoff. No direct probability-tool fallback or numeric balance claim was substituted.

3. **Dynamic admission scenarios remain unproved.** No campaign execution or save-based validation was performed. Required unresolved cases include 245-only versus 245+238 release, province-valid muster and single p39 application, rollback after setup/final-validation failure, both Event 005/006 orders including the force-all DHC path, SOV-219 survival, and charter completion/failure under the accepted budget. The Event MCP view is partial and does not execute the package helpers or state transfers.

4. **The required technology view did not complete.** The source depends on the shared opening-technology inheritance effect, not a DON-specific technology tree: common\scripted_effects\006_independence_wave_force_effects.txt:790–803 calls inherit_technology on the captured former-host target and sets research slots. The exposed hoi4.tech_inspect scan and hoi4.tech_render summary calls each timed out awaiting tools/call after 180 seconds. No technology inspect/render artifact was produced, so source review is not technology-engine evidence; no source change was made that would require a tech comparison.

### Medium findings

1. **The imported DON focus layout remains blocked in MCP.** The root tree imports the five accepted DON nodes at common\national_focus\006_independence_wave_focus.txt:95–100, and the five definitions are present in common\national_focus\006_independence_wave_don_focus.txt:11–128. Current focus inspect/render report 184 direct nodes and omit the imported DON nodes. The user explicitly retained this shared-focus architecture and rejected direct-focus duplicates, so do not create a fallback tree to satisfy the renderer. Attachment, placement, overlap, and native visibility still need parent acceptance evidence.

2. **The DHC interlock is source-wired but not campaign-proved.** IW-039 candidate and final-preflight gates call the DHC guards at common\scripted_triggers\006_independence_wave_package_region_triggers_registry.txt:345–353 and common\scripted_triggers\006_independence_wave_don_package_triggers.txt:265–284. The opposite-side guard at common\scripted_triggers\005_006_liberations_collision_triggers.txt:73–82 blocks Event 005 DHC creation while DON is reserved, pending, prepared, or active; both the ordinary trigger and force-all transfer effect call that guard at common\scripted_triggers\005_soviet_collapse_triggers.txt:8194–8208 and common\scripted_effects\005_soviet_collapse_effects.txt:23503–23531. The source gates cover both directions, but no runtime event-order or transfer case was executed. The prior DHC handoff reports a static SCN-008 matrix witness, which is not engine behavior evidence.

3. **Several player-facing localization strings need clarification.** No broken localization reference was found among the audited references, and the localization auditor found no duplicate keys among the 84 DON keys and confirmed UTF-8 BOM encoding. However:
   - localisation\english\006_independence_wave_don_l_english.yml:4 says “under Don control,” while the mission requires state 245 to remain owned, controlled, and the capital; the source trigger is common\scripted_triggers\006_independence_wave_don_package_triggers.txt:70–73.
   - Localization lines 43 and 46 say the focuses “open” projects but describe the project receipts indirectly; the actual paid actions and timers are common\decisions\006_independence_wave_don_decisions.txt:98–165.
   - Localization lines 32–37 use “issue focuses,” “paid receipts,” and “review window” instead of naming the survey, hearing, Millerovo control, and civilian review.
   - Localization line 63 colors both PP and CP red when either constitutional cost is short; no native decision-row render was available to confirm the blocked-cost presentation.
   - Localization lines 48 and 75 use technical or ambiguous prose for mounted-service commitment and residents outside the host.
   - The cost hover strings at lines 55–67 repeat amounts already shown by the cost row and omit the 75-day and 45-day project durations.

4. **The DON decision category has no description key.** common\decisions\categories\006_independence_wave_categories.txt:66–74 defines independence_wave_don_millerovo_charter_category without a description field, and localisation\english\006_independence_wave_don_l_english.yml:2 supplies only its title. No dangling localization reference exists because the category source does not request a description, but the decisions-missions skill asks for category descriptions.

5. **Two earlier specification status sentences are stale against current source.** Part 4 line 691 and Part 5 line 80 still say IW-039 package implementation and country-specific focus work remain queued, while Part 4 lines 713–741 and Part 5 lines 100–120 record the accepted focus group, implementation evidence, and current HOLD/PARTIAL gates. Reconcile those earlier status sentences without changing the accepted evidence boundary. Part 5 line 98 is current: it says the cost/timing contract is accepted and reflected below.

6. **Some earlier addendum wording can misclassify accepted scope boundaries as missing package work.** The user’s current decision is that no event incidents are accepted or added and FORM-11 stays separate with no carrier selected. Part 5 line 108 records the no-carrier boundary, while the addendum at lines 134, 173, and 180 still describes incidents and the FORM-11 carrier as outstanding or unresolved. Keep proposed incident sketches and a future FORM-11 accession design outside this package’s required implementation; their absence is not an IW-039 defect.

### Low-severity identity boundary

The separate Technology Tree Viewer was checked independently from the MCP tools in the current addendum at docs\plans\006_independence_wave_plans\006_event6_iw039_don_package_improvement_addendum_2026-09-26.md:164 and was absent from Windows PATH, the Codex plugin cache, Roaming npm, and Local Programs. My bounded command/path check also found no viewer command, Local Programs match, or viewer-named top-level entry in the npm/Codex plugin directories. The HOI4 technology routes are exposed in the tool list, but their two calls timed out, so viewer absence must not be confused with technology-route unavailability or health.

## Country package coverage checklist

- **Tag, origin, generation:** source pass. The package uses the existing DON carrier, requires a dormant candidate and candidate-origin availability, rejects a living DON owner for state 245, verifies exact package ID and current-generation receipt, and requires active Event 006 origin before package use.
- **State footprint:** source pass with scenario limit. Reservation names required anchor 245 and optional compact 238; state 218 is not in the IW-039 reservation call; when the former host is SOV, setup/runtime requires SOV ownership of state 219.
- **DHC exclusion:** source pass; campaign-order proof missing. Source guards cover DHC existence/receipt, Event 005 ownership/control/reservations of 218/238, DON pending/prepared/active markers, and the IW-039 optional 238 reservation.
- **Actual-host pointer:** source pass. The former host is stored from the release target, validated against DON and the protected-state owner, used for technology inheritance, and used by the former-host ledger synchronization.
- **Force and vanilla OOB:** source pass; campaign muster proof missing. p39 maps to mounted_mobile, tradition 82, five accepted reinforcement paths, no navy/air inheritance, and one current-generation application after anchor control checks. Setup deletes only the vanilla Kavaleriyskaya Diviziya template before applying the dynamic force.
- **Focus framework:** source pass; imported layout blocked. Five root-level shared focuses use the full framework and state-245 gate; their AI weights lack the mandatory probability receipt.
- **Decisions and mission:** source pass for costs, serialization, success/failure, and cleanup; native cost-row display and campaign affordability remain unverified.
- **Ideas and assets:** all package idea identifiers exist, lifecycle changes are source-wired, and the five focus, idea, decision, and mission sprite registrations and DDS files checked here exist. No new portrait, flag, cosmetic tag, advisor, commander, leader, or GUI dependency is present.
- **Political setup:** the three route choices map to democratic/elections-allowed for the assembly and compact, and neutrality/elections-disabled for emergency staff. Package cleanup restores the vanilla DON neutral ruling party, elections allowed, and 30/20/30/20 popularity baseline. It does not undo direct stability or war-support outcomes, which remain part of the settled or failed charter result.
- **FORM-11 and incidents:** source pass for the accepted boundary. Charter success sets only independence_wave_don_form11_docket_open; failure clears it; no carrier or automatic formation effect is selected. No incident events were accepted.
- **Technology, industry, production, and supply:** package uses former-host technology inheritance and slot floor, dynamic p39 stockpiles/force, and no factory cost or explicit production line. No technology identifier is directly granted by the DON adapter. State 245 is infrastructure 3/local supply 8; optional 238 is infrastructure 2/local supply 0. Dynamic supply, stockpile, and division-placement outcomes were not campaign-tested.
- **AI and playability:** source contains focus, decision/mission, and Region-04 weighted-selection surfaces. Their scenario-specific behavior and quantitative balance remain blocked by the failed AI auditor run and absent runtime scenarios.

## Map and state evidence

The current read-only map inspection selected states 218, 219, 238, and 245 at map revision e24f4f807eb245771b5bf388c80184799cdb6e6b5ffaa78c16bdf55c7f31c79d. The state-layer render included ports, victory points, resources, buildings, supply nodes, railways, and adjacencies and returned MAP_RENDERED. No map rewrite or map-file change was made.

The map inspector did not return the selected state records inline. The static values below are from the installed vanilla state files, not inferred from the render:
- 245-Donetsk.txt: state 245 is rural, Soviet-owned/core, infrastructure 3, Millerovo VP 1, local supplies 8.0, and no factory.
- 238-volgodonsk.txt: state 238 is rural, Soviet-owned/core, infrastructure 2, Volgodonsk VP 1, local supplies 0.0, and no factory.
- 218-Rostov Area.txt: state 218 is Soviet-owned/core, city category, VP 15, infrastructure 3, local supplies 3.0, and contains factory/air/naval buildings; IW-039 never reserves it.
- 219-Moscow Area.txt: state 219 is Soviet-owned/core, has the Moscow VP, infrastructure 4, and local supplies 6.0; package checks ownership when SOV is former host, but does not check controller.

The map inspector’s overall validation was false because its map-wide diagnostic set was truncated: 2,654 building-position and floating-harbor errors were omitted, and the first surfaced examples point to other states in map/buildings.txt. Since the diagnostic payload was truncated, this audit does not claim a clean whole-map locator pass or that no selected-state locator defect exists. The package itself makes no state-history, railway, port, factory, supply-node, or province-position edit.

## Source-level setup, rollback, and cleanup

The planner applies the anchor reservation first; compact state reservation is attempted only for compact-or-higher territory and a failed optional compact is recorded as a trim without invalidating the candidate at common\scripted_effects\006_independence_wave_package_planner_effects.txt:523–560. The IW-039 reservation wrapper in common\scripted_effects\006_independence_wave_package_region_effects_registry.txt:969 names only states 245 and 238.

The DON setup effect at common\scripted_effects\006_independence_wave_don_package_effects.txt:324–373 checks can_initialize_independence_wave_iw_039_package before setting the current generation, assigning the 245 capital, provisioning the accepted paths, loading the p39 mapping, deleting the exact vanilla OOB template, applying the force once, and publishing the setup-complete flags and founding mission. The valid-muster trigger at common\scripted_triggers\006_independence_wave_triggers.txt:202–230 requires valid profile/tradition, at least three paths, command roster, generation, former-host and anchor targets, anchor ownership/control by the released country, and absence of a force receipt for the current generation. The DON postcondition further requires all five exact paths, p39, mounted_mobile, expected path count 5, force-applied flag, capital 245, and no air/navy inheritance at common\scripted_triggers\006_independence_wave_don_package_triggers.txt:214–251.

The p39 table maps to mounted_mobile value 6, tradition 82, reinforcement mask 654, inheritance mask 0, and research-sensitive value 0 in common\script_constants\006_independence_wave_constants_registry.txt:1799–1814, 2022–2066, 2236–2280, 2450–2494, 2664–2708, and 2878–2922. The expected five-path count is 5 at line 1990. The package loader consumes these mappings at common\scripted_effects\006_independence_wave_force_package_effects.txt:356–416, and the shared force effect writes the current generation receipt only after materializing the force at lines 871–890.

The former-host target is captured into the released country’s persistent variable at common\scripted_effects\006_independence_wave_effects.txt:736–737. The Don host-delta wrapper calls the shared former-host ledger path at common\scripted_effects\006_independence_wave_decision_effects.txt:27–38 and common\scripted_effects\006_independence_wave_effects.txt:974–987, 1022–1075; technology inheritance uses the same saved former-host event target at common\scripted_effects\006_independence_wave_force_effects.txt:790–803.

If initialization or final validation does not commit, common\scripted_effects\006_independence_wave_effects.txt:950–953 calls independence_wave_reset_current_generation; that reset dispatches package cleanup first at lines 468–481, and the dispatcher includes DON at lines 3813–3840. DON cleanup removes its missions, decisions, package ideas, generation marker, route flags, receipts, and failure flags at common\scripted_effects\006_independence_wave_don_package_effects.txt:441–490. This is source evidence for country/package cleanup, not proof of state-transfer rollback or campaign-time recovery.

## Politics, ideas, decisions, and assets

The three government choices are mutually gated by the receipts and undecided route, with the emergency choice blocked outside war and the constitutional AI score modified in war at common\scripted_triggers\006_independence_wave_don_package_triggers.txt:141–159 and common\decisions\006_independence_wave_don_decisions.txt:170–244. The emergency review is an active 90-day mission and charter completion waits for its receipt if emergency staff was selected at common\scripted_triggers\006_independence_wave_don_package_triggers.txt:162–211.

The timed railhead and petition decisions pay up front through complete_effect, wait for their accepted durations, publish receipts only on successful removal while Millerovo still qualifies, serialize against each other, and do not refund the paid PP when interrupted. The source and localized cost keys match the accepted values; the budget handoff’s day-347 result assumes uninterrupted state/capital control and no competing political-power spending, so it is a calculation rather than campaign affordability evidence.

The Don idea lifecycle in common\ideas\006_independence_wave_ideas_registry.txt:4610–4693 covers emergency stores, secured stores, unratified mandate, all three settlements, civilian review, chartered service, and fractured charter. The package removes/replaces the appropriate ideas on rail project completion, government selection, civilian review, charter success/failure, and cleanup. Their existing GFX registrations are in interface\006_independence_wave.gfx:58–65; decision/missions at lines 69–79; focus icons at lines 3–22. The referenced DDS files exist. No new visual source or portrait-specific wiring was created.

## MCP and reference evidence

- Focus inspect returned FOCUS_INSPECTED at revision 0f73798f59f1a197ae0964f90698c957f8731744efd6e5cc0380588b3e13abc3: 184 direct nodes, layout hash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7, no blocking diagnostics. Focus render returned FOCUS_RENDERED at the same layout hash; it does not include the five imported DON nodes. [Inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98e4a357c306d7563472473059039b46ea9df889dec60d248a57b5a7eeb6f97f/3168123a16350d42037eccc2d3686fc23779559a575d75c7d25e181155747a70/focus-inspect.0f73798f59f1a197.json) and [rendered SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/78058f286662531158497680801d618c7e70876bf6c25293eaec268b2312e842/independence_wave_focus_tree.focus.svg). The inline source inventory was truncated at 64 of 92/91 paths. Its one long-connector diagnostic and missing vanilla continuous-focus localisation are unrelated to DON.
- Event 006 trace/render and Event 005 DHC trace/render returned EVENT_INSPECTED_PARTIAL and EVENT_RENDERED_PARTIAL at revision a29827c827624d500d049a257e56797e0f7fb54939bf0f0fc3b3ca70acd46d37. Focused reports had zero helper projections, 8,910 unresolved nodes, 2,193 diagnostics with no blocking diagnostics, and omitted over 42,000 nodes. They show event graph structure, not shared helper semantics, DHC transfer ordering, rollback, or campaign outcomes. [Event 006 trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64b0bf606c7f78b6990e2e5a3457feee8d831c513a6d23fa8754b97d16ef080c/223c7b44327971b03c7941ac6e1f8860d32fc331d959cf28746f5f7b5ca49ec8/event-trace-a29827c82762.json), [Event 006 render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74719dadcae3f93ed520ade56c65a388f0cedb94c66343d8f7c12eaa62bd46ac/5cae9ec4704f545f7b420ad9ca5d1b14ad2232ec13de493703d1cdceab7a780d/event-neighborhood-a29827c82762.svg), and [Event 005 render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfcdc3e9c38f9b968dd08ad434dbd627974120412fa88817595c77674c9628b5/c206f605d6f9fad9c598d6351ef70ee7980640392e693b78752a134d4e943043/event-neighborhood-a29827c82762.svg).
- Map inspect selected four states at revision e24f4f807eb245771b5bf388c80184799cdb6e6b5ffaa78c16bdf55c7f31c79d; the full searchable JSON is [here](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e0165d14c86626561fab5e2da301a2c9199e63593ff11a35807b6262d295fe8/5e2a91c6c8539b159b5d9685080faa702537077af5972ddc09aa0d81713cec7a/map-inspect.e24f4f807eb24577.json). Map render returned MAP_RENDERED; the [state-layer render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/895fb10be7067b2414fb65390e7a58d1125bafbee3b8ed036d1e52ed95e15c88/2b8c31071056d5dfaf7a73b4bcce967903ee1fd05d7709b9055caf3998ae6438/map-state.png) is an offline representation.
- hoi4.tech_inspect and hoi4.tech_render were exposed but both timed out after 180 seconds; no tech artifact exists. The standalone viewer absence is recorded separately above.
- hoi4.reference_context, hoi4.reference_search, hoi4.reference_read, and hoi4.source_lookup were not exposed. Relevant local Paradox wiki and installed documentation sections were read directly, with hashes below; no web reference was used.

## Local reference revisions

| Source | Sections/lines used | SHA-256 |
|---|---|---|
| paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | inherit_technology at 1941; delete_units at 2047–2049 | 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C |
| paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md | PREV/event_target scopes at 262–270; has_active_mission at 649; state ownership/control at 1847 | ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06 |
| paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | Event targets at 263–305 | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| paradox_wiki\National focus modding - Hearts of Iron 4 Wiki.md | shared focus imports at 68 and 824; AND/OR prerequisites at 277–288; focus AI at 604–620 | BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203 |
| paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md | custom costs at 314; timed decisions at 339–355; missions at 467–478 | 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md | create_unit at 3278–3301; delete_units at 3506–3516; inherit_technology at 4686–4690; set_research_slots at 7641–7646 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md | has_active_mission at 3022–3028; is_owned_and_controlled_by at 6079–6086 | 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\units\DON_cossack_host.txt | exact template and 15 matching divisions at lines 1–180 | 9C53DD97D9270E5B9C1EE3198B1D30B00C3A0207D72569573BB9E25182E2D18F |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\DON - Don Republic.txt | ruling-party/election baseline at 68–73; popularity at 75–80 | 1E6F0806D11567B458A4E3B7CEA09B6561328B9DD86E4EA20D988C6A2371E4CC |

## File-surface checklist

The following supplied files were inspected in the shared working tree:

- [x] docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md
- [x] docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md
- [x] docs/plans/006_independence_wave_plans/006_event6_iw039_don_package_improvement_addendum_2026-09-26.md
- [x] common/scripted_effects/006_independence_wave_don_package_effects.txt
- [x] common/scripted_triggers/006_independence_wave_don_package_triggers.txt
- [x] common/scripted_effects/006_independence_wave_effects.txt
- [x] common/scripted_triggers/006_independence_wave_triggers.txt
- [x] common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt
- [x] common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt
- [x] common/scripted_effects/006_independence_wave_package_region_effects_registry.txt
- [x] common/scripted_effects/006_independence_wave_package_planner_effects.txt
- [x] common/script_constants/006_independence_wave_don_constants.txt
- [x] common/ideas/006_independence_wave_ideas_registry.txt
- [x] common/decisions/006_independence_wave_don_decisions.txt
- [x] common/decisions/categories/006_independence_wave_categories.txt
- [x] common/national_focus/006_independence_wave_focus.txt
- [x] common/national_focus/006_independence_wave_don_focus.txt
- [x] localisation/english/006_independence_wave_don_l_english.yml
- [x] docs/events/006_independence_wave/systems/iw039_don_millerovo_host_charter.md
- [x] docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_don_dhc_interlock_implementation_2026-09-26.md
- [x] docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_don_flag_and_affordability_review_2026-09-26.md
- [x] docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_don_vanilla_sidorin_portrait_reuse_audit_2026-09-26.md

**Specs and plan:** reviewed Part 4 focus architecture, Part 5 country package/regional overlay, and the 2026-09-26 IW-039/DON addendum.

**Package script:** reviewed DON package effects and triggers, shared Event 006 effects/triggers, package dispatch triggers, Region-04 package triggers/effects, package planner effects, DON constants, and idea registry.

**Player content:** reviewed DON decisions, the DON decision category, the full Event 006 focus tree, the DON shared-focus module, and English DON localization.

**Documentation and prior evidence:** reviewed the Millerovo charter mechanic reference, DHC interlock handoff, flag/affordability review, and Sidorin portrait reuse audit.

**Direct dependencies checked narrowly:** shared package-origin triggers; decision host-ledger effects; force mapping and force creation effects; DHC collision triggers and Event 005 creation trigger/effect; interface\006_independence_wave.gfx and referenced focus/idea/decision DDS assets; vanilla DON OOB and state/country history. No broad audit of unrelated country packages was performed.

## Worktree and changes

The supplied checkout was already dirty before this audit. The following in-scope paths were modified or untracked before the requested handoff: common\decisions\categories\006_independence_wave_categories.txt; common\ideas\006_independence_wave_ideas_registry.txt; common\national_focus\006_independence_wave_focus.txt; common\scripted_effects\006_independence_wave_effects.txt; common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt; common\scripted_triggers\006_independence_wave_package_region_triggers_registry.txt; common\scripted_triggers\006_independence_wave_triggers.txt; the Part 4 and Part 5 specs; the IW-039 addendum; and the new DON decisions, focus module, constants, package effects/triggers, localization, mechanic reference, and affordability handoff.

This audit added only docs\plans\006_independence_wave_plans\subagent_handoffs\006_iw039_don_country_package_audit_2026-09-26.md. No country source, shared gameplay source, map data, assets, or content-attestation entry was changed. No game, save, test suite, or static scenario matrix was run by this subagent; the existing DHC handoff’s static matrix result is not treated as runtime evidence.

## Remaining admission questions

1. Can the parent admit the package only after adding its attestation entry and re-running the compile-time preflight? The current source correctly blocks admission until that decision.
2. What scenario evidence will prove 245-only and 245+238 ownership/control/capital/supply, valid province muster, exact OOB suppression, and one p39 force application?
3. What runtime cases will prove DHC-first, IW-039-first, ordinary DHC, force-all DHC, and optional-238 reservation safety?
4. Does the parent accept the missing imported-node focus layout evidence as a current blocker until the MCP resolver can display the shared nodes?
5. Can the technology viewer/service provide a focused view of the inherited-host tech dependency once available?
6. The 90-day emergency review and 420-day charter feasibility calculation assumes uninterrupted control and no competing PP spending; a scenario run is still missing.
7. The standard decision UI cost row was not rendered, so the red-state cost clarity and text fit remain unverified.

**Static-source admission decision:** not safe to promote to IW-039 package admission or content attestation. It is safe to forward as a source-level audit packet for parent review, provided the listed MCP, probability, and campaign-scenario blockers remain explicit.

**Skills used:** chaos-redux-subagents, chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-event-assets. The focus-tree, decision/mission, localization, and event-completion audit subagents returned read-only findings. The required AI probability auditor was attempted but failed at the account-usage gate described above. No skills were created or edited.

