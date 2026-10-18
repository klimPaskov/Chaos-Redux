# Event 111: This is SPARTA!!!

## Part 7: Presentation, assets, models, and audio

**Planning status:** Working specification. Asset production, runtime identifiers, installed-vanilla calibration, source selection, and in-game acceptance have not been performed. The final gameplay records in the other specification parts determine the exact consumers and unlock conditions.

Read with the [country and military package](111_this_is_sparta_spec_part_2_country_and_military.md), [Age of Heroes](111_this_is_sparta_spec_part_5_age_of_heroes.md), [connections and achievements](111_this_is_sparta_spec_part_6_connections_and_achievements.md), and [implementation contract](111_this_is_sparta_spec_part_8_implementation_and_ai.md). This part owns presentation and asset requirements. It does not change their gameplay gates.

## 1. What the presentation must communicate

Sparta begins as a returned ancient army trying to establish a functioning modern country. Its ordinary presentation should show that transition through institutions, workshops, training grounds, and increasingly modern equipment. Ancient warriors remain visible as the founding elite. Modern citizens become a substantial part of the state and army.

The five conquest routes retain distinct identities throughout their focus icons, territorial panels, diplomatic notices, flags, and completion scenes. Mythological imagery becomes materially supernatural only after Age of Heroes has actually activated and produced the relevant actor or object. A religious policy by itself does not prove that gods or creatures have appeared.

Use bronze, weathered red cloth, dark stone, pale paper, and restrained olive military colours as proposed common visual cues. These are an alternate-history art direction, not a claim about an attested ancient national flag. Historical symbols require source research. The country should not depend on film likenesses, commercial game designs, familiar film posters, or copied soundtrack cues.

### Presentation hierarchy

| Surface | Required presentation | State or consequence communicated |
| --- | --- | --- |
| Ordinary state and military decisions | Normal decision lists, concise formatted value tables, category icon and one eligible static category picture | The current obstacle, available action, cost, and expected effect |
| Conquest and formable progress | One compact event-owned state-puzzle panel for the active route | Required territory, who currently qualifies, unmet conditions, and earned formation readiness |
| Age of Heroes decisions | Normal decisions and concise values, with supernatural category art after activation | Which manifestations exist and what increases or reduces Mythic Strain |
| Important regional or diplomatic changes | Report or news events | What changed, who is affected, and what response is now available |
| Eligible major campaign milestones | Super-event package at the specified threshold | Imperial completion, public proof of mythic power, and Divine Sovereignty |
| Qualifying international defeat aftermath | Required conditional super-event after the authenticated containment of an established imperial or transregional mythic Sparta | The durable loss of the specific order and the consequences for surviving people |

There is no general Spartan management window. The state-puzzle panel has one purpose and does not accumulate unrelated training, economy, religion, or military controls.

## 2. Values, decisions, and state visibility

The displayed values are exactly **Civic Settlement, 0 to 100**, **Military Adaptation, 0 to 100**, and, after evolution, **Mythic Strain, 0 to 100**. Do not introduce an additional presentation-only score or duplicate a hidden variable as another apparent resource.

The value table shows a plain name, current value, current mechanical state, and a brief explanation of the next relevant threshold. Effects, thresholds, and update timing come from the owning gameplay specification. Text uses the same values as decisions and triggers. A UI estimate cannot silently differ from the effect that will execute.

Before evolution, omit the Mythic Strain row and its explanatory artwork. After evolution, show it whenever its owning decisions are available. Its removal during actor cleanup follows the same lifecycle as the gameplay value. A dormant actor must not keep an active-looking supernatural panel.

Ordinary decisions retain native enabled, unavailable, timed, and completed treatment. Tooltips identify the exact missing condition and distinguish cost from reward. Reported success changes the relevant decision, value, territory state, or country condition. It does not merely add a visual seal.

A category picture is permitted only beside an ordinary decision list with a description and basic formatted values. The category must have no additional custom controls, rich panels, meters, or other animated GUI. The picture may show a training ground, administrative rebuilding, or a manifestation scene appropriate to that category. It does not contain painted buttons, values, headings, or state borders.

## 3. Compact conquest state-puzzle panel

### One active route and one geographic truth

The panel reads the current active route and that route's registered requirement groups. It is available only in the correct Spartan country context. Route previews before commitment may describe ambitions, but they must not claim eligibility or completion for a route the country has not selected.

Every state piece comes from the installed map's province and state geometry. One projection, origin, scale, and border treatment applies across the assembled map. Mediterranean and Black Sea islands remain in their actual geographic positions. Any inset needed for legibility is explicitly marked and keeps its own geographic bounds documented. Generated artwork cannot create or modify borders.

The required Laconia state split must be reflected in the combined geometry revision before these pieces are produced. A whole-Peloponnese requirement can include both resulting states, while a Laconian requirement points to the new Laconia state. Rebuild and review the affected registry and consumer crosswalk through the implementation contract. Old unsplit source geometry cannot prove that the new puzzle is complete.

The requirement registry is the source for both the map and formation conditions. For each required state or alternative group, the asset and GUI handoff records the state identifier, display name, exact counting rule, permitted qualifying country relationship, controller and owner treatment, group identifier, mask or sprite, and hover region. State IDs are resolved from the installed repository map during implementation, not guessed from a remembered vanilla map.

### States and interactions

| Panel state | What the player sees | What must remain true |
| --- | --- | --- |
| No route committed | Compact route-selection explanation and native links to the relevant focus or decision | No active formation progress is claimed |
| Active requirement unmet | Grey state fill with a border and an unmet marker | Tooltip names the exact territorial or diplomatic requirement |
| Held but not yet qualified | A distinct pending treatment and the unfinished settlement, usable-port or charter condition | Ownership alone is not presented as a completed route contribution |
| Requirement satisfied | Green qualifying fill plus a distinct check or border treatment | The same qualification passes in the actual formation trigger |
| Alternative group partly satisfied | Individual state states and a group-level count or text | The panel does not imply that every alternative is mandatory |
| Territory lost or relationship changed | The affected piece returns to its current qualifying or unmet state | Previously satisfied territory is never permanently painted complete |
| All territory satisfied, other conditions missing | Territorial success remains visible with the remaining condition listed below | Territorial completion does not enable formation early |
| Formation ready | A clear ready state and native action entry point | The action rechecks current conditions when used |
| Route completed | Earned identity and current post-formation territory state | Historical completion is distinguished from current control |
| Country absent or event cleaned up | Panel closes and its controls cease to respond | No stale target or deleted-country reference survives |

