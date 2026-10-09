# Remaining CBRN source gaps, 2026-10-09

Disposition: bounded read-only completion review, with one confirmed deterministic consumer gap accepted by the parent for a narrow repair.
The broad overhaul remains incomplete.
This auditor changed only this handoff, with no gameplay, shared documentation, assets, workbook, index or commit edits.

## Authority and scope

The controlling acceptance is `docs\specs\chaos_warfare_system_specs\specs\13_2026_09_20_accepted_cbrn_overhaul.md`, especially lines 67-77, 96-98 and 112.
The original source package was consulted through specifications 07 and 10, `matrices\country_program_and_designer_matrix.md`, and the source-of-truth/completion handoffs, with older proposals subordinate to the accepted amendment.
The requirement ledger and `2026-09-25_cbrn_overhaul_completion_report.md` were read as status/evidence locators, then checked against current source rather than treated as executable behavior.
The source review occurred with HEAD `1365a58bdfca348976ce6d115c2911122340204c` in a shared dirty tree.

The parent's protected decisions remain intact: restored main emblem, stronger concentrated doctrine rewards, the 5/3/3/6 contributor assignment across thirteen roles, the 27 technology cost calibrations and twelve numeric getters, and the native-only biological consolidation.
No bonus cuts, new route, substitute operation, free historical stock, periodic world iteration, famine/migration implementation or portrait-source recovery is recommended.
Automatic protection/readiness and the 67-person personnel review belong to the parent and other assigned reviewers.
The parent subsequently accepted the Vehicle Recovery finding below and owns its implementation and test files, so the pre-repair source evidence here must not be mistaken for a review of that later patch.

## Completion by reviewed surface

| Surface | Disposition | Current evidence and limit |
| --- | --- | --- |
| Three generic MIO families and six historical/two fictional variants | Implemented in source, native assignment/card/effect validation unresolved | `common\military_industrial_organization\organizations\cbrn_*_organizations.txt` defines the accepted family architecture and national inheritance. National gates, Showa Denko's June 1939 date and the DuPont polymer distinction are present. No additional bespoke national tree is required by the accepted amendment. |
| Vehicle Recovery Teams effect on existing contamination | Confirmed pre-repair source gap, parent accepted and implementing | The trait completion emits only its tooltip, while the stored state attrition projection is recalculated only by contamination changes or state-control changes. See priority 1. |
| Respiratory and Burn Care continuing-blister hook | Implemented in source, native deaths unproved | `events\cbrn_chemical_delivery_events.txt:184` already calls the treatment helper. The event owns `chaos_state_deaths_mult` before that call. The preliminary absent-hook hypothesis is withdrawn. |
| Eight named projects and advanced discovery alternatives | Implemented in reviewed source, execution evidence partial | All eight project definitions and completion adapters exist. Ordinary discovery plus Event 016/Mengele alternatives have distinct gates. Random project grants guard completion and separately permit missing-technology repair. Native project-card discovery, all completion orders and reward cardinality remain unproved. |
| Historical 1939 industrial differences | Partial source implementation and unresolved historical/design coverage | Britain has the accepted respirator line. USA has the accepted research/reserve distinction. Additional country-specific industry or stock differences are not justified by the existing source dossier. This is not permission for generic grants. |
| CBRN family consumer disposition | Source disposition present, documentation stale | Event 019's support-only boundary is explicit and provider 521 owns the combat `chaos_battalion` family. Its coverage paragraph still lists retired HQ/support definitions. See priority 5. |
| Ongoing civilian protection against chemical contamination | Requirement-to-consumer question, assigned parent scope | The active continuing-death transaction does not read the issued-mask or hospital-response state directly. The relevant inherited requirement and exact path are recorded under priority 2, without inventing a replacement formula. |

## Five prioritized next owner actions

### 1. Review the parent's accepted Vehicle Recovery completion refresh

Acceptance basis: CBRN-12's functional MIO traits and the accepted twelve-node chemical/protection family, with the existing tooltip and reward preserved.
The pre-repair `cbrn_decon_vehicle_recovery_teams` trait at `common\military_industrial_organization\organizations\cbrn_chemical_protection_organizations.txt:147-155` has `on_complete = { custom_effect_tooltip = cbrn_decon_vehicle_recovery_teams_tt }` only.
The tooltip at `localisation\english\cbrn_designers_l_english.yml:64` promises 45% lower attrition from controlled chemical contamination.
Its existing multiplier is `constant:cbrn_decontamination_designer_effect.vehicle_recovery_attrition_mult = 0.55`, at `common\script_constants\cbrn_designer_constants.txt:68`.

