# Event 010 - Death

This overview records package implementation claims.
The [documentation review](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_events_007_010_documentation.md) distinguishes source checks, historical records, and unresolved acceptance or validation.

Event 010 is `Death`, a minor fire-once event rooted at `chaosx.nr10.1`.
It has no cluster and uses `DTH` as the conflict-free country tag.
Death is ruled by Zol with the `God of Death` leader trait, uses an all-black map color and flag set, starts from a remote low-population island, and receives no starting divisions, starting manpower, starting equipment, or public opening notification.

## Flow

The hidden root event launches Death only when it is inactive and undefeated and no world-end campaign is active, consumes one eligible island state, records Death in the event log, and schedules delayed marine-office packets for the former owner/controller and nearby coastal or naval observers.
A valid quiet origin produces no opening popup.
The first `.2` and second `.3` reports are scheduled once per recipient country through `death_missing_island_report_scheduled`, even when several islands share an owner or observer.
Those indirect reports arrive months later and open Missing Island Reports decisions without revealing Death or Zol.
Each recipient keeps its own `death_maritime_evidence` case file.
The first and second reports, registry work, quiet quarantine, survey, weather dismissal, and a later confirmed coastal warning all alter that local file.
Hidden global Death state does not grant a country knowledge by itself.
Invalid or blocked manual starts through the hidden root use the owned `chaosx.nr10.5` failure popup for missing candidates, prior defeat, any world-end campaign, or an active Death crisis.
The hidden root refuses another launch by the same country while that failure popup is pending, preserving the first failure reason.

All consumption paths call `death_consume_current_state` in `common/scripted_effects/010_death_effects.txt`.
The shared effect records the previous population, removes population and state value, transfers owner/controller to Death, adds a Death core, applies active wasteland state effects, records civilian deaths when the deaths system is enabled, updates consumed-state counters, per-continent mainland counters, Last Ferry evacuation credit, withers lingering divisions, and checks reveal, defeat, world-end, and whole-world-consumed gates.

Before reveal, Death is intentionally slow.
Baseline Death consumes one eligible island, waits through long randomized pulses, and does not consume another island until the Second Shore evolution is recorded and Death has taken an island-spread focus.
Hidden island spread then prefers nearby sub-100,000-population islands first, falls back to any eligible sub-100,000 island only when no nearby one exists, and only then widens to the broader low-population island pool.
Each hidden island consumption checks the same former-owner/controller and nearby-observer recipient pool, while the country scheduling guard prevents repeating the first report pair.

Death reveals itself only when it consumes a mainland coastal state above the configured population threshold, and the natural mainland route remains locked until the Mainland Hunger evolution has been recorded, Death has taken the mainland focus, and enough island pressure has built up.
Ordinary mainland revelation and coastal jumps use the same ordered geography: an otherwise-valid coast within 750 distance units of an active wasteland.
Then a warned or investigating coast within 1,500.
Then an otherwise-valid coast within 2,500 while spread pressure is high.
The first tier with a candidate wins.
If no tier has a candidate, the attempt takes its cooldown and preserves its pressure instead of falling back to an unrelated coast elsewhere in the world.
World-end footholds remain a separate explicit exception.

The reveal pans player cameras to the revealed state, fires super-event `62`, declares war on the pre-transfer owner or controller of the consumed state, confirms the coastal warning in each affected living government's case file, and can pull in neighboring countries only when they directly border a Death wasteland or have already recognized a coastal warning.
It does not start a world war by itself.
Landlocked countries do not receive the general coastal response unless Death is physically on their border or already at war with them.
The reveal also immediately consumes unguarded neighboring states from the mainland wasteland and enables containment decisions for countries that have a reason to respond.
After reveal, Death runs daily public pressure from its tag-scoped on-action: living units in active wastelands are withered every day, neighboring living states receive a weaker border-withering modifier and daily unit damage, unguarded neighboring states fall immediately from any mainland Death wasteland, and scheduled pulses are shortened for stronger ghost refreshes, wither checks, and cooldown-limited coastal jumps.
Death becomes a world threat source only after it consumes a continent.

World-end starts only when Death has consumed a whole continent and Chaos is above the Death world-end threshold.
This fires super-event `63`, swaps Zol to the world-end portrait, creates one coastal foothold on each continent without an active Death-controlled wasteland presence, and unlocks the strongest host behavior.
World-end footholds prefer empty non-capital coasts, then relax watch/quarantine and defense filters before falling back to any valid coastal state.
A successful foothold pulls its owner/controller into war if needed.
If every populated state is consumed, super-event `65` fires.

