# Event 31 decision and mission audit handoff

Audit scope is Event 31 Random Terror (`chaosx.nr31.1`), the Minor Repeatable chaos-level-1 event, limited to `common/decisions/031_random_terror_decisions.txt`, `common/decisions/031_random_terror_missions.txt`, and `common/decisions/categories/031_random_terror_categories.txt`.

The accepted evolution names remain Organized Cells, Transnational Terror Network, Territorial Insurgency, The Jihadist International, and The Final Jihad.

No Event 31 GUI, 3D pipeline, Internal Fracture registration, localisation edit, helper edit, or commit was made.

## Evidence and blockers

I read `AGENTS.md`, the complete `docs/specs/031_random_terror_specs/` folder, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` before editing.

I consulted the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, interface modding, and scripted GUI modding.

I consulted the installed vanilla decision documentation and vanilla precedents in `common/decisions/_generic_decisions.txt` and `common/decisions/_exiled_governments_decisions.txt`.

The mandatory `hoi4.gui_inspect` call was attempted against `decision_tab` for `random_terror_government_response_category` with the Event 31 decision IDs and returned: `MCP tool \`hoi4_agent_tools/hoi4.gui_inspect\` is not available to the model`.

The mandatory `hoi4.gui_render` call was attempted for 1920x1080 and 1280x720 across normal, hover, selected, locked, disabled, warning, active, completed, long-text, and missing-localisation states and failed with: `TypeError: tools.mcp__hoi4_agent_tools__hoi4_gui_render is not a function`.

No production GUI render artifact exists, so the source category review below is not equivalent to in-game visual evidence and the visual validation blocker remains open.

The mandatory `hoi4.probability_inspect` call for `decision_ai_will_do` on the three scoped files failed with: `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`.

The read-only `chaosx_ai_probability_auditor` was started for P01 through P10 and returned an incomplete engine audit with no baseline or comparison artifact.

Its source request using `relativePath` failed schema validation with `Unrecognized key: \"relativePath\" at source`.

The corrected `{path: ...}` source request returned `INTERNAL_ERROR` with `artifactCount: 0` and blocker `Unexpected internal error`.

The source-less inspection returned `PROBABILITY_ADAPTERS_LISTED` with `availableAdapters: []`, `candidates: 0`, and `availableCandidates: 0`.

The relative-path inspection timed out after 180 seconds, and the inline Clausewitz inspection was terminated after approximately 95 seconds with no result.

No probability artifact/resource URI, source revision, scenario hash, analysis ID, or comparison ID was produced.

Because the probability route is unavailable, no AI weight was patched and no probability result is claimed.

## Changes made

`common/decisions/031_random_terror_decisions.txt:529-576` now requires `random_terror_evolution_2_unlocked` in the support-disruption visible, available, root-target, and target checks.

Before this change, the visible OR was tautologically true whenever the response cell existed, and the available and target checks omitted Evolution II.

`common/decisions/031_random_terror_decisions.txt:2170-2210` now requires `random_terror_route_shadow_council` in relocation visible and available checks, matching the existing target-root check.

Before this change, relocation could appear with no valid target because only the target-root check knew that it belonged to Shadow Council.

`common/decisions/031_random_terror_decisions.txt:2315-2318` now debits the conversion XP once before and once after `random_terror_actor_convert_militia`.

Before this change, the helper granted the same 8 XP that the decision debited, so the displayed XP cost netted to zero; after the change the helper output is retained as conversion benefit while the decision consumes one conversion cost.

`common/decisions/031_random_terror_missions.txt:511-537` no longer attempts to clear the state-scoped `random_terror_hostages_recovered` and `random_terror_hostage_crisis_resolved` flags as country flags.

The complete and timeout paths still clear both flags inside the subject state and still clear the country mission slot and `random_terror_hostage_crisis_active` flag.

