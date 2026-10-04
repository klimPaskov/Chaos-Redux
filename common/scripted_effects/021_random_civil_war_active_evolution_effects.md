# Event 021 active evolution effects

This API records opening provenance for the accepted active-war Evolution I repair.
The theater review, owned active-front receipt, source commit bridge, and management phase remain separate implementation work; these helpers alone do not implement that transition.

`event021_capture_pending_opening_evolution_stage` accepts ANY scope and reads the existing global active evolution flags.
Its output is `global.random_civil_war_pending_opening_evolution_stage`, with baseline zero and the highest active stage from the existing centralized stage constants.
It changes no country history, generation, actor, weight, timing, or Chaos.
The opening identity helper calls it before mutation.

`event021_commit_opening_evolution_provenance` accepts COUNTRY scope and copies that serial transaction field into `random_civil_war_opening_evolution_stage` after successful host or primary commitment.
Missing scratch does not infer a stage from current world flags or the number of actors.
The host commit, ordinary primary initializer, and proved Event 006 primary war call it.

`event021_inherit_crisis_opening_evolution_provenance` accepts COUNTRY scope with a normal country pointer in `random_civil_war_crisis_host_scope`.
It validates that real host and its stage receipt, reads the host value through a temporary variable, then assigns it in the actor's own scope.
Missing identity or provenance leaves the field unchanged and remains unavailable to a future active review.
Ordinary and complete Event 006 secondary actors use this path.
An additional front inherits the original crisis stage rather than pretending that a baseline war began after an evolution.

Example: capture pending stage in `event021_parent_prepare_crisis_identity`, commit it on successful host registration, and inherit it after setting a secondary actor's exact crisis host pointer.
No image, GUI, animation, super-event, model, country identity, or new tuning family is introduced.

The pending field is overwritten on each serial opening and cleared by startup and rollback.
The public opening wrappers call `event021_parent_release_completed_front_plan` after their mutation executor returns.
That helper clears the pending field only when current host/front/crisis success, primary identity where applicable, terminal row status, completed callbacks, and durable provenance are proven.
An incomplete template is retained rather than hiding its unresolved work.
Opening-stage history remains separate from transient active review receipts.
The child's immutable `random_civil_war_source_front_id` is copied from the validated plan's source-ID column during registration binding and cleared only with full crisis-role teardown.

The API follows the existing normal-variable and explicit-scope contracts in offline Data structures and installed effects documentation, including documented `for_each_loop` indexes at installed lines 4279-4335.
Installed effects revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; offline Data structures revision is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
No engine or full active-evolution acceptance is claimed by this provenance tranche.
