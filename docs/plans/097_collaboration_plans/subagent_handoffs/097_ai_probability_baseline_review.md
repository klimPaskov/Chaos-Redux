# Event 097 Collaboration: AI Probability Baseline Review

- Role: `chaosx_ai_probability_auditor`, read-only, planning-baseline mode.
- Date: 2026-10-06.
- Evidence class: design review only. No HOI4 MCP evidence exists in this report. No vanilla files or vanilla documentation were available.
- MCP blocker: the `hoi4_agent_tools` server failed to connect in this session with `ENOENT: "Executable not found in $PATH: cmd.exe"`. No `hoi4.probability_inspect`, `_evaluate`, `_sweep`, `_compare`, `_simulate`, `_sequence`, or `_render` call ran. Server version, health, live route schemas, and client task negotiation could not be checked.
- Vanilla blocker: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` does not exist in this Linux container, so no vanilla `documentation/` file, vanilla `ai_chance`, or vanilla MTTH precedent was read.
- Disposition: unresolved audit findings for parent review.

## Result classes used in this report

- design-review: a structural reading of the spec, the matrix, and repository source. It is not engine evidence.
- planning-estimate: arithmetic or a simplified model run outside the game. It is not MCP evidence and must not be presented as equivalent to it.
- unresolved: a conclusion that needs the MCP probability workflow, a missing spec input, or a parent decision before it can be accepted.

Every ordering, timing band, dominance limit, and starvation limit in the matrix remains unresolved until the MCP workflow runs on implemented source.

## Sources read

- `AGENTS.md`
- `.agents/skills/chaos-redux-mtth/SKILL.md` and the upload copy `chaos-redux-mtth.md`, which differ only in line endings and one heading capital
- `.agents/skills/chaos-redux-event-planning/SKILL.md` and its upload copy, sections 3.8, 3.8.1, and 3.11
- `.agents/skills/chaos-redux-subagents/SKILL.md` and its newer upload copy, including the MCP evidence and probability rules for this role
- the upload copy of `chaos-redux-events.md`, lines on evolution MTTH pacing and the probability workflow
- `docs/specs/097_collaboration_specs/matrices/097_collaboration_ai_probability_scenarios.md`, re-read after the parent update that removed the S1 war factor
- `docs/specs/097_collaboration_specs/specs/` parts 1, 2, 3, 4, and 6, with Part 1 and Part 6 re-read after they changed on disk, and the cluster section of Part 5
- `docs/specs/097_collaboration_specs/matrices/097_collaboration_chaos_impact_map.md`
- `docs/plans/097_collaboration_plans/subagent_handoffs/097_repo_explorer_handoff.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` (`ai_chance`, `mean_time_to_happen`) and `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` (`ai_will_do`)
- Repository source listed in the next section

## Repository facts that the review relies on

These were read directly from source and are design-review facts, not engine evidence.

1. Shared defaults in `common/script_constants/event_system_constants.txt` (`event_system_defaults`): `event_weight = 1000`, `reduce_cap_factor = 0.5`, `recovery_rate = 20`, `major_event_weight_per_minor = 150`. Timer defaults in `event_system_timer_defaults`: 45 to 60 days, a day decrement that grows by 1 per minor firing up to 15, a maximum-range compression that grows by 1 every third minor firing up to 5, and a 2-day floor. Tier multipliers in `event_system_timer_modifier_default`: 1.0, 0.8, 0.7, 0.6, 0.5, 0.5.
2. `on_repeatable_event_fired` in `common/scripted_effects/chaosx_logic_effects.txt` halves the event's cap with `round_temp_variable`, sets the weight to 0, and then runs the minor pacing update, which immediately raises it to 1. Later pacing updates raise 1 to 20 and then add 20 per update up to the cap.
3. `update_repeatable_event_weights` runs from both `on_minor_event_global_pacing_update` and `on_major_event_global_pacing_update`, so recovery happens after every pacing event, major included. It only recovers while the event's Chaos level is met. It does not check the N/A unavailability chain, so the weight keeps recovering while the event shows N/A.
4. `select_weighted_random_event_id` in `common/scripted_effects/chaosx_settings_effects.txt` draws once from one pool of every valid event (major, repeatable, and fire-once) using current weights times 100, and drops any candidate whose scaled weight rounds below 1. The natural path in `common/on_actions/chaosx_on_actions_system.txt` calls it when the timer reaches 0.
5. Major events start at weight 0 and gain a dynamic amount after each minor firing (`calculate_dynamic_major_weight_gain`). Fire-once events leave the pool after firing.
6. Settings let the player change the default event weight (100 to 5000), the recovery rate (0 to 10000), the cap reduction (0 to 1), the major gain, and the timer modifiers (`settings_advanced_bounds` in `common/script_constants/settings_constants.txt`). These are declared inputs for any S1 analysis.
7. `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt` enables 27 events by default today: ids 1 to 21, 23 to 25, 27, 29, and 32. By category that is 2 major, 12 fire-once, and 13 repeatable. Event 097 is registered as repeatable but is not default-enabled yet.
8. MTTH precedents use two consumer patterns. Events 035, 018, 006, and 014 compute `mtth:` once into a deterministic due date or mission timer. Events 006 and 014 clamp the result with `minimum_days` and `maximum_days` constants (Event 014 uses 21 and 240). Event 005 uses an MTTH-computed weight inside a `random_list` against a miss weight, which is a stochastic roll per check. Event 016 uses `ai_will_do = { base = mtth:... }` for MTTH-backed decision weights.
9. The wiki states that `ai_chance` is proportional, that all-zero weights pick the first option, and that the choice uses a d100 roll so any option below 1 percent is effectively never chosen. It states that native `mean_time_to_happen` is a median polled daily after a 20-day trigger check, and that decisions are never chosen by AI without `ai_will_do`.
10. The only existing Event 097 source is the stub `events/097_collaboration.txt`, SHA-256 `9939cbcb4eab03343a7eedec54a95cb517a6d406b1c153fc481ebf875288f4bd`. Its single option has `ai_chance = { base = 100 }`. It is the only pre-edit source any compare could use today.

## Q1. Are all weighted surfaces named, with complete candidate pools?

### Coverage of the listed surfaces (design-review)

| Surface | Named | Candidate pool complete for its purpose | Gap |
| --- | --- | --- | --- |
| S1 selection weight | Yes | No | The pool composition at release, the Chaos path, and the player settings are not declared. A sequence analysis needs all three. |
| S2 stance | Yes | Partly | Three options are listed. The Screen block threshold is not numeric ("a minimum that the vetting campaign could not push below zero"), so the pool size in low-stability scenarios is unknown. Actor-group precedence is undefined (see Q2). |
| S3 offer | Yes | Partly | Two options are listed. "Plans to annex through a peace conference it expects to win soon" (Part 6) has no measurable input. |
| S4 Unmasked | Yes | Yes | Two options. Only the network band input is missing from P14 and P15. |
| S5 Divided Loyalties | Yes | No | Part 4 caps the category at four visible actions, but A1 to A5 can all be visible at once (P8 with Evolutions II, III, and IV active). Which action is hidden is not specified, so the scored set is ambiguous. A2 is per enemy and its target set is not listed. |
| S6 Prepared Governments | Yes | Partly | B1 and B2 are per target. No scenario lists several targets at once. |
| S7 evolution MTTH | Yes | No | Anchors and factor directions exist. Factor magnitudes, bounds, the consumer pattern, and separate pre-fire and active entries do not. |
| S8 Open Gates | Yes | Partly | The 90-day cooldown, the cap of three, A1 doubling, and the A3 and A4 suspensions are stated. The timer restart rule and the recompute rule on band change are not. |
| S9 Turned Regime | Yes | No | The rival selector is missing (see M3). No factors are declared. |
| S10 installer | Yes | Partly | The final tie-break fails when two qualifiers tie on band and core count and neither received the capitulation. |

### Missing surfaces (design-review)

- M1. Intelligence cluster live trigger roll. `event_cluster_get_live_trigger_weighted_roll` in `common/scripted_effects/chaosx_event_cluster_effects.txt` multiplies each member's current selection weight by an activation chance. Part 5 makes Event 097 a Medium member from 200 Chaos beside 039 and 052. This is a weighted surface that reuses the S1 weight and is not in the matrix. Because the cluster is Fire-Once, it adds at most one firing per campaign, but it also halves 097's cap when it fires.
- M2. Open Gates state selector. Part 3 prefers the lowest victory-point state but gives no tie-break for equal values. It is deterministic and belongs beside S10.
- M3. Turned Regime rival selector. Part 3 does not say which rival receives the government when two rivals qualify. This is a selection surface with no rule.
- M4. A2 target choice among several seating enemies, and B1 target choice among several targets. Part 4 and Part 6 imply an ordering (Strong or Total networks first, own continent first) that no scenario tests.
- M5. World stance distribution. Part 6 and balance item 7 forbid polarization across the world. That is an aggregate over actor groups, not a single-country option share, and needs a declared world population fixture.
- M6. Installation rate per year. Part 6 balance item 5 asks how many governments are installed per year in a world war. S3 and B1 together produce this rate, and the matrix gives no target band. The competing-orders milestone timing follows from it.
- M7. Stance memory. Part 1 says stances are "kept for achievements and AI memory", but no AI memory factor appears in Part 6 or the matrix. Either it is a weighted input that needs a scenario or the phrase should not imply one.
- M8. Long-campaign Chaos sum. The impact map says the probability audit should include a long-campaign scenario that sums expected Event 097 Chaos. The matrix has no such scenario. It depends on S1, S8, S9, M6, and the Collapsing rate.
- M9. Gate scenarios. No scenario covers the Fallout gate, the event disabled in settings, or a single evolution disabled. Each weighted surface should return zero or stop in those states.

## Q2. Are the scenarios sufficient?

All points in this section are design-review. The behavior itself is unresolved.

### Starvation

- The Accept floor appears only in P2 and as a general Part 6 rule. P3, P4, P6, P13, and the new scenarios below need an explicit Accept floor. Because `ai_chance` uses a d100 roll, a declared floor below 1 percent is the same as zero. The parent should choose a numeric floor.
- Cultivate and Screen floors in P1 are written as "clearly above zero" with no number.
- A5 has no scenario in which it is visible. It needs Collaboration Governments active and either 40 percent surrender progress or an occupying Strong network. P8 does not declare evolution states.
- B2 has no scenario for an Imposed or Entrenched government at peace, so the matrix cannot detect B2 being used as a staging shortcut to Entrenched.

### Dominance

- S2 has a two-thirds limit only for P13. The spec forbids polarization into cultivators and screeners, not dominance by Accept, so the limit should be stated per stance and per world fixture. One workable form is a ceiling on the combined Cultivate plus Screen share in war worlds and a floor on Accept in every actor group. The parent chooses the numbers.
- S1 dominance is possible in a small pool because Event 097 is almost always available while other events go N/A. See Q5.

### Polarization

- Actor-group precedence is undefined. A losing expanding power also matches "already losing a war" for the threatened neighbor group. A democracy that borders an expanding power with a claim on it matches both Democracy at peace and Threatened neighbor. An installed government that is losing matches both Installed government and Threatened neighbor. A country in civil war can also match any other group. Without a precedence order the stance outcome for these countries is not defined, and a world simulation cannot be declared.
- "War-preparation focus" in the Expanding power definition has no list of focuses or flags, so it is an undeclared input.
- A cross-firing feedback loop exists. Cultivate raises the cultivator's incoming layer, which makes it more likely to face a Fifth Column, which pushes it toward Screen in the next firing. Testing this needs `hoi4.probability_sequence` across firings with the stance memory rule from M7.
- No world population fixture exists for 1936, 1939, or P13.

### Rank reversal thresholds that need sweeps

| Threshold | Source | In matrix |
| --- | --- | --- |
| Expanding power Cultivate weight falls past 20 percent own surrender progress | Part 6 | No |
| Screen stability minimum and the "near the minimum" decline | Part 1, Part 6 | Only two points, P3 at 55 and P4 at 25 |
| Installer 40 percent surrender progress for the offer and B1 | Part 4, Part 6 | Only two points, P9 at 10 and P10 at 45 |
| Fifth Column band floors 20, 40, 60 with 5-point hysteresis on the way down | Part 3 | No, and the hysteresis direction needs a scheduled path |
| A4 command power cost (25 minor, 40 major, cap 60) | Part 4 | P8 sits exactly on the major cost at 40 |
| A2 manpower cost and "short on manpower" | Part 4 | "manpower short" has no number |
| Purge stability penalty | Part 4 | Only P14 at 50 and P15 at 20 |
| Network band edges 15, 40, 70 | Part 3 | No |
| Installation threshold with its modifiers and clamp from 25 to 60 | Part 3 | No |
| Governments held, two to three, for the continent rule | Part 4, Part 6 | Only P12 at three |

### Timing drift

- S7 needs scheduled state changes after eligibility: a war that starts or ends during the countdown, an earlier evolution that activates during a later evolution's countdown, Chaos falling below the requirement during a countdown, and the evolution being disabled during a countdown. The 035 precedent freezes the due date when it is first computed, so these changes would not move it. The spec does not say whether 097 freezes or recomputes.
- S7 has no pre-fire versus active split, although Part 2 defines both entry paths and the 018 precedent keeps separate intervals.
- S8 needs a rule for a band change during a running timer (Defecting to Collapsing) and for A1 starting or ending during a running timer.
- S9 needs a declared distribution of how many governments are Contested at once in P13.

### Scenarios to add (design-review proposals, the parent decides)

| Id | Scenario | Purpose |
| --- | --- | --- |
| P16 | Expanding power at war at 25 percent own surrender progress | Cultivate reversal past 20 percent |
| P17 | Country in civil war | Screen blocked, Accept largest, valid option remains |
| P18 | Installed government in Imposed and in Entrenched at peace | Baseline for P6 and for B2 starvation |
| P19 | Democracy at peace bordering an expanding power with a claim on it | Actor-group precedence |
| P20 | Installer holding three governments, target on its own continent | Positive counterpart of P12 |
| P21 | Installer at 15 percent surrender progress with a peace conference near | Keep direct occupation case from Part 6 |
| P22 | Host at war at 10 percent surrender progress with Deep or Pervasive incoming networks | A1 taken early before the Fifth Column |
| P23 | Host at Collapsing with Evolutions II, III, and IV active, allies at war, ideology different from the likely installer | A5 visibility, the four-action cap, and the A5 rule |
| P24 | Two enemies hold seated states, one Ordinary and one Strong | A2 target ordering |
| P25 | Expanding power with its own Fifth Column at Wavering | "Rarely takes A1 unless its own Fifth Column appears" |
| P26 | Fallout transition begun, event disabled, and one evolution disabled | Gate behavior on every surface |
| P27 | Long campaign from 1936 to 1946 under three declared Chaos paths and two pool configurations | S1 firing count, M6 installation rate, and M8 Chaos sum |

## Q3. Contradictions between Part 4, Part 6, and the matrix

All items are design-review findings for the parent to settle.

- C1. A3 visibility at Wavering. Part 4 makes A3 visible whenever the Fifth Column spirit is active, which includes Wavering. Matrix S5 P7 says A3 and A4 are not visible at Wavering. The A4 half is consistent. The A3 half contradicts Part 4.
- C2. A5 condition. Part 4 uses "allies still at war, or an ideology different from the likely installer". The matrix uses "allies still at war and a different ideology". Part 6 says a threatened neighbor takes A5 "when it has allies who will fight on" and a democracy at peace "uses A5 readily". Three statements give three different rules.
- C3. Offer outside the home continent. Part 6 says an installer that holds three governments "installs only on its own continent", which implies an Install weight of zero for P12. Matrix S3 P12 only asks that Keep be the largest share. Matrix S6 uses "zero" for the same rule on B1.
- C4. Screen at 25 percent stability. Matrix P4 expects Screen to be blocked or near zero. Part 1 blocks Screen only below a minimum tied to a vetting cost of about 10 percent, which places the block well under 25 percent. Part 6 only says the weight falls near the minimum. The matrix expectation is stronger than either spec part.
- C5. Installed government stance. Part 6 makes Screen the preference when Contested. Matrix P6 only asks that Screen rise above its P1 share, which is a weaker test than the spec.
- C6. S1 wording. Matrix S1 says the event "shows zero weight with a reason". Part 1 says it shows N/A with a reason instead of a silent zero weight. Source writes weight `-1` for N/A in the events tab. The matrix wording should follow Part 1.
- C7. Recovery wording. Part 1 says weight recovers "after each minor firing of any event". Source also recovers after major pacing updates. The difference is small but it belongs in the S1 manifest.
- C8. Evolution II fast factor. Part 2 says faster when a participant has capitulated since Event 097 first fired. Matrix S7 calls it "recent capitulation". The two inputs differ.
- C9. B1 example. Part 4 says "An Ordinary network of 20 points needs 70" compliance, but B1 also requires the network to meet the installation threshold, which never falls below 25. A 20-point network can never use B1. The example sets up an impossible scenario.

## Q4. MTTH structure

### Fit with the MTTH skill and repository precedents (design-review)

The skill structure is a `common/mtth/*.txt` entry with `base`, `modifier` blocks using `factor` or `add`, and consumption through `mtth:` into `set_variable` or `set_temp_variable`. Repository precedents add a constant group for the base and every factor, explicit `minimum_days` and `maximum_days` clamps, and a named consumer pattern.

| Surface | Base | Factors | Bounds | Consumer pattern | Scenario declarations |
| --- | --- | --- | --- | --- | --- |
| S7 Evolution I | 90 days | Directions only | None | Not stated | Fast and slow cases only |
| S7 Evolution II | 90 days | Directions only | None | Not stated | Fast and slow cases only |
| S7 Evolution III | 90 days | Directions only | None | Not stated | Fast and slow cases only |
| S7 Evolution IV | 120 days | Directions only | None | Not stated | Fast and slow cases only |
| S8 Open Gates | 60 Defecting, 30 Collapsing | A1 doubles | Cooldown 90, cap 3 per war | Not stated | Partial |
| S9 Turned Regime | 120 days | None | Once per government per war | Not stated | World band only |

Findings:

- No surface states its consumer pattern. A deterministic due date (035, 018, 006, 014) gives one exact value per scenario, so the matrix request for survival curves would show a step. A stochastic roll (005) gives a real distribution. The words "expected time" in S8 and S9 imply a mean, while native `mean_time_to_happen` is a median. The spec must say which pattern each surface uses before the audit can choose between exact and sampled results.
- No surface declares bounds. The matrix requires that no evolution activates in under 30 days. Planning-estimate: using the 035 factor range of 0.65 to 0.80 as an illustration, three stacked fast factors on a 90-day base give about 25 days at 0.65 each and about 46 days at 0.80 each. Only a declared minimum clamp guarantees the 30-day floor.
- No surface has separate pre-fire and active entries, although Part 2 defines both paths and the 018 precedent splits them.
- S8 pacing is owned by the cooldown, not the MTTH. Planning-estimate: with a deterministic 30-day timer at Collapsing and a 90-day cooldown, incidents land near days 30, 120 to 150, and 210 to 270, so the cap of three binds inside a 365-day war, which matches the matrix. At Defecting with a 60-day timer, they land near days 60, 150 to 210, and 240 to 360, so the cap may not bind within a year. After the first incident the band difference mostly disappears, and A1 doubling only stretches the timer portion. The parent decides whether this is the intended pacing.
- S9 world rate. Planning-estimate: if a government's conditions hold for T days under a stochastic hazard with a 120-day mean, the chance it turns is about 1 minus e to the power of minus T over 120, which is about 0.53 at 90 days, 0.78 at 180 days, and 0.95 at 365 days. Three governments Contested for six months each would give about 2.3 turns in a year, which is above the matrix failure line of two. The spec has no world-level cap or cooldown on this variant, and the Chaos impact map caps only its Chaos at two per campaign. The rate therefore depends entirely on how often eligibility occurs.

### Surfaces that should use MTTH but do not (design-review)

- S2 stance `ai_chance`. Seven actor groups with surrender, stability, ideology, war, and neighbor inputs would produce large conditional blocks across three options. MTTH-backed weights, one entry per option in the style of `ai_will_do = { base = mtth:... }` from Event 016, would keep the tuning in one constant group.
- S5 and S6 decision `ai_will_do`. Part 4 orderings depend on band, command power, manpower, allies, ideology, continent, and government count. Event 016 is the repository precedent for MTTH-backed decision weights.
- S3 and S4 are smaller but share inputs with S5 and S6, so they would benefit from the same entries.

### Surfaces that should not use MTTH (design-review)

- S1, because it belongs to the shared system and has no event-owned factor.
- S10, the Open Gates selector, and the Turned Regime rival selector, because they are deterministic orderings.
- Fifth Column bands, because they are thresholds with hysteresis.
- Native event `mean_time_to_happen` should not drive S8 or S9, because it polls every country and would act as a periodic world scan. Part 3 already plans per-host and per-government scheduling, which fits a due-date or scheduled-event consumer.

## Q5. Expected number of natural firings

### Planning-estimate, unresolved pending MCP

Classification: planning-estimate. This is a simplified Monte Carlo model of the source rules listed above. It is not MCP evidence. It stays unresolved until `hoi4.probability_sequence` runs on a declared manifest.

Mechanism (design-review): the cap halving in Part 1 is shared by every repeatable event, so it does not limit Event 097 on its own. An event that has fired k times has a cap of 1000 divided by 2 to the power k, so events with fewer firings dominate the next draws and the pool equalizes firing counts. Over a long campaign each always-available repeatable fires about once per as many draws as there are active repeatables. Event 097's count is therefore close to the number of repeatable draws divided by the number of active repeatables. The cap sequence of 1000, 500, 250, 125, and 63 in Part 1 is correct for source but says little about the count.

Model assumptions:

- Rules from repository facts 1 to 6 above, with default settings.
- Two pool configurations. The default-enabled pool is today's 27 events plus Event 097, which gives 2 major, 12 fire-once, and 14 repeatable events. The all-enabled pool is every registered event, which gives 9 major, 36 fire-once, and 51 repeatable events.
- Three Chaos paths for the timer multiplier. Calm stays at tier 0. Ordinary rises one tier every two years. Fast rises one tier every year.
- Event 097 is available from day one, because the catalog lists Chaos level 1 and the registry default is tier 0. It is always available apart from its own pass, which the model ignores.
- No cluster draws, no Tensions Rising timer pressure, and one event timer.
- A sensitivity variant makes each other event unavailable on 30 percent of draws and removes 25 percent of fire-once events permanently.
- 1000 seeds per row.

Approximate draws in ten years: about 100 on the calm path, 150 on the ordinary path, and 175 on the fast path.

| Pool | Chaos path | 5 years, median (p10 to p90) | 10 years, median (p10 to p90) | Share of 10-year runs with 2 to 5 firings |
| --- | --- | --- | --- | --- |
| Default plus 097 | Calm | 2 (1 to 3) | 6 (5 to 7) | 0.41 |
| Default plus 097 | Ordinary | 3 (2 to 4) | 9 (8 to 10) | 0.00 |
| Default plus 097 | Fast | 4 (3 to 5) | 11 (10 to 13) | 0.00 |
| All enabled | Calm | 0 (0 to 1) | 1 (0 to 2) | 0.15 |
| All enabled | Ordinary | 0 (0 to 1) | 1 (1 to 2) | 0.48 |
| All enabled | Fast | 1 (0 to 1) | 2 (1 to 3) | 0.72 |

With the unavailability variant, the default ordinary row rises to a ten-year median of 10 (9 to 11), and the all-enabled fast row rises to 3 (2 to 4). Other events going N/A raises Event 097's share because Event 097 is almost always available.

Other outputs from the same model:

- The first natural firing has a median near day 475 to 673 in the default pool, which is mid-1937 to late 1937, and near day 740 to 1870 in the all-enabled pool.
- In the default pool, every ten-year run reached a fourth firing, with a median in year 4.9 on the fast path, year 5.8 on the ordinary path, and year 7.1 on the calm path. In the all-enabled pool, 3 percent of runs or fewer reached a fourth firing.
- The median gap between Event 097 firings was about 230 to 460 days in the default pool and about 900 to 1340 days in the all-enabled pool.

Verdict (planning-estimate, unresolved):

- The Part 1 assumption of two to five natural firings holds in this model only for a pool of moderate size or for roughly the first five years of a campaign.
- If the default-enabled pool stays near today's size at release, a ten-year campaign likely sees about six to eleven natural firings. That also weakens the Part 1 claim that the 80 percent collaboration-government threshold is rare without Evolution IV, because four firings arrive around years five to seven.
- If every event is enabled, a campaign likely sees one to three natural firings. Part 6 balance item 1 ("one firing in 1937") is then unlikely.
- The pool composition at release, the Chaos path, and the player settings are the inputs that decide the answer. The cap halving does not.
- The Intelligence cluster can add at most one more firing.

## Q6. MCP checklist for the implementation agent

Run this only after the `hoi4_agent_tools` connection works. Do not invent adapter ids, fixture keys, or schema fields. Use the adapter id and fields that each live route schema reports, and record them.

### Preconditions

1. Record the connected server's configuration identity, version, health, live schema for every `hoi4.probability_*` route, and client task negotiation.
2. Before any weight edit, preserve immutable copies at real filesystem paths with SHA-256 hashes of the copied bytes for: `events/097_collaboration.txt` (current hash `9939cbcb4eab03343a7eedec54a95cb517a6d406b1c153fc481ebf875288f4bd`), `common/scripted_effects/chaosx_logic_effects.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, `common/script_constants/event_system_constants.txt`, and `common/scripted_triggers/chaosx_settings_triggers.txt`.
3. New Event 097 surfaces have no pre-edit source. The first valid `hoi4.probability_compare` is between an immutable snapshot of the first implemented version and the tuned version. Never compare a file to itself. If no exact before source exists, keep before and after inspect evidence and report the numeric delta as unresolved.
4. Save one scenario fixture for P1 to P27 with its SHA-256 hash, and reuse the identical `scenarioSet` for baseline and compare.
5. Settle the Q3 contradictions and the missing inputs in the open questions below before the baseline run, because otherwise the scenarios have no single expected result.

### Source paths

Use mod-relative source objects in the form `source: { path: "..." }`. The paths below follow repository conventions and are proposals until the implementation creates them: `events/097_collaboration.txt` for S2, S3, and S4, `common/decisions/097_collaboration_decisions.txt` for S5 and S6, `common/mtth/097_collaboration_mtth.txt` for S7, S8, S9, and any MTTH-backed weights, `common/script_constants/097_collaboration_constants.txt` for anchors and bounds, and the Event 097 scripted effects files for S10, the Open Gates selector, and the rival selector.

### Calls per surface

- [ ] S1. `hoi4.probability_inspect` on `common/scripted_effects/chaosx_logic_effects.txt` and `common/scripted_effects/chaosx_settings_effects.txt` to confirm cap reduction, recovery, pool validity, and the draw.
- [ ] S1. `hoi4.probability_sequence` with a complete declared custom-pool manifest (`id`, `selection`, `candidates`, `transitions`) covering every event in the configured pool with initial weights and caps, cap halving with rounding, the 0 then 1 then 20 recovery steps on every pacing update while the Chaos level is met, fire-once removal, dynamic major gain and reset, timer cadence with compression and tier multipliers, and the horizon. Run P27 for the default-enabled and all-enabled pools on the calm, ordinary, and fast Chaos paths for 5 and 10 years, and run settings variants for recovery and cap reduction. Report the firing-count distribution, the first-firing day, and the fourth-firing day.
- [ ] S1. `hoi4.probability_simulate` only for the declared unavailability uncertainty of other events.
- [ ] S1. `hoi4.probability_render` for the sequence and firing-count views.
- [ ] M1. `hoi4.probability_inspect` and `hoi4.probability_evaluate` on `event_cluster_get_live_trigger_weighted_roll` with the 039, 052, and 097 member weights at 200 Chaos and above.
- [ ] S2. `hoi4.probability_inspect` on the opening report options, then `hoi4.probability_evaluate` for P1 to P6, P13, P16, P17, P18, and P19. Check the Accept floor in every scenario and remember that the d100 roll treats any share below 1 percent as zero.
- [ ] S2. `hoi4.probability_sweep` over own surrender progress from 0 to 60 in steps of 5 for P2 and P16, and over stability from 0 to 60 in steps of 5 for P3 and P4, to locate the Cultivate and Screen reversals and the Screen block.
- [ ] S2. `hoi4.probability_simulate` across a declared world population of actor groups for 1936, 1939, and P13 to test the polarization limits, and `hoi4.probability_sequence` across successive firings if stance memory exists.
- [ ] S2. `hoi4.probability_render` as a ranking matrix by scenario and actor group.
- [ ] S3. `hoi4.probability_evaluate` for P9, P10, P11, P12, P20, and P21, then `hoi4.probability_sweep` over installer surrender progress from 30 to 50 and governments held from 0 to 4.
- [ ] S4. `hoi4.probability_evaluate` for P14 and P15, then `hoi4.probability_sweep` over stability from 10 to 60 and over the enemy network band.
- [ ] S5. `hoi4.probability_inspect` on the Divided Loyalties decisions, then `hoi4.probability_evaluate` for P7, P8, P22, P23, P24, and P25. Report score-only results and never present them as click probabilities.
- [ ] S5. `hoi4.probability_sweep` over command power from 20 to 60, over the manpower shortfall, and over surrender progress from 15 to 70 upward and back downward to cover the 5-point hysteresis.
- [ ] S6. `hoi4.probability_evaluate` for B1 with P9 to P12 and P20 analogues and a democratic installer, and for B2 with Imposed, Entrenched, Contested, and enemy-occupied governments. `hoi4.probability_sweep` over installer surrender progress from 30 to 50, network from 20 to 80, and governments held from 2 to 4.
- [ ] S7. `hoi4.probability_inspect` on each evolution MTTH entry, then `hoi4.probability_evaluate` for the ordinary, fast, and slow cases on both the pre-fire and active paths, using the verified game-version MTTH adapter only.
- [ ] S7. `hoi4.probability_sweep` across factor combinations to confirm the minimum clamp and the 30-day floor, with scheduled state changes for a war starting mid-countdown, an earlier evolution activating mid-countdown, Chaos falling below the requirement, and the evolution being disabled.
- [ ] S7. `hoi4.probability_simulate` only if the consumer pattern is stochastic. Otherwise report exact due-day values. Then `hoi4.probability_render` as timing-survival or exact timing views.
- [ ] S8. `hoi4.probability_evaluate` for Defecting, Collapsing, Collapsing with A1, and Collapsing with A3 or A4, then a scheduled 365-day war at each band with the cooldown, the cap of three, and the no-qualifying-state restart. `hoi4.probability_render` for the incident-count and survival views.
- [ ] S9. `hoi4.probability_evaluate` for one eligible government, then `hoi4.probability_simulate` with a declared distribution of zero to five Contested governments in P13 to test the world band of fewer than one per year and the failure line of two. `hoi4.probability_render` for the rate view.
- [ ] S10, M2, and M3. Inspect the deterministic selectors. If the live route accepts a declared custom pool with deterministic selection, evaluate ties, a no-score-above-sentinel case, and the case where the capitulation recipient does not qualify. If not, record the missing route and use `hoi4.event_inspect` evidence.
- [ ] M6 and M8. `hoi4.probability_sequence` or `hoi4.probability_simulate` for P27 to estimate installations per year, the competing-orders milestone date, and the summed Event 097 Chaos against the 30 to 45 point lifetime band in the impact map.
- [ ] P26. Evaluate every surface under the Fallout gate, the disabled event, and a disabled evolution, and confirm zero weight or a stopped timer.
- [ ] After the owner's patch, run `hoi4.probability_compare` with real `before.path` and `after.path` values and the identical saved `scenarioSet` for every surface that changed. Do not add `sourceRevision` or `sourceHash` inside the source objects. Keep hashes and revisions in the handoff.

Classify every result as exact, bounded, sampled, score-only, or unresolved, state whether the candidate pool and external factors were complete, and keep artifact URIs and validation errors in the handoff.

## Open questions for the parent

These need a decision or a missing input. The auditor does not choose balance targets.

1. Should the S1 firing assumption be restated against a declared pool size at release, or should the depth table in Part 1 be checked against six to eleven firings for the default pool?
2. Which consumer pattern does each MTTH surface use, deterministic due date or stochastic roll, and does a running timer recompute when conditions change?
3. What are the minimum and maximum clamps for S7, S8, and S9?
4. What is the actor-group precedence order for S2?
5. What are the numeric floors for Accept, Cultivate, and Screen, and the polarization ceiling?
6. What is the numeric Screen stability minimum?
7. Which rule is correct for A3 at Wavering (C1) and for A5 (C2)?
8. Is the P12 Install weight zero or only lower (C3)?
9. Which action hides when five Divided Loyalties actions qualify at once?
10. Which rival receives a Turned Regime government when several qualify, and should the variant have a world-level cap?
11. What is the final tie-break for S10 and for the Open Gates selector?
12. Does stance memory affect AI weights?
13. What target band applies to installations per year?

## Changed files

- `docs/plans/097_collaboration_plans/subagent_handoffs/097_ai_probability_baseline_review.md`, this report and the only file written to the repository.

The planning-estimate model lives outside the repository at `/tmp/claude-0/-home-user-Chaos-Redux/7c09f8f3-d9fd-5e1e-9f73-3c6bc52512ec/scratchpad/sim_097_firings.py` and `sim_097_extra.py`. It is scratch evidence only and is not a substitute for `hoi4.probability_sequence`.