The transport and retake mission cleanup paths also clear their state-scoped commitment markers, `random_terror_transport_protection_committed` and `random_terror_retake_commitment_active`, on cancellation, completion, and timeout.

The depot repair, external corridor, actor absorption, network-contest, and Jihadist International decisions now repeat their existing route locks across visible/available/target-root layers where the route was previously only enforced in one layer.

The category file was inspected and left unchanged.

## Severity-sorted issues

### Blockers and high severity

1. GUI evidence is unavailable because both required GUI MCP routes failed exactly as recorded above.

2. The government-wide cooldown is not enforced by the decision surface.

`random_terror_response_action_lock` sets the 14-day `random_terror_action_recent` flag in `common/scripted_effects/031_random_terror_effects.txt`, but `random_terror_can_government_response` and the government decisions do not test that flag.

The per-decision `days_re_enable` values prevent repeating one ID, but a player can alternate different government decisions during the shared lock.

The correct owner fix is the shared government trigger/helper or a consistent visible gate in every government decision; it is outside the requested file boundary and was not duplicated locally.

3. The government category contains 24 decision entries including the terminal counteroffensive, while the actor category contains 17 entries.

Their phase and route conditions reduce the set in some states, but there is no category-level phase presentation or hard six-action cap in the scoped source.

A late-network government can expose targeted raids, corridor disruption, allied intelligence, defection, restrictions, community protection, sponsor actions, reinforcement, capital security, territorial recovery, intervention, accounting, reform, and other actions at once.

This violates the accepted compact 3–5 action budget and requires an owner-level phase filtering or replacement pass rather than a new GUI.

4. Several alliance actions are AI-partner-only and cannot provide explicit human-player consent in multiplayer.

`random_terror_request_allied_intelligence` and `random_terror_request_intervention` use `any_country { is_in_faction_with = ROOT is_ai = yes NOT = { has_capitulated = yes } }` and delegate acceptance to helpers.

The action consumes the requester cost before the helper transaction, so the owner must add partner targeting, consent, partner-side cost handling, and invalidation for a partner that changes status between selection and completion.

5. `random_terror_call_coordinated_uprising` validates the controller and pressure in visible, available, and target triggers, but the complete effect does not perform a final controller/pressure/route transaction check before spending and starting the uprising.

In multiplayer, a controller can change between target selection and completion.

The owner must add an atomic final validation and stale-target cleanup without refunding already consumed costs.

6. Four visible costs omit a real spendable resource from localisation.

`random_terror_military_reinforcement` consumes command power, fuel, infantry equipment, and manpower at `common/decisions/031_random_terror_decisions.txt:1034-1047`, but `localisation/english/031_terrorist_attack_l_english.yml:254` displays only command power, fuel, and manpower.

`random_terror_prepare_retake` consumes army experience, fuel, and infantry equipment at `common/decisions/031_random_terror_decisions.txt:1325-1333`, but `localisation/english/031_terrorist_attack_l_english.yml:278` displays only army experience and fuel.

`random_terror_prepare_state_offensive` consumes Network Authority, army experience, fuel, and infantry equipment at `common/decisions/031_random_terror_decisions.txt:2600-2610`, but `localisation/english/031_terrorist_attack_l_english.yml:380` displays no infantry equipment.

`random_terror_recruit_foreign_fighters` requires and later debits `foreign_fighter_manpower` at `common/decisions/031_random_terror_decisions.txt:2837-2860`, but `localisation/english/031_terrorist_attack_l_english.yml:398` displays no manpower.

These localisation fixes are required from the localisation owner and were intentionally not made here.

7. Every actor Network Authority cost is printed as a literal `Network Authority` label without a texticon in `localisation/english/031_terrorist_attack_l_english.yml:314-416`.

The actor costs are still within the four-cost limit, but they violate the icon-first cost contract and are difficult to scan consistently.

`random_terror_convert_militia_cost` also uses `actor_convert_experience` for both the Authority label and the army experience icon, so it will drift if those values are separated later.

