# Event 006 decision and mission re-audit

**Date:** 2026-07-28

**Scope:** Static re-audit of the Event 006 decision and mission matrix after the DM-58 validation-before-cost and coordinator-cleanup repairs.

**Verdict:** The DM-58 source repair remains present, but its full transaction and lifecycle behavior still needs runtime evidence.

Four manually activated deadline missions contained a source defect that made `available` default to true and therefore ended the non-selectable missions immediately instead of letting their timeout paths run.

Those four local defects are repaired in the working tree.

No files were staged or committed.

## Changed files and identifiers

- `common/decisions/006_independence_wave_form01_02_04_decisions.txt`
  - `independence_wave_form01_complete_first_integration_session`
  - `independence_wave_form02_complete_first_maritime_board`
  - `independence_wave_form04_complete_first_league_session`
- `common/decisions/006_independence_wave_rival_bloc_decisions.txt`
  - `independence_wave_rival_bloc_respond_to_invitation`

Each changed mission now declares `available = { always = no }` immediately after its manual-only activation block.

Before the patch, the absence of `available` defaulted it to always true, so an activated non-selectable mission could immediately resolve through its empty `complete_effect` path and bypass the intended deadline timeout.

After the patch, each mission remains active until its explicit completion/removal helper, cancellation trigger, or timeout effect resolves it.

## Issues sorted by severity

### P1 repaired — four deadline missions could disappear immediately

The three Form 01/02/04 first-stage deadlines are activated by `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:597-629` and can be reopened at `:816-828`.

Their intended failure effects are `independence_wave_form01_fail_integration_deadline`, `independence_wave_form02_fail_integration_deadline`, and `independence_wave_form04_fail_integration_deadline` at `:780-814`.

`independence_wave_rival_bloc_respond_to_invitation` is activated by `independence_wave_rival_bloc_issue_invitation` in `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt:454-464` and has the intended expiration helper `independence_wave_rival_bloc_expire_invitation`.

The offline Decision modding reference states that mission `available` defaults to always true and that an unset `selectable_mission` is non-selectable, so all four were vulnerable to immediately ending rather than reaching their deadline outcomes.

### P2 open — DM-58 only cancels on coordinator exit or when the whole league drops below the required member count

`independence_wave_end_active_origin` invokes `independence_wave_cleanup_reclamation_front_operation` when the departing country is the saved DM-58 coordinator at `common/scripted_effects/006_independence_wave_effects.txt:2787-2805`.

`independence_wave_unregister_league_member` instead only clears the departing country readiness fields, removes its league registry row, and calls `independence_wave_revalidate_reclamation_front_operation` at `:2226-2266`.

The revalidation helper at `:2397-2409` only cancels the shared operation if global league membership falls below the formation minimum.

Consequently, an already recorded non-coordinator DM-58 participant can leave while enough unrelated league members remain, leaving its frozen member/state/target receipt in the operation arrays until the scheduled expiry or a larger lifecycle transition cleans the operation.

This is a source-level lifecycle ambiguity rather than a safe local patch candidate because the accepted policy does not state whether any recorded participant loss must cancel the whole operation or whether the remaining witness should be recomputed without reversing claims and finite war goals.

**Recommended parent decision:** Define one policy before patching: cancel the operation on any recorded participant invalidation, or introduce a row-safe revalidation and receipt-removal transaction with an explicit rule for already issued claims and finite war goals.

### P3 open — current DM-58 source is not runtime-attested

The latest repair keeps the witness validation before both strategic and security costs, then applies the claims and finite war goals only after a valid witness in `common/decisions/006_independence_wave_decisions.txt:3554-3615`.

No current evidence proves live success, validation failure without payment, stale-witness invalidation, coordinator exit, non-coordinator exit, scheduled cleanup, save/load, dense league, no-witness, or AI behavior.

## Decision category lifecycle notes

The three formable categories keep their first-stage deadline missions manually activated and remove them during the first-stage success helpers or progression cleanup.

The rival-bloc category now retains its invitation-response deadline until acceptance, decline, invalidation cancellation, or expiration clears the local invitation state.

DM-58 is a high-chaos radical-league mission in the principal Event 006 category, authorized by `independence_wave_focus_coordinate_reclamation_fronts` at `common/national_focus/006_independence_wave_focus.txt:1930-1940` and blocked by its country flag until that focus completes.

The focus is correctly attached to `independence_wave_sponsor_further_ruptures`, writes `independence_wave_focus_reclamation_fronts_authorized` in its completion reward, and feeds the later `independence_wave_rewrite_charter_of_borders` capstone.

No focus-source patch was made.

## Mission quality notes