Colour is reinforced by borders, markers, or text. Hover details identify the actual owner or controller only where the gameplay rules need that distinction. Any subordinate or allied territory counts only if the route explicitly permits that relationship. A faction member, subject, collaborator, or occupation cannot qualify through an invented presentation rule.

The panel contains native labels, requirement counts, tooltips, open and close controls, and the minimal action or focus link. Decorative art occupies a separate layer. There is no painted category picture alongside this interactive panel.

Before native implementation, produce a compositional reference and a numbered mapping of its decorative layers, live labels, controls, hover regions, and map pieces. Review it at the supported UI sizes. Match subsequent GUI inspection, renders, and comparisons to the same country and route states, including a qualifying subordinate, a lost state, a missing nonterritorial condition, and an inactive actor.

### Registered geographic consumers

The [route specification](111_this_is_sparta_spec_part_3_focus_routes.md) defines the complete geographic membership and political requirements. The following set keys are the panel's authoritative consumers. An optional late conquest must not become an undisclosed final-map requirement.

| Source set | Panel-specific requirement |
| --- | --- |
| `111_set_hegemony_final` | Show the fixed Greek homeland after the Laconia split. Union and League modes use their own direct or qualifying-charter predicate. Optional late Aegean extension is not painted as required for the initial Greek charter |
| `111_set_alexander_final` | Show the seven required regional administrations and their actual constituent states. Distinguish valid direct or registered-client contributions without representing client territory as annexed |
| `111_set_thermopylae_south_final` | Show the Greek and Aegean requirements, complete selected southern corridor and Iran. The route cannot satisfy it through a disconnected port or an incomplete northern segment |
| `111_set_thermopylae_north_final` | Show the same common ends and the complete northern corridor. Changing the selected corridor changes the active requirements and retains only genuinely shared progress |
| `111_set_west_final` | Show Laconia, the Italian peninsula, Sicily and Sardinia. Laconia and Rome remain direct holdings. Optional Corsica or later African objectives do not appear as mandatory |
| `111_set_colonies_final` | Show Laconia and the nine selected anchors across five basins, with current sovereignty mode, qualified partners, port usability and basin-service obligations |
| `111_set_alexander_eastern_extension` | After the Alexander charter, show the selected optional Afghan, western-approach and Punjab extension through the same panel's objective context. It does not alter the original charter requirements or grant a new flag or second route-completion super-event |

The colonial map draws its selected anchors from the following finite candidate register. The normal summary shows nine required selections, not thirteen mandatory acquisitions. Alternatives remain identifiable without granting progress from an unselected candidate.

| Basin | Candidate role keys and selection rule |
| --- | --- |
| Aegean | `111_port_crete` or `111_port_rhodes` |
| Eastern Mediterranean | `111_port_cyprus` and either `111_port_alexandria` or `111_port_cyrenaica` |
| Central Mediterranean | `111_port_apulia` and `111_port_sicily` |
| Western Mediterranean | `111_port_provence` and `111_port_catalonia` |
| Black Sea | One of `111_port_crimea` or `111_port_odessa`, and one of `111_port_sinope` or `111_port_trabzon` |

Each role resolves to a real coastal state and usable port. A broad state cannot satisfy two distinct anchor obligations just because it contains two named places. In treaty-commonwealth mode, the Aegean anchor and holdings in at least two other basins remain direct Spartan holdings. Other qualified charter anchors receive a distinct relationship marker and accurate counterpart tooltip. Generic access, docking rights and faction membership remain insufficient.

## 4. Route identity and institutional portraits

| Route | Principal visual direction | Earned transformation and exclusions |
| --- | --- | --- |
| Spartan Hegemony | Spartan civic and military identity, treaty objects and distinct League symbolism | Its League or united Greek form follows the actual formation method. A treaty identity and direct annexation identity cannot share misleading heraldry |
| Legacy of Alexander | Campaign continuity from Greece and Macedonia into the selected eastern conquests, with a distinct Hellenic imperial emblem | The claim is presented as Spartan appropriation of Alexander's legacy. Do not depict Sparta as historically Macedonian or use a modern actor's face |
| Thermopylae Avenged | Defensive memory developed into an eastern military campaign, restrained pass and shield motifs | Persia is represented by the actual current opponent. The image does not imply that all modern Persians are an ancient army |
| The Western Campaign | Amphibious movement, southern Italian and Sicilian campaign settings, then the earned western identity | Rome or Italy is shown only when the corresponding campaign milestone is achieved |
| Hellenic Colonies Reborn | Ports, maritime institutions, convoy infrastructure, and the actual coastal network | Flag and emblem communicate a connected maritime order. Geographic art follows the exact chosen possession requirements |

Each final country or cosmetic identity has its own normal, medium, and small flag set. An ideology variant is added only where that ideology is actually supported. Visually distinct route designs need separate generated source art. Keep the existing no-suffix base flags of other participating countries unchanged.

The required flag families are the opening Sparta design, six earned route identities, and six sacred-dyarchy variants of those earned identities. Each sacred variant preserves the identifying route design while expressing the actual change of sovereign office. Sacred dyarchy requires a completed route charter, so there is no unformed sacred flag. Mortal political reform, custodianship and a mortal government's divine mandate preserve the current route flag unless a specifically accepted matching variant is authored. An older unformed-Sparta flag never overwrites an earned route flag. The four mortal institution portraits do not imply a complete institution-by-route flag matrix.

The opening royal and ephor leadership, and subsequent collective governing institutions, use institutional names and authentic attributed institutional source material. The brief does not authorize invented faces representing historical kings or officeholders. A people-free composition still needs the source-mode gate appropriate to its institution.

Portrait research directions for **Leonidas, Agis, or Cleomenes**, if later accepted as named characters, remain explicitly **blocked for final portrait production under the supplied grounded-person rules** until a permitted source or an explicit rule exception exists. Their names are not an instruction to generate a guessed likeness. This restriction does not remove an accepted gameplay role.

