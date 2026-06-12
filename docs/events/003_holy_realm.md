# The Holy Realm

## Overview

The Holy Realm is event ID 3 and remains registered as a fire-once Chaos Redux event. It transforms Tibet into a full country path rather than a short event chain; if Tibet no longer exists, Bhutan or Nepal can serve as the Himalayan fallback host. If none of those countries exists as a valid normal country, the event is unavailable and displays as N/A in the event list. The route starts as a mountain refuge, becomes a Bodhisattva-led state, creates the Arhat Administration, prepares the Unshaken Seat, and can then realize Buddhahood through teaching, meditation, and low Defilements. Peaceful renunciation, Sangha Compact work, anti-chaos Buddha powers, pilgrimage-protection ledgers, and Final Silence are separate commitments with their own gates and consequences.

The current player-facing surface is the Holy Realm focus tree, decision categories, the compact Holy Mandala decision-category summary, the dedicated Bodhisattva and Buddhahood categories, the built-in Vow and Final Silence balance of power, event choices, event log entries, super events, national spirits, achievements, and localisation. The original Holy Realm values remain live country variables:

- Spiritual Legitimacy
- Compassion Drift
- Mandala Reach
- Final Silence Pressure

The Buddhahood layer adds Bodhi Progress, Dhyana Depth, Compassion, Detachment, Defilements, Meditation Charge, World Suffering, Sangha Cohesion, teaching successes, and crisis teaching successes. These values drive Buddhahood eligibility, Buddha powers, clean-route achievements, the False Buddha Schism, and Final Silence ritual access.

## Flow

