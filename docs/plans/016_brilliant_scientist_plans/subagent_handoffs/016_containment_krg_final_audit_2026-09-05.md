# Event 016 Containment and KRG Final Audit Handoff

Date: 2026-09-05.

Scope: bounded containment, canonical Kruger continuity, KRG formation, territory safety, and project-family inheritance review.

Disposition: one local P2 containment idempotence patch is implemented; one P1 formation blocker is confirmed in the adjacent territory package and remains unresolved because that package is outside this subagent's ownership.

No files were staged or committed.

Existing concurrent staged, deleted, and untracked work was preserved.

## Files inspected

- `common/decisions/016_brilliant_scientist_containment_decisions.txt`.

- `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`.

- `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`.

- `common/script_constants/016_brilliant_scientist_containment_constants.txt`.

- `common/scripted_localisation/016_brilliant_scientist_containment_scripted_localisation.txt`.

- `common/characters/016_brilliant_scientist_characters.txt`.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`.

- `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`.

- `common/script_constants/016_brilliant_scientist_country_constants.txt`.

- `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt`.

- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`.

- `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`.

- `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` and `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt` as required formation dependencies only.

- `common/scripted_effects/016_brilliant_scientist_effects.txt` as the canonical transfer and role dependency only.

- `common/characters/016_brilliant_scientist_characters.txt`, country tag/history/cosmetic files, matching Event 016 localisation, and existing handoffs/specs.

## Implemented patch

Changed file: `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:18-64`.

Changed effect: `brilliant_scientist_select_containment_exile_recipient`.

Before the patch, every call to `brilliant_scientist_prepare_sovereignty_board` cleared `brilliant_scientist_containment_exile_recipient` and randomly selected a new recipient.

The unanswered-deadline resolver calls board preparation again, so a visible exile decision could silently change its recorded recipient before resolution.

After the patch, a recipient is preserved when the global target exists, the target country still passes `brilliant_scientist_is_valid_transfer_recipient`, and the current host is not at war with that target.

The selection pool is rebuilt only when the target is missing, invalid, or hostile, and terminal resolution still clears the global target through `brilliant_scientist_close_sovereignty_board`.

The temporary preservation marker is cleared at the end of the helper, so this guard does not become persistent state.

The target helper remains compatible with the existing transfer validation contract and the existing weighted recipient selection path.

The changed helper has one definition, lines 18-64 are balanced, and no unrelated hunk was introduced by this patch.

## Containment coverage checklist

- The decision package contains the eight response IDs `brilliant_scientist_release_kruger`, `brilliant_scientist_exile_kruger`, `brilliant_scientist_arrest_kruger`, `brilliant_scientist_shutdown_directorate`, `brilliant_scientist_ratify_sovereign_charter`, `brilliant_scientist_launch_military_seizure`, `brilliant_scientist_request_foreign_containment`, and `brilliant_scientist_concede_institutional_authority`.

- Each response has an available gate, a shared custom-cost gate where applicable, one payment path, one timed receipt, and a matching resolver path.

- Low-authority safe containment is source-gated by mandate below `brilliant_scientist_containment.low_authority_ceiling`, dependence below `low_dependence_ceiling`, Independent Capacity below `clean_independent_capacity_ceiling`, deployment count below `clean_deployment_ceiling`, zero weaponization, facility count below `clean_facility_ceiling`, and no sovereign science authority.

- The low-risk path permits release and the adjacent moderate-risk band permits exile when a valid persisted recipient exists; arrest and shutdown remain available through the open board path.

- High authority, dangerous projects, facility count, Independent Capacity, private guard, control loss, and incident history feed the recorded government and Kruger scores rather than an independent random reroll.

- Coercive resolution calls `brilliant_scientist_calculate_containment_scores` again from recorded variables and then routes to takeover, shutdown, confinement, rebellion, enclave uprising, foreign defection, or non-country crisis according to the existing causal thresholds.

- Peaceful charter, rebellion, enclave, and takeover routes all call the territory plan and revalidation helpers before formation mutation.

- The terminal helpers record a durable outcome, clear the action and deadline receipts, remove active Kruger roles, reconcile the former host, clear transfer relationships, and convert live facilities to former-site markers as appropriate.

- The close and record helpers are guarded by existing outcome and transaction receipts, so repeated terminal calls do not duplicate rewards, transfers, or cleanup.

## Canonical Kruger continuity

- `common/characters/016_brilliant_scientist_characters.txt:11-25` contains the only character definition for `KRG_warren_kruger`.

- The same `KRG_warren_kruger` identity is used by the advisor/scientist path, actor and event-target transfer paths, sovereign leader promotion, death and confinement flags, project history, and KRG formation.

