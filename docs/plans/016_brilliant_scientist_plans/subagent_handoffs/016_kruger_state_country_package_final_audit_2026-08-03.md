# Event 016 Kruger State country-package audit

Date: 2026-08-03

## Scope and disposition

This audit compares the current KRG package and finite host-settlement layer with `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_5_kruger_state_country_package.md`, `docs/specs/016_brilliant_scientist_specs/matrices/016_country_package_matrix.md`, the Event 016 source-of-truth map, and the accepted settlement handoffs.

Required repository guidance was read before inspection: `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets`, together with the required offline Paradox wiki pages and relevant vanilla documentation.

No gameplay, asset, localisation, map, or technology source was changed by this audit; the only output is this handoff.

## Country-package coverage checklist

| Surface | Status | Evidence and remaining confidence limit |
| --- | --- | --- |
| Tag and country definition | Pass | `KRG` is registered in `common/country_tags/016_brilliant_scientist_country.txt` and resolves to `common/countries/Kruger State KRG.txt`; the vanilla tag scan found `NO_VANILLA_KRG_TAG`. |
| Dormant history and OOB | Pass with bootstrap caveat | `history/countries/KRG - Kruger State.txt` carries dormant capital `1`, zero research slots, neutrality, fixed characters, and `history/units/016_brilliant_scientist_dormant.txt` is an empty `units={}` package; the formation transaction replaces the bootstrap identity before player-facing sovereignty. A live unformed-tag check remains pending. |
| Formation and territory | Static pass; scenario validation pending | Charter, rebellion, and enclave plans are selected from live facility and logistics markers in `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` and guarded by `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt`; takeover keeps the host carrier. The commit effect revalidates before mutation, transfers only frozen states, sets owner/controller, and preserves host floors. Transfer and cleanup scenarios remain open. |
| Leader and character identity | Pass | `KRG_warren_kruger` is the single fixed Doctor Warren Kruger token; `brilliant_scientist_promote_kruger_as_sovereign` retires the theorist role and adds one sovereign role. Machine succession retires Kruger and promotes institutional `KRG_continuity_network`. No random or opposite-gender leader naming path was found. |
| Advisors and commanders | Pass | `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council` use institutional names, route-gated advisor flags, and corps-command roles; they do not replace Kruger unless the machine succession explicitly promotes the continuity network. |
| Portraits and flags | Pass for active runtime package | KRG and cosmetic route flags exist under `gfx/flags/`; stage 0–4 leader/advisor DDS files are registered in `interface/016_brilliant_scientist.gfx` and resolve on disk. The asset manifest still contains historical stale/missing-source sections and should be reconciled separately. |
| Politics and parties | Pass statically | Formation sets neutral no-election bootstrap politics, then route effects select democratic/fascist/neutrality identities and cosmetic tags; KRG party and adjective keys are present in `localisation/english/016_brilliant_scientist_country_l_english.yml`. |
| Focus tree | Pass | `brilliant_scientist_kruger_state_focus_tree` contains exactly 100 manually-authored KRG focuses with route gates, icons, and localisation. The current read-only focus artifact reports `focusCount=100`, `diagnosticCount=0`, `crossingCount=0`, and 108 connectors. |
| Decisions, missions, and ideas | Static gameplay pass; visual gap | Ten KRG decision categories and the foundation, clone/machine, paleo/xeno, portal/temporal, safeguard, foreign, canonical/exotic, and terminal decision files are present. Four universal starting liabilities plus the conditional Scientific Exodus spirit for enclave/rebellion, and their lifecycle upgrades, are defined and guarded by KRG sovereignty. The country idea file defines 28 KRG ideas but only 7 have explicit `picture` assignments, leaving 21 visible lifecycle/project ideas on generic/default presentation until the bounded icon tranche is completed. Quantitative decision balance remains unvalidated. |
| Technologies and project forces | Static pass with biological blocker | Limited former-host technology inheritance and seven hidden grant-only force technology families are wired; seven custom sub-units/equipment families are history-gated and inactive by default. Biological stockpile/debit accounting is not implemented because the native CBRN callback is unavailable; this is an accepted requirement blocker with no fallback. |
| AI and playability | Static pass; balance pending | Nineteen KRG AI plans cover all four origins, route identities, project lanes, diplomacy, and terminal choices with explicit enable/abort gates. No new whole-world recurring pulse was found. AI survival, route weights, and opening force bands still need scenario and quantitative validation. |
| Finite host settlements | Static pass; probability and live transfer pending | `chaosx.nr16.5` exposes exactly ten country-gated choices for ENG/USA/SOV/JAP/GER/FRA/ITA/CHI/POL/CZE; receipt guards are mutually exclusive and `.7`/`.8` are receipt-driven host reactions. Existing transfer/formation code does not copy settlement receipt flags. |

