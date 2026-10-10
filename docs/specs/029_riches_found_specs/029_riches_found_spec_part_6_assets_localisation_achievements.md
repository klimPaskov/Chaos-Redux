# Event 029: Assets, writing direction, and achievements

## Presentation role

Riches Found needs a coherent visual identity across discovery, administration, crisis, and supernatural escalation.

The event should look grounded during the baseline and increasingly strange only after the relevant evolution enters play.

The asset package should support the state-bound mine system without suggesting a new country, army, or world-scale invasion.

This part is the single owner of the asset inventory, the writing direction, and the achievement definitions; the asset and achievement prompts point here.

Runtime names are locked and registered in `interface/029_riches_found.gfx`; provenance lives in `docs/assets/029_riches_found/` and the dated records under `docs/events/029_riches_found/`.

## Asset status

| Family | Runtime state | Remaining work |
| --- | --- | --- |
| Report images | 13 wired (`GFX_report_event_riches_found_*`), including four deposit-profile discovery variants | Final acceptance with the asset review |
| Category picture and icon | Wired | None beyond final review |
| Decision icons | 47 wired, 10 individually reviewed and promoted | 37 still need individual review or repair |
| Mission icons | 9 wired | Final review |
| State modifier icons | 9 wired; Gold Fever Memory reuses the gold-sick icon and the late-outcome modifiers reuse existing icons | Final review |
| Controller aggregate and idea icons | 1 aggregate icon and 7 stage icons wired | Final review |
| Evolution icons | 3 DDS files and sprites exist | No live consumer reads them yet |
| Achievement triplets | 7 complete, grey, and not-eligible triplets wired | Unlock and disqualifier acceptance |

## Asset source mode

The mine, its workers, guards, claimants, foreign concession staff, Gold Disease incidents, and supernatural chambers are dynamic and fictional in the campaign.

Generated period-authentic documentary art is the preferred source mode for report images and the category picture.

Generated symbolic art is the preferred source mode for icons and achievements.

Production uses the image-generation route defined in `.claude/skills/chaos-redux-event-assets/SKILL.md`.

Internet-sourced archival material should be used only when the final asset is explicitly changed to depict a real photographed object, poster, or place.

No real-person portrait is required.

## Report-event image family

Runtime names follow `GFX_report_event_riches_found_<subject>` in `gfx/event_pictures/029_riches_found/`, and the discovery report has four deposit-profile variants (`_alluvial`, `_deep_vein`, `_gemstone`, `_platinum`) chosen by `GetRichesFoundDiscoveryPicture`.

Target size: 210x176 unless the inspected active consumer uses another verified size.

The images should resemble period documentary photographs from the late 1930s or 1940s.

They should avoid modern machinery, modern protective equipment, contemporary roads, modern uniforms, cinematic color grading, readable generated text, and obvious fantasy concept-art composition.

### Discovery report

Working asset ID: `riches_found_discovery_report`.

Subject direction: Surveyors and workers crowd around newly exposed ore at a rough excavation, with officials trying to control access and prospectors arriving in the background.

Composition direction: The physical material and human rush should dominate, with one clear foreground group and a visible route into the mine district.

Mood direction: Practical amazement, immediate competition, and uncertain order.

Avoid: Treasure chests, giant fantasy crystals, modern open-pit machinery, maps as the main subject, and celebratory propaganda staging.

### Rush settlement report

Working asset ID: `riches_found_rush_report`.

Subject direction: A rapidly built mining camp with workers, merchants, improvised housing, carts or period trucks, and crowded access.

Composition direction: Show pressure on settlement and services through density and movement.

Mood direction: Opportunity mixed with congestion and disorder.

Avoid: A clean planned town, modern shantytown imagery, and caricature.

### Concession struggle report

Working asset ID: `riches_found_concession_report`.

Subject direction: Foreign engineers, local officials, guards, and workers at the mine entrance or processing works, with visible separation between authority groups.

Composition direction: The contract's physical consequences should be visible through equipment, security, and controlled access.

Mood direction: Unequal leverage and organized expansion.

Avoid: A conference table as the main image, readable contracts, flags covering the scene, and generic diplomatic handshakes.

### Claim war and raid report

Working asset ID: `riches_found_raid_report`.

Subject direction: Armed claimants or raiders around a pay wagon, railhead, assay office, bridge, or shaft entrance.

