# Event 032 native evolution clock architecture review

Reviewed 2026-10-08 after interruption, retaining the requested filename.
Disposition: `unresolved` for parent review of implementation constraints, with no new accepted design asserted.
The replacement `AGENTS.md` and the events, subagents, and MTTH skills were read.
Only this handoff was written, and its path was absent immediately before creation.
No gameplay, localisation, asset, Git, game, or log changes and no subagents were used.

Pulse-observed pressure is compatible with the finite observation model in spec part 4:29-62.
Those lines explicitly place a bounded pulse before MTTH and permit firing transactions, tier changes, finite delayed jobs, and exact prerequisite mutations.
Part 8:627-642 forbids recurring global country scans.
The spec does not establish continuous observation of every native change or a maximum detection delay.
Consequently, a complete snapshot at authorized pulses, updated by available exact mutation hooks, plus live validation at attempted unlock is a defensible implementation of that model.
This conclusion does not establish continuously current pressure or continuous eligibility throughout the waiting interval.

There is a genuine observation gap.
An unarmed track can become eligible through native stability drift, equipment production, nuclear production, or research and remain undiscovered until the next permitted pulse.
An armed track can retain an outdated pressure factor, and an eligibility lapse followed by recovery between observations is not observable.
Precommit validation prevents an invalid unlock at that instant, but cannot recover missed eligible time, correct the preceding timing distribution, or discover an unarmed track.
Describe these as pulse observation semantics, not exact mutation coverage.
If continuous freshness or bounded discovery latency is required, the present allowed routes do not prove it.
Do not resolve that gap with a self-rescheduling registry scan or a rolling country watcher.

The installed `common/on_actions/_documentation.md:1-111` contains no generic stability-change, production-completion, or research-completion callback.
Its `on_mio_tech_reseach_completed` entry is MIO-specific and does not establish universal research coverage.
The absence is a documented-route gap, not proof that every undocumented engine facility is impossible.
An arbitrary finite chain of observation jobs also provides no unlimited future coverage after its last job.

| Required boundary | Existing owner location and constraint |
| --- | --- |
| Global firing and initialization | `common/scripted_effects/032_missiles_effects.txt:224-274`, `missiles_global_firing_transaction`, already evaluates after recipient receivers. Publish after all mutations settle. Initialization/normalization owners are `missiles_initialize_or_advance_program:320` and `missiles_normalize_technology_stage:395`. |
| Chaos eligibility changes | `common/scripted_effects/chaos_meter_effects.txt:4436-4467` applies the value and calls `update_chaos_meter_tier:4495`. Cover upward and downward threshold crossings, including 900 inside the 800-1000 tier. A tier-change-only hook misses that crossing. Coalesce to one owner evaluation. |
| Program and site mutations | Core effects own `missiles_add_reserve:497`, `missiles_remove_reserve:519`, `missiles_register_site:733`, and `missiles_recalculate_network:833`. Operations effects own readiness `:1393`, guidance `:1429`, launch-code security `:1438`, hardening `:1502`, completed repair `:1577`, recovery `:1724`, damage `:4683`, disaster damage `:4802`, and operation commit/launch count `:6133-6168`. Refresh affected contributions at the completed transaction, including losses and refunds. |
| World and ownership changes | `common/on_actions/032_missiles_on_actions.txt` supplies war relation `:10`, capitulation `:131`, peace conference `:140`, peace `:149`, state control `:168`, release `:186/:192`, and annexation `:198`. Wire settled participants/sites and changed relationships. Operations effects own control change `:6478`, receiver refresh `:6814`, civil-war child/parent finalization `:6884/:6991`, and removal cleanup `:7057`. Verify exact native callback scope and peace-relation coverage before implementation. |
| Shared payload and control changes | Hook completed shared payload grant, debit, release, transfer, and research/project output transactions where their owners expose them. No generic native-production hook is established. `032_missiles_triggers.txt:373-397` reads a chemical candidate token, biological equipment, and nuclear stock. A cached chemical token alone does not prove current physical stock. Toggle owners are `chaosx_events_log_effects.txt:3066/:4671`, with no GUI redesign required. Disable clears pending state, re-enable permits fresh evaluation, and world end blocks commits and clears clock work. |

