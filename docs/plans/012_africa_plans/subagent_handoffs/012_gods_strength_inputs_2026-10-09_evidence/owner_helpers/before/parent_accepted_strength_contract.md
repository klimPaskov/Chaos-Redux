# Event 012 Strength input contract

Disposition: fundamental census, competition-only military multiplier, explicit zero-army guard and 50/50 political/physical continental blend are `accepted and queued` by parent selection on 2026-10-09 within the full-Gods goal.
The capital/port strategic proposal is `accepted and queued` pending verified province-port aggregation and owner/site semantics.
Rail/resource/base families and unknown-object coverage remain unresolved rather than being replaced with proxies.
The fundamental owner-helper patch is in progress, with final parent integration and required checks outstanding.
This is a source plan, not an implementation or Event 012 completion claim.
Only this handoff was written, with no gameplay, test, Git, game, GUI, or spreadsheet operations.

## Acceptance basis and preserved behavior

The current task explicitly accepts the factor families in `docs/specs/012_africa_is_one_gods_of_africa_specs/specs/012_gods_of_africa_full_spec.md:145–203` and asks for a bounded recommendation for physical territory and world-relative army inputs.
The factor families and prohibition on new recurring world hooks are accepted requirements.
The numerical blends, proposed internal fields, and strategic-site definitions below are proposals, not additional accepted design.
The earlier `012_gods_strength_control_registry_research_2026-10-08.md` is historical research, not a requirement to obtain map or event renders.

Preserve outer component weights 25/20/20/15/10/10, Chaos normalization, evolution amplifiers, industry, reach, internal condition, surrender penalties, capital penalty, ordinary smoothing step 8, public Strength publication, and doctrine/punishment ceilings.
The actual `gods_of_africa_strength.divisions_divisor` is **20**, not 2, at `common/script_constants/012_africa_gods_constants.txt:335`.
Twenty divisions therefore supply 1 point before the optional readiness average.
The pinned source's sustainment shares are **0.6 equipment and 0.4 fuel**, with floor 0.4 and span 0.6 at lines 373–395.
The brief's 80/20 description conflicts with that source.
Do not change sustainment tuning in this repair.

The parent's eight-file baseline is `012_gods_strength_inputs_2026-10-09_evidence/before/manifest.json`, with recorded HEAD `c158d857fc06feb39853b616aad9daf57f4b28c8`.
All eight copied-byte SHA-256 values were verified, and all eight current source files matched those snapshots during this read.
No Git command was used to establish this result.

## Recommended tuning first

Add `common/script_constants/012_africa_gods_strength_inputs_constants.txt` with one unique category `gods_of_africa_strength_inputs`.
Its first entry must be `schema = { any_key = yes data = fixed_point }`.

| Key | Proposed value | Purpose |
| --- | ---: | --- |
| world_share_anchor | 0.10 | Ten percent of deployed world army manpower removes the competition discount. |
| military_absolute_share | 0.75 | Preserve at least three quarters of the existing nonzero military component. |
| military_relative_share | 0.25 | World competition can reduce that component by at most one quarter. |
| continent_political_share | 0.50 | Preserve half the existing cooperative/authority/recognition component. |
| continent_physical_share | 0.50 | Give measured physical control half the continent component. |
| territory_geography_share | 0.80 | Geographic/core evidence supplies most of the physical component. |
| territory_strategic_share | 0.20 | Operational capital/port retention supplies the remaining bounded share. |
| strategic_capital_share | 0.50 | Capital-site retention inside the strategic subcomponent. |
| strategic_port_share | 0.50 | Operational port retention inside the strategic subcomponent. |
| major_territory_loss | 0.15 | A loss of fifteen percentage points since the owner sample triggers the existing immediate path. |

Reuse existing zero, one, and component maximum constants.
Each pair of blend shares sums to one.
No new duration field or public metric is necessary.

## Complete known-country universe within the existing pass

