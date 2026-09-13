# Event 021 independent probability, AI, timing, and recurrence audit

Audit date: 2026-09-01.

Audit mode: read-only independent subagent pass.

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Certification: **FAIL / UNRESOLVED** for this requested slice.

The source review proves several deterministic lifecycle gates, but the sponsor decision adapter did not expose a complete live candidate pool and no named sponsor scenario reached `hoi4.probability_evaluate`. The evolution-effects path named by the request is absent, the timing render exceeded the bounded wait, and the AI-strategy adapter was not inspected before the parent-directed MCP stop. No exact selection probability, MTTH distribution, or campaign recurrence rate is claimed.

## Audited scope

The requested scenario ids were `EVO1-01`, `EVO1-02`, `EVO2-01`, `EVO2-02`, `EVO3-01`, `EVO3-02`, `SPN-01`, `SPN-02`, `SPN-03`, `SPN-04`, `SPN-05`, `REC-01`, `REC-02`, `REC-03`, `REC-04`, `REC-05`, and `REC-06`.

The exact source families read were:

- `common\decisions\021_random_civil_war_decisions.txt`.
- `common\ai_strategy\021_random_civil_war_ai_strategy.txt`.
- `common\scripted_effects\021_random_civil_war_effects.txt`.
- `common\scripted_effects\021_random_civil_war_parent_effects.txt`.
- `common\scripted_triggers\021_random_civil_war_triggers.txt`.
- `common\scripted_triggers\021_random_civil_war_parent_triggers.txt` as the direct helper family for the requested decision and recurrence gates.
- `common\script_constants\021_random_civil_war_constants.txt`.
- `common\on_actions\chaosx_on_actions_chaos_meter.txt` as the direct caller establishing the global pulse cadence.
- `events\021_random_civil_war.txt` for the hidden evolution callback events.

The requested `common\scripted_effects\021_random_civil_war_evolution_effects.txt` does not exist. The current evolution helpers are in `common\scripted_effects\021_random_civil_war_effects.txt` and `common\scripted_effects\021_random_civil_war_parent_effects.txt`; this missing file is a structural blocker, not a substitute path silently treated as equivalent.

Relevant source identifiers and locations are:

- `event021_parent_global_scheduler_pulse` and `event021_parent_process_evolution_schedule` in `common\scripted_effects\021_random_civil_war_parent_effects.txt:311` and `:479`.
- `event021_parent_review_recurrence_window` in `common\scripted_effects\021_random_civil_war_parent_effects.txt:567`.
- `event021_parent_apply_evolution_i`, `event021_parent_apply_evolution_ii`, and `event021_parent_apply_evolution_iii` in `common\scripted_effects\021_random_civil_war_parent_effects.txt:4893`, `:4916`, and `:4948`.
- `event021_apply_evolution_i`, `event021_apply_evolution_ii`, `event021_apply_evolution_iii`, and `event021_prepare_recurrence` in `common\scripted_effects\021_random_civil_war_effects.txt:1371`, `:1389`, `:1409`, and `:1851`.
- `event021_support_government`, `event021_support_opposition`, `event021_offer_mediation`, and `event021_end_sponsor_commitment` in `common\decisions\021_random_civil_war_decisions.txt:380`, `:419`, `:458`, and `:493`.
- `event021_parent_sponsor_candidate`, `event021_country_can_manage_exposure`, `event021_exposure_government_target_valid`, `event021_exposure_opposition_target_valid`, and `event021_parent_recurrence_window_open` in `common\scripted_triggers\021_random_civil_war_parent_triggers.txt:154`, `:585`, `:606`, `:621`, and `:543`.
- `random_civil_war_recurrence_valid` in `common\scripted_triggers\021_random_civil_war_triggers.txt:644`.

## Result-classification key

`Exact lifecycle` means the source gate or state transition is deterministic under the stated flags and dates.

`Bounded` means a deterministic date window or review cadence is present, but the external state that reaches it is not fully declared.

`Score-only` means the source contains an AI score expression, not a normalized click or selection probability.

`Unresolved` means the required MCP adapter, complete pool, external factor, or scenario evaluation was unavailable or incomplete.

## Scenario results

