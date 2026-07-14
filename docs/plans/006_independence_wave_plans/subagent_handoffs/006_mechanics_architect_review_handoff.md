# Event 006 mechanics architect repair handoff

## Status

The five blocking findings from the mechanics architecture review were repaired in the six-file gameplay surface granted by the parent. The invalid idea modifier, phase-gate divergence, patron pruning, host-death cleanup, cleanup API separation, identity repair, setup validation, rollback bound, network invitation, and founder patron-control findings were repaired in the same pass.

This is a completion claim for the assigned architecture-repair tranche, not for all accepted Event 006 content. One cross-event integration blocker remains: Event 005 does not yet publish the explicit active-origin contract consumed by the shared coordinator. No Event 005 file was edited.

## Scope and ownership

Gameplay files edited:

- `common/script_constants/006_independence_wave_mechanics_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt`
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt`

Documentation file edited:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mechanics_architect_review_handoff.md`

No Event 005 gameplay file, event script, decision file, localisation file, specification, package registry, spreadsheet, asset, or unrelated file was edited.

## Blocking repairs

### B1. Idempotent idea lifecycles

The semantic branch and the mutation guard are now separate in:

- `independence_wave_refresh_government_idea`
- `independence_wave_refresh_recognition_idea`
- `independence_wave_refresh_command_idea`
- `independence_wave_refresh_border_idea`
- `independence_wave_refresh_patron_idea`
- `independence_wave_refresh_instability_idea`
- `independence_wave_refresh_league_idea`

Each effect first selects the correct lifecycle from world state. It removes and adds ideas only when the selected idea is absent, and it always synchronizes the lifecycle variable. A repeated refresh with unchanged inputs therefore remains on the selected stage instead of falling through to a lower stage.

`independence_wave_refresh_identity_idea` also validates the region, verifies ownership of the exact desired regional idea, repairs a missing or mismatched idea/marker pair, and clears false success markers for an invalid region.

### B2. Frozen-plan lifecycle and set invariants

New shared triggers:

- `can_liberation_release_reset_plan`
- `has_valid_liberation_release_call`
- `can_liberation_release_begin_plan`

`liberation_release_reset_plan` and `liberation_release_begin_plan` no longer clear collecting, allocating, locked, or executing plans. Reset is restricted to absent, idle, committed, or aborted phases. An invalid begin call records `invalid_scope` without replacing a terminal plan, while a begin call against an active plan records `stale_plan` without erasing its arrays or scope marks. `liberation_release_abort_plan` remains the explicit active-plan teardown API.

New validation effects:

- `liberation_release_validate_plan_contract`
- `liberation_release_validate_set_invariants`

`liberation_release_validate_plan` invokes both before live row validation. The barrier now re-proves:

- valid mode, owner, participant-flag combination, and expected-count bounds;
- unique package IDs, target countries, reserved states, hosts, and nonzero reservation groups;
- valid territory, force, and state-role enums;
- Event 006 package upper bounds;
- primary/state host membership in the host ledger;
- anchor membership in the state ledger;
- row-owner participation in the current plan;
- each state row's exact reserved target-country, plan ID, owner, and package association.

`liberation_release_rollback_candidate_state_reservations` now accepts only a start index from zero through the current state-row count, preventing a negative-start no-progress loop.

### B3. Generation separation and origin history

`independence_wave_reset_current_generation` unregisters the current generation before clearing its key, removes current ideas and patron rows, and clears route, phase, host-outcome, failure, congress, league, identity, date, and package-local state. It preserves the historical ledgers and former-host ledgers owned for other released countries.

`independence_wave_initialize_country_origin` now:

- validates all setup scopes and enums through `has_valid_independence_wave_setup_input` before mutation;
- resets the prior generation atomically;
- allocates `independence_wave_generation_id`;
- registers active/network rows only after league storage is initialized;
- records both the legacy unique-country history and aligned country/generation/package/region/origin-date history rows.

Generation keys were added to and enforced for:

- active countries: `global.independence_wave_active_country_generation_entries`;
- former-host mirrors: `independence_wave_host_generation_entries`;
- patrons: `independence_wave_patron_owner_generation_entries`;
- network members: `global.independence_wave_network_member_generation_entries`;
- league founders: `global.independence_wave_league_founder_generation_entries`;
- league members: `global.independence_wave_league_member_generation_entries`;
- history: `global.independence_wave_historical_generation_entries` and its aligned package, region, and date arrays.

The shared `is_soviet_collapse_active_origin_country` trigger now requires the explicit `soviet_collapse_active_origin` flag and `liberation_origin = constant:liberation_origin.soviet_collapse`; it no longer treats the historical `soviet_collapse_event_created_republic` flag as a permanent active-origin lock.

