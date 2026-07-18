# Event 019 AI, Balance, Performance, and Exploit Independent Audit

Date: 2026-07-16

Role: independent AI, balance, performance, exploit, and improvement-addendum auditor

Mode: read-only source audit. This handoff is the only file created. No gameplay,
localisation, asset, workbook, or export file was edited.

## Verdict

**Not closed.** The audited implementation has one P0 performance and
authorization finding. No additional P1 or P2 finding was found.

| Severity | Count |
| --- | ---: |
| P0 | 1 |
| P1 | 0 |
| P2 | 0 |

The three concrete remediation packages in the near-completion addendum are
present: the three release modes are real and mode-aware, the pre-fire
Evolution IV reception transaction is real and one-time, and the controlled
trial / inventory / fixed-visual documentation is reconciled. Those facts do
not clear the wider Event 019 completion gate because the current evolution
scheduler performs an unapproved recurring whole-world sample.

This report does not claim whole-event completion.

## P0 findings

### P0-019-PERF-01: the evolution scheduler performs an unapproved recurring `every_country` scan

#### Evidence

- The Event 019 performance specification permits one bounded world pass at
  event firing and states that **any whole-world recurring iteration requires
  explicit user permission**. Persistent management must remain country-scoped:
  `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md:935-950`.
- Each active participant's seven-day local pulse calls
  `infantry_spawn_maybe_advance_global_evolution` at
  `common/scripted_effects/019_infantry_spawn_pulse_effects.txt:63-66`. The local
  pulse cadence is `audit_pulse_days = 7` in
  `common/script_constants/019_infantry_spawn_constants.txt:32`.
- When the global due date is reached, the effect advances the date by the
  retry interval and calls `infantry_spawn_refresh_global_evolution_context`:
  `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:869-897`.
- That refresh effect executes `every_country` and derives war, participant,
  control, congestion, claimant, and anomalous-preservation counts from the
  entire world:
  `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:82-132`,
  especially line 92.
- Successful stage activation schedules another MTTH attempt. An unsuccessful
  due check retries after 30 days. The centralized cadence is 90 base days,
  clamped to 21-180 days, with a 30-day retry:
  `common/script_constants/019_infantry_spawn_constants.txt:172-200` and
  `common/mtth/019_infantry_spawn_mtth.txt:4-40`.