`random_terror_build_civil_administration` charges Network Authority using `actor_administration_civilian_factories` at `common/decisions/031_random_terror_decisions.txt:2700-2705`, while its localisation displays a civilian-factory icon and amount; this is a semantic cost mismatch, not merely an icon style issue.

### Medium severity

8. Several accepted operations are not bound to the concrete state, route, or partner described by their visible text.

`random_terror_open_external_corridor` targets an arbitrary actor-controlled state without requiring a border, port, adjacent country, or reachable foreign route.

`random_terror_support_foreign_cell` targets an arbitrary external active crisis without proving that it contains the actor's cell or network.

`random_terror_prepare_state_offensive` targets the actor's own controlled state and does not require war, an adjacent government-held state, supply, or available forces even though its localisation promises a neighboring target.

`random_terror_prepare_retake` does not require war, supply, or available forces beyond the lost-state marker.

Defection and sponsor actions delegate actor/sponsor association to broad or random helper selection rather than binding the selected evidence state to the relevant actor or sponsor.

These require owner/helper or a bounded target-contract change and were not broadened here.

9. `random_terror_establish_response_cell` is a non-targeted decision whose complete effect chooses a random valid owned state at `common/decisions/031_random_terror_decisions.txt:65-72`.

The resulting containment mission does use an exact state subject flag, but the player cannot choose that initial state.

This is a design-level exact-state presentation gap that should be resolved in the specification/owner pass before converting the decision to a targeted action.

10. Several actor actions disappear when later evolutions unlock instead of being replaced by clearly phased equivalents.

Local militia and integrate defectors require `NOT evolution_2`, foreign-cell support, militia conversion, and ideological mobilisation require `NOT evolution_3`, and external corridors require `NOT evolution_4`.

This can leave an actor with fewer than its intended response options during an advanced route and can exhaust actor reserves when the expected late action is no longer available.

The fix needs a route/phase design decision because removing all gates would worsen the already excessive action density.

11. Movement restrictions and community protection use country-level timed flags while the actions are state-targeted.

The target is saved for the immediate effect, but the timed lock does not retain a state subject, so later uses can move the country-wide effect to another state without a state ledger or rising repeat cost.

The owner should either make the effect explicitly country-wide in text and logic or persist and clean an exact state subject.

12. The failed-raid identifiers are inconsistent across the scoped AI checks and helper/effect state.

`random_terror_failed_raid_recorded` is state-scoped in the event resolver, while `random_terror_failed_raid_memory` is set as a country flag by the targeted-raid helper.

The establishment and public-accounting AI checks use `has_country_flag = random_terror_failed_raid_recorded`, and the contain mission AI does the same at `common/decisions/031_random_terror_missions.txt:90`.

The targeted-raid AI check at `common/decisions/031_random_terror_decisions.txt:525` correctly uses the state scope, but the other checks cannot be probability-correct until the owner chooses the intended scope.

This is an AI-weight patch and therefore remains unpatched pending the required P01–P10 baseline and compare workflow.

The probability auditor also found ordinary-government-ideology modifiers on quiet sponsor leverage, public accounting, and security reform at `common/decisions/031_random_terror_decisions.txt:989`, `:1632`, and `:1678`.

These are action-policy weights rather than target or recruitment weights, so they do not by themselves violate the identity-neutral target rule; the owner should remove them if the project rule is intended to cover every action score.

The auditor found a Muslim-named positive AI modifier on community protection at `common/decisions/031_random_terror_decisions.txt:867-868`.

The flag reads as recorded community opposition rather than identity, but its Evolution IV-only producer cannot be proven from this scope and must be verified by the owner.

The auditor also found that several jihadist-route actions rely on the route flag without an explicit Evolution IV check.

The owner must prove that `random_terror_route_jihadist_international` cannot exist before Evolution IV or add the explicit gate consistently, because Evolution IV alone owns the fictional jihadist branch.

