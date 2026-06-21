# Event 012 Africa — Current Source of Truth Map

Updated: 2026-06-21

## Current accepted design

The accepted source package is the full Event 012 Africa spec folder under `docs/specs/012_africa_specs/`. The implementation should treat the main design files as one package rather than elevating any small correction above the continental-unifier system.

Primary design surfaces:

- `specs/012_africa_spec_part_1_core.md`
- `specs/012_africa_focus_tree_plan.md`
- `specs/012_africa_decisions_missions_ui.md`
- `specs/012_africa_country_packages_and_subjects.md`
- `specs/012_africa_evolutions_world_end_and_scenarios.md`
- `specs/012_africa_niche_country_expansion.md`
- `specs/012_africa_niche_polity_expansion.md`
- `specs/012_africa_niche_polities_and_absurd_paths.md`
- `specs/012_africa_niche_authorities_high_chaos_expansion.md`
- `specs/012_africa_high_chaos_absurd_paths.md`

Supporting surfaces:

- `research/` for historical and ecological inspiration notes.
- `matrices/` for AI, asset, decision, country-package, achievement, and acceptance maps.
- `focus_graphs/` for architecture sketches.
- `prompts/` for implementation, asset, achievement, super-event, decision/mission, and `/goal` handoff prompts.

## Foundation addendum disposition

The older working plan `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md` is dispositioned by `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md`. Treat that ledger as the current map for which foundation items were implemented/folded, superseded/modified, queued/still open, or rejected/held.

This disposition resolves the stale-plan bookkeeping problem only. It is not an Event 012 completion claim. Remaining known blockers include targeted scenario validation, live GUI/animation render proof, stale plan cleanup, deeper host and created-country route consequences, AI/balance/exploit validation, spreadsheet/catalog alignment, and final proof that the World Is One terminal path only opens after all continental-unifier prerequisites. The static Continental Congress GUI wiring has been audited against its control names, visibility hooks, sprite registration, DDS dimensions, and localisation references; that audit does not replace live in-game render proof.

## Country naming style

Country and cosmetic names use direct polity names. Avoid generic political attachments in country names: no `Compact`, `Office`, `Bureau`, `Board`, `Commission`, `Registry`, `Mission`, `College`, `Guard`, or `Authority` as the public country name unless it is a real intended state form. `Kingdom`, `Sultanate`, `Republic`, `Federation`, `Confederation`, `Union`, `Empire`, and similar direct state forms are fine when they fit the route. Ideology-specific names are encouraged where they make the tag feel alive.

Mechanic names can still use administrative language. A country can be `Kongo` while its focus branch contains a reconstruction office, or `Oyo` while its army route has a cavalry bureau.

## Leader display-name flavour

The Event 012 leader/court display-name pool includes:

- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

Keep those strings untranslated in player-facing English and keep raw strings out of internal ids, file paths, tags, variables, sprite names, and asset text. The joke belongs to event-created or event-recast public ruler/court/council display names; serious country, office, historical polity, institution, symbol, and source notes remain researched.

## Current design emphasis

- A valid African-capital country becomes the unifier and receives the Africa package.
- Paper cores and staged integration satisfy the catalogue fantasy without creating an instant snowball.
- The Charter League lets African countries cooperate against colonisers before integration pressure begins.
- RSA in the Allies uses the civil-war branch and Allied peace-out rule.
- The Archive of Old Seats and Authority Atlas add niche historical authorities, restoration offices, specialist schools, and high-chaos absurd actors without turning human polities into caricatures.
- Nonhuman/supernatural routes are explicit fictional/high-chaos actors and use shared nonhuman classification when implemented.
- Additional unreleased Event 012 presentation roles still stay research-gated. The accepted live Africa super-event package is sourced and final-wired for visible slots `68-79` plus root-terminal audio id `80`; the `2026-06-19` sponsor-file hash drift audit was closed by normalizing the live `music/` cue from the archived final `.ogg`.

## June 18 implementation disposition

Parent commit `9858db02` closes the previously queued high-chaos actor package gap for:

- `BON` Bonobo Kinship Congress
- `HYR` Hyena Radio Dominion
- `BIR` Bird of the Walls
- `SAO` Sao Terracotta Host