Defeat is custom.
Death is defeated only when it controls no states, not by ordinary capitulation shortcuts.
Defeat clears the world-threat source, removes Death units/templates, and leaves wastelands as recaptured dead zones.
Governments earn limited custodial capacity from one-time surveys and outposts, Living Compact participation, and direct participation in the Death war.
A recaptured state can then progress through Surveyed Dead Zone, Custodial Outpost, and exactly one permanent policy: Sealed Exclusion, Memorial Stewardship, or Transit Custodianship.
Transit requires recurring service stores for its maintained-corridor benefit.
During a Black Friday sale (Event 026) every human response, compact, policy, maintenance, and Black Book payment reads its sale price: the positive amounts of the `death_decision_cost` spend constants are registered in the Black Friday price table as `global.black_friday_price_death_decision_cost_<cost>`, and the affordability triggers, the `death_pay_*` effects, and the cost texts read that one global, so holding exactly the shown amount is enough.
Death's own soul power and the earned custodial capacity are not purchases and keep their amounts.
None of the three restores erased population, state category, factories, resources, or recruitable manpower.
Super-event `64` fires only after public reveal and a major crisis threshold: at least 10 million consumed population, at least three mainland states consumed, or a world-end attempt.

## Gameplay Surfaces

- Event script: `events/010_death.txt`
- Constants: `common/script_constants/010_death_constants.txt`
- Effects: `common/scripted_effects/010_death_effects.txt`
- Triggers: `common/scripted_triggers/010_death_triggers.txt`
- Ideas: `common/ideas/010_death_ideas.txt`.
  The old zombie opening idea is isolated in `common/ideas/002_zombie_ideas.txt`
- State modifiers: `common/dynamic_modifiers/010_death_state_modifiers.txt`
- AI strategy: `common/ai_strategy/010_death.txt`
- Decisions: `common/decisions/categories/010_death_categories.txt`, `common/decisions/010_death_decisions.txt`
- Country package: `common/country_tags/chaosx_countries.txt`, `common/countries/Death.txt`, `common/characters/DTH.txt`, `common/names/chaosx_custom_country_names.txt`, `history/countries/DTH - Death.txt`, `history/units/DTH_1936.txt`
- Custom units: `common/units/010_death_ghost_hosts.txt`
- Focus tree: `common/national_focus/010_death_focus_tree.txt`
- Localisation: `localisation/english/010_death_l_english.yml` plus shared GUI, ideas, achievements, music, event-name, and scenario localisation files
- Triggerable scenario: SCN-006 in the shared triggerable scenario files
- Event log: Death actor mapping, event details, and five milestone evolutions in the shared event-log scripted effects/localisation.
  `The First Silence`, delayed Missing Island Reports packets, the first mainland reveal, and whole-world-consumed finale are baseline crisis flow or terminal history, not normal evolution entries.
  The Event Details catalog lists Second Shore, Mainland Hunger, First Hosts, Hollow Hosts, and World End, while the actual evolution records are written only when their stage gates and Chaos-value gates are reached.
  Beneath those previews, Last Shores has its own clickable world-end row and automatic-selection checkbox.
  Its detail describes the remaining living countries holding distant fronts across empty cities and ruined supply roads, without asserting that several continents have already fallen.
  Its linked super-event presentation remains The Census of Zol.
  Early Death evolution detail pages use the normal Zol portrait.
  World End detail pages use the subtle animated world-end Zol portrait.
- Country identity: all DTH ideology and base flags use the black Death flag set.
  Party localisation resolves to `The Last Office`

## Decisions And AI

Missing Island Reports decisions are limited to countries that receive delayed marine-office packets.
They can send a survey boat, check the telegraph office, issue harbor sanitation notices, or close the file under weather.
The category reports country-specific confidence as fragmentary, patterned, probable, or confirmed.
Before confirmation, its names and tooltips describe silent routes and an unknown coastal threat rather than Death, DTH focus rewards, or world-end rules.
Surveying can confirm the hostile erasure before the world learns its public name and preserves quiet-defeat tracking.
Filing the case under weather removes three evidence points and raises spread pressure.
A later report can reopen the file.

Before confirmation, a coastal report recipient with an eligible port sees the same category as `Coastal Precautions`, containing only spoiler-safe port-watch preparation.
Once that country confirms the case or Death is publicly revealed, the category becomes `The Black Country` and exposes the appropriate public response surface for direct border danger, active war contact, Living Compact membership, or a confirmed coastal warning.
After defeat it becomes `Custody of the Empty Land`.
The public reveal does not make the category global, and landlocked countries outside the danger area do not receive the general coastal response.
The category contains public war recognition, Living Compact coordination, coastal patrols, wasteland gear, Last Shores response, quarantine line actions, coastal-watch state preparation, wasteland surveys, dead-zone outposts, Dark Methods, Black Oath, Herald, and Black Apostolate route decisions.
The forbidden route decisions display in red.
Stability is consumed as a consequence instead of blocking the action when the country is below the stability spend.
The human player can hide or show the state list for port-watch decisions, while AI countries still evaluate those decisions directly.
Keeping a port lit costs a major fuel stockpile and command resources, applies Coastal Watch for 120 days, and blocks normal hidden coastal jumps from selecting that state.
Wasteland Entry Gear, Share Wasteland Entry Gear and Last Shores Response give a country 180 days of gear protection through `death_country_has_entry_gear`: its divisions take half the usual daily damage in wasteland states and the states that border them, using the `geared_*` values in `death_wither_damage`.
A strong global watch network can stop one normal low-pressure coastal jump before it lands, then spends part of the network strength.
The No Ferry Returns focus, high spread pressure, and world-end coastal pressure bypass that interception.
Strengthening a quarantine line also starts a timed hold-line mission.
If the line survives the mission period, global front readiness improves and spread pressure falls, while an early break raises spread pressure.
The Black Atlas can be opened only after public revelation and remains a transient dashboard of text values.
Its GUI source declares a background and animated header.
It has no separate close control or decorative status icons, and its consumed-population line switches to `M` and `B` bands once the totals reach millions or billions.

