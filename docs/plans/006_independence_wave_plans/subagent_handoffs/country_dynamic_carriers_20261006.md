# Event 006 Dynamic Carrier Scope Audit

Disposition: implemented for the owned non-weighted carrier references. The Pacific decision AI modifiers and the FORM-05 host-threat AI helper remain queued for the parent probability pass. No country identity redesign or fallback was introduced.

Basis: D34 in docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md states that AFX, AGX, AJX, ARX, ASX, GZX, and HBX carriers are created with create_dynamic_country. Their runtime tag is dynamic, so a literal X-tag scope reaches no released country. The parent assigned this bounded correction and reserved the weighted surfaces for a baseline audit.

## Country Package Coverage Checklist

- Confirmed the affected package ids are resolved through dynamic original tags AFX, AGX, AJX, ARX, ASX, GZX, and HBX inside global.independence_wave_active_countries.
- Confirmed the FORM-03, FORM-05, FORM-02, FORM-04, and FORM-48 carrier scopes retain their existing route, package, readiness, territory, and consent checks. The bounded lookup adds active-origin and active-country array-alignment guards.
- Confirmed the FORM-04 state proof still requires RHI to qualify at state 51 and the live AJX carrier to qualify at state 42, own and control the anchor, be at peace with RHI, and neighbor RHI.
- The read-only map lookup found all requested states 1, 34, 36, 42, 51, 114, 115, 331, 378, 629, and 684 in the map catalog. The 42 and 51 state tile rendered with adjacency, coast, and port overlays.
- No map files or state definitions were changed. No missing state ids were found in this bounded lookup.
- Political setup beyond these carrier contracts, leaders, portraits, flags, advisors, parties, focus trees, starting forces, technology, industry, supply, and production were outside this subtask and were not audited. No portrait or flag asset work was performed.

## Findings and Changed Surfaces

Before the patch, the listed static country scopes and the AJX neighbor and war targets could not reach the released dynamic carrier. Formation requirements, post-formation member reports, consent accounting, and carrier-specific scripted text could therefore remain false or fail to update.

After the patch, trigger and scripted-localisation checks use any_of_scopes over the active-country registry, with original_tag, aligned-array, and active-country checks before the original package and consent conditions run. Effect paths use deterministic for_each_scope_loop with an inner if.limit over the same registry. Their effect bodies and PREV relationship remain intact.

The deterministic loops have zero or one valid FORM-03 carrier because the active-carrier trigger requires the exclusive global LCX identity and an exact registered package. FORM-05 charter startup requires independence_wave_form05_charter_in_progress to be clear and sets one global in-progress identity. Active-country registration rejects a duplicate THIS entry, and its reconciliation removes duplicate country and generation rows. The loop therefore changes no probability or selection result.

Changed files:

- common/scripted_effects/006_independence_wave_form03_effects.txt: dynamic carrier lookups in independence_wave_form03_join_active_carrier_as_autonomous_member, independence_wave_form03_initialize_late_autonomous_member, independence_wave_form03_apply_member_settlement_to_host, independence_wave_form03_report_current_member_to_carrier, independence_wave_form03_record_member_language_ratification, independence_wave_form03_record_member_corridor_completion, and independence_wave_form03_leave_autonomous_membership.
- common/scripted_effects/006_independence_wave_form05_effects.txt: dynamic carrier consent accounting in independence_wave_form05_accept_invitation.
- common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt: FORM-02 GZX strict preconditions and FORM-04 AJX eligibility, connectivity, and founder proof.
- common/scripted_triggers/006_independence_wave_form03_triggers.txt: carrier partner, consent, connected-member, active-connection, and sovereign-associate checks.
- common/scripted_triggers/006_independence_wave_form05_triggers.txt: prospective and active carrier connections, live post-formation connection, minimum consent, and autonomous-member checks.
- common/scripted_triggers/006_independence_wave_form48_triggers.txt: the HBX member and invitation check in has_independence_wave_form48_exact_founding_ledger.
- common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt: FORM-03 and FORM-05 ledger, capital model, accommodation, integration, phase, language, member status, outcome, and plain-text selectors.

Audited with no change:

- common/scripted_effects/006_independence_wave_form01_02_04_effects.txt already evaluates GZX and AJX with original_tag while walking the frozen member registry. It had no static GZX or AJX country scope.
- common/scripted_effects/006_independence_wave_form48_effects.txt only scopes vanilla HAW and FSM. It had no static HBX country scope.
- The state-puzzle triggers already use the bounded active-country registry and original_tag for these custom carriers.

## Release and Final Validation Review

The parent-owned release path in common/scripted_effects/006_independence_wave_execution_effects.txt creates AFX, AGX, AJX, ARX, ASX, HBX, and GZX through create_dynamic_country, reserves each dynamic country, saves its event target, and calls independence_wave_materialize_custom_carrier. Its startup helper scopes carrier-specific setup by original_tag.

