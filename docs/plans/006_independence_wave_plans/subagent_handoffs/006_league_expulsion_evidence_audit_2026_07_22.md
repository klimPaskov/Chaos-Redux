# Event 006 league-expulsion evidence audit

Date: 2026-07-22
Audited baseline: `60657ac5f698df549079156ec34280673a502e8c`
Scope: DM-42, DM-43, DM-44, DM-60, DM-61 and the factual-expulsion ground
writers, constants, triggers, on-actions, localisation, costs, AI, cleanup,
achievement writer, and decision map. This is a narrow decision/mission audit,
not a completion claim for Event 006.

## Result

Three local defects were patched. The remaining material finding is that
DM-44's `rescue_abandonment` evidence is not factual under the current timed
decision lifecycle: it records an abandonment after aid and a guarantee have
already been delivered, without an action that withdraws or refuses a
continuing obligation. The mutual-defence charter gate is now present, but it
does not make that ground truthful. It needs a parent-owned design decision,
not a cosmetic script fix.

## Issue list, ordered by severity

### High — unresolved: DM-44 can call a completed rescue an abandonment

`independence_wave_dispatch_mutual_defense_aid` immediately spends and sends
the stated infantry/support equipment and issues the guarantee. The only
ground writer is then reached from DM-44's cancellation path when the target
is still at war. A later client-route lock, state-owner change, or other
validity change can therefore produce `rescue_abandonment` even though the
rescuer did provide the aid. Normal expiry succeeds while the target remains
at war.

Recommended parent follow-up: either replace this ground with a factual,
explicit withdrawal/refusal action whose completion changes a maintained
obligation, or remove the writer from the accepted-ground set. Do not describe
the current cancellation as an abandonment in player-facing text.

### High — unresolved: state-targeted timers do not persist their selected country

DM-42, DM-43, DM-44, and DM-60 obtain the target from `FROM.owner` in their
completion/cancellation effects. `FROM` is correctly a state scope for a
state-targeted decision, but ownership may change during its timer. A captured
capital can redirect its resolution to a different active country or cause a
misleading cancellation outcome.

Recommended parent follow-up: store the chosen country scope on the decision
owner at activation, require that it is still the owner of the selected state
on resolution, use that stored pointer for effects, and clear it in every
resolve/cancel/origin-cleanup path. This crosses four existing decision
lifecycles, so it was recorded rather than partially patched.

### Medium — unresolved: “unauthorized war” currently means every offensive war

The event-driven `on_war_relation_added` writer correctly receives `ROOT` as
attacker and `FROM` as defender. It has the defensive-congress and
mutual-defence gates, but there is no positive authorization flag, approval
decision, or doctrine exception. In practice every eligible offensive war is
called unauthorized. Confirm that this is the intended defensive-charter rule,
or add a separate, factual authorization surface before preserving the label.

### Low — resolved: coup civil-war sides were inverted

`independence_wave_start_sponsored_member_coup` selected an opposing revolt
ideology but passed that same ideology as `ruling_party`. Vanilla documentation
defines `ideology` as the revolter and `ruling_party` as the party remaining in
the original country. The helper now passes the target government's actual
party as `ruling_party` for fascist, democratic, and communist targets.

### Low — resolved: stale arbitration responses could create evidence after route loss

`is_independence_wave_binding_arbitration_refusal_target` now also requires a
charter-compliant member and the arbitration pillar. A pending request on a
former member or after the pillar is gone cannot generate a purported charter
refusal.

### Low — resolved: country localisation was invoked from a state target

DM-61 now uses `[FROM.owner.GetNameDef]`; `FROM` is a state scope, so the
previous `[FROM.GetNameDef]` country accessor was not a truthful or supported
target description.

### Low — resolved: witness documentation named the wrong persistence mechanism

`common/scripted_effects/006_independence_wave_effects.md` now identifies the
witness as the persistent country-scope variable used by the helper, rather
than an event-target pointer. That matches the implementation and explains why
the scope survives across decisions.

