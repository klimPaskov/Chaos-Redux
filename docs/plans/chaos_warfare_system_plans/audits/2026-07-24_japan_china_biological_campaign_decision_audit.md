# Japan-China Biological Campaign Decision Audit

## Scope and audit basis

This is a read-only audit of the bounded Japan-China biological campaign decision tranche.

It covers the two state-targeted decisions, their category, Japan-specific constants, triggers, effects, shared ordinary-pathogen lifecycle dependencies, localisation, sprite registration, the stated design documents, route and event dependencies, and the existing doomsday decision.

No gameplay, localisation, specification, asset, or existing documentation file was edited.

The only audit output is this handoff.

The binding audit constraints supersede conflicting wording in the current specification and implementation, especially the prohibition on refunds.

## Decision category lifecycle notes

- Owner: original Japan only, enforced by `original_tag = JAP` in `common\decisions\japan_biological_campaign_decisions.txt:18,84` and route visibility in `common\decisions\categories\japan_biological_campaign_categories.txt:5-10`.
- Category lifecycle: the category is visible only while `japan_bio_campaign_route_is_open` is true, so capitulation, loss of the China war, containment, reform, or shutdown hides both actions through `common\scripted_triggers\japan_biological_campaign_triggers.txt:22-38`.
- Target lifecycle: each decision is a supported state-targeted decision using `state_target = asia`, with the exact selected state in `FROM`, in `common\decisions\japan_biological_campaign_decisions.txt:14-15,80-81`.
- Release lifecycle: the selected state receives the private `japan_china_campaign` route, deliberate source, deterministic success result, real payload proof, exact actor and victim event targets, then `bio_lifecycle_dispatch_seed`, in `common\scripted_effects\japan_biological_campaign_effects.txt:153-168`.
- History lifecycle: only a successful shared dispatch records actor and exact-state history, state and national cooldowns, and the agent-specific history flags in `common\scripted_effects\japan_biological_campaign_effects.txt:45-110,169-183`.
- Cleanup lifecycle: ordinary lifecycle recovery clears active state and scheduling flags, current contamination modifiers, response markers, and related state variables without deleting deliberate-use history in `common\scripted_effects\biological_lifecycle_effects.txt:1948-2031`.

## Findings by severity

### High: doctrine Command Power refunds violate the binding no-refund rule

Theater Contamination refunds 2 Command Power and Terminal Hazard refunds 4 Command Power after a successful dispatch.

The values are defined in `common\script_constants\japan_biological_campaign_constants.txt:49-58`, copied into the decision parameters in `common\scripted_effects\japan_biological_campaign_effects.txt:28-42`, and actually credited back at `common\scripted_effects\japan_biological_campaign_effects.txt:180-183`.

This is a real refund after the displayed four-cost debit, not a preparation or aggression multiplier.

It also makes the visible 10 or 14 Command Power commitment inaccurate for doctrine holders because the actual net cost is lower, while `localisation\english\japan_biological_campaign_l_english.yml:16-24` continues to present the full amount as consumed.

The existing implementation documents the refund at `docs\biological_warfare\japan_china_biological_campaign.md:46-50`, and the shared specification explicitly permits it at `docs\specs\chaos_warfare_system_specs\specs\06_biological_warfare_and_outbreaks.md:228-232,262`.

Those documents therefore conflict with the binding audit constraint that releases use no refunds and that doctrine may reduce only Condemnation.

Recommended fix: remove the refund constants and the credit effect, retain doctrine as a shared lifecycle potency, growth, spread, death, duration, medical-load, preparation, and aggression modifier, and update all affected player-facing and specification wording in the later implementation task.

### High: the selected state can be controlled by a non-Chinese enemy

The decision requires the selected state to be a Chinese homeland core at `common\scripted_triggers\japan_biological_campaign_triggers.txt:85-95,125-133`, but the relationship helper accepts any existing controller that is at war with Japan and is neither Japan, a direct Japanese subject, nor a faction partner at `common\scripted_triggers\japan_biological_campaign_triggers.txt:97-110`.

`has_war_with_chinese_country` only proves that Japan is fighting at least one named Chinese country at `common\scripted_triggers\cbw_triggers.txt:220-231`; it does not prove that the exact selected state is controlled by that Chinese belligerent.

Consequently, a foreign enemy that controls a Chinese core state beside Japanese or Japanese-subject occupation can pass the target relationship gate and receive the Japan-China campaign release.

This contradicts the target tooltip and audit contract that name an enemy-controlled Chinese state, including `localisation\english\japan_biological_campaign_l_english.yml:10-11` and `docs\biological_warfare\japan_china_biological_campaign.md:21-27`.

