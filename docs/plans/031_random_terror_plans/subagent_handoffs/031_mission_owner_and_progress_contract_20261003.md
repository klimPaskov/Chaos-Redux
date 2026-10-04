# Event 031 mission owner and progress contract audit

## Disposition

Read-only source audit; implementation remains parent-owned and unresolved.
The user-designated accepted basis is `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md` and its dedicated `031_random_terror_decision_mission_prompt.md`.
This handoff recommends a bounded ownership/progress repair within those accepted mission contracts; it does not authorize a new mechanic, GUI, or balance target.

No gameplay or asset source was changed, no game was launched, no logs were requested, and no commit was created.
The shared worktree already contains unrelated dirty files; they were left untouched.
Current Event 031 source hashes are listed below.

## Executive finding

Yes.
Country A can consume, resolve, or clear Country B's Event 031 mission subject.
All eight mission definitions use generic state flags such as `random_terror_containment_mission_subject`; their `any_state` predicates and `every_state` completion/cancellation/timeout loops are not limited to the mission country.
The offline scope reference defines `any_state` as checking any state in the game and `every_state` as iterating every state.
A country flag such as `random_terror_mission_slot_1` identifies the country holding a slot, but does not bind that slot to a particular state receipt.

The cross-country failure is concrete: if A has a matching mission slot and B has the corresponding generic state subject, A's mission can see B's state in activation/availability; if it resolves or cancels, its generic `every_state` cleanup also clears B's subject.
State-local pressure/activity/outcome effects can run on B's target while country-level outcome flags are written to A.
For mission types sharing one slot, an unrelated country-level slot flag plus another country's generic subject can also satisfy a second mission's activation, so the three-slot design does not by itself guarantee a maximum of three active missions per country.

Do not repair this by adding `is_owned_by = ROOT` or replacing every subject with an owner check.
Several accepted targets are intentionally foreign-owned or foreign-controlled.
The receiver of the mission—not necessarily the state's owner, controller, or the decision's original `ROOT`—must key the durable receipt.

## Severity-ranked findings

### High — Generic state receipts are world-visible and world-clearable

`common/decisions/031_random_terror_missions.txt` defines eight generic subjects and repeatedly searches them with `any_state` and clears them with `every_state`: containment 19–89, transport 96–168, corridor 175–242, capital 248–320, retake 327–397, civil authority 404–469, hostage 478–540, and uprising 549–617.
In particular, the activation, success, cancel, complete, and timeout blocks all read or clear the same unkeyed state flag.