## File surface checklist

- Registration and identity: `common/country_tags/016_brilliant_scientist_country.txt`, `common/countries/Kruger State KRG.txt`, `common/countries/016_brilliant_scientist_cosmetics.txt`, `history/countries/KRG - Kruger State.txt`, and `history/units/016_brilliant_scientist_dormant.txt`.
- Characters and traits: `common/characters/016_brilliant_scientist_characters.txt`, `common/country_leader/016_brilliant_scientist_traits.txt`, and the fixed IDs `KRG_warren_kruger`, `KRG_continuity_network`, `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council`.
- Formation and map safety: `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt`, and `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`.
- Focus and AI: `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`, `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, and `common/on_actions/016_brilliant_scientist_kruger_state_on_actions.txt`.
- Decisions and ideas: `common/decisions/categories/016_brilliant_scientist_kruger_state_categories.txt`, all `common/decisions/016_brilliant_scientist_kruger_state_*.txt`, `common/ideas/016_brilliant_scientist_country_ideas.txt`, and the related focus/project idea files.
- Technology and forces: `common/technologies/016_brilliant_scientist_project_technologies.txt`, `common/technologies/016_brilliant_scientist_project_force_technologies.txt`, `common/units/016_brilliant_scientist_project_forces.txt`, `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`, and `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`.
- Settlement and reactions: `events/016_brilliant_scientist_context_events.txt`, `events/016_brilliant_scientist_host_reaction_events.txt`, `common/scripted_effects/016_brilliant_scientist_context_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_context_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt`, and `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt`.
- Player-facing surfaces: `localisation/english/016_brilliant_scientist_country_l_english.yml`, `localisation/english/016_brilliant_scientist_focus_l_english.yml`, `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml`, `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`, `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt`, `interface/016_brilliant_scientist.gfx`, and `interface/016_brilliant_scientist_idea_icons.gfx`.

## Formation, map, and cleanup findings

`brilliant_scientist_prepare_formation_territory_plan` selects a viable capital in the documented priority order and expands only through connected facility/support states; `brilliant_scientist_revalidate_formation_territory_plan` clears verification before rescanning and never substitutes a changed state. The trigger contract requires live ownership/control, facility markers, logistics access, route bounds, and host preservation, with multi-site expansion requiring transport proof.

`brilliant_scientist_form_kruger_state_from_verified_plan` requires a verified plan, coherent project history, current host identity, no existing KRG/global lock, and no world-end state before it cores the verified capital, releases `KRG`, transfers the frozen capital and non-capital states, sets KRG capital, snapshots the portfolio, and reconciles the old host. `brilliant_scientist_transform_host_into_kruger_state` is takeover-only and performs no new-tag transfer.

`brilliant_scientist_transfer_selected_state_to_kruger_state` cores only the charter capital and narrow heartland cases, claims non-capital states, removes the former-host core where appropriate, and always sets owner and controller to KRG. No hardcoded Event 016 state list was found; the only numeric state is the documented dormant bootstrap capital `1`.

Old-host reconciliation clears pending context, reports, high-speed trial state, active project variables, temporary targets, and grant-only force outputs while rebuilding the independent ledger. World-end cleanup clears global facility, anchor, former-host, and temporary target pointers. The cleanup graph still needs targeted transfer, annexation, and interrupted-event scenario checks.

## Politics, leaders, portraits, flags, advisors, and parties

Kruger is a fixed male-presenting named character with no random-name pool, and the route office characters use institutional names rather than personal pools. Advisor portraits are generic male shelf portraits with matching male metadata; no female-presenting/opposite-gender pairing was found. The machine route uses the separate institutional continuity leader and marks Kruger removed from rule before succession.

The KRG country and route cosmetic names, adjectives, ideology names, parties, leader names/descriptions, advisor descriptions, and starting idea names/descriptions are present across the country and KRG decision localisation files. Active KRG and route flag triplets are present and the registered DDS/TGA paths resolve. Historical deleted source PNG records and mixed manifest status are documentation/asset-provenance cleanup risks, not missing active runtime files.

## Focus, decisions, ideas, and assets

The focus file has exactly 100 KRG IDs, including the four origin opening focuses, six sovereign identities, project lanes, diplomacy, expansion, and terminal choices. The current read-only artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be6affb97d0521b14b1b1cfc71a2084be0e8413df4782194842fb5ee3a687337/c3b586fe2b292e19a58dc58d9b5b58e6059430f0f18082f660595b56dbd08258/focus-inspect.7640030c8209fb88.json`; its KRG tree diagnostics are zero and the unrelated generic continuous-focus diagnostics do not belong to KRG.

