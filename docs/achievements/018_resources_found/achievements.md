# Event 018 Resources Found Achievements

Event 018 defines 15 custom achievements. Each uses a recorded gameplay predicate and the same stable identifier across `common/achievements/chaos_redux_achievements.txt`, `common/scripted_triggers/018_resources_found_achievement_triggers.txt`, localisation, GFX registration, and the three-state icon package. None unlock merely because Event 018 fired.

## Ordinary field achievements

### One Vein, One Market

Identifier: `018_resources_found_one_vein_market`.

Develop one persistent field until at least 400 units of one standard strategic resource have been added by Event 018. This reads the six exact field ledgers rather than total state resources.

### Everything Under One Hill

Identifier: `018_resources_found_all_resources_one_state`.

Retain a positive Event 018 addition of oil, aluminium, rubber, tungsten, steel, and chromium in one persistent field at the same time.

### Every Worker Home

Identifier: `018_resources_found_every_worker_home`.

Complete a full seal on a substantially developed field with no recorded field deaths, concealed casualties, or coercive-labor choice. Exact seal completion and the safety disqualifiers must belong to the same field record.

### The Deep Door Holds

Identifier: `018_resources_found_full_seal_evolution_three`.

After an Evolution III public attack, finish the full sealing operation, remove all six Event 018 resource ledgers exactly, and permanently prevent Evolution IV in that field.

### Contract of the Century

Identifier: `018_resources_found_contract_of_century`.

Complete a full long-term export review while the exact field remains at Industrial Developed Yield, Workforce Safety remains Managed or Protected, and Foreign Pressure never reaches Crisis. The stored owner must remain sovereign and retain ownership and control throughout; suspension, occupation, public breach, border war, contract invalidation, or threshold failure permanently disqualifies that review cycle. The field-local owner, partner, qualification flag, and immutable mission pointers are authoritative.

### No Claims Left Unsettled

Identifier: `018_resources_found_resolve_field_dispute`.

First take a valid claimant dispute to Crisis Foreign Pressure and at least armed-patrol or frontier-mission stage. Then retain the exact field and keep compensation, arbitration, an international commission, or a demilitarized agreement functioning with the same living claimant for 180 days. Border war, transfer, occupation, subject status, suspension, closure, public breach, renewed confrontation, claimant annexation, or commission collapse cancels the immutable settlement clock.

## Former-owner and anti-cave achievements

### Thirty From Below

Identifier: `018_resources_found_thirty_from_below`.

As the field's legal owner or physical controller at breach, face an Oth-Kesh emergence at the 30-division cap, remain independent and uncapitulated, and retain the recorded starting capital. Both roles are snapshotted before transfer; the opening division count is frozen before either candidate is recorded.

### The Last Shaft Closed

Identifier: `018_resources_found_last_shaft_closed`.

Personally recapture and clean at least three historically mature, non-origin Oth-Kesh anchors, then see every remaining chamber cleared and the regional threat end before it becomes global. Activation marks anchor maturity; cleanup credits each qualifying state once. The origin chamber, World-End footholds, generic restoration sites, and repeated work on one state cannot satisfy the three-anchor ledger.

### The Ground Is Quiet Again

Identifier: `018_resources_found_ground_quiet_again`.

After Event 018 World End and its super-event have historically fired, participate as an ordinary country in the global cave war, make a major anti-cave contribution, survive global defeat, clear every surviving chamber and Oth-Kesh territory, and finish the country's reconstruction obligation. The near-global 365-day aftermath classifier alone is insufficient for this achievement.

## Playable Oth-Kesh achievements

### Ten From One State

Identifier: `018_resources_found_ten_from_one_state`.

As DHO, continuously control a non-origin state with at least 100 total strategic resources until its anchor activates at the 10-division state capacity cap, then let the normal non-World-End spawn queue create a brood from that exact anchor. The state and country completion flags are set only by that spawn; opening divisions or a different anchor cannot satisfy the predicate.

### No Men, No Guns

Identifier: `018_resources_found_no_men_no_guns`.

Maintain at least 25 active cave divisions and four active non-origin anchors. The qualifying formations use zero ordinary manpower, no equipment definition, locked templates, and automatic anchor spawning.

### The Mountain That Moves

Identifier: `018_resources_found_moving_mountain`.