`common\dynamic_modifiers\chemical_state_modifiers.txt:10` consumes the durable STATE variable `cbrn_chemical_truck_attrition`.
`cbrn_designer_refresh_contaminated_state_vehicle_attrition`, at `common\scripted_effects\cbrn_designer_effects.txt:284-299`, derives it from `cbrn_chemical_effective_strength`, the existing base coefficient, and the current controller's completed trait, then forces the dynamic modifier to update.
Its only current calls are `cbrn_chemical_refresh_state_modifier` at `common\scripted_effects\cbrn_chemical_state_effects.txt:228` and the exact `on_state_control_changed` hook at `common\on_actions\cbrn_designer_on_actions.txt:19`.
The continuing-death callback does not refresh this attrition projection, and expiry merely clears it.
Thus a state contaminated before the controller earns the trait keeps its prior stored penalty if no later contamination/cleanup/control event occurs.
This is a concrete source-order gap, rather than uncertainty about native modifier aggregation.

The parent accepted a hidden FROM-country controlled-state refresh using the existing recalculation helper, covering the generic family and inherited ICI, DuPont and Montecatini variants.
The installed MIO contract places `on_complete` in INDUSTRIAL_ORG scope and the country in FROM.
Preserve the exact controller check and set-from-strength calculation so duplicate calls cannot compound 0.55 repeatedly.
Review completion timing of `is_mio_trait_completed`, qualifying active-state filtering, and durable projection consistency alongside new contamination, cleanup, conquest and expiry.
The bounded acceptance cases should include a previously contaminated controlled state, a clean state, a foreign-controlled state, duplicate refresh, a different controller without the trait, and inherited national variants.
No new bonus, weight, world pulse, damage or protection transaction is needed.
This handoff does not certify the parent's later source or tests.

### 2. Resolve the continuing-protection requirement in the parent's existing owner review

Specification 07 at line 204 says Protect Hospitals and Utilities reduces medical saturation and continuing deaths.
The current continuation is `cbrn_delivery.4`, at `events\cbrn_chemical_delivery_events.txt:179-191`.
It takes `cbrn_chemical_continuing_death_rate`, applies the generic density/infrastructure environment multiplier and the existing blister MIO treatment multiplier, then registers the actual civilian loss.
`cbrn_chemical_refresh_continuing_death_profile`, at `common\scripted_effects\cbrn_chemical_state_effects.txt:243-296`, derives the stored rate from contamination stage, agent class and the terminal doctrine spirit.
Neither inspected body reads current issued civilian mask coverage or a hospital-response receipt.
The generic death-registration body at `common\scripted_effects\chaos_meter_effects.txt:3575-3683` consumes the caller's values without a later CBRN protection pass.

This is an unresolved requirement-to-consumer link for the parent, not an assertion that the correctly wired burn hook is absent.
The current hospital adapter at `common\scripted_effects\cbrn_protection_decision_effects.txt:434-435` enters the parent-owned `cbrn_execute_hospital_response_order`, so final review belongs with that owner's current protection repairs.
Require either a demonstrated existing path to the continuing-death calculation or an explicit accepted disposition for the inherited continuing-death claim.
If a repair is needed, preserve the actual issued-equipment contract and the accepted same-mask additional-benefit ceiling, rather than adding another independent protection allowance or an invented proxy.
No new formula, weight or balance target is selected by this auditor.

### 3. Finish historical 1939 entitlement and disposition before new industrial grants

The accepted amendment requires grounded country/program starts, including stock, research, facilities and route state, with industrial distinctions separate from force-scaled masks.
Current `common\scripted_effects\chaosx_startup_history_effects.txt` retains Britain's dated basic-respirator line and USA's accepted 320-lot later-bookmark mustard reserve and phosgene knowledge.
The mask bands and reserves must not be recalibrated from the older fixed matrix.

`subagent_handoffs\2026-09-27_cbrn_1939_industry_personnel_audit.md` records remaining FRA/ITA/JAP/GER/SOV industrial or stock distinctions as unresolved.
Its Army source explicitly rejects a continuous 1939 USA agent-production line: brief 1937 runs and a pilot filling plant do not prove continuous agent output at that bookmark.
The Italy source review supports the existing institution and facility, with no approved extra scientist, dated production line or stock amount.
The next action is a country/date evidence disposition, followed only by source-supported approved setup changes where warranted.
If no extra grant is warranted, record that country-specific conclusion with evidence rather than label a generic missing line as an implementation defect.
Native queue/factory assignment remains a separate validation requirement even where the source grant is accepted.

### 4. Retain the project's discovery/order validation gap without rewriting completed source

