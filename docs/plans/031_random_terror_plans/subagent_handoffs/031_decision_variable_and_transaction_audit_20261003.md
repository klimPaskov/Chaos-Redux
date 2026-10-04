# Event 31 decision and mission variable/transaction audit

Audit date: 2026-10-03.

Disposition: read-only audit of the current shared-tree source. No gameplay, event, focus, localisation, asset, or GUI source was edited, and no commit was made. This handoff is the only requested write.

Acceptance basis: the user-authorized task names `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md` and `031_random_terror_decision_mission_prompt.md` as accepted design. The parent-owned terminal-profile versus actual-entity-classifier probability baseline remains pending and was not duplicated or patched.

## Source identity and scope

Current HEAD observed at final source check: `29284772330386577a63fe6546b114c5377c2e80`. The shared worktree was already broadly dirty, including the Event31 source files below. The decisions and missions files matched the probability auditor's final SHA-256 readings.

| Source | SHA-256 at final source check |
| --- | --- |
| `common/decisions/031_random_terror_decisions.txt` | `EC998C5B3355AAA8546EC73F0174F90F65A4665372C415DD2101315B2265F215` |
| `common/decisions/031_random_terror_missions.txt` | `B24633FA4996FB2D25C44118C44A01F38B3C1C821DBCADF819FA71591813A71D` |
| `common/decisions/categories/031_random_terror_categories.txt` | `F768025B0D1489ED5C44752D5EDFAA7A7C16848F5FE7CC2AB51F7E067A641390` |
| `common/scripted_effects/031_random_terror_effects.txt` | `8EDD15C352B0B4A8143B7A391078B5B6C0A01A41FE64FEA73CC86CED7B68B37A` |
| `common/scripted_triggers/031_random_terror_triggers.txt` | `3848A99005E8111A45B4BD49EF9C0821ACCD0C41029AAA5B1440182A685089C7` |
| `common/script_constants/031_random_terror_constants.txt` | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` |
| `localisation/english/031_terrorist_attack_l_english.yml` | `9C29F413702C5D5E72A4BA728881F71AACE3408E5D13BF9EA3F454C87E4AC065` |
| Supporting scope only: `events/031_terrorist_attack.txt` | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` |
| Supporting writer scan only: `common/national_focus/031_random_terror_focus.txt` | `D3082BA4F338E9CF399E8B0EF37FE89BE48F7A402DA3F66F0E516A738254954E` |

During closeout, another in-scope agent changed the shared effects file. I reviewed the diff and rechecked the mission success-marker producers and ordinary actor-control helpers. The diff was confined to terminal-actor identity/finalization paths, which remain parent-owned. The final effect hash and HEAD are recorded above. The canonical final-cap assignment cited below moved from line 3981 in the first source check to line 3982 in the final snapshot.

Inventory found 42 decision definitions and 8 mission definitions. The matrix has 41 decision rows and does not include `random_terror_terminal_counteroffensive`. The 42nd source definition is therefore an unresolved matrix disposition, not proof that any accepted row is complete or missing.

## Findings sorted by severity

### High

1. Cost affordability is not part of any decision's `available` predicate. A source scan found all 42 decisions use `custom_cost_trigger`, while none repeats its payer-side cost predicate or constants inside `available`. The offline Decision modding page says `custom_cost_trigger` selects the available/blocked cost localisation and does not charge or gate the decision by itself. Direct debits are in `complete_effect`. Therefore source does not establish that an unaffordable click is rejected before debit. The same 42 custom cost triggers use strict `>` comparisons, so a balance exactly equal to the displayed/debited amount fails the cost trigger. Partner accept-option resource triggers in Event31.40–.42 also use strict `>`.

   Recommended fix: use one shared inclusive affordability predicate in both `available` and `custom_cost_trigger`, keep its values aligned with the single payment path, and verify exact-equality affordability. Do not infer click behavior from the blocked cost color.

2. Five missions have no reachable success signal in the current source. All eight missions are non-selectable auto-completing missions, so their `available` condition invokes `complete_effect` as soon as it becomes true. For five missions, the required flag is set only in the mission's own success resolver, or the only non-resolver setter is explicitly cleared by the activating decision.