## Decision category lifecycle notes

| Surface | Owner and category | Lifecycle | Cleanup and duplicate control |
| --- | --- | --- | --- |
| DM-42 `independence_wave_seek_external_recognition` | recognised, charter-compliant League member; network category | 180-day capital-targeted recognition effort | active-crisis guard prevents overlapping Event 006 crises; cancellation applies its stated failure branch; state-owner persistence remains unresolved |
| DM-43 `independence_wave_request_binding_arbitration` / refusal response | requesting member and counterpart; network category | 120-day bilateral state-targeted request, then a target-side response | requester/date/pending state is cleared on success, cancellation, response, and origin cleanup; refusal now requires the live pillar/member route |
| DM-44 `independence_wave_dispatch_mutual_defense_aid` | rescuer and threatened member; network category | 75-day state-targeted aid commitment | aid is paid/sent on activation; cancellation awards outcome or records the unresolved false-abandonment ground; duplicate risk is bounded by active-crisis checks |
| DM-60 `independence_wave_call_charter_expulsion_vote` | lawful charter authority; leader category | 120-day capital-targeted vote | successful verified resolution expels and marks the case resolved; failed/cancelled vote uses its loss path; state-owner persistence remains unresolved |
| DM-61 `independence_wave_sponsor_member_coup` | eligible League member; network category | immediate targeted decision with major cooldown | starts a single target civil war and records the sponsor ground; target cannot already be at war/civil war; it has no separate timed failure branch |

No `mission = {}` blocks exist in this tranche. The matrix's mission wording
maps to timed decisions using `days_remove`, so the timers above are the
relevant mission-quality lifecycle.

## Mission-quality notes

| Id | Owner/category/region | Requirement and duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| DM-42 | compliant member, network category; target capital | low-recognition League member; 180 days | recognition outcome / cancellation loss | low, except target-country owner transfer |
| DM-43 | compliant requester, network category; counterpart capital | reciprocal claims and live arbitration charter; 120 days | claims settled / refusal or cancellation consequence | low after pointer cleanup, except state-owner transfer |
| DM-44 | compliant rescuer, network category; threatened capital | live mutual defence, target at war, material stockpile; 75 days | equipment/guarantee and relief / cancellation branch | low mechanically; high semantic risk in the false-abandonment branch |
| DM-60 | lawful leader, leader category; accused capital | live recorded unresolved ground and authority ledger; 120 days | expulsion and achievement marker / vote-collapse losses | low after resolved marker, except state-owner transfer |
| DM-61 | compliant sponsor, network category; target capital | peaceful active non-client member with no civil war; immediate | civil war and factual coup evidence / unavailable if requirement fails | low; major cooldown and no repeated target loop |

## Cost and requirement clarity

- DM-42 and DM-43 use existing diplomatic-capacity material costs. DM-43's
  response has the matching diplomatic-light cost and a live requester check.
- DM-44 visibly requires command capacity, train/convoy capacity, and the
  infantry/support stockpile it sends. Its completion effect transfers the
  equipment, rather than merely displaying a custom cost.
- DM-60 uses the strategic bundle: stability, war support, command capacity,
  transport capacity, and spare civilian-factory availability. Its completion
  rechecks both authority and the unresolved factual case before expulsion.
- DM-61 pays the security-standard manpower, army-XP, infantry-equipment, and
  support-equipment bundle before the civil-war helper. It grants no sponsor
  units or political-power exchange.
- The cost helpers use strict resource comparisons before payment, matching the
  established Event 006 helper convention. The player-facing custom tooltips
  match the consumption paths inspected here.

## AI validity and route-lock notes

- DM-60 targets only active, non-client members with an unresolved factual
  case and verifies the authority ledger at resolution.
- DM-61 excludes targets already at war or in a civil war. Its AI base weight
  is very low, with the bounded radical-route modifier; it cannot farm units
  because the civil war partitions the target's existing country.