The Death's Muster category is visible only to active DTH.
It shows consumed states, island and mainland counters, consumed population, spread pressure, soul power, spent soul power, host counts, and status lines for island spread, mainland spread, and host availability.
Soul power is generated from consumed states, consumed population, and last-shore footholds after world end begins.
It has no storage cap.
Available soul power is generated soul power minus what Death has already spent on spread decisions or ghost hosts.
Death can spend it to force an eligible island spread, press a valid mainland route when pressure or the war bypass allows it, or raise the ghost-host tier currently unlocked by Chaos and the Death stage.
Forced island spread starts at `constant:death_soul_power.island_spread_cost`, then each successful Death's Muster island consumption raises the next forced island cost by `constant:death_soul_power.island_spread_cost_step`.
Each successful Death's Muster mainland consumption raises the next forced mainland cost by `constant:death_soul_power.mainland_spread_cost_step`.
Each ghost host raised raises all later host costs by `constant:death_soul_power.host_cost_step`.
Spread pressure unlocks the normal mainland route at `constant:death_spread.mainland_pressure_threshold`, makes withering faster at the high and extreme thresholds, shortens coastal-jump cooldowns at those thresholds, and lets Death keep seeking coastal jumps once pressure reaches `constant:death_spread.pressure_coastal_jump_threshold`.
AI Death uses the same decisions.
It prioritizes cheap island consumption before public reveal while island targets remain empty, then spends on mainland pressure and ghost hosts as the crisis opens.

Dark Methods are a living-country desperation route.
A threatened country can open Black Book offices, bind unburied names into weak capped hosts, interrogate empty roads for Death pressure intelligence, seal names in iron, and burn the Black Book before exposure becomes a domestic scandal.
Seal Names in Iron targets one living-controlled recaptured wasteland bordering an active Death wasteland and spends political power, support equipment, and trains through the sale-aware payment path.
Living-controlled recaptured wastelands adjacent to active DTH wasteland carry the existing border-withering hazard unless sealed, as defined by `death_should_have_border_wither_state`.
Seal Names clears the selected state's wither progress and removes its existing `death_border_wither_state` modifier through the border-status refresh.
The 120-day seal blocks that local border hazard and its daily division damage, while the independent 180-day resealing cooldown remains.
A landing or military attack can still retake the state, and actual DTH control recapture during protection adds two spread-pressure points.
That backlash runs in `death_apply_active_wasteland_state` before custodial cleanup clears the seal, reached through `death_on_state_control_changed`.
The consumed-state marker persists on recaptured dead zones, so the first-time consumption branch in `death_consume_current_state` is not the recapture backlash hook.
The action also reduces Black Book exposure by two and mourning debt by one.
If the country only opened the book and took nothing from it, the book can be closed for free.
Once a forbidden method has been used, burning the book costs political power.
The route uses exposure, bound names, and mourning debt variables, keeps AI use conservative, and records the hidden Book Burner predicates only when the country used a Dark Method, burned the book before the high-exposure threshold, and later helped defeat Death.

The Black Oath is a separate betrayal route.
A desperate country can whisper to Zol, take the oath, leave the Living Compact, receive the Herald of Zol cosmetic identity and national idea, and gain Herald decisions.
Heralds can offer a prison census, open dead ports, feed border states to Death through the shared consumption helper, or break the oath and become a direct Death target.
Name debt, black favor, living disgust, sacrificed states, and dead ports control the route.
If a Herald reaches the hidden thresholds after world-end, it can proclaim the Black Apostolate cosmetic identity and route culmination.

After Death is defeated, active war and compact decisions close.
Recaptured wasteland decisions remain available so living countries can survey dead zones, build outposts, and choose one irreversible custodial policy.
Survey requires a division owned by the acting country in the selected recaptured state, with no supplied-status check.
Build the Dead-Zone Outpost requires an acting-country-owned division in the selected surveyed recaptured state, alongside the existing living-control and no-outpost checks.
The guarded field crew uses army experience, support equipment, trucks, and trains, with the existing sale-aware payment path.
The final `death_apply_dead_zone_outpost_to_target` effect revalidates `death_is_valid_dead_zone_outpost_target`, including `death_state_has_player_division`, before payment and outpost work.
This accepted field-delivery requirement makes no claim that the division is supplied and adds no construction-burden effect.
Sealed Exclusion hardens exposed approaches.
Memorial Stewardship spends more capacity on a permanent state memorial and grants the national stability/mourning reconciliation only once per country.
Transit Custodianship preserves a limited supply and movement corridor whose strongest benefits last 180 days per service allotment.
Survey and outpost capacity rewards are retained per-state ledgers, so reconsumption or a change of controller cannot mint them twice.
Death regaining control clears the active project and policy package before reapplying the active wasteland, with any protected-state backlash applied before cleanup.
Dead-zone outpost tracking starts only after the custom defeat path has fired.
Capitulation runs the same defeat cleanup and the winner annexes DTH instead of leaving it as a puppet.
If a peace result still creates a DTH subject, the subject loses Death mechanics, receives a generic focus tree, and is assigned an emergency administrator.