Recommended fix: add an explicit selected-controller Chinese-belligerent identity check inside `japan_bio_campaign_state_relationship_is_valid`, using the same accepted China tag and released-tag policy as the campaign route, before the occupation-link check.

### Medium: `ai_hint_pp_cost` uses a script constant in a field whose documented constant support is unresolved

Both decisions assign `ai_hint_pp_cost = constant:japan_bio_campaign_cost...` at `common\decisions\japan_biological_campaign_decisions.txt:16,82`.

The offline decision reference states that `ai_hint_pp_cost` must be a fixed amount because it only tells AI how much Political Power to reserve, and it does not charge Political Power itself at `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:299-319`.

Vanilla 1.19.2 uses literal values with custom-cost decisions, for example `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\FIN.txt:240-245,426-434,790-796`.

The vanilla script-constant documentation only guarantees `constant:` where the field explicitly supports it, while this field has no documented support declaration in the installed docs at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md:216-226`.

This is an engine-compatibility uncertainty, not a proven gameplay defect, because the referenced values are fixed 35 and 40 and satisfy the semantic requirement if the parser accepts them.

Recommended fix: validate this exact field with the installed parser before commit; if it rejects `constant:`, use the project-approved fixed numeric representation for this engine-only AI reservation hint and preserve the authoritative values in the campaign constants.

### Low: the custom-cost display does not identify payload equipment with an icon

The custom cost text labels raw `Anthrax Payloads` and `Plague Payloads` rather than displaying an established payload text icon at `localisation\english\japan_biological_campaign_l_english.yml:16-21`.

The full cost is still clear in the custom tooltip at `localisation\english\japan_biological_campaign_l_english.yml:18,21`, and the four-cost gate and debit are correct.

This is a presentation-quality gap only; the custom-cost API exposes one met or blocked string for the full conjunction, so it cannot by itself colour each individual failed resource independently.

Recommended fix: use existing agent-payload text icons if they are registered, while retaining the short custom-cost summary and its detailed tooltip.

## Verified compliant behavior

- Exact selected state: the state-targeted decision API exposes the selected state as `FROM`, which the tranche preserves through target validation, saved event target, lifecycle seed, and state history. This is supported engine behavior, not an inferred target, under `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:561-579`.
- Occupation reach: `any_neighbor_state` accepts only a Japanese or direct Japanese-subject controller at `common\scripted_triggers\japan_biological_campaign_triggers.txt:112-123`; no proxy launch state, frontline estimate, or alternate state is created.
- Four-cost semantics: Anthrax and Plague custom-cost helpers each check Political Power, their distinct payload, Support Equipment, and Command Power at `common\scripted_triggers\japan_biological_campaign_triggers.txt:45-59`.
- Four debits: after committed revalidation, the effect debits Political Power, the selected payload type, Support Equipment, and Command Power at `common\scripted_effects\japan_biological_campaign_effects.txt:122-151`.
- Custom-cost semantics: the explicit debits are necessary and present because custom cost only controls availability and presentation, not payment, as documented at `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:299-319`.
- No fallback or refund on a shared lifecycle rejection: the failed dispatch branch sets only `japan_bio_campaign_dispatch_failure_history` at `common\scripted_effects\japan_biological_campaign_effects.txt:175-187`; it creates no proxy state, substitute evidence, inferred history, or material refund.
- Equal delivery acceptance: both decisions prepare only their agent parameters and set `bio_seed_result = ...success` through the one shared release path at `common\scripted_effects\japan_biological_campaign_effects.txt:12-26,114-168`; agent identity changes lifecycle profile, not this decision's delivery result.
- Distinct payloads: Anthrax debits `anthrax_bomb_1` and Plague debits `plague_bomb_1` at `common\scripted_effects\japan_biological_campaign_effects.txt:141-150`.
- Cooldowns and repeat protection: national cooldown is rechecked at `common\scripted_triggers\japan_biological_campaign_triggers.txt:11-20`, exact-state cooldown at `common\scripted_triggers\japan_biological_campaign_triggers.txt:74-83`, and successful dispatch writes national and 180-day state cooldown records at `common\scripted_effects\japan_biological_campaign_effects.txt:99-100,177-179`.
- Same-agent repetition is blocked while active at `common\scripted_triggers\japan_biological_campaign_triggers.txt:135-160`, while permanent target history lowers the future AI weight at `common\decisions\japan_biological_campaign_decisions.txt:69,138`.
- Shared lifecycle lifecycle acceptance requires the supplied payload proof, positive exact payload amount, valid actor and victim, and the selected controller at `common\scripted_triggers\biological_lifecycle_triggers.txt:11-63,214-243`.
- Shared lifecycle scheduling is exact-state event driven, not a global country pulse, through `events\biological_lifecycle_events.txt:15-93` and the scheduler guard comments and effects in `common\scripted_effects\biological_lifecycle_effects.txt:644-729,2034-2093`.
- Canonical severity rank and weapon potency are ordered Tularemia 1 and 0.85, Anthrax 2 and 1.00, Plague 3 and 1.15, and Smallpox 4 and 1.30 at `common\script_constants\biological_lifecycle_constants.txt:217-291`.
- Only Smallpox is accepted as a severe doomsday result in `common\scripted_triggers\biological_lifecycle_triggers.txt:155-211`; the Japan campaign itself always supplies ordinary success.
- Doctrine harm and Condemnation handling is otherwise compliant: doctrine increases potency, growth, spread, deaths, duration, and medical saturation while only Terminal Hazard reduces Condemnation at `common\script_constants\biological_lifecycle_constants.txt:417-446` and `common\scripted_effects\biological_lifecycle_effects.txt:250-349`.
- The doomsday route remains a decision, `bio_unleash_stockpiled_pathogens`, at `common\decisions\chemical_warfare_decisions.txt:59-108`.
- Normal strategic and battlefield delivery remain native raid surfaces outside this decision tranche, as recorded in the specification at `docs\specs\chaos_warfare_system_specs\specs\06_biological_warfare_and_outbreaks.md:238-245`.

## AI validity and route-lock notes

- AI evaluates only the state rows produced by the target trigger, then receives logistics weight for Anthrax and urban weight for Plague at `common\decisions\japan_biological_campaign_decisions.txt:55-75,121-144`.
- AI inherits the human availability checks for route, project, readiness, policy, exact target, payload, Support Equipment, Command Power, Political Power, and cooldown, so no distinct AI-only target or cost route exists.
- The AI repeatedly suppresses an exact previously used state, and reduces use under simultaneous high Condemnation and import vulnerability, at `common\decisions\japan_biological_campaign_decisions.txt:69-74,138-143`.
- The unresolved controller-identity finding above is also an AI target-safety defect because the same state pool is shared by AI and player.

## Cost and requirement clarity notes

- Every gameplay requirement is hidden behind custom trigger tooltips rather than exposing the raw state or policy trigger tree at `common\decisions\japan_biological_campaign_decisions.txt:27-46,93-112`.
- Requirement text names route authority, project, agent payload, Support Equipment, Command Power, and national cooldown at `localisation\english\japan_biological_campaign_l_english.yml:13-14`, while the custom cost strings and effect tooltips add Political Power at `localisation\english\japan_biological_campaign_l_english.yml:16-24`.
- The target tooltips identify Chinese core, enemy control, Japanese or subject adjacency, target profile, active same-agent episode, and cooldown at `localisation\english\japan_biological_campaign_l_english.yml:10-11`.
- The national and state cooldown durations are not displayed in the player-facing tooltip, and doctrine changes the national value, so the exact remaining restriction is understandable but not fully transparent.

## Mission quality notes

There are no missions in this bounded tranche.

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| None | N/A | `japan_biological_campaign_category` | Selected Chinese state | N/A | N/A | N/A | N/A | None |

The two entries are immediate state-targeted decisions, so mission duration, timeout effects, and mission duplicate checks do not apply.

## Localisation, sprite, and raid-icon notes

- All eight decision-facing target, requirements, custom-cost, and effect-tooltip roots referenced by the decision source are present in `localisation\english\japan_biological_campaign_l_english.yml:2-24`.
- Anthrax and Plague use their existing exact-agent sabotage sprites at `common\decisions\japan_biological_campaign_decisions.txt:13,79`, registered at `interface\biological_warfare.gfx:39-47`.
- The category sprite is registered as `GFX_decision_category_japan_biological_campaign` at `interface\biological_warfare.gfx:59-62` and the current DDS exists at `gfx\interface\decisions\biowarfare\japan_china\decision_category_japan_biological_campaign.dds` with a verified 52x40 DDS header and SHA-256 `D8FE58073EC62BA8CD8CB99DB2A3B551D04640D80443EA0D51E0E962ED8D7B04`.
- The category DDS appeared during this audit and is currently untracked, so the eventual implementation commit must include it with the listed decision and GFX changes.
- No current diff exists beneath `gfx\interface\military_raids`, and the campaign decisions reference only the two sabotage sprites rather than a raid icon.
- The category has no `scripted_gui` binding, so no decision-owned GUI window exists to render. Read-only GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cda72b68515c827015864b650d951624c77855990e32f04c2d9c96e77a1bd132/b7ea0b6fe1871d4c48db95d77785f61bbd40845c3ea4aea60fbd5c8dc1b919e0/gui-inspect.025907a8b80df60c.json` at shared revision `025907a8b80df60c4a1672ac3103f955efb388182af2128923f8d8937ca30920` found broad pre-existing workspace symbol collisions but supplied no category-window fidelity result.

