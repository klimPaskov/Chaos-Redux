# Event 12 Africa decision and mission release-candidate audit

## Scope and status

Audited the six Event 12 decision and category files, the Event 12 action, priority-member, RSA, and world-order helpers they invoke, their English localisation, category GUI surface, and focus handoffs.

The original audit covered 212 unique decision or mission identifiers, including the Charter League, high-chaos nature-disaster selectors, priority-member package actions, RSA crisis actions, scramble windows, and world-order sponsorship obligations.

One local decision safety fix was applied.

The shared Charter Ledger icon replacement was reviewed as parallel work and deliberately preserved rather than rewritten by this audit.

## Final release-candidate re-audit, 2026-07-29

The current decision surface contains 213 unique decision or mission identifiers with no duplicate identifier, missing title, missing description, missing custom-tooltip key, undefined action constant, or missing literal decision/category sprite definition.

The installed Charter Ledger asset at `gfx/interface/decisions/012_africa/core/decision_012_africa_charter_ledger.dds` is a valid 32 by 32 DDS and matches the registered `GFX_decision_012_africa_charter_ledger` sprite.

The latest natural-disaster actions validate one exact selected enemy, reserve their Event 013 caller cost before the action record begins, retain the reservation only while the active record exists, set a timed weapon cooldown after the call, and clear the reservation from common action cleanup.

`africa_scramble_close_continental_docket` is host-scoped through its shared availability trigger, requires the completed aftermath requirements and no active intervention war, clears the shared Scramble response state, clears the current quote, and leaves unfinished external continent packages outside the runtime path.

No further narrow decision, mission, helper, localisation, or GFX patch was justified by the final re-audit.

The three formation selectors `africa_select_awaken_stone_cohort`, `africa_select_train_gorilla_heavy_infantry`, and `africa_select_organise_pan_sappers` are deliberately unreachable in this release candidate because their shared global gate `africa_strange_formation_package_ready` has no setter.

The same gate exists in both their player visibility and action-specific validation paths, so neither a player nor the Event 12 AI controller can quote or execute them until a future model, unit-template, spawn-consumer package intentionally enables the gate.

## Changed files and identifiers

| File | Identifier | Before | After |
| --- | --- | --- | --- |
| `common/decisions/012_africa_decisions.txt` | `africa_world_fulfil_sponsorship_obligation` | A country in the sponsorship target array could evaluate the fulfilment decision without an explicit root-host gate. | `target_root_trigger = { africa_is_current_host = yes }` limits the action to the active Africa host while preserving the target, stockpile, PP, deadline, and outcome logic. |

The parallel icon change replaces 165 Event 12 Charter decision and category references from the undefined `GFX_decision_generic_diplomatic_treaty` with `GFX_decision_012_africa_charter_ledger`, registered in `interface/012_africa.gfx`.

The referenced texture is `gfx/interface/decisions/012_africa/core/decision_012_africa_charter_ledger.dds`.

The Charter Ledger DDS is now present, valid, and resolves the shared icon path for all 165 migrated Charter call sites.

## Issue list

### Resolved parallel asset issue

- `GFX_decision_generic_diplomatic_treaty` was not registered by vanilla or the mod, leaving 165 Charter Council decision/category entries without an icon sprite.
- Parallel work has moved every call site to the registered `GFX_decision_012_africa_charter_ledger` path.
- The installed 32 by 32 Charter Ledger DDS now supplies that registered sprite path.

### Medium, patched

- `africa_world_fulfil_sponsorship_obligation` had target eligibility but no explicit `target_root_trigger` for the current host.
- The new root guard prevents a non-host evaluation path without tying an existing unpaid obligation to the package-count gate, so an outstanding obligation cannot be hidden merely because no further sponsor package can be installed.

### Informational, reviewed and accepted

- Twelve other targeted decision or mission entries do not state `target_root_trigger` directly, but their `activation` or category lifecycle is already restricted to `africa_is_current_host = yes`.
- No duplicate decision identifiers, missing Event 12 event references, undefined Event 12 helper calls, missing title/description keys, or missing referenced custom localisation keys were found.
- The action matrix is an intentional centralised quote-and-execute design, not a flat PP store; its 102 action selectors resolve through action metadata, resource-cost helpers, risk, timing, and current-action cleanup.