The shared country setup assigns independence_wave_generation_id before package setup and registers active countries in parallel with generation ids. independence_wave_reconcile_active_registry checks a candidate country against the generation stored in the matching registry row and removes stale or duplicate rows. The formable member and anchor ledger walk repeats the generation check before adding a candidate. The commit trigger routes FORM-02, FORM-03, FORM-04, FORM-05, and FORM-48 through their family-specific strict readiness, territory, and consent proofs.

These shared release, registration, and commit files were read only. They remain parent-owned.

## Validation and MCP Evidence

- Script validation was run on all seven changed script files. The route returned SCRIPT_CHECK_PARTIAL for each file with zero findings, zero unresolved commands, and no truncated findings. It returned valid = null because argument blocks were unchecked and the scripted-effect or scripted-trigger roots had unknown scope. Counts were 198 unchecked argument blocks for FORM-03 effects, 55 for FORM-05 effects, 55 for the combined FORM-01/02/04 triggers, 28 for FORM-03 triggers, 33 for FORM-05 triggers, and 64 for FORM-48 triggers. Scripted localisation is unsupported by this validator, with zero commands checked. These are partial results, not full passes.
- Post-conversion source_lookup artifacts confirm for_each_scope_loop blocks in FORM-03 effects at line 193 and FORM-05 effects at line 218 under source revision 25297b85a7b784a9419d53bd4f1500e55f5d0c42f1cee6957682d64a302390a6.
- Post-change source_lookup confirms current FORM-02/04 triggers, FORM-03/05/48 triggers, and the localisation registry under revisions ece587a64247314975509e197c1872d033b3a82ebdbc297f530cd7cf953c4f4f and a1cedb0f771cde8cf35796feb7abc3f93779bc3ea662d77af9277da74785274f.
- Read the offline wiki Triggers section at paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md lines 639-640, revision abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06. It distinguishes the static tag trigger from original_tag, which includes countries created with create_dynamic_country.
- Read the offline wiki Data structures sections at line 1149 and line 1218, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4. any_of_scopes checks array scopes. for_each_scope_loop executes effects for each scope in the array and changes scope. The separate reference_search request for for_each_scope_loop took too long and was cancelled, so this syntax was checked directly in the offline file. The parent completion audit located and read the installed effects documentation for for_each_scope_loop at lines 4296-4311 under revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
- Installed effects documentation section create_dynamic_country was read at lines 3033-3045, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af. Installed triggers documentation sections any_of_scopes at lines 1531-1545, has_war_with at lines 5051-5059, and is_neighbor_of at lines 5997-6005 were read under revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
- Offline wiki Decision modding target rules at lines 519-530, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, were read alongside the installed Country Decisions documentation at lines 1-46, revision 5e7e686b5582f32c38d898d805e17171e88f4c0fdbf6f2e3f5b3c117a3be4f81.
- Vanilla source_lookup located game:common/decisions/YUG.txt at line 811, revision fcba7008c46a7663a05b255473bad2edab6713a0385206d01174219388f7cb5d. The underlying YUG_ustasa_uprising decision creates dynamic CRO and stores its live country scope.
- Map inspection was lookupOnly for the 11 anchor states listed above, with map revision 72ba1a65ae696aba5e1979f34b4acbefedc338a2f9bd33543469a73501a62ebd. The all-state render exceeded MAP_AREA_TOO_LARGE. A focused state render for states 42 and 51 succeeded with adjacency, coast, and port overlays at the same revision. Useful artifacts: map lookup JSON at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d74469b4139c0ad41c511c2cb4b78d4d3ec2c2af0e445e68389bc7d37f6849b3/d2012171581606847c55471c238e4b665298fd38cb3e63a4ff92c058dcd6bb48/map-lookup.72ba1a65ae696aba.103939852373c4dc.json and focused map tile JSON at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79d55331dba166593d18ab2b47610bfbb0680cd8a0dc98200111aafa6e05e22a/9645770191ce3dffb48b785a9e7a01aab04c1d32d1030208f7134fe208a9cedf/map-state-tile-25c9bc198ea8.json.
- Event inspection and render targeted chaosx.nr6.300. The inspect revision is e11d0418a6f78fc27a817d5b93053cd5f3c8dc28eaacf81409bcad262a262918. The neighborhood render revision is 6dd4a1b7e9309d65f0852f05539362a5231935900beebb51d89726a6b22ef737 and selected three nodes. Both summaries report global partial coverage with 2,285 diagnostics and one blocking count. The parent reviewed the filtered lint evidence and confirmed only informational acknowledgment-option warnings at chaosx.nr6.35, chaosx.nr6.305, and chaosx.triggerable_scenarios.81. No dummy effects were added. Useful artifacts: event lint at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d11da0f6915fb238d6fb8410b19e8dd8ad2db6edc81517fcff952c2c494c6069/220e9366c9c49ad2e936a04e760547d4cd735684073787d30ab5d3dd6f43f81c/event-lint-e11d0418a6f7.json and neighborhood JSON at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5baff736da75af8f738fa1ed12a5fe9f1bf16d0d0d8dfb6842d792a4a381a85/fcd361b69e1a071d378517eef1cf0b8976a630323d84af04bdea322d0845b783/event-neighborhood-6dd4a1b7e930.json.
- Decision inspection for independence_wave_haw_authorize_pacific_delegation used scenario haw_1936_scenario_unspecified with actor HAW, date 1936.1.1, and empty state. It returned DECISION_ANALYZED_PARTIAL at source revision 17650168ce91c11e3f1f3cd44c4e65e9633a2496b2f8e6faf57207209fc21622, with 100 unresolved definitions and decision coverage false. The linked artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be2aedcac8f9398aad636cd025bae704e6e455b10b02d0e94ab149295816285c/9da37d07faf451ea8c5448c2acd2aabe8da5c4f58d314642902653b14cb7f25a/decision-afd8f49f4734fc49bbb2e80a.json. The FSM decision was not individually inspected because the decision route returned broad partial coverage and the parent is routing the required probability audit.
- No spreadsheet or CSV file was edited. No game process or desktop window was opened. Live country and event behavior remains for user validation.

