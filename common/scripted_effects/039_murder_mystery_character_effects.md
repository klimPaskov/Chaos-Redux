# Event 039 character helpers

## `murder_mystery_capture_current_ruling_character`

Purpose: resolve the sitting leader without selecting an opposition party leader.
Scope: the recipient COUNTRY, which may differ from event ROOT.
Inputs: an existing country, a native current-ruling-leader proof from the owning adapter, and `murder_mystery_ruling_selection_authorized` set immediately after that proof.
Defaults: missing leader, stale anchor, ambiguous roster, or absent target returns without success.
Outputs: country flag `murder_mystery_ruling_character_resolved` and regular event target `murder_mystery_current_ruling_character` after exactly one roster match.
Side effects: a modifier-free native country-leader trait is added and removed synchronously before the helper returns.
The helper neither retires characters nor changes politics, portraits, country ownership, or gameplay modifiers.
It consumes the authorization flag on return, including failure.
Callers establish the proof through a native `has_country_leader` query for their verified static identity or generated package name.
The success flag is cleared at entry and callers must test it before consuming the target, because regular event targets cannot be manually cleared.
The target lives only for its effect chain and any events queued from that chain.

```text
if = {
	limit = { has_country_leader = { name = MURDER_MYSTERY_FIRST_KNIFE_NAME ruling_only = yes } }
	set_country_flag = murder_mystery_ruling_selection_authorized
	murder_mystery_capture_current_ruling_character = yes
}
if = {
	limit = { has_country_flag = murder_mystery_ruling_character_resolved }
	event_target:murder_mystery_current_ruling_character = {
		save_global_event_target_as = murder_mystery_first_knife_character
	}
}
```

The country-scoped `add_country_leader_trait` and `remove_country_leader_trait` effects explicitly operate on the country's sitting leader in installed effect documentation lines 1008-1021 and 5946-5959.
Their offline-wiki COUNTRY entries are at Effects lines 2940-2941.
`every_character`, `has_trait`, and character event-target identity retain their documented scopes.
Vanilla Germany's focus source at lines 8090-8103 demonstrates dynamic `is_character = PREV.PREV` identity.
Approved Kaiserreich Fengtian events at lines 6829-6872 demonstrate `is_character = event_target:leaker`.
These are source precedents, not observed Event 039 runtime acceptance.

## `murder_mystery_register_candidate_founder`

Purpose: register the exact created founder after the reserved territory has transferred to the candidate.
Scope: candidate COUNTRY with owned land and the native ruling First Knife name.
Inputs: the current country-creation transaction generation and pre-created leader package.
Outputs: `murder_mystery_first_knife_registered`, the exact global character pointer, and country-local founder generation after safe-target registration succeeds.
Defaults: missing country, leader, unique ruler proof or registry capacity leaves the receipt false.
Side effects: applies the founder character flag to the resolved ruler and creates one owned safe-target row.
It does not transfer land, retire characters, recruit history-only characters, grant units, or commit the country transaction.
The country commit checks both this receipt and current roster membership before publishing the country or its war.
Registering after territory transfer avoids treating a landless carrier as an existing country.
Before transfer, `murder_mystery_assassin_candidate_is_reserved` checks the allocated country target, AXS origin, candidate flag and mirrored allocation generation.
Both the commit wrapper and transaction begin use that reservation proof instead of a pre-transfer COUNTRY-existence requirement.
The capital is assigned after reserved land transfers and before the post-transfer founder and capital postconditions.
This allocation proof does not certify the complete industry, population, supply, force or rollback package.

```text
event_target:murder_mystery_assassin_state_candidate = {
	murder_mystery_register_candidate_founder = yes
}
```

## `murder_mystery_install_movement_successor`

Purpose: install the existing route-compatible successor package before registered founder removal.
Scope: the recorded Assassin State COUNTRY.
Inputs: current route flags and the neutrality government.
Outputs: country-local `murder_mystery_capture_successor_verified` after a native ruling-leader check.
Side effects: creates or reuses the existing route successor role, name, description, and portrait.
It does not retire a character or resolve the country or network.
Missing or incompatible country state returns without success.

```text
event_target:murder_mystery_assassin_state = {
	murder_mystery_install_movement_successor = yes
}
```

The capture transaction remains responsible for exact target identity, registry generation, unused disposition, protection, current recruitment, removal, and persistent receipts.
The static character definitions are not treated as recruited historical objects merely because their tokens exist in `common/characters/`.

## `murder_mystery_apply_live_central_capture_shock`

Purpose: apply the bounded organizational loss from founder capture without resolving a surviving central country.
Scope: COUNTRY investigation actor.
Inputs: committed global core capture and the recorded current central country.
Outputs: actor-local `murder_mystery_live_central_after_capture` when an existing registered Assassin State still owns land.
Side effects: clears the actor's permanent-resolution readiness and applies a once-only Cohesion and Reach shock to the central country.
The shock uses current public values, ratios, floors and ceilings from `common/script_constants/039_murder_mystery_character_constants.txt`.
The helper preserves countries, armies, routes, equipment, foreign cell and derivative registries, runtime activity and the inheritance allowance.
It adds no Chaos and performs no world scan.
Country existence plus owned land is a conservative continuation guard, not certification of the country's complete population, industry, supply or force postconditions.
An absent or structurally uncertain country does not establish permanent resolution and must pass the separate inheritance or global-dismantling proof.

```text
if = {
	limit = { has_country_flag = murder_mystery_core_offender_captured }
	murder_mystery_apply_live_central_capture_shock = yes
}
```