- `common/scripted_effects/016_brilliant_scientist_effects.txt` keeps `transfer_kruger_atomically`, `add_kruger_roles`, and `remove_kruger_roles` on the same character ID.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:15-40` promotes the same character as the sovereign leader and does not generate a second Kruger identity.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1014-1044` reassigns the canonical character and institutional office tokens to KRG during verified formation.

- No confirmed character, advisor, scientist, actor, log actor, transfer, mission, leader, or death identity defect was found, so `common/characters/016_brilliant_scientist_characters.txt` was not changed.

## KRG country and territory coverage

- `common/country_tags/016_brilliant_scientist_country.txt:8` registers `KRG` to `countries/Kruger State KRG.txt`.

- `history/countries/KRG - Kruger State.txt` is a dormant bootstrap with capital state 1 and no live formation territory.

- `common/countries/Kruger State KRG.txt`, KRG cosmetic definitions, country localisation, and the fixed Kruger character are present.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:954-1083` transfers only the verified selected plan states, binds the selected capital, snapshots the former-host portfolio, and initializes KRG from the canonical identity.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:739-755` adds KRG cores or claims and changes owner/controller only inside the selected-state transfer effect.

- The transfer path preserves charter cores and former-host claims according to the existing route contract and does not take third-party occupied states.

## Confirmed P1 blocker outside ownership

File: `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt:36-45`.

`brilliant_scientist_territory_state_is_host_candidate` requires `is_capital = no`.

File: `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt:98-102`.

`brilliant_scientist_territory_state_is_viable_capital` delegates to that host-candidate trigger and therefore also requires `is_capital = no`.

File: `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` in `brilliant_scientist_try_add_formation_territory_capital`.

The capital selector invokes `brilliant_scientist_territory_state_is_viable_capital`, so the current host capital cannot pass the candidate trigger and no other state can be the country's capital.

This makes charter, enclave, and rebellion territory planning fail closed before owner/core mutation, even though the revalidation and ownership guards themselves are correctly fail-closed.

The territory trigger/effect files belong to the adjacent territory/unit audit surface and were not edited here.

Parent follow-up must separate the non-capital support-candidate predicate from the viable-capital predicate or otherwise permit the intended current host capital while preserving the rule that a non-capital support state cannot replace the capital.

Do not claim KRG formation routes are playable until this P1 is corrected and rerun through the territory MCP route.

## Military inheritance separation

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:417-581` applies the conventional Laboratory Guard package once under `brilliant_scientist_conventional_guard_package_applied` and calculates its bounded opening force from host history, guards, facilities, network, factories, population, and war state.

- The conventional guard path is separate from takeover's retained army and does not use project-family materialization receipts.

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:697-698` calls the conventional package and the project-force package as separate effects.

- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:848-902` applies project-family history once through its own transaction and package receipt.

- The project-force family helpers use separate `teleportation`, `cloning`, `robotics`, `paleogenetics`, `xenobiological`, and `temporal` materialization receipts and family-specific templates or equipment.

- The project-force package does not rerun the conventional guard calculation, and the conventional guard package does not manufacture project-family units.

- No confirmed duplicate equipment, template, starting-force, or reward defect was found in the bounded review, so the project-force files were not patched across the unit-audit boundary.

## Localisation, decisions, and assets

- `localisation/english/016_brilliant_scientist_containment_l_english.yml` covers the containment decisions and timed response text.

- `localisation/english/016_brilliant_scientist_l_english.yml` covers the Event 016 event names and Kruger-facing text used by the reviewed routes.

- `localisation/english/016_brilliant_scientist_country_l_english.yml` covers KRG, cosmetic country names, adjectives, and party/country presentation keys found in the package.

- No missing localisation key tied to the reviewed containment/KRG identifiers was confirmed.

- Focus tree, GUI, portraits, and final visual asset production were outside this handoff and were not changed.

## MCP evidence

All MCP calls were read-only.

### Event inspection and rendering

- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

- Post-patch `hoi4.event_inspect` trace for `chaosx.nr16.31` returned `EVENT_INSPECTED_PARTIAL`, revision `fa39cc8b8775d170afcffd913b819e19d58668724ce547e0ec5a30ae5e8610a1`, graph hash `3f50c1f524100609b34403d4c61e9e9411f91a72356e9b2f987184d30d893fe1`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf584bd78c8e707f633ad0615454a1d9dfd8bdb2d8ac7380f8127d036a1feb31/3d054ae78dbdd60138c46273785eb373fd7f05cf14c344419df41a996b87a1a4/event-trace-fa39cc8b8775.json`.

