# Event 012 Africa A1 achievement owner acceptance handoff

## Scope and status

This handoff records the bounded non-diaspora, non-RSA, non-world-order owner repair for the 44-row Event 012 achievement matrix.

The tranche adds exact Kuba and Savanna owner evaluation, live medium-confidence region proof, relationship-transition refreshes, operational infrastructure proof, and favourable-default removal.

No achievement completion claim is made; rows remain explicitly classified below until every matrix-specific positive owner, lifetime disqualifier, cleanup writer, and runtime scenario is present.

No commit was created because the parent agent owns the commit boundary.

## Files changed

- `common/scripted_effects/012_africa_achievement_effects.txt`
  - Requires operational state flags before counting rail, river, or port projects.
  - Seeds foreign-concession and local-ownership shares with `constant:africa_value.invalid` until a live owner writes a measured result.
  - Adds `africa_achievement_record_kuba_restoration_identity`.
  - Adds `africa_achievement_try_record_savanna_settlement`.
  - Adds `africa_achievement_refresh_medium_confidence_regions`.
  - Rebuilds medium-confidence proof from the current relationship ledger during live duration refreshes.
- `common/scripted_effects/012_africa_effects.txt`
  - After a real relationship transition is registered and reconciled, guarded Event 012 achievement refreshes run on the host.
  - The same guarded call retries exact Horn and Savanna settlement owners when a member becomes cooperative after its package or overlay result.
  - The pre-existing `africa_apply_constitutional_overlay_payoff` call from the focus tranche is preserved.
- `common/scripted_effects/012_africa_priority_member_effects.txt`
  - Kilwa convoy access now requires current host generation, no war with the host, and a cooperative relationship.
  - Priority-member completion retries exact Horn and Savanna owner evaluation through the host target.
- `common/scripted_effects/006_independence_wave_iw101_iw102_iw105_cog_overlays_effects.txt`
  - IW-102 Kuba charter completion calls the guarded Kuba identity owner and host Savanna retry.
- `common/scripted_triggers/012_africa_achievement_triggers.txt`
  - Row 19 now documents its runtime-backed owner gate.

The assigned constants file and achievement localisation file were inspected and left unchanged because the existing thresholds and 44 localisation triplets already match the accepted matrix.

## Helper map

| Helper or writer | Scope and inputs | Outputs and side effects | Exact callsites |
|---|---|---|---|
| `africa_achievement_record_full_action` operational proof | Action target after full semantics; reads each selected state’s operational rail, river, or port state flag. | Counts a project only once after the underlying action created the corresponding operational state flag; no selected-state proxy remains. | `africa_apply_current_action_outcome` in `common/scripted_effects/012_africa_action_effects.txt`. |
| `africa_achievement_record_kuba_restoration_identity` | COUNTRY scope on the IW-102 carrier; requires the active IW-102 Kuba route, both final charter flags, a host target, and current host generation. | Sets the Kuba overlap witness, records the Kuba restoration enum once, and refreshes host achievement windows through the shared restoration helper. | `independence_wave_iw102_kuba_choose_charter` in `common/scripted_effects/006_independence_wave_iw101_iw102_iw105_cog_overlays_effects.txt`. |
| `africa_achievement_try_record_savanna_settlement` | HOST scope; scans only `africa_relationship_countries` and requires live current-generation, alive, non-war, cooperative members carrying Luba, Lunda, or exact Kuba settlement flags. | When all three identities and the existing three-court count are present, records the Savanna overlap and common-order milestones and sets `africa_achievement_savanna_owner_ready`. | IW-102 Kuba charter completion, priority-member mechanic completion, and guarded relationship-transition refresh in `common/scripted_effects/012_africa_effects.txt`. |
| `africa_achievement_refresh_medium_confidence_regions` | HOST scope; scans only the host-owned relationship registry for alive current-generation cooperative members with an African overlay and confidence at least medium. | Rebuilds `global.africa_achievement_medium_confidence_regions`, sets the nine-region flag only at the existing threshold, and clears the flag when a live region falls out. | `africa_achievement_refresh_live_duration_counts`, which is reached by host survival refreshes and the guarded relationship-transition call. |
| `africa_achievement_record_horn_corridor_operational` | HOST scope; reads exact Aksum and Harar package settlement flags from current-generation cooperative members. | Sets the shared Horn corridor operational flag only when both named owners are present and refreshes survival windows. | Priority-member completion and guarded relationship-transition refresh. |
| Kilwa convoy-access writer | Priority-member COUNTRY scope after the Kilwa mechanic reaches maximum and `africa_priority_kilwa_common_customs_arbitrated` is set. | Sets maritime convoy access only for a current-generation cooperative, non-war member and refreshes the maritime window. | Kilwa branch of `africa_priority_member_advance_mechanic`. |
| Share-ratio sentinel | Normal-host achievement initialisation; no gameplay measurement is assumed. | Sets foreign-concession and local-ownership shares to `constant:africa_value.invalid`, preventing rows 23, 28, and 30 from passing on favourable defaults. | `africa_achievement_initialize_normal_host`. |

