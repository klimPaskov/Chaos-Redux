# Current diplomatic targets

The Middle Volga trade delegation, Assyrian diaspora expert mission and Assyrian external-guarantee request retain their explicit foreign-country lists and existing reach rules.
Their native target declarations include dynamic countries with those original tags.
An ordinary listed static foreign country keeps its existing diplomatic eligibility, while a newly enumerated dynamic country must prove a current Event 006 registration.

## Identity and generation proof

The existing validated activation path publishes a country/generation row only after package setup is complete.
At that append point, `independence_wave_register_active_country` records the current package, native original tag and publication generation in `independence_wave_registered_package_id`, `independence_wave_registered_original_tag` and `independence_wave_registered_generation_id`.
First publication requires all three receipts to be absent, and a renewed publication requires the current validated generation to exceed the recorded generation.
A same-generation registration or missing-cache-row repair leaves the original tuple untouched.
Partial receipt loss fails closed; it does not authorize restamping from mutable fields.
A validated new generation publishes its own tuple with its new row.
The country pointer, original tag, package and generation therefore remain bound to that publication's source identity.
This is a provenance receipt from the validated writer, not an independent reconstruction of the package/template matrix or authentication of forged console state.

The dynamic target branch requires active Event 006 origin, completed setup, current force generation and all three receipts matching the live fields.
Its stored anchor must still be owned and controlled by the target country.
Native `any_of` reads the aligned active-country and generation arrays at the same index and requires the exact target pointer and current generation.
There is no requirement that the former host remain alive or that the anchor still be the capital.
Event 021 dynamic countries, unregistered civil-war peers, ended origins and stale or divergent registrations do not satisfy this branch.

## Predicate API

`is_independence_wave_current_diplomatic_target` runs in the actual target's COUNTRY scope, entered as `FROM` by each targeted decision.
It takes no caller-supplied temporary inputs and returns only the native trigger boolean.
Its private `independence_wave_diplomatic_registry_country` and `independence_wave_diplomatic_registry_index` temporaries are initialized before indexed iteration and are not outputs.
Missing variables, receipts, aligned rows or anchor control make the registered branch false.
The ordinary branch requires a static country outside the existing Event 006 custom-template classifier, and does not impose Event 006 registration on normal foreign partners.
The predicate has no persistent side effects, payments, grants, flag writes, event targets or world sweep.
Only the existing validated registration effect writes the two normal identity receipts.

Usage inside an existing targeted decision:

```text
targets_dynamic = yes
target_trigger = {
	FROM = {
		hidden_trigger = { is_independence_wave_current_diplomatic_target = yes }
		is_independence_wave_iw043_reachable_partner = yes
	}
}
```

The hidden proof does not add implementation identifiers to the player-visible requirements.
The existing target list, actor gates, reach, peace, subordination, affordability, payment, cooldown and AI factors remain the action's contract.

## Presentation and evidence

The three decisions reuse `GFX_decision_independence_wave_iw043_diplomacy` and `GFX_decision_independence_wave_iw058_diplomacy` through their existing definitions.
No new icon, asset, localisation wording or category is required by this identity guard.
The accepted plan and exact reference boundaries are in [the D34 contract](../../../plans/006_independence_wave_plans/d34_dynamic_target_binding_contract_20261008.md).
The assigned [probability audit](../../../plans/006_independence_wave_plans/subagent_handoffs/d34_dynamic_pool_probability_20261008.md) retains source hashes, named synthetic scenarios, score-only semantics and unresolved target-scope/internal-error findings.
Source checks and read-only models do not establish native enumeration, variable lifetime, costs or campaign selection probabilities.
The full Event 006 goal remains active and incomplete.

## Future work

Complete the same-scenario AI comparison and native consumer evidence without weakening the current identity or generation proof.
Other diplomatic consumers may reuse this predicate after their own target-list and origin requirements are reviewed; this change does not silently widen them.