## Scenarios checked

| Scenario | Result |
| --- | --- |
| Japan meets route, project, readiness, policy, all four costs, and national cooldown; a Chinese enemy homeland state is adjacent to Japanese control and matches Anthrax infrastructure or unit profile | Passes static gate, debits 35 Political Power, 8 Anthrax payload, 35 Support Equipment, and 10 Command Power, then dispatches the exact state as ordinary success. |
| Equivalent valid Plague target with capital, city, port, or population profile | Passes static gate, debits 40 Political Power, 10 Plague payload, 45 Support Equipment, and 14 Command Power, then dispatches the exact state as the same ordinary success. |
| Any one of Political Power, agent payload, Support Equipment, or Command Power is below its exact threshold | Both availability and `custom_cost_trigger` fail; no committed effect runs. |
| Containment, reform, shutdown, capitulation, no China war, missing program/readiness/policy, or missing project | Route or target-root gates hide the category or decision row and prevent AI and player use. |
| Selected state is Japan-controlled, Japanese-subject controlled, faction-partner controlled, non-Chinese core, impassable, uninhabited, lifecycle-ineligible, not occupation-adjacent, or on exact-state cooldown | Correctly rejected by the existing state gates. |
| Selected Chinese core is controlled by a foreign enemy while Japan is separately at war with China and has a qualifying occupation neighbor | Incorrectly eligible under the current controller relationship helper; this demonstrates the high-severity target-identity finding. |
| Successful release followed by immediate reuse against the same state or another state | Actor cooldown blocks all campaign releases, exact-state cooldown blocks the same state, and agent episode flags block the same agent while active. |
| Theater or Terminal doctrine release | Shared lifecycle receives increased operational-harm values and only Terminal reduces Condemnation, but both doctrine variants also credit forbidden Command Power refunds. |
| Shared lifecycle record rejected after debit | No fallback, alternate target, inferred history, or refund is created; only the diagnostic failure history flag is set. |
| GFX and asset review | Both action sprites and the category sprite are registered, all three current DDS paths exist, and no military-raid icon is changed or referenced. |

