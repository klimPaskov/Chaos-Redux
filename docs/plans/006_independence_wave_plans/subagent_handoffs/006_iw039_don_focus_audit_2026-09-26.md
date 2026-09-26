# IW-039/DON focus-tree audit — 2026-09-26

**Disposition:** Read-only audit of the five IW-039/DON shared focuses and their full-tree imports. No gameplay or localisation source was edited, and no direct-focus duplicate is proposed. The only file written by this audit is this handoff. The shared checkout already contained numerous unrelated and concurrent modifications when inspected; findings below describe the current source snapshot.

## Acceptance basis and scope

Part 4, lines 713–739, accepts the five root-level shared focuses, the branch-and-converge route, exact package and state-245 gates, paid rail and hearing receipts, service-quota authorization, government settlement, conditional emergency review, and the imported-node MCP limitation. Part 5, lines 90–118, accepts state 245 as the required DON anchor/capital, 238 as optional, excludes 218, protects SOV 219, and leaves FORM-11 as a separate later objective without an accepted carrier. The IW-039 addendum is partially promoted; its focus group appears at lines 67–82, while the broader package and FORM-11 proposals remain unresolved.

The audit covered:

- common/national_focus/006_independence_wave_don_focus.txt
- common/national_focus/006_independence_wave_focus.txt
- common/scripted_triggers/006_independence_wave_don_package_triggers.txt
- common/scripted_effects/006_independence_wave_don_package_effects.txt
- localisation/english/006_independence_wave_don_l_english.yml
- Supporting decision completion and full-tree package-admission gates where they affect focus reachability.

## High-priority findings

1. **Unresolved focus visibility refresh risk.** Every DON node uses allow_branch = { can_use_independence_wave_don_focus_group = yes }. That shared trigger requires has_complete_independence_wave_iw_039_don_package_setup, including package setup completion and origin_activation_ready (DON triggers, lines 177–184 and 253–263). The package setup calls independence_wave_assign_focus_framework and loads independence_wave_focus_tree at DON effects, line 359, before setting the DON/package setup-complete flags at lines 366–367. The shared assignment helper marks the layout dirty at focus effects, line 97; prepared-country activation sets origin_activation_ready later at independence_wave_effects, lines 870–891, with no focus-layout dirty call in that activation block. The offline focus wiki documents that allow_branch is checked when a tree is first loaded and must be refreshed with mark_focus_tree_layout_dirty when its condition changes (National focus modding - Hearts of Iron 4 Wiki.md, lines 420–422). Source order therefore creates a likely stale-visibility risk: available may become true later, but it does not itself make a hidden branch visible. This is not confirmed as an in-game manifestation because the user prohibited launching HOI4 and the focus MCP omits imported nodes. Parent review should resolve or explicitly carry this risk.

2. **Emergency civilian review can recheck its cost after payment.** The decision calls independence_wave_don_submit_emergency_mandate_for_review as its completion effect (006_independence_wave_don_decisions.txt, lines 247–266). The wrapper checks can_complete_independence_wave_don_emergency_review, pays 10 political power, and then calls independence_wave_don_complete_emergency_review (DON effects, lines 73–79). That completion helper checks can_complete_independence_wave_don_emergency_review again (DON effects, lines 187–195); the trigger includes the same 10-PP affordability predicate (DON triggers, lines 121–123 and 172–175). A route with exactly the accepted 10 PP can therefore pay the cost and fail to set independence_wave_don_emergency_review_complete, leaving Ratify the Millerovo Charter unavailable on the emergency route. This is a source-order finding, not a runtime observation. The elected, constitutional, and emergency government settlement wrappers do not share this specific problem: they precheck affordability, pay, and then call route setters that recheck structural requirements without checking the spent balance (DON effects, lines 45–70 and 111–166).

3. **Automatic package admission is still fail-closed outside the focus group.** IW-039 appears in the adapter allow-list at common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt, line 42, but is absent from the content-attestation OR list at lines 160–203. The runtime preflight requires both adapter support and content attestation at lines 208–212. The current package therefore cannot pass ordinary automatic admission until the parent promotes IW-039 content attestation after its required package audits. This is a broader package-admission gate, not a reason to duplicate these shared focuses.

## Route coverage

