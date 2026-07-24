# Event 012 Africa decision and mission audit handoff

## Scope and status

This audit covered `common/decisions/012_africa_decisions.txt`, `012_africa_priority_member_decisions.txt`, `012_africa_rsa_decisions.txt`, their categories, and the direct Event 12 action, AI, trigger, effect, constant, and localisation dependencies.

No decision-owned scripted GUI surface was changed or rendered because this scope uses standard decision categories and target arrays rather than a scripted GUI interface.

## Matrix coverage

The 102 accepted matrix keys exactly match the 102 `africa_action` constants, the 102 action profiles, the 102 action-specific validation branches, and the 102 full, partial, and failure disposition records.

Every direct decision helper call from the three audited decision files resolved to a scripted trigger or effect.

All 207 audited decision and mission IDs have a name and description in the Event 12 localisation files.

All 68 custom trigger or effect tooltip IDs referenced directly from the three decision files resolve in Event 12 localisation.

## Patched findings

### Medium — seven matrix actions did not charge the commitments described by their accepted cost rows

`africa_prepare_action_profile` now adds existing shared quote components without adding a new cost system.

- `offer_federal_charter` uses political power, civilian capacity, and stability for constitutional administration, representation, and the domestic concession.
- `guarantee_regional_representation` uses political power and civilian capacity for the concession and appointment capacity.
- `continental_procurement_contract` uses political power, civilian capacity, and trains for treasury authority, contracting capacity, and transport.
- `resource_sovereignty_review` uses political power and civilian capacity for political capital and compensation administration.
- `charter_development_fund` uses political power and civilian capacity for treasury share and project administration.
- `consult_oracle_network` uses political power, support equipment, and stability for liaison supplies and ecological concession.
- `ratify_confederal_emergency_action` uses political power, support equipment, and civilian capacity for diplomatic staff, shared compensation, and ratification administration.

The existing quote still applies target scale, selected-state scale, burden, pressure, active-action, confidence, access, war, and route modifiers before payment.

Changed file: `common/scripted_effects/012_africa_action_effects.txt`.

### Medium — priority-member post-settlement actions could reward indefinitely after maturity

`africa_priority_member_can_run_post_settlement_action` now requires absent progress or progress below `constant:africa_priority_member_progress.maximum`.

Before the patch, the sixteen package-specific post-settlement decisions remained available after their shared effect clamped progress at the maximum and still granted their package payload every cooldown.

After the patch, the four normal 25-point advances remain available, while further use is blocked at maturity.

Changed file: `common/scripted_triggers/012_africa_priority_member_triggers.txt`.

### Low — custom cost text lacked blocked and explanatory variants

`africa_selected_action_dynamic_cost` now has `_blocked` and `_tooltip` variants.

The five RSA custom costs now each have a `_tooltip` variant: `africa_rsa_relief_cost`, `africa_rsa_regional_request_cost`, `africa_rsa_citizenship_cost`, `africa_rsa_sovereignty_guarantee_cost`, and `africa_rsa_exile_recovery_cost`.

Changed files: `localisation/english/012_african_union_l_english.yml` and `localisation/english/012_africa_rsa_l_english.yml`.

## Decision category lifecycle notes

`africa_charter_council_category` appears only for the current Event 12 host.

Each action-family category appears only when its family is selected and its route or phase gate is met.

High-chaos, Scramble, world-order, constitutional, post-unification, recovery, and restoration categories each carry their relevant evolution, unification, constitutional, failure, or Congress visibility gate.

The selected-country workflow saves one bounded target, recalculates the quote, validates again at launch, spends once, and creates one generation-safe action record.

An active record blocks a duplicate target, reserves action capacity, marks selected project states, and assigns a 30-day target cooldown during cleanup.

## Mission quality notes

