# The Holy Realm

## Overview

The Holy Realm is event ID 3 and remains registered as a fire-once Chaos Redux event. It transforms Tibet into a full country path rather than a short event chain; if Tibet no longer exists, Bhutan or Nepal can serve as the Himalayan fallback host. If none of those countries exists as a valid normal country, the event is unavailable and displays as N/A in the event list. The route starts as a mountain refuge, becomes a Bodhisattva-led state, creates the Arhat Administration, reaches the Buddha Mandate, and then commits to one of two main branch identities: Peaceful Holy Realm or Final Silence Holy Realm. Expansionism is a separate optional tree with its own pressure, letter, war-goal, and integration tools, not a third main-branch identity.

The current player-facing surface is the Holy Realm focus tree, decision categories, the compact Holy Mandala decision-category summary, the dedicated Bodhisattva category, the built-in Vow and Final Silence balance of power, event choices, event log entries, super events, national spirits, achievements, and localisation. The four Holy Realm values are live country variables and drive focuses, decisions, AI, final warning logic, and event text:

- Spiritual Legitimacy
- Compassion Drift
- Mandala Reach
- Final Silence Pressure

## Flow

1. `chaosx.nr3.1` redirects the event to Tibet if possible. If Tibet no longer exists, it can redirect only to Bhutan or Nepal. If none of those tags exists as a valid normal country, event selection treats the event as unavailable.
2. `chaosx.nr3.2` offers the spec formation choices: leave the monastery outside government, invite the figure into government, restrict the gatherings, or proclaim the mandate immediately.
3. A formed Realm sets cosmetic tag `THR`, loads `THR_focus`, initializes counters, adds immediate Holy Realm cores on Bhutan and Nepal, records the refuge evolution, opens decisions, and broadcasts an ambiguous refuge news item.
4. Refuge policy is remembered through `chaosx.nr3.4`: open roads, register names, or close passes.
5. Bhutan, Nepal, and Tibet can receive a Himalayan unity invitation through `chaosx.nr3.3`.
6. The focus tree drives the major stages. Evolutions are gates: they record that a spiritual or political stage has been reached, unlock the next focus path, and alter later text and AI willingness. Heavy mechanics are attached to focuses, decisions, and event choices inside those paths rather than to the evolution setter itself.
   - `THR_bodhisattva_accepts_seal` fires the Bodhisattva stage.
   - `THR_arhats_take_office` creates the Arhat Administration.
   - `THR_buddha_mandate` fires the Buddha Mandate super event.
   - `THR_throne_without_body` and `THR_doctrine_last_war` open Divine Sovereignty and the locked final doctrine path.
   - `THR_final_silence` can start the world-end branch only when all hard gates pass.
7. Chaos thresholds shape the route and are shown with exact values in focus tooltips. Low-chaos focuses require the Chaos Meter below `250`, `400`, or `600` depending on route tone. Interventionist, coercive, and final doctrine preparation focuses require the Chaos Meter above `400`, `600`, or `800`. Only the actual Final Silence launch requires `1000`.
8. The expansionist tree starts separately with `THR_complete_himalayan_mandala` and `THR_guardians_outer_passes`, then opens through `THR_letters_beyond_passes` without excluding the peaceful or Final Silence main branch. `THR_mandala_receives_borderlands`, `THR_high_pass_states_enter_mandala`, `THR_roads_must_be_quiet`, `THR_outer_valleys_register`, `THR_mandala_borders`, `THR_peace_by_submission`, `THR_northern_indian_register`, `THR_northern_indian_state_registers`, `THR_eastern_mandala`, `THR_western_chinese_registers`, `THR_eastern_chinese_registers`, and the high-chaos `THR_world_is_a_border` unlock peace letters, refusal war goals, Arhat administration, and direct progressive regional cores rather than generic bonuses.
9. Arhat events cover empowered administration, constrained ledgers, village silence, false attainment, inquiries, removals, and expanded methods.
10. Doctrine branches cover restraint, peacekeeping, coercive pacification, Divine Sovereignty, Renunciation, and Final Silence.
11. Decisions provide Arhat oversight, refugee policy, diplomacy, doctrine selection, conquest-route border tools, final warning behavior, Mandala Break disruption, and foreign containment responses.
12. `holy_realm_final_doctrine_balance` initializes at formation and attaches `holy_realm_doctrine_balance_category` to the balance-of-power screen. It represents the struggle between the Vow against Annihilation and Final Silence. Final Silence influence adds a small daily Final Silence Pressure tick; Vow influence lowers pressure.

