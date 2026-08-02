# Fallout Battalion's Bread List chain proof

## Scope and consequence boundary

The Battalion's Bread List is candidate `677` in the dormant Fallout-owned survivor scheduler.

It is an ordinary post-consequence Food Compact country event about a military ration dispute.

It does not request Fallout, start the blackout, perform the strike sweep, delete transition population, alter the permanent `99` percent Air Contamination lock, or register the Fallout consequence as an Event Log event or evolution.

Its Event Log records are survivor memories written after the consequence has completed.

The seven blocks use `chaosx.fallout.677` through `chaosx.fallout.683`.

The human opening is `677`.

The hidden AI opening is `678`.

The visible and hidden delayed results are `679` and `680`.

The visible and hidden callbacks are `681` and `682`.

Cleanup is `683`.

The candidate uses transaction `710068`, route `7168`, and survivor-memory history `9174`.

The route upper bound is `7169`.

Both scheduler activation flags remain unset.

The current reviewed ordinary inventory is `68` rows and `558` defined blocks, with `0 of 660` countable blocks.

## Native target and prerequisite memory

The producer selects the lowest current owned state that passes `fallout_event_pilot_hungry_battalion_granary_state_is_current`.

The state must have a current Fallout identity, durable state resource row, current Supply Access, produced Air Winter snapshot, surviving population, bounded food reserve, bounded exposure and disease, and direct control by the requesting country.

The owner must be Food Compact eligible, retain minimum Cohesion, field more than the configured army-manpower floor, and afford at least one complete branch.

The state must carry one of the four Work for Rations branch flags.

Candidate 677 also requires the durable `fallout_event_670_policy_memory_generation` and `fallout_event_670_policy_memory_owner` receipt.

Work for Rations now writes that receipt with every resolved branch.

The new selector compares the receipt to the current Fallout generation and requesting owner.

This closes the stale-policy gap that existed when three Work for Rations branch flags carried no separate generation proof.

Opening entry rehydrates the typed state target from the issued dispatch envelope and repeats the owner, controller, resource, generation, army, and affordability checks.

There is no generic target fallback.

## Branch contract

The protected military issue spends Food `5`, Fuel `1`, Recognition `2`, and Command Power `6`.

It can improve battalion loyalty, organization, attack, and war support while raising civilian hunger and weakening civil-military trust.

One public measure spends Food `4`, Recognition `1`, and Command Power `3`.

It favors Cohesion, Stability, ration discipline, and trust while accepting lower military readiness.

Field requisition spends Fuel `2`, Medicine `1`, Recognition `2`, and Command Power `8`.

It can add food and military readiness quickly.

It imposes the largest trust loss and the largest bounded failure death rate.

Failure can damage one civilian factory in the selected state before the infrastructure fallback is considered.

Rear-echelon stand-down spends Food `2`, Medicine `1`, and Army Experience `8`.

It applies a `240` day penalty of `-30` percent army organization, `-25` percent army attack, `-15` percent army defense, and `-20` percent mobilization speed.

The result may release at most `1000` personnel on success or `500` on a partial outcome.

The durable `fallout_event_677_stand_down_personnel_released` receipt prevents a second personnel release.

No division is deleted.

No equipment is removed or refunded.

## Deterministic result and AI

The result arrives after exactly `28` days.

The branch grade has no random block.

It uses Food, Supply Access, Cohesion, Adaptation, Reclamation, ration discipline, battalion loyalty, civil-military trust, War Support, Army Experience, inverse Exposure, inverse Disease Pressure, and inverse civilian hunger.

The grade is bounded to `0` through `100`.

Every branch has distinct success and partial thresholds.

The accepted opening freezes Cohesion, War Support, Army Experience, ration discipline, battalion loyalty, civil-military trust, civilian hunger, state population, Supply Access, Exposure, Adaptation, Reclamation, Disease Pressure, and granary reserve under the authenticated transaction.

The hidden AI lane evaluates the same four affordability triggers and calls the same payment, grading, result, callback, history, and cleanup effects as the human lane.

Protected issue scores low battalion loyalty and high War Support.

Equal measure scores low Cohesion and low trust, with continuity and democratic bonuses.

Requisition scores severe food pressure and low trust, with military-authority bonuses.

Stand-down scores Adaptation, Reclamation, peace, and its Army Experience affordability.

Strict greater-than replacement keeps branch order as the deterministic tie break.

## Result, callback, and cleanup

Result effects update Food, Recognition, Cohesion, Stability, War Support, Command Power, Army Experience, Supply Access, Exposure, Adaptation, Reclamation, Disease Pressure, granary reserve, ration discipline, battalion loyalty, civil-military trust, civilian hunger, and the chosen state memory.