| Mission | Success gate | Current producer path and defect |
| --- | --- | --- |
| `random_terror_contain_attack_wave` | State flag `random_terror_containment_success` in `common/decisions/031_random_terror_missions.txt:30-34`. | Only setter found is `random_terror_resolve_containment_mission_success` at `common/scripted_effects/031_random_terror_effects.txt:3598-3606`, called by this mission's `complete_effect`. Both activation callers clear the flag at `common/decisions/031_random_terror_decisions.txt:86` and `:445`. |
| `random_terror_protect_transport_network` | State flag `random_terror_transport_protection_success` at `common/decisions/031_random_terror_missions.txt:107-112`. | `random_terror_decision_protect_transport` sets the marker, but the decision clears it before activation at `common/decisions/031_random_terror_decisions.txt:170-176`. The only remaining setter is the mission success resolver at `common/scripted_effects/031_random_terror_effects.txt:3638-3647`. |
| `random_terror_break_cross_border_corridor` | State flag `random_terror_support_disruption_success` at `common/decisions/031_random_terror_missions.txt:186-190`. | `random_terror_disrupt_support` sets a country-level `random_terror_support_disrupted` flag and activates the mission at `common/decisions/031_random_terror_decisions.txt:608-620`, it does not set the required state flag. The only other producer is `random_terror_resolve_support_disruption` at `common/scripted_effects/031_random_terror_effects.txt:2918-2932`, which has no call site in the scanned source. |
| `random_terror_prevent_capital_seizure` | State flag `random_terror_capital_security_success` at `common/decisions/031_random_terror_missions.txt:259-265`. | The generic setup helper sets it, then the activating decision clears it at `common/scripted_effects/031_random_terror_effects.txt:2198-2208` and `common/decisions/031_random_terror_decisions.txt:1154-1160`. Its only remaining setter is the mission success resolver at `common/scripted_effects/031_random_terror_effects.txt:3714-3727`. |
| `random_terror_restore_civil_authority` | State flag `random_terror_civil_authority_restored` at `common/decisions/031_random_terror_missions.txt:413-420`. | The restore-services helper sets the marker and its caller clears it before activation at `common/scripted_effects/031_random_terror_effects.txt:2249-2261` and `common/decisions/031_random_terror_decisions.txt:1673-1681`. The only remaining setter is the mission success resolver at `common/scripted_effects/031_random_terror_effects.txt:3841-3855`. |

   Recommended fix: give each mission a real external objective-progress producer that sets its success flag only after the accepted requirement is met. Keep the success resolver as the consequence path, not as the sole producer for its own `available` gate.

3. `random_terror_actor_control` and `random_terror_territorial_control` are separate local country variables that start equal and then drift. This is not an uninitialized-start alias: `random_terror_initialize_actor` sets both to `constant:random_terror_tuning.actor_control_start` at `common/scripted_effects/031_random_terror_effects.txt:1552` and `:1564`, and the only `random_terror_actor`/`random_terror_active_actor` flag setter is inside that initializer at `:1538-1539`. Its actor-creation callers include `:1825-1952` and `:4083`.

   After setup, actor action helpers update only `random_terror_actor_control` at `common/scripted_effects/031_random_terror_effects.txt:2298`, `:2306`, `:2340`, `:2359`, `:2365`, and `:3313`. `random_terror_clamp_actor_values` clamps both independently at `:2520-2525` and does not synchronize them. The actor category displays the alias at `localisation/english/031_terrorist_attack_l_english.yml:201`. Actor decisions use it for AI at `common/decisions/031_random_terror_decisions.txt:1909`, `:1972`, and `:2680`, and for visibility/availability at `:2166`, `:2183`, `:2199`, `:2936`, and `:2953`. In contrast, `random_terror_is_viable_actor`, takeover/partition triggers, and global aggregation read local `random_terror_territorial_control` at `common/scripted_triggers/031_random_terror_triggers.txt:43-51`, `:412` and `:425`, `:460` and `:480`, and `common/scripted_effects/031_random_terror_effects.txt:2582-2607`. Additional alias readers are the actor-lifecycle check at `common/scripted_effects/031_random_terror_effects.txt:1772`, takeover commit at `:2675`, and absorption-event AI at `events/031_terrorist_attack.txt:356`. The category can therefore display a value different from the one used by world-level gates and actor-validity checks. The final-actor setup also sets only the canonical local value to its cap at `common/scripted_effects/031_random_terror_effects.txt:3982`.

   Focus writer scan also found alias-only and canonical-only changes in `common/national_focus/031_random_terror_focus.txt`, including alias updates at `:212`, `:278`, `:346`, and `:595`, canonical updates at `:1989`, `:2008`, `:2031`, `:2097`, and `:2142`, and one route that updates both at `:2051-2052`. I did not perform a focus-tree audit or patch focus code. Recommended fix: choose one authoritative actor-control value or synchronize every writer and reader, including the category display and route gates.

4. `random_terror_repair_captured_depot` charges an undisplayed third cost. Its `custom_cost_trigger` checks Network Authority, support equipment, and fuel at `common/decisions/031_random_terror_decisions.txt:2028-2033`, and its `complete_effect` subtracts Network Authority at `:2043`. The linked localisation `random_terror_repair_captured_depot_cost` at `localisation/english/031_terrorist_attack_l_english.yml:358` shows only support equipment and fuel. The authority debit has no cost texticon or blocked display.

   Recommended fix: show Network Authority with its registered `£random_terror_network_authority_texticon` or move it to a clearly non-consumed requirement only if payment is removed.