Composition direction: Show one concrete target and the human struggle around it.

Mood direction: Sudden violence in a valuable working district.

Avoid: Large battlefield panoramas, gore, modern weapons, and anonymous smoke with no readable target.

### Mine collapse report

Working asset ID: `riches_found_collapse_report`.

Subject direction: Rescuers, workers, damaged supports, dust, broken equipment, and a blocked shaft after a serious collapse.

Composition direction: Emphasize rescue and physical destruction.

Mood direction: Loss, urgency, and uncertainty about survivors.

Avoid: Graphic bodies, supernatural symbols unless Evolution III is active, and disaster-film spectacle.

### Gold Disease report

Working asset ID: `riches_found_gold_disease_report`.

Subject direction: Workers and guards obsessively searching, counting, hiding, or fighting over small pieces of valuable material inside a mine office or shaft entrance.

Composition direction: Show altered behavior through hands, posture, barricades, locked boxes, and mutual suspicion.

Mood direction: Compulsion, possession, and group breakdown.

Avoid: Medical isolation suits, plague imagery, glowing infection, zombie behavior, or a literal disease diagram.

### Demonic chamber report

Working asset ID: `riches_found_opened_depths_report`.

Subject direction: A deep chamber with miners, impossible markings tied to accounting or valuation, altered light, and a passage that does not fit the known mine.

Composition direction: Keep period miners and real rock texture as the visual anchor while introducing one impossible spatial or symbolic element.

Mood direction: Uncertainty and an intelligence responding through the mine.

Avoid: Horned fantasy demons, lava caverns, generic occult temples, copied living religious symbols, and modern horror imagery.

### Gilded Sovereignty report

Working asset ID: `riches_found_gilded_sovereignty_report`.

Subject direction: A heavily guarded mine district whose company or local authority controls gates, payroll, transport, housing, and workers more visibly than the state.

Composition direction: Show a functioning enclave with order, wealth, and separation.

Mood direction: Prosperity under private authority.

Avoid: A new national flag, a throne, a fantasy city, and a normal government office.

### Bottomless Account report

Working asset ID: `riches_found_bottomless_account_report`.

Subject direction: An underground assay or ledger room where weighed material, official records, and human observers are connected through an impossible transaction.

Composition direction: The bargain should appear as a physical process inside the mine, not as a floating game interface.

Mood direction: Deliberate exchange and loss of control.

Avoid: Readable generated text, giant coins, demonic merchants, modern banking imagery, and abstract UI panels.

## Decision category picture

Working asset ID: `riches_found_category_picture`.

Reference family: `.claude/skills/chaos-redux-event-assets/assets/gfx_references/icons/decision_categories/pictures/`.

The asset worker must inspect the contact sheet and the actual runtime consumer before locking size.

The reference family uses 114x101, but the active consumer decides the final canvas.

Subject direction: A broad view of the mine entrance, railhead or road, pay transport, workers, guards, rough offices, and growing settlement.

The image should support the whole baseline category.

It should not depict Gold Disease or demons because the same picture remains useful before those evolutions.

It must not contain fake buttons, meters, frames, numbers, or generated text.

A static picture is sufficient.

## Small decision-category icon

Working asset ID: `decision_category_riches_found`.

Target size: Follow the inspected decision-category icon consumer.

Visual direction: A strong central combination of a mine entrance or crossed mining tools with one bright high-value ore specimen and a dark industrial silhouette.

The symbol must remain readable at the actual category-button size.

It should not reuse the report picture or idea icon.

## Decision icons

Target size: 32x32.

Every icon requires separate decision-specific source art.

The icon family can share mineral, timber, rail, ledger, guard, and shaft motifs.

Required working icons:

- `decision_riches_found_survey`
- `decision_riches_found_claim_register`
- `decision_riches_found_claim_freeze`
- `decision_riches_found_claim_court`
- `decision_riches_found_camp_administration`
- `decision_riches_found_local_labor`
- `decision_riches_found_specialist_labor`
- `decision_riches_found_sanitation`
- `decision_riches_found_rail_spur`
- `decision_riches_found_port_route`
- `decision_riches_found_shaft_reinforcement`
- `decision_riches_found_processing_works`
- `decision_riches_found_housing`
- `decision_riches_found_development_fund`
- `decision_riches_found_drive_deeper`
- `decision_riches_found_dividend`
- `decision_riches_found_local_revenue`
- `decision_riches_found_central_revenue`
- `decision_riches_found_stabilization_fund`
- `decision_riches_found_audit`
- `decision_riches_found_replace_administration`
- `decision_riches_found_concession_auction`
- `decision_riches_found_exclusive_concession`
- `decision_riches_found_offtake`
- `decision_riches_found_disclosure`
- `decision_riches_found_publish_contract`
- `decision_riches_found_nationalize`
- `decision_riches_found_buyout`
- `decision_riches_found_mine_police`
- `decision_riches_found_private_guards`
- `decision_riches_found_army_cordon`
- `decision_riches_found_armed_workers`
- `decision_riches_found_pay_train`
- `decision_riches_found_truce`
- `decision_riches_found_temporary_closure`
- `decision_riches_found_quarantine`
- `decision_riches_found_workforce_replacement`
- `decision_riches_found_seal_depths`
- `decision_riches_found_repair`
- `decision_riches_found_evacuation`
- `decision_riches_found_permanent_seal`
- `decision_riches_found_religious_assistance`
- `decision_riches_found_occult_assistance`
- `decision_riches_found_scientific_assistance`
- `decision_riches_found_bargain`
- `decision_riches_found_close_account`
- `decision_riches_found_reopen_mine`

The implementation can reuse one icon across tightly related levels of the same action only when the semantic action is identical and the visual remains accurate.

It must not satisfy the family by resizing focus or idea icons.

## Mission icons

Target size: Follow the decision and mission consumer, normally 32x32.

Required working icons:

- `mission_riches_found_secure_rush`
- `mission_riches_found_open_railhead`
- `mission_riches_found_protect_pay_train`
- `mission_riches_found_break_claim_war`
- `mission_riches_found_restore_shaft`
- `mission_riches_found_hold_mine`
- `mission_riches_found_public_settlement`
- `mission_riches_found_audit_concession`
- `mission_riches_found_evacuate_workforce`

Mission icons should show the objective, not a generic clock.

## State-modifier icon family

Target size: Follow the state-modifier consumer, with 64x64 as the planning reference when the current project pattern uses that size.

Required working states:

- `riches_found_state_new`
- `riches_found_state_developed`
- `riches_found_state_contested`
- `riches_found_state_closed`
- `riches_found_state_ruined`
- `riches_found_state_sealed`
- `riches_found_state_corrupted`
- `riches_found_state_gold_sick`
- `riches_found_state_opened_depths`

The icons should form a coordinated family while remaining separately authored for their state.

The ordinary states use tools, shafts, rail, ore, gates, damage, and seals.

The evolved states add ledger corruption, obsessive hands or guarded boxes, and impossible depth motifs.

## Controller idea icon family

Target size: 64x64.

Required working states:

- `riches_found_idea_windfall_receipts`
- `riches_found_idea_managed_revenue`
- `riches_found_idea_resource_dependence`
- `riches_found_idea_captured_revenue_state`
- `riches_found_idea_gold_sick_administration`
- `riches_found_idea_infernal_accounts`
- `riches_found_idea_reformed_settlement`

The family should use treasury, ledger, mine, state, guard, and contract motifs.

The icons must remain readable without text.

## Evolution icons

Target size: Follow the Event Details evolution-icon consumer.

Required working icons:

- `riches_found_evolution_resource_curse`
- `riches_found_evolution_gold_disease`
- `riches_found_evolution_demons_beneath_mine`

The Resource Curse icon should show mine wealth capturing a government or treasury.

The Gold Disease icon should show possession and concealed material without medical imagery.

The Demons icon should show an opened shaft responding through impossible symbols or light, without a generic horned creature.

Pending: the sprites `GFX_idea_riches_found_evolution_*` exist, but the Event Details and Event Log evolution rows do not read them yet.

## Asset-state review

The asset handoff should include contact sheets that show:

- native dimensions
- alpha behavior
- final alignment
- readability at target size
- visual separation among decision, mission, idea, state-modifier, evolution, and achievement types
- absence of opaque square backgrounds where transparency is required
- absence of white halos and fake checkerboards
- absence of generated text

The report and category art should be reviewed at native size and inside a representative HOI4 frame.

## Writing standard

The final implementation writes complete in-world text.