AI weights are intentionally conservative before reveal, stronger for threatened countries after reveal, and strongest for compact/Last Shores responses.
AI countries will not choose Death war decisions while Death has consumed only its first island.
Once Death has consumed more than one island, aggressive AI countries can use the public war decisions only when they border Death, are already in contact with it, or have a confirmed coastal warning.
Compact invitations and Compact war declarations use the same boundary, so distant countries and landlocked countries outside the danger area stay out.
Dark Methods have low AI weights and are biased toward direct-threat or world-end desperation.
Black Oath AI is heavily restricted to unstable, non-major, threatened countries in world-end conditions, and the Black Apostolate proclamation is player-only.
Death itself has staged ghost behavior: no starting units, weak passive custom hosts at the First Hosts milestone, stronger but still inferior custom hosts at the Hollow Hosts milestone, and aggressive parity hosts only for world-end.
`common/ai_strategy/010_death.txt` keeps public pre-world-end fronts careful and non-executing, then switches Death to rush execution after world-end starts.
Host effects provision only the dummy manpower and infantry equipment needed by the locked custom template at creation time.
Each ghost battalion uses one dummy manpower and one dummy infantry equipment, and Death has no normal recruitment route for these units.
Natural pulses, focus rewards, manual Death's Muster decisions, and last-shore footholds spend from a shared soul budget based on consumed states, consumed population, and recorded last-shore footholds.
There is no soul cap.
The practical limit is rising cost: island spread, mainland spread, and host raising all become more expensive after successful uses.
The Death's Muster AI spends on cheap island spread first while valid empty islands remain, raises available ghost hosts when it is not saving for a pre-reveal mainland press, and spends more aggressively after public reveal or war contact.
SCN-006 directly creates its selected starting hosts and charges the same host counters afterward so later natural spawns keep the same escalating prices.

SCN-006 has one triggerable Death setup: Instant Outbreak.
Manual launch consumes a hidden origin, intensity-scaled extra islands, at least one mainland reveal target, and intensity-scaled ghost hosts.
The Death-specific caller creates the selected hosts and announces success only when `death_instant_outbreak_launch_succeeded` is set after public revelation.
Successful launch at any intensity schedules the ordinary `chaosx.triggerable_scenarios.6` success acknowledgement and one aggregate `chaosx.nr10.4` mainland news through `death_emit_mainland_reveal_news`, guarded by `death_world_news_emitted` for the whole world.
The mainland news is a major news event through `major = yes`.
`death_instant_outbreak_started` is set only after successful mainland revelation.
Successful Instant Outbreak supplies a separate island-spread gate in `death_can_spread_to_islands` through that flag, allowing island spread without fabricating Second Shore or focus-completion flags.
Only a successful Maximum-intensity launch sets `death_maximum_manual_scenario_used`.
The triggerable wrapper checks prior defeat first, then any world-end campaign through `world_end` or `death_world_end_started`, then an active Death crisis.
Those blocks and invalid origin or mainland candidates use the same owned `chaosx.nr10.5` failure popup.
`death_queue_instant_outbreak_failure` sets the country latch `death_instant_outbreak_failure_pending` and the shared `chaosx_manual_event_failure_shown` flag before scheduling that popup.
Both `.1` and `trigger_death_scenario` refuse another same-country launch while the latch is set, so one owned failure response remains pending and the original reason is retained.
The shared flag suppresses a second generic manual-failure popup.
Acknowledging `.5` clears the pending latch and the failure-reason flags, allowing a later launch attempt to be evaluated again.
Instant Outbreak does not set the Chaos Meter, fabricate natural evolution flags, or start world-end.
After launch, Death continues through the same natural pulses and can only escalate further through ordinary crisis growth.

Achievement tracking follows the route predicates described in source.
`death_not_on_my_continent` uses the player's capital-continent mainland-consumption counter, `death_last_ferry` records prepared threatened states only when Death later consumes them, `death_counted_every_name` requires census participation plus major/compact coordination before Hollow Hosts gather and below Black Book scandal exposure, and `death_black_tide_reversed` requires all recorded last-shore footholds recaptured with no surviving Herald of Zol.
Six Continents, One Color requires at least six distinct continents, counted through continent flags and `global.death_world_end_unique_continents`, while the independent `global.death_world_end_footholds` count continues to tune soul power.
Defeat aftermath eligibility is saved in `death_defeat_super_event_pending` before active and world-end flags are cleared, preserving the crisis threshold through teardown.