5. Several accepted actor actions charge and mark a result without performing the mapped operation. `random_terror_raise_local_militia` nets out its manpower/equipment return and debit correctly but only raises `random_terror_actor_control` and sets a state receipt. No formation is created by its decision/helper path (`common/decisions/031_random_terror_decisions.txt:1889-1904`, `common/scripted_effects/031_random_terror_effects.txt:2297-2302`). `random_terror_integrate_defectors` clears the defection receipt and adjusts authority/control but does not transfer or rebuild a formation (`common/decisions/031_random_terror_decisions.txt:1956-1967`, `common/scripted_effects/031_random_terror_effects.txt:2304-2309`). `random_terror_convert_militia` spends authority, XP, infantry and support equipment but only adjusts actor control, refunds XP inside its helper, and sets `random_terror_militia_converted`. No template or formation change is present (`common/decisions/031_random_terror_decisions.txt:2483-2499`, `common/scripted_effects/031_random_terror_effects.txt:2339-2344`). `random_terror_build_civil_administration` spends three types and the helper only sets a country flag plus the shared cooldown. No state control, building, or economy change is present in that helper (`common/scripted_effects/031_random_terror_effects.txt:2370-2373`).

   `random_terror_military_reinforcement` has a related commitment gap. The decision debits four resources, gets manpower and infantry equipment back from a helper, then debits them again, for a net debit matching the display. `random_terror_commit_reinforcement` only sets state/country receipts and a required-count variable at `common/scripted_effects/031_random_terror_effects.txt:3082-3094`. No division binding is present there. The decision itself comments that the parent runtime must bind and release actual divisions (`common/decisions/031_random_terror_decisions.txt:1083-1088`). The matrix maps this action to real unit commitment.

   Recommended fixes are local only if an existing unit or economy helper owns the promised operation. Otherwise the accepted matrix row needs an explicit owner disposition before any redesign.

### Medium

6. Source inventory is 42 decisions versus 41 accepted matrix rows. `random_terror_terminal_counteroffensive` at `common/decisions/031_random_terror_decisions.txt:1785` is the unmapped extra ID. It is not in the supplied matrix or dedicated prompt. The matrix counts `random_terror_accelerate_revelation` among territorial-actor actions even though source places it in the false-revelation category. Record an owner disposition for the terminal-counteroffensive row. I did not inspect terminal-profile/entity-classifier weighting.

7. Five cost strings contain four inline values, above the decision skill's maximum of three inline values: `random_terror_military_reinforcement`, `random_terror_isolate_enclave`, `random_terror_convert_militia`, `random_terror_prepare_state_offensive`, and `random_terror_recruit_foreign_fighters`. Each uses four distinct spendable types, meeting the separate hard maximum of four. No fifth distinct cost was found in the reviewed definition/helper chains.

   Seventeen actor cost strings display a Network Authority icon and then repeat the literal text Network Authority: `random_terror_raise_local_militia_cost`, `random_terror_integrate_defectors_cost`, `random_terror_open_external_corridor_cost`, `random_terror_seek_sponsor_cost`, `random_terror_support_foreign_cell_cost`, `random_terror_relocate_network_cost`, `random_terror_convert_militia_cost`, `random_terror_ideological_mobilization_cost`, `random_terror_absorb_actor_cost`, `random_terror_contest_network_leader_cost`, `random_terror_prepare_state_offensive_cost`, `random_terror_build_civil_administration_cost`, `random_terror_force_extraction_cost`, `random_terror_recruit_foreign_fighters_cost`, `random_terror_join_jihadist_international_cost`, `random_terror_call_coordinated_uprising_cost`, and `random_terror_accelerate_revelation_cost`. The texticon is registered in `interface/031_random_terror.gfx:8-9`. The literal label is redundant under the icon-first cost contract.

8. Cost values are centralized, but current decision/mission cost rows use fixed `random_terror_cost` or `random_terror_tuning` constants rather than scaling with country size, industry, reserves, fronts, pressure, prior outcomes, or evolution as the dedicated prompt describes. All 83 referenced Event31 cost/tuning/value leaf constants checked in decisions, missions, and localisation exist in `common/script_constants/031_random_terror_constants.txt`. No missing leaf constant was found.

9. The hostage mission has no partial-timeout branch. `random_terror_hostage_deadline.timeout_effect` at `common/decisions/031_random_terror_missions.txt:518-540` calls only `random_terror_resolve_hostage_deadline_mission_failure`. The helper at `common/scripted_effects/031_random_terror_effects.txt:3895-3906` always applies the failure outcome. The accepted matrix describes partial success when some hostages are freed but leaders escape.

10. The accepted government phase counts by distinct decision ID are Immediate 6, Network 6, Crisis 3, Territorial 5, Recovery 3, and terminal 1. Actor route-filtered phases stay within six distinct IDs, with Territorial/War Directorate reaching six. However, many actions use `state_target = any_controlled_state`, `any_owned_state`, or `any`. Installed vanilla decision documentation states each matching target creates a dedicated decision entry. No one-target selector or target-count cap was found in the in-scope source. Multiple simultaneous eligible states can therefore multiply visible rows beyond the accepted action budget. Actual on-screen count and clipping remain unverified because GUI MCP is unavailable.