The scope evidence is explicit: `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 382–392 (`any_state` is always usable; `any_owned_state` and `any_controlled_state` are the country-limited alternatives) and line 528 (`every_state` is always usable), SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.
Installed `documentation/triggers_documentation.md`, lines 1612–1681 and 4827–4836, SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE33B27C2D1DE29`, and installed `documentation/effects_documentation.md`, lines 4155–4167, SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`, corroborate the scope types and state-flag operations.

Affected source includes all mission lifecycle blocks in `common/decisions/031_random_terror_missions.txt`, the eight decision setup callers in `common/decisions/031_random_terror_decisions.txt` (lines 74–89, 400–451, 551–620, 1098–1160, 1321–1445, 1619–1681, and 3149–3243), and the resolver/cleanup helpers in `common/scripted_effects/031_random_terror_effects.txt` (lines 3580–3960 and 4210–4316).

### High — A country-local recovery close performs a map-wide subject wipe

`random_terror_clear_country_commitments` is called from `random_terror_close_country_recovery` when that country's recovery package is complete (`031_random_terror_effects.txt:4307–4327`).
Although the helper clears country flags and removes missions in its current country scope, it then runs `every_state` over all states and invokes `random_terror_clear_state_commitments`, which unconditionally clears every generic Event 031 subject family (`4210–4305`).
Thus a recovery close for A can erase B's active receipt(s) and cause B's mission cancellation or mis-resolution.
This helper is also called from the global defeat path (`4385–4400`), where global cleanup may be intentional; those callers need distinct owner-local and explicitly global cleanup contracts rather than one shared global loop.

`random_terror_clear_actor_runtime` and `random_terror_cleanup_actor` also call the all-family state cleanup from `every_owned_state` (`4423–4433`, `4627–4645`).
Because a state subject can represent a mission owned by a different country, actor cleanup can invalidate another receiver's mission on a state owned by the actor.

### High — Five accepted success receipts are circular or cleared before activation

The accepted success targets below are from the matrix's Government missions rows 45–50.
The dedicated prompt additionally requires auto-completion on the real objective, no second paid click, and distinct success/partial/failure behavior (`031_random_terror_decision_mission_prompt.md:205–226`).
The current non-selectable mission's `available` trigger requires the listed success receipt, while its own `complete_effect` calls a resolver that sets that receipt; the resolver cannot be the producer of the condition that must already be true before that complete effect can run.

| Mission | Accepted success target | Current receipt producer/defect | Required producer contract |
| --- | --- | --- | --- |
| `random_terror_contain_attack_wave` (`missions.txt:30–89`) | Pressure falls and spread is blocked, or the original hotspot is cleared; partial means no spread while the original cell remains; failure means a valid new hotspot or stage advance (`matrix.md:45`). | `available` requires `random_terror_containment_success` (`missions.txt:30–36`). The only current setter is `random_terror_resolve_containment_mission_success` (`effects.txt:3612–3625`), called by this mission's `complete_effect` (`missions.txt:55–60`). Both setup callers clear the marker before activation (`decisions.txt:86`, `445`). | Record mission progress from an accepted response action or a real state/spread transition after the commitment; the resolver consumes that receipt and applies outcomes but must not create its own prerequisite. Preserve the accepted no-spread/pressure-or-clear criteria. |
| `random_terror_protect_transport_network` (`missions.txt:96–168`) | Keep the named transport assets operational, preserve supply, and lower activity; partial keeps the route open with bounded damage; failure is disruption/captured supply/pressure (`matrix.md:46`). | `available` requires `random_terror_transport_protection_success` on the subject controlled by ROOT (`missions.txt:107–115`). `random_terror_decision_protect_transport` sets it at commitment (`effects.txt:2076–2088`), but the caller explicitly clears it before `activate_mission` (`decisions.txt:174–176`). The mission resolver is the only remaining setter (`effects.txt:3652–3665`). | Progress must come from a later accepted protection/result source that proves the route/supply/activity condition over the accepted duration, not from the cost-bearing start click or the success resolver. Keep the exact target and receiver paired. |
| `random_terror_break_cross_border_corridor` (`missions.txt:175–242`) | All participants accept and the named valid connection is controlled; success removes the corridor and lowers reach/supply, partial weakens/shifts it, failure causes spread/retaliation (`matrix.md:47`). | `available` requires `random_terror_support_disruption_success` (`missions.txt:186–194`). `random_terror_resolve_support_disruption` can set it (`effects.txt:2932–2947`) but has no call site in current script source. The live decision calls `random_terror_decision_disrupt_support` (`decisions.txt:618`), which sets a country-level `random_terror_support_disrupted`, not the required state receipt. The mission resolver only sets the state receipt from its own complete effect (`effects.txt:3687–3706`). | The producer must be the accepted multi-party corridor transaction after participant acceptance and route/target revalidation. The current single-country disruption action is not proof of the matrix's two-party consent condition; do not wire the dead helper as an unconditional same-click success. |
| `random_terror_prevent_capital_seizure` (`missions.txt:248–320`) | Hold the capital and command continuity and expose compromised actors; partial holds the capital with nearby loss; failure is coup/paralysis/civil war/capital loss (`matrix.md:48`). | `available` requires `random_terror_capital_security_success` on a ROOT-controlled capital (`missions.txt:259–268`). The setup helper writes it only through `every_owned_state` (`effects.txt:2212–2223`), which misses a foreign-owned but ROOT-controlled capital, and the caller clears the selected state's marker immediately after the helper (`decisions.txt:1158–1160`). The resolver itself sets it (`effects.txt:3728–3741`). | Progress must be written against the exact accepted capital target after real continuity/exposure conditions are met. A controlled-but-not-owned capital must remain eligible; do not substitute owner=ROOT for the accepted control requirement. |
| `random_terror_restore_civil_authority` (`missions.txt:404–469`) | Activity clears, legitimacy rises, and the accepted recovery cooldown extends; partial remains contested; failure returns dormant/entrenched (`matrix.md:50`). | `available` requires `random_terror_civil_authority_restored` (`missions.txt:415–423`). `random_terror_decision_restore_services` sets it through the current action target (`effects.txt:2263–2276`), but its caller clears the marker before mission activation (`decisions.txt:1679–1681`). The success resolver sets it again (`effects.txt:3855–3874`). | Advance progress only from the accepted recovery result after the service/revenge/administration criteria hold. Keep the duration and recovery outcome; the start click or resolver cannot stand in for an asynchronous objective. |

These are five distinct self-blocked success predicates.
The current source also has a separate hostage lock described below; it is not counted as one of these five marker cycles.

### High — Mission setup `ROOT` is not always the mission receiver

Direct targeted government decisions have country ROOT and state FROM per the offline decision documentation (`Decision modding - Hearts of Iron 4 Wiki.md:578–581`); for these callers the initiating country is also the mission receiver.
The ordinary helper call does not reroot: the current helper is still executing within the decision's original scope contract.

The offline scope table documents ROOT as the block root and THIS as the current scope (`paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:260–263`).
Therefore helper calls do not by themselves make a nested controller the decision ROOT; nested receiver identity must be carried explicitly.

Two paths deliberately change the receiver:

| Mission | Setup caller | Actual receiver and target | Keying consequence |
| --- | --- | --- | --- |
| `random_terror_hostage_deadline` | `random_terror_apply_incident` saves the current state as regular target; its hostage branch enters that state's `CONTROLLER`, sets the country slot, writes the state subject, then activates the mission (`effects.txt:397–405`, `595–604`). | The target state's controller at incident time receives the mission; it may not be the state owner. The current receiver check refuses to create this mission when that country already has slot 1. | Bind the durable receipt to the country scope that actually executes `activate_mission`, not to the state owner or an assumed outer ROOT. |
| `random_terror_stop_coordinated_uprising` | `random_terror_call_coordinated_uprising` begins with the actor as ROOT, sets a subject on FROM, then enters `FROM.CONTROLLER` to set slot 2 and activate the mission (`decisions.txt:3149–3243`). | The target controller receives the mission; it is distinct from the initiating actor and can also differ from the target's owner. | A `_@ROOT` receipt written in the actor's setup scope would identify the wrong country. Bind to the nested receiver explicitly; callback ROOT must be the mission-owning country. |

For the other six setup paths, ROOT is the initiator and the country that calls `activate_mission`: containment has two callers (`decisions.txt:74–89`, `400–451`); transport (`150–176`); corridor (`598–620`); capital (`1148–1160`); retake (`1428–1445`); and restoration (`1667–1681`).
Their state target can still be foreign-owned: transport/corridor/capital/restoration use controlled targets, while retake intentionally targets an outside state satisfying the parent's claim/core and enemy-controller requirements.

The offline flag guidance supports country-targeted flag suffixes (`Data structures - Hearts of Iron 4 Wiki.md:102–127`), and Chaos Redux already uses state receipts suffixed with `@ROOT` in direct targeted-decision contexts (`common/decisions/028_asteroid_incoming_decisions.txt:743–744`, SHA-256 `E954ED3B45307AD519E773D4F7F0B7FB5898D386B4CB95BACE173248A929C6FD`).
That precedent validates the mechanism, not a blanket substitution.
Use the receiver tag as the key: direct ROOT-owned callers may use ROOT; hostage and uprising setup must capture the nested controller; a cleanup inside `every_country` must key the iterated THIS country rather than an unrelated outer ROOT.
Preserve `is_controlled_by = ROOT` only where the accepted target criterion explicitly requires current control; never impose owner=ROOT across these missions.

### Medium — Hostage success is blocked by the slot that the mission occupies

The only current producer of `random_terror_hostages_recovered` and `random_terror_hostage_crisis_resolved` is `random_terror_decision_security_surge` (`effects.txt:2110–2127`). `random_terror_hostage_deadline` occupies `random_terror_mission_slot_1` (`missions.txt:478–540`), while the security-surge decision's availability requires slot 1 to be clear (`decisions.txt:400–451`).
Therefore the receiving country cannot take the only current progress action while its hostage mission is active.
A different country taking over control can set the generic state marker and accidentally progress the old receiver's mission, which is a cross-country exploit rather than a safe route.
The accepted matrix also calls for partial hostage success (`matrix.md:51`), but the current hostage timeout has failure only (`missions.txt:519–538`) and no partial resolver.

### Medium — State transfer does not rebind or explicitly cancel the old receipt

Most `cancel_trigger` blocks cancel when a generic subject disappears, not when its owner/controller/route changes (`missions.txt:36–44`, `117–123`, `196–201`, `269–275`, `348–353`, `425–430`, `499–508`, `569–575`).
Meanwhile the map state can remain flagged through transfer; the subject flags contain no receiver identity.
Thus an old receiver may retain a live mission on a transferred target, and another receiver may observe the same receipt.
Cancellation, timeout, completion, and state-transfer handling must act on the exact receiver-target pair.
Define whether a transfer invalidates or preserves each accepted objective; do not silently reassign its owner.

`random_terror_retake_lost_state` is the deliberate exception in target type, not in receipt identity: it targets an external claimed/core state and its progress requires control by the mission receiver plus the local-control stage condition (`missions.txt:336–347`).
Preserve this external-target design.
The state-stage helper explicitly clears/recomputes `random_terror_state_lost_local_control` (`effects.txt:294–339`); no Event 031 `on_state_control_changed` producer for that stage receipt was found, so the parent should keep the accepted retake/civil-restoration scenario in regression coverage rather than assuming capture alone clears all stage state.

## Mission lifecycle and accepted quality fields

All eight missions are in `random_terror_government_response_category` (`missions.txt:18`).
They are non-selectable and `fire_only_once = no`; mission auto-completion is driven by `available` and country mission-slot state, not by selecting a second button.
The matrix caps the category at three active missions; current slot families are shared across three mission types each for slots 1 and 2, and two types for slot 3.

| Mission | Receiver / map objective | Accepted requirement and duration | Success / partial target | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `random_terror_contain_attack_wave` | Government receiver; one active state/hotspot. | Valid protection, active target, no invalid duplicate; 90–120 days. | Pressure falls and spread is blocked or hotspot cleared; partial is no spread while original cell remains. | Valid new hotspot or stage advance. | Generic subject can be seen/cleared by every country; shared slot 1. |
| `random_terror_protect_transport_network` | Government receiver; named rail/port/hub/corridor state. | Maintain unit/resource commitment; about 120 days. | No major disruption, supply preserved, activity falls; partial route remains open with bounded damage. | Route disruption, captured supply, pressure rises. | Generic subject and success are shared; shared slot 1. |
| `random_terror_break_cross_border_corridor` | Government receiver; named cross-border connection and participating countries. | All participants accept, route/targets remain valid; about 150 days. | Corridor removed and reach/supply falls; partial corridor weakens or shifts. | Spread or retaliation. | Generic subject; two-country participation is not bound to the receiver receipt; shared slot 2. |
| `random_terror_prevent_capital_seizure` | Government receiver; exact capital/command state. | Capital valid and emergency protection maintained; 60–90 days. | Capital and continuity held, compromised actors exposed; partial capital held with nearby loss. | Coup, paralysis, civil war, or capital loss. | Generic subject; current progress helper is owner-state-limited despite controlled target; shared slot 2. |
| `random_terror_retake_lost_state` | Government receiver; claimed/core state outside the receiver may be the target. | Real war/state objective, forces, supply; about 180 days. | Control restored and recovery opens; partial military control without civil restoration. | Actor entrenches and gains authority. | Generic subject can outlive transfer; shared slot 3. |
| `random_terror_restore_civil_authority` | Government receiver; recaptured/cleared recovery state. | No armed control, damaged services, relief and administration; 120–180 days. | Activity clears, legitimacy rises, cooldown extends; partial state remains contested. | Dormant or entrenched return. | Generic subject; owner-local recovery close wipes all owners; shared slot 3. |
| `random_terror_hostage_deadline` | Target state's controller; exact incident state. | One active crisis and a valid chosen response; 30–75 days. | Hostages recovered/released with bounded casualties; partial some freed while leaders escape. | Mass casualties, propaganda victory, pressure rises. | Controller can differ from owner; shared slot 1 blocks its only current success action. |
| `random_terror_stop_coordinated_uprising` | Target state's controller, not the initiating actor; one pressure-backed state. | Evolution V, real pressure, active cells; 60–120 days. | Uprising collapses and world revolt weakens; partial one state held while cells survive. | Civil war or transfer. | Actor/owner/controller/receiver can all differ; generic subject; shared slot 2. |

The accepted success targets for the five self-blocked markers and the exact source-level producer defects are detailed above.
The other three use external state/action conditions but remain subject to owner-binding and cleanup defects below.

## Exact owner/progress contract for all eight missions

| Mission | Receiver at activation | Durable target/progress now | Owner-safe contract needed |
| --- | --- | --- | --- |
| `random_terror_contain_attack_wave` | Government decision ROOT (response-cell or security-surge caller). | One state flag, shared across countries; success marker self-blocked. | Persist `(receiver, exact state, mission type)`; only that receiver may observe/update/clear its receipt. External progress must prove the matrix's pressure/spread/clear condition. |
| `random_terror_protect_transport_network` | Government decision ROOT. | Controlled FROM state; setup helper sets then caller clears the same success state flag. | Preserve target even if foreign-owned; progress must be later than commitment and prove route/supply/activity result. |
| `random_terror_break_cross_border_corridor` | Government decision ROOT. | Controlled FROM state; the called single-country helper is not the unused success helper. | Preserve exact connection plus accepted participant/consent set; all progress and cleanup are keyed to the receiver transaction. |
| `random_terror_prevent_capital_seizure` | Government decision ROOT. | Controlled capital FROM state; helper searches owned states and caller clears selected receipt. | Key to ROOT receiver and exact capital state; preserve control—not ownership—as the territory test. |
| `random_terror_retake_lost_state` | Government decision ROOT. | External any-state target; mission uses actual ROOT control plus the lost-local-control stage. | Keep parent claim/core, war, supply, and external target requirements; the receiver receipt remains stable through state transfer and only that receiver resolves it. |
| `random_terror_restore_civil_authority` | Government decision ROOT. | Controlled recovery FROM state; setup success is cleared before activation. | Persist exact receiver-target receipt; progress only after accepted recovery conditions; local recovery close may not erase another country's receipt. |
| `random_terror_hostage_deadline` | Target state's CONTROLLER at incident/activation time, if its slot 1 is free. | Event-chain regular state pointer is used synchronously; mission then relies on an unkeyed subject plus generic recovery flags. | Bind to the actual receiving controller and incident state; unlock an accepted progress producer while the mission is active; include the accepted partial outcome. |
| `random_terror_stop_coordinated_uprising` | Target state's CONTROLLER, not the initiating actor ROOT. | Actor writes an unkeyed state subject; defender security surge writes a generic `uprising_stopped` fact. | Bind receipt to receiver controller and target state; actor, target owner, controller, and receiver are distinct identities and must not be conflated. |

The one-per-country slot families are: slot 1 = containment / transport / hostage; slot 2 = corridor / capital / uprising; slot 3 = retake / civil authority.
Every activation block checks only the shared slot flag plus an unkeyed `any_state` subject, not a mission-family receipt.
Keep one active mission per slot; after receipt scoping, add/retain a mission-specific active lock if necessary so one country's slot cannot awaken two different mission definitions from another country's subjects.

## Caller lifetime and persistence

The targeted decision callers save `random_terror_action_state` from FROM and immediately pass it to synchronous helpers.
The uprising path similarly saves/uses `random_terror_uprising_state` during the initiating transaction. `random_terror_apply_incident` saves `random_terror_current_state` and uses it inside the same effect chain.
None of those regular pointers is a durable asynchronous mission binding; the mission callbacks do not refer to them.
The offline `Data structures` reference says regular event targets last only for the originating effect block (and events fired from it), then clear automatically (`lines 263–305`, SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`).
Installed `effects_documentation.md`, lines 6496–6505, lists `save_event_target_as` (`2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`).

