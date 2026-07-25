# Event 006 decision and mission matrix re-audit — 2026-07-26

## Verdict

**HOLD — one high-severity DM-58 availability/preflight defect remains.**

The current Event 006 decision surface retains the expected DM-01 through DM-62 markers, the treasury capstone decision, and the arbitration refusal action.

No gameplay, localisation, GUI, attestation, or registry source was edited by this audit.

## Issue list

### High — DM-58 candidate legality is evaluated in the wrong scopes and does not prove distinct usable fronts

**Files and identifiers:** `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `is_independence_wave_reclamation_front_member_candidate`, `has_independence_wave_reclamation_front_preflight`; consumer `common/decisions/006_independence_wave_decisions.txt`, `independence_wave_coordinate_reclamation_fronts` (DM-58).

Inside `any_country -> any_state -> owner`, `ROOT` is the country activating DM-58 rather than the iterated candidate member, while `PREV` at the `owner` level is the state rather than that member country.

The added `tag`, war, `can_declare_war_on`, and existing-wargoal checks therefore do not consistently validate the member that the preflight counts.

The count also admits several candidate members whose only legal fronts belong to the same owner, while the execution effect deliberately permits only one target owner.

The execution path safely rolls back claims, flags, arrays, and staged wargoals when it cannot assemble the required member count, so this is not a material-resource duplication path.

It can nevertheless let a player or the high-weight AI begin a mission which necessarily collapses into the league-crisis failure branch, contrary to the accepted DM-58 action contract.

**Bounded repair:** rewrite only the candidate preflight helper to carry the iterated member explicitly through the nested scopes and test legality against the current owner, not `ROOT`/state `PREV` aliases.

Add a non-mutating distinct-owner feasibility check where Clausewitz scope permits it; if a fully injective match cannot be expressed safely in a trigger, keep the execution rollback as the authority but change the post-selection mismatch outcome to a clear partial/no-op result rather than the strategic league-crisis failure.

Do not add a new planner, GUI, or broad reclamation system in this repair.

## Category lifecycle notes

- League, high-chaos, client, host, formable, registry, and scenario action families remain route-gated through activation/visible/available checks and their existing scripted helpers: **PASS**.
- Focus integration is restored for DM-58: `independence_wave_focus_coordinate_reclamation_fronts` grants `independence_wave_focus_reclamation_fronts_authorized`, and DM-58 requires it: **PASS**.
- DM-55 remains a selected-formable consumer with no fallback tag path: **PASS**.
- DM-57 continues to consume and clean its sponsorship queue through its existing resolver: **PASS**.
- Scenario controls remain non-AI utility controls and are not reachable as ordinary AI actions: **PASS**.

## Mission quality notes

| Mission | Owner/category/region | Requirement and duration | Success/failure/duplicate risk |
|---|---|---|---|
| DM-58 `independence_wave_coordinate_reclamation_fronts` | Radical revisionist league member; league/high-chaos action | Charter-compliant active member, focus authorisation, reserves and strategic/security costs; selectable 180-day mission | Success stages compatible members, flags a coordinated front, and records the revisionist action. Timeout/cancel/failure clear the mission-facing state, and resolver rollback removes staged claims/wargoals. **HOLD:** availability can count incorrectly scoped or same-owner candidates, producing avoidable failure/crisis. |
| DM-57 sponsorship resolution | League/foreign-service action | Existing queue and route gates | Resolver consumes queue entries and removes stale state; no replay loop found. |
| Treasury public works capstone | Economic high-chaos decision | Focus-gated dynamic public-works cost and finite cooldown | Completion and cooldown cleanup are present; no free equipment/factory loop found. |

## Cost, requirements, AI, and player clarity

- The audited dynamic-cost decisions retain their paired custom cost trigger/text surfaces and effect descriptions: **PASS**.
- DM-58 now has completion, failed, and timeout custom-effect tooltips, and its focus describes the unlock: **PASS**.
- Existing AI gates keep normal route, membership, host, target, and formable decisions behind their corresponding eligibility helpers: **PASS**, except that DM-58 inherits the preflight false-positive risk above.
- No missing decision-owned GUI button behaviour was found in this read-only pass. The status-window GUI is presentation-only for this audit; the prior inspection artifact remains `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20cb8cd69694814ec9d0d4db09236a796159dbe82ccf2c4ef13ceb3c459ddabe/3fd9893a4ce91ccad685c3b2a9b6523494a8c4e7832081995873275cbeceb2bf/gui-inspect.ba4323bf16cb4312.json`.

## Cleanup and exploit-risk notes

- DM-58 execution uses staged-member/state/owner arrays and the reclamation rollback helper; it removes claimed-state markers and finite wargoals on an insufficient completed front: **PASS**.
- League member removal and league phase transitions call the reclamation revalidation/cleanup paths at the current lifecycle boundary: **PASS**.
- No political-power, unit, equipment, core, or war-goal farming loop was identified in the audited action map.
- The only remaining exploit-adjacent behaviour is the DM-58 false-positive launch described above; it wastes a selected mission and applies its intended failure crisis, rather than granting a benefit.

## Validation and boundary

This was a static matrix re-audit after `d8cc2ec99`, `c242def71`, and the DM-58 source repair.

Reviewed the accepted decision-mission map, current decision/trigger/effect/focus call sites, prior DM-58 repair handoffs, required offline decision/scope/effect references, and vanilla decision/mission precedents.

No live-game run was performed, and no broad source patch is recommended until the nested preflight scope relationship is corrected.
