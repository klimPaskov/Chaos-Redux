# Event 096: force measurement and national allowance

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

All coefficients in this file are selected initial tuning values for the proposed design.
Country inputs remain live.
The native-counter and accounting gates in Part 7 must pass before these equations are represented as working game behavior.

## 1. A structural force unit

One force point is a balancing unit for an ordinary fielded battalion or basic support attachment.
It is not a literal number of soldiers, a division, combat width, or industrial cost.
More demanding types consume more points.
This permits a common allowance to include conventional forces and armies with zero ordinary manpower.

Let N be the total number of fielded land sub-units covered by the native aggregate, including support after the boundary is proved.
For each exact sub-unit type b, let n_b be its fielded count and w_b its final weight.

**F = N + sum over known types of (w_b minus 1) multiplied by n_b.**

Every type receives a baseline of one.
Each known type receives exactly one final profile, not cumulative additions for every category it belongs to.
All selected premiums are nonnegative.
An unknown counted type therefore never has zero weight and never reduces the force total.

The preferred documented inputs are country `num_battalions` and `num_battalions_with_type@<exact_subunit_id>`.
Their reference wording describes battalions within land divisions.
Existing CBRN source uses typed counters for support definitions.
The total's support inclusion and foreign attribution remain native acceptance gates.
R02, R04, and R05 document the distinction.

### Initial weight profiles

| Structural profile | Weight per sub-unit | Why this profile exists |
| --- | ---: | --- |
| Ordinary foot infantry, cavalry, foot special forces | 1.00 | Common structural baseline |
| Basic support attachment | 1.00 | A small attachment still commits specialized staff and support capacity |
| Motorized infantry and motorized reconnaissance | 1.25 | Transport and maintenance beyond the baseline |
| Towed line artillery, anti-tank, anti-air, comparable heavy weapons | 1.50 | Equipment and sustainment burden |
| Mechanized infantry and armored-car combat formations | 1.75 | More demanding vehicle establishment |
| Light armor and comparable light tracked formations | 2.00 | Armored establishment |
| Medium or modern armor, corresponding self-propelled combat formations | 2.50 | Heavier armored establishment |
| Heavy armor and corresponding heavy self-propelled formations | 3.00 | High equipment and support commitment |
| Super-heavy armor | 4.00 | Exceptional material commitment |
| `autonomous_robot` | 3.00 | Concrete zero-human armored formation already present in the project |
| `rat_swarm`, `rat_burrowers`, `rat_dock_stowaways`, `rat_tunnelers` | 1.00 | Positive coverage despite zero human manpower and absent conventional equipment needs |
| `rat_brutes`, `rat_carrion_guard` | 1.50 | Heavier rat formation profiles |
| CBRN support companies (`common/units/cbrn_hq_support.txt`, `cbrn_regimental_support.txt`) | 1.00 | Ordinary support attachments; chemical capability is not a structural premium |
| Livens projector support (`common/units/livens_projector_support.txt`) | 1.50 | Heavy-weapon support burden, matching towed heavy weapons |
| Any other unclassified land sub-unit | 1.00 | Complete positive baseline until an explicit profile is assigned |

The current Chaos Redux unit files also define zombie, ghost-host, elephant, strange-force, cannibal irregular, project-force, cave-brood, clone, coal-golem, chaos-battalion and assassin sub-units (`common/units/`).
Each family needs a reviewed explicit profile before balance signoff; until then the 1.00 baseline applies, never zero.

The coding owner must build an exact installed sub-unit inventory and resolve profile precedence once.
An armor and mechanized category overlap does not add both premiums.
A support version receives its own exact classification, rather than accidentally inheriting the full line profile through a broad category query.
Existing anomalous types that visibly depart from the baseline receive a reviewed explicit profile before balance signoff.
This is a mapping and balance audit, not permission to change another event's unit stats.

Technology upgrades, design variants, doctrines, advisors, and Military Madness do not automatically change w_b.
The count follows actual structure.
A deliberate replacement of one sub-unit type with another does change the total.
Weight changes made by a future mod update require versioned recalculation of active incidents.

### Support boundary resolution

If the installed total includes support attachments, use the preferred equation directly.
If it excludes support but exact typed support counters work, add the full support weights separately and apply premiums only to the combat total.
Inventory every installed support definition and provide a registration contract for future additions.
Do not count a support company in both terms.