## System Integration

The Holy Realm extends existing Chaos Redux systems rather than creating parallel ones:

- Chaos Meter: early refuge, mercy, mediation, restrained Arhat, and renunciation content can reduce chaos modestly through `add_chaos_meter_value`; administrative control, coercive pacification, Divine Sovereignty, final warnings, Mandala Break, and Final Silence raise chaos. Stage unlock effects do not add chaos by themselves.
- Evolutions: milestones record to the shared event-log evolution pipeline as evolution type `3` and act as focus-path gates. If a Holy Realm evolution is disabled from the event-details UI, the matching focus path is treated as unlocked without requiring that stage log.
- Focus tags: every Holy Realm focus has a `# THR FOCUS TAGS:` comment with area, tone, chaos requirement, system, and path-role metadata for audits. The focus tree also exposes custom sorting filters for Holy Realm Peace, Final Silence Pressure, and Mandala Integration. The custom filters follow gameplay role rather than raw tag presence: peaceful refuge, restraint, diplomacy, and defensive preparation appear under Holy Realm Peace; focuses that alter or gate the Final Silence pressure system appear under Final Silence Pressure; territorial register, conquest, and coring focuses appear under Mandala Integration.
- Event logs: event ID 3 has a dedicated event-detail description and six Holy Realm evolution preview entries covering Mountain Refuge, Bodhisattva, Arhat Administration, Buddha Mandate, Divine Sovereignty, and Final Doctrine path gates. The evolution list row shows the short evolution name and chaos tier; the detailed panes keep the evolution stage.
- Super events: values `7`, `8`, `9`, `10`, `11`, and `51` display Buddha Mandate, Final Silence, thermonuclear Final Silence, Mandala Breaks, Divine Sovereignty, and Mandala of Nations.
- World-end scenarios: Final Silence sets `world_end` and `world_end_final_silence`; interruption sets `world_end_final_silence_interrupted` and clears the active world-end flag.
- Settings: Final Silence is blocked by `world_end_disabled`.
- Triggerable scenarios: the scenario window can start Final Silence directly from the current player country as either the normal nuclear payload or the thermonuclear payload. This bypasses the standard Holy Realm launch gates but uses the same `holy_realm_prepare_final_silence`, strike-wave, fallout, deaths, wasteland, super-event, and follow-up wave logic.
- Multiplayer behavior: human countries receive ambiguous observation events around the Buddha Mandate and direct warnings only when the final doctrine is armed.
- Condemnation: Final Silence adds unconventional-warfare condemnation and applies existing diplomatic consequences.
- Deaths: Final Silence uses the shared `chaos_meter_register_state_civilian_deaths_percent` pipeline with the dedicated `chaos_meter_deaths_reason.final_silence` cause. The normal launch kills `90%` of each struck non-Realm state's current population with a high billion-scale cap; the thermonuclear variant kills `97%`.
- Air cleanliness: Final Silence applies air contamination unless the air cleanliness setting is disabled.
- Nuclear and wasteland logic: Final Silence resolves in regional strike waves: Asia and the Middle East, Europe and Africa, the Americas, then Oceania plus any remaining valid states. Each wave uses `launch_nuke` with `use_nuke = no` for the struck states so the visual nuclear effect appears, applies fallout, removes state buildings, sets the state category to `wasteland`, and marks struck/burning/wasteland/silent state flags. State flags prevent duplicate population/death processing. Holy Realm states are not struck, but they receive fallout from the global launch sequence.
- World threats: Divine Sovereignty, final warnings, and armed doctrine can set `world_threat_source_holy_realm`; the early refuge and Buddha Mandate are not treated as existential threats by themselves.
- AI: peaceful Holy Realm strategies prioritize defense, infrastructure, legitimacy, and low-chaos paths. Expansionist AI sends letters and pressures weak neighbors only after the separate expansion tree is opened, with forced integration weighted toward strong, prepared, high-chaos states. Final Silence AI remains locked behind late high-chaos, industry, doctrine, year, and warning gates.
- Mandala of Nations: `THR_mandala_of_nations` creates the `faction_template_holy_realm_mandala_of_nations` faction, sets peaceful faction rules, adds goals, applies the Mandala Peace Vow to members, and reduces chaos when countries join. Members receive a `can_not_declare_war` rule while inside the faction, so the peaceful coalition cannot declare offensive wars.
- Doctrine balance: the built-in balance of power uses `common/bop/003_holy_realm_bop.txt`, with Vow and Final Silence sides. It gives range modifiers, stores current doctrine pressure flags, and is moved by decisions, focuses, and teaching events. Final Silence launch now requires the Final Silence side to dominate the balance.
- Bodhisattva bhumi system: `holy_realm_advance_bodhisattva_bhumi` advances up to ten bhumis, refreshes the leader portrait, and swaps leader traits through `holy_realm_bodhisattva_pramudita`, `holy_realm_bodhisattva_vimala`, `holy_realm_bodhisattva_acala`, and `holy_realm_bodhisattva_dharmamegha`.