11. Government category text is static and misses accepted status content. `random_terror_government_response_category_desc` at `localisation/english/031_terrorist_attack_l_english.yml:199` shows Terror Pressure and Response Legitimacy plus a general sentence, but no exact active-state list or next threshold/mission. `random_terror_actor_command_category_desc` at `:201` displays three raw values but does not explain meaning, cause, threshold, consequence, or response. The corresponding pressure/legitimacy values are initialized at `common/scripted_effects/031_random_terror_effects.txt:127-134`. Actor control, authority, and supply are initialized in `random_terror_initialize_actor` at `:1552-1564`. The initialization is present, while value significance and the alias split remain unclear.

12. The source has 42 base `custom_cost_text` localisation keys, but no matching `_blocked` or `_tooltip` key for any of them in `localisation/english/031_terrorist_attack_l_english.yml` (zero blocked keys found). The offline Decision modding reference says the blocked and hover variants are read by the custom-cost UI. Titles, descriptions, and source-referenced requirement/effect tooltip keys were found. The missing coverage is the cost-specific blocked and hover text.

## Category lifecycle, action budgets, and cognitive load

`random_terror_government_response_category` is visible to non-actor countries outside World End when government response or reconstruction is available. It has a static picture and state highlights. `random_terror_actor_command_category` is visible to actors outside World End with its own picture and owned-crisis highlights. `random_terror_false_revelation_category` is gated to a final actor or enabled revelation candidate. These are ordinary decision categories. No Event31 scripted GUI is present in the accepted design or category source.

The 6/6/3/5/3 distinct government phase counts are at the accepted hard maximum or below. Targeted decisions can render once per matching state, so those counts are not a proof of actual visible rows. The AI auditor counted 17 actor-command definitions plus one separate revelation accelerator. Route filters keep distinct action IDs within the six-action maximum, but multi-state target fan-out has the same unresolved risk.

The category headers do not expose the exact active-state list, the next threshold, or a next mission summary required by the dedicated prompt. Pressure and legitimacy are initialized and rendered as integers. Territorial Control is rendered from the unsynchronized alias. No dedicated value tooltip was found for the displayed government or actor values, so cause, threshold, consequence, and player response are not explicit in the header.

## Mission quality inventory

| Mission | Owner/category and target region | Requirement and duration | Success / timeout outcomes | Duplicate risk and lifecycle |
| --- | --- | --- | --- | --- |
| `random_terror_contain_attack_wave` | Response-country ROOT, `random_terror_government_response_category`, active crisis state. | Subject receipt and slot 1, 90 days. | Partial and failure have distinct pressure/activity outcomes. Success marker has no producer after setup clears it. | Slot 1 is shared with transport and hostage missions, cancel, timeout, and success paths clear subject and slot. |
| `random_terror_protect_transport_network` | Response-country ROOT, one controlled transport state. | Subject plus route control/protection state, 120 days. | Partial/failure are distinct. Success marker is cleared by setup and has no other producer. | Slot 1, cleanup clears subject, commitment, success, and active flags. |
| `random_terror_break_cross_border_corridor` | Response-country ROOT, recorded sponsor/corridor state. | Subject plus support-disruption success flag, 150 days. | Partial/failure are distinct, but the required success flag has only an unused helper producer. | Slot 2 is shared with capital and uprising missions, all branches clear subject and slot. |
| `random_terror_prevent_capital_seizure` | Response-country ROOT, controlled capital state. | Subject, capital, control, and success marker, 75 days. | Partial when capital is held at timeout, otherwise failure. Success marker is cleared at activation and has no external producer. | Slot 2, cleanup clears subject, success, and capital-security flags. |
| `random_terror_retake_lost_state` | Response-country ROOT, named lost-control state. | Subject and restored control without lost-local-control flag, 180 days. | Map-state success can auto-complete, partial/failure have distinct effects. | Slot 3 shared with civil-authority restoration, target and commitment flags are cleaned. |
| `random_terror_restore_civil_authority` | Response-country ROOT, controlled recovery state. | Subject and civil-authority-restored flag, 150 days. | Partial/failure are distinct. The initiating restore action sets then clears the success marker, no external producer was found. | Slot 3 shared with retake, cleanup removes subject, success, and slot. |
| `random_terror_hostage_deadline` | Response-country ROOT, state with active hostage crisis. | Subject plus hostages recovered and crisis resolved, 45 days. | Success can be produced by a successful security-surge response. Timeout has failure only, no accepted partial branch. | Slot 1, cancel/timeout/success clear hostage receipt, subject, and slot. |
| `random_terror_stop_coordinated_uprising` | Response-country ROOT, active uprising state after Evolution V. | Subject plus uprising stopped and controlled state, 90 days. | Security surge can set the stop receipt, partial/failure paths are distinct. | Slot 2, evolution/World End cancel path clears subject and slot. |

All eight use `selectable_mission = no`, so their `available` predicates auto-complete them. Their constant durations are varied and match the supplied bands: 90, 120, 150, 75, 180, 150, 45, and 90 days. The three country-level mission slots limit simultaneous active missions to three.

## Cost, requirement, and transaction audit

