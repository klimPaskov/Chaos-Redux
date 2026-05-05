# Mengele and Tibet Expedition

## Overview

The Mengele and Tibet Expedition content is a Germany gameplay chain, not a Chaos Redux random-event pool entry. It is implemented in `events/germany_mengele.txt` with the `germany_mengele.*` namespace and starts from normal HOI4 event triggers when fascist Germany controls Auschwitz after 1940.06.13.

The system has three connected layers:

1. The Auschwitz Experiments authorization chain.
2. The hidden Mengele autonomy and Angel of Death civil war branch.
3. The Final Solution decision layer and Tibet Expedition branch.

These layers share variables, flags, condemnation, chaos-meter history, deaths-system calls, world-threat state, foreign reactions, Holy Realm hooks, and later-branch flags.

## Core Flow

`germany_mengele.1` fires for fascist Germany once Auschwitz is controlled. Auschwitz is the shared Kielce-state node used elsewhere in the mod: state `88`, province `9412`. Germany can authorize the Auschwitz Experiments, restrict the file to camp administration, or shut it down.

Full authorization gives the timed `germany_auschwitz_experiments` national spirit for two years, sets `mengele_permission_level` to full authority, increases hidden `mengele_autonomy`, marks Auschwitz as an experiment-linked atrocity site, records condemnation memory, raises chaos slightly, and schedules the report chain. After the spirit expires, the program keeps a short `germany_mengele_program_recently_expired` window for coup eligibility, then closes through `germany_mengele_expire_program` if no coup has fired. Restriction gives a smaller timed spirit, marks Auschwitz as restricted experiment evidence, and sets permission to restricted. Rejection, closure, or expiry set permission back to rejected.

The report chain uses:

- `germany_mengele.10` Reports Without Names
- `germany_mengele.11` The Twin Registers
- `germany_mengele.12` A Laboratory Without Berlin
- `germany_mengele.13` The Children Do Not Answer to Guards
- `germany_mengele.14` Warnings from Auschwitz

Each report can increase or reduce `mengele_autonomy`, affect SS archive control, add experiment deaths, and push chaos or condemnation memory.

## Permission Levels

`mengele_permission_level` is the hidden permission scale that connects the Auschwitz chain to the genocide system:

- `0`: rejected or closed program
- `1`: restricted camp administration
- `2`: limited experimental authority from record-classification decisions
- `3`: full Auschwitz Experiments authorization
- `4`: SS laboratories bypassing state and military oversight

Higher permission levels increase experiment deaths, hidden atrocity score, discovery condemnation, coup pressure, and the number of laboratory units spawned if the Directorate appears. Bypass permission is reached by rewarding abnormal laboratory results, hiding the child-guard warning, silencing dissenting files, or accepting new facility demands.

## Facility Demands

When coup pressure is above the warning threshold and the demand is not on cooldown, `germany_mengele.17` can fire. Accepting instantly adds one `biowarfare_facility` to a suitable controlled state, preferring Auschwitz/Kielce (`88`, province `9412`), then Krakow (`89`, province `11411`), Brandenburg (`64`, province `3499`), and Sud-Hannover (`60`, province `3561`). Acceptance raises autonomy, condemnation, chaos, and permission to bypass. It also rolls for early completion of one normally gated biological special project, including the weaponized zombie project. Refusal reduces autonomy and costs political power.

## Angel of Death Coup

The coup monitor `germany_mengele.20` runs only after the full program is active. It recalculates coup pressure from:

- `mengele_autonomy`
- controlled biowarfare facilities
- `mengele_permission_level`
- war with the Soviet Union
- fascist popularity
- high chaos tier
- desperate war state

The coup requires 1943 or later, fascist Germany, war with the Soviet Union, high fascist support, at least three controlled biowarfare facilities, and pressure above the configured threshold.