## Interactive Values

The Holy Mandala category uses a compact scripted GUI instead of a separate dashboard. It shows the three core values, Bodhisattva bhumi, colored Chaos value, and Final Silence Pressure without adding a duplicate title or direct warning labels. The detailed mechanics are hoverable read-only value rows:

- `THR_status_spiritual_legitimacy` explains how Spiritual Legitimacy affects stage text, peaceful AI, Arhat legitimacy, and non-final authority.
- `THR_status_compassion_drift` explains mercy versus coercive drift, event text changes, dangerous AI willingness, and final pressure interactions.
- `THR_status_mandala_reach` explains diplomacy, peace letters, regional integration, Chinese registers, and Ministry of Silence reach gates.
- `THR_status_sealed_ledger` displays Final Silence Pressure, the `45/55/65/75` preparation thresholds, and the hard launch gates.

These rows are intentionally unavailable decisions so players can hover them without accidentally firing effects.

Routine value growth has diminishing returns. Positive Spiritual Legitimacy, Mandala Reach, and Final Silence Pressure gains are halved above `70` and halved again above `90`. Compassion Drift slows in either extreme above `70` and `90`. Routine actions remain useful, but the last value tiers need major focuses, missions, accepted submissions, doctrine commitments, or final-preparation choices.

## Focus Tree Balance

Early identity and refuge focuses use short costs so the Realm becomes active quickly. Mountain Refuge, Bodhisattva government, refugee shelter, guarded passes, and the Seal of Refuge now provide large stability, political organization, protected manpower, infrastructure, supply, bunkers, and legitimacy without early villain framing. Peaceful Himalayan unity adds `holy_realm_himalayan_unity`; forced cleanup through `THR_complete_himalayan_mandala` instead adds Mandala Reach and Compassion Drift memory.

Arhat Administration and Buddha Mandate are mid-game power spikes. They unlock stronger administration, compliance and construction tools, Arhat oversight, Mandala diplomacy, the Mandala Bureau intelligence agency, military organization, doctrine branches, faster industry, stronger vow-keeper forces, and accelerated nuclear preparation if the player later enters the final doctrine route. The expansion route adds strong regional tools but carries Compassion Drift, foreign suspicion, refusal records, and high-chaos locks rather than free world conquest. Acceptance of letters is intentionally rare; major powers and faction members cannot accept.

The Mandala of Nations is the peaceful faction route. Its goals are completed through decision-based acts of kindness:

- `THR_mandala_open_refuge_corridors`
- `THR_mandala_white_flag_congress`
- `THR_mandala_open_granaries`

Each act reduces chaos modestly and completes a visible faction goal that adds faction initiative and power projection. Additional countries joining the Mandala of Nations reduce chaos once per country.

After formation, the same decision category opens active Mandala work:

- `THR_mandala_arbitration_letters` targets a country at war and starts `chaosx.nr3.125`; one enemy receives `chaosx.nr3.126` only if the first side accepts. White peace fires only when both sides accept while still at war.
- `THR_mandala_observer_mission` targets a country at war, sets a target cooldown, improves relations, and records Mandala observer work.
- `THR_mandala_development_mission` targets poor, rural, underdeveloped, or war-affected African, South American, and Asian countries and repairs one eligible controlled state with infrastructure, possible civilian industry, and resistance/compliance recovery.
- `THR_stand_between_armies` sends one limited Mandala Peacekeeping Brigade to eligible minor democratic defenders, with yearly target cooldowns and manpower/equipment costs. After `Shelter the Exiles`, faction members can also receive this support.