- The MTTH use itself is valid: the result is read through
  `mtth:infantry_spawn_evolution_interval`, clamped, and stored as a global due
  date at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:56-69`.
  MTTH scheduling changes cadence; it does not make the due action
  country-local or one-time.

The immediate due-date move prevents two countries from sampling the world on
the same day. It does not remove recurrence. Until all four evolutions are
active, the world scan can repeat every failed 30-day retry and after each
successful 21-180-day stage interval.

#### Impact

This is both an authorization violation and an avoidable runtime cost in a
global event that may have many active participant pulses. It contradicts the
specification's explicit-permission boundary and the repository rule that a
whole-world recurring iterator must not be implemented without the owner's
permission. Therefore Event 019 cannot pass the requested performance or
near-completion closure audit in its current form.

The finding is limited to the scheduled sampler at evolution-effects line 92.
The following global passes are not recurring and are not findings:

- the initial manifestation pass at
  `common/scripted_effects/019_infantry_spawn_core_effects.txt:472-508`;
- the one-time per-stage application passes at
  `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:775-848`;
- the action-triggered SCN-013 actor-selection passes at
  `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2916` and
  `:2929`.

No Event 019 daily, weekly, or monthly all-country on-action was found. The P0
exists because the delayed country-pulse/MTTH chain is still a recurring
whole-world iterator.

#### Required disposition

The parent must not silently substitute a weaker pacing model. Before a
completion claim, either:

1. replace the whole-world sample with a genuinely country-local or bounded
   participant-ledger design whose signals remain sufficient for all four
   evolution gates; or
2. obtain explicit user permission for the recurring world sample and then
   align the specification and performance documentation with the approved
   cadence and cost.

No such fallback or permission was assumed in this read-only audit.

## Addendum closure verdict

Source reviewed:
`docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`.

| Addendum finding | Independent verdict | Evidence and qualification |
| --- | --- | --- |
| 1. Separate ordinary claimant, anomalous claimant, and claimant-independent family release modes | **Mechanically closed** | `infantry_spawn_begin_selected_claimant_natural_revolt` starts in ordinary mode, only upgrades to anomalous mode when Evolution IV plus an eligible registry row exist, and falls back to ordinary mode when no row is found (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5485-5504`). `infantry_spawn_begin_natural_independent_family_breach` uses the independent-family mode with no claimant dependency (`:5468-5483`). Multi-state releases share the recreate/prove/delete transaction at `:5139-5292`; exact source deletion uses `delete_unit ... disband = no` only after replacement proof (`:3715-3789`); source/global accounting commits afterward (`:4400-4565`). The one-state route requires the whole live army to be the exact claimant-free selected family set before same-tag takeover (`:5294-5466`). Player and AI reach the same country-pulse effects. This finding's mechanics pass, but it does not override P0-019-PERF-01. |
| 2. Evolution IV pre-fire first-family reception | **Mechanically closed** | The entry path freezes one complete registry index, family, provider, visual profile, and monotonic nonce (`common/scripted_effects/019_infantry_spawn_evolution_effects.txt:463-501`), dispatches `.105` once or leaves a country-local pending retry (`:504-531`), and validates the frozen row before resolution (`:536-560`). `chaosx.nr19.105` exposes guarded cantonment, negotiated reception, and refusal options to player and AI with constant-backed AI factors (`events/019_infantry_spawn.txt:128-211`). Accepted routes use the registered provider snapshot/payment/materialization/proof/rollback transaction and grant one package; refusal grants none. Resolution state is written only after the outcome proves. Normal active-transition countries do not consume this pre-fire entry. This finding's reception path is local; the separate global evolution sampler remains P0. |
| 3. Controlled-trial, inventory, asset, blocker, and catalog reconciliation | **Closed at its intended pre-final status** | Direct source parsing gives 39 decisions + 11 missions in the main file, 6 claimant decisions, and 23 derivative decisions + 3 missions: exactly **68 decisions and 14 missions**. The four controlled-trial decisions and one trial mission are represented in the live map. Eleven Event 019 achievements exist in `common/achievements/chaos_redux_achievements.txt:3121-3233`. The repository contains 20 claimant source scenes, 6 derivative-host source scenes, 1 neutral source scene, 27 processed PNGs, 27 separate 156x210 runtime DDS files, and exactly 20 + 6 + 1 matching sprite definitions in `interface/019_infantry_spawn.gfx:51-158`. The blocker document identifies the owner-approved substitutes and keeps Event 019 and SCN-013 `In progress` pending a fresh whole-project audit (`docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md:161-170`). The exported catalog is also still `In progress`, which is correct while this P0 remains open; the workbook must not be promoted merely to make the addendum appear closed. |

Accordingly, the addendum's three implementation tranches exist and are not
paper-only claims. **Addendum-level readiness as a whole is not accepted**
because its AI/balance/performance evidence gate is independently failed by
P0-019-PERF-01.

## Balance, AI, exploit, and reachability evidence

### Diminishing territorial coverage

`infantry_spawn_calculate_selected_state_target` implements a joined,
monotonic count-space ladder with no fixed absolute cap at
`common/scripted_effects/019_infantry_spawn_core_effects.txt:14-62`. Thresholds
and growth rates are centralized in
`common/script_constants/019_infantry_spawn_constants.txt:534-575`.

Representative results from the live formula are:

| Eligible states | Selected states | Coverage |
| ---: | ---: | ---: |
| 1 | 1 | 100.0% |
| 5 | 5 | 100.0% |
| 6 | 5 | 83.3% |
| 15 | 12 | 80.0% |
| 16 | 12 | 75.0% |
| 35 | 21 | 60.0% |
| 36 | 21 | 58.3% |
| 70 | 31 | 44.3% |
| 71 | 31 | 43.7% |
| 100 | 38 | 38.0% |
| 200 | 63 | 31.5% |

The absolute target never drops at 5/6, 15/16, 35/36, or 70/71. The live
results remain inside the requested small/regional/medium/large/continental
coverage bands and continue to increase for large countries. Weighted state
selection removes each chosen state from the temporary pool, so duplicated
weights cannot select a state twice (`019_infantry_spawn_core_effects.txt:64-160`).

### Formation, lot, equipment, and manpower accounting

- Ordinary and registered formation materialization derives obligation rows
  from the exact manifest rather than from a flat proxy
  (`common/scripted_effects/019_infantry_spawn_generation_effects.txt:1654-1897`
  and `:2092-2320`).
- Finite prototype equipment is separately recorded before it is granted
  (`019_infantry_spawn_generation_effects.txt:1900-2089`).