1. `chaosx.nr3.1` redirects the event to Tibet if possible. If Tibet no longer exists, it can redirect only to Bhutan or Nepal. If none of those tags exists as a valid normal country, event selection treats the event as unavailable.
2. `chaosx.nr3.2` offers the spec formation choices: leave the monastery outside government, invite the figure into government, restrict the gatherings, or proclaim the mandate immediately.
3. A formed Realm records its host origin, sets the shared `THR` cosmetic tag, loads `THR_focus`, initializes counters, adds immediate Holy Realm cores on Bhutan and Nepal, opens decisions, and broadcasts an ambiguous refuge news item. The event transforms an existing host; it does not set `holy_realm_event_created_country`.
4. Refuge policy is remembered through `chaosx.nr3.4`: open roads, register names, or close passes.
5. Bhutan, Nepal, and Tibet can receive a Himalayan unity invitation through `chaosx.nr3.3`.
6. The focus tree drives the major stages through country flags and focus prerequisites. Evolutions are reserved for special crises or transformations rather than normal stage advancement.
   - `THR_bodhisattva_accepts_seal` fires the Bodhisattva stage.
   - `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, and `THR_many_lamps_one_flame` expose the teaching route and require successful teaching missions, including a crisis teaching success, before the Unshaken Seat. `THR_four_teaching_seats` expands the teaching network after the requirement gate and reveals late foreign teaching tools.
   - `THR_sit_beneath_prayer_flags`, `THR_first_quiet`, `THR_second_quiet`, `THR_third_quiet`, and `THR_fourth_quiet` expose the Dhyana route and require the concentration sequence to raise `dhyana_depth`. `THR_return_to_the_seat` keeps meditation active after Buddhahood and unlocks the emergency vow decision for real chaos threats.
   - `THR_council_of_abbots`, `THR_name_protector_regent`, and `THR_seat_pilgrim_assembly` are the mutually exclusive early governance choices before the Unshaken Seat.
   - `THR_arhats_take_office` creates the Arhat Administration.
   - `THR_buddha_mandate` is localised as the Unshaken Seat and marks the focus prerequisite for Buddhahood.
   - `THR_the_awakened_one`, `THR_show_the_powers`, `THR_powers_are_not_toys`, `THR_read_pattern_suffering`, `THR_one_becomes_many_focus`, `THR_path_through_walls`, `THR_lotus_bridge_focus`, `THR_vanishing_from_sight_focus`, `THR_seated_in_sky_focus`, and `THR_touch_sun_moon_focus` form the post-Buddhahood anti-chaos power branch.
   - `THR_debate_the_pretender_focus`, `THR_exile_the_echo`, `THR_break_false_mandala`, and `THR_absorb_the_shadow` are hidden until the False Buddha Schism evolution has triggered. They resolve the Schism through teaching, exile, suppression, or high-chaos absorption. If the echo is exiled, `THR_answer_false_buddha_echo_abroad` can turn it into a foreign incident: a contacted or unstable host may contain the echo and clear the route stain, or shelter it and keep the crisis alive.
   - `THR_throne_without_body` and `THR_doctrine_last_war`, localised as the Last Wheel, open Divine Sovereignty and the locked final doctrine path after the powers have been shown.
   - `THR_witnesses_gather`, `THR_extinction_of_defilements_focus`, and `THR_final_silence` expose the final ritual gates, while Final Silence completion remains handled by the ritual decision gate.
   - `THR_empty_seat` is the non-terminal aftermath focus when Final Silence completes without setting a world-end. `THR_witnesses_keep_the_record` follows it by turning taught countries, Mandala mission hosts, observer hosts, development hosts, and valid compact members into public Empty Seat witnesses.
7. Chaos thresholds shape the route and are shown with exact values in focus tooltips. Low-chaos focuses require the Chaos Meter below `250`, `400`, or `600` depending on route tone. Interventionist, coercive, and final doctrine preparation focuses require the Chaos Meter above `400`, `600`, or `800`. Only the actual Final Silence launch requires `1000`.
8. The borderland tree starts separately with `THR_complete_himalayan_mandala` and `THR_guardians_outer_passes`, then opens the pilgrimage-protection route through `THR_letters_beyond_passes` without excluding the peaceful or Final Silence main branch. `THR_mandala_receives_borderlands`, `THR_high_pass_states_enter_mandala`, `THR_roads_must_be_quiet`, `THR_outer_valleys_register`, `THR_mandala_borders`, `THR_peace_by_submission`, `THR_northern_indian_register`, `THR_northern_indian_state_registers`, `THR_eastern_mandala`, `THR_western_chinese_registers`, `THR_eastern_chinese_registers`, and the high-chaos `THR_world_is_a_border` unlock protection letters, refusal war goals, Arhat administration, and direct progressive regional cores rather than generic bonuses. The lower branch is framed as pilgrimage corridors, petitions, and protection ledgers; the high-chaos capstone remains explicitly coercive.
9. Arhat events cover empowered administration, constrained ledgers, village silence, false attainment, inquiries, removals, and expanded methods.
10. Doctrine branches cover restraint, peacekeeping, coercive pacification, Divine Sovereignty, Renunciation, and Final Silence.
11. Decisions provide Arhat oversight, refugee policy, diplomacy, doctrine selection, conquest-route border tools, concentration vows, Buddhahood realization, Buddha powers, False Buddha Schism resolution, Final Silence ritual completion, Mandala Break disruption, and foreign containment responses.
12. `holy_realm_final_doctrine_balance` initializes at formation and attaches `holy_realm_doctrine_balance_category` to the balance-of-power screen. It represents the struggle between the Vow against Annihilation and Final Silence. Final Silence influence adds a small daily Final Silence Pressure tick; Vow influence lowers pressure.

## System Integration

The Holy Realm extends existing Chaos Redux systems rather than creating parallel ones:

- Chaos Meter: early refuge, mercy, mediation, restrained Arhat, and renunciation content can reduce chaos modestly through `add_chaos_meter_value`; administrative control, coercive pacification, Divine Sovereignty, final warnings, Mandala Break, and Final Silence raise chaos. Stage unlock effects do not add chaos by themselves.
- Evolutions: four special tracks record to the shared event-log evolution pipeline as evolution type `3`: Pattern of Suffering, False Buddha Schism, Relic Mandala, and Wrathful Protection. Normal stage advancement is handled by country flags and focus prerequisites, not event-log evolution rows. False Buddha Schism also refreshes the focus-tree layout so its conditional branch appears after the evolution is recorded.
- Focus tags: every Holy Realm focus has a `# THR FOCUS TAGS:` comment with area, tone, chaos requirement, system, and path-role metadata for audits. The focus tree exposes custom sorting filters for Holy Realm Peace, Final Silence Pressure, Mandala Integration, Bodhi, Teaching, Meditation, Governance, Sanctuary, Compact, Anti-Chaos, Nirvana, and Hidden content. The custom filters follow gameplay role rather than raw tag presence: peaceful refuge, restraint, diplomacy, and defensive preparation appear under Holy Realm Peace; focuses that alter or gate the Final Silence pressure system appear under Final Silence Pressure; territorial register, conquest, and coring focuses appear under Mandala Integration; the Buddhahood route filters identify the visible teaching, Dhyana, and governance gates.
- Event logs: event ID 3 has a dedicated event-detail description and four Holy Realm evolution preview entries covering the Pattern of Suffering, False Buddha Schism, Relic Mandala, and Wrathful Protection. The evolution list row shows the short evolution name and chaos tier; the detailed panes keep the evolution stage.
- Country package: Tibet remains the primary host. Bhutan or Nepal can host only if Tibet is gone. Formation sets `holy_realm_origin_tibet`, `holy_realm_origin_bhutan`, or `holy_realm_origin_nepal` and uses the shared `THR` cosmetic tag instead of origin-specific country names or a separate released country.
- Super events: values `7`, `8`, `9`, `10`, `11`, `51`, and `61` display The Awakened One, non-terminal Final Silence, terminal Final Silence, Mandala Breaks, Divine Sovereignty, Mandala of Nations, and Powers of the Awakened.
- World-end scenarios: terminal Final Silence sets `world_end`, `world_end_final_silence`, and `world_end_final_silence_completed`; non-terminal Final Silence sets `holy_realm_final_silence_nonterminal_completed` without ending the world. Interruption sets `world_end_final_silence_interrupted` and clears the active world-end flag.
- Settings: Final Silence is blocked by `world_end_disabled`.
- Triggerable scenarios: the scenario window can start Final Silence directly from the current player country as either the normal nuclear payload or the thermonuclear payload. This bypasses the standard Holy Realm launch gates but uses the same `holy_realm_prepare_final_silence`, strike-wave, fallout, deaths, wasteland, super-event, and follow-up wave logic.
- Multiplayer behavior: human countries receive ambiguous observation events around the Buddha Mandate and direct warnings only when the final doctrine is armed.
- Condemnation: Final Silence adds unconventional-warfare condemnation and applies existing diplomatic consequences.
- Deaths: Final Silence uses the shared `chaos_meter_register_state_civilian_deaths_percent` pipeline with the dedicated `chaos_meter_deaths_reason.final_silence` cause. The normal launch kills exactly `75%` of each struck non-Realm state's current population with a high billion-scale cap; the thermonuclear variant kills exactly `95%`.
- Air cleanliness: Final Silence sets global air contamination to exactly `100%`, marks it irreversible, locks future contamination changes at that value, and overrides the disabled air-cleanliness setting for the terminal branch.
- Nuclear and wasteland logic: Final Silence resolves in regional strike waves: Asia and the Middle East, Europe and Africa, the Americas, then Oceania plus any remaining states. Each wave uses `launch_nuke` with `use_nuke = no` for every state in that wave so the visual nuclear effect appears worldwide. Non-Realm target states also receive Final Silence deaths, fallout, building destruction, `wasteland` state category, and struck/burning/wasteland/silent state flags. State flags prevent duplicate population/death processing. Holy Realm states are not lethal target states, but they receive visible strikes and fallout from the global launch sequence.
- World threats: Divine Sovereignty, final warnings, and armed doctrine can set `world_threat_source_holy_realm`; the early refuge and Buddha Mandate are not treated as existential threats by themselves.
- AI: peaceful Holy Realm strategies prioritize defense, infrastructure, legitimacy, and low-chaos paths. Once Chaos Tier begins, peace-route focus and letter weights are suppressed, the Final Silence entry becomes available, and Totalen Chaos or World Collapse heavily multiplies Final Silence preparation and launch weights. Expansionist AI sends letters and pressures weak neighbors only before high chaos closes the peace-letter route, with forced integration weighted toward strong, prepared, high-chaos states. Final Silence remains locked behind Buddhahood, the armed final doctrine, doctrine dominance, the Extinction of Defilements rite, capital control, schism state, sovereignty, Chaos Meter state, and world-end settings.
- Mandala of Nations: `THR_mandala_of_nations` creates the `faction_template_holy_realm_mandala_of_nations` faction as the Sangha Compact implementation, sets peaceful faction rules, adds goals, applies the Mandala Peace Vow to members, and reduces chaos when valid countries join. Entrants must be non-chaos, non-puppet, minor countries with a crisis, chaos threat, teaching history, observer/development contact, or Pilgrim Assembly humanitarian opening. Invalid joins are rejected and reduce Sangha Cohesion. Members receive a `can_not_declare_war` rule while inside the faction, so the peaceful coalition cannot declare offensive wars.
- Compact refusal and exit notices: invalid entrants fire `chaosx.nr3.128` for the rejected country and `chaosx.nr3.129` for the Holy Realm before they are removed. A member leaving after receiving the Mandala Peace Vow fires `chaosx.nr3.130` for the Holy Realm, clears the vow, and refreshes valid compact status without adding a polling hook.
- Doctrine balance: the built-in balance of power uses `common/bop/003_holy_realm_bop.txt`, with Vow and Final Silence sides. It gives range modifiers, stores current doctrine pressure flags, and is moved by decisions, focuses, and teaching events. Final Silence launch now requires the Final Silence side to dominate the balance.
- Bodhisattva bhumi system: `holy_realm_advance_bodhisattva_bhumi` advances up to ten bhumis, refreshes the leader portrait, and swaps leader traits through `holy_realm_bodhisattva_pramudita`, `holy_realm_bodhisattva_vimala`, `holy_realm_bodhisattva_acala`, and `holy_realm_bodhisattva_dharmamegha`.

