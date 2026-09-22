# 08 · Physical damage and casualties

## One actual result per physical operation

Every impact has a unique causal key, a selected state, a responsible actor and a provider. Every sub-pulse within an experiment has its own key. Resolve the affected targets and write the mutation-intent record before issuing the effect. A duplicate callback must see that key and return without applying damage or granting rewards again.

After the effect, capture its applied result. Reports, achievement counters, condemnation and Event 076 totals consume that result. They do not independently recalculate an intended percentage against a later population snapshot.

Distinguish requested damage, applied damage and an unverified mutation. A result is not verified merely because the effect was called. Where the engine cannot expose enough evidence to prove the result, mark the affected integration unresolved and keep it out of any claim of exact casualty accounting.

## Civilian population

The supplied dynamic-effects documentation defines `apply_exact_state_civilian_population_loss`. It is a state-scoped gateway with requested loss, technical minimum remaining population, reason, optional Deaths logging, target-country context and a one-shot contract input. Its result includes `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`.

Use that gateway for conventional civilian losses that have no existing owner transaction. Request the family profile's computed loss, use the owner's technical population floor, and record the returned actual applied amount. Do not reuse the example minimum population from the documentation as a special survivor guarantee for every minor.

The helper also deals with the engine's unintended recruitable-manpower credit when a negative state population effect is used. The inspected Deaths documentation notes that its same-effect observation can remain an engine-build risk. Recheck that behavior in installed vanilla and the current helper. A planning reference to the helper is not proof that this risk has been tested away.

Civilian deaths cannot be represented by a country-scope `add_manpower` penalty, a recruitable-population modifier or a text-only total. Actual state population must fall by the recorded amount. Civilian migration must remain distinct from death.

## Shared Deaths registration

When the population gateway performs Deaths registration, Event 076 must not call `chaos_meter_register_deaths` a second time. When an owning nuclear, chemical, biological or disease effect already registers the loss, consume that receipt and retain the owner as the mortality authority.

Add an Event 076 reason through the shared reason registry only after inspecting the current allocation. Do not guess a free numeric reason ID. Preserve the family or owner reason where the shared design requires it, and add the experiment identity as attribution without creating another death record.

The required default-enabled result is equality between Event 076's cumulative actual civilian losses and the sum of its attributed civilian transactions in the shared Deaths system. An original impact report uses the impact receipt. A later cumulative report includes new tail receipts once. These two report types must be clearly distinguished.

The inspected shared documentation says a disabled Deaths accounting setting can suppress ledger movement while physical loss still occurs. Event 076 must always submit or expose its real result through the owner contract and preserve its own physical receipt. It must not override the setting or claim numerical parity with a deliberately disabled ledger. Resolve the exact disabled-accounting contract with the shared owner before claiming coverage under every setting.

## Military deaths and equipment

Military personnel already serving in deployed formations are not a second civilian-population deduction. A unit adapter must identify units actually inside the affected area and measure its real personnel or strength loss. Equipment losses must come from those units' actual damage or destruction, not an unrelated national-stockpile penalty.

The shared Deaths mechanic already aggregates military casualties. A native effect whose losses enter that aggregation must not also be registered as a direct Event 076 military transaction. For an effect that does not enter the aggregate, use a verified direct-registration contract with explicit deduplication. The implementation must prove which route each unit-damage provider uses.

The same rule applies to naval crews and air-unit losses. Do not infer crew deaths from a count of destroyed ships or aircraft without an owner-supported casualty result. A formation that moved outside the impact footprint before execution remains unharmed by that local test.

This is a required implementation gate. A version that damages buildings and civilians while claiming unimplemented deployed-unit losses has not satisfied the brief.

## Buildings and supply

Use `damage_state_building_dynamic` where its documented type and amount inputs fit a state-level repairable building effect. It does not automatically select the correct targets, clamp all game limits or damage every provincial installation. Its documented provincial behavior is especially important for forts and naval bases.

Record repairs and destruction separately. A damaged level still exists and can be repaired. A destroyed level has been removed and must be rebuilt. Count neither as lost twice. Infrastructure, civilian factories, military factories, air bases, radar, anti-air, forts, ports and other relevant existing buildings are eligible through their appropriate providers.

Railway edges and supply infrastructure require explicit scope and native-effect verification. Do not assert a railway network was destroyed because infrastructure fell. An isolated supply hub, a damaged hub and a removed hub are different states of the world.

When a provider calls a combined helper that also changes state population, disable its optional mortality path or avoid the separate civilian gateway. In particular, a broad random-state damage helper with an optional population percentage cannot be combined blindly with a second exact-loss call.

## Continuing consequences

A continuing owner effect sends actual pulse receipts containing its instance, state, cause and applied loss. Event 076 records them once and updates the appropriate country and global experiment totals. If a new government controls the state, the physical effect follows the owner system's lifecycle. Responsibility does not disappear with the original victim tag.

Native bombing detection, global military aggregation, nuclear impacts, contamination pulses and disease outbreaks can all overlap. Establish an ownership table before implementation and test the overlaps deliberately. The same person cannot be counted once as a bomb victim and again as an unobserved estimate added by the reporting layer.

## Chaos accounting

Deaths-to-Chaos remains in the shared Deaths system. Nuclear use remains on the shared nuclear-use ladder. Wars and air contamination keep their existing contributions. Event 076 does not add those same values a second time.

Two proposed event-specific non-mortality milestones may add direct Chaos: plus 2 when the first coercive foreign-range program produces an actual completed test, and plus 5 when completed tests have established the program in three distinct continents. Both are once per campaign and require real completed impacts, not proposals or empty clicks. They represent institutional and international spread, separate from deaths or weapon use. The shared Chaos owner must approve their overlap treatment before implementation.

A verified international relief effort restoring the event-damaged access network in three affected countries may reduce direct Chaos by 2 once. This recognizes repaired infrastructure and renewed cooperation. It does not refund Chaos from deaths, cancel a nuclear use, or reset repeat-farming guards.
