# Event 012 protection eligibility baseline and bounded AFTER audit

Status: The frozen baseline and the owner-applied AFTER source gate have been reviewed. The AFTER source matches the accepted eligibility policy, but the MCP numeric before/after comparison returned no terminal result, so no effective score delta, eligibility trace, ranking, or selection probability is certified.

This audit covers only the targeted decision gods_of_africa_protect_partner and its protection eligibility call chain. No gameplay source, localisation, Git state, or game runtime was changed by this audit. The parent’s separate production-predicate test remains independent and is not represented as MCP probability evidence here.

## Audited surface and source identity

The weighted surface is the one targeted decision candidate gods_of_africa_protect_partner in common/decisions/012_africa_gods_decisions.txt, source lines 1650–1725. The candidate's AI willingness block is lines 1714–1724. Its target trigger calls gods_of_africa_participant_can_receive_protection, availability calls gods_of_africa_protection_package_is_affordable, and the AI block applies a zero factor when the package is unaffordable.

The immutable BEFORE manifest is docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_eligibility_2026-10-08_evidence/before/manifest.json. All seven copied files and all seven current logical files matched their recorded raw SHA-256 hashes at baseline. The decision source hash was ae732079d66e081b0b6a13fbbe411b42936722009652639106d42d2b2144bfb9.

The AFTER copies and raw hashes are in docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_eligibility_probability_2026-10-08_evidence/after/manifest.json. The decision file remains byte-identical to BEFORE. The eligibility trigger, new private trigger file, constants file, and localisation file changed. The contract trigger, epoch-binding trigger, and contribution constants remain byte-identical to BEFORE. The protection effects and contribution effects were captured AFTER for call-chain review, but neither was in the seven-file BEFORE manifest, so their historical equality is not established by this audit.

At report finalization, all ten AFTER evidence copies still matched their live logical files by raw SHA-256.

The current source gate is defined by common/scripted_triggers/012_africa_gods_triggers.txt::gods_of_africa_participant_can_receive_protection at lines 755–773 and the new common/scripted_triggers/012_africa_gods_protection_eligibility_triggers.txt. The root decision still uses that shared gate for target discovery, package affordability, and AI affordability. The protection effect at common/scripted_effects/012_africa_gods_effects.txt::gods_of_africa_protect_partner line 5371 rechecks the same package affordability trigger.

The supporting exact identifiers are gods_of_africa_participant_needs_reconciliation in common/scripted_triggers/012_africa_gods_contract_triggers.txt, participant hold checks in common/scripted_triggers/012_africa_gods_triggers.txt, and the ownership check gods_of_africa_participant_owns_host_core_state in common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt. The AFTER localisation key gods_of_africa_protection_target_requirements_tt is present at line 360 of localisation/english/012_africa_gods_l_english.yml.

## MCP evidence and result classes

The connected HOI4 Agent Tools server status reported version 3.10.0 and a live server. The workspace ID is mod_chaos_redux_ea3b2d67c2c0.

The required baseline hoi4.probability_inspect call succeeded for adapter decision_ai_will_do with the single supplied candidate gods_of_africa_protect_partner. The adapter reported poolComplete=true, candidates=1, zero required input paths, and zero unresolved parser items. Its source revision is 86c898c52c72dcc14a5ddb887a9d8485776597919063b15b3f726fdfec62904f and its separate MCP sourceHash is d293000a078bb966741261dda45c92c4d802e8fbf86f97560098407f586de48c. The full inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c4159e792ee993bf73381cabdcdaf423d00847456bb5a438f9a36593ce6fc59/7fad0a3782239554f9f44c638c787fbcc1b252db908c4c0a5e709ff4b8bb0392/probability-inspect-d293000a078b.json, SHA-256 1c4159e792ee993bf73381cabdcdaf423d00847456bb5a438f9a36593ce6fc59, size 21,896 bytes. The inspector listed only the frozen decision snapshot in filesScanned; it did not establish a transitive frozen-helper overlay. An empty requiredInputPaths list is not proof that every scope, war relation, or strategy factor was supplied.

A first inspect request used unsupported snapshot and sha256 keys and was rejected by argument validation. The corrected call used path, snapshotPath, and expectedSourceHash and succeeded; the validation rejection was not a service failure.

A bounded baseline probability_evaluate request was submitted for ONE_PAYMENT_HIGH_WRATH with one candidate and raw_value only. It remained pending for about 52 seconds and was stopped without an analysis ID, scenario hash, score trace, or artifact. The after-source probability_inspect attempt remained pending for about 47 seconds and returned no artifact. The probability_compare request used the immutable BEFORE decision snapshot and the AFTER decision snapshot with the same logical decision path and the seven named fixtures in scenario-set.json. It remained pending for about 52 seconds and returned no terminal MCP payload, comparison ID, scenario hash, or artifact. A second compare used only ONE_PAYMENT_HIGH_WRATH, the same source selectors, and one candidate; it remained pending for about 47 seconds without a result. These outcomes are observer/server unknown, not confirmed route failures.