## Interactive Values

The Holy Mandala category uses a compact scripted GUI instead of a separate dashboard. It shows Spiritual Legitimacy, Bodhi, Dhyana, teaching successes, Meditation Charge, Defilements, colored Chaos value, and Final Silence Pressure without adding a duplicate title or direct warning labels. The detailed mechanics are hoverable read-only value rows:

- `THR_status_spiritual_legitimacy` explains how Spiritual Legitimacy affects stage text, peaceful AI, Arhat legitimacy, and non-final authority.
- `THR_status_compassion_drift` explains mercy versus coercive drift, event text changes, dangerous AI willingness, and final pressure interactions.
- `THR_status_mandala_reach` explains diplomacy, peace letters, regional integration, Chinese registers, and Ministry of Silence reach gates.
- `THR_status_sealed_ledger` displays Final Silence Pressure, the `45/55/65/75` preparation thresholds, and the current Buddhahood/ritual/world-end gates.

These rows are intentionally unavailable decisions so players can hover them without accidentally firing effects.

Routine value growth has diminishing returns. Positive Spiritual Legitimacy, Mandala Reach, and Final Silence Pressure gains are halved above `70` and halved again above `90`. Compassion Drift slows in either extreme above `70` and `90`. Routine actions remain useful, but the last value tiers need major focuses, missions, accepted submissions, doctrine commitments, or final-preparation choices.

## Focus Tree Balance

Early identity and refuge focuses use short costs so the Realm becomes active quickly. Mountain Refuge, Bodhisattva government, refugee shelter, guarded passes, and the Seal of Refuge now provide large stability, political organization, protected manpower, infrastructure, supply, bunkers, and legitimacy without early villain framing. Peaceful Himalayan unity adds `holy_realm_himalayan_unity`; forced cleanup through `THR_complete_himalayan_mandala` instead adds Mandala Reach and Compassion Drift memory.

Arhat Administration and Buddha Mandate are mid-game power spikes. They unlock stronger administration, compliance and construction tools, Arhat oversight, Mandala diplomacy, the Mandala Bureau intelligence agency, military organization, doctrine branches, faster industry, stronger vow-keeper forces, and accelerated nuclear preparation if the player later enters the final doctrine route. The borderland route adds strong regional tools but carries Compassion Drift, foreign suspicion, refusal records, and high-chaos locks rather than free world conquest. Acceptance of protection letters is intentionally rare; major powers and faction members cannot accept.

The guardian branch now runs through `THR_vow_keeper_regiments`, `THR_shelters_under_stone` as Fortress Without Hatred, `THR_quiet_mobilization` as Mountain Pass Detachments, `THR_mountain_artillery_mandalas` as The Bell and Rifle, and `THR_unbroken_pass` as the anti-chaos defensive capstone. `THR_vow_keeper_regiments` also unlocks `THR_bodhisattva_guard_pilgrimage_route`, a map-targeted timed escort mission that occupies a teaching seat, spends Command Power and support equipment, requires two divisions in a controlled route state, and rewards guarded pass infrastructure, Bodhi, Compassion, Sangha Cohesion, Mandala Reach, and Army Experience if the route is held. The capstone requires real chaos pressure, a recent capital-sanctuary fall, or Chaos Tier pressure and applies the Last-Pass Mobilization idea without opening ordinary conquest tools.

The sanctuary logistics branch now names its map work directly: `THR_count_mountain_roads` is Pilgrimage Roads, `THR_monastic_labor_vows` is Monastery Workshops, and the follow-up focuses `THR_mountain_granaries`, `THR_snowline_clinics`, and `THR_storehouses_for_world` add granaries, clinics, supply nodes, support equipment, and compact infrastructure aid.