| Cost count result | Decision IDs |
| --- | --- |
| Four distinct spendable types, the hard maximum | `random_terror_military_reinforcement`, `random_terror_isolate_enclave`, `random_terror_convert_militia`, `random_terror_prepare_state_offensive`, `random_terror_recruit_foreign_fighters` |
| Hidden third spendable type | `random_terror_repair_captured_depot` charges Network Authority but shows only support equipment and fuel |
| More than four distinct spendable types | None found in the reviewed decision definitions and called helper chains |

Most fixed payment snapshots align with their displayed constants. `random_terror_army_experience_payment` is initialized as a temporary value, negated, and charged at the caller before helper return. Actions that intentionally return XP/resources then debit those returned amounts a second time. `raise_local_militia`, `integrate_defectors`, `convert_militia`, and `military_reinforcement` net to one displayed charge at current source values. `prepare_retake` charges XP twice around a helper grant: current retake cost and helper grant are both 10, but they are separate constants, so tuning one without the other changes the net debit.

Decision actions save `random_terror_action_state` as a regular event target before calling the helper that consumes it. These uses remain inside the same effect chain. Partner request effects likewise save regular requester/sponsor targets and fire the response event from that chain. No global action-state target or caller-consumed temporary output that disappears before use was found in these paths.

Partner consent is correctly sequenced for Event31.40–.42. The partner's command power/support, command power/convoy/support, or political power/infantry/support payment occurs inside the accept option at `events/031_terrorist_attack.txt:236-250`, `:272-288`, and `:310-327`. The refusal options at `:253-257`, `:291-295`, and `:330-335` do not charge the partner. Human countries choose the option. AI uses `ai_chance`. Initiators pay their own request cost up front. Acceptance affordability also uses strict `>`.

## Localisation and texticon coverage

Every decision and mission title/description key and every source-referenced custom requirement/effect tooltip key in this scope was found. All 42 base cost strings are present, but none has its `_blocked` or `_tooltip` companion key. The repair-depot authority debit has no cost texticon. The 17 actor cost keys listed in Finding 7 repeat the literal resource name after the registered Network Authority texticon. The four-value rows are source-level inline-budget violations. Clipping itself is unverified without the production UI render.

## AI validity, route locks, and probability evidence

The weighted-logic auditor was used for all 42 decision weights and 8 mission weights, excluding `random_terror_accelerate_revelation` and the parent-owned terminal classifier/W01-W08 cases. It found no callable `mcp__hoi4_agent_tools__hoi4_probability_*` route. `hoi4.probability_inspect`, `evaluate`, `sweep`, `compare`, and `render` were blocked before service calls. There is no workspace ID, source revision, artifact URI, scenario hash, ranking, normalized probability, or comparison. This is a route-availability blocker, not a timeout. No narrowed retry was possible, no gameplay change was made, and no compare was required.

The following formulas are source-score findings only. `ai_will_do` remains a willingness score, not click probability. Decision bases are low 1, medium 3, high 7, urgent 12. Factors are low 0.5, high 2, urgent 4. The mission source uses the same tiers. No factor was multiplied into a computed score.

| Government decision | Source `ai_will_do` factors |
| --- | --- |
| `random_terror_establish_response_cell` | Base 3, ×2 active state, ×2 failed raid, ×4 pressure above high, ×0.5 at war. |
| `random_terror_protect_transport` | Base 3, ×4 capital or transport disrupted, ×2 port disrupted, ×0.5 at war. |
| `random_terror_support_victims` | Base 3, ×2 relief strain, ×2 legitimacy below low, ×4 recent incident, ×0.5 at war. |
| `random_terror_intelligence_sweep` | Base 3, ×2 breakthrough, ×2 legitimacy above high, ×0.5 at war. |
| `random_terror_security_surge` | Base 7, ×4 capital infiltration or hostage crisis, ×2 recent incident, ×0.5 at war. |
| `random_terror_targeted_raid` | Base 3, ×2 intelligence breakthrough, ×4 capital infiltration, ×0.5 at war, ×0.5 failed raid on target. |
| `random_terror_disrupt_support` | Base 3, ×2 corridor evidence, ×2 sponsor evidence, ×4 already disrupted, ×0.5 low global reach. |
| `random_terror_request_allied_intelligence` | Base 1, ×2 faction member, ×2 breakthrough, ×4 at war. |
| `random_terror_offer_defection_channel` | Base 3, ×2 defection, ×4 military defection, ×0.5 low legitimacy. |
| `random_terror_movement_restrictions` | Base 1, ×4 target pressure above severe, ×0.5 low legitimacy, ×0.5 at war. |
| `random_terror_protect_community_sites` | Base 3, ×2 Muslim-community opposition, ×2 community rejection, ×4 low legitimacy. |
| `random_terror_expose_sponsor` | Base 3, ×2 sponsor evidence, ×2 faction member, ×0.5 low legitimacy. |
| `random_terror_quiet_sponsor_leverage` | Base 3, ×2 democratic, ×2 breakthrough, ×0.5 sponsor exposed. |
| `random_terror_military_reinforcement` | Base 7, ×4 capital, ×2 armed insurgency, ×0.5 at war. |
| `random_terror_capital_security` | Base 12, ×4 at war, ×2 major. |
| `random_terror_isolate_enclave` | Base 7, ×4 target pressure above severe, ×2 corridor, ×0.5 low legitimacy. |
| `random_terror_relief_corridor` | Base 7, ×4 relief strain, ×2 low legitimacy, ×0.5 at war. |
| `random_terror_prepare_retake` | Base 7, ×4 target pressure above severe, ×2 reinforcement active, ×0.5 peace. |
| `random_terror_negotiate_surrender` | Base 3, ×2 enclave isolated, ×4 low legitimacy, ×0.5 major. |
| `random_terror_request_intervention` | Base 3, ×2 major, ×4 target lost local control, ×0.5 peace. |
| `random_terror_restore_services` | Base 7, ×4 target in recovery, ×2 legitimacy below high, ×0.5 at war. |
| `random_terror_public_accounting` | Base 3, ×2 democratic, ×2 failed raid, ×2 sponsor exposed, ×0.5 at war. |
| `random_terror_security_reform` | Base 3, ×2 democratic, ×2 accounting complete, ×4 major. |
| `random_terror_terminal_counteroffensive` | Base 12, ×2 at war, ×0.5 low legitimacy. |