All character portraits belong to `chaosx_portrait_creator`. Fictional supernatural individuals, if the final roster creates them, follow their separately recorded impossible-entity classification. Historical people are not moved into that class to bypass the source rule. No advisor, high-command, or dossier-card family is inferred from a small-portrait field. Such cards require an explicit asset requirement.

The accepted mythic characters are Castor and Polydeuces. Each has a separate one-person 156×210 portrait and a real character consumer before the late political choice. Sacred dyarchy makes Castor the visible country-leader character representing joint divine kingship. Country identity and polity-spirit text explain co-rule. Polydeuces receives a real senior military office with its own independently composed 65×67 advisor portrait and may use his 156×210 portrait for the accepted commander role. His field, office, training, and tournament assignments obey the character contract. Castor is not simultaneously a freely deployed field commander while serving as visible sovereign. A composite portrait is not required or permitted by this specification.

Before the final constitution, the pair has at most one active field-command or national training service at a time. Presentation distinguishes available, assigned, recovering, withdrawn, sovereign and tournament states through the actual character record and native availability treatment. It does not display two active-service benefits or a second copy of a hero merely because both portraits exist. Polydeuces is the specific mythic tournament entrant.

Mortal custodianship and a divine mandate claimed by mortal rulers retain their actual mortal institutions. Divine imagery does not silently replace their leader with either twin.

## 5. Asset requirement register

The identifiers below are planning requirement identifiers, not verified runtime sprite names. Before production, expand each listed collection against the final gameplay records. The resulting manifest contains one row per required logical slot and explicitly lists aliases sharing a runtime file.

| Requirement | Exact scope to expand | Native delivery and consumer |
| --- | --- | --- |
| `111_FLAG_BASE` | Initial Sparta and each genuinely supported ideology variant | Flat TGA ladder at 82×52, 41×26 and 10×7 in tag-based flag paths |
| `111_FLAG_ROUTE:<identity>` | Every earned cosmetic or final country identity in the route register | Independent flat source design and complete TGA ladder, linked to the exact transformation effect |
| `111_PORTRAIT:<institution_or_character>` | Each accepted leadership or commander portrait requirement | 156×210, correct role-specific reference and portrait registration, with source state recorded |
| `111_FOCUS:<focus_id>` | Every focus in the final tree manifest | Focus-specific art, nominal 94×86, linked to that focus's sprite |
| `111_IDEA:<idea_id>` | Every event-owned national spirit or idea requiring art | Independently composed 64×64 idea art |
| `111_DECISION:<decision_or_mission_id>` | Every event-owned decision or timed mission | Independently composed 32×32 art with action-readable silhouette |
| `111_CATEGORY:<category_id>` | Every event-owned decision category | Category icon using its actual consumer canvas |
| `111_CATEGORY_PICTURE:<category_id>` | Only simple categories that pass the presentation gate | Static themed picture, exact canvas verified from the consumer. The reference family uses 114×101 |
| `111_CONQUEST_PANEL` | One compact active-route panel | Separate frame, decorative layers, native controls, and exact state pieces. Final size comes from the approved composition and consumer |
| `111_STATE_PIECE:<route>:<state_or_group>` | Every territorial requirement in the active-route registries | Exact masks or sprites, shared projection, unmet and qualifying states, native tooltip region |
| `111_REPORT:<milestone_id>` | Every report event with a distinct scene requirement | 210×176 sepia documentary card with transparent margins and consistent local card processing |
| `111_NEWS:<milestone_id>` | Every news event with a distinct scene requirement | 397×153 black-and-white documentary scene |
| `111_SUPER:<milestone_id>` | Each authorized super-event variant described below | 457×328 scene image plus complete text, image, slot, and audio handoff |
| `111_FACTION:<faction_id>` | Each actually created League or other event-owned faction identity | Faction-specific emblem using the exact installed consumer |
| `111_ACHIEVEMENT:<achievement_id>` | Every achievement in the final achievement register | One original subject, deterministic completed, grey and not-eligible 64×64 states, root-only achievement paths |
| `111_EQUIPMENT:<equipment_id>` | Each new equipment definition introduced by the accepted unit roster | Separate equipment illustration using its actual technology or equipment consumer canvas |
| `111_COUNTER:<subunit_id>:<surface>` | Every new custom subunit on every required counter surface | Bespoke counter art, actual frame semantics and sampled vanilla green palette |
| `111_TEMPLATE_EMBLEM:<template_id>` | Only explicitly accepted template-emblem requirements | Separate large 76×42 and small 30×12 emblem canvases |
| `111_MODEL:<model_id>` | Every accepted custom model in the unit and myth roster | Complete geometry, materials, rig, semantic actions, sourced audio and counter handoff |
| `111_ANIMATION:<animation_id>` | Only the meaningful animated families in the final register | Real source frames, static fallback, horizontal sheet DDS and verified state binding |

### 5.1. Settled country and campaign consumers

The following IDs are the shared authoring IDs supplied by the country and gameplay parts. They are not installed game identifiers. Preserve this crosswalk when the implementation assigns its final IDs.

| Consumer group | Authoring consumers | Asset obligation |
| --- | --- | --- |
| Mortal governing institutions | `111_identity_joint_royal_ephors`, `111_identity_reformed_dyarchy`, `111_identity_civic_assembly`, `111_identity_military_directorate` | One accepted institutional portrait requirement for each actual leader change, source classification and replacement state. A new flag is required only if the country or cosmetic identity actually changes |
| Hegemony formation | `111_identity_hegemony_union`, `111_identity_hegemony_league` | Two distinct earned identity flag sets, separate union and League presentation, and the appropriate territory predicate in the shared route panel |
| Eastern imperial formation | `111_identity_alexander_empire` | Its own earned flag set, imperial seal or faction emblem only for an actual consumer, and an eastern completion scene |
| Eastern retaliation formation | `111_identity_thermopylae_dominion` | Its own earned flag set and completion scene, distinct from the Alexander route |
| Western formation | `111_identity_western_empire` | Its own earned flag set and completion scene linked to the achieved western geography |
| Maritime formation | `111_identity_colonial_commonwealth` | Its own earned flag set and completion scene tied to the actual port and coastal network |
| Sacred dyarchy after formation | The sacred variant of each of the six earned identity consumers above | Six independent flat flag designs and complete TGA ladders. The base route identity remains legible. No pre-formation sacred design or automatic mortal-policy variant is required |
| Route completion milestones | `111_milestone_hegemony_complete`, `111_milestone_alexander_complete`, `111_milestone_thermopylae_complete`, `111_milestone_west_complete`, `111_milestone_colonies_complete` | One earned completion consumer for the chosen route. The Hegemony scene and identity match the union or League outcome |