The teaching route uses active teaching seats to keep the Bodhisattva category paced. Basic Dharma teaching work can run up to three timed teaching missions at once. `THR_four_teaching_seats` raises the cap to four and reveals late follow-up letters, foreign pilgrimage, Mandala missions, and sympathetic-government support. Buddhahood, One Becomes Many, or the One Becomes Many focus raises the cap to five.

Governance choices now have later route-specific follow-up focuses. `THR_abbot_examiners` lets Council of Abbots governance open the fourth active teaching seat before the wider teaching network is complete. `THR_regent_pass_watch` turns Protector Regent governance into capital-pass defenses, support equipment, and command capacity at the cost of a small Defilements increase. `THR_pilgrim_refuge_courts` lets Pilgrim Assembly governance widen the low-stability humanitarian compact path and adds refugee manpower, Mandala Reach, and Sangha Cohesion.

The meditation route now continues after awakening. `THR_return_to_the_seat` adds a post-Buddhahood Dhyana payoff and unlocks `THR_renew_vow_under_fire`. That emergency decision is visible from the awakened meditation seat, requires the fourth Dhyana, a controlled capital, and a real chaos threat to the Realm, a neighbor, or a compact ally. It spends Command Power, support equipment, and a small amount of Stability to restore Meditation Charge faster, add Detachment, reduce Defilements, and record Wrathful Protection readiness.

The Mandala of Nations is the peaceful Sangha Compact route. Its goals are completed through decision-based acts of kindness:

- `THR_mandala_open_refuge_corridors`
- `THR_mandala_white_flag_congress`
- `THR_mandala_open_granaries`
- `THR_mandala_demand_anti_puppet_clauses`
- `THR_mandala_joint_defense_of_passes`

The first three acts reduce chaos modestly and complete visible faction goals that add faction initiative and power projection. Anti-puppet clauses enforce the compact's independence rule, remove hard-invalid members, and improve Sangha Cohesion without being a kindness goal. Joint Defense of the Passes is the crisis defense act: it appears only during a true chaos threat to the Realm, its neighbors, or the compact, spends command capacity and support equipment, strengthens compact initiative, and sends defensive support to valid compact members. Additional valid countries joining the Mandala of Nations reduce chaos once per country. Governance choices alter compact work: the Council of Abbots adds political capacity and cohesion, the Pilgrim Assembly adds refugee manpower and stronger cohesion, and the Protector Regent adds command capacity while raising Defilements and slightly straining cohesion.

After formation, the same decision category opens active Mandala work:

- `THR_mandala_arbitration_letters` targets a country at war and starts `chaosx.nr3.125`; one enemy receives `chaosx.nr3.126` only if the first side accepts. White peace fires only when both sides accept while still at war.
- `THR_mandala_observer_mission` targets a country at war, sets a target cooldown, improves relations, and records Mandala observer work.
- `THR_mandala_development_mission` targets poor, rural, underdeveloped, or war-affected African, South American, and Asian countries and repairs one eligible controlled state with infrastructure, possible civilian industry, and resistance/compliance recovery.
- `THR_stand_between_armies` sends one limited Mandala Peacekeeping Brigade to eligible minor democratic defenders, with yearly target cooldowns and manpower/equipment costs. After `Shelter the Exiles`, faction members can also receive this support.

The Vow and Final Silence balance of power adds a second late-game management surface. It includes Political Power decisions for public vows, mercy councils, Bodhisattva council missions, lamp processions, lotus audits, outer-monastery reconciliation, sealed-name releases, sealed ledger readings, launch ledger sealing, silence-cell expansion, black ledger drills, silent transit codes, the Nuclear Sutra Committee, Last-Pass Watch, the White Mandala Oath, and the Empty Mandala Session. These decisions move the doctrine balance, alter Final Silence Pressure, alter Compassion Drift or Spiritual Legitimacy, and in some cases reduce or increase Chaos. The daily pulse is intentionally small so the balance creates pressure over time without replacing focus and decision choices.

Expansion coring is progressive and direct:

- `THR_high_pass_states_enter_mandala` adds Holy Realm cores on Tibet, Bhutan, Nepal, and Kham/Chamdo states.
- `THR_northern_indian_state_registers` adds Holy Realm cores on northern Indian protection-ledger states after the northern Indian claim focus.
- `THR_western_chinese_registers` adds Holy Realm cores on western Chinese protection-ledger states after the Eastern Mandala opens.
- `THR_eastern_chinese_registers` adds Holy Realm cores on eastern Chinese crisis-ledger states only under extreme chaos and high Mandala Reach.

Expansion decisions live in `holy_realm_expansion_category` after `THR_letters_beyond_passes`:

- `THR_send_peace_letter` targets eligible neighbors or countries bordering Holy Realm subjects.
- `THR_prepare_forced_integration` grants a war goal only after refusal.
- `THR_administer_submitted_territory` raises compliance and lowers resistance in submitted or registered states.
- `THR_integrate_himalayan_mandala_state`, `THR_integrate_northern_indian_register_state`, and `THR_integrate_eastern_mandala_state` add state-by-state cores only after ownership, control, Mandala Reach, Arhat administration, and region unlock conditions are met.
- `THR_mandate_kneeling_province` is unlocked by `THR_world_is_a_border` and cores claimed, controlled, non-core states one province at a time after the Realm has forced the world into its register.

## Focus Route Coverage