| Route step | Source and behavior | Audit result |
| --- | --- | --- |
| Register Millerovo Authorities | independence_wave_don_register_millerovo_authorities follows independence_wave_prepare_capital_administration; one prerequisite, 5 focus units. | Present and ordered as accepted. |
| Rail survey and petition hearing | independence_wave_don_survey_rail_and_remount_stores and independence_wave_don_hear_land_and_service_claims both require registration and are sibling lanes, each 5 units. | Present; both lanes are complementary, not mutually exclusive. |
| Set Service Quota | Two separate prerequisite blocks require both lane focuses (AND semantics); availability separately requires both paid receipt flags. Its effect also checks both focus companion flags and both receipts. | Correct convergence and receipt gate. |
| Ratify Millerovo Charter | Follows the quota focus; can_ratify_independence_wave_don_charter_focus requires the open charter mission, both paid receipts, quota flag, government receipt plus one government-route flag, and emergency civilian review when the emergency route is selected. | Source gate matches the accepted receipt/route order; source-order payment defect is resolved in the current follow-up below. |
| Charter success / FORM-11 | The successful mission callback sets the accepted internal later-gate flag independence_wave_don_form11_docket_open; failure and cleanup clear it. | Accepted flag-only scope: there is no current consumer, carrier, accession decision, or formation, and the focus does not form FORM-11 (Part 4, line 725; Part 5, lines 108 and 118). |

The focus costs are 5/5/5/7/7 units, 203 nominal days after the existing 35-day capital-administration focus, matching Part 4, lines 719–723. Vanilla focus prerequisite semantics and the offline wiki agree that separate prerequisite blocks are AND, while focuses inside one prerequisite are OR (National focus modding - Hearts of Iron 4 Wiki.md, lines 277–284).

## Exact focus gate and reward-only receipts

The shared gate in 006_independence_wave_don_package_triggers.txt, lines 177–184, requires an active Event 006 country, exact DON/IW-039 package generation, clear DHC runtime preflight, complete package setup, the full focus framework, the generic-focus contract, state 245 owned and controlled by DON and capitalized, and a non-failed charter. The underlying active-origin trigger requires the Event 006 origin flag/value and no ended-origin flag (006_independence_wave_triggers.txt, lines 9–13). The DON package-generation trigger requires original_tag DON, package ID iw_039, and the generation ID matching the current generation (DON triggers, lines 21–36). The anchor trigger checks 245 ownership/control and capital status (DON triggers, lines 70–73). Every focus repeats the shared gate in allow_branch and available; every reward helper rechecks the package gate, and the quota and charter helpers recheck their own receipts/route conditions (DON effects, lines 207–258).

The receipt boundary is correct in focus rewards. The rail and petition completion helpers set only their focus-companion flags (DON effects, lines 216–228). Paid project completion writes independence_wave_don_railhead_receipt and independence_wave_don_petition_receipt only in the timed project completion helpers after the decision completion callbacks (DON effects, lines 74–108; decisions, lines 98–168). The quota effect requires both receipts before setting independence_wave_don_service_quota_set (DON effects, lines 230–250).

Each government callback sets exactly one route flag together with independence_wave_don_government_receipt (DON effects, lines 111–166). The government requirements require an undecided route and no existing route flag (DON triggers, lines 141–158), so the current decision path selects one settlement. The current charter trigger explicitly requires both independence_wave_don_government_receipt and one of the three route flags (DON triggers, lines 188–200); the success-condition trigger repeats both (lines 203–214).

## Missing or simplified content

- The quota focus records an authorization flag and applies capacity, security, former-host-obligation, and network deltas; it does not define a numeric quota or expose a manpower/equipment/command-capacity-bounded force action. The addendum’s row at line 77 describes a bounded mobile-force commitment tied to those inputs and a depot receipt. Part 4, line 723, narrows the accepted behavior to a package-owned authorization “without creating a second force.” Treat the implementation as the narrower accepted authorization; the richer addendum force-commitment surface remains simplified/unimplemented, and the quota flag is consumed only by charter success gating and cleanup.

- FORM-11 remains flag-only for later gating. Charter success sets independence_wave_don_form11_docket_open and failure/cleanup clear it (DON effects, lines 300–305, 327–336, and 453–492). The current source has no consumer, decision, carrier, accession action, or formation. This matches Part 4, line 725, and Part 5, lines 108 and 118. Current localisation describes the federation question as a later, separate settlement rather than an available current action (DON localisation, lines 16 and 59).

