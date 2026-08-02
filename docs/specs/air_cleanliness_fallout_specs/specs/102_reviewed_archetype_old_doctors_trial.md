# Reviewed Archetype: The Old Doctor's Trial

The Old Doctor's Trial is a fictional Congo Green Basin mutant-polity chain about accountability after a clinic director's coercive treatment and forged-consent records are discovered. It follows the closed Fertility Question memory and treats altered society as fictional civic history. The records do not establish ordinary radiation biology, and the chain never presents mutation as a diagnosis or a real-world medical claim.

The dormant runtime package uses human and hidden-AI events `chaosx.fallout.1023` and `chaosx.fallout.1024`, delayed result events `chaosx.fallout.1025` and `chaosx.fallout.1026`, callback events `chaosx.fallout.1027` and `chaosx.fallout.1028`, and cleanup event `chaosx.fallout.1029`. Its scheduler candidate id is `901`, transaction key `710100`, route `7232`, and Event Log history id `9206`. Fallout remains a consequence rather than an ordinary event, evolution, scenario log entry, or super-event.

## Candidate boundary

The row is eligible after campaign day `1600` and before day `11000` when the country retains the Congo Green Basin memory and the `mutant_polity` government archetype. The country must have current registry and survival-resource rows, Medicine at least `14`, Cohesion at least `32`, Recognition at least `18`, trial legitimacy at least `55`, atrocity pressure at least `5`, and at least one affordable branch. The country must not already have an open, committed, pending, or closed Old Doctor's Trial chain.

The scheduler selects the lowest owned state whose population exceeds the minimum, Air Winter Shelter is at least `22`, Supply Access is at least `16`, Adaptation is at least `18`, Disease Pressure is at least `20` and below `90`, Exposure is at least `10` and below `90`, and the Air Winter phase is between phase one and phase six. The state must have durable identity, survival-resource, and Supply Access rows, and must have a foreign neighboring state with a current identity row. The state also carries the closed `fallout_event_894_memory_closed` flag from The Fertility Question. Controlled evacuation flags block selection.

The opening candidate freezes the owner, controller, transition generation, selected ward, Air Winter values, Supply Access, and the lowest eligible foreign witness state. Every result, callback, and cleanup lane revalidates those receipts. A changed owner, controller, state, witness, generation, or durable row cancels the chain and lets authenticated cleanup release the reserved rows.

## Branches

| Branch | Cost | Civic direction |
| --- | --- | --- |
| Open a public trial | Food `2`, Medicine `3`, Recognition `2` | River and hill witnesses hear the consent failures in a public ward proceeding. |
| Convene a truth commission | Scrap `2`, Power `2`, Recognition `2` | Three archives preserve statements and expose the clinic network. |
| Pardon the doctor for retained knowledge | Fuel `1`, Recognition `2`, Cohesion `1` | The former director keeps supervised clinical work under two-witness review. |
| Keep the records under seal | Food `1`, Medicine `1`, Fuel `1`, Recognition `1` | A guarded archive protects witnesses while limiting public access to the record. |

The opening choice is paid once through a country flag and is refunded only on a failed queue transaction. The option trigger prevents a branch from appearing unless its exact survival-resource and Cohesion requirements are met.

## Grading and delayed consequences

The deterministic result grade weights frozen Supply Access, Shelter, Adaptation, Disease Pressure relief, Exposure relief, Medicine, Recognition, trial legitimacy, atrocity-pressure relief, medicine trust, and refugee-pressure relief. The mutant-polity archetype receives a small explicit bonus. Each branch has separate success and partial thresholds, with failure as the remaining outcome.

Result effects change the five Air Winter state ledgers, Supply Access, Medicine, Cohesion, Recognition, and the country ledgers for trial legitimacy, atrocity pressure, medicine trust, witness confidence, refugee pressure, doctor fatigue, and trial cause memory. Success, partial, and failure write separate branch memories. Failure uses the established Deaths request contract with a bounded percentage and a minimum remaining population. Bilateral opinion modifiers distinguish public trial, truth commission, supervised pardon, sealed retention, and register failure.

The result transaction resolves after exactly `56` days. It schedules a callback after exactly `420` days. The callback grades trial legitimacy, Cohesion, Recognition, medicine trust, witness confidence, trial cause memory, atrocity pressure, refugee pressure, doctor fatigue, and current state Supply Access, Reclamation, and Disease Pressure. Callback outcomes again alter Air Winter, Supply Access, survival resources, civic stability, and the country ledgers. Callback failure uses a separate bounded Deaths request. The state memory closes only after both delayed transactions and their cleanup receipts settle.

Human and hidden-AI lanes share branch legality, costs, deterministic grading, result timing, callback timing, bilateral memory, and cleanup. AI branch priorities prefer truth commission, supervised pardon, sealed retention, and public trial according to the authored constants, while invalid branches are rejected. No lane creates a country, changes a government archetype, requests Fallout, transfers population between states, or adds a recurring scheduler.

## Characters and fictional boundaries

The accused former director, river midwives, hill delegates, and foreign witness are represented as authored event roles and durable country and state memory flags. No real person or grounded historical leader is invented. A future character package may promote one of these roles into a scripted character only after a separate accepted character specification and portrait manifest exist.

## Runtime surfaces and assets

Gameplay constants live in `common/script_constants/fallout_world_end_old_doctor_trial_constants.txt`. Triggers and effects live in `common/scripted_triggers/fallout_world_end_old_doctor_trial_event_triggers.txt` and `common/scripted_effects/fallout_world_end_old_doctor_trial_event_effects.txt`. The shared candidate producer is `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.

Dynamic modifiers, opinion modifiers, Event Log routing, events, and localisation use dedicated Old Doctor's Trial names. The fictional report image source, processed preview, manifest, and GFX handoff are under `docs/assets/901_old_doctor_trial/`. Runtime art is `gfx/event_pictures/old_doctor_trial/report_event_fallout_old_doctor_trial.dds` registered as `GFX_report_event_fallout_old_doctor_trial`.

The chain is dormant and contributes no release-floor block until the Fallout scheduler's activation review opens it. Focused source inspection may prove syntax and helper references, but it does not claim HOI4 runtime acceptance, multiplayer behavior, host authority, save recovery, full-screen blackout delivery, or the exact engine-native province sweep.