| Actor decision | Source `ai_will_do` factors |
| --- | --- |
| `random_terror_raise_local_militia` | Base 3, ×2 active target, ×2 alias control below low, ×0.5 at war. |
| `random_terror_integrate_defectors` | Base 3, ×2 defection recorded, ×2 alias control below low, ×0.5 at war. |
| `random_terror_repair_captured_depot` | Base 7, ×4 depot compromised, ×2 external supply below low, ×0.5 at war. |
| `random_terror_open_external_corridor` | Base 7, ×4 supply below low, ×2 sponsor contact, ×0.5 at war. |
| `random_terror_seek_sponsor` | Base 3, ×2 supply below low, ×2 Ideological Secretariat, ×0.5 at war. |
| `random_terror_support_foreign_cell` | Base 7, ×4 network reach below high, ×2 Jihadist International, ×0.5 at war. |
| `random_terror_relocate_network` | Base 7, ×4 entrenched target, ×0.5 at war. |
| `random_terror_convert_militia` | Base 3, ×2 armed-insurgency target, ×0.5 peace. |
| `random_terror_ideological_mobilization` | Base 3, ×2 active target, ×0.5 at war. |
| `random_terror_absorb_actor` | Base 3, ×2 target alias control below low, ×2 Ideological Secretariat, ×0.5 at war. |
| `random_terror_contest_network_leader` | Base 7, ×4 unity below low, ×0.5 peace. |
| `random_terror_prepare_state_offensive` | Base 12, ×2 armed-insurgency target, ×0.5 peace. |
| `random_terror_build_civil_administration` | Base 7, ×4 target lost local control, ×0.5 at war. |
| `random_terror_force_extraction` | Base 1, ×2 armed-insurgency target, ×0.5 peace. |
| `random_terror_recruit_foreign_fighters` | Base 7, ×4 supply below low, ×2 Evolution IV, ×0.5 at war. |
| `random_terror_join_jihadist_international` | Base 7, ×4 unity below low, ×2 Jihadist International, ×0.5 at war. |
| `random_terror_call_coordinated_uprising` | Base 12, ×4 target-controller pressure above high, ×0.5 at war. |

| Mission | Source `ai_will_do` factors |
| --- | --- |
| `random_terror_contain_attack_wave` | Base 7, ×4 pressure above high, ×2 failed raid, ×2 at war. |
| `random_terror_protect_transport_network` | Base 7, ×4 capital subject, ×2 at war. |
| `random_terror_break_cross_border_corridor` | Base 7, ×4 support disrupted, ×2 at war. |
| `random_terror_prevent_capital_seizure` | Base 12, ×4 at war, ×2 major. |
| `random_terror_retake_lost_state` | Base 7, ×4 retake subject plus armed insurgency, ×2 at war. |
| `random_terror_restore_civil_authority` | Base 7, ×4 low legitimacy, ×2 at war. |
| `random_terror_hostage_deadline` | Base 12, ×4 hostage crisis active, ×2 at war. |
| `random_terror_stop_coordinated_uprising` | Base 12, ×4 at war, ×2 unity above high. |

Named scenario fixture requirements from `031_random_terror_ai_scenario_matrix.md` are preserved without invented IDs:

| Scenario | Required input fixture and relevant checks |
| --- | --- |
| `P01_stable_peace_state` | Stable peace, one active urban state, high legitimacy, good intelligence, adequate reserves, compare response-cell, transport, victim-support, intelligence, surge, raid, containment, and transport weights, sweep legitimacy 40–90. |
| `P02_unstable_wartime_authoritarian` | Low stability, war, poor intelligence, strong army, weak legitimacy, several fronts, compare surge, capital security, reinforcement, raid, allied intelligence, containment, and capital mission, sweep capital deadline 90–15 days and reserves from zero to strong. |
| `P03_occupied_resistance_context` | Occupied states, resistance, supply strain, one active network, compare transport/reinforcement/isolation/relief/retake/intervention and actor corridor/cell choices, sweep supply-hub importance low to critical. |
| `P04_successful_response` | Protection, victim support, high legitimacy, breakthrough, one weakened cell, compare raid/intelligence/support/recovery/accounting and related missions, sweep intelligence quality low to high. |
| `P05_transnational_safe_haven` | Weak host, three affected countries, sponsor, two corridors, high reach, compare support disruption, allied intelligence, sponsor exposure/leverage, intervention, actor corridor/sponsor/cell/fighter actions and corridor mission, sweep evidence wrong to confirmed. |
| `P06_territorial_spawn` | Pressure above severe, Lost Local Control, defectors, equipment, viable parent/carrier, connected state group, evaluate decisions only after valid actor creation. Spawn selection and force-fill are outside this score pass. |
| `P07_muslim_government_against_jihadist` | Evolution IV actor, Muslim-majority government, strong local rejection, pair with an otherwise identical non-Muslim case and keep opposition flags separate from ordinary baseline score. |
| `P08_cannibal_border` | Event31 and Event14 actors share a border and each has another enemy, compare corridor, foreign cell, absorption, offensive, and relevant mission choices. No inspected in-scope formula directly references Event14 factors. |
| `P09_major_intervention` | Capable major, threatened ally, access, low domestic pressure, compare intervention and allied intelligence, sweep partner access false to true. |

Actor-route inputs are six descriptive rows, not machine scenario IDs: isolated state/strong parent/foreign cells. Four connected states/defectors/supply. Strong recruitment/charismatic leader/low conventional equipment. Sponsor-backed criminal-political actor. Evolution IV leader-seeking actor. And actor under immediate parent offensive. The auditor did not invent IDs or schema fields. P10 and W01-W08 plus the false-revelation accelerator/classifier remain excluded by the parent-owned terminal audit boundary. The coordinated-uprising mission has no matching P01-P09 fixture, so its in-scope weight needs a separately authorized non-classifier fixture or the matrix's P10 context when the MCP route is available.

A separate consent-option probability-auditor pass was requested for Event31.40–.43, but it did not return after three 30-second waits and was shut down. No event-option analysis artifact or probability result was received. The source branch findings below remain source-only.

Source-level AI mismatches that need same-scenario evaluation, not an automatic patch:

- `random_terror_support_victims` raises willingness when legitimacy is below 25, while P01 expects victim support to rise across legitimacy 40–90. Its direct factor never activates in that sweep.
- `random_terror_movement_restrictions` is penalized below 25 legitimacy but has no direct high-legitimacy reduction. P01's coercion-ordering expectation therefore remains unresolved.
- The P02 capital-deadline sweep is absent from the direct surge/capital weights, and frontline-reserve sensitivity is absent from reinforcement.
- `random_terror_protect_transport` weighs capital/transport/port flags but has no direct supply-hub-importance factor.
- `random_terror_targeted_raid` weights a breakthrough flag, not continuous intelligence quality. Its outcome distribution is outside the decision/mission source files.
- `random_terror_request_intervention` uses faction membership as the visible partner relation and has no separate access trigger in the decision weight/target path. Confirm whether faction membership is the accepted access proxy before interpreting P09.
- The P07 demographic pair must hold the two explicit community-opposition flags constant to test ordinary-score neutrality. I did not inspect the flag-generation classifier.
- No rank reversal, dominance, starvation, repetition rate, exact score, or normalized event-option share is established without the MCP analyzer.

## AI validity, route-lock, partner consent, and event-option weights

Route/source checks found sponsor targets must exist, not be actors, not be capitulated, and be neighbors or in the same faction. Commit rechecks partner capacity. Intervention partners are selected from non-capitulated faction members with the required resources. Absorption targets must exist, be actors, and be non-final/non-capitulated. The accept event transfers states only in the target's accept option. A distinct access trigger beyond faction relation was not found for intervention.

Event31.40/.41/.42 partner payments occur after explicit accept options, while refusal options do not charge partner resources. Event31.43 actor absorption transfers states only in its accept option at `events/031_terrorist_attack.txt:351-372`, and Event31.44 faction membership is accepted/refused at `:391-419`. AI uses `ai_chance` accept/refuse branches. A human chooses the same event options. The initiation decisions pay their own displayed request costs before the response.