13. Several state commitment flags have no source-local cleanup path.

The scoped source sets `random_terror_community_protection_committed`, `random_terror_reinforcement_subject`, `random_terror_reinforcement_committed`, `random_terror_relief_corridor_subject`, `random_terror_state_offensive_subject`, and `random_terror_force_extraction_subject` without clearing them.

Some appear intentionally persistent as one-per-state duplicate guards, but the owner must document and verify cleanup on state loss, annexation, actor defeat, route closure, evolution disablement, and scenario end.

`random_terror_surrender_negotiation_active` is helper-owned and likewise has no clear in the scoped source.

14. Mission cancellation checks `world_end` but not `random_terror_terminal_active`.

The terminal category and terminal counteroffensive use `random_terror_terminal_active`, so the owner must confirm whether ordinary active missions should be cancelled at terminal entry or remain available for terminal counterplay.

This was not changed because the accepted specification says to preserve terminal campaign logic and the shared terminal contract is outside the three allowed files.

### Lower severity and quality gaps

15. Most costs are centralised `script_constants`, but they are flat values rather than state-size, industry, stockpile, supply, geography, pressure, or actor-resource-scaled costs.

They are readable and concrete, but the balance specification calls for dynamic scaling where it affects large states, foreign reach, and territorial operations.

16. Custom requirement tooltips are present for the decisions, but several only say that a valid partner, route, threat, or site is required and do not expose the exact blocked threshold or the reason a selected target is invalid.

17. The false-revelation decision correctly delegates the final gate to `random_terror_can_begin_false_revelation`, requires Evolution V and the fictional final actor route, and does not bypass the Chaos/readiness/territory checks when acceleration is pressed.

Its category visibility lacks an explicit `world_end` check, so the owner should verify the final-actor cleanup state in production evidence.

## Category lifecycle and cognitive load

The government category is visible for non-actors before world end when a government response or reconstruction state exists, has an ordinary static picture and icon, and highlights owned/claimed/core states with the Dormant, Active, Entrenched, Armed Insurgency, Lost Local Control, and Recovery flags.

The actor category is visible for actor countries before world end, uses a static picture and icon, and highlights actor-controlled crisis stages.

The false-revelation category is visible for the final actor when the terminal is active or the branch is enabled and has no scripted GUI.

The category descriptions are concise and expose Terror Pressure plus Response Legitimacy for governments and Territorial Control plus Network Authority plus External Supply for actors.

The values have clear names, but the category text does not show the next threshold, state activity, route lock, mission slot, or consequence band, so players still need tooltips and map state flags to understand significance.

The government and actor source surfaces exceed the accepted six-primary-action ceiling in combined late states.

The eight mission definitions use three country slots, so at most one slot-1, one slot-2, and one slot-3 mission can be active, which keeps simultaneous missions at three.

Decision descriptions are generally one sentence and the mission descriptions are compact, but generic blocked tooltips and the uniconised Authority costs create avoidable scan load.

No scoped trigger uses religion, ethnicity, nationality, refugee status, or ordinary ideology as a baseline target or recruitment weight.

The only Muslim-specific flags in scope are state-level opposition/rejection signals used by the community-protection response, and the jihadist actions are gated by the fictional Evolution IV route flags.

## Government action audit

The following entries cover every government and terminal action in the scoped file.