## Constants and tuning table plan

No constant was added or changed.

The tranche reuses the existing `africa_achievement_count` thresholds, `africa_achievement_ratio` thresholds, restoration enums, overlay enums, confidence measures, and `africa_value.invalid` sentinel.

The three-court threshold, nine-region threshold, and medium-confidence floor remain centralised in `common/script_constants/012_africa_achievement_constants.txt` and `common/script_constants/012_africa_constants.txt`.

## Event-target, flag, variable, and cleanup plan

The tranche uses the existing short-lived `africa_host` target and host-owned `africa_relationship_countries` registry.

No global event target, recurring all-country on-action, world scan, or new persistent pointer was introduced.

`africa_achievement_medium_confidence_regions` is initialised with the existing achievement arrays, rebuilt from live relationships, and cleared by the existing region-confidence-collapse helper.

The Savanna readiness flag is set only after the exact final owner evidence exists and is not cleared on later retries because the row’s sticky court-annexation and court-destruction disqualifiers prevent a later false completion.

Restoration identity country flags remain lifetime evidence and are consumed by the existing annexation and capitulation callbacks, which set the row-specific sticky disqualifiers for Savanna, Nile, Horn, and plateau identities.

No readiness setter was added for Nile, Monsoon, Horn, Gold Roads, refusal, Development, Common Reserve, or Rain on Command because at least one required positive or invalidating owner is still absent.

## Migration from duplicated or proxy proof

Action project counters now require the exact operational state flags emitted by the full action semantics, so selecting a state or reaching a generic action branch cannot create infrastructure evidence.

The live medium-confidence array is no longer left as an action-only accumulation; relationship transitions and host refreshes rebuild it from current-generation cooperative members.

The previous favourable initial values for foreign-concession and local-ownership shares are replaced with an invalid sentinel, so the resource and ownership thresholds remain unreachable until an owning system writes a measured value.

Package-specific identity and corridor writes remain in their owning package completion branches, while generic host refreshes retry them only after a real relationship transition.

## 44-row disposition

`Implemented / partial` means the positive owner or shared lifetime hook is present, but the row still has one or more matrix-specific owner gaps and is not completion-ready.

`Implemented / owner complete` means the named owner and existing loss hooks are wired for this tranche; no runtime campaign claim is implied.

`Blocked` means a required owner remains absent and its readiness gate intentionally stays unset.

`Model-gated` and `World-gated` are intentional package barriers and were not opened by this tranche.

