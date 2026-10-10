# 03. The worldwide opening and territorial allocation

## One global opening

Every valid ordinary country participates in one frozen opening snapshot. The snapshot precedes territorial, political, military, and stock changes. Each country receives its own proportional nomination, then all nominations are combined into one physical state plan. A state, unit, leader, or stockpile cannot be transferred twice because it appeared in several countries' records.

The snapshot records owner and controller relationships, communist popularity, eligible states, 001 state levels and rebel lineage, existing wars and factions, current leadership, military sources, industry, population, and logistics. The committed episode additionally records the actual successful firing date and month. Later choices consume this opening record. They do not reroll it using a changed popularity or a newly occupied map.

## Eligibility of states and countries

An ordinary participant is an existing non-special country with relevant physical ownership or control. Its pool is the deduplicated union of eligible owned states, controlled states, and associated 001 rebel-held states with valid provenance. A state appears once within each country's pool, even if it is both owned and controlled by that country.

An eligible state is valid, transferable under the relevant native and cross-event contract, and useful as actual territory. Impassable states and states held by incompatible special actors are not silently confiscated through an ordinary-country selector. Inhabited states are favored over wasteland, and available industry, victory points, supply, ports, and airfields matter to additional selection. A valid inherited base is preserved even when its current condition is poor.

The implementation must distinguish an excluded state from a state that is eligible but receives a low selection weight. Excluding a strategically inconvenient or well-defended capital merely to protect a country from collapse is not allowed. Capital states can be selected. A one-state country can lose its only eligible state. The old 001 minimum-country-size rule does not apply as a protective cap to 091.

An active 001 rebel is handled through its lineage and political disposition. It does not receive an additional ordinary-country popularity roll on top of the original host's associated pool. Its real territory remains in the opening history, and its continued country existence depends on its actual alignment choice.

## Proportional nomination

For each country, let N be its frozen eligible pool size and p its communist popularity in percent. Compute:

`raw target = N × p / 100`

Take the whole part, then add one state with probability equal to the fractional remainder. Draw that fractional result once and store it. There is no fixed minimum or maximum beyond the size of the pool.

All established 001 states count first, including correctly associated rebel-held territory. If G is the number of those guaranteed inherited states, select only `max(0, rounded target - G)` additional states. If G exceeds the target, keep all G and add zero. Established history is the explicit exception to the nominal target, as required by the brief.

| Example | Calculation | Result |
| --- | --- | --- |
| N = 10, p = 30 percent, G = 1 | Raw target 3, additional shortfall 2 | Three nominated states, including the inherited one |
| N = 7, p = 20 percent, G = 0 | Raw target 1.4 | One state with 60 percent rounding chance or two with 40 percent |
| N = 3, p = 10 percent, G = 0 | Raw target 0.3 | Zero states with 70 percent chance or one with 30 percent |
| N = 4, p = 25 percent, G = 3 | Target 1, inherited count 3 | Keep all three inherited states and add none |
| N = 1, p = 100 percent, G = 0 | Target 1 | The country can lose its sole state if its political disposition transfers it |
| N = 20, p = 0 percent, G = 2 | Target 0, inherited count 2 | Preserve both established bases |

These are arithmetic illustrations of the specified rounding rule. They are not outputs of the HOI4 probability tools or a balance simulation.

## Weighted selection and coherent fronts

After inherited states are selected, additional nominations use selection without replacement. Prefer states next to existing nominated bases, then states that can connect important bases, industrial and populous states, supply and transport hubs, and vulnerable occupied or war-weary regions. Ritual sites, strike history, local communist pressure, weak government, and a justified origin-region connection raise priority.

Coherence is a preference rather than a rule that deletes isolated uprisings. A distant shipyard, mining region, or colonial port can become an independent front. The force allocator gives such a front an appropriate finite package and a real supply problem. It does not create a free global teleport network to make every selected state equally useful.