| Scenario | Current source result | Candidate pool and external factors | Evidence classification |
|---|---|---|---|
| `EVO1-01` | Evolution I is processed on the first global-host pulse after the tier-I unlock flag is published. Large war size, low authority, and an extra valid actor do not appear in the activation gate. | No pool applies because no weighted timing surface was discovered. The matrix factors are not consumed by the schedule. | Exact lifecycle gate; expected faster timing unresolved. |
| `EVO1-02` | Evolution I uses the same unlock-and-not-recorded gate as `EVO1-01`. Near defeat and the absence of an extra region do not create a slower MTTH branch. | No pool applies. The matrix factors are not consumed by the schedule. | Exact lifecycle gate; expected slower timing unresolved. |
| `EVO2-01` | Evolution II is processed on the first global-host pulse after the tier-II unlock flag is published, after the wrapper calls Evolution I. Exposure then iterates eligible immediate neighbors of active fronts. | No pool applies. Border length, sponsor-route count, and survivor state are not timing weights. | Exact lifecycle gate; spread/timing expectation unresolved. |
| `EVO2-02` | Evolution II has the same tier-II gate and does not check early settlement or neighbor strength before activation. A settled or inactive front can prevent downstream exposure, but that is a deterministic state consequence rather than a slow probability. | No pool applies. Settlement and neighbor strength are not declared timing modifiers. | Exact lifecycle gate; expected slow/no-spread timing unresolved. |
| `EVO3-01` | Evolution III is processed on the first global-host pulse after the tier-III unlock flag is published, after the wrappers call Evolution I and II. It activates the global threat source and leaves country launches to the bounded registry/critical queue. | No pool applies. The “normal shared MTTH” expected by the matrix is not present in the inspected schedule. | Exact lifecycle gate; normal timing unresolved. |
| `EVO3-02` | If Evolution III is already active, the core apply effects do not re-set the active state or date. The parent wrappers still backfill any missing unrecorded stage rows once, in order, through the `*_recorded` guards. | No pool applies. Prefire active flags are not enough to prove that corresponding historical receipt flags already exist. | Exact conditional lifecycle; duplicate safety conditional on recorded flags. |
| `SPN-01` | A major exposed neighbor is assigned the opportunistic sponsor profile. Government and opposition support each have base score `1` multiplied by `1.5`; mediation has base score `1` multiplied by `0.75`. | MCP reported `poolComplete:false`, zero available candidates, three unresolved inputs, and no scenario evaluation. Target scope, aligned-side viability, and live resources were incomplete. | Score-only source trace; unresolved sponsor result. |
| `SPN-02` | Support decisions have exact availability gates of 20 political power, 200 infantry equipment, and 5 convoys. Mediation has gates of 20 political power, 10 command power, and 5 convoys. The AI score blocks contain no explicit desperate-war or low-equipment modifier. | The adapter could not prove which candidates remain eligible under the declared resource state. | Exact availability gates; score-only AI trace; selection unresolved. |
| `SPN-03` | Both support decisions use the same profile factors, so rival sponsors and opposing viable sides do not receive distinct side-sensitive AI scores. `event021_neighbor_action_used` limits the recipient action path, while the commitment helper uses a 120-day commitment and support amount `1`. | No complete rival-sponsor pool or sponsor-cap state was exposed by MCP. | Score-only; competitive ranking and cap behavior unresolved. |
| `SPN-04` | Sponsor-candidate validity checks a normal human, non-capitulated, non-reserved country with more than zero factories. Exposure target validity checks active side/host scopes, but the decision gates do not directly require an administration or survival path. | Administration factories, survival path, and target viability were not complete external inputs. Positive support scores can therefore remain source-possible when the broader matrix says recognition and large aid should be suppressed. | Exact source gate; exploit/starvation risk unresolved by MCP. |
| `SPN-05` | A non-major exposed neighbor above stability `0.65` receives the mediator profile. Mediation is multiplied by `1.5`, while both support choices are multiplied by `0.75`; support is discouraged but not zeroed. | Complete target-scope and resource inputs were unavailable, and no normalized action probability was produced. | Score-only; mediator preference bounded, military suppression unresolved. |
| `REC-01` | Recurrence is a boolean eligibility gate after the earliest date, not a low MTTH or low random weight. Government-victory or coalition settlement adds a `-20` score contribution, but completed disarmament and high authority are not direct recurrence-relief terms in `event021_prepare_recurrence`. | No pool applies. Residual fracture pressure, memory, review registration, reconstruction, and external state were not fully declared. | Exact lifecycle/score gate; “very low recurrence” probability unresolved. |
| `REC-02` | Failed settlement adds `+20`, settlement violation or breached obligation adds `+25`, sponsor evidence or commitment adds `+10`, and recurrence is eligible once the score reaches threshold `45` inside the window and outside successor grace. | No pool applies. The threshold and window are source-complete, but scheduler registration and live postwar flags were not supplied to an analyzer. | Exact lifecycle/score gate; “high recurrence” frequency unresolved. |
| `REC-03` | `random_civil_war_recurrence_valid` rejects `random_civil_war_successor_grace`; the parent review also holds the next review at the grace end. This makes the recurrence path ineligible during grace rather than merely unlikely. | No pool applies. The exact grace flag and date would be sufficient for the gate, but no probability adapter is applicable. | Exact lifecycle zero/invalid gate; not a probability claim. |
| `REC-04` | A partition or maintained armistice has no dedicated branch in the recurrence score. Violations add `+25`, while residual pressure and other persistent flags continue to control threshold eligibility. | No pool applies. Partition, armistice, violation, and review cadence were not represented as a complete weighted state because no recurrence weight exists. | Exact source behavior; expected low/moderate result unresolved. |
| `REC-05` | A generic settlement violation or breached obligation adds `+25`, but there is no autonomy-guarantee-specific recurrence factor. The increase alone does not guarantee threshold `45`. | No pool applies. The exact autonomy-guarantee state and residual pressure were not analyzer inputs. | Exact score contribution; strong-recurrence outcome unresolved. |
| `REC-06` | `random_civil_war_recurrence_valid` requires a normal human country, and the parent scheduler also requires that predicate. A nonhuman successor is therefore excluded from recurrence. | No pool applies. This is a deterministic validity exclusion. | Exact lifecycle zero/invalid gate; not a probability claim. |