| ID | Target and lifecycle | Cost and AI review |
|---|---|---|
| `random_terror_establish_response_cell` | Non-targeted; finds a random owned active crisis state, reserves slot 1, and activates containment. | Command power plus support equipment; one-use; AI exists, but the random target weakens exact-state presentation and its failed-raid country check is scoped incorrectly. |
| `random_terror_protect_transport` | Exact controlled active/entrenched state with infrastructure or transport/port disruption; reserves slot 1 and activates the 120-day transport mission. | Trains, fuel, and support equipment; AI has capital/disruption priorities; success is deferred to the mission. |
| `random_terror_support_victims` | Exact controlled active/entrenched/recovery or relief/transport-strain state; timed country commitment with no mission. | Support equipment, trains, and manpower; target is blocked while a response cell is active except recovery, matching an immediate-response phase but not stated in the action text. |
| `random_terror_intelligence_sweep` | Exact controlled active/entrenched state; requires a response cell and no existing evidence/high-pressure shortcut; records a country breakthrough and state completion. | Command power plus support equipment; AI exists and target flag is state-scoped. |
| `random_terror_security_surge` | Exact active/entrenched incident state; reserves slot 1 and activates containment, hostage, or uprising resolution hooks. | Command power, fuel, and support equipment; AI prioritises capital, hostage, and recent incidents; it is unavailable once the response cell is active. |
| `random_terror_targeted_raid` | Exact active/entrenched state; requires response cell plus intelligence or high legitimacy and resolves through the five-outcome helper. | Command power, army experience, and support equipment; AI exists, but failed-raid memory/recorded identifiers need probability-audited correction. |
| `random_terror_disrupt_support` | Exact evidence-bearing state; now requires Evolution II in all visible, available, and target checks, reserves slot 2, and activates corridor mission. | Convoys, command power, and support equipment; before the patch the response-cell OR bypassed Evolution II. |
| `random_terror_request_allied_intelligence` | Exact active/entrenched state; requires an AI faction partner and opens a helper-owned request without selecting the partner. | Command power plus support equipment; multiplayer human consent and partner-side spending are missing. |
| `random_terror_offer_defection_channel` | Exact active/entrenched defection state; requires a reachable non-final actor and opens a helper-owned channel. | Command power, manpower, and support equipment; AI reacts to defection flags, but leader/atrocity validation is helper-owned. |
| `random_terror_movement_restrictions` | Exact active/entrenched state above the high pressure threshold; applies a 45-day country flag. | Stability, support equipment, and manpower; repeated target changes are not state-ledgered and the cost does not rise. |
| `random_terror_protect_community_sites` | Exact threatened active/entrenched state with rejection or Muslim opposition evidence; applies a timed country commitment. | Support equipment plus manpower; the opposition flag is actor-specific in the accepted design, but the decision has no explicit Evolution IV guard and depends on upstream flag discipline. |
| `random_terror_expose_sponsor` | Exact sponsor-evidence state; one-use exposure and neutralisation helper. | Command power plus support equipment; AI and cleanup are present, with no human partner selection. |
| `random_terror_quiet_sponsor_leverage` | Exact sponsor-evidence state; one-use quiet leverage helper. | Command power plus support equipment; AI and cleanup are present, but the request is helper-owned and not a visible consent transaction. |
| `random_terror_military_reinforcement` | Exact controlled active/entrenched/armed state that is not lost; commits a reinforcement marker. | Command power, fuel, infantry equipment, and manpower; all four are debited, but the localisation omits infantry equipment and the helper does not itself create a division. |
| `random_terror_capital_security` | Exact capital state with infiltration; reserves slot 2 and activates the 75-day capital mission. | Command power, fuel, and support equipment; AI prioritises war and major-country capital defense. |
| `random_terror_isolate_enclave` | Exact lost-local-control claimed/core state; applies isolation and a surrender window. | Trains, fuel, convoys, and support equipment, exactly four spendable types; target and supply-route validation are helper-dependent. |
| `random_terror_relief_corridor` | Exact lost/armed/recovery claimed/core state with relief strain; applies recovery effects. | Convoys, support equipment, and manpower; exact state is saved, with no separate mission. |
| `random_terror_prepare_retake` | Exact lost-local-control claimed/core state; reserves slot 3 and activates the 180-day retake mission. | Army experience, fuel, and infantry equipment, exactly three source costs; the helper grants XP so the double debit is intentional, but localisation omits infantry equipment. |
| `random_terror_negotiate_surrender` | Exact isolated lost state with surrender window and a live non-final actor owner; helper checks whether terms are viable. | Command power, manpower, and support equipment; one-use decision protects against repeated selection, but actor acceptance and atrocity/apocalyptic blocks are helper-owned. |
| `random_terror_request_intervention` | Exact lost/armed claimed/core state; requires an AI faction partner and opens helper-owned intervention. | Command power, convoys, and support equipment; human consent, partner targeting, and race-safe acceptance are missing. |
| `random_terror_restore_services` | Exact controlled recovery state; reserves slot 3 and activates the 150-day civil-authority mission. | Support equipment, trains, and manpower; success and cleanup are state-scoped. |
| `random_terror_public_accounting` | Country-wide, non-targeted post-incident/sponsor/raid accountability action. | Command power plus support equipment; a country-level completion marker prevents normal repetition, but failed-raid flag scope is wrong in source AI and requirements. |
| `random_terror_security_reform` | Country-wide recovery action requiring public accounting/reconstruction and no active state. | Army experience, support equipment, and manpower; AI exists, but the category still shows many unrelated actions alongside it. |
| `random_terror_terminal_counteroffensive` | Country-wide terminal action for an affected government, one-use and not actor-owned. | Command power plus support equipment; helper owns terminal result, with no local cooldown beyond one-use. |