At `africa_initialize_scramble_and_world_packages`, `common/scripted_effects/012_africa_world_order_effects.txt:820–825`, initialize a separate host-owned `gods_of_africa_strength_countries` array and clear its census-complete receipt.
At lines **905–913**, retain each supplied country object **before** `gods_of_africa_candidate_can_be_remembered` runs.
Keep the existing candidate insertion and candidate filters unchanged.
There is one traversal of `global.countries`, with two different consumers inside it.

Measurement-roster admission has no existence, major, player, humanity, special-country, geography, or host exclusion.
It retains dormant tags and any reserved dynamic objects exposed by the engine array.
Deduplicate by country object using `is_in_array` on the measurement array.
Record `gods_of_africa_strength_census_size = global.countries^num` and set `gods_of_africa_strength_census_complete` only after that pass finishes.
Do not borrow `gods_of_africa_candidate_census_complete` as proof of measurement coverage.

The installed getter documentation describes `global.countries` as all countries including nonexistent objects.
Vanilla `COG_set_up_african_resistance_states` and `COG_setup_freedom_at_gunpoint_array` iterate that array and explicitly select `exists = no`.
This is a genuine known-country universe, unlike the ordinary Gods candidate roster.
During measurement, include every retained object satisfying `exists = yes`, including nonhuman/special countries, governments in exile, minors, and capitulated countries with a living army.
Do not apply participant eligibility or a capitulation exclusion to the world denominator.

For later named transactions, insert the country independently of participant validity and before the ordinary participant path's settlement gate.
Use the existing ROOT/FROM calls in `common/on_actions/012_africa_gods_on_actions.txt:14–16,88–113`.
A named release/government callback can append a newly allocated object even when it fails candidate membership in `global.countries`.
No new global discovery hook is proposed.

**Coverage limit:** native collection-input documentation distinguishes existing from possible countries but does not explicitly certify the dynamic allocation pool.
The offline wiki's game-array table says `countries` includes the 50 dynamic countries even before an original tag is assigned.
That supports reserved-slot coverage, but does not prove that every future engine/mod-created object belongs to the frozen set or fires these existing callbacks.
Dormant loaded-tag releases are covered by retained object identity.
Dynamic objects already retained are covered when they become live.
An object allocated outside the set and never named by these callbacks is a real gap.
On the existing owner clock compare current `global.countries^num` with retained census coverage as a diagnostic, without rescanning it.
Cardinality equality alone cannot prove identity equality.
Mark `gods_of_africa_strength_world_coverage_incomplete` if an observed mismatch cannot be reconciled by named insertions.
Never call a known-incomplete sum an exact world total or silently replace it with a major/candidate proxy.
A guarantee covering unknown objects would require a separately accepted discovery contract, which this recommendation does not authorize.

## Exact helpers and internal data contract

Use the parent's staged `common/scripted_effects/012_africa_gods_strength_inputs_effects.txt` and matching `.md` documentation.
The parent supplied and this task read the unwired `gods_of_africa_measure_territorial_control` collector after the initial contract draft.
Retain that API and its field names, adding the world and member/site contracts in the same owner surface without a competing territorial collector.
Add an owner-API link to `common/scripted_effects/chaosx_dynamic_effects.md` rather than moving Event 012 orchestration into the shared helper file.
The inspected shared dynamic registry has no country-census or ownership-control helper that supplies this contract.