### B4. Authoritative registry reconciliation

New or rewritten reconciliation APIs:

- `independence_wave_reconcile_active_registry`
- `independence_wave_reconcile_network_registry`
- `independence_wave_reconcile_league_founder_registry`
- `independence_wave_reconcile_league_member_registry`
- `independence_wave_reconcile_registries`
- `independence_wave_rebuild_network_regions`
- `independence_wave_rebuild_league_regions`

Country scope plus generation is the row identity. Reconcilers reverse-prune dead, ended, stale-generation, ineligible, and duplicate rows; repair flags from surviving rows; and derive active, network, founder, member, and region counts from the aligned arrays. Network removal cascades league-member and founder removal. League confidence divides by the derived member-array count.

Network, founder, and member registration now require membership in the authoritative upstream array, not only a country flag. Founder reconciliation refreshes patron ledgers before applying patron-control eligibility, so a dead or emptied patron row cannot preserve or incorrectly block founder status.

`independence_wave_leave_league` removes founder/member records only. It preserves network membership and active Event 006 origin and records the league-exit cleanup reason separately.

### B5. Exact and idempotent league transitions

`independence_wave_clear_league_phase_flags` centralizes clearing the mutually exclusive active phase flags. Every transition has an exact source phase, sets its date once, and becomes a no-op after it leaves that source:

| Effect | Exact transition |
| --- | --- |
| `independence_wave_open_regional_conference` | Informal Network to Regional Conferences |
| `independence_wave_complete_congress_preparation` | Regional Conferences to Congress Preparation |
| `independence_wave_fail_congress` | Congress Preparation to Congress Failed |
| `independence_wave_reopen_regional_conferences` | Congress Failed to Regional Conferences |
| `independence_wave_open_charter_vote` | Congress Preparation to Charter Vote |
| `independence_wave_proclaim_consultative_league` | Charter Vote to Consultative League |
| `independence_wave_proclaim_formal_league` | Charter Vote to Formal League |
| `independence_wave_upgrade_consultative_league` | Consultative League to Formal League |
| `independence_wave_mark_league_durable` | Formal League to Durable League |
| `independence_wave_enter_league_crisis` | Formal or Durable League to League Crisis |
| `independence_wave_reform_league` | League Crisis to Reformed League |
| `independence_wave_split_league` | League Crisis to Rival Leagues |
| `independence_wave_normalize_reformed_league` | Reformed League to Formal League |
| `independence_wave_reunify_rival_leagues` | Rival Leagues to Formal League |
| `independence_wave_dissolve_league_to_network` | League Crisis to Dissolved Network |
| `independence_wave_restart_informal_network` | Dissolved Network to Informal Network |

Formation now requires Congress Preparation exactly and revalidates every founder as an active, current-generation network member that is neither client-locked nor under patron control. Vote, crisis, and dissolution dates cannot be reset by repeated calls in their destination phase.

## Secondary repairs

- Replaced both invalid `reinforce_rate` idea modifiers with documented `land_reinforce_rate`.
- Aligned founding gates with the accepted wording: Emergency plus capital control and capacity for Provisional; Provisional plus de facto recognition or any settled host relation for Recognized; Recognized plus the accepted regional value and route gates for Regional Power.
- Added `has_valid_independence_wave_region`, `has_current_independence_wave_identity_idea`, and `has_valid_independence_wave_setup_input`.
- Added `independence_wave_remove_patron_row` and `independence_wave_prune_patron_ledger`; strongest-patron and patron-count calculations now use current-generation, living, positive-influence rows.
- Added generation-aware host mirror synchronization/removal and `independence_wave_handle_former_host_death`. Former-host death records Host Collapse and removes only the bilateral mirror; it does not end the released country's origin.
- Split `independence_wave_origin_end_reason` from `independence_wave_relationship_cleanup_reason`. Origin termination accepts only annexation, voluntary reunion, formable absorption, or dissolution. Host death and league exit use their dedicated cleanup paths.
- Rewrote network invitation eligibility to test absence from the network rather than absence from the league.
- Added current patron-control checks to founder registration and formation revalidation.

## Validation evidence

Targeted static checks against the final six-file snapshot found:

- all 219 distinct `constant:category.key` references resolve to installed script-constant definitions;
- all 98 Event 006/coordinator scripted effect and trigger calls resolve to top-level definitions;
- all 41 referenced Event 006 ideas resolve to definitions in `006_independence_wave_ideas.txt`;
- all 18 idea modifier keys appear in the installed vanilla modifier documentation, including both repaired `land_reinforce_rate` uses;
- the two touched effects files contain 107 top-level effects and 152 internal call edges with no scripted-effect recursion cycle;
- the host-relation mutation block contains only its eight deltas, clamp, mirror sync, and lifecycle refresh. A context scan found no bare region-trigger fragments in effect scope; every remaining `AND = { ... }` is nested in a legitimate trigger limit;
- the setup, host, patron, active, network, founder, member, and history ledgers each have explicit alignment triggers for every added generation/value array;
- the Event 5 source surface contains no setter or clearer for `soviet_collapse_active_origin` and no assignment of `liberation_origin.soviet_collapse`, confirming the blocker below rather than silently assuming it is wired;
- no broad daily, weekly, monthly, or world-country iteration was added.

Final gameplay-file SHA-256 snapshot:

- `FCE975C56B3BE4694D7DB9781109CBECBCFE9E491A9E8A0A60FBB32A93A90D11` — `common/script_constants/006_independence_wave_mechanics_constants.txt`
- `74E252017C06038789842C7126BBA4CFC37D324C10BE39DC7D01E04805A06FD1` — `common/scripted_triggers/006_independence_wave_triggers.txt`
- `908B321CA2873074B6EDA7DF84BF1A2D246BAA5F864DC9A9633547B819421CAD` — `common/ideas/006_independence_wave_ideas.txt`
- `7BC0F5BECAE6B15CC3C7EEB2A1E0F6DCD59616607A8741E24572CF7B0367982F` — `common/scripted_effects/006_independence_wave_effects.txt`
- `2926D3AAF72CA953F694AA323CFCDC4116B5197FC53496C7ECDCF891666BEED0` — `common/scripted_effects/chaosx_liberation_release_effects.txt`
- `B9E33690A227C6578C1CC343726A3635F19B0ECE317FA10DC194F6587CA29FCF` — `common/scripted_triggers/chaosx_liberation_release_triggers.txt`

The optional Event Chain Viewer workspace lint completed only as `EVENT_INSPECTED_PARTIAL` because its inline inventory was capped and two unrelated event-analysis sources were skipped. It supplied no task-specific defect and is not used as acceptance proof for this mechanics repair.

## Remaining cross-event blocker

Event 005 must set this contract on each currently active Soviet Collapse-created origin:

- `set_country_flag = soviet_collapse_active_origin`
- `set_variable = { liberation_origin = constant:liberation_origin.soviet_collapse }`

It must clear the active flag and return `liberation_origin` to `none` when that origin ends, is absorbed, reunites, dissolves, or otherwise ceases to be the active Event 005 generation. Until that Event 005-owned work is implemented, the shared trigger is correct but cannot distinguish live Event 005 origins in runtime data. This blocker was intentionally not patched because Event 005 files were outside the granted surface.

## Parent integration resolution

The parent review resolved the cross-event blocker after this handoff. `soviet_collapse_setup_breakaway_country` now publishes the explicit active-origin contract for Event 005-created republics and high-chaos successors, and the Event 005 annex cleanup clears it without erasing historical creation flags. Event 006 tag availability now rejects only active Event 005 provenance, allowing a later resurrection to receive the origin that actually recreates it as required by the accepted specification.

The shared coordinator also has a locked-plan capital-relocation API. It moves a host capital to the already validated protected state only when the current capital is a frozen release row, verifies the relocation before state ownership changes, and exposes a failure reason to the Event 006 executor. Joint execution must call the same API before either origin mutates the map.

## Accepted content gaps outside this repair tranche

The architecture blockers above are repaired, but the broader Event 006 implementation still needs the accepted content work already identified by the source specs, including:

- route-specific institutions and country-specific founding identity progression beyond the regional foundation ideas;
- patron influence calculation from channel, visibility, and domestic absorption capacity rather than only a precomputed delta;
- a documented aggregate founder recognition/network-standing calculation;
- full charter compatibility, approval, arbitration, defense acceptance, patron exceptions, expulsion, associate status, and faction behavior;
- the coordinator's explicit host-capital relocation when the protected-state choice falls back from the current capital.

These items were not simplified or replaced in this pass; they remain separate implementation work.

## Simplifications, omissions, and blockers

No fallback, placeholder, or simplification was introduced inside the assigned repair surface. The only implementation omission is the explicitly out-of-scope Event 005 active-origin setter/clearer described above. The accepted broader content gaps are not claimed complete.

No commit was created by this subagent; final diff review and the plan-scoped commit remain with the parent agent.

## Reference basis

The repair used the mandatory offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Installed vanilla documentation for effects, triggers, variables, arrays, loops, event targets, script constants, collections, ideas, and modifiers was rechecked, along with vanilla precedents for `all_of_scopes`, state/country event-target comparison, array loops, and idea modifiers.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`

No skill was created or updated.