- The imported shared-node geometry, overlap, and normal-zoom visual route clarity remain unverified by MCP. Do not add direct-focus duplicates; the limitation is explicitly accepted in Part 4, line 715, and the addendum, lines 80–82.

## Icon coverage

Each focus uses a distinct reused Event 006 sprite. The corresponding base and _shine sprite names are registered in interface/006_independence_wave.gfx, lines 3–22, and all five DDS paths exist. The shared-node MCP render does not display these nodes, so this confirms source wiring and file presence, not rendered icon appearance.

| Focus ID | Base sprite | Shine sprite | DDS exists |
| --- | --- | --- | --- |
| independence_wave_don_register_millerovo_authorities | GFX_goal_independence_wave_founding_administration | GFX_goal_independence_wave_founding_administration_shine | Yes |
| independence_wave_don_survey_rail_and_remount_stores | GFX_goal_independence_wave_infrastructure_authority | GFX_goal_independence_wave_infrastructure_authority_shine | Yes |
| independence_wave_don_hear_land_and_service_claims | GFX_goal_independence_wave_popular_councils | GFX_goal_independence_wave_popular_councils_shine | Yes |
| independence_wave_don_set_the_service_quota | GFX_goal_independence_wave_army_integration | GFX_goal_independence_wave_army_integration_shine | Yes |
| independence_wave_don_ratify_the_millerovo_charter | GFX_goal_independence_wave_former_host_settlement | GFX_goal_independence_wave_former_host_settlement_shine | Yes |

## Localisation and reward mismatch list

All five IDs have matching title, description, and reward-tooltip keys in localisation/english/006_independence_wave_don_l_english.yml, lines 45–59. No focus key is missing.

| Focus ID | Title / description / tooltip coverage | Reward alignment |
| --- | --- | --- |
| independence_wave_don_register_millerovo_authorities | All three present. | The effect adds 5 legitimacy, matching the reward tooltip. The updated description says the offices may act in the provisional council’s name (line 46), without implying that the charter is already ratified. |
| independence_wave_don_survey_rail_and_remount_stores | All three present. | The focus enables the paid railhead project and does not grant its receipt or stores. The updated tooltip says the council can commission the paid survey (line 50), describing the player action without implementation wording. |
| independence_wave_don_hear_land_and_service_claims | All three present. | The focus enables the paid hearing, and its updated tooltip says the council can convene it for host and non-host claims (line 53). The decision callback remains the only writer of the paid receipt. |
| independence_wave_don_set_the_service_quota | All three present. | The effect adds security, capacity, former-host obligations, and network standing. The updated description and tooltip at lines 55–56 name those effects; they do not promise a second force or numeric equipment purchase. |
| independence_wave_don_ratify_the_millerovo_charter | All three present. | The focus marks charter ratification; mission success publishes only the accepted later-gate flag. The capstone and success tooltip say the federation question is recorded for a later, separate settlement (lines 16 and 59). No current accession action or FORM-11 formation is promised or wired, matching the accepted boundary. |

## Focus AI behavior

All five focuses define ai_will_do. The shared constants resolve to 10 for standard and 25 for high (006_independence_wave_constants_registry.txt, lines 1743–1753).

| Focus ID | Base score | AI gap |
| --- | ---: | --- |
| independence_wave_don_register_millerovo_authorities | 10 | Static score; no node modifier. |
| independence_wave_don_survey_rail_and_remount_stores | 25 | Static score; ties with the other three high-score focuses when eligible. |
| independence_wave_don_hear_land_and_service_claims | 25 | Static score; ties with the rail survey when eligible, which suits complementary branches. |
| independence_wave_don_set_the_service_quota | 25 | Static score; prerequisites/receipts block it until valid. |
| independence_wave_don_ratify_the_millerovo_charter | 25 | Static score; shared gates and government/review receipts block it until valid. |

No exact-ID ordered-focus or strategy factor was found in the searched AI strategy sources. The full Event 006 tree gives an urgent selection factor to an active full-framework country, but the focus inspector excludes the imported DON candidates. The constant scores are source facts, not a route probability analysis.