## Actor action audit

| ID | Target and lifecycle | Cost and AI review |
|---|---|---|
| `random_terror_raise_local_militia` | Exact actor-owned state; baseline action is disabled after Evolution II and helper returns manpower/equipment before the final debit. | Network Authority, manpower, and infantry equipment; three costs and actor cooldown are present, but later-route disappearance needs design review. |
| `random_terror_integrate_defectors` | Exact actor-owned defection state; baseline action is disabled after Evolution II. | Network Authority, infantry equipment, and manpower; helper output is netted, with actor cooldown. |
| `random_terror_repair_captured_depot` | Exact compromised state on supported actor routes; route locks now repeat in visible, available, and target-root layers. | Support equipment and fuel; target, helper effect, and actor cooldown align. |
| `random_terror_open_external_corridor` | Exact owned/controlled state on Evolution II ideological/jihadist routes; route locks now repeat in visible and available, but the action is disabled after Evolution IV. | Network Authority, convoys, and fuel; no actual border/port/foreign-route target is required, and later Jihadist use may lose a required supply action. |
| `random_terror_seek_sponsor` | Targeted live non-actor neighboring or faction country; helper records a sponsor request. | Network Authority, command power, and support equipment; partner consent and hostile/route-change cleanup are helper-owned. |
| `random_terror_support_foreign_cell` | Exact external crisis state owned by a live non-actor; Evolution II route action is disabled after Evolution III. | Network Authority, convoys, and support equipment; it resolves immediately, but its late-route disappearance is a balance gap. |
| `random_terror_relocate_network` | Exact controlled active/entrenched threatened state; visible and available now require Shadow Council, matching target root. | Network Authority, fuel, and support equipment; the patch removes the dead-action presentation. |
| `random_terror_convert_militia` | Exact actor-controlled active/entrenched militia state on the War Directorate route; disabled after Evolution III. | Network Authority, army experience, infantry equipment, and support equipment, exactly four costs; the patch makes XP consumption net real. |
| `random_terror_ideological_mobilization` | Exact active/entrenched state on the ideological route; disabled after Evolution III. | Network Authority, manpower, and support equipment; timed action and helper cleanup exist, but route progression can remove it too early. |
| `random_terror_absorb_actor` | Targeted live non-final actor on compatible routes; route locks now repeat in visible, available, target-root, and target layers; one-use merge transaction and cleanup helper. | Network Authority, support equipment, and fuel; MP target races still need helper validation. |
| `random_terror_contest_network_leader` | Targeted live jihadist actor with network leadership; Evolution IV and Jihadist International route are now both visible/available gated. | Network Authority, command power, and support equipment; helper owns the contest debit and outcome, and AI requires probability comparison. |
| `random_terror_prepare_state_offensive` | Exact controlled active/entrenched/armed state on War Directorate after Evolution III. | Network Authority, army experience, fuel, and infantry equipment, exactly four costs; state subject and helper commit are present, but localisation omits infantry equipment and no actual neighboring target is selected. |
| `random_terror_build_civil_administration` | Exact lost state on War Directorate after Evolution III. | Source charges Network Authority, manpower, and support equipment, while localisation displays a civilian-factory cost; source and visible cost are inconsistent. |
| `random_terror_force_extraction` | Exact controlled populated active/entrenched state on War Directorate after Evolution III. | Network Authority, manpower, and support equipment; helper raises supply and records condemnation, with no free resource path. |
| `random_terror_recruit_foreign_fighters` | Country-level one-use Evolution IV ideological/jihadist action requiring external supply. | Network Authority, convoys, infantry equipment, and manpower; manpower is required and debited but omitted from localisation, and helper output still needs scenario balance evidence. |
| `random_terror_join_jihadist_international` | Targeted live jihadist network leader after Evolution IV; route locks now repeat in visible, available, target-root, and target layers; one-use transaction. | Network Authority, command power, and support equipment; final transaction validation exists, but MP target change can consume cost before helper rejection. |
| `random_terror_call_coordinated_uprising` | Exact external active crisis state after Evolution V with pressured controller; starts slot-2 uprising mission. | Network Authority, convoys, and support equipment; final controller race and stale mission cleanup remain unresolved. |