| # | Achievement | Disposition | Exact owner or callsite evidence and remaining blocker |
|---:|---|---|---|
| 1 | `africa_guardians_without_borders` | Implemented / partial | Protection-war and live snapshot helpers are active; archive destruction and some partner-loss owners remain absent. |
| 2 | `africa_last_convoy_home` | Implemented / partial | Action start/full proof and convoy settlement hooks are active; abandonment and every final loss branch still need exact writers. |
| 3 | `africa_no_empty_promises` | Implemented / partial | Guarantee and coercive-annexation hooks are active; remaining constitutional failure owners are not all exposed. |
| 4 | `africa_the_interveners_left` | Implemented / partial | Scramble victory and expedition defeat evidence are active; partition-acceptance ownership remains absent. |
| 5 | `africa_archive_of_the_living_state` | Implemented / partial | Archive evacuation/restoration and annexation cleanup are active; destruction or suppression owners remain absent. |
| 6 | `africa_twelve_empty_chairs_filled` | Implemented / partial | Congress live-count and retention helpers are active; the authoritative full-agenda final-result writer still needs confirmation. |
| 7 | `africa_the_clause_is_the_country` | Implemented / partial | Clause and representation action proof is active; clause-cancellation ownership remains absent. |
| 8 | `africa_exit_without_war` | Implemented / partial | Peaceful reassociation clock is active; exit-war, coup, and coerced-return writers remain absent. |
| 9 | `africa_no_second_capital` | Implemented / partial | Rival monitoring and resolution proof are active; rival annexation and terminal coercion writers remain absent. |
| 10 | `africa_every_region_speaks` | Implemented / partial | Regional proof arrays and formation barriers are active; post-proof region-loss cleanup remains absent. |
| 11 | `africa_confidence_is_contagious` | Implemented / partial | Live high-confidence counts and transition refreshes are active; every confidence-loss route still needs its own sticky owner. |
| 12 | `africa_federation_by_consent` | Implemented / partial | Federal route and constitutional snapshots are active; military takeover and other forced-result owners remain absent. |
| 13 | `africa_republic_of_many_capitals` | Implemented / partial | Republic institution and succession evidence are active; suspension, centralisation, and military-transition owners remain absent. |
| 14 | `africa_crowns_at_one_table` | Implemented / partial | Crown recognition and restoration annexation cleanup are active; court deposition and abolition writers remain absent. |
| 15 | `africa_union_of_work_and_land` | Implemented / partial | Worker-region, food, and socialised-project proof is active; takeover, private-concession, and famine writers remain absent. |
| 16 | `africa_order_without_partition` | Implemented / partial | Military route, intervention victories, and emergency reduction are active; permanent emergency, genocide, and partition writers remain absent. |
| 17 | `africa_confederation_that_endured` | Implemented / partial | Live sovereign count, burden ceiling, and Scramble settlement are active; federal-annexation cleanup remains absent. |
| 18 | `africa_covenant_with_the_impossible` | Model-gated | Nonhuman actor registration and unit package are not runtime-ready; no gate was loosened. |
| 19 | `africa_kings_of_the_savanna` | Implemented / owner complete | Luba and Lunda package settlements, IW-102 Kuba charter/compact, current cooperative relationship checks, Savanna milestones, and existing annexation/capitulation loss hooks are connected; runtime campaign evidence is still pending. |
| 20 | `africa_nile_has_many_memories` | Blocked | Nubia package identity is connected, but Kush, Makuria, Alodia, Nile overlap/corridor owners, and capital-dispute cleanup are absent; `africa_achievement_nile_owner_ready` remains unset. |
| 21 | `africa_ports_of_the_monsoon` | Implemented / partial | Kilwa customs arbitration now writes guarded convoy access and existing port actions require operational flags; two-port-loss and inland-shortcut owners are absent, so readiness remains unset. |
| 22 | `africa_walls_courts_and_caravans` | Implemented / partial | Aksum and Harar identities plus the joint corridor writer are connected; package war, abolition, and corridor-loss writers are absent, so readiness remains unset. |
| 23 | `africa_the_old_gold_roads` | Implemented / partial | Great Zimbabwe identity and processing proof are connected and ownership now starts unknown instead of maximum; Mutapa, Rozwi, measured local ownership, and plateau-loss owners are absent, so readiness remains unset. |
| 24 | `africa_member_who_said_no` | Blocked | Existing refusal/rival flags and host rival-count refresh are active, but the recognised-alternative milestone and colonial-puppet, League-destruction, and terminal-chaos owners are absent. |
| 25 | `africa_return_without_compulsion` | Implemented / G1-owned and preserved | Diaspora consent/capacity/outcome hooks remain owned by `012_africa_diaspora_effects.txt`; no duplicate writer was added. |
| 26 | `africa_tools_books_and_ballots` | Implemented / G1-owned and preserved | Diaspora skill and representation hooks remain owned by the active G1 protocol; programme-denial writers remain a follow-up. |
| 27 | `africa_four_oceans_homeward` | Implemented / G1-owned and preserved | Exact origin-group ledger remains owned by G1; catastrophic-return and forced-relocation writers remain a follow-up. |
| 28 | `africa_capital_without_capture` | Implemented / partial | Diaspora project ownership remains G1-owned and the favourable local-ownership default is removed; a measured ownership writer and capture/corruption outcomes remain absent. |
| 29 | `africa_rails_rivers_roads_and_ports` | Implemented / partial | Four corridor systems use exact operational state flags and action failure records network split; connected-region-loss cleanup remains absent. |
| 30 | `africa_ore_leaves_as_machines` | Implemented / partial | Resource and processing counters are active and foreign-concession share now starts unknown; live concession measurement, raw-export crisis, and forced-seizure owners remain absent. |
| 31 | `africa_bread_before_banners` | Implemented / partial | Food proofs and pre-unification snapshot are active; preventable famine and civilian-wrath owners remain absent. |
| 32 | `africa_development_without_overstretch` | Implemented / partial | The nine-region medium-confidence flag is rebuilt from live relationship members and resets on confidence collapse; project-exploitation scandal ownership remains absent, so readiness remains unset. |
| 33 | `africa_common_reserve_answers` | Blocked | The reserve helper remains definition-only because no authoritative six-war deployment result or deadline/capital/offensive-abuse owners are exposed. |
| 34 | `africa_no_foreign_boot_remains` | Implemented / partial | Scramble settlement and external-puppet callback are active; African-core cession and unreversed-capitulation owners remain absent. |
| 35 | `africa_beasts_but_not_caricatures` | Model-gated | Strange formation package readiness remains unset and no fallback unit family was created. |
| 36 | `africa_elephants_crossed_the_desert` | Model-gated | Elephant formation, supply, and entity package owners remain deferred. |
| 37 | `africa_the_forest_kept_its_word` | Implemented / partial | Ecological bargain and accepted hostile-disaster writers are active; forest-rampage ownership remains absent. |
| 38 | `africa_rain_on_command` | Blocked | Weather-army defeat, weather-war victory, and the three weather invalidation owners remain definition-only; readiness stays unset. |
| 39 | `africa_disease_made_and_unmade` | Implemented / partial | Disease branch, outbreak, and containment counters are active; uncontrolled-release, irreversible-outcome, and terminal-disease owners remain absent. |
| 40 | `africa_stone_walks_into_parliament` | Model-gated | Stoneborn model, constitutional, war, erasure, and rights owners remain deferred. |
| 41 | `africa_another_continent_stood_up` | World-gated | External continent package readiness remains unset and no world-order files were changed. |
| 42 | `africa_two_continents_one_name` | World-gated | World package installation and compatible integration remain gated; no external focus or world-order writer was changed. |
| 43 | `africa_war_between_worlds` | World-gated | Continental-war owner exists behind world package readiness; debug-surrender and global-revolt cleanup remain future work. |
| 44 | `africa_the_world_is_one` | World-gated | Terminal identity and super-event readiness remain unset; no terminal fallback or world-order edit was introduced. |

