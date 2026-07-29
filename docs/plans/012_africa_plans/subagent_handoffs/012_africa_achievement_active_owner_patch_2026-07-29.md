# Event 012 Africa achievement active-owner patch

## Scope and ownership

This handoff records the bounded owner-callsite patch for audit rows 19-24, 32-33, and 38 from `012_africa_achievement_callsite_audit_2026-07-29.md`.

The patch only connects existing Event 012 priority-member outcomes to the achievement ledgers, adds narrow host refresh and cleanup logic, and adds reviewed readiness gates where the accepted owner is still absent.

No country tags, models, model consumers, world-package gates, recurring all-country on_actions, fallback proofs, or unrelated dirty-worktree files were changed.

No commit was created because the parent task explicitly owns the commit boundary.

## Helper map

| Helper or trigger | Scope and inputs | Outputs and side effects | Exact callsite |
|---|---|---|---|
| `africa_achievement_record_priority_member_identity` | Priority-member country scope after the package mechanic reaches its existing maximum; reads the package predicate and its already-set mechanic proof flag for Luba, Lunda, Nubia, Aksum, Harar, or Great Zimbabwe. | Sets the matching restoration enum temporary and calls `africa_achievement_record_restoration_identity`, which appends the host ledger identity, increments the existing regional counter, and marks an identity-specific country flag. | Completion branch of `africa_priority_member_advance_mechanic` in `common/scripted_effects/012_africa_priority_member_effects.txt`. |
| `africa_achievement_record_horn_corridor_operational` | Host country scope; loops only `africa_relationship_countries` and requires live current-generation Aksum and Harar packages, settled politics, and their exact mechanic proof flags. | Sets `africa_achievement_horn_corridors_operational` only when both owners are present, then refreshes the host duration windows. | End of every priority-member mechanic payload through the host event target. |
| Kilwa convoy-access writer | Host event-target scope; runs only after the Kilwa mechanic reaches its existing maximum and `africa_priority_kilwa_common_customs_arbitrated` is set. | Sets `africa_achievement_maritime_convoy_access_active` and refreshes survival windows, allowing the existing maritime deadline to start when the count thresholds are met. | Kilwa completion branch of `africa_priority_member_advance_mechanic`. |
| Medium-confidence region ledger | Host scope through `africa_achievement_record_region_proof`; reads the existing development-project proof and current member confidence. | Adds each qualifying region once to `global.africa_achievement_medium_confidence_regions`, sets `africa_achievement_all_regions_medium_confidence` at the existing nine-region threshold, and clears the array when confidence collapses. | Existing development-project action proof and `africa_achievement_record_region_confidence_collapse`. |
| Rival-bloc count refresh | Host scope through `africa_achievement_refresh_live_duration_counts`; reads the existing `africa_rival_bloc_countries` array. | Snapshots `global.africa_achievement_rival_bloc_member_count` for the four-member refusal achievement. | Existing host duration refresh, additionally called after refusal and rival-bloc victory. |
| Identity-specific capitulation/annexation cleanup | Affected country scope; reads the identity flags written by the restoration helper. | Sets the row-specific global disqualifier for savanna, Nile, Horn, and plateau identities on capitulation or coercive annexation. | `africa_achievement_record_member_capitulation` and the existing definition-only `africa_achievement_record_coercive_annexation`. |

## Constants and tuning

No constants were added or changed. The patch reuses the existing Event 012 enums and thresholds in `common/script_constants/012_africa_achievement_constants.txt`, including the three savanna courts, three Nile identities, six maritime polities, five maritime ports, nine continental regions, four rival-bloc members, and the existing duration bands.

## Event targets, variables, flags, and cleanup

The patch uses the existing short-lived `africa_host` event target and the existing host-owned relationship array. It adds no global event target and therefore requires no new global-target cleanup.

The new `global.africa_achievement_medium_confidence_regions` array is initialized with the other achievement arrays and cleared by the confidence-collapse disqualifier. The new rival-bloc count is initialized with the other host ledgers and refreshed from the live rival-bloc array.

Identity flags are lifetime evidence on the package country and are consumed only by the existing affected-country capitulation or annexation cleanup helpers. No recurring on-action or world iteration was introduced.

## Row dispositions

