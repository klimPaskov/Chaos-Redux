# The First Red Line

## Scope

The First Red Line is the reviewed Quarantine archetype chain for a surviving country after the Fallout consequence. It is an ordinary survivor-country story chain. It does not request Fallout, start the blackout, perform the thermonuclear sweep, rewrite the world, or register the Fallout consequence as an ordinary Event Log entry or evolution.

The chain uses candidate `684`, event blocks `chaosx.fallout.684` through `chaosx.fallout.690`, transaction `710069`, scheduler route `7170`, route upper bound `7171`, and survivor-memory Event Log history `9175`.

The candidate producer and every event surface remain dormant while the shared Fallout scheduler activation flags are unset. This tranche receives no release-floor credit and does not claim runtime acceptance.

## Admission and target contract

The country must have a current Fallout registry row, durable survival-resource row, Quarantine government archetype, minimum Medicine, Cohesion, and Recognition, and one complete affordable branch during the authored campaign window from day `365` through day `4499`.

The producer selects the lowest native owned state id that is controlled by the country and has a current identity row, durable state-resource row, current Supply Access, a produced Air Winter snapshot from the current Fallout generation, surviving population, Shelter Capacity at least `20`, Supply Access at least `15`, Adaptation at least `5`, Disease Pressure from `20` through `84`, Exposure below `75`, and Air Winter phase from `1` through `6`.

The producer writes the native state id into the typed candidate row and into the ordinary dispatch envelope. It never fabricates a state, province, country, actor, partner, or fallback target. Opening, delayed result, callback, and cleanup gates revalidate the country, owner, controller, state identity, registry generation, and frozen receipt before applying effects.

## Opening branches

The human and hidden-AI openings share the same four branch affordability gates and cost ledger.

1. Strict Cordon spends Medicine `3`, Fuel `1`, and Recognition `1`.
2. Medical Checkpoints spends Medicine `2`, Scrap `1`, and Power `1`.
3. Controlled Evacuation spends Medicine `4`, Fuel `2`, and Shelter Capacity `2`.
4. Local Self-Control spends Food `2`, Medicine `1`, and Recognition `2`.

The human option order is the deterministic tie order. Hidden AI uses the same affordability checks and authored priorities of `58`, `64`, `52`, and `46`, with strict-greater replacement so an equal score preserves the earlier branch.

The accepted opening records one branch choice in survivor memory `9175`, freezes the current Air Winter ledgers, records the owner and controller, reserves the state, and schedules a result after exactly `21` days.

## Deterministic result

The result grade is bounded from `0` through `100`. It combines current Supply Access, Shelter Capacity, Adaptation, Reclamation, inverse Disease Pressure, inverse Exposure, Medicine, Cohesion, and a Quarantine government bonus. Each branch has distinct success and partial thresholds.

Success, partial, and failure apply branch-specific deltas to Disease Pressure, Shelter Capacity, Exposure, Adaptation, Reclamation, Supply Access, Medicine, Cohesion, Recognition, and the selected branch ledger. They also update public-health, grievance, and cause-memory values on the country. The state applies the Air Winter disease modifier after clamping all five affected Air Winter ledgers.

Failure damages one repairable infrastructure level and sends a bounded `0.1` percent state population request through `apply_exact_state_civilian_population_loss` with the `fallout_aftermath` Deaths cause. The minimum remaining population floor is `100` people. Partial and success results do not call Deaths.

The result writes a branch outcome history payload and schedules a callback after exactly `180` days. Result modifiers last `120` days. The callback modifiers last `240` days.

## Callback and cleanup

The callback grade reads public health, Cohesion, Recognition, cause memory, grievance, the selected branch ledger, current Supply Access, Reclamation, and Disease Pressure. Success, partial, and failure update all seven country ledgers, the Air Winter state ledgers, Medicine, Recognition, Cohesion, Supply Access, and the branch memory.

Callback failure sends a separate bounded `0.05` percent population request through the same Deaths helper, again preserving the minimum remaining population floor. Callback effects write the callback history payload only after the delayed receipt is accepted.

The cleanup event consumes the authenticated cleanup ticket. It first releases callback cleanup and then the result cleanup when necessary. Only after both receipts are released does it clear state reservations, pending flags, transaction variables, frozen values, and temporary cost state. It preserves the durable branch ledgers, public-health memory, grievance, cause memory, and the closed state-memory flag. Repeating cleanup is idempotent because the release and closed receipts gate every mutation.

## Presentation and ownership

The dedicated report asset is `GFX_report_event_fallout_first_red_line`, backed by `gfx/event_pictures/fallout/report_event_fallout_first_red_line.dds`. Source, processed image, prompt, manifest, review notes, and GFX handoff live under `docs/assets/684_first_red_line/`.

Player-facing text names the Quarantine State, the ash road, the clinic, the wards, and the chosen policy. The Event Log name and payload detail route through history `9175` and dedicated scripted localisation. These survivor memories are not a registration of the Fallout consequence itself.

## Proof boundary

Static proof is recorded in `docs/plans/air_cleanliness_fallout_plans/FALLOUT_FIRST_RED_LINE_CHAIN_PROOF.md`. The proof covers identifiers, target shape, generation receipts, branch costs, deterministic grading, delayed timing, hidden-AI parity, Deaths integration, asset wiring, localisation, Event Log routing, and cleanup. Engine runtime delivery, multiplayer host authority, save recovery execution, and player-visible rendering remain unproven because Hearts of Iron IV is not launched for this task.