## Static valid and invalid scenario matrix

The following scenarios were checked against source conditions and writer presence without launching HOI4.

| Family | Valid static path | Invalid static path | Result |
|---|---|---|---|
| Savanna restoration | Luba and Lunda package maxima plus recorded overlap dispositions, IW-102 Kuba charter and territorial compact, current-generation cooperative relationships, and three identities. | Any missing charter flag, capitulated member, host war, non-cooperative relationship, or missing identity prevents the owner flag. | Positive owner is wired and loss hooks remain sticky. |
| Nile restoration | Nubia package identity is present. | Kush, Makuria, or Alodia owner absent, or Nile overlap/corridor result absent. | Blocked with readiness unset. |
| Maritime | Kilwa mechanic maximum, customs arbitration, current host generation, cooperative relation, no war, and operational port action. | Missing customs result or host war leaves convoy access unset; two-port-loss and shortcut owners are absent. | Positive partial only. |
| Horn | Aksum and Harar exact package settlement flags, current-generation cooperative members, no host war. | Either package missing or relationship not cooperative leaves corridor flag unset. | Positive partial only. |
| Plateau | Great Zimbabwe package restoration and processing flags. | Unknown local-ownership share, missing Mutapa/Rozwi owner, annexation, or corridor loss blocks readiness. | Positive partial only; favourable default removed. |
| Refusal | Existing validated player origin, refusal, rival victory, rival count, independence, and recognised alternative. | Missing recognised-alternative milestone or any terminal/puppet condition blocks readiness. | Blocked pending final owner. |
| Development | Thirty exact operational/development projects, nine developed regions, nine live cooperative overlays at medium confidence, low burden, and no scandal. | One relationship leaves the cooperative set, confidence drops, or a scandal owner is missing. | Live medium-confidence proof is wired; scandal remains blocked. |
| Common reserve | No authoritative reserve-arrival result is exposed. | Any inferred war answer would be a proxy and is intentionally rejected. | Blocked with readiness unset. |
| Weather | No authoritative weather-army defeat or weather-war result is exposed. | Generic action success, weather value, or war presence cannot create the proof. | Blocked with readiness unset. |
| Diaspora rows 25–28 | G1 consent, capacity, origin, skill, project, and trust writers remain the source of truth. | No duplicate achievement writer was added from non-diaspora files. | Preserved for the active G1 owner. |
| Model rows 18, 35, 36, 40 | Model/package readiness remains absent. | No synthetic unit, tag, or fallback proof can pass. | Model-gated. |
| World rows 41–44 | World-package and terminal readiness remain absent. | No world scan, external focus edit, or terminal fallback can pass. | World-gated. |