| Boolean effect call | Scope and inputs | Outputs and side effects | Direct callers |
| --- | --- | --- | --- |
| `gods_of_africa_remember_strength_country = yes` | COUNTRY object, authoritative host target and initialized measurement roster. No existence or candidate filter. | Idempotently appends THIS to the host roster. No gameplay grants or participant enrollment. | Existing one-time census before its filter, existing named onboarding callbacks. |
| `gods_of_africa_measure_strength_armies = yes` | Committed HOST, complete retained roster. | Replaces host normal `gods_of_africa_strength_world_army_k`, `gods_of_africa_strength_host_army_k_sample`, `gods_of_africa_strength_army_sample_day`, and sample host-id/generation. Reads `deployed_army_manpower_k` from each live entry. | Activation before first refresh, due owner review before refresh, legitimate owner rebind before reuse. |
| Existing `gods_of_africa_measure_territorial_control = yes` | Current HOST, native Africa collection. No caller inputs or temporary outputs. | Existing normal territorial counts, score and observation day listed below. Proposed member/site counting extends this same state pass. Changes no ownership, cores, diplomacy or buildings. | Proposed integration into existing `gods_of_africa_refresh_strength`, including ordinary owner and relevant transaction calls. |
| `gods_of_africa_blend_strength_inputs = yes` | ANY scope, caller-initialized unscoped numeric temporary inputs for old military/continent, current host army, corrected cached world army, land/core/site counts. | Overwrites caller-initialized temporary military/continent outputs. No persistent mutation or random selection. | `gods_of_africa_refresh_strength` after existing sustainment and recognition arithmetic. |
| `gods_of_africa_clear_strength_input_sample = yes` | HOST object. | Clears cached sums, sample identity/day, counts, previous-loss samples and internal validity/dirty flags. Discovery rosters are retained through loss/recovery/settlement until the parent-owned Event 012 lifetime ends. | Existing Gods cleanup/revocation and transfer invalidation paths. |

All effect calls use `= yes`, with documented caller variables where required and explicit outputs, never named argument blocks or `$PARAM` substitution.
Initialize temporary outputs before invoking a helper so their values survive returning from a scripted effect.
Temporary variables are unscoped, so never use `ROOT.temp` or `PREV.temp`.
Use normal host fields or caller-supplied host-id/generation when scope persistence is needed.
Boolean conditions use flags or pure triggers, not persistent numeric 0/1 variables.
Any extracted legitimacy predicate is a pure COUNTRY trigger reading the caller's host identity/generation and existing member receipts, with no writes or parameter macro.
No new global event targets are required.
Use the existing `event_target:africa_host` and transfer target, with explicit identity checks instead of assuming native ROOT is the host in callbacks.

## Military equation and cache lifetime

Use **deployed army manpower in thousands**, `deployed_army_manpower_k`, for numerator and denominator.
This is a direct fielded-land-force quantity documented in both source families.
It avoids treating a tiny formation and a large formation as equal in the relative measurement.
It does not measure foreign equipment quality, air/naval capability, or foreign sustainment.
Those limits must remain explicit.
Keep the existing host division/readiness/sustainment calculation as the absolute capability ceiling.

Let `A` be the current host's deployed army manpower and `W` the sum across all living roster entries.
The host is **already one row of W**.
Never calculate `host + sum(roster)`.
Let `q = A / W`, with `q = 0` when W is zero and a guarded validity flag for absent/incomplete samples.
Compute divisions/readiness exactly as current source, clamp to 0–100, and multiply by the current sustainment factor to obtain `M_old`.

Recommended military output:

`M_new = M_old × (0.75 + 0.25 × clamp(q / 0.10, 0, 1))`.

If the host has zero deployed divisions or zero deployed army manpower, set the military output to zero.
This explicit zero-army branch prevents readiness alone from supplying an army component.
That is the only proposed change to the physical/readiness guard.
The new multiplier never exceeds one and therefore cannot inflate a weak host above its existing physical/readiness/supply result.
A high share in an almost empty world also cannot manufacture absolute power.

Sample W on the **existing due 30-day owner clock**, activation, or legitimate owner rebind.
Do not resample all retained countries on every battle callback or every demand refresh.
Between samples correct only the host row: `W_now = W_sample - A_host_sample + A_host_now`.
This removes the old host contribution before adding its current value, so host losses are immediately reflected without self-double-counting.
Foreign army changes remain a 30-day sample until the next owner review.
This is a cached world-relative input, not an exact instantaneous world total.
Missing census/sample evidence is a lifecycle defect to repair, not a reason to claim q is zero or silently disable the factor.

## Physical African territory and legitimate member separation

Use `every_collection_element = { input = collection:states_in_africa ... }`.
The selector key is **input**, not `collection`.
The native collection supplies the complete geographic state universe using `game:all_states` and the Africa continent limit.
Do not enumerate manual IDs, use country capital geography as a territory denominator, or substitute host cores for all Africa.

