# Private clone Deployment: existing production consumer review

Date: 2026-09-08.
Disposition: read-only source audit implemented; throughput and native-receipt proposals unresolved pending parent acceptance.
Only this handoff was added.
No gameplay, AI, localisation, existing handoff, scheduler or other file was changed; no commit was made.
All facility/equipment terminology below describes fictional game mechanics only.

## Conclusion

Private Deployment can deepen the existing `germany_mengele_produce_clone_equipment` consumer instead of adding another growth-site or production subsystem.
However, its authentic native receipt currently belongs to a different project from the producer's receipt, and the private-native path itself has an admission gap.
These must be reconciled explicitly before claiming a completed progression.
The prior `016_private_custom_deployment_payoffs_2026-09-08.md` cloning proposal was unresolved and did not account for this existing periodic producer.
This review recommends replacing that proposed additional-site subsystem with the existing consumer approach; it does not retrospectively mark either proposal accepted.
The separate KRG paid maturation correction remains separate and is not a substitute for private Deployment.

## Actual production and economics

`common/scripted_effects/germany_mengele_effects.txt:77` defines `germany_mengele_count_biowarfare_facilities`.
It iterates the invoking country's controlled states and increments once for each state with `biowarfare_facility > 0`.
It counts facility-bearing states, not building levels; a level-two facility in one state still counts once.
It does not require ownership, a special site flag, live project-provider validity, or an active native research project.

At line 85, `germany_mengele_produce_clone_equipment` requires only country flag `germany_mengele_cloning_project_completed`.
It multiplies the count by `constant:germany_mengele_cloning_project.clone_equipment_per_facility_per_week`, currently one, rounds, and adds that many `clone_equipment_1` when positive.
It then calls `clone_refresh_reserve_manpower` even when the facility count is zero.
The output's `producer = ROOT` is provenance, but can refer to an outer event country when the helper is invoked through another country's scope; implementation should review this separately from the equipment recipient, which is the current country.

For N controlled facility-bearing states, each invocation therefore creates N clone equipment.
There is no recurring PP, support, fuel, manpower, truck or factory deduction in this helper.
Existing `clone_equipment_1` inherits build cost 12, one steel and two rubber from its archetype for ordinary factory manufacture; the scripted facility producer does not pay those factory inputs.
The shared reserve consumer multiplies stored clone equipment by ten weekly manpower and removes that contribution when equipment leaves the stockpile.
One continuously controlled facility-bearing state produces 52 equipment over 52 regular weekly invocations: 624 nominal equipment IC, with 520 weekly reserve manpower at the end if all equipment remains stored.
Completion adds an immediate extra invocation, so an uninterrupted example with completion plus those 52 ticks yields 53 equipment, not 52.
These are arithmetic projections, not instantaneous manpower awards or a claim of actual campaign production.

## Exact callers and cadence

| Source | Call condition and consequence |
| --- | --- |
| `common/on_actions/germany_mengele_clone_on_actions.txt` | Existing user-authorized `on_weekly` country hook checks the old completed flag and calls the producer. No new scheduler is needed. |
| `germany_mengele_complete_cloning_project`, effects line 104 | Sets the old completed flag, clears pending unlock, sets Directorate completion, selects Mengele refinement, immediately produces equipment, and may schedule `germany_mengele.24`. |
| `germany_mengele_add_requested_biowarfare_facility`, producer call around line 457 | After successful requested construction and its other consequences, calls the producer for the entire current facility count, not just the newly built state. |
| `mengele_clone_army_add_biowarfare_facility`, producer call around line 541 | Successful construction similarly calls the producer for the entire count. |
| Civil-war/faction inheritance block, around lines 2053–2074 | When the loyalist has the old completed flag, the new faction receives that flag and Directorate availability/completion, selects Mengele refinement and immediately produces from its controlled facilities. |

Those are all direct references to the producer found under `common` and `events`, besides its definition.
The distinct `common/on_actions/clone_system_on_actions.txt` weekly hook only refreshes reserve manpower; it does not produce equipment.
Calling both hooks does not double-create stockpile equipment.