| Mission family | Owner and category | Requirement and duration | Success, failure, and duplicate handling |
| --- | --- | --- | --- |
| Shared action missions | Current Event 12 host in `africa_charter_council_category` | Active target record plus the matching short, medium, long, or epic flag; host-initialised 60, 120, 240, or 540 day duration | Timeout resolves the shared full, partial, or failure outcome. Invalidation cancels through the same cleanup. Active target records, capacity reservations, project flags, and cooldowns prevent duplicates. |
| Priority-member withdrawal | Registered priority member in `africa_priority_member_category` | Departure or rival relationship and `africa_priority_member_withdrawal_in_progress`; 90 days | Timeout completes peaceful withdrawal. Relationship recovery or notice removal cancels and clears withdrawal state. |
| RSA first proof | Continental Coalition in `africa_rsa_crisis_category` | Civil-war corridor security; `africa_rsa_first_proof_days` | Completion records the proof. Timeout or invalid coalition/civil-war state fails the proof. The active civil-war route is the ownership and duplicate gate. |
| Scramble phase windows | Current host in `africa_charter_council_category` | Exact active Scramble phase; phase-specific constant duration | Timeout advances or resolves the phase. A phase change cancels its old window, preventing overlapping windows. |

## Cost and requirement clarity notes

The shared action quote is dynamic and payment checks the same political power, command power, manpower, equipment, fuel, capacity, stability, and war-support values shown to the player.

The matrix cost pass removed every action profile with fewer than two cost components.

Priority-member force reinforcement is not a free-unit loop: its availability requires manpower and the shared effect deducts `constant:africa_priority_member_manpower.force_spend` before applying the force payload.

Priority-member mechanics remain political-power primary, but they are bounded by progress and cooldown. The post-settlement loop is now similarly bounded.

## AI validity and route-lock notes

Actions 77 through 92 have a bounded live AI dispatcher with target-specific checks for usable, non-dead targets, applicable Scramble/world-order flags, war capability where needed, and selected-state control for world-region administration.

The AI profile and MTTH context registry evaluates all families, but the live dispatcher selects only actions 77 through 92.

The matrix selectors and launch decisions for actions 1 through 76 and 93 through 102 are intentionally AI-disabled in the decision file, and no equivalent bounded dispatcher was found in this audit scope.

This is the primary unresolved issue: AI-controlled Event 12 hosts do not autonomously enact the opening, regional, integration, economy, diaspora, rival-bloc, high-chaos, constitutional-crisis, post-unification, recovery, or priority-promotion action rows through the shared system.

Recommended parent follow-up: design one bounded dispatcher family for these rows using the existing profile registry, target roster, quote/payment check, and action-specific validation. Do not simply enable the player selectors for AI because they require target selection and state context.

## Localisation and tooltip notes

The Event 12 decision and mission text is complete for the audited IDs, and the patched custom cost keys have normal, blocked, and tooltip forms.

The shared dynamic cost string still displays zero-value components. A nonzero-only breakdown would require a separate scripted-localisation composition and UI review, so it was not introduced as a local audit patch.

## Cleanup and exploit-risk notes

Shared action cleanup clears the active mission, target and state arrays, active-count reservation, duration flags, project locks, and action quote state before applying the target cooldown.

The shared action system applies full, partial, and failure disposition flags for every matrix row. Eight partial and six failure rows receive additional bespoke semantic branches, while the remainder use their family-level partial or failure semantics. This is not a missing cleanup path, but it remains a content-depth risk if action-specific consequences are required beyond the accepted shared family effects.

## Validation performed

Static coverage confirmed exact 102-of-102 matrix, constant, profile, validation, and full/partial/failure disposition coverage.

Static helper resolution found 111 direct decision helper calls and no unresolved helper identifier.

Static localisation coverage confirmed 207 decision or mission names and descriptions plus 68 custom tooltip identifiers with no missing Event 12 key.

Static custom-cost coverage confirmed normal, blocked, and tooltip localisation for the shared action cost and all five RSA custom costs.

Static cost coverage confirmed no action profile has fewer than two declared quote components after the patch.

Static exploit coverage confirmed all sixteen priority-member post-settlement decisions use the newly capped shared trigger.

Meaningful validation skipped: no game runtime or decision GUI render was available in this subagent environment, so the dynamic quote values and mission activation were reviewed structurally rather than exercised in a live scenario.

## Remaining issue and parent handoff

The bounded autonomous AI gap for actions 1 through 76 and 93 through 102 remains unresolved and requires a planned extension rather than a local patch.

No fallback or simplification was introduced by this audit patch.
