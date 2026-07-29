# Event 013 Natural Disasters, implementation readiness ledger

> Implementation disposition, 2026-07-10: this ledger remains the acceptance checklist. The live implementation and final audit evidence are recorded outside the source specification in `docs/events/013_natural_disasters/overview.md` and `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md`.

This ledger turns the expanded planning package into a practical completion gate. It does not add new mechanics. It names what the coding pass must implement, which source files anchor the requirement, what simplification is forbidden, and what evidence should exist before completion is claimed.

## Core system gates

| Surface | Anchor files | Must exist in implementation | Forbidden simplification | Meaningful completion evidence |
| --- | --- | --- | --- | --- |
| Event 013 source identity | Part 1, Part 5 | Fresh Event 013 chain with repeatable selection, delayed subevents, and one history row per Event 013 firing. | Logging every disaster subevent as a separate Event 013 history entry. | Manual test or scripted trace showing one sequence with multiple impacts and one Event 013 history row. |
| Dynamic call contract | Part 2, disaster call matrix | Reusable callable disaster entry point with family, random family, country, state, region, severity, report, news, aftermath, chain, death, and damage parameters. | Copying family logic into external events or creating one-off callers for gods, sandstorms, or scenarios. | At least two distinct call sites using the same helper path, one normal random firing and one external or manual call. |
| Target selection | Part 2, family mini-specs | Target scoring that respects family geography, density, infrastructure, current damage, local climate direction, coastal status, volcanic or seismic suitability, and invalid target skips. | Pure random global state selection for every family. | Debug or review notes showing family-specific target filters and invalid target behavior. |
| Delayed sequencing | Part 1, Part 2, Part 5 | Baseline and evolved seasons schedule impacts with delay bands, with shorter spacing only when the sequence intentionally intensifies. | Same-day pileups for ordinary baseline multi-disaster sequences. | Test sequence or script evidence showing staged delay, affected reports after impact, and no normal same-day spam. |
| Deaths-system integration | Part 1, Part 2, Part 7, family mini-specs | Disaster deaths reduce population through the shared deaths system with density, severity, infrastructure, supply, stability, vulnerability, and chain factors. | Tiny flavour deaths, fixed death values, or deaths only represented by national spirits. | Review of death call path and several family examples showing baseline, Evolution II, and Evolution III scaling. |
| Building and supply damage | Part 2, Part 3, Part 8 | Family-specific damage to infrastructure, factories, ports, airfields, rail, supply, and state modifiers when appropriate. | One generic damaged state modifier with no family identity. | Family damage table or script review proving distinct effects for seismic, water, wind, fire, heat, cold, ash, meteor, and moving systems. |
| News throttle | Part 2, news matrix, Part 7 | News appears for early meaningful disasters, later large, strange, cascading, or global disasters, with throttling to avoid spam. | Generic news for every small disaster or no specific disaster news at all. | News eligibility review showing family, severity, evolution, and cooldown gates. |
| Affected-country reports | Part 1, Part 2, family mini-specs | Affected countries receive specific delayed reports that name the disaster family and affected place direction. | Only global news without private affected-country report. | Test with an AI or player country hit through reusable call and report delivered after 1 to 2 days where applicable. |
| Aftermath notification | Part 1, Part 4, Part 10 | A visible category popup or notification opens when a country has actionable aftermath. | Quietly adding a decision category that the player must notice manually. | Test or code review showing notification path for normal random and external reusable calls. |

## Disaster family gates