- The annexation and war writers use their documented on-action scopes:
  `on_annex` records the winner before the victim disappears, and
  `on_war_relation_added` records only the attacker while excluding civil wars.
- The event-driven writers require the active Event 006 route and appropriate
  charter pillars. The new arbitration gate prevents a closed route from being
  used as evidence. The new mutual-defence gate prevents DM-44 evidence when
  that pillar is absent, though it does not resolve the factual-abandonment
  defect.

## Localisation, cleanup, and exploit notes

- Ground display uses the target country (`[FROM.owner.GetNameDef]`) and the
  dynamic ground text. No raw trigger chain is exposed in the player-facing
  DM-60 description.
- Expulsion resolution marks a case resolved and clears its active-case flag;
  historical ground/count/witness data is deliberately retained. Generation
  reset and Event 006 origin termination call the case cleanup helper.
- Arbitration request state is cleared on all normal success, cancellation,
  response, and origin-end paths. A physically stale marker is non-actionable
  because the response trigger now requires a live compliant requester and
  pillar.
- There are no daily, weekly, or world-iteration on-actions in this tranche.
  Annexation and offensive-war evidence is written only in event-driven hooks.
- No political-power store, free-unit loop, equipment farming, war-goal spam,
  or core-grant loop was found. The only material transfer, DM-44 aid, removes
  the stated stockpile from the rescuer before transferring it.

## Rival-bloc boundary

The existing `independence_wave_split_league_after_expulsion` helper only
changes Event 006 phase flags. It has no call site, faction template,
membership contract, or cleanup owner. A genuine post-expulsion rival bloc is
still omitted and must remain an explicit follow-up rather than a cosmetic
phase claim.

## Patch handoff

Changed files:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.md`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- this handoff

Changed identifiers and before/after behaviour:

| Identifier | Before | After |
| --- | --- | --- |
| `independence_wave_start_sponsored_member_coup` | revolt ideology was also supplied as the original country's ruling party | original ruling party matches the target government's party; revolt remains the opposing ideology |
| `is_independence_wave_binding_arbitration_refusal_target` | a stale pending request could be refused after membership/pillar loss | response is available only to a compliant member while arbitration remains charter law |
| DM-44 cancellation evidence branch | could record rescue abandonment without confirming mutual-defence law | requires the mutual-defence pillar; timing truthfulness remains unresolved |
| `independence_wave_sponsor_member_coup_desc` | treated a state target as a country for `GetNameDef` | names the target state's owner country |
| `006_independence_wave_effects.md` witness output | called a scoped variable an event target | documents the actual persistent country-scope variable |

## Validation and limits

- Consulted the offline wiki and vanilla documentation/precedents for
  state-targeted decisions, decision cancellation, scope variables,
  `on_annex`, `on_war_relation_added`, script constants, and
  `start_civil_war` semantics.
- Compared the coup helper with vanilla civil-war call sites and verified the
  corrected `ideology`/`ruling_party` roles against the effects documentation.
- Inspected each factual writer, all affected target/cancel branches, custom
  cost helper call sites, achievement writer call site, decision-map rows, and
  the Event 006 on-action file. Targeted searches confirmed no periodic
  on-action was introduced in this tranche.
- No live HOI4 runtime parse or save-state execution was available in this
  bounded audit, so dynamic target-owner transfer, decision visibility, and
  civil-war runtime partitioning remain source-reviewed rather than exercised.

## Parent follow-up

1. Decide whether DM-44 gains a factual withdrawal/refusal lifecycle or loses
   `rescue_abandonment` as an expulsion ground.
2. If these timed state-targeted decisions remain, add persistent selected
   country pointers and owner-stability checks across DM-42/43/44/60.
3. Confirm whether all offensive wars under the defensive charter are intended
   to be unauthorized; otherwise design the missing authorization state.
4. Keep the rival-bloc gap in the Event 006 completion report.