Therefore the current use of a persistent state receipt rather than a regular pointer is directionally correct for a 30–180 day mission; the defect is that the receipt has no receiver key.
A global event target is not a drop-in fix: it is one pointer per name and persists until explicitly cleared.
If used instead of an owner-keyed state receipt, it must be namespaced by receiver and mission, updated only after revalidation, and cleared on all complete/cancel/timeout/invalid-target/global-defeat paths.
Do not use one shared `random_terror_action_state`-style global target for concurrent countries.

## Parent patch map (recommendation only; no source edits here)

1. `common/decisions/031_random_terror_missions.txt`: bind every activation/available/cancel/complete/timeout predicate to the receiver's exact receipt; make every cleanup clear only that receipt.
   Keep physical state facts separate from mission ownership: a shared state fact may be checked, but only alongside the receiver-keyed subject on that same state.
2. `common/decisions/031_random_terror_decisions.txt`: set the receiver-keyed receipt on the exact selected state before activation.
   Direct country decisions use their existing ROOT receiver; the hostage incident and coordinated-uprising paths must bind to the actual `CONTROLLER` receiver.
   Retain the existing foreign-owned/foreign-controlled target rules.
3. `common/scripted_effects/031_random_terror_effects.txt`: move each of the five success writes to the existing accepted external action/progress source that proves its matrix criterion; keep outcome resolvers as consumers, not prerequisite producers.
   Decide whether the uncalled `random_terror_resolve_support_disruption` is actually the accepted bilateral corridor producer before wiring it.
   Separate owner-local `random_terror_clear_country_commitments` from deliberate global defeat cleanup; make actor cleanup remove only the intended owner's receipts.