The route panel contains five geographic route families and the distinct Hegemony qualification methods. It does not treat six identity designs as six concurrently active campaigns.

### 5.2. Ordinary decisions and category pictures

| Category | Main action consumers | Category icon and picture direction |
| --- | --- | --- |
| `111_category_home` | `111_action_emergency_supply`, `111_action_civic_compact`, `111_action_industrial_project`, `111_action_armament_contract` | Original administration or provisioning icon. A simple-category picture may show civilian registration and the practical work of establishing a functioning Laconian administration |
| `111_category_agoge` | `111_action_agoge_intake`, `111_action_convert_returnees` | Original training institution icon. An eligible picture shows adult modern recruits and returned veteran instructors, with equipment appropriate to the actual training stage |
| `111_category_campaign` | `111_action_select_objective`, `111_action_diplomatic_offer`, `111_action_campaign_preparation`, `111_action_proclaim_route` | Original campaign category icon and the one compact state-puzzle panel. No category picture |
| `111_category_settlement` | `111_action_postwar_settlement`, `111_action_regional_integration` | Original settlement icon. An eligible picture shows the civil and transport work of incorporating an affected region without asserting an unattained country identity |
| `111_category_myth` | `MY01` through `MY14`, exposed in their relevant investigation, service, site, recovery or constitutional context | Original investigation and custody category icon. A quiet Laconian site picture precedes activation, with no supernatural value row. Confirmed custody artwork appears only after proof. The category remains a simple list with concise values |
| `111_category_containment` | `EX01`, `EX02`, `EX03` for actual authority-qualified outside actors | Original containment icon and an eligible static scene of the actual custodial aftermath. It uses exposed site status and native costs. It does not copy Sparta's private values into the outsider's country fields |

Every listed action has a decision or mission icon requirement. Contextual actions and mission variants added by the final action ledger create their own logical slots. A collection count does not replace those rows. When a category acquires a rich control or animated GUI during implementation, its picture eligibility must be rechecked before that change is accepted.

The following eight ordinary mission consumers also receive explicit icon and state coverage. Their deadlines, outcomes and receipts come from [Part 4](111_this_is_sparta_spec_part_4_decisions_and_settlements.md). At most three player-accepted work undertakings are active for the same acting country across ordinary and mythic categories, including at most two territorial or industrial programs and one intake or conversion. Use Part 4's exact classification for mythic creation, custody and outsider work. An outsider's containment work uses its own country budget, so Sparta's full queue cannot block it. Native task information communicates capacity without creating another custom meter.

Warnings, service expiry, cooldowns and pure holding periods are independent durable records. They do not consume additional accepted-work slots. This includes the single shared 180-day containment result and achievement observations. EX03's paid industrial undertaking still occupies one territorial/industrial slot while material work remains. Its durability record adds no second slot. A selected paid repair also consumes its assigned slot. `MY10` remains available when every work slot is occupied, with any safe-withdrawal delay represented by its own actual due-date record. Do not hide a fourth construction, training or binding project inside a status timer.

| Mission consumer | Icon and visible state direction |
| --- | --- |
| `111_mission_home_supply` | The selected Laconian logistics intervention and its actual observation state |
| `111_mission_civic_settlement` | Delivery of the promised civic agreement, with pending or breached terms distinct |
| `111_mission_agoge_training` | The funded adult cohort and its actual training period |
| `111_mission_returnee_conversion` | The selected surviving ancient cohort receiving modern equipment and training |
| `111_mission_industrial_delivery` | The concrete construction, repair or arms delivery under its actual deadline |
| `111_mission_campaign_preparation` | The selected staging, crossing, transport or operational objective |
| `111_mission_regional_settlement` | The real regional administration or basin-service project and observation period |
| `111_mission_charter_repair` | The selected broken territorial, treaty or service obligation, with actual authority loss reflected immediately |

| Mythic or outsider action | Independent icon direction |
| --- | --- |
| `MY01` | A Laconian investigation and witnessed discovery, without promising an already manifested army |
| `MY02` | A defined heroic service term and the assigned person's actual role |
| `MY03` | A negotiated site-custody charter with the relevant physical location |
| `MY04` | A controlled Theban earthborn manifestation ground |
| `MY05` | One paid earthborn company or the replacement of actual losses |
| `MY06` | The unique bronze guardian under restoration |
| `MY07` | The same guardian's recovery or legal relocation, with contextual states identified |
| `MY08` | The Arcadian flock and its controlled nesting or airfield service |
| `MY09` | A bounded commitment of the selected actual family, with a separate logical slot for each supported contextual overdrive |
| `MY10` | Agreed safe withdrawal and recovery |
| `MY11` | Restored custody and the specifically warned obligation |
| `MY12` | The actual rupture's settlement, binding, release or recorded loss |
| `MY13` | Permanent release and durable aftercare |
| `MY14` | The three mutually exclusive constitutional options, each with its own contextual subject |
| `EX01` | A real outside controller securing the exposed site |
| `EX02` | Dismantling the specific unlawful or hostile binding |
| `EX03` | A durable international containment settlement |

### 5.3. Focus and spirit families

Each anchor below supplies a visual vocabulary for the focuses actually enumerated beneath it. The anchor is not one image to reuse across its entire branch. The complete tree manifest must enumerate each focus's independent source and sprite requirement.

