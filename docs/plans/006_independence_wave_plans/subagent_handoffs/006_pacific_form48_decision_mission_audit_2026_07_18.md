# Event 006 Pacific / FORM-48 decision and mission audit — 2026-07-18

## Verdict

**PASS — no P0/P1 issue remains in the audited decision and mission surface.**

FORM-48 runtime admission is intentionally **fail-closed** until the six shared
registry readiness flags and `independence_wave_form48_readiness_attested` are
provided by their owning implementation. This audit did not promote admission,
weaken the registry transaction, or alter package attestations.

## Scope reviewed

- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `common/decisions/categories/006_independence_wave_pacific_categories.txt`
- `common/decisions/006_independence_wave_form48_decisions.txt`
- `common/decisions/categories/006_independence_wave_form48_categories.txt`
- Pacific package constants, scripted triggers/effects, and focus-project
  concurrency in `common/national_focus/006_independence_wave_pacific_focus.txt`
- FORM-48 constants, registry transaction/admission, postformation effects,
  high-chaos reason-4 publication, and English Event 006 localisation coverage.

No decision-owned scripted GUI exists in this surface, so GUI inspection/render
was not applicable. No advisor icon, sprite, portrait, flag, focus DDS, or GFX
file was created or edited.

## Issues, sorted by severity

### Resolved — P1: FSM government projects could become obsolete mid-timer

The four exclusive FSM government settlement decisions had an initial capital
control requirement but no cancellation path. If the capital fell, the package
ended, or another authoritative route closed the government slot during the
timer, their guarded completion could silently no-op after the player had paid.

Changed identifiers:

- `should_cancel_independence_wave_fsm_government_settlement`
- `independence_wave_fsm_ratify_federal_council_compact`
- `independence_wave_fsm_confirm_traditional_leaders_council`
- `independence_wave_fsm_adopt_inter_island_constitution`
- `independence_wave_fsm_accept_protected_ocean_mandate`

Before: an invalidated settlement could remain active until expiry and have no
meaningful resolution. After: it cancels immediately. If no rival route has
completed, the existing project-failure consequence applies; if a rival route
has already filled the slot, it closes without a second, erroneous penalty.

### Resolved — P1: island delegation could become FORM-48-ready after capital loss

`independence_wave_haw_authorize_pacific_delegation` and
`independence_wave_fsm_ratify_autonomous_federation_mandate` required control of
the capital only when started. They could otherwise finish after the capital was
lost and set the strict-ledger delegation readiness flag.

Before: a lost-capital project could report a delegation as ready. After: both
decisions cancel on package loss or capital loss and use the existing project
failure effect while their package remains valid. This preserves the strict
FORM-48 founding ledger.

### Resolved — P2: FORM-48 cost gates required more than their displayed price

FORM-48 uses strict `>` resource checks. Directly comparing those checks with a
cost constant made the player need 21 command power to spend 20, 21 convoys to
spend 20, and similarly one additional equipment/fuel unit. Vanilla decision
precedent uses a predecessor threshold for strict availability checks.

Added centralized `*_availability_threshold` constants and changed the five
FORM-48 payer triggers to use them:

- `can_pay_independence_wave_form48_carrier_convoy_cost`
- `can_pay_independence_wave_form48_carrier_procurement_cost`
- `can_pay_independence_wave_form48_carrier_basing_cost`
- `can_pay_independence_wave_form48_member_convoy_cost`
- `can_pay_independence_wave_form48_member_procurement_cost`
- `can_pay_independence_wave_form48_member_basing_cost`

The displayed and deducted costs remain unchanged; exactly that amount now
permits the decision. Civilian-factory availability was intentionally left
unchanged because it is a sustained project-capacity reservation rather than an
instant, deducted resource.

### Deliberate gate, not an audit defect