The weekly filter and producer do not check program closure, rejection, defeat, expiry, capitulation, world end or the strict private provider gate.
Thus retained old completion plus controlled facilities can continue scripted production even when the private Event 016 provider would be invalid.
That is a source finding, not authority to silently remove legacy behavior.
The completion helper itself has no repeated-completion guard, so replaying it can immediately produce another full-count batch and re-run its other consequences.
It is unsafe as a generic receipt-reconciliation helper.

## Native project, private stages and refinements

There are two distinct native projects:

- `sp_mengele_cloning` in `common/special_projects/projects/mengele_cloning_projects.txt` calls `germany_mengele_complete_cloning_project` directly.
  Its admission uses `camp_rework_germany_cloning_project_currently_available`, which has the Germany program route and a separate `is_mengele_clone_directorate_country` route accepting Directorate cloning/all-project availability.
  It therefore supplies the real receipt required by the legacy weekly producer.
- `sp_brilliant_scientist_cloning` in `common/special_projects/projects/016_brilliant_scientist_projects.txt:385` sets the shared family selector and calls `brilliant_scientist_record_new_project_prototype`.
  That dispatcher can call the private bridge, but the native project's own admission still calls `brilliant_scientist_can_research_cloning_prototype`.
  That trigger currently requires the current Kruger host, primary facility, Kruger Theory ledger and Capacity.
  A source search found only one project and one admission-trigger definition, so the private bridge's existence does not prove a reachable private native project.

`brilliant_scientist_mengele_cloning_native_output_is_authentic` accepts only actual completion of `sp_brilliant_scientist_cloning`, strict private provider validity, exact family selection and private Theory.
It does not accept `sp_mengele_cloning` or `germany_mengele_cloning_project_completed` as an alternative.
The seven-family native grant helper repeats the same exact project requirement for cloning.
Private Prototype records `mengele_event016_cloning_prototype_completed` and `directorate_special_project_cloning_completed`, but not `germany_mengele_cloning_project_completed`.
Private Deployment records its own receipt and calls the neutral operational grant; its physical producer therefore remains disconnected.
The parent-added Deployment modifier parity does not change this receipt gap.

Neutral clone operational access grants the existing operational technology/template/manufacture path, without native project completion or physical stockpile production.
Keep that full-strength grant at authentic Prototype.
Legacy `sp_mengele_cloning` completion additionally calls `clone_select_mengele_refinement`, which removes the incompatible Kruger refinement technologies and grants `mengele_clone_refinement_tech`.
The private clone Weaponization upgrade also selects that same Mengele refinement through `chaosx_grant_custom_technology_upgrade`.
Consequently, adopting legacy native completion introduces a preexisting-refinement case in which that later private refinement effect is already present; do not conceal this further payoff collision by delaying or revoking the legacy refinement.
The explicit Aryan refinement is separate and must not be inferred from either native project.

The old completed flag has consumers outside production, including camp/project gates, revolt-related logic and the narrower Event 019 Aryan-provider checks.
Fabricating it merely to activate the producer would assert unrelated history.
Use actual native completion/private receipts directly instead.

## One concrete proposal: private Deployment throughput tier

Proposal, not an accepted tuning change: retain the existing producer and facility count, then make paid private Deployment increase its regular weekly physical yield from one to five clone equipment per qualifying state.
This is an additional four physical equipment per week per qualifying state, not a modifier-only reward, free formation loop or a second maturation system.
For one continuously qualifying state, the additional 52-week output would be 208 equipment, 2,496 nominal equipment IC and 2,080 weekly reserve manpower at year end if all extra equipment remains stored.
The number five is an explicit proposal for parent balance review, not a user-selected amount or an AI-weight recommendation.

Minimal integration contract:

1. Resolve the native path causally: adopt actual `sp_mengele_cloning` completion as an explicitly approved alternative for private cloning Prototype after private Theory, and update both the private authentication trigger and seven-family grant guard consistently.
   Preserve the existing native project output/refinement and the full neutral operational grant; do not replay `germany_mengele_complete_cloning_project`, fabricate native completion, or charge another native Prototype.
   For already completed native work, the existing post-Theory adoption mechanism must use the same approved alternative.
   For native completion after private Theory, add a bounded call from that genuine completion callback into private Prototype synchronization; the legacy project currently calls only its legacy completion helper.
2. Extend the existing producer's admission with an explicit private receipt branch, rather than setting the legacy completed flag.
   The private branch requires strict private provider validity, authentic native completion, private Prototype and neutral clone operational knowledge.
   Preserve the legacy branch's baseline output unless a separate lifecycle correction is accepted.
   Countries satisfying both branches receive one baseline computation, not two added copies.
3. For the proposed Deployment enhancement, require exact `mengele_event016_cloning_deployment_completed` and the same live private provider/native/technology proof.
   Reuse actual facility buildings, not KRG growth-site flags or a new facility registry.
   A conservative proposed bonus gate additionally requires current ownership and control for the invested facility-bearing states; the legacy controlled-state baseline is left unchanged.
   Parent must accept that bonus-only ownership condition explicitly.
4. Apply the enhanced portion only from the existing weekly invocation, not from completion, new-facility construction or inheritance callbacks.
   Give the central producer an explicit weekly-context input, set and cleared by the existing weekly caller; direct event/construction callers remain baseline-only.
   The producer consumes/clears that temporary input, so an earlier weekly call cannot leak an enhanced payout into another callback.
   No additional world-iterating hook, new scheduler or persistent throughput meter is needed.
5. Keep stockpile addition and `clone_refresh_reserve_manpower` in the existing producer, with one combined output and one refresh per invocation.
   Closing the private program or losing ownership/control removes the enhancement on the next eligible invocation without deleting completed research or stored equipment.
   The existing paid Deployment receipt already owns its stage payment and one-time settlement; repeated callbacks cannot create another tier or an immediate enhanced batch.

This concentrates the payoff in the already established facility economy while preserving ordinary factory production from Prototype and avoiding another paid site-construction requirement.
If the proposed recurring yield is rejected on balance grounds, retain the architecture but leave the throughput value unresolved; do not substitute the existing stage modifier and call the physical payoff complete.
The separate legacy-provider shutdown behavior and private Weaponization/refinement collision remain explicit follow-up decisions.

## Validation required before implementation acceptance

Test old-project-only, Event-016-project-only and both-project countries; native completion before/after private Theory; actual private Prototype adoption exactly once; no legacy-history fabrication; Prototype retains full neutral manufacture; private Deployment increases only the existing weekly producer; completion/construction/inheritance remain baseline-only; captured versus owned facilities; zero facilities; multiple building levels in one state; invalid private provider; repeated stage callbacks; stale weekly-context input; and equipment consumption reducing reserve manpower.
The current narrow source review establishes caller/receipt behavior, not engine cadence or balance acceptance.
No probability-bearing source was edited or AI weight selected.
Existing event MCP inspection remains partial with deferred helper lifecycle coverage and does not prove this proposed production integration.
Parent owns focused event/scope evidence, any probability comparison for changed weighted consumers, localisation and final integration review.

SHA-256 source snapshot:

| File | Hash |
| --- | --- |
| `germany_mengele_effects.txt` | `fbe41476b84f2b6d2c4faba5ccaf1c82c45a714b0c814fba782c8a80f02657ac` |
| `germany_mengele_clone_on_actions.txt` | `83f2b2664723f0dd0911ad060b1244c2a06d0c9adf59bff66718c89f94884cdf` |
| Private stage triggers | `9990812298092939c45070acbe111f8c0d4248596b9648412019d04201b312af` |
| `mengele_cloning_projects.txt` | `313b75317c645f6640c6ff96dfb1a1aeb50907d0c9c54b496f197e8824b8f168` |