Only the current country's own sealed selection context affects its nomination weights. Country A being processed first cannot make Country B's states more likely to be selected. The physical union is built after all local nominations are sealed, which removes country-order advantage and makes retries reproducible.

### Concrete selection weights

The initial implementation proposal uses a strictly positive additive weight. These numbers establish an auditable starting model, with balance acceptance reserved for the native probability review. For each remaining eligible state, calculate `w = 1 + 4A + 3B + 2P + 2F + 2L + V + 2R + S + C + H + W + O`. Every input is frozen before selection except A and B, which depend only on this country's own already selected states.

| Input | Exact meaning and range |
| --- | --- |
| A | One if the state has a land adjacency to an already selected local state, otherwise zero. Adjacency to another country's nomination gives no credit |
| B | One if adding the state joins two otherwise disconnected components of this country's currently selected land-adjacency graph, otherwise zero. This can coexist with A |
| P | State population divided by the largest state population in this country's frozen pool. Use zero if that maximum is zero |
| F | Actual fixed civilian and military factories in the state divided by the largest such count in this country's pool. Use zero if the maximum is zero. Do not count damaged factories twice or add country-wide totals |
| L | The sum of three binary flags divided by three: usable port, usable supply hub with a real railway connection, and usable airfield |
| V | State victory-point total divided by the maximum state victory-point total in the pool, or zero when that maximum is zero |
| R | One for a recorded active prepared ritual or underground arsenal, one half for a recorded surviving but disrupted preparation, otherwise zero. Existing guaranteed 001 bases have already been removed from this candidate set |
| S | One for recorded local strike or revolt history associated with the current 001 crisis, otherwise zero. Unrecorded history gives no invented bonus |
| C | Communist popularity of the frozen physical controller divided by 100. This is country popularity, not a fabricated state ideology statistic. Use the legal owner only when a valid physical controller does not exist |
| H | One minus the frozen controller's stability divided by 100, clamped to zero through one |
| W | The frozen controller's surrender progress, clamped to zero through one. Use zero when that country is not in a relevant war |
| O | One when the frozen native rights show foreign military occupation with different legal owner and physical controller, otherwise zero. This uses actual pre-opening occupation, independent of either government's later response |

All normalized inputs lie in zero through one, so weights lie in one through twenty-two. An absent optional historical marker gives zero for that marker. A missing required population, country, state, or rights input is a disclosed feasibility problem, not an invented zero. No state is made ineligible merely by receiving the minimum weight.

For each required additional nomination, sort remaining states by stable state identity, recompute A and B, sum the positive weights, and select the first cumulative interval containing a stored draw in `[0, total weight)`. Intervals are left-inclusive and right-exclusive. Remove the selected state, append its identity and actual draw to the proposal, and repeat until the exact shortfall is filled. Fractional quota rounding uses its own independent stored draw before these draws. The installed engine's random resolution and numeric limits must be inspected and any quantization documented before this model is translated to script.

This is sequential weighted selection without replacement. It is not a one-pass set of independent Bernoulli tests, and it is not a weighted ordering shared across countries. Resume a bounded continuation from the exact remaining set and local graph. A retry with the same proposal must consume the saved results rather than regenerate them.

## Occupation overlap: explicit interpretation

Owned-or-controlled pools necessarily overlap. A selected occupied state can affect both its legal owner and its current controller. The accepted design preserves every country's independent nomination target and records the resulting physical effects separately.

For example, A owns ten states and has 10 percent communist support. B occupies two of A's states and has 100 percent support. A nominates one state. B nominates both occupied states. The final union can affect two or three A-owned states, even though A's own nomination was one.

The additional loss is an occupation-overlap effect from B's revolution. It is disclosed in the opening record and report. It is not a second roll against A, and it does not grant extra forces for the same physical state. Converting the pools to owner-only territory would violate the requested owned-or-controlled rule. Reserving each state for the first country processed would introduce order bias and underfill later countries. The independent nomination and union policy is the accepted resolution.