## Category lifecycle notes

- `africa_charter_council_category` is host-owned and pages its action families through visible phase, evolution, and route flags.
- The 102 selectors only choose an action; execution requires a generated current quote and uses the active-target arrays, giving each action an explicit phase, cost, duration band, and resolution path.
- `africa_priority_member_category` requires registration and a package before its ratification, political, League, overlap, force, and post-settlement surfaces appear.
- The priority-member withdrawal mission cancels when departure state ends or the relationship is no longer leaving/rival, and its timeout resolves the intended withdrawal rather than leaving a stale mission.
- `africa_rsa_crisis_category` is gated by its contact and crisis flags, with one-use or phase-completion flags on corridor, citizenship, lease, and exile actions.
- Scramble and world-order surfaces use separate target arrays and phase flags, avoiding the Charter Council’s selected-target arrays leaking into regional sponsorship actions.

## Mission quality notes

| Mission family | Owner | Category | Region | Requirement | Duration | Success | Failure or cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mission_africa_action_short`, `medium`, `long`, `epic` | Current Africa host | Charter Council | Selected country or host action | Matching active record, action generation, and duration flag | 60, 120, 240, or 540 days through action variables | Resolves the current action outcome | Cancels on event end or stale generation and uses cancellation cleanup | Active action arrays and one current-action record prevent parallel duplication |
| `mission_africa_complete_continental_peace_exemption` | Current Africa host | Charter Council | Exemption target array | Active exemption target and continental-peace condition | Targeted timed objective | Completes the exemption path | Cancels if the relevant target state is no longer valid | Target array ownership is host-scoped |
| Scramble recognition, coalition, intervention, and aftermath windows | Current Africa host | Scramble actions | Selected external participants | Scramble phase and participant validity | 90, 120, 150, and 180 days | Resolves the named scramble window | Window expiry and phase cleanup remove stale access | Separate phase flags prevent repeat window activation |
| `africa_world_sponsorship_obligation` | Current Africa host | World-order actions | Sponsoring package country | Target has an unpaid installed sponsorship obligation | 180 days | Fulfilment decision clears the due state | Timeout defaults the obligation and removes the active target relationship | Host-owned target array and due flag prevent duplicate missions |
| `africa_priority_member_withdrawal_mission` | Priority member country | Priority-member package | Package country | Withdrawal state and leaving/rival relationship | Centralised priority-member duration | Peaceful withdrawal resolution | Cancel cleanup when the departure no longer applies | The package’s active-mission flags prevent a second withdrawal mission |
| RSA first-proof mission | RSA crisis actor | RSA crisis | RSA | First-proof route and required crisis state | Route variable | First-proof completion helper | Both cancel and timeout use the failure helper | Route completion flags make the mission one-shot |

## Cost and requirement clarity

- Charter selectors intentionally cost zero because the generated quote applies the action-specific PP, equipment, trains, convoys, manpower, command-power, factory, legitimacy, support, target, or risk commitment before execution.
- The four duration bands and action costs are centralised under Event 12 action constants instead of being duplicated across the selector list.
- RSA’s civilian-corridor, regional-support, citizenship, sovereignty-guarantee, base-lease, and exile actions have explicit one-use or target-validity gates and use their corresponding resource effects.
- The sponsorship fulfilment decision visibly consumes PP and requires infantry equipment, support equipment, and convoys before its Event 12 effect removes those stockpiles.
- No passive PP-only loop, free unit loop, equipment farming loop, war-goal spam path, core spam path, or cooldown-bypass loop was identified in the audited decision surface.

## AI validity and route-lock notes

- Player-facing Charter selectors have zero AI weight while the designated Event 12 AI action controller selects and executes legal quoted actions through the same action metadata.
- Priority-member focus integration uses explicit package, settlement, mechanic, League, overlap, and force-ready flags, and its focus steps feed the corresponding package helpers rather than independent reward dumps.
- The continental focus tree checks the recorded full, partial, and failure flags produced by Charter action resolution, giving those decisions route consequences.
- RSA’s targeted sovereignty guarantee excludes capitulated, subject, non-neighbour, non-African-core, and already-guaranteed targets.
- The new sponsorship root guard closes the only reviewed explicit host-scope gap.

## Localisation and tooltip notes

- All audited Event 12 English localisation files have UTF-8 BOM encoding.
- Category titles, descriptions, decision titles, descriptions, custom effect tooltips, and referenced scripted-localisation keys resolved in the static audit.
- The action quote flow keeps raw resource and target requirements behind custom tooltip and dynamic-localisation surfaces rather than exposing long implementation triggers to the player.
- No localisation patch was needed for the host-scope correction because it does not alter player-facing cost, target, timing, or effect text.

## Scripted GUI evidence

- Reviewed `common/scripted_guis/012_africa_charter_scripted_gui.txt` and the linked Charter UI source.
- The GUI only selects pages, current overlay/member/state targets, and action quote context; it does not bypass the decision costs, availability checks, or resolution helpers.
- GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7e702a0ee7af78c48a5aab504aed3aae3f7431cd7b05e2dc413705abada95f5/1dfeb15b739b996b4350e322d87d9efb87998713a2c39842f15afe19be62e308/gui-inspect.449c42a80ca0b635.json`.
- GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe3f1eb7c6cb9069d07b28296ab58c962c5512ab29d886ac9e67a8bb81e29417/043e15a2bfb6a1eaa7ac13889c9d10a9ea875dfbfcb751e324fb8795c4e87fff/africa_charter_window-full.svg`.
- The MCP diagnostics included global workspace collisions and truncated global counts, so its 663 modelled, 91 approximated, 135 ignored, 6 missing, 93 unsupported, and 13 unresolved items cannot be attributed to Event 12 alone.
- No GUI source change was justified by that non-specific diagnostic output.

## Meaningful validation

- Confirmed all six audited decision/category files have balanced brace counts and contain no unsupported `<=` or `>=` operators.
- Confirmed the final surface has 213 unique decision or mission identifiers with no duplicates.
- Confirmed no missing Event 12 event IDs, Event 12 helper references, titles, descriptions, or referenced custom-localisation keys.
- Confirmed the action registry covers selectors 1 through 102 and the quote-to-execute paths reference the centralised action constants and helpers.
- Confirmed `africa_world_fulfil_sponsorship_obligation` now includes the host root gate.
- Confirmed the retired generic diplomatic-treaty decision icon has zero remaining Event 12 Charter references and all 165 references use the Charter Ledger sprite name.
- Confirmed the Charter Ledger texture exists as a 32 by 32 DDS and the 62 literal Event 12 decision/category sprite names all resolve in the mod or vanilla GFX registries.
- Confirmed all eight active nature/disaster action rows are registered in the action constants, have a profile, and have player localisation.
- Confirmed the three deferred formation actions cannot become active because `africa_strange_formation_package_ready` has no setter in `common/` or `events/` and both their selectors and validators require it.

## Skipped validation and remaining issues

- No live HOI4 launch was performed because live consumer validation belongs to the user and this audit does not launch the game.
- No GUI rewrite or visual-fidelity conclusion was made because the available GUI MCP diagnostics are workspace-global and cannot isolate Event 12 findings.
- The formation package is deliberately deferred: no model, unit-template, spawn consumer, or setter for `africa_strange_formation_package_ready` exists, so actions 74 through 76 are non-executable future content rather than active release mechanics.
- No out-of-scope Event 70 Africa Gods files were audited or changed; the Event 12 high-chaos nature-disaster selectors were included.

## Simplifications, omissions, and blockers

No gameplay simplification was introduced by this audit.

The active Event 12 decision and mission release-candidate surface is otherwise complete for this bounded audit scope.

## Guidance used

Applied `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-focus-trees` for decision-focus integration, and `chaos-redux-subagents` handoff requirements.

## Release-candidate correction (2026-07-29)

The Charter Ledger DDS is present at `gfx/interface/decisions/012_africa/core/decision_012_africa_charter_ledger.dds` and is registered by the Event 12 interface definition. The earlier pending-DDS wording in this handoff is historical and is superseded for the current asset ledger.

The 165 call sites and the registered sprite remain in the decision audit scope. The final decision re-audit and registration scan report no active blocker for this surface; bounded gameplay and GUI ownership review remains a separate acceptance record.