| Family group | Anchor files | Must exist | Forbidden simplification | Evidence |
| --- | --- | --- | --- | --- |
| Seismic, earthquake, aftershock | Parts 3 and 8 | Warning decisions, collapse damage, aftershock route, tsunami route when origin permits, rescue and retrofit options. | Reusing old Earth Earthquake logic or reducing all quakes to one infrastructure hit. | Family review with ordinary quake, regional quake, and Evolution III rupture separately handled. |
| Flood, storm surge, tsunami | Parts 3 and 8, aftermath matrix | Water damage, port and rail disruption, disease or famine risk, coastal evacuation, delayed wave route for tsunami. | Treating river floods, surge, and tsunami as identical. | Separate family entries and chain missions for water cleanup, port lifeline, and tsunami warning. |
| Wildfire, heat, drought | Parts 3 and 8 | Fire spread, smoke, drought crop pressure, local heat deaths, water security, Event 051 non-stack handling. | Allowing Event 013 heat to stack with active Event 051 logic. | Compatibility trigger or decision path showing skip, bridge, or non-stack conversion. |
| Cold, blizzard, hail | Parts 3 and 8 | Exposure deaths, supply disruption, rail clearing, shelter and livestock or crop pressure where relevant. | One generic winter penalty with no report or recovery route. | Distinct reports, state modifier directions, and recovery options for blizzard, cold wave, and hail. |
| Wind, thunderstorm, cyclone, tornado | Parts 3 and 8 | Wind damage, airfield and port disruption, moving corridor or tornado path when abnormal, shelter and route-clearing decisions. | Treating all storms as the same weather popup. | Separate ordinary wind, cyclone, thunderstorm, and abnormal corridor handling. |
| Mass movements | Parts 3 and 8 | Dry and wet landslide or debris routes, rail and mountain pass disruption, rescue and route clearing. | Only infrastructure damage without terrain-sensitive identity. | Target filters for mountain, wet, dry, rail, and valley contexts. |
| Volcanic and ash | Parts 3 and 8 | Ash, lava or lahar direction, port or air disruption, crop and water chains, massive eruption abnormal case. | Using one volcanic event without ashfall and lahar aftermath. | Eruption impact plus ash, lahar, exclusion, and abnormal massive eruption route. |
| Meteor and skyfire | Parts 5, 8, 9 | Evolution III meteor or skyfire impacts, crater or exclusion state, abnormal GUI path or impact markers, super-event candidate when scale fits. | Small flavour meteor that only damages one factory with no abnormal presentation. | Meteor family impact path, GUI marker, crater recovery, and super-event gate. |
| Dust and sandstorm | Parts 3 and 8, catalog alignment | Dust family with grounded aircraft, clogged engines, water contamination, and Event 099 bridge or placeholder. | Keeping Event 099 as a separate fully active sandstorm system. | Event 099 disposition note and Event 013 dust caller branch. |

## Recovery and aftermath gates

| Surface | Anchor files | Must exist | Forbidden simplification | Evidence |
| --- | --- | --- | --- | --- |
| Aftermath cards | Part 4, Part 10 | Cards show active disaster, affected states, damage type, disruption, recovery needs, cleanup phase, and chain risks. | Generic aftermath category with no affected place or disaster identity. | GUI or decision category review showing dynamic card values. |
| Early rescue | Part 10 | Search teams, shelters, route clearing, evacuation, triage, and port lifeline families where appropriate. | One flat relief button. | Decision family review with varied costs and family-specific AI priority. |
| Middle stabilization | Part 10 | Clean water, rail, port, food, factory inspection, and chain prevention families. | Recovery as a passive timer only. | At least several targeted decisions with success, partial success, and failure states. |
| Late reconstruction | Part 10 | Resilient rails, seismic retrofit, coastal barriers, firebreaks, volcanic routes, water security, and crater or exclusion handling. | Removing state modifiers by paying political power once. | Late project evidence with non-PP costs and family resilience. |
| Active mission caps | Part 10, decisions skill | Caps limit visible missions by phase and keep categories readable. | Showing every possible recovery mission at once. | Review of cap logic and active mission queue. |
| Foreign relief | Part 10 | Inbound and outbound relief variants with donor capacity, route access, convoy or train burden, influence risk, and refusal or delay options. | Free foreign aid without cost, route, or political consequence. | Relief decision review with donor and affected-country sides. |