- The trace had zero blocking diagnostics but was focused and partial because the large workspace deferred helper and lifecycle projections; the inline source inventory was limited to 64 of 369 paths.

- `hoi4.event_render` option views for `.30`, `.31`, and `.32` completed as partial read-only renders; the `.31` option manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37df0fbab2e8cac0f9da21bfb743cd161331ebf1e13f43e06a55591f409a51b2/ee6d2499db21d133305af533a41057ebc0f4258e78aee41981c77d22e782a4e1/event-options-fa39cc8b8775-manifest.json`.

- The `hoi4.event_compare` attempt using the available trace artifact timed out after 180 seconds; the installed service guidance says report/render envelopes are not graph-bearing compare inputs, so no comparison result is claimed.

### Map inspection and rendering

- `hoi4.map_inspect` for state 1 returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/902fea16470505e68a4a3c084c92082f0acc5600d0fcb776cd1614f238f7ee35/fa7285ff44bb943549f3dba9aa8f4df2ca591cdd41c6ce4e238c8a75d75472fb/map-inspect.2da749d9c53e8084.json`.

- A `hoi4.map_inspect` query for `KRG` returned zero static query matches in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d518d0f4df9042496aaefa038c81d88c5ec33803c5a7197d7e8c3cc9a736c6fb/be6211c1e42e2226340a0821b53ae410542087e0ced3b2017a3809387b6b718d/map-inspect.2da749d9c53e8084.json`.

- `hoi4.map_render` of the state layer with coastlines, ports, state buildings, supply nodes, and railways returned a read-only validated render at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41f03b07c45491bb51246c8b4abac0c265ddb0fd30dd96739bc0b548952b80c3/113c3b0164474ca8b56e48a7b03f0092efdb718e4d7ca7fc1aaedddfea23f661/map-state.png`.

- The map service reported unrelated global locator diagnostics and truncated them; no map write was attempted.

### Probability and decision evidence

- There is no exposed decision-specific MCP inspector in the installed package.

- `hoi4.probability_inspect` on `common/decisions/016_brilliant_scientist_containment_decisions.txt` returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/528796f71a8b59b893fdc3cd55f85d688ac614acfb14cc3109480e3b7341e6be/6ea989ec73cb24bf000c155ae43de01cdfa0a2a96e99b09fde3c3bfdbc161173/probability-inspect-9af82543f8c9.json`.

- The requested `decision_ai_will_do` adapter had no direct candidates, while the service suggested `mission_ai_will_do` with all eight containment decision identifiers.

- Direct `hoi4.probability_evaluate` through the suggested adapter used `E016_CONTAINMENT_COST_CLOSURE_2026_09_02.scenarios.json`, 17 scenarios, all eight candidates, and 136 candidate rows.

- The evaluate artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65ffcee591bef754818a16408645b89cfb8606f6bdbe1dc934d8d2e51c289232/429271e7185d393cad34916b635781f4487b816fdf9d3162213c0ac5f03b665c/probability-0558a792bb13c642fa234e30.json`.

- The probability pass reported 36 unresolved bounded cases and one informational diagnostic that the concession strong-factor modifier was not activated by any supplied scenario; this is a fixture coverage gap, not a confirmed code defect.

- The named `chaosx_ai_probability_auditor` collaboration route was unavailable in this session, so the direct MCP result is recorded without claiming a named-auditor handoff.

- No weighted AI source changed in this patch, so no probability compare was required for the recipient idempotence fix.

## Required reading and engine references

- `AGENTS.md` was read to EOF.

- `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md` were read to EOF.

- The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, character modding, division modding, equipment modding, map modding, and scripted localisation were consulted.

- Vanilla documentation for effects, triggers, script concepts, event/state transfer, equipment, divisions, country setup, and script constants was consulted.

- A vanilla state-owner/controller transfer precedent was checked before accepting the KRG transfer source.

## Remaining risks, omissions, and blockers

- The viable-capital P1 described above blocks all planned dynamic KRG territory formations until the adjacent territory owner patches it.

- Event MCP evidence is focused and partial for the large workspace, and the compare call timed out.

- No decision-specific MCP inspector or installed standalone Technology Tree Viewer is available.

- Live Hearts of Iron IV execution was not performed because live validation belongs to the user.

- No character, portrait, focus, GUI, model, foreign, evolution, biological, Portal, Alien, DHR, achievement, super-event, catalog, or project-force patch was made.

- The facility counter conservatively counts Event 016 facility markers; no setter for `brilliant_scientist_facility_destroyed` was found, so no speculative change was made.

- Parent should route the territory P1 to the territory/unit audit, rerun map and formation validation after that fix, and keep this handoff as the source of the containment recipient patch and evidence limits.