## Origin selection

Choose one valid origin in this order:

1. A selected Level 3 Communist Lockdown.
2. A selected Level 2 Insurgent Stronghold.
3. A selected Level 1 Agitation Zone.
4. A selected active 001 rebel base with valid physical and political handoff.
5. A selected inhabited industrial state in the strongest eligible communist-pressure country that can supply a viable origin. For this fallback class, eligibility requires positive frozen population and at least one actual fixed civilian or military factory. Greater population and industry raise its weight, with no extra arbitrary population minimum. A damaged but existing factory is recorded as damaged and still requires a viable repair and supply plan.

Within the highest valid class, weigh population, industry, victory points, supply, ports or air access, communist pressure, preparation, host strength, current war, adjacency, and the ability to sustain a country. Petrograd or Leningrad is a historical preference only when the actual state exists, is valid, and fits the connected crisis. Its legacy state ID is not a universal hardcoded requirement.

Origin ranking first applies the class order above as a hard precedence rule. Within the surviving highest class, use a separate stored weighted draw with `origin weight = 1 + 3P + 3F + 2L + 2V + 2C + 2R + H + W + 2A + K`. P, F and V are normalized over that origin class, A means adjacency to another state in the sealed physical union, and the other inputs retain the definitions above. K is one only for a source-verified Petrograd or Leningrad state connected to this actual 001 crisis, otherwise zero. A sovereign origin must also pass country, capital, actual supply and force-creation feasibility. If a candidate fails a concrete feasibility check, retain the reason, remove it from the viable class, and continue through the same saved proposal, advancing to the next class only when the higher class has no viable candidate. Within each remaining origin class, use the same stable state-identity order, positive-weight sum, left-inclusive and right-exclusive cumulative intervals in `[0, total weight)`, and sum/select/remove procedure defined for additional-state selection. Every attempted candidate consumes its own independently saved origin draw from the remaining class. The earlier draw is never remapped to a reduced pool, and a retry reuses the saved attempted identities and outcomes. For the fallback class, strongest communist pressure means highest frozen communist popularity among countries with viable nominated populous industrial states, with equal popularity resolved by greater eligible population, then greater actual industry, then stable country identity. The strength of its former host is represented by H and W, with a weak or stressed host making the origin more likely, while real viability remains a hard gate.

The origin must belong to the frozen inherited or nominated state set. The design does not add an extra origin state when every proportional result is zero. That would introduce the fixed minimum the user prohibited.

If no viable origin survives preflight, 091 does not actually fire. No country or army is created, no fire-once history is consumed, no Chaos is added, and stored weight is retained. The selector excludes that failed proposal for the current selection cycle. Its random results remain tied to the proposal until a meaningful relevant world-state change, so a reload, popup, retry, or UI refresh cannot fish for a new map. This is a rare failed preflight, with the valid-origin gate honestly enforced. It is not a completed opening without Lenin.

## Country creation and first forces

Activate one audited World Revolution identity, create sovereign ownership and control of the origin, establish a dynamic capital there, and attach the single authoritative Lenin identity. Complete laws, initial administration, compatible technology, real stocks, templates, command structure, and the finite seed host through the accepted country contract.

The seed host guarantees that a successfully committed opening reveals the promised nonhuman army. The rest of the force plan is sourced from inherited formations, prepared bases, actual defection, local recruitment or conversion, and finite equipment. A technical failure to instantiate the actor or origin must be detected before the irreversible opening commit.

The origin is sovereign World Revolution territory even if its former government joins. This exception concerns the disposition of a selected state, not adding a state beyond the nomination. The origin owner is told clearly that joining does not return the revolution's capital.

## Diplomatic disposition

Noncommunist ordinary governments enter the central war immediately, including those with zero territory selected. Existing defensive alliances and wars remain meaningful. The event does not force the world into one anti-Lenin faction or dissolve unrelated wars just to simplify its diplomacy.