The required read-only chaosx_ai_probability_auditor pass ran through hoi4.probability_inspect/evaluate. The source-file inspect returned PROBABILITY_SOURCE_DISCOVERED with zero weighted candidates (source revision ed84fec89eb9fd85075b1aace5e95f6c5ae638529e5b86d1aa1b1abfa7071a4a; source hash be227d2d99f20d3d88b416b82446d6802e0b58a5002b5f528da36a34946db62d; artifact link below). The full-tree inspect found 184 direct focus candidates with poolComplete=false and zero of the five DON IDs. A targeted-pool evaluation returned PROBABILITY_SURFACE_EMPTY before any scenario was analyzed; candidate-pool and external-factor completeness are unresolved, and no scenario hash/analysis ID was produced. Named cases included setup/no receipts, one vs both receipts, the three settlements, emergency review pending/complete, and invalid-origin/package/capital probes. The invalid-package case did not encode a wrong package ID, and the capital probe supplied no state-scope fact. No probability, ranking, sweep, comparison, render, simulation, or sequence result is claimed. The previous 2026-09-26 completion audit’s AI pass had no result; this handoff adds the current explicit source-discovery and empty-surface evidence.

## MCP evidence and references

The correct importer, common/national_focus/006_independence_wave_focus.txt, was passed to hoi4.focus_inspect and hoi4.focus_render for tree independence_wave_focus_tree. Both returned ok, no blockers, and zero DON-specific diagnostics. Current inspect revision: 0f73798f59f1a197ae0964f90698c957f8731744efd6e5cc0380588b3e13abc3. Layout hash: a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7. The projection contains 184 direct nodes and excludes the imported shared DON definitions.

- [Current focus inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d3941e2e95181e47bf3127eb6a273a76cf9e19b7df3e7eb2e56ad1c7e0a0d37/c66d0fd121b4b481d1069f9375e466e7637eda968ad16b85b8c1f756e5d1fecc/focus-inspect.0f73798f59f1a197.json)
- [Current focus SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/78058f286662531158497680801d618c7e70876bf6c25293eaec268b2312e842/independence_wave_focus_tree.focus.svg)
- [Current focus JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2427d341ab44eb6bff85b6381510245fdc22d2bdf7ace2c5796798bde9806726/a172c93d956bc0d032b69fc4155620123bb5a2ae81ff4c59e2f5cfa6315eb689/independence_wave_focus_tree.focus.json)
- [Current focus source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/951c7f480a787b1dffc3cff3c1943117d68a043382d9f29292c489e7a566b345/3347e13c6830afc4723c9499627717af9b8af0954a5b0096c894e5002121e8f1/independence_wave_focus_tree.focus.source-map.json)
- [Focus-weight probability source inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/414471741b8f3b37bb07241acb0fa4c7e5b694966da2e7f5c76518c1fefd3616/ab481effca3369a0b8c08a56d0c808130486f6fc0a217d0bf8d3c90f3b761938/probability-inspect-be227d2d99f2.json)
- [Parent-tree candidate-pool inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b1df5b0b5a851b0d889672a40a804fca72bc36bfd7c29e7114a4a7576e295d4/24e4077cacad404cde1aa617ea4c8b628b38777ccc562d1c9063a40368466068/probability-inspect-8812fee8dd4b.json)
- [Targeted DON-pool receipt](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3826ba91f4e9580c2e5158e0541f07bf1313be1295e1be9ae40f0ba7a0feca04/6b7fde6e7a46f01eabe9ef046b904960b713fd8d6f3a74ad6a844bcf65f77854/probability-inspect-8812fee8dd4b.json)

Other MCP findings: long connector independence_wave_adopt_military_archetype_program to independence_wave_adopt_reclamation_doctrine spans 10 columns, unrelated to IW-039; vanilla continuous focus continuous_restrict_freedom lacks description localisation, unrelated. This is distinct from imported-node exclusion: the former are actual MCP diagnostics, the latter is a coverage limitation.

The connected tool list did not expose hoi4.reference_context, hoi4.reference_search, hoi4.reference_read, or hoi4.source_lookup. The offline wiki National focus modding page was read directly for AND/OR prerequisites, available versus allow_branch, focus AI scores, root-level shared-focus imports, and _shine sprite names (relevant spans: 277–292, 333–335, 409–422, 604–625, 818–824). The installed documentation folder has no focus-specific documentation file; the vanilla shared-focus source precedent at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\national_focus\austro_hungarian_releasable_shared.txt was inspected. The reference-route gap and local source paths are recorded here; no web wiki was used.