| Mission | Owner/category/region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| `independence_wave_form01_complete_first_integration_session` | Form 01 Congress / forming country / formable scope | Manually activated after formation or reopen; `long_treaty` deadline | Explicit first-stage ratification removes it; timeout applies Form 01 deadline failure | Low after repair because activation is explicit and `remove_mission` is used by completion and cleanup helpers |
| `independence_wave_form02_complete_first_maritime_board` | Form 02 Union / forming country / maritime formable scope | Manually activated after formation or reopen; `long_treaty` deadline | Explicit first-stage ratification removes it; timeout applies Form 02 deadline failure | Low after repair for the same reason |
| `independence_wave_form04_complete_first_league_session` | Form 04 League / forming country / league formable scope | Manually activated after formation or reopen; `long_treaty` deadline | Explicit first-stage ratification removes it; timeout applies Form 04 deadline failure | Low after repair for the same reason |
| `independence_wave_rival_bloc_respond_to_invitation` | Rival Bloc / invitation recipient / league network scope | Manually activated when invited; invitation-response deadline | Accept or decline removes the pending response; timeout expires it; invalidity cancellation declines it | Low after repair, subject to runtime validation of reinvitation and stale-target cleanup |
| `independence_wave_coordinate_reclamation_fronts` | High Chaos / radical league coordinator / distinct external state-owner pairs | Focus authorization, route, league membership, witness preflight, shared reserve, strategic and security affordability; `long` duration | Valid witness pays once then issues claims and finite war goals; timeout/failure applies crisis consequences | P2 if a recorded non-coordinator participant exits while the league remains above minimum |

## Cost and requirement clarity notes

DM-58 uses explicit strategic and security affordability checks in both `available` and `custom_cost_trigger`, plus a localized `independence_wave_cost_reclamation_front` cost line.

Its dynamic requirements are readable through the dedicated preflight custom tooltip instead of exposing the raw witness trigger to the player.

The Event 006 scan found 104 unique `custom_cost_text` identifiers and every base, `_tooltip`, and `_blocked` localisation key exists in the Event 006 English localisation set.

The four deadline repairs do not add costs because they are passive timed objectives rather than player-selected exchanges.

## AI validity and route-lock notes

The static mission scan found no explicitly selectable Event 006 mission lacking `ai_will_do`.

DM-58 has an AI weight and source-level gates for high-chaos actions, charter membership, the radical revisionist league route, the completed authorization focus, member minimum, resource reserves, and the exact preflight witness.

The focus-to-mission route lock is source-valid, but neither an MCP focus artifact nor a probability/AI sweep was available in this session, and no runtime AI result is claimed.

## Localisation and tooltip notes

No new player-facing identifier was introduced by the patch, so no localisation file changed.

The existing deadline titles, descriptions, timeout tooltips, DM-58 preflight tooltip, custom cost text, and success/failure/timeout tooltips remain the applicable player-facing surfaces.

## Cleanup and exploit-risk notes

The formable deadline missions are removed by explicit first-stage success or package cleanup helpers, and the rival-bloc response uses accept, decline, cancellation, and expiration helpers.

The DM-58 cleanup helper clears the coordinator target, shared-operation flag, readiness fields, state receipt flags, and frozen arrays, while finite war goals are intentionally left to their finite expiry.

The unresolved participant-invalidation policy is the remaining source-level cleanup and exploit-risk item because it determines whether a non-coordinator exit can leave a stale frozen row while the operation stays active.

## Meaningful validation performed

- Re-scanned all Event 006 decision files after the patch: 43 mission blocks, with no missing top-level `available`, activation, or cancellation trigger, and no explicitly selectable mission without `ai_will_do`.
- Asserted that all four patched missions have manual-only availability, a timeout duration, and a timeout effect.
- Followed every patched mission to its activation and its success/removal or failure/expiration helper.
- Re-scanned 104 Event 006 custom cost identifiers against all Event 006 English localisation files: no missing base, `_tooltip`, or `_blocked` keys.
- Reviewed the offline Decision modding, National focus modding, triggers, effects, scopes, localisation, AI, and data-structure references, plus the vanilla Afghan equipment decision/mission precedent and vanilla effect/trigger documentation.
- Reviewed the current Event 006 source-of-truth map, resume packet, DM-58 reconciliation handoff, v27 transaction audit, and decision-mission map.

## Skipped meaningful validation

No HOI4 launch or live scenario validation was performed.

No Decision/GUI or Focus MCP artifact was produced because the installed tool list exposed no `hoi4.*` callable tool in this session and no GUI source was in scope.

Runtime checks remain required for the four repaired deadline lifecycles, especially immediate activation versus timeout, explicit removal, cancellation, reactivation, and rival-bloc reinvitation behavior.

DM-58 still requires the full current runtime and AI/balance matrix listed in the source-of-truth materials.

## Remaining issues and recommended next action

The four deadline-mission source defects are repaired without a simplification or fallback.

Event 006 as a whole remains incomplete because its accepted runtime matrix, AI/balance evidence, and the P2 DM-58 non-coordinator participant-invalidation policy are still open.

No separate plan handoff was written because the only broad finding needs a parent design choice before an implementation plan can be safely authored.