The current documentation evidence for that closure is:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_missing_high_chaos_actor_parent_handoff.md`
- `docs/assets/012_africa/missing_high_chaos_actor_assets/manifest.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `docs/events/012_africa_foundation.md`

This closes the actor-package, portrait/flag, achievement-icon, and prompt-named achievement queue for those four tags. It does not close the broader Event 012 completion blockers around accepted foundation-addendum depth, Continental Congress presentation depth, country-package depth, UI/animation proof, balance proof, or live scenario validation.

The root-terminal World Is One super-event disposition is an intentional hybrid. The World Root terminal branch shares base slot `72` text and image presentation (`The World Is One`) and uses distinct root-terminal audio id `80`. Archive remains the distinct terminal presentation variant where implemented through slot `79`.

Later June 18 parent tranches close additional bounded gaps:

- `063e2354` regenerates the Event 012 Africa goal and idea icons without white backgrounds. Goal icons remain goal-sized DDS files, while idea icons are distinct 64x64 designs rather than downscaled goal art. The live DDS files are under `gfx/interface/goals/012_africa/` and `gfx/interface/ideas/012_africa/`, with source packages and manifests under `docs/assets/012_africa/`.
- The current live icon source packages are the 2026-06-21 v6 goal-icon package and v7 idea-icon package: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/` and `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/`. They supersede the earlier v3/v6 icon-package notes; `docs/assets/012_africa/implementation_asset_manifest.md` is current for the live package paths, checker contact sheets, and validation summaries. The `.gfx` sprite names and live texture paths remain unchanged.
- `c13fe459` makes the high-chaos Bestiary focus branch hidden until `AFR_high_chaos_door` reveals it through `africa_high_chaos_branch_revealed` and `mark_focus_tree_layout_dirty`.
- `94857ce3` gives the Continental Congress Seats and Bestiary Terms GUI actions the same concrete support-equipment, manpower, and command-power requirements as their decision equivalents, using shared helpers so the GUI and normal decision paths cannot diverge.
- The current dossier-AI tranche adds Authority Atlas lifecycle and eight-profile historical dossier AI to `common/ai_strategy/012_africa.txt`, and weights the Authority Atlas dossier decisions by route/profile in `common/decisions/012_africa_decisions.txt`.
- The current dossier-settlement tranche adds once-only value-only settlement outcomes for every historical dossier ID through `africa_apply_selected_dossier_specific_settlement_effects`, visible through `GetAfricaSelectedDossierSettlementSummary` in the Authority Atlas header.
- The current dossier-resistance tranche turns post-settlement resistance watches into active gameplay: observer, protected-seat, and rejected-claim settlements can commit timed Congress mediation, regional-office and direct Archive settlements can commit timed enforcement, each path pays concrete non-PP resources plus dossier-profile logistics, uses the stored resistance dossier/seat context after the selected dossier advances, blocks further settlements while the one active watch is unresolved, and produces profile-specific value movement plus visible local reports that name the intervention method.
- The earlier settlement-fork tranche expanded the dossier settlement split beyond observer seats with protected seats, regional authority offices, and direct Archive seals. Protected seats require trust/authority and spend rifles, support equipment, and manpower before using the mediation watch; regional offices require authority/cohesion and spend support equipment, trains, and manpower before using the enforcement watch. The Authority Atlas header exposes those counters beside the rejected-claim counter, and watch success/failure moves distinct values for each settlement mode.
- The current rejected-claim tranche adds the fifth accepted Authority Atlas settlement fork: `Reject Counterfeit Claim`. It opens from documents-before-consent, the Authority Register, an exposed direct Archive seal, or Ananse counterfeit-watch access; spends political power, support equipment, manpower, command power, and army experience; applies its own profile movement; tracks a rejected-counterfeit settlement counter; and starts a stored rejected-claim resistance watch that can resolve through Congress mediation or fail into Archive Mandate/Colonial Alarm pressure.
- The current forgery/museum crisis tranche gives direct Archive seal failure an active follow-up instead of only a passive exposed-seal flag. A failed `africa_direct_archive_seal_mission` stores the sealed dossier and old-seat state, starts a 90-day `africa_forgery_museum_crisis_mission`, exposes live status in the Authority Atlas header, and unlocks the separate paid timed investigation `africa_expose_forged_archive_case`. That investigation requires seat control/protection, Archive Mandate, Old-Seat Legitimacy, Restoration Debt discipline, political power, support equipment, manpower, command power, and army experience to break the forged file. Ananse Ledger counterfeit-watch access turns the success path into a web intercept with additional Archive Mandate and Colonial Alarm relief; timeout hardens the forged file into a museum-label crisis that damages Archive Mandate and Old-Seat Legitimacy while raising Restoration Debt, Local Sovereignty pressure, and Colonial Alarm.
- The current old-seat arbitration tranche adds the second-stage Authority Atlas rivalry calendar. Six once-only rivalry pairs or clusters can open after their relevant historical dossiers are settled: Great Lakes, Central River, Western Crowns, Red Sea, Monsoon Rova, and Sahel Caravan. The convene decision spends political power, support equipment, manpower, command power, and army experience, stores the active pair and old-seat state, and starts a one-at-a-time mission. Success requires the stored seat to stay secured plus pair-specific visible value gates; failure keeps the pair retryable while raising sovereignty/debt pressure. The Authority Atlas header exposes active status, active case, and the settled-pair counter.
- The historical case-mission layer places a required step between old-seat guards and settlement. Guarded dossiers start a typed case mission through `africa_prepare_selected_historical_dossier_case`: site cases cover Nile/Red Sea, Maghreb/desert, and southern stone profiles; route cases cover Sahel charter, central river, and Indian Ocean profiles; hearing cases cover western crowns and Great Lakes profiles. Each case stores its dossier id, seat state, and type in a reusable slot, spends political power plus concrete equipment/manpower/command/XP resources, checks visible value gates, records per-dossier success or failure, and blocks all five settlement forks until the selected dossier has a successful case. The Authority Atlas header, Continental Congress panel, AI strategy, and World Is One certification expose or require the historical case success count.
- The current Continental Congress presentation pass adds the selected historical case type/status, all three reusable historical case slot statuses and hover details, local resistance watch seat context, and active old-seat arbitration hearing/seat/gate details to the custom decision-category panel. This closes the immediate presentation gap left by the historical case and old-seat arbitration mechanics, though broader country-package depth and live scenario validation remain open.
- The high-chaos companion parity tranche gives `BON`, `HYR`, `BIR`, and `SAO` separate pre-World Witness route focuses and tag-specific capstones inside `africa_high_chaos_actor_focus_tree`: Bonobo kinship-boundary pacts and a gentle veto court, Hyena/Bird signal-omen work leading to Hyena night broadcasts or verified wall warnings, and Sao terracotta-citadel terms leading to the Terracotta Line. These focuses move the same visible Africa value set as the rest of the Bestiary layer and keep the last four actors from relying on another actor's branch.
- The current triggerable-scenario validation tranche makes the Continental Pole scenario a usable late-route validation launch. It opens the sponsor staff, cross-continent charter, proof-ledger, one-charter, and route logistics gates that the late sponsor/proof decisions actually require; high intensity fills the dossier, regional-authority, regional package-action, living-core, and high-chaos validation counters; maximum intensity adds the external continent-ready hooks and Totalen Chaos tier needed to test the certification route. It still does not set proof-verified flags, `all_continent_unifiers_world_end_ready`, `africa_world_is_one_gate_prepared`, `world_end_africa_world_is_one`, or terminal World Is One flags.
- The current selected-unifier origin tranche makes the host archetype affect more than selection text. `africa_apply_unifier_origin_package` classifies registered host tags into Highland Legacy, Atlantic Return Route, Union Rupture, Nile Sea Gate, Western Congress Ports, Congo River-Forest Mandate, Indian Ocean Gate, or General Congress Mandate. Each profile applies one visible spirit, moves mapped Event 012 values through script constants, grants matching opening logistics, sets a profile flag and variable, appears in the Continental Congress header through `GetAfricaUnifierOriginProfileName`, has cleanup in `africa_clear_runtime_context`, and has AI posture coverage in `common/ai_strategy/012_africa.txt`.
- The current origin-mandate-case tranche turns that profile into active gameplay after `AFR_the_charter_mandate`. The Continental Congress now has `africa_open_origin_mandate_case`, which pays political power, support equipment, and profile-specific equipment/manpower/command/XP logistics, then starts `africa_origin_mandate_case_mission`. The mission requires capital control plus profile-specific visible value gates and either files the origin case with another profile-specific value shift or times out into Legitimacy/Authority damage, Colonial Alarm, and Restoration Debt. The standard decision header and scripted GUI expose the origin case status, and dynamic localisation shows the current cost and requirement family.
- The current regional-authority mandate tranche gives created regional authority subjects a leader-side active consequence after their companion tree work. `africa_commission_regional_authority_mandate` targets a confirmed loyal regional authority, spends political power, command power, manpower, rifles, and support equipment, transfers the committed resources to the subject, and starts a 150-day `africa_regional_authority_mandate_mission`. Success requires the target to keep its capital, avoid capitulation or war with the Charter leader, and complete its tag capstone focus; success increments a visible mandate count and applies role-specific effects for West/Sahel, coastal, interior, or southern authorities. Failure damages Regional Trust, raises Colonial Alarm and Paper-Core Burden, and leaves the subject retryable.
- The current regional-authority package tranche adds tag-specific post-mandate follow-up actions for all ten regional authorities: WAC port congress, SAH caravan columns, MAG harbor dockets, NHR highland warrants, EAC railway timetable, GLK lake guards, CBC river quartermasters, ZSC stone-city yards, SLC mine-port belt, and IOC sea lanes. Each action requires a successful mandate, loyal subject status, capital control, the matching companion-tree capstone, and a one-time target flag; spends concrete non-PP resources through the custom-cost path; transfers equipment, manpower, convoys, trains, infrastructure, dockyard or industrial capacity, or guard divisions to the authority; moves visible Africa values; fires local reports `chaosx.nr12.55` through `chaosx.nr12.64`; exposes `africa_regional_package_action_count` against the configured goal in the Charter diplomacy header; and gates sponsor readiness plus the terminal World Is One certification path through `has_africa_required_regional_package_actions`.
- Later June 20 regional-package audit evidence supersedes earlier handoff notes that treated this regional-authority package work as dirty, WAC/SAH/IOC-only, or still in progress. `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_all_regional_package_decision_audit_handoff.md` records all ten actions as live and audited with no blocking gameplay issue; `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_package_gate_scripted_helper_audit_handoff.md` records the package-action gate helper as valid. Current tree evidence also includes same-tick `available` revalidation for the ten package decisions and `_tooltip` hover localisation for their custom costs, so the older recommendations for those two items are closed unless later edits remove them.
- The created-actor Charter lifecycle keeps named regional or Bestiary seat spirits after a country leaves the League or prepares resistance, while removing Charter umbrella spirits and bindings. Peaceful exit records `africa_charter_former_member` and the distinct `constant:africa_charter_league.former_member`; armed resistance stays on the separate resistant-member path.
- The current targeted scenario-validation tranche adds explicit `Fragile Unifier` and `Ally Under Attack` Africa triggerable scenario profiles alongside Standard Unifier, RSA Civil War, Liberation League, High-Chaos Covenant, and Continental Pole. `Fragile Unifier` selects a small African-capital host where possible or uses a marked WAC/weighted fallback with lower authority and higher restoration strain. `Ally Under Attack` requires an outside holder of African land, seeds a Charter regional authority under attack, stores the ally and selected holder as global scenario targets, gives both countries visible scenario flags and AI posture, and opens the existing aid, corridor, defensive, and liberation responses against that live ally. Runtime cleanup clears the scenario actor/target flags, target pointers, scenario globals, and fallback markers. The tranche also aligns `AFR_congress_of_continents` and `africa_proclaim_dynamic_cross_continent_union` with the one-or-more sponsored charter rule while keeping the later World Is One proof/certification path all-four. `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md` records static/script coverage for the eight required acceptance scenarios. It does not replace live scenario proof.
- The terminal World Is One preparation layer has a distinct resource commitment: `africa_prepare_world_is_one_gate` uses `can_africa_prepare_world_is_one_gate`, then revalidates the full prerequisite chain and spends political power, convoys, trains, support equipment, manpower, command power, and army experience before setting only the prepared-gate marker. `AFR_the_world_is_one` remains the only terminal starter through `can_africa_start_world_is_one_gate`.
- The visible World Gate status now mirrors the same terminal chain: it displays `Gate Prepared` only when `can_africa_start_world_is_one_gate` is true, and stale certification cannot hide a missing external-continent readiness flag.
- Cross-continent sponsor charters and the dynamic union proclamation use route-specific and pay-specific triggers in the visible requirement/cost path and in the click-time completion path. The sponsor charters spend political power, convoys, equipment, manpower, and command power only after the relevant staff/focus route, world-end state, one-time flag, and resource layer revalidate. The dynamic union proclamation likewise revalidates one-or-more sponsored charters, the World Root/Congress route flags, and the full convoy/rifle/support/manpower/command-power/army-XP layer before spending and applying the identity.
- External continent-unifier proof audits use route-specific pay triggers in both the visible custom-cost gate and the click-time start path. The start helpers spend political power, equipment, manpower, command power, and army experience only after route validity and resources are revalidated, then the timed proof can still fail if its external readiness hook or world-order route context drops before completion.
- The Continental Congress scripted GUI static wiring audit closes the known missing-fallback-hook risk for the Charter banner and records that all six visual-strip controls have matching scripted visibility hooks, sprite registrations, existing alpha-capable DDS assets, and localisation. The remaining UI blocker is live render/animation proof in-game.
- The historical source-asset blocker is narrowed by the latest source-research pass: Benin, Sokoto, Kuba, Luba, Adal/Ifat, Ajuran, and Zanzibar now have local raw and processed source files plus rights notes. Bunyoro/Kabalega remains documented-only until a rights-clean portrait or period print is found.

These tranches reduce the active blocker list, but they do not close Event 012. Remaining known blockers still include live scenario validation for the static validation matrix, live GUI/animation render proof, deeper route-specific country-package consequences beyond the selected-unifier origin profile/case, regional-authority mandate/package cycle, current dossier slot families, and created-actor role packages, the remaining Bunyoro/Kabalega source lead, AI/balance/exploit validation, spreadsheet/catalog alignment, and live proof that the World Is One terminal path only opens after all continental-unifier prerequisites. The accepted Africa super-event package is blocker-free for the live slots: visible slots `68-79` and the root-terminal hybrid using shared slot `72` text/image plus dedicated audio id `80` are sourced, wired, documented, and file-reconciled. The high-chaos capstone parity gap for `BON`, `HYR`, `BIR`, and `SAO` is closed by their kinship-boundary, signal-omen, terracotta-citadel, and tag-specific capstone focuses.

## June 20 stale-note disposition

- Earlier v3/v6 icon-package source claims are superseded by the v6 goal-icon and v7 idea-icon packages in `docs/assets/012_africa/implementation_asset_manifest.md`.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_post_package_completion_audit_handoff.md` is superseded only where it says the regional-authority package expansion was dirty, WAC/SAH/IOC-only, or not closed. Its broader completion blockers remain current.
- `docs/plans/012_africa_plans/2026-06-17_event_012_africa_achievement_completion_handoff.md` should be read with its later-closed achievement section: the Hyena Radio Dominion, Bonobo Kinship Congress, Bird of the Walls, and Sao Terracotta Host achievement rows are no longer queued.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_created_actor_static_country_package_audit_handoff.md` records static country-package coverage for all 25 created Event 012 actors and found no missing tag/history/OOB/portrait/flag/localisation/focus/AI surface. It does not close the broader route-depth or live-validation blockers.
- `docs/assets/012_africa/source_research/manifest.md` should be read as current for historical source confidence. The only documented-only row left by the latest source pass is Bunyoro/Kabalega.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_completion_gap_audit_handoff.md` remains current for the non-completion verdict and the larger validation/depth blockers, but its icon-package and regional-package evidence should be read through this current-source update.

## Cleanup note

Earlier correction-only name-protocol files and matrices have been removed from the current handoff. Their useful content is folded into the normal country-package, prompt, and acceptance surfaces above.

## V7 prompt note

The implementation goal prompt is intentionally longer than the V6 compact version and still points to the spec pack instead of repeating the whole design.

## V8 naming note

The latest cleanup keeps the longer V7 goal prompt but adds the direct country-name rule. Country and cosmetic names should be simple polity/place names with ideology variants where useful, while generic administrative words stay in mechanics, decisions, focus groups, or subject-status notes.

## V9 structure cleanup note

Short addenda and duplicate manifests are no longer separate source files. Their content is folded into the main spec, matrix, prompt, graph, and subagent-handoff files. Use the primary design surfaces listed above instead of chasing small revision fragments.