Preserve the existing method boundaries in `common/scripted_effects/032_missiles_operations_effects.txt`:

- `missiles_measure_evolution_pressure:543-594` owns measurement. Publish durable global values for later native event checks, with observation date/generation for evidence. Temporary outputs need caller-owned storage if consumed after return.
- `missiles_evaluate_evolution_unlocks:816-978` owns all five complete eligibility checks at allowed boundaries. Ordinary arming reads complete observations and does not commit because an old due date elapsed.
- `missiles_select_evolution_host:744-764` owns the living registered country pointer, `global.missiles_evolution_host`. Removal `:7057-7080` must subtract its contributions, reselect once, and preserve outstanding finite deadlines. Zero surviving programs leaves no host until a later exact initialization.
- `missiles_commit_evolution_track:717-730`, `missiles_record_evolution_unlock:412-479`, and `missiles_set_evolution_log_context:486-511` retain live prerequisite validation, enabled/world-end/already-recorded guards, actorless once-only logging, and country adoption receiver `.8`.
- `missiles_arm_evolution_track:655-712`, queue/requeue `:767-813`, and `missiles_run_evolution_job:1020-1123` retain only the finite first-high-chaos exception. Remove the ordinary watch owners `:983/:991` and event `.191`, including their removal-recovery enqueue path.

Native triggers and MTTH modifiers must read only host identity, pending/mode, enabled, world-end, recorded, and cached eligibility/pressure fields.
The offline event reference describes trigger checks every 20 days, followed by daily checks with chance `1 - 2^(-1/M)` while eligible, and variable-supported modifiers.
Therefore the native timer itself adds an activation-check delay and cannot repair an unobserved prerequisite.
Keep the five tracks independent and distinguish native-pending state from legacy-job-pending state so `.190` and native events never race as two delivery paths for one track.
On failed live validation, disarm that track and await an authorized observation boundary instead of repeatedly firing an invalid cached gate.

Do not blindly copy Iceland's `fire_only_once = yes` onto a native attempt whose immediate block can reject.
The documented once-only state is consumed by event firing, which could permanently lose a track after rejection.
Successful global unlock/log state must provide the once-only commit guarantee, while rejected attempts remain eligible for later rearming.
The existing commit helper's commit counter also increments after its recorder call without testing whether that invocation recorded anything, so a fresh-success result must distinguish duplicate/no-op calls.

Per-country contribution deltas can avoid a registry recount on every small action.
Replace each country's previous contribution with its freshly measured contribution once at settlement, remove it exactly once on cleanup, and recompute ratios from aggregate numerators and denominators.
This is exact only for inputs whose mutation paths are covered.
At a full authorized observation or final live prerequisite check, do not simply sum stale country caches and call that live validation.
Pair updates need endpoint and relationship invalidation rather than a scalar country delta.

`missiles_measure_evolution_pressure:574-583` currently counts response-capable countries having any operational war opponent.
Two responders facing only each other produce count 2 for one distinct pair, while one responder facing two opponents produces count 1 for two pairs.
Define and deduplicate actual unordered qualifying country pairs, maintaining response capability separately or explicitly in the pair predicate.
The current predicate proves war relations only, not every hostile or severe-tension condition mentioned in part 4:837.
The intended non-war relation predicate remains for the parent to resolve without inventing one.

