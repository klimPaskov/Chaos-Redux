# Fallout The First Red Line chain proof

## Scope and consequence boundary

The First Red Line is candidate `684` in the dormant Fallout-owned survivor scheduler.

It is an ordinary post-consequence Quarantine country chain about a fever-struck settlement, an ash road, and the first public-health cordon.

It does not request Fallout, start the blackout, perform the thermonuclear sweep, delete transition population, alter the permanent `99` percent Air Contamination lock, or register the Fallout consequence as an Event Log event or evolution.

Its Event Log records are survivor memories written by the chain after the consequence boundary has completed.

The seven blocks use `chaosx.fallout.684` through `chaosx.fallout.690`.

The human opening is `684`.

The hidden-AI opening is `685`.

The visible and hidden-AI delayed results are `686` and `687`.

The visible and hidden-AI callbacks are `688` and `689`.

Cleanup is `690`.

The candidate uses transaction `710069`, route `7170`, and survivor-memory history `9175`.

The route upper bound is `7171`.

Both scheduler activation flags remain unset.

The chain is not release-floor credit and does not claim runtime acceptance.

## Native target and admission

The producer selects the lowest owned native state id that passes `fallout_event_pilot_first_red_line_state_is_current`.

The state gate requires a current state identity row, durable state-resource row, current Supply Access, a produced Air Winter snapshot from the current Fallout generation, surviving population, Shelter Capacity at least `20`, Supply Access at least `15`, Adaptation at least `5`, Disease Pressure from `20` through `84`, Exposure below `75`, and Air Winter phase from `1` through `6`.

The owner must be a current Fallout registry country with durable survival resources, the Quarantine government archetype, campaign days from `365` through `4499`, Medicine at least `5`, Cohesion at least `20`, Recognition at least `5`, and one complete affordable branch.

The producer stores the selected native state id in the candidate row. It sets the row's Air Winter pressure source, Quarantine government requirement, Medicine resource requirement, first-winter requirement, route identity, state target type, and current phase value. It does not invent a state, province, country, actor, partner, or fallback target.

Opening entry rehydrates the typed state target from the ordinary dispatch envelope and repeats the country, owner, controller, identity, resource, Air Winter, generation, and affordability checks.

## Branch contract

Strict Cordon spends Medicine `3`, Fuel `1`, and Recognition `1`.

Medical Checkpoints spends Medicine `2`, Scrap `1`, and Power `1`.

Controlled Evacuation spends Medicine `4`, Fuel `2`, and Shelter Capacity `2`.

Local Self-Control spends Food `2`, Medicine `1`, and Recognition `2`.

The four branch affordability triggers are complete and exhaustive. A failed delayed transaction refunds the selected branch cost before releasing the state reservation.

The human option order is the tie order. Hidden AI uses the same affordability checks with authored priorities `58`, `64`, `52`, and `46`, and strict-greater replacement. It therefore chooses deterministically without a random block or a weighted fallback.

## Deterministic result and delayed callback

The accepted opening freezes the current Air Winter generation, owner, controller, Shelter Capacity, Supply Access, Adaptation, Reclamation, Exposure, and Disease Pressure. It also stores the selected branch, target state, result generation, result day, and cleanup receipt.

The result arrives after exactly `21` days.

The bounded grade combines Supply Access, Shelter Capacity, Adaptation, Reclamation, inverse Disease Pressure, inverse Exposure, Medicine, Cohesion, and the Quarantine government bonus. Every branch has distinct success and partial thresholds.

Result success, partial, and failure update Disease Pressure, Shelter Capacity, Exposure, Adaptation, Reclamation, Supply Access, Medicine, Cohesion, Recognition, public health, grievance, cause memory, and the selected branch ledger. The state applies the Air Winter disease modifier after clamping the affected ledgers.

Result failure damages one repairable infrastructure level and sends a `0.1` percent state population request through `apply_exact_state_civilian_population_loss` with cause `fallout_aftermath`. The Deaths helper receives a `100` person minimum remaining floor. Partial and success do not send a Deaths request.

The result records one branch outcome payload in history `9175`, then schedules the callback after exactly `180` days. Result modifiers last `120` days.

The callback grade uses public health, Cohesion, Recognition, cause memory, grievance, the selected branch ledger, current Supply Access, Reclamation, and Disease Pressure. Callback success, partial, and failure update the same durable country and Air Winter state surfaces.

Callback failure sends a `0.05` percent state population request through the same Deaths helper and preserves the `100` person floor. Callback modifiers last `240` days.

The callback records its outcome payload only after the delayed receipt is accepted.

## Event Log, localisation, and asset proof

History `9175` contains four branch-choice payloads, twelve branch-result payloads, three callback payloads, and one cancellation payload.

The shared Event Log name router maps history `9175` to `fallout.event_log.first_red_line.name`.

The shared Event Log detail router maps history `9175` to `fallout.event_log.first_red_line.detail`, which calls `GetFalloutEvent684EventLogDetail`.

Every payload maps to a dedicated localisation key. The player-facing opening, result, callback, option names, tooltips, Event Log title, and Event Log details are present in `localisation/english/fallout_consolidated_l_english.yml`.

The report sprite is `GFX_report_event_fallout_first_red_line`.

The runtime texture is `gfx/event_pictures/fallout/report_event_fallout_first_red_line.dds` with `210x176` dimensions and exact byte length `147968`.

Source, processed image, prompt, review notes, manifest, and GFX handoff are under `docs/assets/684_first_red_line/`.

No zombie or Final Silence id, file, asset, audio, sprite, or path is reused.

## Cleanup and proof boundary

Cleanup consumes the authenticated cleanup ticket and releases callback cleanup before result cleanup when both are present. It clears transaction receipts, frozen values, reservations, pending flags, temporary cost state, and open-chain flags only after both receipts are released. It writes the closed state-memory flag and preserves durable branch ledgers, public-health memory, grievance, and cause memory. Repeated cleanup is idempotent because ticket-release and closed receipts gate the mutation path.

Static source review covers unique ids `684` through `690`, unique transaction `710069`, unique route `7170`, unique history `9175`, seven event blocks, four complete affordability branches, deterministic hidden-AI parity, exact `21` and `180` day timing, Deaths integration, state-ledger effects, dedicated report art, localisation references, Event Log routing, current-generation revalidation, and dormant scheduler ownership.

Engine runtime delivery, multiplayer host authority, save recovery execution, delayed queue delivery, player-visible rendering, and Deaths readback remain runtime-unproven because Hearts of Iron IV was not launched.

The exact engine-native all-valid-province thermonuclear sweep remains a separate Fallout consequence blocker and is not claimed by this chain.

Candidate `684` remains dormant and receives no release-floor credit.