## Evolution, GUI, and presentation gates

| Surface | Anchor files | Must exist | Forbidden simplification | Evidence |
| --- | --- | --- | --- | --- |
| Evolution I | Part 5 | Wider family pool and more active sequences without major strength jump. | Turning Evolution I into baseline with only larger numbers. | Family pool and sequence count differences. |
| Evolution II | Part 5, Part 7 | World-spanning seasons, neighboring-state damage, harder deaths, supply disruption, famine, disease, refugee pressure, and recovery strain. | News spam for every small worldwide hit or deaths that only slightly increase. | Evolution II test or review showing global handling and throttled news. |
| Evolution III | Part 5, Part 8, Part 9 | Abnormal disasters, huge destruction, moving paths, meteor, rupture, massive eruption, tsunami, tornado or storm corridor variants, and super-event candidates. | Treating Evolution III as ordinary disasters with bigger modifiers. | Abnormal controller review and at least one moving or path-based GUI route. |
| Abnormal scripted GUI | Part 9, diagrams, asset prompt | Panel layout, active cards, path preview, next-hit list, warning states, static fallback, and frame-sheet animation handoff. | GIF-only assets, transform-only fake animation, or a static-only final plan without reason. | Sprite list, GUI state flow, and frame-animation package handoff. |
| Super-event package | Part 6, super-event matrix, super-event prompt | Research-gated super-event candidates for abnormal campaign moments with image, text, audio, docs, and settings-aware playback planned. | Final quotes, remarks, titles, or audio invented inside the planning spec. | Research notes from super-event text and audio workflows before final localisation. |
| Achievements | Part 7, achievement prompt | Difficult achievements with non-trivial conditions, disqualifiers, tracking, and icon direction. | Automatic unlock for seeing Event 013 or clicking obvious relief once. | Achievement registry review, tracking flags, icons, and route condition proof. |
| Asset families | Part 6, asset prompt | Icons, report and news images, super-event images, abnormal UI sprites, animations, static fallbacks, manifests, and handoffs. | Placeholder art or missing manifests treated as complete. | Asset manifest, DDS paths, contact sheets where relevant, and gfx handoff. |

## Related-event gates

| Related item | Anchor files | Required outcome | Completion evidence |
| --- | --- | --- | --- |
| Event 046 | Parts 1, 2, 5, 8 | Inactive unknown placeholder. No independent Earth Earthquake gameplay. | Catalog or docs note plus no old logic caller remains. |
| Event 099 | Parts 1, 2, 3, 8 | Placeholder or narrow bridge into Event 013 dust and sandstorm calls. | Bridge helper or placeholder note, with no duplicate sandstorm logic. |
| Event 051 | Parts 1, 3, 5, 8, 10 | Separate heat wave event. Event 013 heat must not stack with it. | Compatibility trigger or conversion path. |
| Event 043 and Event 120 | Catalog notes | Do not absorb automatically without separate acceptance. Event 013 can cover ordinary flood and massive volcanic directions inside its own system. | No unintended conversion of unrelated catalog rows. |

## Final audit gates

| Gate | Required pass |
| --- | --- |
| Live file map and vanilla precedent | Main agent or `chaosx_repo_explorer` if file locations or patterns are unclear. |
| Reusable helpers | `chaosx_scripted_system_architect` for effects, triggers, constants, targets, cleanup, and call sites. |
| Decisions and missions | Parent implementation plus `chaosx_decision_mission_auditor`. |
| Localisation and scripted localisation | Parent implementation plus `chaosx_localisation_auditor`. |
| Assets and animation | Asset subagents by source mode, with `chaos-redux-frame-animation` for frame sheets. |
| Super-event text and audio | `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`. |
| Docs and spreadsheet | Documentation pass and `chaosx_spreadsheet_doc_worker` after final in-game wording exists. |
| Final completion | `chaosx_event_completion_auditor` before completion is claimed. |