The Vow and Final Silence balance of power adds a second late-game management surface. It includes Political Power decisions for public vows, mercy councils, Bodhisattva council missions, lamp processions, lotus audits, outer-monastery reconciliation, sealed-name releases, sealed ledger readings, launch ledger sealing, silence-cell expansion, black ledger drills, silent transit codes, the Nuclear Sutra Committee, Last-Pass Watch, the White Mandala Oath, and the Empty Mandala Session. These decisions move the doctrine balance, alter Final Silence Pressure, alter Compassion Drift or Spiritual Legitimacy, and in some cases reduce or increase Chaos. The daily pulse is intentionally small so the balance creates pressure over time without replacing focus and decision choices.

Expansion coring is progressive and direct:

- `THR_high_pass_states_enter_mandala` adds Holy Realm cores on Tibet, Bhutan, Nepal, and Kham/Chamdo states.
- `THR_northern_indian_state_registers` adds Holy Realm cores on the northern Indian register states after the northern Indian claim focus.
- `THR_western_chinese_registers` adds Holy Realm cores on western Chinese register states after the Eastern Mandala opens.
- `THR_eastern_chinese_registers` adds Holy Realm cores on eastern Chinese register states only under extreme chaos and high Mandala Reach.

Expansion decisions live in `holy_realm_expansion_category` after `THR_letters_beyond_passes`:

- `THR_send_peace_letter` targets eligible neighbors or countries bordering Holy Realm subjects.
- `THR_prepare_forced_integration` grants a war goal only after refusal.
- `THR_administer_submitted_territory` raises compliance and lowers resistance in submitted or registered states.
- `THR_integrate_himalayan_mandala_state`, `THR_integrate_northern_indian_register_state`, and `THR_integrate_eastern_mandala_state` add state-by-state cores only after ownership, control, Mandala Reach, Arhat administration, and region unlock conditions are met.
- `THR_mandate_kneeling_province` is unlocked by `THR_world_is_a_border` and cores claimed, controlled, non-core states one province at a time after the Realm has forced the world into its register.

## Final Silence Conditions

Final Silence uses strict standard conditions:

- the Holy Realm exists and is the acting country
- the Holy Realm is sovereign
- the Final Silence stage has been reached through the locked focus path
- the Ministry of Silence has armed the final infrastructure; preparation focuses can be completed once the `800` chaos final-doctrine threshold is met
- the final doctrine is armed and not renounced
- the final warning chain has reached `The World Is Marked as a Wound`
- the date is later than 1944.12.31
- Chaos Meter is above `1000` for launch
- the Holy Realm has more factories than every other country and at least the tuned minimum factory count
- nuclear or scripted strike capability exists, including the HOI4 stockpile cap of `999` nuclear weapons
- Final Silence dominates the Vow and Final Silence balance of power
- `world_end` is not already active
- `world_end_disabled` is not set

If the date is later than 1946.12.31, thermonuclear technology or doctrine exists, the shared nuclear stockpile is at `999`, and `holy_realm_thermonuclear_payloads_prepared` is above `99`, the thermonuclear variant is used. The focus path grants `990` normal nukes and `100` thermonuclear payloads when the technology exists, forcing the Holy Realm to produce at least `9` normal nukes itself. The variant applies larger air damage, higher death percentages, stronger fallout, a separate global flag, super-event image ID `9`, and a distinct thermonuclear Final Silence audio track through audio ID `9`.

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

## Icons And Assets

Holy Realm-specific sprite names are registered in `interface/003_holy_realm.gfx`, `interface/chaosx_achievements.gfx`, and `interface/chaosx_super_events.gfx`. Report-event, focus, idea, decision category, achievement, and super-event files use their normal Chaos Redux folders.

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

- `29_the_lamps_remain_lit_achievement`
- `30_mandala_of_nations_achievement`
- `31_mountain_circle_by_vow_achievement`
- `32_mandate_without_a_sword_achievement`
- `33_register_without_edges_achievement`
- `34_empty_mandala_achievement`

These use complete placeholder DDS triplets in `gfx/achievements/` until final achievement art is supplied.

Super-event art:

- `gfx/super_events/super_event_the_buddha_mandate.dds`
  - referenced as `GFX_super_event_buddha_mandate`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_the_final_silence.dds`
  - referenced as `GFX_super_event_final_silence`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_the_final_silence.dds`
  - referenced as `GFX_super_event_final_silence_thermonuclear`
  - registered in `interface/chaosx_super_events.gfx`; a dedicated thermonuclear super-event image is still needed