## Source-backed findings

### Evolution timing

`event021_parent_global_scheduler_pulse` calls `event021_parent_process_evolution_schedule` after runtime initialization, Chaos-tier synchronization, and capacity refresh at `common\scripted_effects\021_random_civil_war_parent_effects.txt:311-320`.

The existing Chaos meter `on_daily` host path calls that parent pulse at `common\on_actions\chaosx_on_actions_chaos_meter.txt:10-35`, with tag-switch and no-player fallbacks at `:37-90`.

`event021_parent_process_evolution_schedule` only tests `random_civil_war_evolution_i_unlocked`, `random_civil_war_evolution_ii_unlocked`, and `random_civil_war_evolution_iii_unlocked`, each against its corresponding `*_recorded` flag at `common\scripted_effects\021_random_civil_war_parent_effects.txt:479-500`.

The core effects set active flags and activation dates at `common\scripted_effects\021_random_civil_war_effects.txt:1371-1425`; they do not contain MTTH modifiers, candidate normalization, or scenario-specific timing factors.

The declared `evolution_minimum_days = 60` and `evolution_maximum_days = 180` constants are present at `common\script_constants\021_random_civil_war_constants.txt:326-339`, but no use was found for them in the named Event 021 evolution schedule files and no `mtth:` block was found in the inspected evolution wrappers.

Evolution I, II, and III parent wrappers record their event-log rows only when the active flag exists and the corresponding recorded flag is absent at `common\scripted_effects\021_random_civil_war_parent_effects.txt:4893-4967`.

The Evolution II wrapper deterministically iterates the active-theater array and calls exposure propagation for each active front side at `common\scripted_effects\021_random_civil_war_parent_effects.txt:4916-4940`; this is not a probability-proportional sponsor or spread pool.

The Evolution III wrapper activates the global threat source but does not itself launch countries at `common\scripted_effects\021_random_civil_war_effects.txt:1406-1425` and `common\scripted_effects\021_random_civil_war_parent_effects.txt:4945-4967`.

### Sponsor AI and validity

The three exposure decisions are source-weighted `ai_will_do` blocks, but they are score races rather than normalized click probabilities.

`event021_support_government` and `event021_support_opposition` use `base = 1`, `priority_major = 1.5` for the opportunistic sponsor profile, and `discourage_repression = 0.75` for the mediator profile at `common\decisions\021_random_civil_war_decisions.txt:412-455`.

`event021_offer_mediation` uses `base = 1`, `priority_major = 1.5` for the mediator profile, and `discourage_concession = 0.75` for the opportunistic sponsor profile at `common\decisions\021_random_civil_war_decisions.txt:486-490`.

`event021_end_sponsor_commitment` uses `base = 1` and the negotiator factor `1.5` at `common\decisions\021_random_civil_war_decisions.txt:521-524`; it is a settlement/disengagement action and was not included in the five sponsor scenarios except in the inspected candidate-boundary request.