The four universal starting spirits are `brilliant_scientist_improvised_laboratory_state`, `brilliant_scientist_inherited_project_portfolio`, `brilliant_scientist_fragmented_command`, and `brilliant_scientist_experimental_supply_chain`; `brilliant_scientist_scientific_exodus` is added only for enclave or rebellion formation to represent displaced researchers. Their lifecycle effects remove or transform liabilities through focus/decision routes instead of granting a second research-director bonus. KRG decision categories and the existing thirteen-icon idea sprite tranche are present, but 21 visible lifecycle/project ideas still lack bespoke `picture` and 64x64 art wiring. Full quantitative decision balance is still open.

## Starting military, technology, industry, supply, and production

`brilliant_scientist_apply_conventional_guard_package` creates the bounded `Laboratory Guard` template, scales division count from origin, host army/guard strength, security, facilities, factories, population, war state, and capped constants, and grants matching manpower/equipment/fuel. Takeover explicitly receives no free conventional manpower/equipment/units.

The country inherits only the bounded ordinary host technology list in `brilliant_scientist_inherit_limited_former_host_technology`; project families are unlocked by hidden grant-only bridge technologies and history-derived ledgers. The project dispatcher rebuilds templates and caps from history and only the guarded formation dispatcher creates opening project formations for portal, clone, robot, paleogenetic, xenobiological, exotic, and temporal families.

Biological history currently sets native delivery technologies/ideas and weaponization flags but deliberately creates no stockpile, debit, proxy, or fabricated biological force. The spec row is therefore incomplete until a supported native CBRN callback or equivalent approved implementation is available; no fallback should be added.