The Death focus tree is a fixed-purpose 26-node lane tree.
It has an opening trunk, Shroud/Hunger/Census pre-reveal lanes, a `Public Death` convergence focus gated by public reveal, Coastal/Wasteland/Host post-reveal lanes, and a terminal Last Shores/World Consumed branch.
Public Death requires the three separate endpoints `death_island_pattern`, `death_mainland_smell`, and `death_first_ghost_muster`.
Shroud focuses bypass after public revelation without granting their completion rewards, and Public Death bypasses after successful Instant Outbreak through `death_instant_outbreak_started`.
The Shroud lane is available while Death is hidden, at peace, and no later than Gathering Storm, and it closes once a living-country survey war has started.
The Island Pattern can be taken before Second Shore, but its immediate island consumption only fires when island spread is already active.
If a living country declares war after the Second Shore evolution, Death can complete Mainland Smell before the natural Mainland Hunger tier and record that evolution early.
This bypass never works before Second Shore.
No Graves Needed grants a one-time shared soul-pool bonus equal to the weak-host cost at focus completion through `death_award_no_graves_muster_reserve`.
The bonus enters `global.death_focus_soul_power_bonus` and is fungible with other soul power, so it is available to spread and host spending rather than earmarked for one host.
Wasteland Roads adds one extra wither-progress point to the eligible border state selected by each wither attempt during a spread pulse.
The forbidden routes live on living-country decisions instead of adding another DTH focus branch.

## Assets

Registered sprites:

- `GFX_portrait_DTH_zol`, `GFX_portrait_DTH_zol_world_end`, and `GFX_portrait_DTH_zol_world_end_animated` in `interface/chaosx_characters.gfx`, files under `gfx/leaders/010_death/`
- `GFX_report_event_death_mail_boat`, `GFX_report_event_death_lighthouse`, `GFX_report_event_death_census`, `GFX_news_event_death_mainland_reveal`, `GFX_news_event_death_defeated` in `interface/chaosx_pictures.gfx`
- `GFX_super_event_death_reveal`, `GFX_super_event_death_world_end`, `GFX_super_event_death_defeat`, `GFX_super_event_death_world_consumed` in `interface/chaosx_super_events.gfx`
- `GFX_super_event_death_black_oath` in `interface/chaosx_super_events.gfx`, file `gfx/super_events/010_death/super_event_death_black_oath.dds`
- Black Atlas sprites and frame-sheet definitions in `interface/010_death.gfx`, used by `interface/010_death_black_atlas.gui`
- Decision, focus, and idea sprites in `interface/010_death.gfx` and `interface/chaosx_ideas.gfx`
- Achievement sprites in `interface/chaosx_achievements.gfx`

The maritime and spatial decisions reuse the registered survey boat, coastal watch, quarantine line, Living Compact, dead-zone outpost, and wasteland-gear icons in `interface/010_death.gfx`.
Custodial-capacity payments use the dedicated `GFX_death_custodial_capacity_texticon`, registered in `interface/010_death.gfx` and displayed as `£GFX_death_custodial_capacity_texticon`.
Its transparent 18×18 DDS is installed at `gfx/interface/texticons/010_death/010_death_custodial_capacity_texticon.dds`.

Death super-event package:

- `62`, `Death`, image `GFX_super_event_death_reveal`, audio `sound/010_death/super_event_32_death_reveal.wav`, quote source Francis Bacon
- `63`, `The Census of Zol`, image `GFX_super_event_death_world_end`, audio `sound/010_death/super_event_33_death_world_end.wav`, quote source Matthew Arnold
- `64`, `The Unfinished Work`, image `GFX_super_event_death_defeat`, audio `sound/010_death/super_event_34_death_defeat_aftermath.wav`, quote source Abraham Lincoln
- `65`, `No Witness Remains`, image `GFX_super_event_death_world_consumed`, audio `sound/010_death/super_event_35_death_world_consumed.wav`, quote source Edward Young
- `66`, `A Covenant with Death`, image `GFX_super_event_death_black_oath`, audio `sound/010_death/super_event_36_death_black_oath.wav`, quote source Isaiah 28:15

The former final-asset record `docs/assets/010_death/generated_art_manifest.md` is absent and Git records its deletion in `487670dee3722238dadc218a30d84c59aa27594a`.
Its historical path is retained for provenance, and no replacement source manifest was established by this review.
Inherited static wiring is recorded for Death, Herald of Zol, Black Apostolate, the Black Oath super-event, and the world-end Zol portrait fallback.
The parent repair evidence records a lossless BGRA32 DDS-container conversion that preserves decoded pixels and alpha, with archived originals and hashes under the ignored `docs/assets/010_death/dds_container_repair` and `docs/assets/portraits/010_death/zol_world_end` workspaces.
That conversion establishes container repair only, and the inherited masters' source or ImageGen provenance remains unresolved.
The Black Atlas keeps its stable background and animated header.
Its eleven existing summary values are grouped into Seas, Fronts, Compact and conditional Book tabs, with at most four visible values per pane.
The current and maximum Watch Network counts are both included in the Fronts budget.
Native label/value controls use one aligned value column; Close hides the view and the free opener allows immediate reopening to Seas.
The source-state and production-render limits are in `docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06.md`.
The [2026-08-15 dashboard handoff](../../plans/010_death_plans/subagent_handoffs/2026_08_15_death_shared_dashboard_scripted_gui_handoff.md) records the historical `hoi4.gui_rewrite` failure for the proposed shared Atlas and `death_black_ledger_category` extension.
The user-supplied AGENTS.md on 2026-09-06 makes that rewrite route optional, so the recorded transaction failure alone is not a current implementation gate.
The pending extension remains separate from the existing living-country Atlas source and outside this documentation task.
The historical animation package describes an eight-frame sheet and registered animated sprite, while its inherited source-frame provenance remains unresolved.
World-end gameplay uses the static fallback for the country leader portrait.