4. Keep one mission-type lock per shared slot and make receiver state explicit through nested scopes.
   Any `@ROOT` token in the direct callers is only valid where caller ROOT equals receiver.
   For per-country iteration use the iterated country scope, not the outer initiating ROOT.
   Do not replace target eligibility with owner=ROOT.
5. Resolve the hostage slot deadlock using an already accepted progress action/contract, and disposition the matrix's partial hostage result; do not let another country spoof progress via its controller changing.

## Proposed regression fixtures (not run; parent implementation tests)

- A and B each have the same mission type active on different states.
  Complete, timeout, cancel, and close recovery for A; only A's state receipt and A's country slot/outcome may change, and B remains active.
- A holds slot 1 for transport while B has a containment subject.
  A must not auto-activate/complete containment or exceed one active mission in the slot.
  Repeat for shared slot 2 and slot 3 families.
- Both countries have distinct receiver receipts on the same state after a transfer/restart edge.
  Resolve or cancel one receipt; the other remains or is explicitly invalidated by its own contract, never silently consumed.
- Exercise the foreign-target cases: foreign-owned but ROOT-controlled transport/capital/restoration target; enemy-controlled claimed/core retake target; incident state whose controller differs from owner; uprising where actor ROOT, state owner, and receiving controller are all distinct.
- Change target controller/owner during each active mission, then exercise complete/cancel/timeout.
  Confirm the old receiver's policy is deterministic, cleanup is idempotent, and a new receiver cannot inherit the old receipt.