The spec gives direction and must not be copied directly into localisation as finished prose.

All event text should identify the current actor, mine state, relevant foreign actor, current crisis, or selected policy when those details are visible to the player.

The writing should not describe implementation history, hidden variables, tuning, or future surprises.

## Event title direction

The entry title should communicate that a specific state has revealed exceptional wealth.

It should be concise and adaptable to dynamic state context.

It should avoid generic phrases about destiny, a changed world, limitless riches, or a miracle.

## Discovery description direction

Viewpoint: The receiving country's government observing the first confirmed effects in the selected state.

Visible information:

- survey confirmation
- workers and prospectors arriving
- claims appearing
- prices or traffic changing
- the immediate political opportunity
- uncertainty about control

Uncertain information:

- exact long-term scale
- future corruption
- evolution state
- hidden foreign interest
- supernatural content

Tone: Practical amazement and urgency.

Avoid: A treasury report as the emotional center, a generic official denial, and a list of bonuses.

## Discovery option direction

The entry offers the five opening policies listed in Part 1, and no option may be a clearly dominant reward choice.

Each option tooltip names the lasting direction in one line (who gains, what it risks) and shows at most the two value changes that matter for that policy.

A row of four one- or two-point changes on a 0 to 100 scale reads as noise, so the current four-value option tooltips should be trimmed (pending).

Option tone can vary through confident state control, cautious survey language, speculative enthusiasm, local-rights emphasis, military urgency, and cynical patronage.

Final wording should be researched for country and ideology context where cultural references are used.

## Baseline report direction

### Claims and rush

Write about physical access, repeated claims, camp growth, shortages, violence, and sudden fortunes.

Use restrained irony for fraud, speculation, inflated prices, and administrative absurdity.

Do not use cheap jokes during killing, eviction, or collapse.

### Development

Write about rail, drainage, reinforcement, housing, processing, and the visible change in the mine state.

The text should make project completion or failure concrete.

### Revenue settlement

Write about who receives money, who waits, what is built, and which promises are trusted.

Avoid treating revenue as an abstract national number.

### Concessions

Write about equipment, access, guards, transport, ownership, and public terms.

Do not default to a conference-room scene or generic diplomatic wording.

### Armed competition

Name the target of the raid or dispute.

Describe the pay route, gate, shaft, bridge, office, or shipment under attack.

Avoid generic reports that violence has increased.

### Collapse

Focus on rescue, blocked workings, damaged support, missing workers, and the cost of reopening.

Do not use empty disaster language.

## Resource Curse writing direction

Viewpoint: Government, workers, local residents, auditors, contractors, or political factions experiencing the mine's capture of institutions.

Visible pattern:

- jobs and contracts allocated through influence
- receipts missing
- budgets dependent on future output
- officials protecting ownership networks
- local services failing despite visible wealth
- ordinary industry losing workers or investment

Tone: Political and economic pressure described through concrete behavior.

Avoid: A lecture on economic theory, a direct label that the resource curse has arrived, and generic corruption exposition.

## Gold Disease writing direction

Viewpoint: Workers, guards, families, administrators, soldiers, and investigators.

Visible pattern:

- material hidden in clothing or tools
- obsessive counting and searching
- refusal to leave shifts
- barricades
- guards and soldiers turning on one another
- official records altered to claim possession

Uncertain information:

- whether the condition is psychological, supernatural, social, or caused by the material
- how far it has moved
- whether replacement workers are safe

Tone: Severe and concrete.

Avoid: Virus, plague, infection, zombie, medical horror, and generic madness.

The player can use quarantine language for the action because movement is being restricted.

The event text should not present the syndrome as biological fact.

## Demons Beneath the Mine writing direction

Viewpoint: Miners, rescuers, guards, engineers, clergy, investigators, officials, and the controller.

Visible pattern:

- responsive knocks
- impossible distances
- missing teams
- altered ledgers
- ore appearing after a cost
- contracts with unknown authorship
- workers returning with changed priorities
- sealed workings reopening

Tone: Uncertain until repeated evidence makes the supernatural condition undeniable.

Avoid: A generic demon reveal, horned monsters, copied religious language, invented quotations, and direct explanation of future bargain routes.

The entity's behavior should revolve around valuation, promises, possession, and exchange.

## Gilded Sovereignty writing direction