## Validation and limits

- Task-specific validation completed: current source route graph, package gates and effect call sites, receipt writers, localization coverage/reward wording, icon/shiny registrations and DDS file presence, full-tree focus inspect/render, and specialist focus-weight probability audit.
- No HOI4 launch or live-game observation occurred, as instructed. MCP import exclusion prevents rendered layout/overlap/icon proof for the five nodes.
- No source patch was authorized. No tests or unrelated validation suite were run.

## High-priority parent follow-up

1. Resolve the emergency review's affordability recheck after payment and refresh focus-tree visibility after the group gate is truly satisfied; preserve the imported shared-focus architecture.
2. Keep the IW-039 content-attestation gate closed until parent-required package audits are accepted; then verify focus group visibility and route availability through the normal admitted package.
3. Preserve FORM-11 as a flag-only later gate; the accepted carrier, accession action, and formation remain unresolved by design.
4. Keep the quota at the accepted authorization-only scope, or request a new accepted design if a manpower/equipment-bounded mobile-force action is intended.
5. Obtain a complete imported-node candidate-pool AI analysis when the adapter supports shared focuses; no numeric balance target is established here.

## Parent follow-up recheck — current source, 2026-09-26

**Disposition:** The parent-reported fixes were rechecked in the current shared checkout. This section supersedes the earlier emergency-review, focus-visibility, unused-docket, and quota-localisation findings above where noted. No gameplay or localisation source was edited in this follow-up; this section was appended as requested.

| Earlier finding | Current source check | Recheck |
| --- | --- | --- |
| Emergency review could spend 10 PP and then fail a second affordability check. | The guarded wrapper still checks can_complete_independence_wave_don_emergency_review before payment, then deducts the cost. The completion helper now checks only is_independence_wave_don_emergency_review_open before setting the completion flag (DON effects, lines 73–79 and 227–239; DON triggers, lines 172–175). | **Resolved in source.** The helper no longer rechecks the spent PP balance. |
| allow_branch could remain stale because focus layout was dirtied before setup readiness. | independence_wave_activate_prepared_country_origin sets independence_wave_origin_activation_ready, then for package ID iw_039 with the DON setup flag calls mark_focus_tree_layout_dirty (006_independence_wave_effects.txt, lines 890–897). The DON failure effect sets charter_failed before refreshing, and exact-generation cleanup clears the DON package/route gates before refreshing (DON effects, lines 326–335 and 453–490). | **Resolved at source-order level.** The refresh runs after the relevant readiness or gate state changes. This removes the earlier stale-visibility source-order risk. |
| FORM-11 scope was previously described as a removed docket flag. | The current source restores independence_wave_don_form11_docket_open as a flag-only later gate: charter success sets it; failure and cleanup clear it. A current source search found no consumer, decision, carrier, accession, or formation. The success and Ratify strings say the federation question is recorded for a later, separate settlement (DON localisation, lines 16 and 59). | **Confirmed accepted boundary.** The flag remains; no current FORM-11 action or formation is implied. |
| Quota text omitted the former-host obligation increase and implied a force action. | The quota description and reward tooltip now state the mounted-service commitment, security/capacity gains, added former-host obligations, and network-standing gain (DON localisation, lines 54–55). These align with the quota helper’s current deltas (DON effects, lines 270–290). | **Resolved for player-facing wording.** The implementation remains the accepted authorization/delta reward; it does not create a second force. |
| Player-facing route/receipt flags were not localized. | The localisation file now has keys for the DON setup-complete flag, all three government-route flags, charter ratified/failed, and the railhead, petition, and government receipts (lines 3–12). | **Resolved for these exposed flags.** |

### MCP visibility and layout status

The source-order refresh now supports the conclusion that the imported branch should be re-evaluated after setup readiness. Runtime visibility is still unobserved: the current focus MCP projection excludes all imported DON shared nodes, so it cannot certify their visible state, placement, overlap, or icon appearance.

The fresh importer inspect/render both returned ok with no blockers and zero DON-specific diagnostics. The current inspect revision is b4eb144da36811cc2b8155fd1cab3970e222cd905689cc2cc6c52230bd0cfc7a; the layout hash remains a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7. The projection still contains 184 direct nodes only. The only warnings remain the unrelated 10-column connector from independence_wave_adopt_military_archetype_program to independence_wave_adopt_reclamation_doctrine and vanilla continuous_restrict_freedom missing its description localisation.