Keep operational, mature, and response-capable counts separate.
Operations triggers `:992-995` define operational as guided stage plus a working site, `032_missiles_triggers.txt:116-123` defines mature as complete stage, and operations triggers `:1031-1041` add advanced stage, control, reserve, and a secure site for response capability.
Part 4:99 requires a stage-2-or-higher share for Saturation, while `:836-838` requires two operational countries and at least one capable responder for Retaliation.
Its overview `:15` says two countries can support retaliation, so that shorthand and the detailed rule must not be silently treated as two mature responders.
The current firing snapshot `operations_effects:30-73` uses weaker/different guided, vulnerability, and payload predicates and cannot replace the complete evolution measurement unchanged.

Reuse `missiles_evolution_timing`, `missiles_evolution_pressure`, and `missiles_evolution_pacing` in `common/script_constants/032_missiles_constants.txt:414/:786/:812`.
Preserve ordinary base targets of 90/105/120/120/150 days and the explicit first-fire `21 + 14 × eligible-track-index` exception.
The existing randomized 0.75-1.25 delayed job is not native MTTH.
Retire its ordinary-delay/watch tuning consumers as part of migration rather than retain a fallback clock.
Part 6:527-550 asks the probability pass to account for program count, launches, reserve, vulnerable owners, payload owners, and actual hostile pairs.
No balance targets or new constants were selected here.
No new event targets are needed for this owner route, and helper/API documentation belongs with the parent's eventual patch.

Evidence and validation limits:

- `hoi4.source_lookup` resolved `missiles_measure_evolution_pressure:543-594` at workspace revision `d2d484d00542c47f960e898d9f832a2e5f5782b89f9a619521000e245845cf9c`. Its inline body was truncated, and the full relevant local source was read separately. Operations source SHA-256 was `5f803dd63867d0303d19e7e7e388f00ba6440130b53237ffbe961b715d0ae67b`.
- `hoi4.reference_context`, `reference_search`, and `reference_read` succeeded. Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150` revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` supplies polling, hazard, variables, and once-only rules. Installed `documentation/effects_documentation.md:2943-2967` revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` supplies the delayed country-event contract. The context bundle omitted additional topics, so it is not evidence of comprehensive reference coverage.
- Direct installed reads: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\_documentation.md:1-111`, SHA-256 `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`, and `events\AAT_Iceland.txt:182-198`, SHA-256 `26114b8af98adbdb78db9e2491d99b0a995ce4508271722ecdfc9e25d50bf278`.
- Probability discovery succeeded with `requested_adapter_empty`, zero native MTTH candidates in the unchanged Event 32 event file, source hash `2096d97d46e15f4a9abca1925a9960e8f50d29f12409f0380df670e55d657c7e`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38b42fdd2557567b13759c72980a8691cac86f8984d96eb641646586282f80f1/300ca80539aa5c9af1665218bcf4a3de17bc89190d0ec87724571c1b85e5f50b/probability-inspect-2096d97d46e1.json`.
- The bounded `.190` event trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis, and zero helper projections, revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a6f6351d347d6c1b45b32097b3f828b01df692f088d8e3dcf3243a74d34fc29/56826505781fc045a510bfa66ebc52162e1cff9fa9e873279b72080a5a7e22c1/event-trace-db07bcddfa36.json`. No full helper/lifecycle or runtime coverage is claimed.
- The interrupted request's prior exec handle was unavailable on resume. Fresh read-only calls succeeded, so no current MCP outage is asserted. Large linked reports were not expanded for this requested immediate handoff.

Parent validation must cover native-only eligibility gain before a later pulse, stale-positive rejection, lapse-and-recovery between observations, the 899-to-900 crossing without tier change, disable/re-enable, host loss with surviving and zero programs, duplicate deliveries, native/legacy exclusivity, and the two pair-count counterexamples.
No engine execution, timing implementation, probability evaluation/compare, or specialist auditor pass was performed here.
The parent owns that evidence pass through `chaosx_ai_probability_auditor` under the same named scenarios after preserving the baseline.
No gameplay simplifications or substitute polling route were implemented.