Count each African state once, into mutually exclusive ownership/control buckets:

| Internal count | Exact meaning |
| --- | --- |
| Existing `gods_of_africa_strength_african_state_total` | N, every element of the native Africa collection. |
| Existing `gods_of_africa_strength_african_owned_states` | Host-owned African land, including land lost to occupation. |
| Existing `gods_of_africa_strength_african_controlled_states` | Host-controlled African land, including occupation of foreign land. |
| Existing `gods_of_africa_strength_african_secured_states` | H, owned **and** controlled by the current host. |
| `gods_of_africa_strength_member_states` | L, owned and controlled by the same live, non-capitulated, registered current-generation cooperative member, excluding the host. |
| Existing `gods_of_africa_strength_african_core_total` | K, every African state that is a core of the current host, regardless of owner/controller. |
| Existing `gods_of_africa_strength_african_secured_cores` | Hc, states in H that are host cores. |
| `gods_of_africa_strength_member_core_states` | Lc, states in L that are host cores. |
| `gods_of_africa_strength_occupied_states` | Host or legitimate member owned African land controlled by an outsider. Diagnostic only, never counted in H/L. |
| Existing `gods_of_africa_strength_territorial_control` | 100 Hc/N, direct secured host cores as continental extent. |
| Existing `gods_of_africa_strength_territory_observation_day` | Date of the authorized territorial observation. |

Member legitimacy requires membership in the host's `africa_relationship_countries`, `africa_member_host_generation_is_current`, and `africa_relationship_is_cooperative`.
The latter permits protected, associate, chartered, autonomous federal, and integrated relationships.
Resistant, leaving, rival-bloc, occupied-settlement, outside, stale-generation, capitulated or unregistered countries cannot supply L.
An unrelated faction ally cannot supply L.
The member bucket represents sovereign cooperative capability and must never be described as direct host ownership.
Foreign land merely occupied by the host is outside H/L.
Allied cross-control is also outside these conservative self-owned/self-controlled buckets.
Crediting that cross-control would need a separate accepted rule.

Maintain direct ratios H/N and Hc/K separately from member ratios L/N and Lc/K.
For separate diagnostics use `U = (H + L) / N` and homeland retention `C = (Hc + Lc) / K`.
Use zero for ratios whose measured numerator is zero.
If K is genuinely zero, flag homeland retention as unavailable rather than pretending it is 100%.
If N is zero, flag the geographic measurement invalid and return zero physical territory pending correction.
Core recognition at `012_africa_action_effects.txt:7320–7328` can grant host cores on member-owned land without control, so core membership alone never proves retention.

For the minimum scored blend use **`F = (Hc + Lc) / N`**, preserving the staged collector's secured-core continental-extent semantics.
In implementation terms F is `gods_of_africa_strength_territorial_control / 100` plus `gods_of_africa_strength_member_core_states / gods_of_africa_strength_african_state_total`, with clamp 0–1.
The member term remains separately recorded and never changes the existing direct-host territorial output.
K supplies the separate homeland retention ratio, not a denominator that makes a compact host look continent-wide.
Noncore owned/control counts remain measured diagnostics, with no unaccepted new noncore reward coefficient.

## Strategic sites and transaction responsiveness

Strategic evidence is required by spec lines 173, 176 and 191.
The following minimum source families must remain explicit rather than being replaced by charter authority or recognition.

**Capitals:** retain unique African capital STATE scopes supplied by live countries in the existing census, plus the host's African institutional capital.
Maintain `gods_of_africa_strength_capital_sites` independently of participant eligibility and append newly named African capitals when a release/member transaction supplies them.
Retain old anchors when an emergency capital moves, so relocation does not erase a lost institution.
On legitimate succession preserve the old continental sites and append the successor's capital once.
Current `capital_scope` alone can move after occupation and is insufficient as the historical anchor.
The denominator is explicitly Event 012's retained capital sites, not an asserted census of every dormant historical African capital.