If neither documented counter exposes actual fielded support, this requirement remains blocked pending a proven exact alternative.
A combat-battalion-only result must not be shipped as the complete design.
A division-count fallback, per-division Boolean type-presence score, or human-manpower proxy is also unacceptable.

## 2. What is counted

The intended owner is the country that owns the formation and its establishment, even if the formation operates abroad.
Merely hosting an allied army does not make it part of the host's force budget.
Sent expeditionaries and volunteers remain attributable to their source owner.
Borrowed foreign formations are not counted twice.
Exile and colonial arrangements must follow the actual owner, not the manpower donor alone.

This is a definition that the native aggregates must satisfy.
Do not assume their ownership semantics match the country division iterator without testing both.
A transfer between owners must conserve global counted structure, and there must be no instant in which both countries omit it.

| Included | Treatment |
| --- | --- |
| Deployed combat battalions | Count full current template establishment |
| Deployed support attachments | Count the chosen structural weight |
| Understrength, encircled, out-of-supply, or disorganized formations | Same structural burden until actual structure changes |
| Robot, rat, undead, and other special fielded formations | Count positive structural weight |
| Protected provider-owned formations | Count even when the voluntary removal pool excludes them |
| A formation granted while the lock is active | Count on the next refresh and before any release or action |

Unused template definitions, manpower reserves, the deployment queue before deployment, occupation garrisons represented outside division units, intelligence decoys, air wings, ships, and stockpiled equipment are not fielded division structure.
Standalone railway guns and state defenses are outside the division-template formation measure.
They do not provide an alternative way to conceal battalions.
These boundaries require fixture verification where the native total is not explicit.

A merge is invariant when it preserves the same multiset of battalions and attachments.
A merge that removes real support companies legitimately changes F.
Do not demand numerical equality after actual structure has been removed.

## 3. Live national capacity

Use controlled territory for the population and territorial contribution.
Ownership without control, claims, faction membership, and subjects' territory do not supply those inputs.
This lets conquest raise capacity before a peace conference while preventing a defeated country from retaining the capacity of land it no longer controls.

For each controlled state s, define access q_s as follows:

- If the state is a core of the inspected country, q_s is 1.
- Otherwise q_s is 0.25 plus 0.75 multiplied by current compliance expressed from 0 to 1.
- Clamp the compliance input to its documented range before use.
  If a non-core state has no valid compliance model, use the 0.25 access floor.

The non-core floor gives immediate but limited benefit from conquest.
Integration and compliance then improve usable national capacity.
It does not grant direct manpower, factories, cores, or compliance.

Define these internal inputs:

| Input | Exact selected meaning |
| --- | --- |
| P | Sum of q_s multiplied by current state population in millions, using `state_population_k / 1000` |
| T | Sum of q_s multiplied by `(0.5 + 0.1 multiplied by infrastructure level)` across controlled states, with infrastructure bounded to the installed legal range and normalized to the five-level reference |
| C | Current total domestic civilian factory capacity assigned to this country, including valid offsite factories, excluding factories received temporarily through trade |
| M | Current total domestic military factory capacity assigned to this country, including valid offsite factories |

C and M use total factory capacity, not the currently idle factories, construction allocations, consumer-goods remainder, or current production output.
A player cannot change its allowance by pausing a construction project or moving factories between equipment lines.
Subject and occupied industrial contributions are counted once through the country's actual assigned factory capacity, without adding the subject's entire factory stock to an overlord again.

The initial policy counts completed factories through temporary bombing damage.
Permanent removal, loss of the factory's assigned territory, conversion between civilian and military industry, and genuine offsite gains change the inputs.
This avoids turning short repair fluctuations into an additional daily punishment.
It is a deliberate measure of industrial base.
The native total-factory getters must be verified against this policy.
If they differ, implement the same accounting with proven state and offsite inputs, rather than silently substituting available factories or excluding offsite capacity.

The proposed baseline capacity is:

**A_raw = 10 + 5P + 2T + 3C + 5M.**

The final allowance at evolution regime e is:

**A = round down to the nearest 0.25 of max(10, s_e multiplied by A_raw).**