Failure calls `apply_exact_state_civilian_population_loss` with `fallout_aftermath` as the Deaths cause.

The branch-specific failure bands are `0.04` percent for protected issue, `0.025` percent for equal measure, `0.15` percent for field requisition, and `0.035` percent for stand-down.

These are bounded local losses inside a survivor chain.

They are separate from the Fallout transition's required `90` to `95` percent state population deletion.

The callback arrives after exactly `210` days.

It checks current Supply Access, Disease Pressure, granary reserve, civil-military trust, and civilian hunger.

Success preserves an accepted ration settlement.

Partial success preserves a contested settlement.

Failure records a ration crisis, applies a smaller Deaths-system loss, and adds the granary grievance modifier.

Field requisition carries an additional owner-state ledger with current generation and outcome.

Cleanup requires the issued cleanup ticket and current state registry.

It clears transaction receipts, frozen values, and the state reservation.

It preserves branch memories, review memories, the requisition ledger, the stand-down personnel receipt, and the four civil-military ledgers for later chains.

## Public history and presentation

The dedicated sprite is `GFX_report_event_fallout_hungry_battalion`.

It points to `gfx/event_pictures/fallout/report_event_fallout_hungry_battalion.dds`.

The DDS is an uncompressed `210x176` BGRA card with exact length `147968` bytes.

The source, processed image, decoded review image, prompt, hashes, contact sheet, and GFX handoff are under `docs/assets/677_hungry_battalion/`.

The final player title is The Battalion's Bread List.

The opening uses `GetFalloutEvent677RationAuthority` to name a food council, quartermaster command, emergency cabinet, elected ration board, or survival council from current government evidence.

History `9174` records four choices, twelve branch results, three callback results, and authenticated cancellation.

The shared Event Log name and detail routes point to `GetFalloutEvent677EventLogDetail`.

The Fallout consequence itself still has no Event Log or evolution row.

The authoritative workbook row is `Events!A259:M259` with identity `FALLOUT-677`.

Its evolution and World-End Scenario cells are blank.

The event catalog CSV was regenerated from the workbook.

## Static audit and engine-sensitive boundary

Static review confirms unique ids `677` through `683`, unique transaction `710068`, unique route `7168`, history `9174`, seven event blocks, four complete affordability paths, human and hidden-AI parity, exact `28` and `210` day timing, Deaths-system integration, dedicated art, complete localisation references, current-generation prerequisite memory, no scheduler activation setter, and no zombie or Final Silence path reuse.

The narrow Event Chain Viewer inspection produced linked source evidence with no blocking diagnostic.

Its workspace analysis remained partial because the repository graph exceeded the inline lifecycle-analysis limit.

That tool result is not runtime proof.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beb1895c0871379554f23da409b7f127978b13a20f4f9fe60204af411b7278d3/d96cca9c15bb29de3eb3d89a08ce3ba8b7ce3a196b3cee722fa63048f1c70a41/event-lint-a6aba9b1dea6.json`.

The probability inspector was also pointed at the dedicated effects file with the four branch names.

It found no compatible declared weighted pool because this chain uses explicit deterministic score comparisons rather than `random_list`, `ai_chance`, or a declared custom pool.

It therefore reported four unresolved supplied candidates and no validation failure.

The branch arithmetic, affordability gates, fixed-order tie break, and government modifiers were reviewed directly.

Probability inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2900b51280ead26de50e5addd2445e5ca27684e1f8020ddb34af8f49ce01e5ca/c88fdd6762463910ba8f0d8d23f663f8733a9879cc94f17984c519587c477a56/probability-inspect-afd73cd2b677.json`.

| Engine-sensitive surface | Static evidence | Status |
| --- | --- | --- |
| Event ids and namespace | Seven unique `chaosx.fallout` blocks in the dedicated event file | proven statically |
| Typed target persistence | Dispatch, generation, owner, controller, and cleanup receipts are present | runtime unproven |
| Delayed result and callback | Exact due-day constants and authenticated queue calls are present | runtime unproven |
| Save recovery | Cleanup and generation checks exist | runtime unproven |
| Multiplayer host authority | This chain consumes the shared coordinator | runtime unproven |
| Event Log rendering | History and scripted-localisation routes are wired | runtime unproven |
| DDS consumer rendering | Sprite, DDS, and decoded source review are complete | runtime unproven |
| Deaths readback | Exact population-loss API and cause are wired | runtime unproven |
| Full-screen blackout | Owned by the separate Fallout consequence coordinator | runtime unproven |
| All-valid-province thermonuclear sweep | No exact engine-native sweep proof is created by this tranche | blocker remains |

Hearts of Iron IV was not launched.

Candidate 677 remains dormant and receives no release-floor credit.