The current technology inspection returned `TECH_INSPECTED_PARTIAL` with direct evidence linked at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2a35156aca7bdbff197535c7c58fb26145845d9fe99629d071612c512408ecc/04c142c6ca1809e2bc190b797695537f4357940b22d17da37e785dd74316a46d/technology-scan-eda906319162.json`; helper projections were deferred for the large workspace, so this is not a complete KRG-only technology-tree proof.

## AI and playability findings

The 19 named plans are `KRG_charter_republic_plan`, `KRG_rebellion_directorate_plan`, `KRG_enclave_survival_plan`, `KRG_takeover_consolidation_plan`, `KRG_takeover_post_audit_plan`, `KRG_clone_sovereignty_plan`, `KRG_machine_ascendancy_plan`, `KRG_paleogenetic_plan`, `KRG_xenobiological_plan`, `KRG_project_synthesis_plan`, `KRG_portal_plan`, `KRG_temporal_plan`, `KRG_alien_arms_plan`, `KRG_biological_containment_plan`, `KRG_biological_last_resort_plan`, `KRG_commonwealth_plan`, `KRG_submission_plan`, `KRG_laboratory_world_plan`, and `KRG_singularity_plan`.

Origin plans require their formation flags and abort at the founding audit; project plans require operational history and abort after their capstone; commonwealth/submission plans are mutually exclusive; laboratory-world/singularity plans are mutually exclusive terminal choices. Static gates cover supply stabilization, inherited project use, facility defense, host prioritization, and disabled terminal routes. AI weights and opening force bands remain unproven without scenario probability/live play validation.

## Finite country-settlement findings

`chaosx.nr16.5` contains the generic `.a/.b/.c` assistant outcomes plus exactly these country-gated choices: `.5.d_eng` (ENG), `.5.e_usa` (USA), `.5.f_sov` (SOV), `.5.g_jap` (JAP), `.5.h_ger` (GER), `.5.i_fra` (FRA), `.5.j_ita` (ITA), `.5.k_chi` (CHI), `.5.l_pol` (POL), and `.5.m_cze` (CZE). Each option clears pending state, sets the common resolution receipt, calls one guarded settlement helper, and schedules the existing lecture follow-up.

The accepted additive settlement vectors are recorded in order `(Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, Grievance)`: ENG `(+5,-10,+15,+5,+20,-15)`, USA `(+10,+5,+10,+15,+5,-5)`, SOV `(+5,+20,-5,+15,-5,+20)`, JAP `(+15,+5,+5,+10,+5,+5)`, GER `(+10,+20,-10,+20,-15,+20)`, FRA `(+10,-10,+15,+5,+25,-20)`, ITA `(+20,+10,+15,+15,+5,-5)`, CHI `(+5,+25,-10,+20,-20,+15)`, POL `(+15,0,+10,+5,+15,0)`, and CZE `(+5,-15,+15,+15,+20,-15)`.

`brilliant_scientist_context_country_settlement_is_unresolved` guards all ten receipt flags, while `brilliant_scientist_clear_context_pending_state` clears only transient briefing/conflict/follow-up flags and intentionally preserves resolved settlement history. Formation and ordinary transfer surfaces contain no settlement-receipt copy logic. `.7` and `.8` host reaction events use the existing facility/custody receipt model and do not add a second choice surface.

Current read-only Event Chain Viewer lint for `.5`, `.7`, and `.8` returned `EVENT_INSPECTED_PARTIAL`, `status=ok`, and zero blocking diagnostics on revision `d4554138622a675f8893ef2eb6a2475018c90d98c1d33b88aaacf8e22fae440f`; the three current artifacts are linked as `event-lint-d4554138622a.json` under the workspace artifact paths. The report explicitly defers workspace-wide helper/lifecycle projections, so transfer/cleanup and probability behavior remain open. Existing settlement handoffs also record partial AI-chance analyses with unresolved scenario inputs; they are not balance certification.

## Validation and limitations

- Static tag collision check: no vanilla `KRG` definition was found, while the Chaos Redux registry contains the reserved `KRG` entry and country-file reference.
- Focus inspection: current KRG tree reports 100 focuses, zero KRG diagnostics, zero layout crossings, and 108 connectors.
- Event inspection: current `.5`, `.7`, and `.8` focused lints report zero blocking diagnostics but partial workspace analysis.
- Technology inspection: direct scan/explain calls return `TECH_INSPECTED_PARTIAL`; helper projections are deferred in the large workspace and no complete bounded KRG technology-tree acceptance artifact is available.
- Source scans covered transfer owner/controller/core/claim calls, cleanup targets, settlement receipt guards, hidden technology bridges, project-force spawn gates, leader/portrait/GFX paths, focus localisation, and KRG AI plan IDs.
- No Hearts of Iron IV process, save, GUI live session, or consumer acceptance run was launched.

## Missing, stale, and blocked surfaces

1. Biological stockpile/debit lifecycle remains a blocking accepted requirement because the native CBRN callback is unavailable; the current implementation intentionally stops at history-derived delivery flags/ideas and must not be represented as complete.
2. Targeted charter, rebellion, enclave, takeover, transfer, annexation, cleanup, and interrupted-event scenarios remain pending, as do quantitative conventional-guard, project-force, AI-route, and settlement-probability balance checks.
3. The installed inspection package provides partial technology analysis but no complete bounded KRG Technology Tree Viewer acceptance proof; retain the unresolved limitation rather than claiming a rendered technology-tree pass.
4. The 21 visible KRG lifecycle/project ideas without explicit `picture` assignments in `common/ideas/016_brilliant_scientist_country_ideas.txt` do not yet meet the accepted bespoke 64x64 idea-art criterion; this is a non-model visual gap, not a gameplay fallback.
5. `docs/assets/016_brilliant_scientist/manifest.md` contains mixed historical status sections and tracked legacy portrait-source deletions even though active DDS/TGA runtime paths resolve; documentation/asset-provenance reconciliation is still needed.

## Patch handoff

Changed gameplay files: none.

Changed tags, states, leaders, parties, focus IDs, localisation keys, and formable IDs: none.

Plan handoff: this file, `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_country_package_final_audit_2026-08-03.md`.

Parent review should carry the four blockers/limits above into the final Event 016 completion report and schedule targeted validation rather than adding a new KRG identity or fallback CBRN implementation.