## Mission audit

All eight missions are non-selectable ordinary decision missions with constant-driven timeouts, exact state subject flags, success-driven `available` completion, explicit cancellation, complete effects, timeout effects, AI, and three shared mission slots.

| Mission | Owner/category/region and duration | Requirement, success, failure, cleanup, duplicate risk |
|---|---|---|
| `random_terror_contain_attack_wave` | Government response category, ROOT government, exact containment subject state, 90 days. | Success requires containment success; timeout is partial when activity is at/below the active threshold and failure otherwise; subject, success, slot, and surge flags clear; AI has a country/state failed-raid scope mismatch. |
| `random_terror_protect_transport_network` | Government response category, ROOT government, exact transport subject state, 120 days. | Success requires ROOT control plus transport protection success; timeout is partial when transport remains undisrupted and failure when disruption persists; subject, commitment, success, slot, and active flag clear. |
| `random_terror_break_cross_border_corridor` | Government response category, ROOT government, exact corridor subject state, 150 days. | Success requires support-disruption success; timeout is partial when the corridor is no longer recorded and failure when it remains; subject, success, and slot clear. |
| `random_terror_prevent_capital_seizure` | Government response category, ROOT government, exact capital subject, 75 days. | Success requires a controlled capital plus capital-security success; timeout is partial while the capital remains controlled and failure otherwise; subject, success, slot, and active flag clear. |
| `random_terror_retake_lost_state` | Government response category, ROOT government, exact retake subject, 180 days. | Success requires ROOT control and no lost-control flag; timeout is partial while controlled and failure otherwise; subject, commitment, slot, and preparation flag clear. |
| `random_terror_restore_civil_authority` | Government response category, ROOT government, exact recovery subject, 150 days. | Success requires control plus civil-authority restored; timeout is partial only at Dormant and failure otherwise; subject, success, and slot clear. |
| `random_terror_hostage_deadline` | Government response category, ROOT government, exact hostage subject, 45 days. | Success requires recovered or resolved state flag; timeout is a complete failure with no partial branch; state flags, subject, slot, and active country crisis clear, with the invalid country-scope clears removed by this audit. |
| `random_terror_stop_coordinated_uprising` | Government response category, ROOT government, exact uprising subject after Evolution V, 90 days. | Success requires uprising stopped; timeout is partial while ROOT still controls the state and failure otherwise; subject, stopped flag, and slot clear. |