## Remaining Issues and Parent Follow-up

- The FORM-05 helper has_independence_wave_form05_active_carrier_host_threat at common/scripted_triggers/006_independence_wave_form05_triggers.txt lines 501 and 505 still uses static ARX and ASX scopes. common/decisions/006_independence_wave_form05_decisions.txt decision AI modifier consumes this helper at line 95. The parent should baseline and compare it through chaosx_ai_probability_auditor before changing it.
- common/decisions/006_independence_wave_pacific_decisions.txt keeps four static HBX references inside two ai_will_do blocks. They belong to independence_wave_haw_authorize_pacific_delegation at lines 277 and 281 and independence_wave_fsm_ratify_autonomous_federation_mandate at lines 435 and 439. The parent should audit the exact HAW and FSM scenarios before changing these modifiers.
- Suggested named probability scenarios are haw_no_collapse, where actor HAW has no collapse flag and the HBX carrier is active but not collapsed; haw_hbx_collapse, where HAW has no collapse flag and the active HBX carrier has independence_wave_host_collapse; haw_actor_collapse, where HAW itself has independence_wave_host_collapse; and the same three states with actor FSM. Include an absent-HBX baseline for each actor. The score difference remains unmeasured until the auditor binds or records the unresolved dynamic-country inputs.
- D34 also leaves the Event 021 adapter registry queued. The related files common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt and common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt are outside this subtask's ownership and were not patched.
- This is a focused dynamic-carrier correctness patch, not a full country package certification. Broad politics, portraits, flags, parties, industry, military, technology, supply, AI survival, and asset coverage remain unreviewed here.

## User Live Validation Scenarios

- Release GZX dynamically at state 331, confirm the bounded registry contains its active origin row, obtain the required accepted FORM-02 member invitations, and verify that the Newfoundland port, founder, readiness, consent, and territory proof allow formation. The state remains owned and controlled by the expected live country through commit.
- Release either AFX or AGX dynamically at state 34 or 36, complete the charter, and invite consenting BEL_flanders, HOL, and LUX members. Verify member records and scripted status, language, phase, and outcome text update on the live carrier. Trigger one corridor or ratification report and confirm the member receives one report chain.
- Release AJX dynamically at state 42 with RHI at state 51. Verify the FORM-04 connection passes while the live countries are neighbors and at peace, then fails if war or adjacency breaks. Keep all existing founder and consent conditions in the scenario.
- Release ARX or ASX dynamically at its state 114 or 115 anchor, invite an autonomous member, and accept from that member. Verify the carrier's consent count updates once and the FORM-05 capital and ledger text resolves for that carrier.
- Release HBX dynamically at state 378, satisfy the existing HAW and FSM membership and invitation proofs, and verify FORM-48's exact founding ledger and runtime commit proof recognize the active HBX carrier. The Pacific AI modifier remains pending the parent audit.

## Simplifications, Omissions, and Blockers

No fallback identity, tag, state, consent rule, cost, AI weight, or map value was introduced. The seven non-weighted file changes implement the D34 queued dynamic-carrier corrections. Weighted Pacific and host-threat conditions are intentionally left for the parent probability audit, the Event 021 adapter registry remains outside this ownership boundary, and broad country package surfaces remain unaudited.