Viewpoint: Residents, workers, central officials, guards, and foreign partners confronting a mine district governed by its own operating system.

Visible pattern:

- gates and payroll obey private authority
- local courts or rules differ from national law
- government officials need permission to enter
- transport, housing, and security belong to one network
- workers receive order and wages under constrained political rights

Tone: Functional prosperity under rival authority.

Avoid: Declaring a new nation when no tag exists, generic corporate dystopia, and modern business vocabulary.

## Bottomless Account writing direction

Viewpoint: The controller reading and fulfilling visible obligations whose consequences appear in the state.

Visible pattern:

- material, authority, promises, or people assigned a value
- receipts arriving after a defined loss
- terms changing after breach
- officials and workers debating whether the mine is obeying a contract

Tone: Deliberate, severe, and specific.

Avoid: A supernatural shop, game-currency language, arbitrary sacrifice, and open-ended death rewards.

## Decision and mission writing direction

Titles name concrete actions.

Descriptions explain what will be done and why the current state makes it relevant.

Cost text remains icon-first.

Tooltips state:

- immediate visible action
- operating-state change
- main value movement
- principal risk or mission objective
- blocked reason when unavailable

A normal action tooltip fits in two to four short lines; a contract may need more when it names its partner and terms.

They do not reveal hidden pressure formulas, exact random chances, future evolution incidents, or secret foreign involvement.

Options involving mass violence, forced labour, or sealed workers use severe in-world language and clear visible consequences, never cheap humour.

Ordinary claims, commercial absurdity, bureaucracy, and speculative excess can carry restrained irony when it fits the actor and the stakes.

## Event Details direction

Event Details should explain this premise:

A random country receives a political windfall after a vast source of wealth is found in one state.

The state remains valuable under any controller and develops through claims, settlement, construction, revenue policy, concessions, security, raids, closure, and recovery.

The detail should mention that high-chaos evolutions can distort government, behavior, and the mine itself without listing their hidden conditions or final outcomes.

It should not list raw modifiers or exact values beyond the defining 1,000 political-power discovery grant when the catalog policy allows that visible fact.

## Catalog direction

The event catalog row should remain player-facing and align with Event Details.

Suggested content direction:

- random country receives a major political windfall
- one state gains a persistent mine identity
- ongoing benefits follow the controller
- ordinary play covers development, revenue, concessions, guards, raids, and control
- evolutions introduce government capture, obsessive greed, and a supernatural force below the mine

Do not mention implementation files, hidden values, unresolved prompts, or Event 018 separation in the player-facing row.

## Achievement set