| Row | Positive owner proof connected | Disqualifier or cleanup connected | Reviewed readiness gate and remaining owner |
|---:|---|---|---|
| 19 `africa_kings_of_the_savanna` | Luba and Lunda mechanic settlements now record their existing restoration identities. | Luba/Lunda/Kuba identity flags now map capitulation to `africa_achievement_savanna_court_destroyed` and coercive annexation to `africa_achievement_savanna_court_annexed`. | `africa_achievement_savanna_owner_ready` remains intentionally unset. Kuba has no Event 012 priority package, and the three-court overlap plus same-order final settlement writers are still missing. |
| 20 `africa_nile_has_many_memories` | Nubia mechanic settlement now records the existing Nubia restoration identity. | Kush/Nubia/Makuria/Alodia identity flags map affected-country capitulation to `africa_achievement_nile_identity_erased`; coercive annexation uses the same Nile erasure flag. | `africa_achievement_nile_owner_ready` remains intentionally unset. Kush, Makuria, and Alodia owners, Nile overlap and corridor final-result writers, and corridor-failure/capital-dispute owners are missing. |
| 21 `africa_ports_of_the_monsoon` | Kilwa customs arbitration now sets `africa_achievement_maritime_convoy_access_active` and refreshes the existing maritime clock. | No new positive inference was made. | `africa_achievement_monsoon_owner_ready` remains intentionally unset because exact two-port-loss and inland-military-shortcut outcomes have no current owners. |
| 22 `africa_walls_courts_and_caravans` | Aksum and Harar mechanic settlements now record their existing identities; the host joins their exact settled mechanic flags into `africa_achievement_horn_corridors_operational`. | Aksum/Harar identity flags map affected-country capitulation to `africa_achievement_horn_package_war`; coercive annexation uses the same Horn-war disqualifier. | `africa_achievement_horn_owner_ready` remains intentionally unset because package war, abolition, and corridor-loss final outcomes have no current writers. |
| 23 `africa_the_old_gold_roads` | Great Zimbabwe mechanic settlement now records its existing restoration identity. | Great Zimbabwe/Mutapa/Rozwi identity flags map affected-country capitulation to `africa_achievement_plateau_polity_annexed`; coercive annexation uses the same plateau-annexation disqualifier. | `africa_achievement_gold_roads_owner_ready` remains intentionally unset. Mutapa and Rozwi owners, the real local-ownership writer, foreign-majority cleanup, and plateau-corridor failure owners are missing. |
| 24 `africa_member_who_said_no` | Existing refusal and rival-victory flags remain the exact owner outcomes; the host now refreshes the existing rival-bloc member count after refusal and rival victory. | No unowned alternative or terminal outcome was invented. | `africa_achievement_member_refusal_owner_ready` remains intentionally unset because the recognised-alternative milestone and colonial-puppet, League-destruction, and terminal-high-chaos owners are missing. |
| 32 `africa_development_without_overstretch` | Existing development-project proofs now build the nine-region medium-confidence ledger and set `africa_achievement_all_regions_medium_confidence` at the existing threshold. | Existing integration-burden and confidence-collapse cleanup remains active; confidence collapse now clears the new region ledger. | `africa_achievement_development_owner_ready` remains intentionally unset because the project-exploitation-scandal owner is missing. |
| 33 `africa_common_reserve_answers` | No reserve-war proof was invented; the existing `africa_achievement_record_reserve_war_answered` helper remains definition-only. | No reserve deadline, protected-capital, or offensive-abuse owner was invented. | `africa_achievement_common_reserve_owner_ready` remains intentionally unset until the six defensive-war deployment and all four cleanup outcomes have exact final callsites. |
| 38 `africa_rain_on_command` | No weather-army or weather-war proof was invented; the existing helpers remain definition-only. | No weather disaster, neutral-targeting, or ecological-wrath owner was invented. | `africa_achievement_rain_command_owner_ready` remains intentionally unset until weather defeat, weather-war victory, and all three disqualifier outcomes have exact final callsites. |

## Migration plan

Existing priority-member mechanic payloads remain the source of truth for package outcomes. Their existing completion branch now calls the achievement identity helper after the package reaches its mechanic maximum, so no duplicated package-specific achievement writes are required in events or decisions.

The generic restoration and milestone helpers remain available for future exact owner callsites. The nine reviewed gates intentionally prevent partial counters, flags, or duration ledgers from claiming an achievement before their named owner systems are implemented.

## Validation

The following narrow source checks were run:

- `rg` confirmed each new helper has a definition and the intended priority-member callsite.
- `rg` confirmed each reviewed readiness gate appears only in its corresponding achievement trigger and has no setter under `common/` or `events/`.
- `rg` confirmed rival-bloc count refresh uses the existing `africa_rival_bloc_countries^num` array and the existing host refresh paths.
- The touched-script diff was inspected for balanced block structure and for accidental edits outside the three Event 012 gameplay files plus this handoff.

HOI4 was not launched, and no in-game save or live consumer validation was performed because runtime validation belongs to the parent/user workflow.

## Limitations and follow-up

Rows 19-24, 32-33, and 38 remain intentionally blocked by their reviewed gates. The patch does not create missing countries, world/model packages, reserve systems, weather systems, or terminal outcomes, and it does not convert any simplified existing proof into a claim of exact completion.

The next owner pass should implement the missing package and final-result writers named in the row table, then set the corresponding readiness gate only after the positive proof, disqualifier, cleanup, localisation, and validation evidence are complete.