When the coup fires, `germany_mengele_start_coup` stores loyalist Germany as `germany_mengele_loyalist`, starts a fascist civil war, and stores the breakaway as `germany_mengele_faction`. The breakaway state receives Auschwitz, controlled biowarfare-facility states, Josef Mengele as leader, the `germany_mengele_directorate` cosmetic tag, laboratory-state ideas, cloning manpower, and Experimental Twin Formation units. Loyalist Germany receives the response event and decisions to crush the Directorate, reclaim results, or make a temporary truce if the Soviet war is desperate.

The Directorate remains a world-threat source while the civil war is active through `world_threat_source_mengele`. If it wins, it annexes loyalist Germany and changes from `germany_mengele_directorate` to the consolidated `germany_mengele_angelic_directorate` cosmetic tag.

If an enemy captures an Auschwitz-linked site or biological facility while Germany has high autonomy and controlled laboratory territory remains, the genocide state-control hook can trigger `germany_mengele.22`. This starts the laboratory revolt as an emergency response to the invader. The Directorate declares on the invader first, then `germany_mengele.38` waits until it is at peace before declaring on loyalist Germany.

## Deaths, Condemnation, and Chaos

Experiment deaths are recorded through `chaos_meter_register_deaths` in Auschwitz state scope. Report deaths use squared hidden autonomy, facility count, permission level, and an Auschwitz-site bonus, then clamp to a hard cap so late-stage autonomy escalates sharply without breaking the deaths system. Coup deaths are recorded in Auschwitz and biowarfare-facility states through `chaos_meter_register_state_civilian_deaths_percent`.

The chain adds dedicated chaos-meter history reasons:

- `mengele_authorization`
- `mengele_reports`
- `mengele_coup`
- `mengele_purge`
- `mengele_truce`
- `mengele_victory`
- `tibet_claim`
- `tibet_scandal`

Condemnation uses the existing chemical/biological condemnation variable and diplomatic consequence effect.

## Final Solution Decision Layer

The `germany_final_solution_category` decision category appears for fascist Germany from 1938 onward. It tracks:

- `racial_policy_radicalization`
- `ss_archive_control`
- `ahnenerbe_influence`
- `foreign_atrocity_awareness`
- `aryan_origin_preparation`

The decisions do not require the Auschwitz program. They can prepare the Tibet Expedition independently while still interacting with Mengele autonomy when SS offices are strengthened.

Implemented decisions:

- `centralize_race_offices`
- `expand_ss_archive`
- `classify_eastern_records`
- `protect_ahnenerbe_budget`
- `search_ancestral_traces`
- `silence_dissenting_file`
- `close_auschwitz_program`
- `military_review_of_auschwitz`
- `purge_ss_medical_offices`

## Tibet Expedition

Once `aryan_origin_preparation` is high enough, Germany can use `prepare_tibet_mission` in `germany_tibet_expedition_category`.

The expedition begins with `germany_mengele.40` and can take three routes:

- scientific cover
- covert SS mission
- Holy Realm contact

Progress events cover transit papers, scientific cover, mountain interpreters, and the symbol problem. The result system can produce no result, ambiguous result, fabricated positive result, Holy Realm interpreted confirmation, scandal, or mission loss.

The output flags are deliberately phrased as regime claims:

- `germany_aryan_origin_claim_prepared`
- `germany_master_race_claim_established`
- `germany_holy_realm_contact_positive`
- `holy_realm_german_origin_claim_contact`

These flags mean German institutions believe or manufacture a racial-origin claim. They do not mean the claim is true, and they do not mean the Holy Realm agrees with Nazi ideology.

If the Mengele coup happens during an active expedition, the mission is compromised, exposure rises, and the result resolves early. If the Directorate wins, `germany_master_race_claim_established` is granted automatically.

When the master-race claim exists and the Directorate is active or victorious, `germany_mengele_perfect_aryan_formations` is applied. This represents the Directorate treating its own manufactured claim as command doctrine; it strengthens laboratory formations but increases instability and political cost. There is also a chance that those formations overthrow Mengele, replacing his leader portrait with `GFX_portrait_GER_perfect_aryan` and firing `germany_mengele.37`.