The narrow decision_inspect route was also attempted. An initial shape without scenarios was rejected with the exact message “Decision inspection requires declared scenarios at scenarios”; the corrected one-scenario request remained pending for about 47 seconds and returned no structural artifact. The parent’s separate production-predicate source model is not replaced by this incomplete MCP observation.

The probability comparison request and exact source selectors are preserved in compare-request.json. The scenario set has raw SHA-256 c7da165c96c60293b2bc7876827f53839e830a0d58951fb5d56ee377f55917dc. This is a local fixture hash, not an MCP canonical scenario hash.

## BEFORE score and gate findings

The frozen source gate required a current registered participant, no defiance, gods_of_africa_reliable_memory_applied, no war with the host, an expired protection cooldown, and a valid current host. One completed payment can set the reliable-memory flag. The gate did not require Wrath below 30, at least three completed demands, meaningful voluntary aid, no unresolved major offense or treaty break, or no African host core held or owned.

The frozen decision score has base 10. Its source modifiers are factor 0 when gods_of_africa_protection_package_is_affordable fails, factor 3 for gods_of_africa_ai_is_proven_partner, factor 1.5 for a shared enemy, and factor 0.3 when Africa is near collapse. The proven-partner trigger is true when either gods_of_africa_compliance_count or gods_of_africa_aid_count is positive. These are source-defined score inputs, classified score-only; the MCP returned no effective score trace.

The baseline source therefore permits a one-payment participant with high Wrath to pass the relationship gate when the remaining current-host, war, cooldown, and affordability conditions pass. The same gap applies to a paid occupier, a tiny aid receipt, and unresolved hostility unless another old gate blocks the case. These are exact source-structure findings, not probability-evaluate outcomes.

## AFTER source review

The new helper gods_of_africa_protection_relationship_is_eligible requires all of the following:

- gods_of_africa_wrath exists and is strictly below constant:gods_of_africa_wrath.watchful, whose value is 30.
- gods_of_africa_compliance_count exists and is at least constant:gods_of_africa_protection.minimum_completed_demands, whose AFTER value is 3.
- gods_of_africa_protection_has_meaningful_aid succeeds from either measured receipt ledger: gods_of_africa_voluntary_paid_infantry_k or gods_of_africa_voluntary_paid_fuel_k.
- gods_of_africa_participant_needs_reconciliation is false.
- The participant neither holds nor owns an African core state of the host.

The meaningful-aid helper derives each receipt threshold from the existing voluntary_aid_equipment_amount or voluntary_aid_fuel_amount multiplied by contribution_measure.k_per_native. The constants remain 500 native units and 0.001 thousand units per native unit, so the input threshold is 0.5k in either measured ledger. This is a unit conversion in the accepted source policy, not a probability result. The contribution receipt implementation adds measured gods_of_africa_receipt_quantity_k into the voluntary paid ledger. Parent policy confirms Council voluntary rifle pledges count when they create that measured receipt; no new paid quantity or AI weight was added.

The existing participant gate wraps the private helper in a custom trigger tooltip and retains the generation, registration, reliable-memory, host-war, cooldown, and current-host checks. The target trigger still calls this shared gate. Availability and the AI zero-factor path use gods_of_africa_protection_package_is_affordable, which calls the same gate before checking host funds. The protection effect also rechecks that package gate. The qualitative tooltip is present. The decision file is unchanged, and the existing protection AI factors remain 10, 3, 1.5, and 0.3. The new minimum threshold is added to the constants file; the existing protection costs, cooldown, and service quantities were not changed in the reviewed constants and decision sources.

The helper’s source conditions align with the accepted target policy. Separately, the parent supplied docs/plans/012_africa_plans/subagent_handoffs/012_gods_protection_eligibility_2026-10-08_evidence/source_model_after.json, SHA-256 8e6fa64fbfc9c28b2e594c96f000946359f773d4f4e30600b0f1dacf605e73b0. That bounded production-predicate source model records 34 cases, engineEvaluation=false, actualProtectionBodyPreserved=true, and matching hashes for its seven AFTER source inputs. It reports the expected false-to-true boundary at Wrath 29.999/30, one completed demand versus three, measured receipt 0.499k versus 0.5k, fuel receipts, Council measured rifle aid, coarse aid-history rejection, wrong-actor aid rejection, treaty/offense/defiance/war rejection, held/owned host-core rejection, stale authority and cooldown behavior, and continued relationship eligibility with a poor host. This parent result is source-model evidence only and does not replace MCP evidence or claim engine evaluation. The MCP did not evaluate these predicates for the named cases, so each expected scenario outcome below remains unresolved at the analyzer level.

## Named scenario coverage

All fixtures bind ROOT to the synthetic host country ETH and FROM to the synthetic participant GER, with event_target:africa_host bound to ETH. The decision candidate pool is complete only for the single supplied decision score. It is not the full host decision race or a live list of every participant. No click probability is claimed.