`common\special_projects\projects\cbrn_special_projects.txt` has the eight accepted projects, with completion flags in `common\scripted_effects\cbrn_special_project_effects.txt:5-40` and discovery/prerequisite gates in `common\scripted_triggers\cbrn_special_project_triggers.txt:3-85`.
The advanced biomedical, cloning, paleogenetics and xenobiological native project definitions call the ordinary/story completion adapters at `common\special_projects\projects\016_brilliant_scientist_projects.txt:272,452,622,713`.
The ordinary APIs already have durable grant/provenance and runtime-reconciliation contracts.
The guarded `grant_random_chaos_special_project_available_tech` in `common\scripted_effects\cbrn_project_effects.txt` distinguishes incomplete completion from missing-technology repair.
The accepted UWR and CXT exact-site corrections remain separate facility contracts, not authorization for arbitrary arsenal grants.

No additional concrete duplicate-reward defect was demonstrated in this pass.
Keep CBRN-10 partial until ordinary, story and exceptional scripted-grant completion orders establish one output/grant, recover missing technology without repeating project rewards, and preserve valid exact-site registration.
The prior special-project AI/prototype probability adapter failures remain blockers.
This deterministic pass selected no weight repair or retuning, and provides no replacement probability claim.
Any weighted owner change still requires `chaosx_ai_probability_auditor` baseline and matching comparison scenarios.

### 5. Reconcile the CBRN support-family coverage paragraph

`docs\events\019_infantry_spawn\systems\unit_family_coverage.md:37` still calls eighteen old CBRN support IDs real current units, including `cbrn_hq_intelligence_weather_cell`, `cbrn_hq_mobile_decontamination_column`, `cbrn_hq_biological_security_section`, `cbrn_nerve_suppression_detachment` and `cbrn_field_epidemiology_detachment`.
The installed HQ source now defines only `cbrn_hq_operations_section`, `cbrn_hq_protective_logistics_section` and `cbrn_hq_medical_countermeasure_directorate` in `common\units\cbrn_hq_support.txt:54,117,176`.
The accepted nerve function is an upgrade within the consolidated structure rather than a missing standalone definition.
Update only the CBRN owner inventory and its migration/disposition explanation after checking current unit source and CXT formation coverage.
Preserve provider 521 and the support-only parent ownership rule, without introducing a new central family list or standalone support provider.
This is stale documentation evidence, not a missing Event 019 gameplay provider.
The unrelated provider rows and shared registries are outside this audit's repair authority.

## Accepted-plan disposition

The accepted September amendment remains the controlling implemented/partial/blocked requirement set, with no new exception promoted by this audit.
The Vehicle Recovery finding is parent-accepted implementation of an existing trait, with the parent's source/test work in progress at handoff time.
Further 1939 industrial quantities remain unresolved rather than accepted and queued implementations.
The existing Event 020 six-lane response addendum remains unresolved, and its implementation is not inferred from a board render.
Famine/migration work remains the delivered plan-only handoff under the parent's explicit restriction.
No additional improvement planner or broad expansion is needed to resolve the deterministic MIO refresh.

## Meaningful references and MCP limits

Live `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` were exposed and called.
The general context omitted Modifiers and Scopes sources, so it is not a claim of full reference coverage.
Targeted reads establish the narrow MIO and bounded-state scope contract below.