| Anchor | Icon direction |
| --- | --- |
| `111_anchor_foundation` | Laconian establishment, returned standards, supply and civic registration |
| `111_anchor_polity` | The accepted governing institution, legal authority and citizenship |
| `111_anchor_state_capacity` | Workshops, reconstruction, transport and industrial capacity |
| `111_anchor_research` | Schools, technical instruments and the earned research institution |
| `111_anchor_land_forces` | The finite ancient host, modern cadre and actual conventional branch |
| `111_anchor_sea_power` | Ports, escorts, naval administration and supported ship types |
| `111_anchor_air_power` | Airfields, pilot education, aircraft production and supported air roles |
| `111_anchor_foreign_relations` | Negotiation, treaty objects and the live diplomatic relationship |
| `111_anchor_hegemony` | Greek consolidation, with union and League outcomes distinguished |
| `111_anchor_alexander` | The acknowledged Macedonian legacy claim and successive eastern campaigns |
| `111_anchor_thermopylae` | Defensive memory, Aegean security and the chosen eastern campaign |
| `111_anchor_west` | Amphibious logistics and the earned Italian and western milestones |
| `111_anchor_colonies` | Ports, coastal networks, convoy access and maritime administration |
| `MYTH_WITNESS` | The Laconian investigation and first tangible service |
| `MYTH_SERVICE` | Defined heroic duties, rotation and custody |
| `MYTH_SITES` | Actual access to Theban, Cretan and Arcadian sites |
| `MYTH_EARTHBORN` | The distinct earthborn tradition and bounded companies |
| `MYTH_BRONZE` | The unique bronze guardian, support crews and its custody |
| `MYTH_WINGS` | Avian flight, nesting and short-range service |
| `MYTH_LIMITS` | Recovery, binding limits and the right to refuse service |
| `MYTH_MORTAL_SETTLEMENT` | Continued mortal sovereignty and voluntary cooperation |
| `MYTH_SACRED_DYARCHY` | The actual twins in sovereign office after the route charter |
| `MYTH_MANDATE` | A mortal institution's coercive claim and its concrete obligations |

The three focus-tree spirit slots are polity, military institution, and state capacity. Give every accepted stage its own logical icon requirement and an explicit stage-to-consumer mapping. Replacement stages remain in the same mechanical slot. Mythic changes update the appropriate accepted stage instead of creating artwork that implies a fourth simultaneous tree spirit.

### 5.4. Portrait and custom military coverage

| Accepted subject or family | Required visual surfaces |
| --- | --- |
| Each of the four accepted mortal institutions | Grounded institutional leadership portrait, with authentic source evidence and pending or accepted style state |
| Castor | One fictional one-person 156×210 portrait, reused only through explicit aliases for his accepted individual character and later visible sovereign consumers |
| Polydeuces | One fictional one-person 156×210 character portrait and one independently composed 65×67 senior-office portrait, each with its own source and review record |
| Returned ancient host, `111_unit_returned_host` | `111_MODEL:RETURNED_HOST`, ancient body and held items, complete consumed actions, separate equipment illustration where defined, land counters, accepted template emblem and sourced sounds |
| Modern Spartan cadre, `111_unit_modern_cadre` | `111_MODEL:MODERN_CADRE`, modern body and firearm, complete consumed actions, separate equipment illustration where defined, land counters, accepted template emblem and sourced sounds |
| Earthborn Spartoi | `111_MODEL:SPARTOI`, one distinct custom land body and item package, complete consumed actions, equipment or recruitment presentation from the actual definition, land counters, accepted template emblem and sourced sounds |
| Talos | `111_MODEL:TALOS`, one unique custom heavy land entity, complete consumed actions, unique deployment and remaining-status presentation, land counters, accepted template emblem and sourced sounds |
| Stymphalian birds | `111_MODEL:STYMPHALIAN_BIRDS`, one custom air creature family with animated anatomy, actual aerial equipment and air-wing consumers, air counters and emblem where supported, deployment and mission-state presentation, and sourced sounds |

This is five military model packages and two mythic character subjects. Castor and Polydeuces do not add humanoid map-model packages merely because they are characters. There is no sea creature model, naval creature counter, or unused naval equipment artwork in the accepted roster. Any Dioscuri navigation or escort benefit uses only the scoped native support consumer proven by the gameplay implementation.

The four custom land families each need their actual map counter and large counter, with the installed definition and DDS inspected before production. The reference large-land layout is 152×42 with two 76×42 frames. The first uses the sampled muted vanilla green silhouette treatment. The second is an independently composed sparse pale or white schematic, not a white duplicate of the first. Air counter dimensions and states are resolved from the actual air consumer. A land layout cannot be assumed for the birds.

Each accepted custom land template needs independently composed 76×42 and 30×12 emblem surfaces. The bird wing receives the exact emblem and icon surfaces supported by its native air consumer. Do not replace a missing counter, equipment illustration or emblem with a resized focus icon, or claim an uninspected air surface exists.

### 5.5. Complete achievement icon register

All twenty achievements are accepted requirements. Their exact gameplay and reveal conditions remain in [Part 6](111_this_is_sparta_spec_part_6_connections_and_achievements.md). Each row below requires one original subject and its completed, grey and not-eligible 64×64 states, including achievements hidden until a real qualifying event occurs. The proposed keys are checked against the installed registry before final paths are assigned.