| Scenario | Declared distinguishing inputs | AFTER source expectation | MCP result |
| --- | --- | --- | --- |
| ONE_PAYMENT_HIGH_WRATH | Wrath 65; one completed demand; no measured voluntary receipt. | Ineligible: Wrath is not below 30 and completed demands are below 3. | Unresolved; compare returned no result. |
| PAID_AFRICAN_OCCUPIER | Wrath 15; three completed demands; 0.5k rifle receipt; GER controls Ethiopian state 271, whose vanilla definition is an ETH core. | Ineligible because the participant holds an African host core. | Unresolved; state/control predicate was not confirmed by the probability adapter. |
| LOW_WRATH_STRONG_PARTNER_WITH_MEANINGFUL_AID | Wrath 15; three completed demands; 0.5k fuel receipt. | Relationship gate passes if no war, cooldown, host, and reconciliation conditions are clear. | Unresolved; compare returned no result. |
| COUNCIL_AID_HISTORY | Wrath 15; three completed demands; 0.5k measured rifle receipt, declared as Council voluntary aid. | Relationship gate passes on the measured aggregate receipt; Council origin is not a separate helper input. | Unresolved; receipt lineage is a declared scenario fact, not replayed by MCP. |
| TINY_AID | Wrath 15; three completed demands; 0.49k rifle receipt and no qualifying fuel receipt. | Ineligible because neither receipt reaches the 0.5k threshold. | Unresolved; compare returned no result. |
| UNRESOLVED_HOSTILITY | Wrath 15; three completed demands; 0.5k rifle receipt; unresolved treaty-break and major-offense flags. | Ineligible because participant_needs_reconciliation is true. | Unresolved; compare returned no result. |
| ZERO_RECEIVER_STOCKPILE | Wrath 15; three completed demands; 0.5k fuel receipt; GER receiver has zero infantry-equipment and fuel stock. Host funding remains available. | Relationship gate passes; recipient stockpile is not a relationship prerequisite. Host funding and package affordability remain separate gates. | Unresolved; compare returned no result. |

The fixture sets has_war=false but the source checks the pairwise relation has_war_with = event_target:africa_host. The fixture does not encode a distinct pairwise war relation, so that external gate is incomplete. The shared-enemy modifier, every competing host decision, external AI strategy factors, and live host/participant histories are also incomplete. The scenarios are synthetic and do not describe observed campaign state.

## Balance and validity findings

The AFTER source removes the identified relationship false positives at the source gate and preserves the prior affordability zero factor, cooldown, payment amounts, and AI weights in the decision and constants files. This is an exact source review only. Because the probability comparison did not return, there is no MCP proof of effective AI weight, candidate ranking, or gate projection for any fixture.

No dominance, starvation, rank reversal, repetition rate, snowball, or exploit-rate conclusion is established. The candidate pool excludes all other available host decisions, and the tool returned no score trace. The relationship gate now blocks protection for insufficient cooperation, high Wrath, insufficient actual aid, unresolved hostility, and African core ownership/control by source definition. The 180-day protection cooldown remains the repetition guard. Sequence analysis is out of scope because this is not a declared custom weighted pool with cadence and transitions.

There is no numeric tuning recommendation. Keep the existing protection AI factors and package quantities. The owner-applied eligibility helper and its shared call sites are the concrete source fix reviewed here. For any later numeric comparison, the MCP needs a way to bind the BEFORE helper dependency set as well as the decision root; the present compare request binds the decision snapshot but does not establish historical transitive helper resolution.

## Skipped analyses, blockers, and references

hoi4.probability_sweep was not completed because the bounded AFTER compares returned no analysis artifact or score trace from which to render threshold sensitivity or rank reversals. hoi4.probability_render was not called because no successful analysis ID exists. hoi4.probability_simulate was not used because no uncertain-input distribution was declared. hoi4.probability_sequence was not used because no complete custom weighted pool with cadence and state transitions is in scope. The final named-case MCP compare is unresolved after one seven-case attempt and one single-case retry; it is not marked as a service or adapter failure.

The full offline Paradox Wiki Decision modding AI section was read at paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md lines 357–374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162. The AI modding MTTH section search result covered lines 26–37 at revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818; its separate reference_read remained pending and was stopped after about 42 seconds. The installed vanilla decisions documentation was read at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md lines 1–46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019. It defines the country and FROM scopes and the checks for target_root_trigger, target_trigger, visible, and available. Vanilla state 271 is in history/states/271-ethiopia.txt; owner ETH is at line 24 and add_core_of ETH at line 39.

Skills read and applied: .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, and .agents/skills/chaos-redux-event-planning/SKILL.md. The MTTH skill was consulted; no separate MTTH entry or MTTH-backed weight is involved. AGENTS.md and the parent-named full specification, scenario contract, and BEFORE manifest were read. No tests or live game were run, as this was a read-only audit and the parent is running a separate production-predicate test.