**Ports:** maintain unique African state scopes in `gods_of_africa_strength_port_sites`, seeded and extended during the same bounded Africa state measurement when `building_level@naval_base` is positive.
For retention require H/L ownership-control eligibility and positive `non_damaged_building_level@naval_base`.
Retain the site after destruction or control loss so the denominator cannot shrink away a defeat.
Both getters are documented state building-type getters, but state aggregation of province naval bases needs parent source/engine-semantic review.
A coastal state is not proof of a port and a completed port action flag is not proof it remains operational.

Let retained capital and port fractions be Ca and Po.
Use their average `J = 0.5 Ca + 0.5 Po` when both families have sites, or the present family's fraction when one is empty.
If both are genuinely empty, use F with an explicit unavailable-site receipt, avoiding a fabricated strategic capability.
Physical component proposal: `T = 100 × (0.80 F + 0.20 × min(F, J))`.
Geographic/core capability caps the strategic term, so a tiny host cannot gain continental control merely by holding its sole capital and port.
Blend the old political continent value only after recognition and its existing clamp: `Continent_new = 0.50 Continent_old + 0.50 T`.

**Rail corridors/resources/foreign bases:** the existing capital railway receipt and `has_railway_connection` at `012_africa_action_effects.txt:7267–7294` are a usable topology pattern.
Rail existence alone does not establish corridor ownership, operational control, damage or supplies.
The source `africa_scramble_foreign_base_holder` at `012_africa_world_order_effects.txt:669–674` is assigned for any owned African state and is a colonial-interest proxy, not an active-base measurement.
`resource@steel` and other state getters supply physical extraction, but the accepted Event 012 strategic resource/site roster and weighting are not established by this bounded read.
Do not claim the proposed capital/port subcomponent fulfills these additional source families.
The parent must retain these gaps explicitly or resolve their existing owner/site contracts before claiming the full Strength-source specification complete.

Extend existing `on_state_control_changed` in `012_africa_world_order_on_actions.txt:450` using documented ROOT=new controller, FROM=old controller, FROM.FROM=state.
Inspect only that African state and the host/member/site identity relevant to it.
Refresh measured land and the existing Strength helper for relevant capture/recovery, using the cached military denominator.
Reuse `gods_of_africa_strength_immediate` for a retained institutional-capital loss or a cumulative U drop of at least 0.15 from the last owner sample.
Ordinary smaller changes retain smoothing.
Do not install a second world scan, world hook, recovery clock or new damage penalty.
Extend existing pairwise `on_war_relation_added:42`, peace/annex/capitulation callbacks and `africa_apply_relationship_transition:1425` only to invalidate/refresh the relevant host sample.
Keep the existing owner dates and scheduler unchanged.
Native state-controller events do not prove ownership-only transfers or every direct script mutation invokes the same callbacks, so the owner-clock land recount remains the bounded repair path.

## Succession, cleanup and migration order

1. Preserve the baseline and select the proposed tuning/site semantics before implementation.
2. Add constants and documented owner helpers, then initialize the measurement roster inside the existing pre-filter census.
3. Sample armies before activation refresh at `012_africa_gods_effects.txt:621–623` and before due owner refresh at `:147–149`. Integrate the parent's existing territorial collector, without declaring its unwired source complete.
4. Blend into `gods_of_africa_refresh_strength:630–816` after existing sustainment and continent recognition. Leave its outer weighted sum/public publication unchanged.
5. Extend named country registration independently of candidate filters. Add local transaction refreshes without changing demand, settlement or clock permissions.
6. Extend `africa_host_transfer_stage_arrays:685`, `africa_host_transfer_restore_world_order_state:439`, and `africa_host_transfer_clear_staging:1439` to stage, restore and clear the measurement roster, site arrays, census receipts and coverage metadata.
7. Invalidate cached army/land sums and old sample identity after restoring the successor. Recount only when the existing Gods epoch/owner rules authorize that host. Roster inheritance does not confer Gods mandate or start tribute.
8. Clear temporary transfer staging only after successful copy. Preserve suspended-crisis staging, following the existing transfer contract. Do not prune a dormant former host or add the successor as a separate army summand.
9. Extend `gods_of_africa_clean_system:4751` and original-epoch revocation to clear transient samples and loss flags. Retain discovery data for the existing bounded recovery lifecycle. Clear discovery/site arrays on the parent-owned final Event 012 teardown, not Scramble cleanup or ordinary Gods settlement.
10. Update the helper `.md`, shared owner index, `docs/events/012_africa/gods_of_africa.md` and relevant accepted-spec implementation evidence. Existing public cause wording may describe held territory and stronger foreign armies qualitatively, with no new public counters. The parent owns localisation and any decision/UI changes.