| Event option pool | Source AI weights and relevant named fixture | Evidence status |
| --- | --- | --- |
| Event31.40 allied intelligence | Accept base 70, × high factor at war, refuse base 30. P05 transnational safe haven, with partner capacity and faction relation. | Source formula only, no normalized share. |
| Event31.41 intervention | Accept base 70, × high factor for a major, refuse base 30. P09 major intervention, sweeping partner access and capacity. | Source formula only, no normalized share. |
| Event31.42 sponsor | Accept base 70, × low factor at war, refuse base 30. P05, sweeping sponsor evidence and partner capacity. | Source formula only, no normalized share. |
| Event31.43 actor absorption | Accept base 60, × high factor when target actor control is below low, × low factor when target is at peace, refuse base 40. Use the matching descriptive actor-route row, such as sponsor-backed criminal-political actor or compatible faction-seeking actor. | Source formula only, no machine scenario ID exists in the matrix. |
| Event31.44 Jihadist International membership | Accept base 70, × high factor when the receiving actor is network leader, refuse base 30. Use the Evolution IV-compatible actor seeking faction leadership row. | Source formula only, no machine scenario ID exists in the matrix. |

The P05/P09 and actor-route option pools have no probability artifacts. The follow-up auditor request covered Event31.40–.43 but did not return after three 30-second waits and was shut down. Event31.44 was separately checked in source and remains equally unresolved because the probability route is unregistered. Do not treat these source formulas or consent branches as event-option probability evidence.

## Cleanup, cooldown, and exploit-risk notes

Mission slots 1–3 cap the number of concurrent country missions at three. The eight mission IDs are divided across slots 1, 2, and 3. Cancel, timeout, and completion paths clear subject receipts and the corresponding slot. Actor decisions use the 14-day action lock and target receipt flags. Government decisions use centralized re-enable constants and close recovery/action families through cleanup helpers.

`random_terror_movement_restrictions` has a hard expiry through `days = @rt_restriction_days` and prevents concurrent stacking with `random_terror_movement_restrictions_active`. A permanent `random_terror_movement_restrictions_used` flag makes repeat use add Condemnation, but the repeat cost does not rise as the accepted matrix requests.

Finite receipts are consumed for defection, militia-conversion, target support, mission slots, and actor-action cooldowns. The helper-return debit/regrant patterns net to one displayed payment at current constants. The retake XP double debit depends on the currently equal but separately tuned `government_army_experience` and `retake_army_experience` constants. No proven free equipment/manpower loop was found in those paths. The larger risk is that required unit operations are absent while flags report the action.

## References and validation limits

Local offline reference fallback was used because the callable `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup` methods were absent. `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:308-340` documents custom-cost base/blocked/tooltip keys and that custom costs require manual debit. `:463-478` documents mission timeout/available/selectable semantics. `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:1250`, `:1516`, and `:1522` document manpower, equipment, and fuel comparisons using `>` or `<`. Installed `common/decisions/_documentation.md:18-45` documents `available`, `target_trigger`, and that each matching target creates a dedicated decision entry. Vanilla precedent `common/decisions/BRA.txt:357-377` uses a targeted custom cost and manually debits command power in `complete_effect`. Its cost threshold is `>24.9` for a cost of 25.

The event-target and temporary-variable lifetime review used `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263-305` and `:435-442`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:357-360`, installed `effects_documentation.md:6496-6511`, and installed `triggers_documentation.md:3844-3851`. Regular targets persist through events fired by the originating effect chain and then clear automatically. Caller-preinitialized temporary values can be modified by scripted helpers inside that chain.

The requested `hoi4.decision_inspect`, `hoi4.gui_inspect`, and `hoi4.gui_render` calls each failed before service dispatch with `TypeError: tools.mcp__hoi4_agent_tools__<route> is not a function`. `Object.keys(tools)` contains no callable `mcp__hoi4_agent_tools__*` methods, although metadata lists schemas. The probability auditor independently confirmed that probability inspect/evaluate/sweep/compare/render routes are unregistered in its active tool inventory. These are pre-call route blockers, not timeouts. No narrower retry could be made. No MCP artifact, screenshot, GUI render, focus render, runtime validation, game launch, or log request exists.

Meaningful checks performed: direct source/line tracing of all decision cost triggers and complete effects, all 8 mission lifecycle blocks and relevant outcome helpers, category gates, actor-variable initialization/read/write sites, cost-key coverage, constants, and partner accept/refuse branches. A mechanical check found no missing referenced Event31 cost/tuning/value constant leaves among 83 distinct references and no missing decision/mission title, description, or source-referenced trigger/effect tooltip key. It found zero cost `_blocked` and `_tooltip` companions. No tests were run because this was an explicitly read-only audit.

## Handoff summary

Files changed: this handoff only. No decision, mission, scripted-GUI, gameplay, asset, or localisation identifier was changed. Before/after gameplay behavior is unchanged. The findings describe current source behavior.

Remaining blockers: five mission success flags have no reachable producer. The actor-control value aliases diverge after initialization. Affordability is not explicitly gated in `available` and exact balances fail strict `>`. Depot repair hides its Authority cost. Five operations exceed the three-value inline display limit. Cost blocked/hover localisations are absent. Several mapped actor operations do not perform their promised unit/economic change. The hostage mission lacks partial timeout. Actual multi-target row counts and visual layout remain unverified. And all AI probability results remain unresolved until callable HOI4 MCP routes are restored.

No separate improvement-plan file was written because the user requested this bounded audit and one evidence handoff only. The report identifies the existing-file fixes and the wider design gaps for owner disposition.
