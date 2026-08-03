# Event 016 KRG country-package audit handoff

Date: 2026-08-03  
Scope: read-only audit of the fixed `KRG` package and its Event 019 provider surface.  
Result: the static package is broad and internally connected, but transfer/formation, live playability, Event 019 isolation/cleanup, biological stockpile delivery, and portrait-pipeline acceptance remain open. No gameplay file was changed.

## Evidence and method

- Required repository guidance and the country/event/focus/decision/asset skills were read before inspection.
- Offline wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, State modding, National focus modding, Division modding, Equipment modding, Technology modding, and Unit modding.
- Vanilla documentation consulted: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.
- Static checks run: focus id/localisation/icon comparison, KRG portrait DDS dimensions, KRG flag dimensions, KRG idea GFX/texture comparison, decision localisation coverage, provider callback/trigger inspection, and `.tools/audit_chaosx_country_tags.py`.
- `audit_chaosx_country_tags.py` reported 0 external country-definition or identity-surface collisions. The broader vanilla/workshop tag scan was started but timed out and is not evidence of global uniqueness.
- No HOI4 launch, live save, map write, or Technology Tree Viewer run was performed. The installed package exposes no Technology Tree Viewer, so projected technology-tree rendering remains unresolved.

## Country package coverage checklist

| Surface | Static result | Evidence |
| --- | --- | --- |
| Tag and definition | Covered | `common/country_tags/016_brilliant_scientist_country.txt:1-3` registers `KRG` once; `common/countries/Kruger State KRG.txt:1-4` defines western-European graphical culture and base colour. |
| Cosmetic identities | Covered | `common/countries/016_brilliant_scientist_cosmetics.txt` defines `KRG_SCIENTIFIC_REPUBLIC`, `KRG_REPLICATED_STATE`, `KRG_MACHINE_STATE`, `KRG_TEMPORAL_CONTINUUM`, `KRG_XENOBIOLOGICAL_ASCENDANCY`, and `KRG_PROJECT_SYNTHESIS`. |
| Dormant history | Intentional dormant state | `history/countries/KRG - Kruger State.txt:1-17` uses capital `1`, empty dormant OOB, zero slots/stability/war support, neutrality, and the fixed character roster. `history/units/016_brilliant_scientist_dormant.txt:1-3` is empty by design. |
| Character/leader roster | Covered statically | `common/characters/016_brilliant_scientist_characters.txt` defines `KRG_warren_kruger`, `KRG_continuity_network`, `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council`; route staff reset/recruitment lives in `common/scripted_effects/016_brilliant_scientist_effects.txt:2796-2841` and `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1221-1247`. |
| Politics and route tags | Covered statically | `common/scripted_effects/016_brilliant_scientist_country_effects.txt:586-614` applies formation government by origin; `:1036-1071` handles takeover; `:1100-1194` applies six route cosmetic tags, ideology, popularity, and route ideas. |
| Focus loading | Covered statically | `common/scripted_effects/016_brilliant_scientist_country_effects.txt:660-679` and `:1036-1071` set the active flag and load `brilliant_scientist_kruger_state_focus_tree` with `keep_completed = no`. |
| Decisions and missions | Covered statically | Eighteen KRG decision files under `common/decisions/` expose 144 `brilliant_scientist_krg_*` decision/mission keys; aggregate Event 016 localisation has no missing title/description keys in the static comparison. |
| Ideas | Covered statically | `common/ideas/016_brilliant_scientist_country_ideas.txt` and related Event 016 idea files define lifecycle, route, supply, command, and Event 019 host ideas; `interface/016_brilliant_scientist_idea_icons.gfx` has 34 picture registrations and all 34 referenced DDS files exist. |
| Focus assets/localisation | Covered statically | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` contains 100 unique KRG focuses, 100 `ai_will_do` blocks, and no missing focus title/description keys; `gfx/interface/goals/016_brilliant_scientist` contains 100 KRG DDS icons and `interface/016_brilliant_scientist_kruger_state_focus.gfx` has matching base/shine sprite names. |

## File-surface checklist

The fixed-tag package spans the expected country, history, OOB, characters, leader/scientist traits, country/focus/territory/project-force effects and triggers, 18 KRG decision files, five idea files, two project technology files, project equipment and sub-units, route AI plans, country/focus/idea GFX, English localisation, flags, portraits, and Event 019 provider adapters. The key runtime surfaces are:

- `common/country_tags/016_brilliant_scientist_country.txt`
- `common/countries/Kruger State KRG.txt`
- `common/countries/016_brilliant_scientist_cosmetics.txt`
- `history/countries/KRG - Kruger State.txt`
- `history/units/016_brilliant_scientist_dormant.txt`
- `common/characters/016_brilliant_scientist_characters.txt`
- `common/country_leader/016_brilliant_scientist_traits.txt`
- `common/scientist_traits/016_brilliant_scientist_traits.txt`
- `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`
- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt`
- `common/units/016_brilliant_scientist_project_forces.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `interface/016_brilliant_scientist.gfx`, `interface/016_brilliant_scientist_kruger_state_focus.gfx`, `interface/016_brilliant_scientist_idea_icons.gfx`, and `interface/016_brilliant_scientist_kruger_state_decisions.gfx`
- `localisation/english/016_brilliant_scientist_country_l_english.yml`, `016_brilliant_scientist_focus_l_english.yml`, `016_brilliant_scientist_kruger_state_decisions_l_english.yml`, and the other Event 016 localisation files

## Map and state setup

The dynamic formation transaction is the strongest part of the package. `common/scripted_effects/016_brilliant_scientist_territory_effects.txt:796-863` revalidates the frozen plan immediately before mutation, rejects stale host/route/snapshot/capital/contract state, and clears state marks and event targets on invalidation. `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt:34-61` requires the host to own/control candidates and requires actual logistics access; `:98-132` requires a viable facility capital and contiguous/strategic support; `:313-362` preserves host states, cores, factories, and route contracts. `common/scripted_effects/016_brilliant_scientist_country_effects.txt:716-732` gives charter states KRG cores and a host claim, cores only the frozen capital for enclave/rebellion, claims other seized states for KRG, and sets owner/controller to KRG. `:931-975` seeds the verified capital, executes `release = KRG`, transfers selected states, and resets the KRG capital to the verified state.

Static risk remains because no targeted charter, enclave, rebellion, takeover, stale-plan, third-party-occupation, state-loss, or annexation scenario was executed. The dormant history capital `1` is intentionally only a bootstrap value; live acceptance must prove that release succeeds after the verified capital is cored and that no orphaned capital or duplicate owner remains.

## Politics, leaders, portraits, flags, advisors, and parties

- `KRG_warren_kruger` is a single fixed fictional identity with stage-0 leader/advisor portraits and no random personal-name pool. His sovereign role is added exactly once by `brilliant_scientist_promote_kruger_as_sovereign` (`common/scripted_effects/016_brilliant_scientist_country_effects.txt:15-40`), while the research director and polymath traits live in `common/country_leader/016_brilliant_scientist_traits.txt` and `common/scientist_traits/016_brilliant_scientist_traits.txt`.
- The four command offices use institutional names and route-gated advisor/commander/leader roles. They currently reuse vanilla generic male portrait GFX; this is statically valid and avoids opposite-gender pool use, but the institutional visual identity is intentionally generic.
- Static country localisation covers `KRG`, `KRG_ADJ`, all six cosmetic names, Kruger, the continuity network, and all four offices. Route politics and popularity are set in the country effects cited above; no separate party-definition file is required by the current route design.
- `gfx/flags/KRG.tga` and six route flags exist at 82x52, 32-bit TGA: `KRG_SCIENTIFIC_REPUBLIC.tga`, `KRG_REPLICATED_STATE.tga`, `KRG_MACHINE_STATE.tga`, `KRG_TEMPORAL_CONTINUUM.tga`, `KRG_XENOBIOLOGICAL_ASCENDANCY.tga`, and `KRG_PROJECT_SYNTHESIS.tga`.
- Runtime leader DDS files under `gfx/leaders/KRG/` are present at 156x210 for stage 0, stages 1-2, and the six stage-3/stage-4 route variants. Portrait provider compliance is not fully evidenced: the durable package is under `docs/assets/016_brilliant_scientist/source_png/portraits`, not the mandated `docs/assets/portraits/<event>_<slug>/` archive, and the recorded masters are approximately 1,000x1,400 rather than exact 832x1120. The runtime art is present, but pinned-provider commit/job-manifest, exact-master, identity/framing, and DDS acceptance should be re-audited before calling the portrait package final.

## Focus, decisions, ideas, and assets

The focus tree is 100 nodes with 100 AI blocks, all 100 localisation pairs, 100 KRG goal DDS files, and matching normal/shine GFX names. It contains distinct governance, conventional security, clone, machine, paleogenetic, xenobiological, portal, temporal, support, diplomacy, and terminal routes, with mutually exclusive Laboratory World/Singularity capstones. Focus effects call route/lifecycle helpers in `common/scripted_effects/016_brilliant_scientist_focus_effects.txt` and the country effects file. The static package has no missing icon or focus text found by the comparison.

The decision surface is large and route-specific, with target-state gates, costs, AI weights, one-use cleanup, missions, and terminal actions distributed across the 18 KRG decision files. Static localisation coverage is complete for the 144 KRG decision/mission blocks inspected. Quantitative cost/weight balance, AI choice distributions, and cleanup after state loss remain validation-pending.

The KRG idea surface is wired to 34 Event 016 DDS icons and includes the current 28 visible lifecycle/project ideas documented by the source-of-truth handoff. The biological-supply focus/idea path is visible, but the stockpile/reservation/consumption/expiry/defeat callback remains blocked by the native CBRN dependency; no fallback or free payload is present.

## Starting military, technology, industry, supply, and production

- Dormant KRG begins with an empty OOB and zero research slots by design. Formation initialisation (`common/scripted_effects/016_brilliant_scientist_country_effects.txt:660-679`) restores configured research slots, political power, limited former-host conventional technology, starting ideas, the conventional guard package, carried project history, and the KRG focus tree.
- `brilliant_scientist_apply_conventional_guard_package` (`common/scripted_effects/016_brilliant_scientist_country_effects.txt:417-583`) builds a six-infantry Laboratory Guard template and derives guarded divisions, manpower, infantry/support/motorised equipment, fuel, experience, and equipment/manpower factors from route and host history. Takeover deliberately receives no free conventional grant.
- Seven project sub-units are defined in `common/units/016_brilliant_scientist_project_forces.txt`: `kruger_portal_raider`, `kruger_clone_infantry`, `kruger_robot_frame`, `kruger_paleogenetic_beast`, `kruger_xenobiological_assault`, `kruger_exotic_guard`, and `kruger_temporal_guard`. Project equipment and the two project technology files define matching equipment/technology IDs; project technologies are history/focus unlocked (`allow = { always = no }`) rather than generic researchables.
- Production and supply are intentionally constrained by the starting ideas and route decisions. Static source wiring is present; affordability, stockpile quantities, template materialisation, fuel/supply survival, and route-specific balance need live or scripted scenario evidence.

## AI and playability

`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` contains 19 KRG plans covering charter, rebellion, enclave, takeover, each project family, biological containment/last resort, commonwealth/submission, and the two terminals. Each plan has an `allowed = { NOT = { original_tag = DJX } }` loader-safe gate and a continuously evaluated KRG sovereign/focus/route `enable` and `abort` gate. `DJX` is a real Event 006 dormant tag (`common/country_tags/006_independence_wave_countries.txt:50`), so this is not an unresolved tag token; the broad allowed gate is intentional to let a transformed host reach takeover plans. The older handoff claiming `original_tag = KRG` is stale and should not override the current file.

Static AI plan references resolve to the 100 KRG focus IDs and route triggers. The AI survival design prefers stabilisation, supply, facility defence, and portfolio-specific routes. No weighted simulation or live AI campaign was run, so route choice, plan queue transitions, takeover consolidation, and terminal disarmament/arming behavior remain unproven.

## Event 019 provider integration

The Event 019 bridge is statically coherent. `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:531-537` registers providers after the history-derived Event 016 runtime package is current. `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:15-172` registers generic providers 504-510 for clone, robot, paleogenetic, xenobiological, alien-interface, portal, and temporal families with family-only lot policy, derivative/sustainment/containment/AI/visual/cleanup/parent-isolation profiles, spawn weights, and registry contract version. `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt:9-112` requires current Event 016 package flags and family-specific prototype/deployment history or an isolated derivative receipt. Provider rows expose template/build, spawn, management, sustainment, derivative, and cleanup callbacks, and use the existing KRG sub-units without Event 016-native spawn calls.

Event 019 provider creation, management, derivative parent isolation, defeat cleanup, and final cleanup were not executed. The current source-of-truth handoff explicitly marks these scenarios pending; treat cross-event playability as unresolved until Anomalous Rising, management, defeat, and final-cleanup scenarios show no Event 016 state leakage.

## Missing or stale surfaces and remaining risks

1. **Targeted formation acceptance (open):** run charter, enclave, rebellion, and takeover scenarios through capital selection, `release = KRG`, state transfer, capital reset, focus load, party/leader setup, conventional guard/project force materialisation, and former-host cleanup. Relevant files: `common/scripted_effects/016_brilliant_scientist_country_effects.txt:931-1081`, `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`, and `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt`.
2. **State-loss/annexation cleanup (open):** prove that project flags, state facility targets, event targets, character nationality, ideas, providers, and host recovery paths clear or persist exactly when KRG loses facilities or is annexed. Static cleanup hooks exist, but no scenario evidence was available.
3. **Biological stockpile (blocked):** `KRG_biological_supply_network` and the biological project-force history bridge are present, but native CBRN reservation/outcome/cancellation/expiry callbacks are absent. Do not add a parallel ledger or free payload without an accepted callback contract.
4. **Event 019 isolation (open):** providers 504-510 are source-wired, but derivative and defeat/final cleanup acceptance is still pending.
5. **Portrait provenance (open):** runtime DDS and source PNGs exist, but the current source archive/master dimensions and provider records do not match the mandated durable `832x1120`/`156x210` portrait job evidence standard.
6. **Global tag uniqueness (open):** the Chaos Redux collision audit found 0 collisions; the broader vanilla/workshop scan timed out, so installed-mod uniqueness remains unverified.
7. **Technology projection (open):** no Technology Tree Viewer is installed, so complete placement/prerequisite/unlock rendering could not be verified. Static technology IDs and effects were inspected only.
8. **Quantitative balance and AI (open):** no live campaign, weighted simulation, affordability sweep, or route terminal scenario was run.

## Changed files and validation

Only this handoff was added: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_country_audit_final_2026-08-03.md`. No gameplay, asset, localisation, or spreadsheet file was edited. Meaningful static checks and their limits are recorded above. No fallback or simplification was introduced by this audit.