## Repair Decisions And Evidence

The acceptance basis for this bounded repair is the parent's explicit 2026-10-05 decisions in the documentation assignment and the final-source and late-source follow-ups, including the G6-approved weak-design rewrites.
The parent owns the durable reason record at `docs/plans/010_death_plans/agent_decisions_2026-10-05.md`.
The evidence below describes the current source and does not establish engine behavior, visual acceptance, or balance validation.
Older package claims outside these repair rows remain subject to the linked documentation review.

| Surface | Disposition | Acceptance basis and current evidence | Limit |
| --- | --- | --- | --- |
| Quiet launch, first report pair, mainland news | implemented | Parent decision 1 and 3, `chaosx.nr10.1` and `.5` in `events/010_death.txt`, `death_schedule_missing_island_reports_for_country` and `death_emit_mainland_reveal_news` in `common/scripted_effects/010_death_effects.txt` | Source-supported guards, incomplete MCP event coverage |
| Public Death convergence and bypasses | implemented | Parent G6 decision 2, separate endpoint prerequisite blocks and bypass blocks in `common/national_focus/010_death_focus_tree.txt` | Current structure inspection, no engine proof |
| No Graves Needed and Wasteland Roads | implemented | Parent G6 decision 2 and late-source follow-up, `death_award_no_graves_muster_reserve`, the shared pool calculation, and `death_try_wither` in `common/scripted_effects/010_death_effects.txt` | No Graves is a fungible shared-pool bonus, source-supported rewards have no weighted scenario validation |
| Local Seal Names protection and recapture backlash | implemented | Parent G6 decision 2 and late-source follow-up, `death_apply_seal_names_to_current_state`, border-status refresh, `death_on_state_control_changed`, and `death_apply_active_wasteland_state` in the Death effects, plus the Seal tooltip and `death_decision_tuning` constants | Source removes the local border hazard and daily damage while sealed, actual DTH control recapture applies backlash before cleanup, engine validation unresolved |
| Recaptured-state border hazard | implemented | Parent late-source follow-up, `death_should_have_border_wither_state` includes living-controlled recaptured wastelands adjacent to active DTH wasteland unless sealed | Existing border hazard deliberately covers recaptured dead zones, engine damage behavior unresolved |
| Global-only seal scaling proposal | superseded | Parent G6 decision 2 replaces it with the local Seal Names design described above | No retained authorization for global-only scaling |
| Instant Outbreak success and failure | implemented | Parent decision 3, `death_launch_instant_outbreak` and `death_cleanup_triggerable_scenario_context` in the Death effects, `trigger_death_scenario` in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, and `GetDeathInstantOutbreakFailure` in `common/scripted_localisation/010_death_scripted_localisation.txt` | Source-supported launch result and maximum-use guards, no engine proof |
| Launch failure response latch | implemented | Parent final latch follow-up, `death_queue_instant_outbreak_failure` sets the country pending flag and shared manual-failure flag before queuing `.5`, `.1` and `trigger_death_scenario` guard repeated launches, and `.5` acknowledgement clears pending/reason flags | One owned failure response remains pending per country with its first reason preserved, generic duplicate suppressed, engine outcome unresolved |
| Instant Outbreak island-spread gate | implemented | Parent late-source follow-up, `death_can_spread_to_islands` in `common/scripted_triggers/010_death_triggers.txt` accepts the successful launch flag separately from the natural Second Shore and focus gates | No natural evolution or focus-completion flags are fabricated, engine continuation unresolved |
| Distinct continent achievement and defeat aftermath | implemented | Parent decision 4, `death_mark_world_end_foothold_created` and `death_finish_defeat` in `common/scripted_effects/010_death_effects.txt` | Source-supported counting and saved eligibility, engine outcome unresolved |
| Survey owned-division presence | implemented | Parent final-source follow-up, `death_state_has_player_division` uses `any_state_division = { OWNER = { tag = ROOT } }` inside the selected-state eligibility checked by `death_survey_the_wasteland` | Current source requires the actor's own division in the selected state, engine outcome unresolved |
| Survey supply-status gate | superseded | Parent G6 decision replaces the old supplied-division requirement with an acting-country-owned division present in the selected state plus paid transport stores because no documented native supply-status predicate could be verified | The implemented gate checks ownership and physical presence; it makes no supply-status claim |
| Build the Dead-Zone Outpost guarded field delivery | implemented | Parent acceptance of the final G6 Outpost closure, `death_is_valid_dead_zone_outpost_target` requires `death_state_has_player_division` in the surveyed recaptured state, and `death_apply_dead_zone_outpost_to_target` revalidates that target before payment | Army experience, support equipment, truck, and train costs are retained, with no supplied-status or construction-burden claim, engine outcome unresolved |
| Build the Dead-Zone Outpost supply-connection claim | superseded | Parent acceptance of the final G6 Outpost closure replaces the earlier supply-connection requirement with the guarded field-delivery row above because no documented native state-connection predicate was found | No supply-connection proxy was added, and the accepted field-delivery gate checks owned-division presence |
| Four-resource decision costs | implemented | Parent final-source follow-up, matching sale-aware payment, affordability, and display consumers for Patrol, Last Shores, and Transit setup/upkeep in the Death effects, triggers, and localisation | Each action fits four spendable types total. Transit setup uses one custodial capacity and three stockpiles; upkeep uses the three stockpiles. Engine affordability remains unverified |
| Weighted behavior and GUI acceptance | unresolved | Parent decision 6 retains partial/current MCP evidence and unavailable scenario baseline/compare | Partial focus probability and unobserved bounded decision comparisons, with no complete GUI comparison evidence |
| DDS containers and inherited masters | implemented / unresolved | Parent decision 7 records lossless container repair and archived originals/hashes, while master provenance remains unresolved | Container evidence cannot prove source artwork or native ImageGen production |
| Reveal super-event title | implemented | Parent decision 8, `chaosx_super_event.62.t: "Death"` in `localisation/english/010_death_l_english.yml` and the matching text-research table | Quote text and quote-source claims are preserved without re-research |