`common/national_focus/003_holy_realm.txt` contains 111 Holy Realm focus blocks. The required Buddhahood route families are implemented as follows:

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening survival trunk | `THR_mountain_refuge`, `THR_shelter_border_villages`, `THR_guard_high_passes`, `THR_bodhisattva_accepts_seal` | Implemented | Establishes the refuge, border shelter, high-pass defense, Bodhisattva government, early stability, protected states, supply, and legitimacy. |
| Teaching mission path | `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, `THR_many_lamps_one_flame`, `THR_four_teaching_seats` | Implemented | Requires teaching successes and crisis teaching before the Unshaken Seat, then expands the active teaching-seat cap and late teaching tools. |
| Meditation and Dhyana path | `THR_sit_beneath_prayer_flags`, `THR_first_quiet`, `THR_second_quiet`, `THR_third_quiet`, `THR_fourth_quiet`, `THR_return_to_the_seat`, `THR_renew_vow_under_fire` | Implemented | Gates Dhyana depth through the concentration sequence and keeps meditation relevant after Buddhahood through the emergency vow loop. |
| Governance route family | `THR_council_of_abbots`, `THR_name_protector_regent`, `THR_seat_pilgrim_assembly`, plus `THR_abbot_examiners`, `THR_regent_pass_watch`, `THR_pilgrim_refuge_courts` | Implemented | The three governance choices are mutually exclusive and each has a later teaching, defense, refugee, or compact hook. |
| Industry and sanctuary logistics | `THR_labs_snow_line`, `THR_refuge_foundries`, `THR_count_mountain_roads`, `THR_monastic_labor_vows`, `THR_mountain_granaries`, `THR_snowline_clinics`, `THR_storehouses_for_world` | Implemented | Adds map-facing roads, workshops, granaries, clinics, supply nodes, support equipment, and compact infrastructure support. |
| Guardian military | `THR_vow_keeper_regiments`, `THR_shelters_under_stone`, `THR_quiet_mobilization`, `THR_mountain_artillery_mandalas`, `THR_unbroken_pass` | Implemented | Provides defensive pass forces, guardian artillery support, the anti-chaos defensive capstone, and the active pilgrimage escort mission. |
| Sangha Compact diplomacy | `THR_mandala_of_nations`, `THR_mandala_demand_anti_puppet_clauses`, `THR_mandala_joint_defense_of_passes`, compact kindness acts | Implemented as Mandala of Nations | The Mandala of Nations is the Sangha Compact equivalent, with non-chaos membership rules, cohesion checks, invalid-member rejection, exit notices, independence enforcement, and crisis defense. |
| Liberation or pilgrimage expansion | `THR_complete_himalayan_mandala`, `THR_guardians_outer_passes`, `THR_letters_beyond_passes`, `THR_mandala_receives_borderlands`, `THR_high_pass_states_enter_mandala`, `THR_mandala_borders`, `THR_peace_by_submission`, regional register focuses, `THR_world_is_a_border` | Implemented | The normal branch is framed as pilgrimage corridors, petitions, protection ledgers, progressive cores, and refusal responses; `THR_world_is_a_border` remains the high-chaos coercive capstone. |
| Anti-chaos powers | `THR_the_awakened_one`, `THR_show_the_powers`, `THR_powers_are_not_toys`, `THR_read_pattern_suffering`, `THR_one_becomes_many_focus`, `THR_path_through_walls`, `THR_lotus_bridge_focus`, `THR_vanishing_from_sight_focus`, `THR_seated_in_sky_focus`, `THR_touch_sun_moon_focus` | Implemented | Paces all major named powers after Buddhahood and uses the shared `is_special_chaos_country` gate for valid chaos targets. |
| Buddhahood and Final Silence | `THR_buddha_mandate`, `THR_the_awakened_one`, `THR_doctrine_last_war`, `THR_witnesses_gather`, `THR_extinction_of_defilements_focus`, `THR_final_silence`, `THR_empty_seat`, `THR_witnesses_keep_the_record` | Implemented | The Unshaken Seat requires teaching, Dhyana, and governance gates; Final Silence remains gated by the ritual decision and splits into terminal and non-terminal outcomes. |
| Hidden Schism branch | `THR_debate_the_pretender_focus`, `THR_exile_the_echo`, `THR_break_false_mandala`, `THR_absorb_the_shadow`, `THR_answer_false_buddha_echo_abroad` | Implemented | Hidden until the False Buddha Schism evolution triggers, with debate, exile, suppression, high-chaos absorption, and foreign echo response paths. |

## Final Silence Conditions

Final Silence uses a ritual gate and an outcome gate.

- the Holy Realm exists and is the acting country
- the Holy Realm is sovereign
- Buddhahood has been realized
- the Final Silence focus path is unlocked
- the final doctrine is armed and not renounced
- Final Silence dominates the Vow and Final Silence balance of power
- an anti-chaos Buddha power has been demonstrated
- Extinction of Defilements has been completed
- the capital sanctuary is controlled
- no active False Buddha Schism remains
- `world_end` is not already active

If global Chaos is above `1000`, `world_end_disabled` is not set, and no other world-end is active, the terminal branch sets the Final Silence world-end flags and shows super-event slot `9`. Otherwise completion uses the non-terminal Empty Seat branch, leaves `world_end` unset, disables the armed doctrine, and shows super-event slot `8`. After `THR_empty_seat`, `THR_witnesses_keep_the_record` sends the aftermath back through prior teaching and compact contact: valid witnesses gain opinion, stability, and, for compact members, war support, while the Realm gains Sangha Cohesion if at least three witnesses answer.

If the date is later than 1946.12.31, thermonuclear technology or doctrine exists, the shared nuclear stockpile is at `999`, and `holy_realm_thermonuclear_payloads_prepared` is above `99`, the terminal branch also sets `world_end_final_silence_thermonuclear`. The thermonuclear presentation uses the terminal Final Silence slot and currently shares the same image texture as the normal terminal Final Silence sprite while retaining distinct audio wiring.

The three preparation focuses before the Ministry of Silence use short costs. They unlock foreign target audits, global final warning letters, and internal non-return shelters before the final ministry can be completed. Before launch, the armed doctrine runs a warning chain. This chain can be completed before Chaos Meter reaches `1000`; it is a launch prerequisite, not the launch trigger itself:

1. `chaosx.nr3.74` - The Ledgers Are Sealed.
2. `chaosx.nr3.75` - No More Peace Delegations.
3. `chaosx.nr3.76` - foreign containment, negotiation, or evacuation responses.
4. `chaosx.nr3.77` - The Sky Is Entered into the Register.
5. `chaosx.nr3.78` - The Last Debate Is Cancelled.
6. `chaosx.nr3.79` - The World Is Marked as a Wound.

Foreign responders can disrupt the final network before or during the world-end branch. During the active branch this fires the Mandala Break super event, records the interruption, clears the active Final Silence flag, and leaves the wider danger as campaign memory. Once Divine Sovereignty is embraced, the player stays on that doctrine path; the former refusal option is not presented in the sovereignty event.

## Reserved Hooks

The Holy Realm reserves clean flags and a global event target for later chains without implementing them:

- `holy_realm_memory_himalayan_unity`
- `holy_realm_memory_himalayan_refusal`
- `holy_realm_memory_snow_line_labs`
- `holy_realm_scripted_strike_network`
- `holy_realm_final_silence_engine`
- `holy_realm_hook_tibetan_expedition_available`
- `holy_realm_hook_mengele_experiment_contact_reserved`
- `holy_realm_hook_malta_crusader_reaction_reserved`
- `holy_realm_hook_teutonic_order_contact_reserved`
- `holy_realm_hook_final_crusade_contrast_reserved`
- `holy_realm_hook_atlantis_betrayal_target_reserved`
- `event_target:holy_realm_country`

No Germany, Mengele, Tibet expedition, Malta Crusader, Teutonic Order, Final Crusade, or Atlantis content is implemented here.

## Achievements

Holy Realm achievements are registered in `common/achievements/chaos_redux_achievements.txt` and localised in `localisation/english/chaosx_achievements_l_english.yml`:

- `29_the_lamps_remain_lit_achievement`: complete the Vow against Annihilation and renounce Final Silence before Chaos reaches `600`.
- `30_mandala_of_nations_achievement`: form the Mandala of Nations and complete its three kindness acts.
- `31_mountain_circle_by_vow_achievement`: complete Himalayan unity peacefully and receive the Himalayan Unity spirit.
- `32_mandate_without_a_sword_achievement`: reach the Buddha Mandate with Compassion Drift below `1` and without arming Final Silence.
- `33_register_without_edges_achievement`: integrate Northern Indian and Eastern Mandala states, then unlock `The World Is Asked to Kneel`.
- `34_empty_mandala_achievement`: complete the Final Silence world-end scenario as the Holy Realm.
- `holy_realm_no_empire_of_the_wheel`: become the Buddha through the clean renunciation route, help defeat chaos, and avoid offensive conquest against normal countries.
- `holy_realm_four_dhyanas_under_fire`: reach Dhyana Depth 4 during a chaos war while the capital is controlled.
- `holy_realm_one_becomes_many`: complete three teaching or relief missions during One Becomes Many, including one under chaos-war pressure.
- `holy_realm_wall_river_sky`: use Passing Through Walls, Walking on Water, and Seated in the Sky in one anti-chaos war and win without normal-country power abuse.
- `holy_realm_empty_seat`: complete non-terminal Final Silence and preserve at least three faction members under the Empty Seat.
- `holy_realm_final_silence_world_end`: complete terminal Final Silence above `1000` chaos without a recent capital sanctuary fall.
- `holy_realm_no_false_buddha`: become the Buddha without an active False Buddha Schism and without crossing the clean Defilements limit after high Bodhi progress.
- `holy_realm_debate_the_pretender`: resolve the False Buddha Schism through debate rather than suppression.
- `holy_realm_sangha_of_nations`: lead at least eight valid non-chaos, non-puppet Sangha members with high cohesion for `180` days.
- `holy_realm_mercy_in_the_ashes`: complete five low-Defilement relief/refugee missions, including a threatened-capital mission.
- `holy_realm_sun_and_moon`: use Touching the Sun and Moon during world collapse with multiple chaos sources or a major-capital chaos source, then win within `365` days.
- `holy_realm_lotus_bridge`: protect a valid Lotus Bridge target capital for `180` days.

## Icons And Assets

Holy Realm-specific sprite names are registered in `interface/003_holy_realm.gfx`, `interface/chaosx_achievements.gfx`, and `interface/chaosx_super_events.gfx`. Report-event, focus, idea, decision category, achievement, and super-event files use their normal Chaos Redux folders.

Leader stage portrait aliases are registered in `interface/chaosx_characters.gfx`. The static fallback portrait DDS files live in `gfx/leaders/THR/`, with source/processed review files and contact sheet under `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/`. The Buddha Mandate stage also has the animated sprite `GFX_portrait_THR_buddha_mandate_animated` backed by `gfx/leaders/THR/portrait_THR_buddha_mandate_animated.dds`, and the Empty Seat aftermath has `GFX_portrait_THR_empty_seat_animated` backed by `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds`.

The Holy Mandala scripted GUI is intentionally compact and attached only to the decision category. It does not replace the focus tree, the balance-of-power screen, or the Bodhisattva mission category.

Imported package asset folders reserved for the later replacement UI:

- `gfx/holy_realm/mandala_panel/`
- `gfx/holy_realm/final_silence_ledger/`
- `gfx/holy_realm/map_overlay_icons/`
- `gfx/holy_realm/leader_portrait_frames/`

Focus icons:

- `GFX_goal_THR_refuge`
- `GFX_goal_THR_bodhisattva`
- `GFX_goal_THR_arhat`
- `GFX_goal_THR_buddha`
- `GFX_goal_THR_diplomacy`
- `GFX_goal_THR_mercy`
- `GFX_goal_THR_pacification`
- `GFX_goal_THR_final`

The remaining Holy Realm focuses intentionally use unique vanilla/generic icons so no two focus icons repeat. If more custom focus icons are desired, the highest-value replacements would be:

- `goal_holy_realm_expansion_letters.dds`: sealed white letter over mountain passes, for the expansion-letter branch.
- `goal_holy_realm_himalayan_mandala.dds`: circular Himalaya/pass mandala, for Bhutan/Nepal/Tibet integration.
- `goal_holy_realm_northern_india.dds`: northern Indian register map with saffron/white ledger marks.
- `goal_holy_realm_western_china.dds`: western Chinese border ledger with pass-road lines.
- `goal_holy_realm_eastern_china.dds`: eastern Chinese register with dense city seals.
- `goal_holy_realm_mandala_of_nations.dds`: peaceful faction seal with white flags and lamps.
- `goal_holy_realm_reactors.dds`: reactor cooling tower wrapped by a prayer wheel, for nuclear preparation.
- `goal_holy_realm_ministry_release.dds`: sealed ministry stamp over black ledger, for late Final Silence preparation. The asset filename keeps the stable internal focus ID while the player-facing name is Ministry of Silence.

Decision category icons:

- `GFX_decision_category_holy_mandala`: `gfx/interface/decisions/holy_realm/decision_category_holy_mandala.dds`
- `GFX_decision_category_final_ledger`: `gfx/interface/decisions/holy_realm/decision_category_final_ledger.dds`
- `GFX_decision_category_holy_doctrine_balance`: vanilla `gfx/interface/decisions/decision_category_generic_political_actions.dds`
- `GFX_holy_realm_mandala_meditation_animated`: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation_animated.dds`
- `GFX_holy_realm_mandala_awakened_animated`: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened_animated.dds`
- `GFX_holy_realm_mandala_final_silence_animated`: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence_animated.dds`
- `GFX_decision_holy_realm_dhyana_seal`: `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal.dds`
- `GFX_decision_holy_realm_dhyana_seal_animated`: `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`
- vanilla `GFX_decision_category_generic_political_actions` for Letters of Peace and Authority
- vanilla `GFX_faction_logo_generic_democratic` for the Mandala of Nations faction logo until custom faction art exists