- Complete A's recovery package while B has each mission family active.
  Then exercise deliberate global defeat cleanup separately; the first is owner-local, the second may be intentionally global.
- Run a hostage mission with slot 1 occupied and verify that accepted hostage progress remains possible without a second paid click; cover success, partial, failure, cancel, and timeout.
- Save/reload during each active mission and confirm the owner-target receipt persists while regular caller event targets are no longer required.

These are source/gameplay regression scenarios for the parent; they were not run in this read-only subtask.
The user performs live-game validation.

## References and exact revisions

Accepted implementation contract:

- `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_matrix.md`, Government missions lines 41–52, SHA-256 `037B6E780972600CCB5259426D19005BA419CADD9058186603B7327569495C76`.
- `docs/specs/031_random_terror_specs/031_random_terror_decision_mission_prompt.md`, missions lines 205–226, cleanup lines 405–432, validation cases 480–498, SHA-256 `7B1037A7F9E303FDF5984510F562207AE5B0395E34EBB4F756F09A70BED3FE5A`.
- `AGENTS.md`, SHA-256 `38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF`.

Offline and installed engine references:

- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 382–392 and 528, SHA-256 `18EF5249E4991F5427ECA9EC2A4F66DD47F51E26A491C730ADC622F1F5DB1B49`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, flags lines 102–127 and event targets lines 263–305, SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, mission lifecycle lines 467–478 and targeted-decision FROM/target rules lines 578–581, SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
- Installed `documentation/triggers_documentation.md`, lines 1612–1681 and 4827–4836, SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE33B27C2D1DE29`.
- Installed `documentation/effects_documentation.md`, lines 4155–4167 and 6496–6505, SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- Installed `common/decisions/_documentation.md`, target country/controlled state semantics lines 39–44, SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.

Vanilla mission precedent:

- Installed `common/decisions/PRC.txt`, `PRC_assaulting_guyuan` activation at line 6541 and mission/cancellation on exact state 1045 at lines 6592–6617, SHA-256 `19B5776BF0E91A419946BEDAF3AA5E052EC09165AE8BDBCB0F1800CD081A01DF`.
  It binds the mission to its country ROOT and explicit state target/control conditions rather than a generic world-visible state receipt; used here as a structure precedent, not as the Event 031 design.

Current parent boundary/current source:

- Current HEAD observed: `72c748ace` (`Repair Missiles target selection and launch preparation`).
  Parent commits `87948c017bb34070917a90d5e30b83efbd038a6a` and `720a2457cd5ae01227bf5c5551fba90eb5ff94f9` exist and their terminal/depot handoffs were read; neither fix is duplicated here.
- Current `common/scripted_effects/031_random_terror_effects.txt` SHA-256 `DD87C9D0DE7AE88CE258A0D798B9410A33C37B00B7F011271C8B0AB649760E85` and `common/scripted_triggers/031_random_terror_triggers.txt` SHA-256 `AEB0C8376214F1BF7BD498F8C266E9669284BC831984C21000287DCD2FAB0060` match the frozen parent wave patch hashes.
  They were not changed or re-audited for the terminal baseline.
- Other current source revisions: `common/decisions/031_random_terror_missions.txt` SHA-256 `B24633FA4996FB2D25C44118C44A01F38B3C1C821DBCADF819FA71591813A71D`; `common/decisions/031_random_terror_decisions.txt` SHA-256 `EC998C5B3355AAA8546EC73F0174F90F65A4665372C415DD2101315B2265F215`.

## MCP and validation limits

The connected inventory exposes no `mcp__hoi4_agent_tools__hoi4_*` routes.
Narrow attempts returned the actual runtime errors `TypeError: tools[name] is not a function` for `hoi4_decision_inspect`, `hoi4_event_inspect`, `hoi4_reference_context`, `hoi4_reference_search`, and `hoi4_reference_read`.
The local reference sections above were read directly.
No decision/event MCP result is claimed.
No weight or balance target was chosen in this follow-up.
The connected probability-inspect attempt returned `TypeError: tools[name] is not a function`, so no probability baseline/comparison is claimed here.
The recommended owner-bound activation/availability repair may change AI mission eligibility; if the parent implements that change, route the affected mission scenarios through the probability auditor and compare the exact same fixtures before accepting the eligibility change.
No GUI surface is in scope.

No gameplay test, syntax validation, or runtime scenario was run because this was a bounded read-only audit and no game launch was authorized.
The test list above is a handoff, not evidence of execution.
The audit is actionable but incomplete until the parent applies the owner/progress contract and reviews the resulting source and regression evidence.