| Source read | Lines | Revision |
| --- | --- | --- |
| Installed `common\military_industrial_organization\organizations\_documentation.md`, completion scope and equipment limits | 136-155 | `f922d406197239435aedb16f85bd50eac533ca63cc2c41ad4e25f0d08b3fa6fd` |
| Offline `paradox_wiki\Military industrial organization modding - Hearts of Iron 4 Wiki.md`, `on_complete` | 273 | `6d0a87c0cd738de48e4cde4296c0c38e035ab11a0f8afa24cdc05b5b15703121` |
| Installed `documentation\effects_documentation.md`, controlled-state iterator | 3800-3819 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, controlled-state iterator | 124 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Installed `documentation\triggers_documentation.md`, completed trait | 5949-5964 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md`, completed trait | 2243 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Installed `documentation\effects_documentation.md`, production-line scope/fields | 1207-1232 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, production line | 2260 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |

Vanilla `common\military_industrial_organization\organizations\GER_organization.txt:117-121` and `CZE_organization.txt:656-660` were read as completion effects entering FROM country, not as proof of the custom trait's completion timing.
`source_lookup` returned the exact attrition helper at revision `8579e551ce6525e745aa04b55ab3bbcdae7d32ef39fb7b59a62b9ae5150adf1d`.
It returned no national MIO/trait definition, so source-only national reads remain separate from a complete MIO domain inspection.
An initial invalid `maxDefinitions=4` request was corrected to the live maximum of three.
No dedicated MIO inspection/render route was exposed, and no health/version or task-negotiation claim is made from the exposed tools.

The exact STATE attrition helper passed no full semantic gate: `hoi4.script_validate` returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, eleven checked commands, six unresolved findings, five unchecked argument blocks and one omitted finding.
Its aggregate installed-doc revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
This is baseline command-kind/scope evidence only, not modifier execution or repair validation.

The read-only event pass selected `cbrn_delivery.1` and `cbrn_delivery.4` at revision `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889`.
Both inspect/render results were partial and focused, with zero helpers and deferred whole-workspace lifecycle projections.
Each render selected one node, and the summaries omitted 46,294 other nodes.
An initial incorrectly named `cbrn_chemical_delivery.1` selector was corrected and supplies no valid selection evidence.
The current-revision comparison route attempt returned `EVENT_GRAPH_ARTIFACT_LIMIT`: graph size 96,944,773 bytes against a 67,108,864-byte ceiling.
It supplied no comparison artifact and is not historical before/after evidence for any source patch.

Retained event artifacts:

- [Exact expiry trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f866421a38ebdcbec7d42d28faf3f229b4a6445a353312b8d3c4a2f81b565e3a/611ef02880026fe696c45994509c2000cf8f03a76450d42fcd0853782d0021cb/event-trace-283a55008536.json).
- [Expiry timing manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/267099e3b3fe517986de517e7d9ee11bd76756296d0f5edafdd72a50442de716/b27cb56eb7142ddda183e136ecba53406f79d840723b4b9b0e7616694963a31d/event-timing-283a55008536-manifest.json) and [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d221bf3eabca44a1d9c3960615a4615b7d505330bccf4d15606deb4fc0509d8f/58750d09a376634e68a48bcf202a09db7f860bfce49deacf49f69171e41b164d/event-timing-283a55008536.png).
- [Exact continuing-death trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec412a9bb385ae0d061bc3cad6b77e4312c57dc430efe424358e23f7a9147798/f5fa769dbbc73e30ee268701494fa0ce0db3b8f27c9b1a545fee98f9ac6ab18a/event-trace-283a55008536.json).
- [Continuing-death state manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02acbd39534fa882cbd05641dceb2421d09caaf3a3fa2d586aeccca2eccc4af4/003237f0d13dc270def14c7e88f7b3219771cb70d68a41601970a41655797c0f/event-state-283a55008536-manifest.json) and [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f248f560a7c47032747dae4f435c1074b336a4d3f6e55f2ed61fa503837b1e83/999448cc9ac8f96595e9aed252ca1155d89fe2ddafd688150b448a7aa6a9a4f2/event-state-283a55008536.png).

Artifact links preserve route outputs and limits only.
No complete resource read, pixel approval, helper-closure proof or observed native execution is claimed by this audit.

## Source identity and remaining blockers

The pre-repair files were fingerprinted independently of the shared Git index.

| File | SHA-256 |
| --- | --- |
| `common\military_industrial_organization\organizations\cbrn_chemical_protection_organizations.txt` | `85e1c32c153e48be48403a3c11070e46af6d8c6fddb3909bde49147d0a4f1c5e` |
| `common\scripted_effects\cbrn_designer_effects.txt` | `c82da050c071d79e446430c58cd368cd05ace2d32c39bb0a73d7b3ea7e02bffa` |
| `common\scripted_effects\cbrn_chemical_state_effects.txt` | `1873d29b193023e5121273376ac28af0119f91a0c11e4a7eb0e4b2a5ac063f40` |
| `events\cbrn_chemical_delivery_events.txt` | `0069266630afe853007311b0d03ddac38ff678245a035d2451aa58bcbaf21d40` |
| `common\on_actions\cbrn_designer_on_actions.txt` | `fb9879c536d5d4b3dceb768b8a5c0f723a6c95ea8eb5669707f2bf4021d7f757` |

Known native blockers remain those identified by the parent: reservation/cancel/refund cardinality, exact assigned-division-to-commander association, exact forecast/supply achievement predicates, effective combat/modifier aggregation and native 1920/2560 consumers.
This review does not reclassify them as source defects or choose weaker substitutes.
Project/MIO probability and native assignment evidence remain unresolved, with no numerical weighted conclusion produced here.
Assets and portrait archives were not reopened, and no new character portrait or model package was introduced.
Event logs, catalog rows, shared GUI and unrelated country/focus/formable systems were not changed or audited as complete.
No simplification was made by this auditor.
The bounded report is complete, while CBRN implementation and acceptance remain partial.

Skills applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-decisions-missions` and `chaos-redux-native-raids`.
No skill was changed.