- Exact settlement preflights affordability, freezes obligation UIDs, debits
  the corresponding stock/fuel/manpower profiles, and atomically changes the
  obligation, lot, and country totals
  (`common/scripted_effects/019_infantry_spawn_management_effects.txt:2458-2609`).
- Standardization uses exact paid material rows and an explicit loss fraction
  (`019_infantry_spawn_management_effects.txt:1089-1265` and `:1906-2286`).
- Supervised demobilization requires a proved exact unit/template set, deletes
  with `disband = no`, and grants the 30% salvage rate only from settled,
  unit-backed `salvageable_paid` rows
  (`019_infantry_spawn_management_effects.txt:2617-3150`).
- Prototype cannibalization applies its separate 45% return only to paid
  physical material. Unpaid obligations are forfeited without becoming
  salvage (`019_infantry_spawn_management_effects.txt:3940-4050`).

No free disband, free standardization, double-refund, or unpaid-material
salvage route was found.

### Muster Control, Army Congestion, integration, and demobilization

Muster Control and Army Congestion use centralized 0-100 scales and staged
thresholds. Audits, territorial assignment, standardization, emergency
integration, integration staff work, demobilization, and incident outcomes all
mutate those shared variables through the same management effects. Player
decisions and the AI management pulse call those effects rather than maintaining
a second AI economy. Delayed actions freeze their selected lot and revalidate
the live row before completion. Integration does not erase unsettled material
obligations; demobilization does not create salvage before exact settlement.

The reviewed values are reachable: positive control gains and congestion
relief exist for audits/standardization/demobilization; emergency integration
trades immediate absorption for a control penalty; the AI has affordable-lot
selection and pressure-sensitive alternatives instead of being trapped behind
player-only selectors.

### Four evolutions and pre-fire entry

All four evolution activation effects exist, are sequential, and have one-time
country migration passes. Countries that enter after a stage is active receive
the corresponding pre-fire setup without replaying earlier public evolution
reports. Evolution III creates its opening package unless Evolution IV entry
owns the first-family reception. Evolution IV entry uses `.105` as described
above. The active and pre-fire paths call the same subsystem initialization and
cleanup helpers.

The evolution-score thresholds and cadence are centralized and the next stage
can be reached from war, low control, severe congestion, stacked generations,
claimant history, or anomalous preservation signals. The score logic itself is
reachable. Its world-sampling implementation is the P0.

### Evolution III material quality, coherence, and safe randomness

- Material quality and structural coherence are rolled in separate functions
  and stored as independent axes
  (`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:1563-1714`).
- Combat and support cardinalities are separately rolled and clamped to the
  intended 1-25 combat battalions and 0-5 support companies
  (`:1715-1778`).
- The registry has 87 aligned component rows. Candidate construction applies
  slot type, installed technology/DLC/provider gate, material-quality bias,
  coherence bias, request bias, and row weight before selection
  (`:1780-2330`).
- Selected rows are removed from the candidate set where uniqueness is
  required. Support rows also carry same-support-type exclusion metadata, so
  mutually equivalent support families cannot bypass the no-duplicate rule.
- Materialization proceeds only when the final combat/support counts equal the
  frozen targets and every manifest row resolves. Otherwise the result is
  tagged `manifest_incomplete` and no partial unsafe template is accepted
  (`:2331-2639`).

This supports strange compositions without invalid tokens, unowned DLC rows,
duplicate supports, empty divisions, or templates above the intended 25 + 5
limit.

### Evolution IV training, spawning, containment, saturation, and reinforcement

- Provider 501 registers the base zombie family as
  `trainable_and_spawnable`; provider 502 (ghost) and provider 503 (golem)
  register as `spawn_only`
  (`019_infantry_spawn_unit_registry_effects.txt:4031-4034`, `:4211-4214`,
  and `:4382-4385`).