Mission duplicate protection is good at the slot level, because decisions reserve slot 1, 2, or 3 before activation and subject flags prevent a second target in the same mission family.

Mission cancellation still depends on the shared response trigger and helper cleanup for annexation, actor defeat, route closure, target change, evolution disablement, sponsor death, and save/reload transitions.

## Cost and requirement audit

Every scoped action has a `custom_cost_trigger`, a `custom_cost_text`, and an explicit debit in its complete effect.

The source cost count is within the four-spendable-type ceiling for every decision, with the maximum being four on enclave isolation, military reinforcement, militia conversion, and state offensive preparation.

The costs are mostly constants, not unexplained magic numbers, and mission durations are centralised under `random_terror_tuning`.

The missing infantry-equipment displays and uniconised Network Authority labels listed above violate the required visible-cost contract and need localisation-owner changes.

The strict `>` checks require one more unit than the named constant, which may be an intentional reserve buffer but is not explained in the generic requirement tooltips.

## AI validity, route locks, surrender, and coalition counterplay

All decision and mission blocks define `ai_will_do`; there are no omitted AI blocks that silently default to never.

The actor shared cooldown is part of `random_terror_can_actor_action`, while the government shared action lock is not part of `random_terror_can_government_response`.

Most targeted AI candidates have root and target triggers, but scenario-specific weights, invalid-target zeroing, reserve exhaustion, and route frequency cannot be certified without the unavailable probability MCP route.

The AI scenario contract requiring P01 stable peace, P02 unstable wartime authoritarian, P03 occupied resistance, P04 successful response, P05 transnational safe haven, P06 territorial spawn, P07 Muslim government against jihadist, P08 cannibal border, P09 major intervention, and P10 maximum scenario remains unrun.

Surrender is restricted to a lost isolated state with a live non-final actor and delegates weakness, settlement, atrocity, and apocalyptic checks to helpers.

Intervention and allied intelligence provide the only explicit coalition support path in the scoped decisions, and both currently exclude human allies.

Foreign sponsor, absorption, jihadist membership, and uprising transactions need helper-level consent and final target validity for safe multiplayer use.

No baseline target or recruitment logic in the three scoped files increases weight because of religion, ethnicity, nationality, refugee status, or ordinary ideology.

## Localisation, cleanup, and exploit notes

Category, action, mission, requirement, and effect keys are present in the inspected English localisation file, but the cost display omissions and literal Authority labels need owner fixes.

The mission cleanup paths are generally complete and clear subject flags on success, failure, timeout, and cancellation.

The patched hostage path now clears hostage result flags in state scope only.

The remaining exploit risks are alternating government actions through the missing shared cooldown, re-targeting country-timed restrictions/support commitments, consuming costs across multiplayer target races, and late-route actors losing the action needed to spend their own reserves.

Victim support, reinforcement, militia raising, defector integration, and retake preparation use helper output plus compensating debits; the inspected source does not show a free repeated unit/equipment loop, but the foreign-fighter output still needs scenario balance evidence.

## Validation and handoff

The three patched source files were re-read after the edits, and the exact Evolution II, Shadow Council, conversion XP, and hostage state-scope changes were confirmed by line-level searches.

The eight mission IDs and 41 decision IDs were enumerated from the scoped source, with no Internal Fracture identifier found.

The required GUI and probability MCP validations were attempted but remain blocked by the exact errors recorded above.

No in-game launch or live gameplay validation was performed, as required by repository policy.

Remaining work is the GUI production evidence, P01–P10 probability baseline/compare, category phase-density redesign, government shared cooldown owner fix, multiplayer consent/atomic transaction fixes, and localisation cost-icon/amount corrections.

Handoff path: `docs/plans/031_random_terror_plans/subagent_handoffs/031_decision_mission_audit_handoff.md`.