The seven achievements are registered in `common/achievements/chaos_redux_achievements.txt` with localised titles and descriptions, tracked by `common/scripted_effects/029_riches_found_achievement_effects.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.

Unlock and disqualifier acceptance is pending; each definition below is the contract that acceptance checks.

### `029_public_fortune`: Public Fortune

- Visibility and difficulty: visible, hard.
- Eligible: the country that received the mine's original discovery.
- Route: after the mine reaches the mature band and a citizens' dividend or local revenue settlement exists, hold the original mine open for two continuous years with Local Order and Revenue Legitimacy in their high bands and Extraction Pressure below severe, having completed at least one lasting public project.
- Disqualifiers: an exclusive concession on that mine, the Resource Curse recorded on it, mass killing tied to it, a patronage-dominance resolution, permanent closure or destruction, or losing the mine before the hold ends (loss resets the timer; recapture never clears a permanent disqualifier).
- Why it matters: it asks the player to turn the windfall into reliable public value and give up the strongest short-term extraction.
- Icon: a bright ore specimen above a public road, houses, or civic building, with a balanced treasury motif.

### `029_claim_jumper`: Claim Jumper

- Visibility and difficulty: visible, medium to hard.
- Eligible: any country that did not receive this mine's original discovery.
- Route: take a mine discovered by another country through war, civil war, annexation, liberation, or peace settlement; after the new contribution is reconciled, settle it through an occupation settlement, a renegotiated contract, a replaced administration, or a completed repair, and keep it operating for one year.
- Disqualifiers: permanent closure before the hold ends, or a contribution left with the former controller.
- Implemented detail: every controller change clears `riches_found_claim_jumper_settled` and the hold window, so each new controller must settle and hold the mine itself.
- Icon: a hand or claim stake seizing a marked ore claim across a broken boundary marker.

### `029_the_pay_train_runs`: The Pay Train Runs

- Visibility and difficulty: visible, medium.
- Eligible: any mine controller with a rail or convoy pay route.
- Route: complete three distinct Protect the Pay Train missions, each started under real raid, disorder, or route risk, with supplied security on the route and no successful robbery between them, while the mine stays open.
- Disqualifiers: a robbery, mine loss, or permanent closure resets the sequence; one mission can never count twice; a pay train whose route is damaged while it runs fails and ends the run.
- Icon: a guarded period train or pay wagon carrying a sealed strongbox through a mining district.

### `029_all_that_glitters`: All That Glitters

- Visibility and difficulty: visible, very hard.
- Eligible: any ordinary country.
- Route: control at least three open mines at once, counted through the bounded mine registry, each with Local Order and Revenue Legitimacy above their stable bands and none with Gold Disease, Demons Beneath the Mine, or an unanswered Gilded Sovereignty, and hold that for 180 days under a valid capped aggregate.
- Disqualifiers: a duplicated contribution, a mine closing or entering a forbidden crisis during the hold, or falling below three mines.
- Icon: three distinct mine entrances or ore specimens balanced under one national ledger.

### `029_no_man_owns_the_mountain`: No Man Owns the Mountain

- Visibility and difficulty: hidden until The Gilded Sovereignty appears on a player mine, very hard.
- Eligible: the current controller of that mine.
- Route: answer the authority through a successful revocation, a buy-back, shared sovereignty, or a representative board; restore civil administration and high Revenue Legitimacy; keep the mine open through a post-reform verification period.
- Disqualifiers: letting the board govern as an enclave, seizing the enclave by force, destroying or permanently closing the mine, losing control before the reform completes, catastrophic collapse, or foreign military intervention after the authority arose.
- Implemented detail: foreign military intervention is recorded only for raids by foreign agents or a hostile neighbour, foreign-armed incidents, and capture by a foreign country at war with the owner; diplomatic and economic pressure never counts.
- Icon: a broken private gate or charter seal above an intact mine and a public authority emblem.

### `029_close_the_account`: Close the Account

- Visibility and difficulty: hidden until The Bottomless Account appears, extreme.
- Eligible: the current controller of the affected mine.
- Route: enter the account through a deliberate agreement, reject further terms through Close the Account or a successful binding, evacuate the workforce or keep Event 029 deaths below the containment ceiling, and finish permanent sealing or another closure that ends the supernatural contribution, with national stability above its floor and control held throughout.
- Disqualifiers: Predatory Prosperity as the final state, a catastrophic collapse from a broken term, losing the mine before closure, or the mass-death disqualifier; a payment warning alone does not disqualify, and unrelated deaths can never satisfy any part of it.
- Icon: a shut ledger chained across a sealed mine entrance, with one extinguished golden light.

### `029_the_last_shift`: The Last Shift

- Visibility and difficulty: hidden until Demons Beneath the Mine is recorded on a player mine, very hard.
- Eligible: any controller of that mine.
- Route: complete the Evacuate the Workforce mission, complete one scientific, religious, or controlled engineering assistance route, then seal the mine permanently while holding it.
- Disqualifiers: forced entombment, a military purge, mass deaths, any supernatural agreement, losing the mine during the project, or reopening the sealed sections.
- Icon: miners leaving a dark shaft while a final reinforced gate closes behind them.

## Achievement tracking rules

Tracking uses stable flags for true or false history and variables only for counts and dates.

A final-state check is never enough where the route needs a past action or an avoided event.

Mission cleanup clears temporary mission state but never permanent achievement history or disqualifiers.

Achievements follow the shared achievement eligibility contract for debug, force-trigger, and custom setups.

## Achievement asset triplets

Each achievement has a 64x64 completed, grey, and not-eligible DDS directly under `gfx/achievements/`, named after the full achievement ID, with the grey and not-eligible states made through the repository achievement workflow and reusable overlay.

## Asset completion boundary

Asset production is complete only when source files, processed previews, final DDS files, contact sheets, manifests, and handoffs exist.

The asset agents must not create primitive placeholder art, resize one icon type into another, reuse unrelated assets, or substitute a static unrelated image for a required scene.

Live visual validation belongs to the user and is not an agent completion step.