Balance of power icons:

- `GFX_bop_THR_vow_against_annihilation_side`: currently uses the Holy Realm mercy art.
- `GFX_bop_THR_final_silence_side`: currently uses the Holy Realm final doctrine art.

Useful custom BoP icon replacements:

- `bop_holy_realm_vow_against_annihilation.dds`: white lotus, open hand, or lamp over a sealed nuclear ledger.
- `bop_holy_realm_final_silence.dds`: black ledger, closed mandala, pale launch seal, no gore.
- `decision_category_holy_doctrine_balance.dds`: optional custom split mandala with white vow half and dark sealed-ledger half.

Decision icons:

- Refuge and mercy decisions use vanilla `generic_welfare` and `generic_protection`.
- Arhat administration uses vanilla `generic_colonial_administration`.
- Diplomacy and letters use vanilla `generic_political_discourse` and `generic_political_address`.
- Forced integration uses vanilla `border_war`.
- Staged coring uses vanilla `generic_form_nation` and `generic_nationalism`.
- Final doctrine decisions use vanilla `generic_scorched_earth`.

Idea icons use a separate folder and sprite set, not focus icons. Placeholder DDS files are registered under `gfx/interface/ideas/holy_realm/` until final custom idea art is provided:

- `GFX_idea_holy_realm_refuge`
- `GFX_idea_holy_realm_bodhisattva`
- `GFX_idea_holy_realm_arhat`
- `GFX_idea_holy_realm_buddha`
- `GFX_idea_holy_realm_diplomacy`
- `GFX_idea_holy_realm_mercy`
- `GFX_idea_holy_realm_pacification`
- `GFX_idea_holy_realm_final`