Survey requires a division owned by the acting country to be present in the selected recaptured state through `death_state_has_player_division`.
That helper uses `any_state_division = { OWNER = { tag = ROOT } }`, and the requirement is exposed by `death_survey_field_division_required`.
Survey does not require or verify that this division is supplied.
The parent's local-reference findings locate `any_state_division` at installed `documentation/triggers_documentation.md:1684-1692` and `divisions_in_state` at `:2648-2662`, neither of which documents a division-supply status or ratio predicate.
The offline wiki search for `is_in_supply trigger scope` returned no result, and `source_lookup(symbol="is_in_supply")` returned zero definitions.
The exact blocker is the absence of a verified native `is_in_supply` or equivalent division-supply predicate, so source-only review cannot establish that Survey requires a supplied division.

The following decision costs each use four matching paid and displayed resource components through the existing Black Friday sale-price globals.
Transit Custodianship setup also spends the separate custodial-capacity amount.

| Action | Paid and displayed resources | Source consumers |
| --- | --- | --- |
| Joint Coastal Patrol Plan | Command power, fuel, convoys, support equipment | `death_pay_patrol_cost`, `can_pay_death_patrol_cost`, `death_patrol_cost_text` |
| Last Shores Response | Command power, army experience, fuel, trucks | `death_pay_last_shores_response_cost`, `can_pay_death_last_shores_response_cost`, `death_last_shores_response_cost_text` |
| Transit Custodianship setup | Custodial capacity, support equipment, trucks, fuel | `death_pay_transit_custodianship_policy_cost`, `can_pay_death_transit_custodianship_policy_cost`, `death_custodial_transit_custodianship_cost_text` |
| Transit Custodianship upkeep | Support equipment, trucks, fuel | `death_pay_transit_custodianship_upkeep`, `can_pay_death_transit_custodianship_upkeep`, `death_custodial_transit_upkeep_cost_text` |

Patrol and Transit setup/upkeep have no train payment or affordability requirement, Transit has no Command Power payment, and Last Shores has no convoy or support-equipment payment or affordability requirement.
The parent final-source follow-up records that unused Event 026 quote rows remain registered, while the active Death consumers use only the resource sets above.