Complete the Stone Phalanx capstone, then defeat a major country that had anti-cave armor preparations before the qualifying war without losing the cave origin. Preparation is snapshotted when the cave war begins. Only the named capstone records route completion; an ordinary Phalanx Assault project cannot substitute for it.

### The Front Has a Floor

Identifier: `018_resources_found_front_has_a_floor`.

Complete the Burrow War capstone, prepare an approach from an active nondisrupted anchor, and capture the exact defended capital, supply hub, or level-3 fortified objective during its 90-day mission. The state, defender-at-start fact, stored pointer, mission, and pre-World-End state must all agree at the control-change hook; timeout, cancellation, defeat, retargeting, and World End clear the live evidence. The approach project records the operation, but only the named capstone records route completion.

### When the Hills Begin to Move

Identifier: `018_resources_found_hills_begin_to_move`.

Complete The Hills Begin to Move, the Scree Tide capstone, and sustain at least three deployed Oth-Kesh Scree Pack formations within legal brood capacity. Only then can Release Raiding Broods open a 180-day qualifying surge. Capture five different states and defeat two different countries inside that one ledger while at least three Scree Packs and legal capacity still exist; success is latched at the final qualifying control change or capitulation. Per-attempt state and country marks prevent recaptures or repeated capitulations from inflating either threshold.

### Continental Appetite

Identifier: `018_resources_found_continental_appetite`.

As the playable Oth-Kesh Host, verify ownership and control of every eligible origin-continent state and complete the continental objective before terminal transformation.

## Tracking and disqualifiers

The achievement effects record evidence at the action source:

- field record creation, exact resource ledger changes, safety and exploitation choices;
- contract activation, breach, settlement, border-war history, and commission settlement;
- Evolution III public breach and exact full seal;
- pre-transfer cave opening strength, former owner, and former capital;
- anchor activation, capacity, loss, recapture, cleanup, and state contribution;
- doctrine completion, prepared-war snapshots, marked objectives, surge state/country counters, origin loss, continent verification, and world-end timing;
- regional or global scale, cave defeat, reconstruction, and contributor status.

Disqualifiers include hidden casualties, coercive labor, contract breach, border-war resolution where negotiation is required, origin loss in a qualifying doctrine war, incomplete reconstruction, and the wrong player role. The generic custom-achievement availability rules continue to govern game mode and mod settings.

## Icon wiring

Every achievement has three separate 64 by 64 runtime files under `gfx/achievements/`:

- `<achievement_id>.dds` for completion;
- `<achievement_id>_grey.dds` for incomplete eligibility;
- `<achievement_id>_not_eligible.dds` for unavailable status.

The icon set is registered in `interface/chaosx_achievements.gfx`. Source prompts, type-specific masters, processed PNGs, overlays, contact sheets, dimensions, and final paths were produced in the deleted temporary evidence workspace; their durable source-to-runtime conclusions are recorded in `docs/events/018_resources_found/assets.md`, `docs/plans/018_resources_found_plans/subagent_handoffs/achievement_icon_handoff.md`, and `docs/plans/018_resources_found_plans/subagent_handoffs/asset_audio_reaudit_handoff.md`.

## Implementation surfaces

- definitions: `common/achievements/chaos_redux_achievements.txt`;
- predicates: `common/scripted_triggers/018_resources_found_achievement_triggers.txt`;
- evidence writes: `common/scripted_effects/018_resources_found_achievement_effects.txt` and the field, decision, event, cave, focus, and on-action call sites;
- names, descriptions, and requirement tooltips: `localisation/english/chaosx_achievements_l_english.yml`;
- sprite registration: `interface/chaosx_achievements.gfx`;
- icon package: `gfx/achievements/`, with the durable inventory in `docs/events/018_resources_found/assets.md`.

## Temporary-workspace disposition

The event-scoped `docs/assets/018_resources_found/` workspace is temporary evidence rather than a runtime dependency. A bounded cave-monster reconstruction tranche is retained there while final Event 018 evidence gates remain open; the whole event-scoped workspace must be deleted only after genuine goal closure.

## Future extension rules

Future Event 018 achievements must bind to a persistent field, contract, commission, anchor, doctrine, campaign, or reconstruction ledger. Event receipt, button presses without outcomes, and generic division counts without capacity evidence are not sufficient predicates.