If Germany stops being fascist while the expedition is active, `germany_tibet_cancel_expedition` closes the mission, blocks the active chain, resets expedition preparation, reduces Ahnenerbe influence, and clears expedition origin/contact targets. If ideology changes during preparation, `germany_tibet_cancel_preparation` blocks the mission before it starts. Delayed expedition progress events expose only a closed-file option after that cleanup.

## Holy Realm Interaction

The expedition checks the existing Holy Realm triggers:

- refuge or Bodhisattva stage gives weak or ambiguous contact pressure
- Arhat Administration gives a strong positive-interpretation path
- Buddha Mandate guarantees the internal claim route
- Divine Sovereignty gives the strongest claim pressure
- Final Silence turns the route dangerous and can cause mission loss

Holy Realm contact can add `holy_realm_german_origin_claim_contact` and a small Mandala Reach increase when the Holy Realm is used as the interpreted confirmation.

## Foreign Reactions

The coup broadcasts targeted reactions:

- Soviet Union receives a condemnation event.
- Democratic majors receive an intelligence/condemnation event.
- German fascist allies receive a distancing event.
- Neutral majors receive rumor-driven embassy reports.
- Holy Realm receives a contact event if approached during the expedition.

Opinion modifiers are defined in `common/opinion_modifiers/germany_mengele_opinion_modifiers.txt`. Foreign reaction ideas are defined in `common/ideas/germany_mengele_ideas.txt`: `mengele_soviet_no_surrender`, `mengele_allied_intelligence_focus`, `mengele_fascist_ally_distancing`, and `mengele_neutral_embassy_alarm`.

## Files

Gameplay:

- `events/germany_mengele.txt`
- `common/script_constants/germany_mengele_constants.txt`
- `common/scripted_triggers/germany_mengele_triggers.txt`
- `common/scripted_effects/germany_mengele_effects.txt`
- `common/decisions/germany_mengele_decisions.txt`
- `common/decisions/categories/germany_mengele_categories.txt`
- `common/ideas/germany_mengele_ideas.txt`
- `common/country_leader/germany_mengele_leader_traits.txt`
- `common/opinion_modifiers/germany_mengele_opinion_modifiers.txt`
- `common/ai_strategy/germany_mengele_ai_strategy.txt`
- `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds`

Integration:

- `common/script_constants/chaos_meter_constants.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`
- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_triggers/chaosx_world_threat_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `interface/chaosx_pictures.gfx`
- `interface/chaosx_super_events.gfx`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `localisation/english/germany_mengele_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Assets

Registered event picture:

- `GFX_report_event_tibet`
- referenced in `interface/chaosx_pictures.gfx`
- uses existing `gfx/event_pictures/report_event_lhasa.dds`

Registered super-event image:

- `GFX_super_event_angel_directorate`
- referenced in `interface/chaosx_super_events.gfx`
- file path: `gfx/super_events/super_event_angel_directorate.dds`

The super-event image is registered under the final filename and currently contains the default super-event art so the game has no missing sprite. Replace that DDS with final art under the same filename.

Registered leader portrait:

- `GFX_portrait_GER_perfect_aryan`
- referenced in `interface/_scientists_portraits.gfx`
- file path: `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds`

The portrait uses a vanilla German officer portrait copied into `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds`. Dedicated final portrait art can replace that file in place; the GFX name and code references should remain unchanged.

## Future Plans

- Add a custom dossier scripted GUI if the decision categories need visible meters for autonomy, SS archive control, Ahnenerbe influence, and expedition exposure.
- Add later Teutonic Order, Blessed Hitler, Final Crusade, and Atlantis chains that consume `germany_master_race_claim_established` without treating the claim as true.
- Add targeted sabotage or bombing decisions against Directorate biowarfare facilities if Allied intelligence mechanics need a larger gameplay response.
- Add post-regime investigation events for non-fascist Germany after the program collapses.