- [Current follow-up focus inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f9a6f420d46d8a55e95300d780bcf14b6c4232fbd5b3b7c3880fc63c420f0d3/fd66eb6832b829aba2e3801c690f5bf04e01590b80fb15b3d1261505feb3eaaf/focus-inspect.b4eb144da36811cc.json)
- [Current follow-up focus SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/53c7ee8d4b2b0caf1e3e5942ee1a9f1a69c1d6e3098087d987701601a2822e79/independence_wave_focus_tree.focus.svg)

### Probability blocker recheck

The five focus scores are unchanged in source: registration uses independence_wave_focus_ai.standard = 10; the other four use independence_wave_focus_ai.high = 25 (DON focus file, lines 32, 55, 78, 104, 127; constants registry, lines 1743–1754). They remain static bases without per-focus modifiers.

The fresh chaosx_ai_probability_auditor pass returned no numeric result. Direct probability inspection returned status=ok, code=PROBABILITY_SOURCE_DISCOVERED, and zero weighted candidates (revision 36f08ad82630a9385c946983b0bcb54f96c4a77c7cf1e3523ea0c0b57b5e7afe; source hash be227d2d99f20d3d88b416b82446d6802e0b58a5002b5f528da36a34946db62d). Importer inspection returned status=ok with 184 direct candidates and zero matches for the five imported DON IDs (revision 5b87b504b9937791276e6a639f419400d757629a495e1a31987ff6954aa2afa9; source hash 8812fee8dd4be1579b8159b1f58cc9ce0ced48823331dcfd33fac693f13ef83f). Evaluation of scenario set iw039_don_shared_focus_current_source_2026_09_26 returned status=error, code=PROBABILITY_SURFACE_EMPTY, before analyzing any scenario. Its cases were setup/no receipts, both receipts/no government, elected assembly, constitutional compact, emergency review pending/complete, invalid origin, unbound invalid package ID, and state 245 not capital. No scenario hash, analysis ID, score trace, or probability was produced. Candidate-pool and external-factor completeness remain unresolved, including focus history, package/generation variables, missions, state scopes, and active strategy context. No sweep or comparison was warranted with zero matched candidates and no weight change.

- [Fresh direct-focus probability inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43343c74a2b762c2151e9516d1da456c68b24d6e014dc21997c67ff06c1068d6/98277f891976ee10ffcd05fc7a0feb60169b778fc4b5cbc7ba6702ca1377cff4/probability-inspect-be227d2d99f2.json)
- [Fresh importer candidate inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4df1bfb11689d1636c7398682667c37d1d1671e65bacdf11302fd30993cc4085/e40bc7c97ca7db95eb52768a787dfd9ddbe313c8576ccec938de1017a1393d35/probability-inspect-8812fee8dd4b.json)

- [Current direct-focus probability inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43343c74a2b762c2151e9516d1da456c68b24d6e014dc21997c67ff06c1068d6/98277f891976ee10ffcd05fc7a0feb60169b778fc4b5cbc7ba6702ca1377cff4/probability-inspect-be227d2d99f2.json)
- [Current importer candidate inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4df1bfb11689d1636c7398682667c37d1d1671e65bacdf11302fd30993cc4085/e40bc7c97ca7db95eb52768a787dfd9ddbe313c8576ccec938de1017a1393d35/probability-inspect-8812fee8dd4b.json)

### Remaining limits

The IW-039 content-attestation gate remains absent from the central package preflight list, as recorded in the earlier handoff; package admission remains fail-closed pending parent acceptance of the required package audits. The current focus MCP still cannot prove imported-node layout, and the probability adapter still cannot analyze the five shared-focus weights. No live-game validation was performed.

The current capstone checks both paid project receipts, the quota flag, independence_wave_don_government_receipt plus one government-route flag, and emergency-review completion when emergency host staff is selected. These checks run inside the full focus-group gate, which requires active Event 006 origin, exact DON/IW-039 generation, complete setup, the full-tree/generic-focus contract, and state 245 owned, controlled, and capitalized. Part 4, line 725, accepts success as setting only the internal later-gate flag; the current focus does not create an accession action or formable.

