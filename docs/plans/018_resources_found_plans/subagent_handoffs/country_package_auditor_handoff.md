# Event 018 DHO Country-Package Audit Handoff

Date: 2026-07-11  
Mode: patch-capable country-package audit; no commit  
Scope: the final live Oth-Kesh (`DHO`) country package, including creation, identity, locked brood forces, opening strength, resource-fed reinforcement, diplomacy, AI, defeat/world-end cleanup, and the country-facing asset surface  
Status: **static country-package acceptance repaired and passed; engine-execution acceptance remains unproven because Hearts of Iron IV was not launched**

## References followed

This pass used `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, and `chaos-redux-event-assets`. It read the complete Event 018 spec package, especially the country-package, brood-warfare, AI, tuning, and acceptance matrices; the implementation-depth addendum; the current cave-country documentation; and the completed focus-tree auditor handoff.

The audit also consulted the required offline wiki pages, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus, Unit modding, and Division modding. Official vanilla documentation and vanilla country, OOB, locked-template, AI-strategy, character, and portrait precedents were checked in parallel. No online Paradox wiki page was used.

## Files patched by this audit

- `history/units/DHO_1936.txt`
  - normalized all five template `priority` constants to the vanilla-supported 1-2 range while preserving named tuning constants;
  - retained all five locked, non-recruitable templates.
- `history/countries/DHO - Oth-Kesh Host.txt`
  - removed the root `set_oob = "DHO_1936"`; the live emergence setup now loads the OOB exactly once.
- `common/units/018_resources_found_cave_broods.txt`
  - corrected `maximum_speed` values to multipliers rather than mistaken absolute km/h values;
  - reconciled the final Scree value with the focus audit so every cave sub-unit remains slower than an ordinary 4 km/h foot unit after route bonuses.
- `common/scripted_effects/018_resources_found_cave_effects.txt`
  - disabled market access for DHO;
  - added one idempotent origin supply node at completed emergence transfer;
  - replaced the two-hour counterplay response with a named 14-day first-battle-analysis delay.
- `events/018_random_resource.txt`
  - made event `.83` set piercing or hostile-air observations only from the matching ordinary-country response choice;
  - kept the refusal option observation-neutral.
- `common/scripted_triggers/018_resources_found_achievement_triggers.txt`
  - removed the dead `resources_found_normal_training_completed` disqualifier from `No Men, No Guns`.
- `common/ai_strategy/018_resources_found_ai_strategy.txt`
  - added explicit ordinary-country desire and acceptance rejection for DHO military access.
- `localisation/english/018_resources_found_system_l_english.yml`
  - completed DHO democratic, fascist, communist, and neutrality-facing country/party localisation;
  - retained UTF-8 BOM after the edit.
- `docs/events/018_resources_found/cave_country.md`
  - aligned the single OOB load, origin supply node, market isolation, speed table, route-spirit lifecycle, and Vhorruk portrait surfaces with the live implementation.
- `docs/plans/018_resources_found_plans/subagent_handoffs/country_package_auditor_handoff.md`
  - records this final static audit and its unexercised engine gates.

Other Event 018 agents concurrently repaired the focus/idea lifecycle and landed the final focus/idea/state icon tranche. Those changes were re-read and rescanned in the final working tree rather than duplicated here.

## Static acceptance matrix

| Country-package surface | Static result | Evidence |
| --- | --- | --- |
| Reserved tag and country identity | Pass | `DHO` is unique in Chaos Redux, current vanilla, and the three approved reference mods; all ideology name/DEF/ADJ and party strings resolve. |
| Literal nonhuman sovereign | Pass | Vhorruk is recruited before politics; his source/runtime portrait depicts a rock creature rather than a costumed human. |
| Bespoke command staff | Pass | Three named commanders, three full portraits, and three small portraits are wired. |
| One-time country/OOB creation | Pass | Country history no longer sets an OOB; `resources_found_cave_setup_country` loads `DHO_1936` once behind the country-created guard. |
| Viable emergence origin | Pass statically | Completed transfer creates one supply node only when the origin has none; live supply propagation was not exercised. |
| Mandatory opening strength | Pass | `6 + floor(protected_strength_score / 5)`, score clamped to 0-120, yields 6-30 opening broods; the mandatory package resource floor is 720. |
| Five bespoke brood templates | Pass | War-Brood, Stone Phalanx, Burrow Column, Scree Pack, and Feeding Guard names match every `create_unit` consumer. |
| No manpower/equipment recruitment | Pass statically | All five sub-units use zero manpower and no equipment need; templates are locked with `force_allow_recruiting = no`; DHO has zero research slots, no market access, and no Event 018 stockpile-transfer path. Engine behavior was not exercised. |
| Resource-fed capacity | Pass statically | Non-origin capacity is `floor(total six strategic resources / 10)`, capped at 10; activation is 30 days, loss grace is 21 days, one paced automatic spawn is used, and excess divisions receive Unfed Broods. |
| Automatic neighbor wars | Pass statically | Controlled passable states scan neighboring passable states, resolve owner/controller, and guard existing-war/can-declare conditions; the recurring hook is `on_daily_DHO`, not a global country loop. |
| Focus package | Pass by formal focus audit | 65 focuses, complete graph/localisation/AI/rewards, exactly one hierarchy + one doctrine + one adaptation route spirit for all 18 completed combinations. |
| Diplomacy isolation | Pass for supported scripted surfaces | DHO cannot join/create factions, puppet, send volunteers, access the market, force governments, or issue cross-ideology guarantees; ordinary AI rejects alliance and military-access requests. |
| Cave and counterforce AI | Pass statically | Front requests, garrison behavior, objectives, hierarchy/doctrine routing, spawn choices, and ordinary anti-cave AT/CAS production strategies resolve. Live unit allocation was not exercised. |
| Regional/global defeat | Pass statically | Defeat requires zero controlled DHO states; cleanup removes cave anchors, footholds, denial sites, targets, arrays, and flags; regional and global outcomes remain distinct. |
| World-end gate | Pass statically | Exact origin-continent verification, Chaos strictly above 1000, a 60-day final gate, and a valid outside-continent foothold are all required. |
| Country-facing assets | Pass | Flags, portraits, focus sprites, idea/state sprites, and Vhorruk's Event Details animation all resolve to runtime files. |

## Brood balance and movement proof

`maximum_speed` is a multiplier on the ordinary unit baseline, not a literal speed. With the country-wide Slow Blood penalty applied to a 4 km/h foot baseline, the base packages are:

| Brood | Template priority | Armor | Hardness | Sub-unit speed modifier | Approx. base speed with Slow Blood |
| --- | ---: | ---: | ---: | ---: | ---: |
| War-Brood | 1 | 78 | 90% | -45% | 1.43 km/h |
| Stone Phalanx | 2 | 108 | 97% | -65% | 0.91 km/h |
| Burrow Column | 2 | 58 | 78% | -30% | 1.82 km/h |
| Scree Pack | 1 | 36 | 64% | -45% | 1.43 km/h |
| Feeding Guard | 2 | 92 | 94% | -75% | 0.65 km/h |

The focus audit additionally verified that the fastest completed Scree/Open package remains below the ordinary 4 km/h foot baseline, including the terminal World Below bonus.

The armor ladder preserves counterplay. Vanilla line anti-tank piercing is approximately 60 in 1936, 90 in 1940, and 125 at the later tier. War-Broods and Burrow Columns are reachable with concentrated early anti-tank, while Stone Phalanxes and Feeding Guards demand stronger or later piercing. Ordinary-country Event 018 strategies prioritize anti-tank and CAS, and the response ideas add hard attack/piercing instead of silently weakening the cave templates.

## Force-model proof

- Every cave sub-unit has `manpower = 0`, no `need` block, `active = no`, and the named long training-time constant.
- Every DHO template has `is_locked = yes` and `force_allow_recruiting = no`.
- The offline Division Modding reference states that a locked template cannot be created, deleted, or edited through the normal template surface and that `force_allow_recruiting = yes` is required to recruit a locked template. The DHO templates deliberately use `no`.
- `cave_resource_born_broods` removes recruitable population and ordinary AI division demand, while the country receives no research slots and no market access.
- A targeted live-code scan across Event 018 effects, on-actions, and events found no `transfer_navy`, `transfer_ship`, `create_ship`, `create_air`, `load_naval_oob`, `load_air_oob`, or `add_equipment_to_stockpile` effect.
- The removed `resources_found_normal_training_completed` key has no live-script reference. The older error-log handoff still mentions it as historical audit evidence; that documentation mention is not a runtime consumer.

## First-battle adaptation proof

The ordinary-country war-registration effect schedules `chaosx.nr18.83` after 14 days. Its immediate block only manages presentation state. The player response is the state source:

- anti-tank or heavy-gun choices set `cave_enemy_piercing_observed` on DHO;
- the air-power choice sets `cave_hostile_air_power_observed` on DHO;
- refusal sets neither observation.

The event trigger remains queue-based, so a short war does not strand the queue forever. This is a bounded campaign-response proxy, not combat telemetry; that limitation is reported below.

## Focus and icon reconciliation

The completed focus audit's earlier note that idea/state sprites were still pending is superseded by the current working tree:

- 65 unique live focus icon references resolve to 65 registered 94x86 DDS files;
- 20 national-idea picture references and 17 state/dynamic-modifier icon references collapse to 36 unique idea/state tokens;
- all 36 unique tokens resolve to registered 64x64 DDS files;
- the combined 101 live focus/idea/state references have no missing registration or missing texture file;
- all 101 corresponding DDS files have the expected dimensions and no duplicate SHA-256 asset hash.

The focus audit also repaired doctrine/adaptation swapping. Every completed hierarchy/doctrine/adaptation combination has exactly three focus-created route spirits: one hierarchy, one cumulative doctrine, and one cumulative adaptation spirit.

## Flag and portrait proof

- Six flag identities (`DHO`, four ideology variants, and `DHO_WORLD_BELOW`) exist in all three required sizes: 82x52, 41x26, and 10x7. All 18 are 32-bit TGA and have distinct hashes.
- Vhorruk's static country-leader portrait is 156x210 DDS.
- Khalvek, Orrukesh, and Thessik each have a 156x210 full portrait and 50x67 small portrait.
- Vhorruk's eight-frame Event Details sheet is 1248x210 DDS and is registered as `GFX_portrait_DHO_vhorruk_animated`.
- The character definition intentionally keeps `large = GFX_portrait_DHO_vhorruk`. The animated sprite is limited to the Event Details consumer, which already supports `frameAnimatedSpriteType`.

## Meaningful validation performed

- Reconciled the current 65-focus audit and verified the final 101/101 focus/idea/state sprite reference-to-registration-to-file chain after the icon tranche landed.
- Verified all flag and portrait dimensions, bit depth where applicable, and uniqueness hashes.
- Confirmed exactly one live OOB load path and no country-history OOB replay.
- Recomputed the opening-strength clamp/formula and anchor-capacity clamp/formula from their live constants and effects.
- Confirmed every spawn template string resolves to one of the five locked OOB templates.
- Confirmed the Event 018 scripted force path contains no navy, air, equipment-stockpile, or naval/air OOB creation-transfer effect.
- Confirmed the world-end and defeat helpers retain separate exact gates and cleanup paths after concurrent focus changes.
- Confirmed `DHO` does not collide with the current vanilla tag set or the approved reference mods.

## Simplifications, omissions, and blockers

1. **No engine run was performed.** Per task instruction, Hearts of Iron IV was not launched. Equipmentless `create_unit`, zero-manpower/no-need reinforcement, locked-template queue behavior, origin supply propagation, the 6-30 opening-spawn result, 30-day anchor activation, 21-day grace, one-at-a-time spawning, Unfed Broods, DHO front allocation, and regional/global/world-end cleanup remain statically proven but not engine-exercised. The supplied `error.log` contains only an initialization window and no Event 018 runtime trace; several audited files are newer than that log.
2. **Event `.83` is a proxy rather than combat telemetry.** The engine surface used here does not expose a supported generic combat on-action with the exact opposing-country equipment/response state this design needs. A 14-day war response and the actual option selected are used instead. This can delay the Stone or Sky observation focus gate when no ordinary participant selects that response; no synthetic observation or bypass was added.
3. **Vhorruk is not animated on the country-leader screen.** No vanilla-safe precedent was found for assigning a `frameAnimatedSpriteType` directly to a character's large portrait. The country character uses the static portrait, while Evolution IV's Event Details surface uses the real eight-frame animation. This surface split is deliberate and documented.
4. **Generic peace-conference naval/air behavior was not engine-exercised.** Event 018 itself has no scripted path that creates or transfers ships, aircraft, air OOBs, naval OOBs, or equipment stockpiles. The audit cannot prove how every generic engine peace-conference outcome behaves without a live run.
5. **AI allocation is statically configured, not observed.** Country-wide garrison priorities and dynamic origin/front requests use supported AI strategy surfaces, but actual interior-origin force allocation was not measured in a campaign.

No country route, brood type, focus route, commander, flag variant, resource-capacity step, AI strategy family, defeat outcome, or world-end requirement was omitted. Outside the explicitly reported first-battle proxy and character-screen animation limitation, no fallback or weaker substitute was introduced by this audit.

No commit was created.