Use native scope iterators, not numeric `for_loop_effect` or `while_loop_effect` over whole country/state cardinality.
Installed defines set `MAX_EFFECT_ITERATION = 1000`, and the wiki explicitly warns about that cap for numeric loops.
Do not silently truncate a roster at 1000 or assume an undocumented collection/array cap bypass.
For any iterator uncertainty the parent should compare processed-row count with the intended roster/collection cardinality, with completeness kept distinct from arithmetic validity.

## Representative arithmetic, not campaign probabilities

The following cases use actual division divisor 20 and the existing military/continent outer weights 0.25/0.20.
R is readiness and S is the already computed unchanged sustainment factor.
All other components are held constant and capital/surrender penalties are excluded unless stated.
Values are continuous arithmetic expectations before smoothing and engine rounding, not native execution proof.

| Case | D, R, S, world share q | Old military → proposed | Old continent → proposed | Change in raw weighted Strength |
| --- | --- | --- | --- | ---: |
| Weak compact Africa | 20, 20, 1, 1%. F=5%, J=5%. | 10.5 → 8.1375 | 60 → 32.5 | -6.090625 |
| Strong Africa | 800, 80, 1, 20%. F=80%, J=80%. | 60 → 60 | 80 → 80 | 0 |
| World competition at anchor | 400, 60, 1, 10%. F=80%, J=80%. | 40 → 40 | 60 → 70 | +2 |
| Same Africa, larger world armies | Same host, q=4%. Same land. | 40 → 34 | 60 → 70 | +0.5, which is 1.5 below the preceding case |
| Occupation | 400, 60, 1, 10%. F=30%, J=30%. | 40 → 40 | 60 → 45 | -3, which is 5 below the unoccupied anchor case |
| Unsupported army | 400, 60, S=0.4, 10%. Same strong land. | 16 → 16 | 60 → 70 | +2 entirely from physical territory |
| Zero deployed army despite readiness | 0, 60, 1, q=0. Same strong land. | 30 → 0 | 60 → 70 | -5.5 |

Without readiness, a weak 20-division host has M_old=1 and M_new=0.775 at q=1%, rather than receiving a new ten-point military bonus.
At q=0 and positive physical capability the proposed world multiplier is 0.75.
At or above q=10% it is 1.
Sustainment remains a multiplicative ceiling, with no later world-share addition to bypass it.
If every living army is zero, W=0, A=0 and military output is zero without division by zero.
If no valid host exists, measurement/publication is rejected by the current owner lifecycle and existing cleanup owns public zeroing.

Host-switch conservation case: total world army=4000k, outgoing host=100k, successor=200k, each present once in the same roster.
World total remains 4000k after transfer. Host share changes from 2.5% to 5%.
Their world multipliers are 0.8125 and 0.875 respectively, applied to each host's own unchanged absolute component.
The outgoing host remains a denominator row if alive. A duplicate successor insertion must leave cardinality and W unchanged.
Transfer with invalid Gods authority must not refresh or publish either as an authorized Gods host.

## Evidence and validation limits

HOI4 reference/source routes were absent from this session's connected tool inventory.
No reference request, MCP job, graph, viewer or renderer was attempted, and none is claimed as passed.
Direct local reference reads were used, without accessing the online wiki.
The parent owns source implementation, final lifecycle validation, and the `chaosx_ai_probability_auditor` baseline/compare for weighted consumers affected by Strength.
No weighted helper was changed and no probability audit was commissioned here.
The deterministic case arithmetic above is source-derived reasoning, not a replacement for that parent audit.

Primary local citations, with revisions for additional reads appended below:

- Parent `initial_reference_evidence.json` records exact SHA-256/path/spans for native `common/collections/collections.txt:303–312`, `_documentation.md:20–41`, `COG_scripted_effects.txt:196–215`, `documentation/script_collection_input.md:36–60`, and offline Data structures `:1263–1274`.
- Installed `documentation/dynamic_variables_documentation.md:271–272,553–555,972–975,1101–1102,1112–1119,1139–1143,1157–1158` establishes the manpower getter, division-control caveat, countries array and state getters.
- Installed `documentation/effects_documentation.md:3763–3796,4296–4311,6496–6512,2733–2741` establishes collection/array iteration and target lifetime operations.
- Installed `documentation/triggers_documentation.md:5381–5397,6006–6014,6079–6095,4603–4626` establishes control/core/geography/ownership and railway checks.
- Installed `common/factions/goals/faction_goals_long_term.txt:160–168` is the primary iterator precedent using `every_collection_element` with an `input` field. For Africa the direct selector is `input = collection:states_in_africa`.
- Installed `common/scripted_effects/COG_scripted_effects.txt:239–253` gives the second dormant-country array precedent.
- Installed `common/on_actions/00_on_actions.txt:4911–4914,5075–5076` establishes war/capture callback scopes, and `common/defines/00_defines.lua:25` records the iteration ceiling.
- Installed `documentation/script_concept_documentation.md:184–215,216–239` and `common/script_constants/documentation.md:12–32` establish math-expression caveats, constants and schema-first categories.
- Offline Data structures `:429–449,1069–1077,1214–1220,1779–1787,1591–1594` establishes variable/array scoping, iterator limits, the wiki dynamic-pool claim and deployed manpower units.
- Offline Effects `:151`, Scopes `:388–392,639–650`, Triggers `:1842–1854,1867`, and On actions `:448–450,250,257–259` provide parallel collection/control/core/callback references.

Meaningful validation performed: exact baseline-byte verification, candidate/census/transfer/owner call-path review, dormant-country vanilla precedent review, and numerical weak/strong/competition/occupation/zero/succession cases.
Not performed: gameplay patch validation, foreign-object allocation coverage, province naval-base aggregation, operational rail/resource/base certification, or engine fixed-point execution.
No requested implementation was simplified because this task produced a recommendation only.
The recommendation has explicit limitations for unknown dynamic objects, sampled foreign armies, allied cross-control and the unresolved rail/resource/base source families.
These must remain visible in the parent's implementation disposition.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were changed.

### Local reference revisions

Paths in the first table are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
These are local file SHA-256 revisions, not MCP revisions.

| Installed path | SHA-256 |
| --- | --- |
| documentation/dynamic_variables_documentation.md | 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda |
| documentation/effects_documentation.md | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| documentation/triggers_documentation.md | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| common/factions/goals/faction_goals_long_term.txt | 8b356091135ba0390f9acaca4c8a80c7fd9d7a4117abe120ee2ce819c88d1350 |
| common/scripted_effects/COG_scripted_effects.txt | 77fd69835f9a7115fc60d85de61c5c31e4c7880e30fb6d6e8ae494f318b02710 |
| common/on_actions/00_on_actions.txt | 52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9 |
| common/defines/00_defines.lua | 405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4 |
| documentation/script_concept_documentation.md | 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7 |
| common/script_constants/documentation.md | e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c |


| Repository offline wiki path | SHA-256 |
| --- | --- |
| paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| paradox_wiki/Effects - Hearts of Iron 4 Wiki.md | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md | 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md | abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06 |
| paradox_wiki/On actions - Hearts of Iron 4 Wiki.md | 6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a |

Parent source review also identified the existing `africa_is_current_host` predicate as ROOT-dependent.
The input owner must use an exact COUNTRY-object predicate against `event_target:africa_host`, and the integration must avoid borrowing native ROOT from unrelated callback/scenario countries.
The prototype's six typed territorial cases cover counting but its first authorization fixture hid this legacy predicate behavior.
The owner implementation must execute its actual corrected authorization predicate before claiming ROOT-independent acceptance.