| Record and proposed key | Subject direction |
| --- | --- |
| ACH01, `chaosx_111_ach_civic_reconstruction` | An open civic assembly, restrained Spartan shield and modern workshop |
| ACH02, `chaosx_111_ach_returned_survivors` | A weathered ancient shield, maintained modern rifle and small veteran emblem |
| ACH03, `chaosx_111_ach_independent_arsenal` | A working modern arsenal incorporating Spartan identity without foreign heraldry |
| ACH04, `chaosx_111_ach_league_of_partners` | Three clearly distinct shields around a shared Greek civic emblem |
| ACH05, `chaosx_111_ach_greek_union_by_consent` | Joined civic columns, one unified shield and an open hand |
| ACH06, `chaosx_111_ach_alexander_administered` | An eastward imperial route and seven small administrative seals, simplified for native readability |
| ACH07, `chaosx_111_ach_eastern_horizon` | The established route continuing through a mountain pass toward a great river |
| ACH08, `chaosx_111_ach_restored_persia_defeated` | A defended pass opening onto a settled eastern road, with separately researched Spartan and Persian references |
| ACH09, `chaosx_111_ach_mandate_under_siege` | The mortal mandate's emblem and a bronze guardian behind a battered defensive ring |
| ACH10, `chaosx_111_ach_western_campaign_sustained` | A functioning sea supply connection to an Italian port and restrained Roman architectural silhouette |
| ACH11, `chaosx_111_ach_coastal_chain` | Separate coastal holdings joined by sea routes, with the inland space kept secondary and dark |
| ACH12, `chaosx_111_ach_commonwealth_kept` | Distinct harbor emblems surrounding a Spartan maritime seal |
| ACH13, `chaosx_111_ach_measured_myth` | Three distinct creature motifs and a paired-star motif within a balanced civic frame |
| ACH14, `chaosx_111_ach_polydeuces_open_victory` | The specific fictional boxer, twin-star symbolism and a clear tournament victory emblem |
| ACH15, `chaosx_111_ach_guardian_by_agreement` | One bronze guardian, a Cretan coastal cue and two distinct treaty seals |
| ACH16, `chaosx_111_ach_after_the_rupture` | A visibly repaired bronze seal with its fracture still legible |
| ACH17, `chaosx_111_ach_mortal_custody` | A human civic institution beneath two restrained stars, with a shield held in reserve |
| ACH18, `chaosx_111_ach_sacred_dyarchy_endures` | Two distinct star-crowned sovereign symbols above an earned-charter emblem. Keep this icon applicable to every route, with no composite portrait |
| ACH19, `chaosx_111_ach_macedonian_partner` | Separate Spartan and Macedonian-inspired emblems linked to the eastern campaign, with each historical motif researched |
| ACH20, `chaosx_111_ach_outsider_containment` | A human defensive formation sealing a fractured symbolic mythic gate, with the subdued Spartan emblem secondary |

The completed source subject is original and transparent, with no frame, text, red cross or baked square background. Derive the grey subject deterministically and apply the unchanged supplied overlay to the not-eligible state at exact alignment. Process all three through the current achievement workflow with the immutable supplied templates. Verify source-to-output compositing, native-size distinctions and decoded DDS results. A hidden or unavailable achievement still needs all three files, while runtime visibility follows its authentic eligibility and reveal record.

One focus painting resized into an idea, decision, counter, and achievement does not satisfy four rows. Each surface gets its own source art and native composition. A supplied canonical background component may be used only under its cataloged role, with the generated subject retained separately.

All 2D final DDS files use the current 2D conversion workflow. Model textures use the separate compressed full-mip route. Final runtime assets go into event-owned folders under their actual category, with engine-required root exceptions for flags and achievements. No runtime reference points into the temporary evidence workspace.

## 6. Custom model families and actions

### Baseline families

| Family | Identity and visible equipment | Action and delivery requirements |
| --- | --- | --- |
| Returned Spartan host | Finite returned ancient soldiers with the accepted shield, spear, armour, and other equipment inventory | Empty-handed body input and one separate input and geometry task for each held item. Genuine idle, movement, melee engagement, defensive response, and death roles where consumed |
| Modern Spartan cadre | A modern rifle-equipped soldier retaining restrained Spartan identity cues | Separate item-free body and firearm tasks, provider body rig and actions where eligible, then live assembled-model contact correction. Every actual firing state needs a discharge timing, locator, appropriate effect and sourced sound row |

Both families need distinct model identity, equipment art where new equipment exists, bespoke counters, and sourced role audio. Retraining and equipment change must select the correct consumer. A modernized unit cannot keep a spear attack or a permanently obsolete silhouette because its old model was already registered.

Ordinary modern armour, aircraft, ships, mountain troops, and marines follow the accepted gameplay plan. Their use does not automatically create a separate custom model family. If a branch specifies a new subunit or a distinct custom visual, add it as an explicit requirement with the complete companion package.

### Mythic military families

| Family | Identity and components | Action, scale and consumer requirements |
| --- | --- | --- |
| Earthborn Spartoi | Armed warriors of the earthborn Theban tradition, visually separate from returned Spartans. The accepted body, armour and held weapon inventory are recorded before production | A land infantry scale crosswalk, separately prepared held items, actual emergence or recruitment presentation where consumed, articulated movement, melee strike, guard, impact and death roles. Recruitment art must not imply another inexhaustible returned Spartan population |
| Talos | A singular bronze guardian associated with the accepted Cretan custodial site. Its silhouette and material treatment distinguish it from both a modern tank and a generic human soldier | A measured heavy-land scale and province-visibility audit, a complete anatomy and material plan, deliberate locomotion, the accepted close-combat action, defensive response and a complete incapacitation sequence. Any thrown or held object needs its own explicit item and action consumer. It receives no invented cannon, muzzle flash or gunshot |
| Stymphalian birds | A limited short-range wing of mythic birds with a distinct avian body and wings | A measured native-air scale crosswalk, non-biped rig map, real articulated wing motion, the exact supported flight and strike states, and an actual death or disappearance state where consumed. Preserve visible distinction from conventional aircraft and the gameplay vulnerability to fighters and antiaircraft fire |

The mythic equipment and deployment interfaces must communicate finite availability, an absent or inactive manifestation, its current assignment, losses, and any accepted recovery state. A counter or model appearing on the map is evidence of an actually fielded unit, not proof granted by an unlocked focus alone. Talos remains one entity. A bird-wing image does not imply unlimited wing size, global range, or immunity to modern weapons.

A hero implemented as command support uses the authorized portrait, trait, office and tournament presentation. Maritime support by the Dioscuri does not create a sea body or new naval weapon family. These distinctions remain explicit in the asset manifest and the sound-binding audit.

### Shared acceptance contract

The current `chaos-redux-3d-model-pipeline` controls production. The parent brief supplies the actual profile, deterministic job root, named installed references, model identity, item inventory, required actions, source permissions, exact output paths, and runtime consumer. A named installed mesh, measurement, scale, or binding is not considered verified by this specification.

Before generation, inspect the actual vanilla domain reference and entity scale. Record source dimensions, effective runtime dimensions, axes, origin, ground or water contact, and the applied scale. Nonhumanoid bodies additionally need a measured numeric scale crosswalk and a written anatomy-appropriate rig map. Do not apply entity scale twice.

Every held item is generated separately and then fitted, controlled, and reviewed as part of the complete performance. Actions preserve equipment contacts, genuine articulated movement, and the unit's role. A shield-bearing melee unit needs its actual guard and strike behaviour. A rifle unit needs its actual aiming and discharge behaviour. A required death action includes collapse, impact, and settling.

