# Biological sabotage native target scope repair

Disposition: implemented and reviewed source repair; native warning disappearance is not claimed.
Acceptance basis: the user's live QA on 2026-10-03 reports repeated Country-only trigger errors at biological_sabotage_triggers.txt lines 69, 70, 74 and 78 and explicitly requests caller tracing, repair and a scoped commit.
The broader CBRN goal remains incomplete.

## Cause and repair

The relationship helper was embedded in bio_sabotage_common_target_state, which all four pathogen profiles use.
Twelve loaded native sabotage raid definitions call those profiles in target_type.state as well as through country show/available/launch gates and AI selection.
Native state enumeration is the confirmed state-ROOT caller; no current decision, mapmode or scripted-GUI call to this helper was found.
The helper entered ROOT from the target controller and executed faction, subject and war checks, so native enumeration attempted Country commands in STATE scope.

The common and four agent profiles now contain physical STATE eligibility only.
The explicit COUNTRY helper bio_sabotage_actor_relationship_with_from_is_valid uses native actor ROOT and victim FROM, preserving existence, non-self, no-faction, both subject directions, wartime strategic authorization and peacetime unrestricted authorization.
It derives the exact bilateral retaliation target ID from FROM; it does not infer an actor from the selected state's owner or controller.
Country bio_sabotage_raid_target_from_is_valid invokes this gate before checking the selected state's controller against FROM and its physical profile.
All twelve show/available/launch paths already call that country gate directly or through their preparation/launch helper.
bio_sabotage_ai_may_target_state runs inside the raid's own var:target_state block, so it calls bio_sabotage_actor_relationship_with_from_is_valid on native actor ROOT directly instead of the state-reading wrapper.
Agent decision, recorded in agent_decisions_2026-10-04.md: the installed raid documentation guarantees FROM and var:target_state only inside the raid's own ai_will_do, show_target, available, launchable and launchable_from blocks, so re-reading var:target_state from a nested country scope relies on a guarantee the documentation does not give.
The selected state's own physical profile is already checked in the same predicate and the engine enumerates only the victim's states for the AI, so the direct call loses no restriction.
Native outcome dispatch retains the explicit actor/victim/state event-target checks in bio_sabotage_raid_native_context_is_valid.
No cost, preparation, success factor, doctrine, payload, effect, project, icon, public label or category changes.
Battlefield-only authorization still does not authorize strategic supply-chain sabotage.

## References and evidence

Installed common/raids/_documentation.md, lines 69-78 and 95-135, documents actor AI/preflight with target country FROM and selected var:target_state, alongside the state target filter.
Its SHA-256 is eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e.
The offline Scopes wiki dual-scope table was read through reference_read at lines 253-267, revision 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49: ROOT depends on the containing block, while controller is a country scope from STATE.
The installed facility_strike precedent in common/raids/air_raids.txt lines 50-67 puts faction checks in show_target, war checks in launchable, and physical type filtering in target_type.
A narrow source_lookup of that raid returned no indexed definition; the exact local vanilla source was read instead.
The service reference context/search/read routes responded with both installed and offline sources; generated script-document coverage remains absent.

The probability specialist captured four immutable before files and inspected the native raid source before this repair.
The installed probability route reported no weighted surfaces/adapters/candidates for that native source; numerical native AI selection evidence cannot be substituted with a decision adapter.
Recorded route gap: discovery returned no weighted surface or candidate for the native raid source and the matching eleven-scenario comparison returned PROBABILITY_SURFACE_EMPTY, so no probability narrative exists for this repair and none is linked.
The returned-call summary and the unsupported-comparison result are retained in [probability_mcp_evidence.json](../../testing/2026-10-04_bio_sabotage_scope_probability/probability_mcp_evidence.json) beside the immutable before sources and the declared [scenario matrix](../../testing/2026-10-04_bio_sabotage_scope_probability/scenario_matrix.json); those eleven fixtures are declared inputs, not executed native AI evidence.
The [scope source suite](../../testing/2026-10-04_bio_sabotage_scope_source_tests.js) executes parsed state/country contracts with modeled native scopes and explicit policy fixtures; 106 of 106 cases pass, with detailed limits recorded in the [test handoff](subagent_handoffs/2026-10-04_bio_sabotage_scope_source_tests.md).
Source evidence is separate from live engine warning absence.

The [CXT facility audit](subagent_handoffs/2026-10-04_cxt_facility_construction_gate_audit.md) is a separate requested diagnostic, preserving the user's 25 failed foreign-state attempts and source/DLC/technology distinctions.
No facility availability bypass or force construction is part of this scope repair.

No gameplay simplification is introduced.
Skills used: native raids, decisions/missions, subagent routing and shared-tree commits.

## CXT construction diagnostic

No explicit source DLC gate or enable_building research unlock was found for land_facility or biowarfare_facility.
CXT grants technologies before placing facilities, transfers each foreign candidate before checking ownership and native construction, and restores rejected candidates.
The indexed workspace has 688 technologies, below the documented 1,000-loop cap; this count does not measure the live runtime array.
The native shared facility group cap and one additional pilot building can reject a state, but that single pilot does not explain all 25 attempts.
The source bound starts at zero and stops after greater than 24, matching 25 attempts; the bound is unchanged.
The native rejection remains unresolved rather than being attributed to an absent DLC or research without evidence.
The temporary STATE helper chaosx_test_country_trace_facility_candidate reads actor/owner/controller identity, the Gotterdammerung flag, shared placement requirements and native can_construct_building for the current token after transfer.
It runs only under the existing setup-trace flag and changes no construction, transfer, retry bound, ownership, technology, or cost.
Remove its source file and single parent call once the rejection is identified; no periodic/worldwide hook or forced-construction fallback is added.

The CXT audit describes the current shared working-tree setup, including another owner's bounded-search additions.
This repair owns only the guarded diagnostic call in chaosx_test_country_effects.txt; those other setup/bound changes remain outside its isolated commit.
Public event, evolution and detail wording is unchanged, so this scope/debug repair warrants no event-catalog workbook edit or CSV export.