Major status deterministically assigns the opportunistic profile, while non-major stability above `0.65` assigns the mediator profile and the remaining exposed neighbors receive containment at `common\scripted_effects\021_random_civil_war_parent_effects.txt:4821-4837`.

The supporting AI strategy profiles are source-only in this audit because their dedicated `ai_strategy_factor` MCP inspection was not completed before the bounded stop. The relevant values are opportunistic sponsor `build_army 95`, infantry `80`, artillery `50`, and `avoid_starting_wars -35` at `common\ai_strategy\021_random_civil_war_ai_strategy.txt:118-128`; neutral mediator `avoid_starting_wars 150` and infantry `35` at `:107-116`; and containment `build_army 65`, infantry `50`, and `avoid_starting_wars 90` at `:95-105`.

Sponsor-candidate validity at `common\scripted_triggers\021_random_civil_war_parent_triggers.txt:154-166` requires a normal human, non-capitulated, non-active, non-reserved country with more than zero factories and either no subject status or a sponsor-side flag.

Exposure management at `common\scripted_triggers\021_random_civil_war_parent_triggers.txt:585-604` requires a normal human exposed neighbor and a live active source with a registered theater/front or same-tag contest, while the government/opposition target helpers at `:606-634` validate side and host/actor scope shape.

Those helpers do not directly prove the administration, survival, aligned-side, rival-sponsor, or low-equipment conditions named by the scenario matrix. The decision availability blocks do prove resource thresholds at `common\decisions\021_random_civil_war_decisions.txt:387-401`, `:426-440`, and `:462-475`.

### Recurrence

`event021_prepare_recurrence` starts from `random_civil_war_fracture_pressure`, adds post-war memory `+10`, failed settlement `+20`, violation/breached obligation `+25`, sponsor evidence/commitment `+10`, and authority-collapse pressure, then subtracts `20` for government victory or coalition settlement before clamping at `common\scripted_effects\021_random_civil_war_effects.txt:1851-1900`.

The recurrence threshold is `45`, the earliest window is `60` days, the latest window is `180` days, and successor grace is `45` days at `common\script_constants\021_random_civil_war_constants.txt:336-344` and `:634-645` plus the settlement tuning block.

`random_civil_war_recurrence_valid` requires a normal human, no terminal lock, no successor grace, no expired window, dates inside the stored window, no still-blocking recent target, and a score at least `45` at `common\scripted_triggers\021_random_civil_war_triggers.txt:644-677`.

`event021_parent_review_recurrence_window` clears grace after its deadline, expires after the latest date, and sets eligibility immediately when the deterministic validity trigger passes at `common\scripted_effects\021_random_civil_war_parent_effects.txt:567-641`.

When recurrence is invalid while the window is open, the parent schedules the next review `stable_review_days = 120` later at `common\scripted_effects\021_random_civil_war_parent_effects.txt:599-613`. A review late in a 180-day window can therefore be scheduled after the latest date and miss the remaining opportunity before the next expiry check; this is a recurrence starvation risk, not a measured probability.

The recurrence code contains no `ai_will_do`, `ai_chance`, `random_list`, or MTTH selection for the requested scenarios. REC-03 and REC-06 are exact invalid-gate results; the other recurrence labels are score/eligibility behavior and cannot be translated into “high,” “low,” or “moderate” probabilities from the current implementation.

## MCP calls and preserved evidence

All calls below used workspace id `current`, which resolved to `mod_chaos_redux_ea3b2d67c2c0` where a structured result was returned.

### 1. Broad evolution timing inspection

Exact call:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "event_mean_time_to_happen",
    "source": {"path": "common/scripted_effects/021_random_civil_war_parent_effects.txt"},
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: the call remained live through the bounded wait and its returned payload exceeded the available response context; no structured result, revision, hash, scenario hash, analysis id, or artifact URI was recoverable. This attempt is not used as positive analyzer evidence.

### 2. Narrow evolution timing inspection

Exact call:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "event_mean_time_to_happen",
    "source": {
      "identifier": "event021_parent_process_evolution_schedule",
      "path": "common/scripted_effects/021_random_civil_war_parent_effects.txt",
      "line": 479
    },
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: `status=ok`, `code=PROBABILITY_SOURCE_DISCOVERED`, `sourceRevision=3b697c40d7c38856a45ce5045338431d28ac2aaad3043d97e79335b11565b63a`, and `sourceHash=6d6a23e510f29da5ade41458b6772dc78e4f9eb057eb06507119a78fa4b64994`.