- `gfx/super_events/super_event_the_mandala_breaks.dds`
  - referenced as `GFX_super_event_mandala_breaks`
  - registered in `interface/chaosx_super_events.gfx`
- `gfx/super_events/super_event_divine_sovereignty.dds`
  - referenced as `GFX_super_event_divine_sovereignty`
  - registered in `interface/chaosx_super_events.gfx`; fires when Divine Sovereignty is accepted under high crisis, high Final Silence Pressure, or prior coercive doctrine
- `gfx/super_events/super_event_mandala_of_nations.dds`
  - referenced as `GFX_super_event_mandala_of_nations`
  - registered in `interface/chaosx_super_events.gfx`; fires when the Mandala of Nations is formed

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
- Audio sources, licenses, durations, and conversion notes are recorded in `docs/super_events/super_event_audio_packages.md`.

Holy Mandala and Final Silence Ledger gameplay values remain in the country, event log, focuses, decisions, and localisation. The scripted GUI surface is disabled for now, so the player sees the Holy Realm through focus tree, decisions, events, super events, national spirits, achievements, and event log entries until the replacement UI is implemented.

The Holy Mandala decision category includes routine actions for high-pass storehouses, relief caravans, civil-register scribes, snow-line signal posts, second refuge registration, Arhat road audits, Mandala border courts, foreign target audits, global final warnings, and internal non-return shelters. These decisions unlock from the existing focus and stage flags, and they move Spiritual Legitimacy, Compassion Drift, Mandala Reach, Final Silence Pressure, local infrastructure, manpower, command resources, or foreign opinion instead of acting as simple flavour buttons.

The Vow and Final Silence Balance of Power includes both Vow-leaning and Final-Silence-leaning choices before the final path is fully open. Guarded Silence Clause and Last-Resort Register provide small early pressure toward Final Silence without arming the final path. Peace decisions move the balance more slowly than before, so repeated doctrine work is needed to dominate the balance instead of one or two routine decisions ending the struggle.

The former Mandala Panel package paths are not loaded while the scripted GUI is disabled. Use the replacement UI pass to reintroduce those assets under stable names after the new design is provided.

Future visual interaction pass:

- Put Spiritual Legitimacy, Compassion Drift, Mandala Reach, and Final Silence Pressure values on individual hoverable bars with threshold markers at 45/55/60/65/70/75/90.
- Make the doctrine balance a central Vow-versus-Final-Silence slider with clickable decision buttons directly under each side.
- Make Bodhisattva bhumi progression a ten-step vertical ladder; each step should reveal its Sanskrit name, current leader trait, next mission, and active country modifier.
- Use map overlay icons for states under peace-letter demand, refused letters, Arhat administration, staged integration, and Final Silence marking.
- Show recent value changes as short ledger rows so players can see which focus, decision, or teaching event moved a value.
- Let doctrine memory slots display the most important hidden choices: open refuge, false attainment response, peace letters accepted/refused, vow chosen, sealed ledger read, or Final Silence armed.

Remaining clean asset needs:

- final achievement icons for `29_the_lamps_remain_lit_achievement`, `30_mandala_of_nations_achievement`, `31_mountain_circle_by_vow_achievement`, `32_mandate_without_a_sword_achievement`, `33_register_without_edges_achievement`, and `34_empty_mandala_achievement`
- dedicated thermonuclear Final Silence super-event art, currently routed through the normal Final Silence sprite name because no separate DDS exists yet
- Vow against Annihilation capstone super-event art if that optional spec super event is implemented later
- stage-composited leader portraits for Bodhisattva, Buddha Mandate, Divine Sovereignty, Final Silence, and Mandala Break if the actual country leader portrait should change in the politics view
- final custom report-event pictures if the current Holy Realm report-event DDS files are only temporary art
- dedicated custom balance-of-power icons for the Vow, Final Silence, and doctrine-balance category if the current Holy Realm art should be replaced

## Failure And Off-Ramps

- Formation can be refused by leaving the monasteries outside government or restricting the gatherings.
- Refuge policy can reduce legitimacy or increase later pressure depending on open, registered, or closed roads.
- Arhat investigations and false-attainment reviews reduce drift and affect final-event memory.
- The Renunciation and Mercy path sets `holy_realm_final_doctrine_renounced` and blocks Final Silence.
- Foreign disruption can reduce pressure before launch or break the Mandala during the active world-end sequence.
