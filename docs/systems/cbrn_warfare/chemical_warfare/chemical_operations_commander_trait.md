# Chemical Operations Commander Trait

## Current source contract

`chemical_operations_commander` is an assignable corps-commander trait with an additional service-earned route in `common/unit_leader/chaosx_traits.txt`. It is credited to the named leader after two qualifying, fully completed CBRN Headquarters operations, under `common/script_constants/cbrn_commander_progression_constants.txt` and the character-scoped effects and triggers in `common/scripted_effects/cbrn_commander_progression_effects.txt` and `common/scripted_triggers/cbrn_commander_progression_triggers.txt`. Decontamination Corridor is the qualifying chemical-operation code; two successfully supplied completions earn the service trait. The completion callback runs after the final successful paid upkeep while the operation and leader still match, then refreshes earned traits. A random new-leader or level-up roll is not part of this path.

The trait is the source for a native CBRN High Command advisor role at specialist, expert, or genius rank through `common/country_leader/cbrn_high_command_traits.txt`. Current source sets `gain_xp = { always = no }`, `trait_type = assignable_trait` and the historical 500-cost manual assignment value; manual assignment has no doctrine prerequisite. The Chemical Operations Academy spirit retains its +3% army experience gain and the historical trait-grant attempt when an army leader is created or levels up. The two systems can coexist without making academy selection a service substitute.

## Cylinder abilities and support bonuses

The trait unlocks all four `chemical_<agent>_attack` cylinder abilities through their historical `enable_ability` entries. Each ability also requires the trait, its gas technology, a corps commander outside border combat, and no other active cylinder barrage. Native CBRN raids and operation adapters remain a second delivery route. The trait gives the active consolidated Chemical Projector Battery +25% soft attack and breakthrough; the eighteen agent-specific tank companies remain inactive compatibility definitions under the consolidated unit design.
The native effect list displays the projector bonus, with the existing ability and preparation text appended.
Its national High Command ranks provide chemical/biological casualty and medical-saturation reductions and HQ preparation reductions of 20%, 30%, and 40%, bounded by the shared hazard-response and preparation floors.
Only the strongest appointed rank contributes to either operational multiplier.

The earlier historical candidate review considered Soviet, Japanese, Italian, Spanish, French, Canadian, British, German, and American commanders as research provenance. A search of current `history/countries/` found no `chemical_operations_commander` preassignment, so those names are not a current starting-roster claim. Any historically preassigned commander or new trait icon requires separate source and asset evidence before this guide can present it as active.

## Evidence limits and future depth

The source checks above establish definitions and callback wiring, not live-game award timing, advisor visibility, or player-facing presentation. The parent owns final integration and the user owns live consumer validation. Future expansion could add a distinct earned specialization only after its service trigger, effect budget, localisation, and visual consumer are approved.

## Restoration evidence

The ability bodies come from `726103283^`; the impossible target-receipt gate introduced in `726103283` and the inert replacements in `067d392c1` are absent.
Their AI blocks come from `81972d868^`, before the negative disable score; the trait selection block is the original `factor = 0.5` from `76bfc2885`.
Academy callbacks and manual assignment follow `309d1df5c`, with current earned-service and High Command role fields retained.
The original custom winged gas-mask art introduced in `c11750f18` is retained for chlorine and restored for phosgene, mustard and lewisite from before `cc5f0e876`; each DDS SHA-256 is `b4e635ee71851af0d8db20758f10fd109b14c1d93c1e73862a5091b9dc180d3d`.
The shared state modifier has independent legacy and modern readers so current raid cleanup does not erase a restored ability's timed contamination.
All twenty historical cylinder-production floor blocks, including the Japan bonuses and retaliation tiers, come from `726103283^`; their original enemy-Condemnation predicate is preserved under `chem_cylinders_enemy_has_used_chemical_weapons` so the newer confirmed-history predicate remains intact for newer routes.
The four ability icon consumers are `GFX_ability_chlorine_attack`, `GFX_ability_phosgene_attack`, `GFX_ability_mustard_attack` and `GFX_ability_lewisite_attack` in `interface/chaosx_ability.gfx`, pointing to the corresponding `gfx/interface/abilities/chemical_<agent>_attack.dds` files.
All four original textures decode at 34 by 33 pixels and were reviewed at native size; no sprite or texture path was repointed.
The five stock/requirement lines preserve their historical wording while formatting values of at least one thousand as lowercase `k`, including `48200` as `48.2k`, under the owner's explicit UI-number rule.
Independent AI source review confirms historical ability scores of 7.9/6.9/6.9/6.9 for the declared high-pressure Japan-China favourable-wind scenario and 6.3/5.3/5.3/5.3 for its adverse-wind counterpart; these are willingness scores, not selection probabilities.
The production-floor scenarios are Japan chlorine 2/3/4/5 factories and Germany phosgene or United States lewisite 1/2/3/4 as the strict enemy-Condemnation thresholds pass 2, 5 and 10; source floors do not prove actual factory allocation.
The historical academy roll is uniform from 0 to 100 with a threshold below 50; endpoint precision is undocumented, so its exact engine probability is not claimed.
The helper-closure review resolves 47 recovered helper bodies, 230 referenced constant leaves and 71 localisation keys, and the two state-modifier bodies match their respective preserved source bodies.
Twelve source scenarios check simultaneous effects and each expiry order; they are not game observations.
The file-mode `hoi4.script_validate` request timed out after 600 seconds and the ability probability inventory stalled, each on its sole relevant attempt; neither result is claimed as a passed check.
No useful correction justified retrying those unchanged requests, and a responsive service would be required for another attempt.
No requested ability, production stack, icon, localisation or AI branch is omitted, and no design fallback or retuning was applied.
