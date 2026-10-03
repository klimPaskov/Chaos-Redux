# Asteroid mineral-control API

This Event 028 owner API implements the accepted Extraordinary Minerals control rule: one main-crater contribution of `armor_factor = 1.00` and an uncapped fragment contribution of `0.20` per valid controlled fragment center.
It changes existing land-division armour multiplicatively through the army modifier, not flat armour, piercing, hardness, aircraft or naval values.
The source arithmetic and lifecycle cases are not combat-engine measurements.

## Entry point and inputs

Call `asteroid_incoming_refresh_mineral_control = yes` from any synchronized gameplay scope.
The legacy entry point delegates only to `asteroid_incoming_refresh_uncapped_mineral_control` in the owning TXT file.
It reads the persistent `asteroid_incoming_minerals_active` flag, the main-crater state target, the registered fragment-state array, actual state control, prior recipient countries and existing six presentation aliases.
No caller temporary input, output, parameter block or new periodic hook is needed.
An absent active flag grants no mineral bonus and removes existing owned bonuses on refresh.

```txt
# After accepted physical impact receipts, or a registered site's control change.
asteroid_incoming_refresh_mineral_control = yes
```

## Validity and recomputation

`asteroid_incoming_is_processed_mineral_fragment` is STATE-scoped and read-only.
It requires membership in `global.asteroid_incoming_fragment_site_states`, the fragment-site and mineral-site markers, an applied physical receipt, the actual fragment-center profile and absence of a main-crater marker.
It deliberately does not require ownership, population, cores, an overlord or ordinary impact-target eligibility.
The state iterator, not the potentially duplicated registry array, determines each unique contribution.

`asteroid_incoming_count_controlled_mineral_fragments` is COUNTRY-scoped.
It overwrites the normal `asteroid_incoming_country_controlled_fragment_count` from that predicate and actual controlled states, with zero when minerals are inactive.
The existing monthly achievement loop calls this same counter, replacing its weaker flag-only count without adding another world-country sweep or creating presentation scratch data.

`asteroid_incoming_recompute_mineral_country` is COUNTRY-scoped and belongs to the global refresher.
It uses the shared count, overwrites `asteroid_incoming_fragment_armour_bonus` as the count times `constant:asteroid_incoming_mineral.fragment_site_armour_factor`, maintains the one main idea and one fragment dynamic modifier, and publishes current recipient/scratch entries.
It is not a standalone public country refresh: the enclosing refresher owns clearing and rebuilding those arrays and the main-controller pointer.

## Outputs and side effects

Normal country variables retain the count and fragment factor across helper returns.
The existing main idea supplies the sole `1.00` main contribution to its actual current controller, including an occupier or subject.
The existing fragment-material-1 idea is a visible modifier-free marker, preserving the existing AI idea predicate without duplicating stats.
Retired fragment markers 2–6 carry no stats and are removed.
One `asteroid_incoming_fragment_crater_armour` dynamic modifier binds to the recipient's normal factor variable and is force-updated on a positive refresh.
Zero count removes the modifier and marker.
The bonus is overwritten rather than accumulated, and no six-slot cap is used for gameplay.

The enclosing refresher replaces the current recipient array and main/fragment controller targets, cleans dead prior recipients and migration-era aliases, then clears its typed fragment scratch array after publishing the six compatibility labels.
`asteroid_incoming_clear_dead_mineral_recipient` is COUNTRY-scoped cleanup: it zeroes count/factor and removes all owned main/fragment bonuses.
The annex callback invokes that cleanup explicitly on FROM after refresh even if the native existence transition has not yet completed; the name does not make `exists = no` an internal precondition.
The callback's actual native ordering and the later state-control refresh still require live evidence.

The state-control callback derives recipients from actual control, not the event ROOT or original target.
Annexation, civil-war completion, release as free/subject and peace-conference liberation have gated refresh hooks.
Owner changes that leave control unchanged leave the control-derived bonus unchanged.
No identity, state, unit, population, building, Deaths, Chaos, nuclear or diplomacy mutation is performed by this API.

## Icons and localisation

The main idea uses `GFX_idea_asteroid_incoming_main_crater_material`, backed by the existing 64×64 idea texture under `gfx/interface/ideas/028_asteroid_incoming/`.
The fragment marker and new dynamic modifier use `GFX_idea_asteroid_incoming_minerals`, backed by `asteroid_fragment_material.dds` in that same folder.
Both sprites are declared in `interface/028_asteroid_incoming.gfx`.
The new modifier's name/description are in `028_asteroid_incoming_mineral_dynamic_modifiers_l_english.yml`; the description exposes the current count and percentage.
The distinct 32×32 crater state icons are not substituted for either material idea.

## Evidence and remaining acceptance

The [mineral implementation handoff](../../docs/plans/028_asteroid_incoming_plans/subagent_handoffs/mineral_uncapped_20261003.md) retains exact before bytes, source-model cases, relevant wiki/installed sections, source revisions and native limitations.
The parent reread installed `every_controlled_state` at effects lines 3800–3818, `force_update_dynamic_modifier` at 4372–4381, the vanilla dynamic-modifier variable example at lines 1–28, `armor_factor` at modifier lines 1752–1755, and offline Modifiers lines 108–180.
Fresh MCP `reference_read` covered `add_dynamic_modifier`, effects lines 1153–1173, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and the offline on-annex/release contracts at On actions lines 244–287, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`.
The exact installed vanilla callback comments at `common/on_actions/00_on_actions.txt:1615–1617` and 5075–5085 corroborate winner/annexed and new/old/state scope identities.
Fresh source lookup found one unshadowed wrapper at runtime lines 1826–1828, revision `e4bc672fe557abe235c477f9f9c5b29f3d16f594c96aacb23779806f19182423`; its reference coverage was incomplete and is not a caller audit.
`hoi4.script_validate` is not exposed in this connection.
The returned event trace was partial with zero projected helpers; no helper-lifecycle or native armour acceptance is claimed from it.

Live land-armour values, zero-base divisions, piercing thresholds, subject/annex/release transitions, cached-stat refresh, tooltip rendering and MP/save behavior remain acceptance gates.
The fixed user-authorized `+100%` and `+20%` values must not be reduced or capped to resolve a balance concern.

## Future scope

No extra mineral stat or new strategic objective is implied by this API.
Any future scientific profile or rival-site expansion must retain the current-controller contract and be accepted separately from the uncapped armour calculation.