First-pass read-only MCP event inspection and neighborhood rendering returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `78377da4c592b4d65f740f74c4c0f1020990fd9dbb860e9f3851214a8aa444f4`.
The [bounded event trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed6593829d1c5c088ebd4cd2aed165efbd0d9ce24c714dd7ecb9a7aa04b01bc8/5b032f2156b21135e6a15d42a52cbefeae22320f964a143f381beee1a3967499/event-trace-78377da4c592.json) uses focused analysis with depth 1, eight-node and twelve-edge bounds, no helper expansion, and one blocking event diagnostic.
It cannot prove helper lifecycle behavior or complete Event 010 coverage.
The [refreshed hidden-root trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24403cfe6831dbcbae0c613feba2857793ff1128f5179a98a144378e85f1e078/0bf00a26ab552e1067a7315065505f5f98296c503427c0e11336c44e71dd9a38/event-trace-b765d69103fd.json) returned `EVENT_INSPECTED_PARTIAL` at revision `b765d69103fd513d1e287784b899ece50a0fa989e6eb9b818722710128ea7375` with the same focused depth, node, and edge bounds and one blocking event diagnostic.
It retains the helper-lifecycle and engine-behavior limits of the first-pass evidence.
The [late-source hidden-root trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e83563a557eea4f4d0eadd1a30a2a1bed0e8240da22bd016eb3f406ffa93b95d/ac14bdcf5b9cc6621e77f8bedc33418d559adfa7b024b61977f863fe96594b4b/event-trace-dd0eb9760ebd.json) returned `EVENT_INSPECTED_PARTIAL` at revision `dd0eb9760ebd24bb27c0cfbaf888395739be24ce484ccb885a86895fb9b7ca1e`, again with focused depth 1, eight-node and twelve-edge bounds, no helper expansion, and one blocking event diagnostic.
It does not validate the Seal recapture helper, daily border damage, shared soul spending, or post-launch island continuation in the engine.
The [current focus inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27d7b59d04ada102eb873f71ec086f91e3941cd1995f9b73a533008487ef0489/32c947451f52b77e23931a17d351d826cd9f5345aef48428f7e97dac2d7ff211/focus-inspect.b59b8768be0204d1.json) returned 26 Death focuses and no Death-tree diagnostic at revision `b59b8768be0204d13e759f54501f33b2195150cfcb798bb0b993ff696b7b3866`, with a separate warning for vanilla `continuous_restrict_freedom_desc`.
The [current focus render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4de3f15ab05af84352ed13bdf1c4540ad5874ef3602463fbc0ab5820b91c63a6/9d78bfd9b77b8635b26472346cda6afc2682f363c7a103deb818f706e980c84f/death_focus_tree.focus.svg) returned `FOCUS_RENDERED` with matching layout hash `afe9a7ce44ea42428115815cd2c328dfd8135f711991db9c26c1bc7b9464adf1`.
This artifact records current layout output without establishing an engine result or a reviewed before-and-after scenario.
First-pass decision inventory returned `DECISION_ANALYZED_PARTIAL` at revision `03a4d7e5d2f9179a2d8bff007c3f4fd57bf86f1548c827c630616607c273f754`, with `complete = false`, zero declared scenarios, and 100 unresolved definitions.
The [follow-up decision inventory](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74fb0976850affc5ea1f6aa90dca456824cdd22f79834b7170a1456523606eb0/c4bfc43a89b8008865a3a04722fed8f27271c770cc6c1b9d36d916f4a80b3ba7/decision-2de59143004b0ff2aa002c48.json) returned `DECISION_ANALYZED_PARTIAL` at revision `0f318ae2a013fdb4c89767c5ce296fb2183759b027e87ebcd14606df5df3b33b`, still incomplete with zero declared scenarios and 100 unresolved definitions.
The late-source `hoi4.decision_inspect` inventory refresh for `death_seal_names_in_iron` delivered no final result before client observation was stopped.
That request's tool outcome remains unresolved, and the prior inventory is retained without treating it as validation of the late Seal helper changes.
The final G6 `hoi4.decision_inspect` request for `death_build_dead_zone_outpost` under the unbound `documentation-outpost-unbound` scenario also delivered no final result before client observation was stopped.
The owned-division gate and final-effect revalidation are current source evidence, while the requested MCP scenario outcome remains unresolved.
The failure-latch `hoi4.event_inspect` trace for `chaosx.nr10.5` also delivered no final result before client observation was stopped, leaving refreshed latch coverage unresolved.
The [current Atlas inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0409f19d138b85c4eb5080ff1033a85647d4b177f3340b59c0928c23ce106ff7/dcf11512a2c7b63b2f9a2f3d320e6aefd1fe842f3729aec28f985fcf40832fc9/gui-inspect.0ba93b175482e098.json) returned `GUI_INSPECTED` at revision `0ba93b175482e09814d727d839f7e3522481e96c8bd37caa274f5d419d7e8e0f` for `death_black_atlas_container` under generated scenario `death-doc-public-generated-1`.
It reports four unresolved fidelity entries, a missing static fallback for `GFX_death_black_atlas_header_animated`, and seven visible-overlap findings that remain unreviewed in a matching production render.
This generated inspection is current source evidence and does not establish complete GUI state, resolution, or before-and-after visual acceptance.
Tool exposure and these successful responses establish only the returned read-only evidence, while standalone viewer availability remains unverified.
No engine proof, complete GUI before-and-after comparison, or weighted scenario baseline/compare is available.
AI descriptions above are source intent and cannot establish balanced campaign behavior.

## Future Plans

These retained proposals have unresolved current acceptance and do not authorize implementation through this documentation cleanup.

- Expand Living Compact obligations, shared missions, leadership disputes, and success or collapse thresholds in a separately accepted tranche.
- Add regional Black Atlas diagnostics after public revelation while keeping decisions authoritative.
- Add route-aware aftermath for Compact members, Black Book users, Heralds, and oathbreakers.
- Replace any generated static fallback asset only by keeping the existing sprite names and final paths stable.