| Regime | s_e |
| --- | ---: |
| Base | 1.00 |
| Evolution I | 0.85 |
| Evolution II | 0.80 |
| Evolution III | 0.70 |
| Evolution IV | 0.55 |

Apply only the highest active multiplier.
Do not multiply the stages together.
The floor of ten points gives even a severely reduced actor a small establishment allowance and keeps ratios defined.
It is a minimum allowance, never a maximum army size.
There is no national upper cap and no tag-specific coefficient.

The fixed coefficients establish one balancing scale.
Every country's result comes from its live inputs.
Population, geography, civilian industry, military industry, and infrastructure jointly represent national capacity.
Neither major-country status, score ranking, current division count, surrender progress, combat strength, conscription law, nor a temporary combat bonus is a capacity input.
These exclusions prevent circular allowance growth from the army itself.

## 4. Precision and arithmetic

Store F and A for decision purposes in integer quarter-points.
F_q equals four times the weighted total.
A_q equals the floor of four times the final positive allowance.
Compare those integers.
Show the exact same point values in player surfaces, with enough precision for .25, .50, and .75.
Equality in the display must mean equality in the release test.

Population inputs are divided into millions before accumulation.
Do not sum raw human counts into an overflow-prone variable.
Intermediate arithmetic must remain in the documented safe range for extreme population events.
A numeric overflow guard is an error condition to diagnose, not a covert maximum allowance.

Keep internal excess e as max(0, F/A minus 1).
It controls batch eligibility, inspection cadence, AI policy, and severity wording.
It is not a third persistent public meter.
The same unambiguous F and A supply every consumer.

Capacity is refreshed from authoritative live inputs on entry, repeats, local review, action commit, action completion, and relevant state changes.
Cached values are published atomically only when the full calculation completes.
A partly updated state sum may not release a country or authorize destructive action.

## 5. Calibration examples

These are invented numerical fixtures.
They are not claims about a historical country or an actual save.

| Fixture | P | T | C | M | Base allowance | Evolution IV allowance |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Small state | 0.3 | 1 | 1 | 0 | 16.50 | 10.00 |
| Minor with a modest industrial base | 3 | 4 | 4 | 2 | 55.00 | 30.25 |
| Regional industrial power | 15 | 12 | 20 | 15 | 244.00 | 134.00 |
| Large industrial power | 80 | 45 | 80 | 60 | 1040.00 | 572.00 |
| Former power after major losses | 5 | 6 | 8 | 6 | 101.00 | 55.50 |
| Expanded late-campaign power | 130 | 60 | 150 | 150 | 1980.00 | 1089.00 |

An ordinary formation with nine foot battalions and three basic support attachments consumes twelve points.
Eighteen foot battalions with three support attachments consume twenty-one.
Six medium-armored battalions, four motorized battalions, and three basic support attachments consume twenty-three.
Twenty-four autonomous robot battalions with three basic support attachments consume seventy-five.
None of these numbers depends on the formation's current manpower fulfillment.

Four formations with six ordinary battalions each and one formation with twenty-four consume the same twenty-four points.
The number of division icons has no separate term.

For the minor fixture, a force of sixty exceeds its base allowance of fifty-five.
Two additional civilian factories would raise the allowance to sixty-one if every other input stays unchanged.
A force of one hundred and twenty needs much more growth or a much larger reduction.
In an illustrative scenario that starts after day seven and then gains exactly one allowance point daily, those gaps close after five and sixty-five further days respectively.
The event itself does not create that growth.

## 6. Balance acceptance targets

The initial coefficient set must produce substantial differences between small countries, populated agrarian countries, industrial powers, and defeated remnants.
Large countries should not share a practical cap with minors.
Strong industrialization must be a plausible route to resolving moderate excess.
Major conquest should produce a visible but access-weighted capacity increase.

Base-level firing should release a large share of reasonably proportioned countries after the minimum week.
Long restrictions should concentrate on actual structural excess.
Evolution IV may keep enormous armies locked for very long periods, but should still permit a country with sufficient capacity to comply without forced destruction.

Calibrate with complete native saves covering early, middle, and late campaigns.
If these targets fail, adjust the central coefficients and profile weights together, preserve the monotonic relationships and positive fallback, and rerun the same scenarios.
Do not fix balance through national exception lists or hidden expiry timers.