Communist governments choose joining or refusal. Stalin as current Soviet leader takes the required refusal immediately. Trotsky as current Soviet leader joins immediately as an autonomous cofounder. Ordinary choices use a bounded native response with refusal as the non-consenting default. Their selected non-origin bases remain under guarded provisional administration until the request resolves. The initial Lenin reveal and noncommunist wars do not wait for every communist player.

| Current rights before the opening | Final selected-state disposition after responses |
| --- | --- |
| Joined government owns and controls | Retain ownership and control as an allied local base |
| Enemy or refuser owns and controls | Transfer to World Revolution |
| Joined owner, hostile occupier | Joined government retains legal ownership, revolutionary forces take hostile control under the verified split-rights contract |
| Enemy owner, joined controller | World Revolution receives the hostile ownership claim, joined government retains local control where native semantics support it |
| Two joined governments hold different rights | Preserve the existing owner and controller relationship and register one allied base |
| Two hostile governments hold different rights | One World Revolution state transaction, with both displacement histories recorded |
| Either communist response is still pending | Apply only the rights already authorized when native semantics permit, otherwise keep a guarded provisional state of the unresolved rights, and revalidate at resolution |
| A valid special actor already controls the state | Preserve the special-actor exclusion and record an unresolved contested claim unless the exact cross-event capture contract permits mutation |
| Sovereign origin | World Revolution receives ownership and control once |

Split ownership and control is a required technical feasibility check. Two sequential whole-state transfers are not proof that the intended rights survive. If the native contract cannot support a listed disposition, the implementation must show the limitation and propose a specific preserving solution before claiming the opening complete.

## Existing rebels

An 001 rebel can join the international as an independent government, accept a subordinate arrangement, voluntarily merge, or reject Lenin and fight as a human communist movement. Current leadership, ideology, prior host relations, patronage, state history, Stalin or Trotsky alignment, and player control shape that decision.

Guaranteed inheritance means the established state and its history are preserved in the opening plan. It does not erase a real rebel polity's explicit refusal. A refusing rebel's non-origin base receives the recorded disposition that an established revolutionary region denied Lenin access. The state is not rolled away and replaced elsewhere. Its human army remains an actual opponent. The sovereign origin still transfers under the global origin exception, with the same possibility of real collapse or exile if it was the rebel's last state.

Absorption transfers real units, commanders, equipment, and stocks through measured native contracts. Joining retains local assets and uses actual expeditionary, volunteer, aid, or command relationships. A country with surviving meaningful content keeps that content unless a specific accepted route changes it.

## Full collapse and player control

No hidden one-state remainder protects an ordinary government. A full loss uses actual native collapse, capitulation, exile, release, or player-continuation rules. An exile is available only when the game's legitimate framework creates it. The event must not invent a phantom government with invisible land solely to avoid a difficult result.

The optional World Revolution switch belongs by default to the human country that controlled the physical origin at the snapshot, with its legal owner disclosed when different. This is the explicit occupation interpretation of origin-owner play. Only one player can receive that default offer. The current player and country authority are revalidated before switching, and the switch is the last country-scoped action so subsequent effects do not run on the wrong player country.

## Later changes are targeted

New countries, changes of government, subject releases, ordinary occupations, and fresh 001 cells after the opening receive their own bounded role updates. They do not trigger another worldwide nomination. Capturing a state does not repeat its original muster. A newly communist government at war can negotiate through a guarded later alignment route, but it cannot retroactively retain states already lost in the opening without a real peace or transfer outcome.

### Acceptance

Review exact-integer and fractional quotas, inherited excess, zero target, one-state collapse, overlapping occupation, two joining claimants, a refusing rebel, missing legacy lineage, no viable origin, a month boundary, multiple human players, and duplicate callback delivery. The opening passes only when the stored plan explains the actual map, troops, diplomacy, and history without a reroll or duplicate asset.