Eligible bipeds use the verified Meshy 7 rig and action route with recorded attempt limits. Unsupported anatomy and rejected or missing roles go to live Blender authoring. Repository code does not create formula-based bones, weights, or keyframes. Exported `.mesh` and `.anim` bytes are reimported or decoded and reviewed, with loop phases, contacts, facing, material binding, and actual consumer evidence kept separate.

Source models, item tasks, animations, and accepted checkpoints retain their own lineage. Model textures use BC1 diffuse and BC3 normal/specular with complete mip chains, normally 512 pixels and a concrete justification for 1024. The current owning skill defines the exact processing and packed-channel checks. The generic uncompressed 2D DDS converter is not the model texture delivery route.

Select the model reference from the current skill's eligible modern designed-art sources and verify rights and any AI-use restriction. An archival photograph, museum object, statue, historical painting, or reenactment is not an eligible final model-generation reference under that workflow. The ancient returned host and explicitly fictional mythic roster have a documented antique or fantasy period exception in their model briefs. The modern cadre retains the campaign's contemporary military setting. Retain the researched source and the original source-informed derivative separately, and do not ship copied commercial character art as a runtime asset.

### Unit sound identity

Each custom family has sourced selection, movement, action, impact, and death or disappearance audio as exposed by its actual consumer. Selection is a separate mandatory binding. For country infantry voices, audit the country or original tag and every infantry consumer under it. Do not assume a new sprite or subunit name provides an independent selection channel.

Returned humans retain a human military identity. Mythological beings use appropriately sourced nonhuman or mechanical roles where the accepted creature requires them. A melee unit does not receive firearm discharge effects merely because it carries weapons. An actual firing or supernatural discharge state receives its own verified action, synchronization, effect, and audio mapping.

Only legitimate sourced recordings and permitted mechanical edits can satisfy the audio rows. Final sound definitions, entity binding, country voice mapping, and in-game evidence remain parent-owned. No source, licence, recording, model task, or playback result is selected or claimed here.

## 7. Animated presentation

The one accepted animated family is `111_ANIMATION:SACRED_DYARCHY_PORTRAIT_OVERLAY`. It marks the earned installation of actual divine rulers. The first proof scene, normal route flags, ordinary values and category pictures remain static. The animation is a separate transparent layer over Castor's existing portrait, not an animated replacement for his identity source.

| Planning field | Required direction |
| --- | --- |
| Consumer | The verified loaded country-leader portrait window showing Castor as the sacred-dyarchy sovereign |
| Canvas | 156×210 per frame, aligned to the actual portrait consumer and its UI scale |
| Frame plan | 32 real authored source frames at 12 frames per second, a loop of approximately 2.67 seconds |
| Horizontal sheet | 4,992×210, with no labels, padding gaps or duplicated terminal frame |
| Composition | Restrained paired votive ornaments and physically changing cloth or ribbon forms around the portrait edge, with the face, office and other native information unobscured |
| Motion | Frames 000–007 develop the opening motion, 008–015 carry its crest, 016–023 settle it, and 024–031 return continuously toward the initial state. Each meaningful cloth shape is real source art |
| Anchor and playback | Bottom-centred alignment within the portrait canvas, stable camera and subject bounds, looping, restart on show after the exact consumer confirms that behavior |
| State predicate | The selected country is the actual Spartan actor, Age of Heroes and the sacred dyarchy are active, Castor is the displayed sovereign, and the actor and portrait window remain valid |
| Companion | Static fallback from the accepted seed, source and processed frame records, sheet PNG and DDS, native review contact sheet, review-only GIF, metadata and exact GUI handoff |

The production brief may refine the decorative motif after native reference review, while preserving this restrained state purpose. A lower frame count needs a concrete native-size or performance justification and smooth-motion review. Every texture side remains within 16,384 pixels.

Use the current frame-animation skill for real per-frame generation or editing, native transparency, stable anchors, frame lineage and loop review. Its named model requirement applies where the exposed image tool offers a selector. Record the actual exposed path when it does not. A moved, recoloured, blurred or pulsing still cannot satisfy the frame requirement. Loss of divine sovereignty, Castor's removal, actor cleanup or a different displayed country hides the overlay immediately. It never blocks clicks or supplies a third category picture. The static fallback is a companion asset, not permission to omit the accepted animation.

## 8. Super-event register and production direction

These are working milestone labels and content directions. They are not final localisation, verified quotes, selected recordings, reserved runtime slots, or audio IDs.

| Planning milestone | Trigger contract | Image and sound direction |
| --- | --- | --- |
| `111_SE_ROUTE_COMPLETION:HEGEMONY_UNION` | `111_milestone_hegemony_complete` is committed with `111_identity_hegemony_union` | A public scene of the actual united Greek order and a distinct ceremonial recording |
| `111_SE_ROUTE_COMPLETION:HEGEMONY_LEAGUE` | The Hegemony milestone is committed with `111_identity_hegemony_league` and qualifying actual partners | A League ceremony showing real negotiated authority, separate from the union scene and recording |
| `111_SE_ROUTE_COMPLETION:ALEXANDER` | `111_milestone_alexander_complete` and `111_identity_alexander_empire` are committed after the full charter | The governed eastern imperial order, acknowledging the Macedonian legacy claim, with its own scene and recording |
| `111_SE_ROUTE_COMPLETION:THERMOPYLAE` | `111_milestone_thermopylae_complete` and `111_identity_thermopylae_dominion` are committed | The achieved eastern settlement and its cost, with an actual present opponent or postwar context and its own recording |
| `111_SE_ROUTE_COMPLETION:WEST` | `111_milestone_west_complete` and `111_identity_western_empire` are committed | The earned Italian and western order with a route-specific scene and recording |
| `111_SE_ROUTE_COMPLETION:COLONIES` | `111_milestone_colonies_complete` and `111_identity_colonial_commonwealth` are committed | A functioning maritime network and its actual civic order, with a distinct scene and recording |
| `111_SE_MYTH_PUBLIC_PROOF` | The successful Laconian investigation has manifested Castor and Polydeuces together once, and their real assigned service commits `C111_HERO_PROOF` | One primary period documentary scene of the actual twins and witnesses in a Laconian setting. This is a scene, not a composite character portrait. Its cue supports material revelation and the consequences of their accepted service |
| `111_SE_DIVINE_SOVEREIGNTY` | The late sacred-dyarchy transformation has met its complete earned conditions, installed the actual twins in sovereign offices and committed `C111_DIVINE_SOVEREIGNTY` | An established divine governing order shown through its actual identity, people and institutions. Castor's visible sovereignty and Polydeuces's office are represented consistently. Mortal custodianship and a mortal divine mandate do not trigger this package |
| `111_SE_INTERNATIONAL_DEFEAT` | Required conditional content. The actual Spartan opponent has `C111_TRANSREGIONAL` or `C111_ROUTE_ORDER`, prior material `C111_DIVINE_SOVEREIGNTY` or `C111_COERCIVE_MANDATE`, a valid authenticated `EX03` containment settlement and its 180-day durable result | A reflective aftermath scene tied to the contained imperial mythic order and its survivors. Mere early defeat, temporary retreat or an unfulfilled settlement never triggers it |