Additional custom idea icons that would improve clarity:

- `idea_holy_realm_himalayan_unity.dds`: three mountain seals joined by one lamp.
- `idea_holy_realm_outer_pass_guardians.dds`: shielded pass road and snow ridge.
- `idea_holy_realm_border_quiet.dds`: closed road gate with an administrative seal.
- `idea_holy_realm_arhat_outer_register.dds`: Arhat ledger and valley stamp.
- `idea_holy_realm_mandala_borders.dds`: border posts inside a mandala ring.
- `idea_holy_realm_mandala_peace_vow.dds`: white flag and vow seal.

Event pictures:

- `GFX_report_event_holy_realm_refuge`
- `GFX_report_event_holy_realm_arhat`
- `GFX_report_event_holy_realm_buddha`
- `GFX_report_event_holy_realm_final_silence`

Achievement icons:

Legacy Holy Realm achievement triplets:

- `29_the_lamps_remain_lit_achievement`
- `30_mandala_of_nations_achievement`
- `31_mountain_circle_by_vow_achievement`
- `32_mandate_without_a_sword_achievement`
- `33_register_without_edges_achievement`
- `34_empty_mandala_achievement`

Buddhahood achievement triplets:

- `holy_realm_no_empire_of_the_wheel`
- `holy_realm_four_dhyanas_under_fire`
- `holy_realm_one_becomes_many`
- `holy_realm_wall_river_sky`
- `holy_realm_empty_seat`
- `holy_realm_final_silence_world_end`
- `holy_realm_no_false_buddha`
- `holy_realm_debate_the_pretender`
- `holy_realm_sangha_of_nations`
- `holy_realm_mercy_in_the_ashes`
- `holy_realm_sun_and_moon`
- `holy_realm_lotus_bridge`

Each achievement uses completed, grey, and not-eligible DDS files in `gfx/achievements/`. Source PNGs, processed PNGs, contact sheets, and final paths for the Buddhahood achievement set are recorded in `docs/assets/003_holy_realm_buddhahood/manifest.md`.

Super-event art:

- `gfx/super_events/super_event_the_buddha_mandate.dds`
  - referenced as `GFX_super_event_buddha_mandate`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_the_final_silence.dds`
  - referenced as `GFX_super_event_final_silence`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_the_final_silence.dds`
  - referenced as `GFX_super_event_final_silence_thermonuclear`
  - registered in `interface/chaosx_super_events.gfx`; currently shares the terminal Final Silence texture