The returned discovery reason was `identifier_not_found`; the requested adapter had zero candidates, zero available candidates, zero required inputs, and zero unresolved inputs in this narrow selector, with no available adapter suggested.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/baaacbfeb39f4f9bf396021ef30a97387074575ca911535379539f1fa1cfbd0f/ac6a729ce4f8f1d6823555712db40458edb5d91e7977774ac9b433fb00a0a630/probability-inspect-6d6a23e510f2.json`.

This is the MCP evidence supporting deterministic/no-MTTH classification for the selected evolution scheduler identifier; it does not provide a timing probability.

### 3. Initial structural event-inspect validation error

Exact call intent was a downstream trace for `chaosx.nr21.11` using a selector with `identifier` and `path` but without the required selector discriminator.

Result: MCP error `-32602`, `Invalid arguments for tool hoi4.event_inspect: Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`.

The call was corrected immediately and the invalid request produced no evidence artifact.

### 4. Structural event trace

Exact call:

```json
{
  "tool": "hoi4.event_inspect",
  "arguments": {
    "mode": "trace",
    "selector": {"kind": "event", "eventId": "chaosx.nr21.11"},
    "direction": "downstream",
    "expandHelpers": true,
    "maxDepth": 4,
    "maxNodes": 120,
    "maxEdges": 240,
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: `status=ok`, `code=EVENT_INSPECTED_PARTIAL`, `revision=8cde42798e040fdadd5e86c2c299c46a8802c4ba48ebe7af4175cc8665b7864d`, and `graphHash=46db6136a16ab3119b59fa9c08b10cfb018dcbbdfbef7cdbaf77d618720da6e8`.

The bounded trace reported counts of `events=9725`, `options=15153`, `entries=1138`, `terminals=7771`, `edges=38341`, `stateAccesses=30319`, `unresolvedNodes=8698`, `issues=2206`, and `blockingDiagnostics=1`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da6cfaaa23657c9d1fea08dcce6c4f57a4efee12b8a23774f29a9e1c2c6a1764/e8edfc2d9b230fa71b8e5bc2ff177935e69ddf9d6dcd4740855dfe4ab3a77168/event-trace-8cde42798e04.json`.

Diagnostic: `MCP_INLINE_FILES_TRUNCATED`, with 368 inline paths and 64 returned. The structured result listed no top-level blockers, but the trace counts retain one blocking diagnostic and many unresolved nodes, so this is structural context rather than complete event-chain proof.

### 5. Structural timing render

Exact call:

```json
{
  "tool": "hoi4.event_render",
  "arguments": {
    "view": "timing",
    "selector": {"kind": "event", "eventId": "chaosx.nr21.11"},
    "direction": "downstream",
    "expandHelpers": true,
    "maxDepth": 4,
    "maxNodes": 120,
    "includeHtml": false,
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: the call remained live after the bounded waits and was terminated without a structured result or artifact URI. No rendered timing evidence is claimed.

### 6. Broad sponsor decision inspection

Exact call:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "decision_ai_will_do",
    "source": {"path": "common/decisions/021_random_civil_war_decisions.txt", "line": 380},
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: the call exceeded the bounded wait without a structured result and was terminated. No revision, hash, candidate set, or artifact from this attempt is used.

### 7. Narrow single-decision inspection

Exact call:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "decision_ai_will_do",
    "source": {
      "identifier": "event021_support_government",
      "path": "common/decisions/021_random_civil_war_decisions.txt",
      "line": 380
    },
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Result: the call exceeded the bounded wait without a structured result and was terminated. No evidence from this attempt is used.

### 8. Candidate-bounded sponsor inspection

Exact call:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "decision_ai_will_do",
    "source": {"path": "common/decisions/021_random_civil_war_decisions.txt", "line": 380},
    "candidatePool": [
      "event021_support_government",
      "event021_support_opposition",
      "event021_offer_mediation",
      "event021_end_sponsor_commitment"
    ],
    "refresh": false,
    "workspaceId": "current"
  }
}
```

Result: `status=ok`, `code=PROBABILITY_SOURCE_INSPECTED`, `adapterId=decision_ai_will_do`, `poolComplete=false`, `sourceRevision=71734ea9623dc0b43447072d978febac51f3a5e7a104c1009c2d17d1a2f65302`, and `sourceHash=b012bf7ee5789568875a8e9eb6c1fdb57ad206b1a9e04348eea9523070aa4b6d`.

The adapter reported `candidates=1`, `availableCandidates=0`, `availableAdapters=[]`, `requiredInputs=1`, and `unresolved=3`; it returned no candidate examples and no diagnostics or top-level blockers.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a2cecd1b5638cc84e23389db3e7650f7f394d3905e4647639803e7cd1b0ba4c/8d362cbb4e74f9c2b6778a51b3c86134ae1cf645c6fc201bc159fc42a75eaf1a/probability-inspect-b012bf7ee578.json`.

This result is an adapter discovery and pool-completeness result only. It is not a sponsor ranking or probability result.

## Skipped analyses and exact reasons

`hoi4.probability_evaluate` was not completed for `SPN-01` through `SPN-05` because the only completed sponsor inspection reported `poolComplete=false`, zero available candidates, one required unresolved input group, and three unresolved values. Continuing with an incomplete candidate/target scope would violate the complete-pool and external-factor contract, so all five sponsor outcomes remain unresolved rather than being fabricated.

`hoi4.probability_evaluate` was not issued for `EVO1-01` through `EVO3-02` or `REC-01` through `REC-06` because the completed evolution inspection found no MTTH surface and the source review found recurrence to be a deterministic validity/window gate rather than a weighted selection. The deterministic conclusions above are explicitly not probabilities.

`hoi4.probability_sweep` was skipped because no continuous weighted timing or complete decision surface was available after inspection. No sensitivity or rank-reversal result is claimed.

`hoi4.probability_compare` was skipped because this audit has no declared before/after source revision and the user expressly prohibited inventing a before revision. No comparison id exists.

`hoi4.probability_simulate` was skipped because no uncertain input distributions or valid complete candidate pool were declared. No seed, sample count, interval, or sampled timing result exists.

`hoi4.probability_sequence` was skipped because no complete custom weighted-pool manifest with cadence, state transitions, recovery, caps, cooldowns, removals, resets, and terminal states was declared. No manifest JSON body was created or used.

`hoi4.probability_render` was skipped because no evaluate, sweep, simulate, sequence, or compare analysis id was produced. The separate structural `hoi4.event_render` timing call was attempted and timed out as recorded above.

The required `ai_strategy_factor` inspection for `common\ai_strategy\021_random_civil_war_ai_strategy.txt` was not completed before the parent-directed stop. Its values are therefore source-only and cannot certify sponsor selection behavior.

No scenario hash, probability analysis id, probability-render artifact, comparison id, or custom-pool manifest exists for this handoff.

## Findings requiring owner review

1. The probability matrix describes faster, slower, and normal evolution timing, but the current scheduler is a daily deterministic Chaos-tier transition with no inspected MTTH or scenario-specific timing modifiers. Either the implementation needs a declared timing surface keyed to the matrix factors or the matrix must be rewritten in deterministic tier-gate terms.

2. `evolution_minimum_days` and `evolution_maximum_days` are declared tuning values without a discovered consumer in the named evolution schedule. Their intended contract should be made explicit before tuning.

3. Prefire Evolution III safety depends on the relationship between active flags and `*_recorded` flags. A prefire state with active flags but missing recorded flags causes one-time history backfill on the next scheduler pulse; a state with both active and recorded flags is idempotent. This should be accepted or explicitly normalized.

4. Sponsor AI has profile factors but no direct low-equipment, desperate-war, administration, survival-path, aligned-side, or rival-sponsor modifiers. The source validity gates should be checked against the matrix’s intended suppression semantics through a complete analyzer scenario.

5. Mediator support is discouraged by `0.75`, not suppressed to zero. The owner should decide whether “suppressed” means this bounded score reduction or an eligibility/weight-zero rule.

6. Recurrence is a thresholded deterministic gate, not a probability. The matrix’s “high,” “low,” and “moderate” recurrence language needs either a real timing/selection surface or a terminology change to score bands and eligibility windows.

7. Partition and armistice state has no dedicated recurrence branch, and autonomy-guarantee failure is represented only by the generic violation/breached-obligation contribution. If those distinctions are intended, they need explicit identifiers and scenario coverage.

8. The open-window invalid branch schedules the next review 120 days later, which can fall beyond the 180-day maximum window and starve a later valid recurrence opportunity. This is a concrete timing/recurrence risk for owner review.

These are recommendations only. No gameplay, AI, event, localisation, asset, workbook, configuration, or existing report file was edited, and no commit was made.

## Post-owner-patch evolution timing re-audit

Audit date: 2026-09-01.

Scope: `EVO1-01`, `EVO1-02`, `EVO2-01`, `EVO2-02`, `EVO3-01`, and `EVO3-02`, plus the recurrence retry clamp. This append is read-only with respect to gameplay and records the owner patch currently present in the shared workspace.

### Source identity and patch boundary

Repository base revision: `af53bc55e178af776e79d3c83dd131b29e988718`.

Current live file SHA-256 values:

- `common/mtth/021_random_civil_war_mtth.txt`: `74f9b639a53b2ddb1845db23bdcf72b5731b2562fa7740455f86480a54ce5623`.
- `common/script_constants/021_random_civil_war_constants.txt`: `8fc148a0d41777f2ca44b4f16409ee330ade7d641b6b77f41524a9850c047126`.
- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: `d49b7f7a9e38603876be6276f0c96ee20bfd28507a8432e150c6529d9a2e0da7`.

The prior deterministic baseline is the completed MCP inspection already recorded above: `sourceRevision=3b697c40d7c38856a45ce5045338431d28ac2aaad3043d97e79335b11565b63a`, `sourceHash=6d6a23e510f29da5ade41458b6772dc78e4f9eb057eb06507119a78fa4b64994`, discovery reason `identifier_not_found`, zero candidates, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/baaacbfeb39f4f9bf396021ef30a97387074575ca911535379539f1fa1cfbd0f/ac6a729ce4f8f1d6823555712db40458edb5d91e7977774ac9b433fb00a0a630/probability-inspect-6d6a23e510f2.json`. That baseline proved that the old `event021_parent_process_evolution_schedule` selector had no weighted MTTH surface and activated unlocked stages deterministically on the scheduler pulse.

The owner patch adds three source-backed MTTH entries. Their bases are 90, 135, and 120 days. `event021_parent_schedule_evolution_due_date` samples the relevant entry once, clamps the sampled delay to 60 through 180 days, and stores one absolute global due date. `event021_parent_process_evolution_schedule` requires Evolution I to be recorded before scheduling Evolution II and Evolution II to be recorded before scheduling Evolution III. Before any committed Event 021 opening, each unlocked and unrecorded stage instead activates immediately.

Candidate-pool completeness is not applicable to these MTTH entries because they are timing surfaces rather than normalized candidate selections. No custom manifest was created or used.

### Exact MCP call and bounded result

The mandatory first operation for the first live weighted source was:

```json
{
  "tool": "hoi4.probability_inspect",
  "arguments": {
    "adapter": "event_mean_time_to_happen",
    "source": {
      "identifier": "random_civil_war_evolution_i_days",
      "path": "common/mtth/021_random_civil_war_mtth.txt",
      "line": 5
    },
    "refresh": true,
    "workspaceId": "current"
  }
}
```

Bounded execution result: the call remained live after the initial 31-second execution window and one 31-second completion wait. It was then terminated. It returned no structured `status`, `code`, blockers, diagnostics, source revision, source hash, scenario hash, analysis id, unresolved count, or artifact URI. This is a tooling-route blocker, not probability evidence.

No second inspection retry was made. The parent instruction required completing the report rather than continuing open-ended analysis once the route was blocked.

### Scenario results

The formulas below are direct current-source traces. They are not substitutes for the blocked MCP probability analysis. A nominal MTTH is the source base multiplied by every modifier explicitly declared for the named scenario before the separate 60-to-180-day clamp is applied to the sampled delay.

| Scenario | Current source result | Evidence classification | MCP evidence state |
| --- | --- | --- | --- |
| `EVO1-01` | Failing authority, a large country, and an extra valid actor apply `90 × 0.75 × 0.85 × 0.75 = 43.03125` nominal days. The sampled delay is nevertheless clamped to at least 60 days. This source-wise supports Faster Evolution I relative to the 90-day base. | `score-only` formula plus source-exact 60-to-180-day bound | `unresolved`; first-tier inspect timed out and returned no analysis id or scenario hash |
| `EVO1-02` | Near defeat with no extra actor applies `90 × 1.50 × 1.35 = 182.25` nominal days. If the settlement-phase flag is also present, the nominal value is `255.15` days. The sampled delay is capped at 180 days. This source-wise supports Slow Evolution I. | `score-only` formula plus source-exact 60-to-180-day bound | `unresolved`; no legal evaluate followed the blocked inspect |
| `EVO2-01` | Border exposure, active sponsor commitment, and a surviving independence front apply `135 × 0.75 × 0.75 × 0.80 = 60.75` nominal days. If the multifront flag is additionally present, the nominal value is `51.6375` days before the minimum clamp. This source-wise supports Faster Evolution II. | `score-only` formula plus source-exact 60-to-180-day bound | `unresolved`; second-tier inspect was not started after the route blocker |
| `EVO2-02` | Settlement progress, a strong neighbor, and no exposure route apply `135 × 1.40 × 1.25 × 1.25 = 295.3125` nominal days, with the sampled delay capped at 180 days. This supports slow activation and can leave no Evolution II spread before an earlier war settlement, but settlement timing versus the stored due date remains campaign-dependent. | `score-only` formula plus source-exact 60-to-180-day bound; campaign ordering unresolved | `unresolved`; no legal evaluate followed inspection failure |
| `EVO3-01` | Severe or critical opening severity applies `120 × 0.80 = 96` nominal days. The sampled due date is bounded to 60 through 180 days and cannot activate until Evolution II is recorded. This source-wise supports the normal shared MTTH activation path. | `score-only` formula plus source-exact sequencing and 60-to-180-day bound | `unresolved`; third-tier inspect was not started after the route blocker |
| `EVO3-02` | With Evolution III unlocked and no committed Event 021 opening, the scheduler takes the immediate prefire branch. `event021_parent_apply_evolution_iii` calls the Evolution II and Evolution I apply helpers, while each log write is guarded by its corresponding `*_active` and `NOT *_recorded` conditions. The path is deterministic and does not sample the Evolution III MTTH. | `exact` deterministic lifecycle/source trace, not weighted | Not applicable; fabricating an MTTH evaluation for this bypass path would be incorrect |

All six requested scenario ids are therefore covered. Five have source-supported direction and hard delay bounds but remain MCP-unresolved as probability distributions. `EVO3-02` is explicitly deterministic.

### Evaluate, sweep, and compare disposition

`hoi4.probability_evaluate` was not called. The mandatory `probability_inspect` for `random_civil_war_evolution_i_days` did not complete, so proceeding to evaluation would violate the inspect-first workflow. Consequently there are no evaluation source revisions, scenario hashes, analysis ids, artifacts, or authoritative unresolved-input counts for `EVO1-01` through `EVO3-01`.

`hoi4.probability_sweep` was not called for the same blocker. The current source has meaningful sensitivity at the 60-day and 180-day clamps and at each modifier trigger, but no sweep result, breakpoint artifact, or elasticity is claimed.

`hoi4.probability_compare` was not called. The recorded before state is a genuine deterministic source with no weighted candidate, while the after state is a new MTTH source. The adapter compares two weighted surfaces under identical scenarios and cannot derive an event-timing delta from a before source that the prior inspection proved had zero MTTH candidates. In addition, the current weighted source never completed inspection. This is an unsupported cross-surface comparison plus a live route blocker, not an invented before revision. No comparison id, scenario hash, attribution artifact, or compare unresolved count exists.

The named scenario JSON was therefore not submitted to any MCP analysis and has no authoritative scenario hash. No manifest JSON body exists.

### Recurrence retry clamp

The earlier starvation defect is fixed source-wise. In `event021_parent_review_recurrence_window`, an open recurrence window that is currently invalid sets `random_civil_war_next_review_date` to the current date plus `stable_review_days`, then compares that value with `random_civil_war_recurrence_latest_date` and replaces it with the latest date when it would overshoot. Expiration uses `global.date > random_civil_war_recurrence_latest_date`, so a review scheduled exactly on the latest date still receives one final validity check before the window expires on a later pulse.

This is a deterministic lifecycle conclusion. It has no weighted pool, normalization, scenario hash, or probability artifact. It fixes the specific source-wise starvation path identified in the prior handoff, where the retry could jump beyond the latest date without a final in-window review.

### Verdict

The owner patch passes the source-level evolution timing design check: stages have distinct scenario-sensitive MTTH formulas, each committed-campaign stage samples one absolute due date, delay is bounded to 60 through 180 days, sequencing is enforced, and prefire activation remains immediate and idempotently recorded. The recurrence retry starvation issue is fixed source-wise.

This slice does not pass probability certification because the live `hoi4.probability_inspect` route did not return a structured result and therefore no evaluate, sweep, render, or supported compare evidence exists. The remaining certification blocker is tooling evidence, not a source-level timing defect found in this re-audit.

No gameplay, localisation, assets, workbook, configuration, or other report was edited, and no commit was made.