- The zombie training route enables recruiting only for the proved base zombie
  template. It does not unlock mutated or weaponized zombie variants
  (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5811-5880`).
- Ghost and golem templates remain locked and are produced only by registered
  spawn transactions.
- Player and AI family reinforcement use the same provider evaluation,
  snapshot, payment, spawn, proof, and rollback functions. Payment occurs
  before formation credit; a refund is allowed only after the resource and
  ledger snapshot is proved restored. Failed rollback quarantines instead of
  granting a cooldown or formation credit.
- Saturation is recomputed from exact local family divisions, active family
  rows, uncontained presence, claimant/request/evolution pressure, and current
  management relief, then clamped to the common 0-100 scale. Containment and
  sustainment decisions mutate the same family ledger the AI reads.

No free anomalous reinforcement, spawn-only training escape, provider-parent
progression leak, or duplicate reception package was found.

### Decisions, missions, focus routes, and AI parity

The direct source inventory is exact:

| Surface | Decisions | Missions |
| --- | ---: | ---: |
| Main Event 019 | 39 | 11 |
| Claimant | 6 | 0 |
| Derivative | 23 | 3 |
| **Total** | **68** | **14** |

Every actionable decision has an explicit `ai_will_do` block and a reachable,
positive centralized base. Entries with deliberately disabled decision AI are
display/open-board/select-row controls; the seven-day AI pulse chooses a live
lot or highest-pressure registered family and invokes the same settlement,
management, containment, or reinforcement effect used by the player. Missions
are started by the corresponding decisions/incidents and do not require an AI
selection weight.

`common/national_focus/019_infantry_spawn_derivative_focus.txt` contains exactly
45 unique focus nodes: 30 shared plus 5 zombie, 5 ghost, and 5 golem nodes. Each
family therefore sees 35 nodes. Every node has a completion reward and an
explicit AI weight. Family and claimant branches are gated through
`allow_branch`/`available`, while mutually exclusive political routes remain
exclusive. No player-only focus reward path or permanently zero-weight required
node was found.

### Controlled-trial exploit isolation and eleven achievements

The controlled trial package passes the requested source-level isolation audit:

- it freezes one exact Event 019 attacker by generated identity, unit UID,
  generation UID, lot UID, template UID, and monotonic trial nonce;
- it requires an adjacent state that is literally division-free and belongs to
  a peaceful, independent AI country outside Event 019 and the special scenario
  exclusions;
- it creates one locked, one-battalion defender and verifies the exact
  one-versus-one participant set before starting and before awarding;
- the border war uses `change_state_after_war = no` and a 14-day engine minimum;
- the mission times out after 45 days and a completed attempt applies a 90-day
  cooldown;
- cleanup deletes without refund, callbacks are nonce-bound and idempotent,
  and unproved cleanup enters quarantine rather than awarding or restoring
  free value.

The relevant implementation is in
`common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt:117-451`
and
`common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1190-1735`.

Exactly eleven Event 019 achievements are defined at
`common/achievements/chaos_redux_achievements.txt:3121-3233`. The four
exact-formation combat achievements use the controlled trial; the remaining
achievements read durable Event 019 state. SCN-013 tracking freezes launch type,
intensity, and starting country and rejects later intensity changes or tag
switching. No achievement route was found that can award from a fabricated
casualty ratio, state transfer, unrelated border war, duplicate callback, or
scenario-host contamination.

### Centralized tuning and recurring work

Gameplay tuning for coverage, pacing, control, congestion, AI weights,
settlement losses, salvage, provider costs, trial durations, release deferral,
and family pressure is centralized under Event 019 script constants. Remaining
numeric literals above 0/1 on the audited gameplay surface are structural
coordinates, identifiers, or engine-shape values rather than duplicated
balance thresholds.

Country-local work remains bounded by active Event 019 state. Ledger compaction
is phased, cursor-based, and capped per pulse; registry iteration is bounded by
registered providers; exact division scans occur at a transaction or proof
boundary. No independent P1/P2 performance problem was found beyond the P0
world sampler.

## Method and evidence boundaries

The audit used the complete Event 019 source specifications, the
near-completion addendum, current gameplay source, current matrices and
handoffs, the required offline Paradox wiki pages, installed HOI4 official
documentation, and vanilla precedents for decisions, missions, dynamic
countries, border wars, AI strategy, focus trees, unit creation/deletion, and
equipment stockpile effects.

Skills used:

- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`
- `hoi4-focus-trees`
- `hoi4-mtth`

The read-only HOI4 focus inspector was attempted against the Event 019 focus
file but returned `ARTIFACT_STORAGE_LIMIT`. Focus cardinality, branch gating,
AI weights, and rewards were therefore checked directly from source. This tool
capacity condition is not a gameplay finding and no fallback implementation
was made.

## Simplifications, omissions, and blockers

- No gameplay simplification or fallback was introduced; this was a read-only
  audit.
- The audit does not claim runtime facts the engine does not expose atomically.
  The owner-approved recreate/prove/delete formation-transfer limitations and
  controlled one-formation combat-trial limitations remain exactly as
  documented.
- **Blocker:** P0-019-PERF-01 must be resolved or explicitly authorized before
  the AI/balance/performance audit can close and before the workbook/catalog may
  be promoted from `In progress`.