- `gfx/super_events/super_event_the_mandala_breaks.dds`
  - referenced as `GFX_super_event_mandala_breaks`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_divine_sovereignty.dds`
  - referenced as `GFX_super_event_divine_sovereignty`
  - registered in `interface/chaosx_super_events.gfx`; fires when Divine Sovereignty is accepted under high crisis, high Final Silence Pressure, or prior coercive doctrine
- `gfx/super_events/super_event_mandala_of_nations.dds`
  - referenced as `GFX_super_event_mandala_of_nations`
  - registered in `interface/chaosx_super_events.gfx`; fires when the Mandala of Nations is formed
- `gfx/super_events/super_event_powers_of_the_awakened.dds`
  - referenced as `GFX_super_event_powers_of_the_awakened`
  - registered in `interface/chaosx_super_events.gfx`; fires when anti-chaos Buddha powers are first demonstrated

Super-event audio:

- The Buddha Mandate, audio ID `7`:
  - music file: `music/super_event_buddha_mandate.ogg`
  - sound definition: `chaosx_super_event_buddha_mandate_track`
- Final Silence, audio ID `8`:
  - music file: `music/super_event_final_silence.ogg`
  - sound definition: `chaosx_super_event_final_silence_track`
- Thermonuclear Final Silence, audio ID `9`:
  - music file: `music/super_event_final_silence_thermonuclear.ogg`
  - sound definition: `chaosx_super_event_final_silence_thermonuclear_track`
- The Mandala Breaks, audio ID `10`:
  - music file: `music/super_event_mandala_breaks.ogg`
  - sound definition: `chaosx_super_event_mandala_breaks_track`
- Divine Sovereignty, audio ID `11`:
  - music file: `music/super_event_divine_sovereignty.ogg`
  - sound definition: `chaosx_super_event_divine_sovereignty_track`
- Mandala of Nations, audio ID `51`:
  - music file: `music/super_event_mandala_of_nations.ogg`
  - sound definition: `chaosx_super_event_mandala_of_nations_track`
- Powers of the Awakened, audio ID `61`:
  - music file: `music/super_event_powers_of_the_awakened.ogg`
  - sound definition: `chaosx_super_event_powers_of_the_awakened_track`
  - image: `gfx/super_events/super_event_powers_of_the_awakened.dds`
- Audio sources, licenses, durations, and conversion notes are recorded in `docs/super_events/super_event_audio_packages.md`.

Holy Mandala and Final Silence Ledger gameplay values remain in the country, event log, focuses, decisions, and localisation. The live scripted GUI surface is `holy_realm_mandala_category_scripted_gui` attached to `holy_realm_mandala_category`; it uses `holy_realm_mandala_category_container` in `interface/chaosx_decisions.gui` to display the current mandala state, core Buddhahood counters, route text, and clickable tab flags inside the decision category.

The Holy Mandala decision category includes routine actions for high-pass storehouses, relief caravans, civil-register scribes, snow-line signal posts, second refuge registration, Arhat road audits, Mandala border courts, foreign target audits, global final warnings, and internal non-return shelters. These decisions unlock from the existing focus and stage flags, and they move Spiritual Legitimacy, Compassion Drift, Mandala Reach, Final Silence Pressure, local infrastructure, manpower, command resources, or foreign opinion instead of acting as simple flavour buttons.

The Vow and Final Silence Balance of Power includes both Vow-leaning and Final-Silence-leaning choices before the final path is fully open. Guarded Silence Clause and Last-Resort Register provide small early pressure toward Final Silence without arming the final path. Peace decisions move the balance more slowly than before, so repeated doctrine work is needed to dominate the balance instead of one or two routine decisions ending the struggle.

A larger full-screen Mandala panel remains future presentation work. The replacement UI pass should expand the current decision-category GUI under stable sprite and scripted-GUI names rather than disabling it or moving gameplay validation out of the existing decisions.

The three-minute Dhyana Seal mouse-hold concept is implemented as the accepted concentration sequence because the available HOI4 scripted GUI model provides click effects, visibility, scripted properties, and tooltips rather than a reliable continuous held-button timer. The active implementation uses `THR_begin_concentration_sequence`, `THR_hold_intention`, `THR_hold_energy`, `THR_hold_mind`, and `THR_hold_investigation`, with the animated Dhyana Seal icon and meditation Mandala state showing the vow while the timed sequence flags remain active.

Future visual interaction pass:

- Put Spiritual Legitimacy, Compassion Drift, Mandala Reach, and Final Silence Pressure values on individual hoverable bars with threshold markers at 45/55/60/65/70/75/90.
- Make the doctrine balance a central Vow-versus-Final-Silence slider with clickable decision buttons directly under each side.
- Make Bodhisattva bhumi progression a ten-step vertical ladder; each step should reveal its Sanskrit name, current leader trait, next mission, and active country modifier.
- Use map overlay icons for states under peace-letter demand, refused letters, Arhat administration, staged integration, and Final Silence marking.
- Show recent value changes as short ledger rows so players can see which focus, decision, or teaching event moved a value.
- Let doctrine memory slots display the most important hidden choices: open refuge, false attainment response, peace letters accepted/refused, vow chosen, sealed ledger read, or Final Silence armed.

Remaining clean asset needs:

- dedicated thermonuclear Final Silence super-event art if the shared terminal Final Silence texture should be split later
- Vow against Annihilation capstone super-event art if that optional spec super event is implemented later
- final custom report-event pictures if the current Holy Realm report-event DDS files are only temporary art
- dedicated custom balance-of-power icons for the Vow, Final Silence, and doctrine-balance category if the current Holy Realm art should be replaced

## Failure And Off-Ramps

- Formation can be refused by leaving the monasteries outside government or restricting the gatherings.
- Refuge policy can reduce legitimacy or increase later pressure depending on open, registered, or closed roads.
- Arhat investigations and false-attainment reviews reduce drift and affect final-event memory.
- The Renunciation and Mercy path sets `holy_realm_final_doctrine_renounced` and blocks Final Silence.
- Foreign disruption can reduce pressure before launch or break the Mandala during the active world-end sequence.