There are nine required production packages across all possible playthroughs: six route-completion variants, one Dioscuri first-proof package, one sacred-dyarchy package and one conditional international-defeat package. At most one route completion plays per run. All nine packages require complete production and wiring. The sacred-dyarchy package can retain one scene and one recording across the six flag states because its depicted constitutional event is the same. If its scene shows a route-specific flag, that image detail must be supplied through the correct consumer or an explicitly registered variant. It cannot paint the wrong national identity.

The international-defeat trigger uses the exact qualifying-opponent and authenticated `EX03` settlement predicates shared with `ACH20` in [Part 6](111_this_is_sparta_spec_part_6_connections_and_achievements.md), together with the `C111_MAJOR_CONTAINMENT` durable-outcome receipt in [Part 1](111_this_is_sparta_spec_part_1_core.md). The 180-day result is proved by those authoritative records. A copied achievement flag, cosmetic identity or separate approximate presentation check cannot substitute for them. The scene grants no additional containment reward.

The opening report is a separate scene of the actual returned host physically present in Laconia with contemporary witnesses and the local terrain. It does not receive a super-event at birth. The first heroic proof is also separate from merely activating Age of Heroes, and the later first fielding of Spartoi, Talos or birds does not replay that heroic proof. Super-event playback grants no additional Chaos, unit, character, route or formation reward.

For each implemented variant, `chaosx_super_event_text_researcher` researches several primary-source or otherwise traceable short quote candidates and cultural remarks. Historical attribution and translations must be verified. No recognisable quotation is inserted into the planning document as if it had already been checked.

`chaosx_super_event_audio_researcher` first checks the narrow approved repository track inventory, then researches suitable sources when needed. Each implemented super-event has a unique final musical recording, audio ID, and registration unless the user has approved exact reuse. Prefer 60 to 120 seconds, with no final cue above 120 seconds absent approval. Check composition and recording rights separately. Film scores, modern commercial recordings, pure drones, and generic sound effects do not become acceptable through thematic fit alone.

The handoff aligns the slot, title direction, description direction, button direction, verified quote, image sprite, final WAV, sound definition, volume wrappers, scripted image and text getters, visibility flag, and settings-aware playback helper. It also records one-shot guards and queue behaviour so two earned milestones do not overwrite one another's image or sound.

## 9. Source, evidence, and ownership gates

The active asset manifest begins from every accepted requirement, including conditional and route-specific rows. It records logical slot, source package, selected candidate, runtime path, alias, consumer, state binding, current evidence, and status. File inventory, alias use, source provenance, and accepted completion are separate facts.

The producer retains exact generation requests, source or licence records, accepted and rejected candidate lineage, native-size reviews, contact sheets, final DDS decoding, and the explicit final selection. All counter frames and achievement states are reviewed. Raw source art, processed previews, and runtime copies remain distinct.

| Owner | Owns | Parent review before acceptance |
| --- | --- | --- |
| `chaosx_asset_source_researcher` | Nonportrait archival imagery, historical symbols, flag design research, source documentation | Source identity, terms, date fit, and correct asset family |
| `chaosx_portrait_creator` | Every portrait source, crop, fictional portrait generation, portrait-specific wiring and review handoff | Classification, independent identity and framing review, current consumer and final or pending state |
| `chaosx_generated_event_art` | Non-icon event scenes, flat flag output, faction or institutional decoration, category pictures, allowed animation layers | Scene meaning, native readability, source mode, and separation from functional controls |
| `chaosx_icon_artist` | Focus, idea, decision, category, achievement, technology, exact-map state-piece and bespoke counter packages within its assigned surfaces | Correct family-specific source, canvas, palette, frame state and exact consumer |
| `chaosx_3d_model_pipeline` | Body and item source preparation, provider tasks, live model authoring, exports, sourced unit audio, counter handoff and model evidence | Complete assembled identity, actions, contacts, texture binding, actual delivered bytes, and live consumer |
| `chaosx_super_event_text_researcher` | Verified quotation and cultural-reference research in the named handoff, without final localisation or script edits | Attribution, exact wording, translation, fit, and an explicit final-selection decision |
| `chaosx_super_event_audio_researcher` | Source research, permitted download and editing, final WAV and provenance, without sound or script wiring | Composition and recording rights, uniqueness, duration, playback evidence, and complete wiring facts |
| Parent implementation agent | Nonportrait GFX, GUI, gameplay and country consumers, sound definitions, route identity changes and final runtime integration | Row-level coverage and user-provided in-game evidence |

These are future implementation ownership maps. The present task has not executed any of these production roles or their validation tools.

## 10. Implementation evidence and closure

The implementation asset register must distinguish source acceptance, production, delivered-file checks, registered consumers, and in-game acceptance. Installed map geometry, reference canvases, model calibration, portrait source selection, recordings, quotations, runtime slots, and generated outputs remain implementation gates. The source-reading receipts and repository inspection limitations are recorded in the package's source evidence records.

At full implementation completion, promote durable provenance, accepted lineage, crosswalks, model and audio evidence, and integration facts into permanent documentation. Place final files in their engine-facing folders, verify that no consumer points into `docs/assets/`, and then remove only the event's temporary workspace. Retain the durable portrait source archive and reusable skill references. Blocked or incomplete work keeps its evidence workspace.