`has_independence_wave_formable_commit_readiness` still requires all six shared
readiness flags plus `independence_wave_form48_readiness_attested`. The FORM-48,
Pacific-package, and registry effect surfaces contain no setter for any of
those flags; FORM-48 only clears readiness during registration/cleanup. This
is the required fail-closed state, not a route-lock bug.

## Decision-category lifecycle notes

### Pacific founding categories

- **HBX coastal command, HAW island authority, and FSM Micronesian federation**
  become visible only for their exact country package. Each starts with a
  240-day non-selectable founding mission whose success requires the relevant
  pressure/authority threshold and capital control. Its timeout and invalidation
  paths have named failure consequences.
- Timed HBX/HAW/FSM projects set no free progress: they spend varied strategic
  or administrative resources on start, serialize through one active-project
  predicate, and complete into explicit pressure, ledger, route, or delegation
  state.
- HBX and HAW have paired focus/decision projects with reciprocal locks:
  completed/in-progress focuses prevent the decision, while an active decision
  prevents the focus. HAW's unpaired mandate focuses have no competing decision.
  FSM deliberately keeps its owning focus tree and serializes its four route
  settlements through the package active-project predicate.
- Pacific origin cleanup removes active projects/missions and calls the narrow
  FORM-48 origin cleanup only for the exact Pacific member. It does not scan
  countries or erase unrelated Event 006 state.

### FORM-48 categories

- **Autonomous invitations** are visible only to the pending human HAW/FSM
  target. Acceptance spends its member convoy cost, locks the transaction and
  reply, and writes consent through the shared resolver. Withholding has no
  resource charge because it is the sovereign refusal choice and applies its
  immediate ledger trade-off. AI is blocked from the human-only responses.
- **Federal compact** is visible only to the postformation carrier or an active
  member. HBX/PFX may start one stage-specific paid carrier project. The helper
  clears prior replies, sets exactly one active-cycle flag, and explicitly
  activates its mission. Member fulfil/withhold decisions use one response lock
  per stage. Dissolution is available on high strain, a departed member, or an
  unbound compact and calls the centralized cleanup.
- Carrier cycle success resets replies and advances the stage; timeout and
  withhold effects change the host/member/league ledgers and strain. A cycle
  repeats only after the defined stage rotation, not as a passive store or an
  equipment/unit reward loop.

## Mission quality notes

| Owner/category/region | Requirement and duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- |
| HBX / Coastal Command / California | Stable coastal command and controlled capital; 240 days | Marks the founding mandate resolved; timeout or invalidation applies the named failure state | None: one founding mission and resolved flag |
| HAW / Island Authority / Hawaii | Shipping-security threshold and controlled capital; 240 days | Resolves island mandate; timeout or invalidation applies failure | None: one founding mission and resolved flag |
| FSM / Micronesian Federation / Micronesia | Inter-island authority threshold and controlled capital; 240 days | Resolves federation mandate; timeout or invalidation applies failure | None: one founding mission and resolved flag |
| PFX/HBX / Federal Compact / Pacific | Both sovereign members fulfil the active convoy, procurement, or basing obligation; 180/240/210 days | Success advances the cycle and public ledgers; timeout produces a material failure and may dissolve at extreme strain | None: one active-cycle flag, response locks, and explicit mission removal on cleanup |

## Cost and requirement clarity

- The Pacific surface is not a political-power store. Its short/standard/long
  projects use existing administrative, diplomatic, security, or island
  strategic cost helpers; island strategic projects require stability, war
  support, command power, manpower, and convoys instead of impossible factory
  costs.
- FORM-48 carrier actions vary among command power, fuel, convoys, infantry
  equipment, support equipment, and sustained civilian-factory capacity.
  Member obligations use their own smaller, material costs. All player-facing
  custom cost references resolve in Event 006 English localisation.
- No audited decision/effect adds political power, grants a free unit, creates a
  unit, or returns spent equipment/resources. All FORM-48 `*_spend` constants
  referenced by stockpile/command/fuel effects are negative.