These are source-level acceptance scenarios, not a live game simulation or a substitute for the parent’s final gameplay review.

## Commit verdict

The bounded tranche is not ready to commit as compliant with the binding audit constraints.

It requires remediation of the forbidden doctrine refund and the non-Chinese controller target hole before commit.

The `ai_hint_pp_cost` constant form also needs installed-engine parser confirmation before the AI reservation behavior can be considered proven.

The category DDS is present in the final audit snapshot but remains untracked, so it must be included in any future tranche commit.

No Stage 7 or overall CBRN completion claim is made by this audit.

## Recommended follow-up files and identifiers

1. `common\script_constants\japan_biological_campaign_constants.txt`, `japan_bio_campaign_doctrine`: remove Command Power refund values.
2. `common\scripted_effects\japan_biological_campaign_effects.txt`, `japan_bio_campaign_prepare_doctrine_parameters` and `japan_bio_campaign_begin_release`: remove refund preparation and credit behavior.
3. `common\scripted_triggers\japan_biological_campaign_triggers.txt`, `japan_bio_campaign_state_relationship_is_valid`: require that the exact state controller is an accepted Chinese belligerent.
4. `localisation\english\japan_biological_campaign_l_english.yml` and `docs\biological_warfare\japan_china_biological_campaign.md`: align cost and doctrine wording once the behavior is fixed.
5. `docs\specs\chaos_warfare_system_specs\specs\06_biological_warfare_and_outbreaks.md`: reconcile the refund allowance with the binding doctrine rule in the accepted follow-up.
6. `common\decisions\japan_biological_campaign_decisions.txt`, `japan_bio_campaign_contaminate_supply_network` and `japan_bio_campaign_disperse_plague_vectors`: validate the two `ai_hint_pp_cost` fixed-value tokens against the installed parser.