## Validation evidence

- Source-level brace checks returned zero unmatched braces for all five touched script files.
- Unsupported comparison token checks returned zero `<=` or `>=` tokens in all five touched script files.
- Matrix count is 44 rows, completion-trigger count is 44, and the corrected matrix-to-trigger key comparison is empty.
- Registry audit found all 44 matrix keys in `common/achievements/chaos_redux_achievements.txt`.
- Readiness-writer census found exactly one setter for `africa_achievement_savanna_owner_ready` and no setters for the other eight reviewed readiness gates.
- The achievement localisation file retains its UTF-8 BOM and was not rewritten.
- Static helper census found definitions and intended calls for Kuba identity, Savanna retry, medium-confidence refresh, and Horn corridor evaluation.
- Read-only HOI4 MCP event scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3a3416f29876a6dc0da9ee79e212eb34cb6d06c37c9bc929c40f07734584e41/9a58468e13af673fc6243d4684c7708503d453a43e8eeaf7366b05df48d48e35/event-scan-e1943c8330f6.json`.
- MCP returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; workspace-wide helper projections were deferred and the linked artifact is the supported evidence reference.

HOI4 was not launched, and no live save, in-game scenario, or player-session validation was performed.

## Unsupported analysis, limitations, and follow-up

The current action and package surfaces do not expose exact owners for Kush, Makuria, Alodia, Mutapa, Rozwi, reserve deployments, weather combat, project-exploitation scandal, or several row-specific terminal disqualifiers.

The tranche does not infer those outcomes from regional overlays, current control, generic action success, war presence, confidence alone, or default ratios.

The existing G1 diaspora protocol, RSA succession integration, model packages, and world-order packages remain owned by their respective agents and are intentionally not duplicated here.

No fallback, simplification, new tag, model, world package, recurring world iteration, or readiness setter for an absent owner was introduced.