## AI validity and route-lock notes

- Founding missions and projects have explicit AI weights; high-risk delegation
  and patron choices are conditional on collapse/threat/patron state. Human
  FORM-48 invitation choices have blocked AI weights.
- FSM settlement visibility, availability, the new cancellation trigger, and
  route-selection effects all enforce the one-route government slot. No closed
  or completed route can be selected again.
- FORM-48 admission validates exact packages, founding ledger membership,
  consent, anchors, capital control, active Event 006 origin, selected family,
  and readiness. It does not use an invalid/dead generic country target or a
  world scan. Generic human invitation categories explicitly exclude FORM-48.

## Localisation, tooltip, cleanup, and exploit notes

- All 98 `name`, `desc`, `custom_cost_text`, and `custom_effect_tooltip`
  references collected from the Pacific and FORM-48 decision files resolve in
  `localisation/english/006_independence_wave*_l_english.yml`.
- Long raw availability logic is kept behind custom cost/tooltip helpers rather
  than exposed directly to the player.
- FORM-48 cleanup removes all three missions, all owned decisions and ideas,
  active-cycle/reply flags, values, and transaction-owned reciprocal access or
  guarantees. The bounded member ledger is checked against the same carrier
  generation before cleanup affects a relationship.
- `fire_only_once = no` is appropriate for the three stage missions: response
  flags and the active-cycle flag serialize recurrence, while cycle results
  adjust ledgers rather than farming equipment, cores, war goals, or units.
- Reason 4 is wired from FORM-48 postformation only when the durable radical
  league predicate passes. It sets
  `independence_wave_danger_selected_reason` to
  `hidden_formable_bloc_center` and calls the one-shot danger publisher; the
  publisher retains the super-event guard.

## Files changed by this audit

- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`
- `common/script_constants/006_independence_wave_form48_constants.txt`
- `common/scripted_triggers/006_independence_wave_form48_triggers.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_pacific_form48_decision_mission_audit_2026_07_18.md`

No commit was created. The first four files were already untracked concurrent
Event 006 work in this dirty workspace; no unrelated change was reverted.

## Meaningful validation

- `python .tools/audit_event6_allocator.py` passed: 149 publishers, 126
  automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable
  packages, and the expected 3/4/5/7/10 automatic counts.
- Checked brace balance across 12 Pacific/FORM-48 decision, category, focus,
  constant, trigger, and effect files; all balances matched.
- Confirmed the four FSM government settlement ids carry the shared cancellation
  helper and failure behavior; verified HAW/FSM delegation cancellation includes
  loss of capital.
- Confirmed all FORM-48 strict resource availability tests use centralized
  predecessor thresholds matching the unchanged negative payment constants.
- Searched the audited scope for periodic world actions and country scans; none
  were present. Searched for political-power stores, positive resource returns,
  and unit creation; none were present.
- Checked the direct FORM-48, Pacific package, and registry setup surfaces for
  setters of the six shared readiness flags or FORM-48 attestation; none exist,
  preserving fail-closed admission.

## Skipped validation and remaining issues

- A narrow `hoi4.event_inspect` lint request against the Pacific decision file
  could not produce an artifact because the MCP workspace returned
  `ARTIFACT_STORAGE_LIMIT` (workspace
  `mod_chaos_redux_ea3b2d67c2c0`; no diagnostics/artifacts returned). This is a
  tooling-storage limitation, not a substitute for gameplay review.
- Full live admission/postformation validation cannot be reached in this tranche
  because the required readiness attestations deliberately remain unset. They
  must stay unset until their owning implementation is accepted; this audit did
  not introduce a fallback or bypass.
- No broad design handoff was written: the audited system already has distinct
  lifecycle, cost, failure, and cleanup branches, and all findings were small,
  local fixes.

## Guidance used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop` (depth review only; no expansion was needed)
