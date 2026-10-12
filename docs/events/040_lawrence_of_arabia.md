# Event 40: Lawrence of Arabia

Source design: `docs/specs/040_lawrence_of_arabia_specs/`. This page describes what the repository implements. Design acceptance follows the release-pass decision that the spec is the accepted source for this event.

## What the event is

Britain recalls T. E. Lawrence, reported dead after a motorcycle crash in 1935, and sends him into one Arabian government at a time. The target decides the terms of access, Britain pays for shipments, officers and ministries take sides, and every target ends in one settlement. Later targets follow after a delay and are internal stages of the same fire-once event.

- Entry event `chaosx.nr40.1`, Minor Fire-Once, Chaos level 1, no cluster. The id is registered in `global.fire_once_events` and no longer in `repeatable_events`.
- Catalog note: the exported catalog row still reads Minor Repeatable. That row is stale and is corrected in the workbook by the spreadsheet worker, followed by `python .tools/export_event_catalog_csv.py`. This page does not edit the workbook.
- Enabled by default through `event_log_event_is_reworked_default_enabled`.
- Event Details text key `lawrence_of_arabia.event_details.description`. It lists no mechanics.

## Phase status

| Phase | Content | State |
| --- | --- | --- |
| 1 | Recall, target registry and weighting, Lawrence's Influence, decision and mission families, settlements, intelligence, AI, reports, Event Details, event log, achievements, ideas, character | implemented, never run in game |
| 2 | Evolutions I and II: revolt cells, government replacement, British Arabian System, favoured partner, client autonomy, counter-bloc | implemented, never run in game |
| 3 | Evolution III, federation transaction, country package, Federal Authority, focus tree, super-events | implemented, never run in game |

## Event map

| Event | Role |
| --- | --- |
| `.1` | hidden entry on Britain, opens the campaign |
| `.2` `.3` | opening report to the target and the recall report to Britain |
| `.4` | terms of access, four answers |
| `.5` | weekly pulse (hidden), one chain per live target |
| `.6` | delayed next-target job (hidden, Britain) |
| `.7` `.8` | Embedded and Ascendant band reports |
| `.9` `.10` `.11` | protectorate terms, independent treaty, British notice |
| `.12` `.13` | shipment on the road and landed |
| `.15` `.16` | bases for aid, exchange of a prisoner |
| `.17` `.18` `.19` | turned contact, failed approach, detected deception |
| `.20` to `.25` | recovery and detention reports |
| `.26` | local agents decision after Lawrence is dead or defected |
| `.27` | campaign watchdog (hidden, Britain) |
| `.28` | campaign closed |
| `.30` | Lawrence's choice (personal route) |
| `.40` | news, five variants |
| `.45` | British retaliation choice after a double game |
| `.50` `.51` | neighbour alarm and overture |
| `.60` `.61` `.62` | baseline incidents: payroll, a commander, a courier |
| `.71` to `.78` | settlement reports, one per identity, both sides |

## Lifecycle

1. Random pool. `lawrence_prepare_random_event_fire` (called by `fire_event_by_temp_id_no_cluster` before history is recorded) draws one valid target by weight and saves `lawrence_prefire_target`, which becomes the Event History actor. Without Britain able to act or without a valid target the Events tab shows N/A (reasons 400 and 401) and the fire-once state is not consumed.
2. Opening. `.1` runs `lawrence_open_campaign` on Britain: one canonical character is recruited once, global trust and credibility start from the constants, and `lawrence_begin_target` starts generation one on the target.
3. Terms of access (`.4`). The four answers set broad, liaison, escorted or refused terms. Refusal is open only below Influence 60 and ends the mission at once.
4. Contest. A weekly pulse on the target computes the drift of Influence from six visible causes, applies it (bounded to plus or minus 4 a week), updates the band and trend, lands shipments, tracks mission holds and confirmation windows, rolls baseline incidents on an MTTH interval and checks the personal route.
5. Settlement. One transaction per target (`lawrence_settle`): identity recorded, package applied, reports sent to both sides, generation cleared, delay scheduled.
6. Next target. After 90 to 240 days (MTTH: base 150, faster with several clients and good credibility, slower in a British war, after a dismantlement, or after Lawrence is gone) Britain draws the next government from the whole registry. A pause counter closes the campaign after six failed monthly attempts.
7. Watchdog. Every 30 days while a target is live, `chaosx.nr40.27` ends a generation whose target was annexed, capitulated or became a subject, and closes the campaign if Britain cannot act for six checks.

No whole-world timer runs. The only world pass is the one-off candidate pool when a target is drawn.

## The one public value

Lawrence's Influence runs from 0 to 100 on the target. The category header shows the exact value, the band, the trend, the next threshold, the largest cause and Lawrence's current state. The header is a text line: the category picture and a meter cannot be combined under the current presentation rules, so the unresolved picture-plus-meter conflict of the spec is settled in favour of the category picture, with the numeric value read from the header text. No scripted GUI exists.

| Range | Band |
| --- | --- |
| 0 to 19 | Broken Access |
| 20 to 39 | Restricted Mission |
| 40 to 59 | Contested Network |
| 60 to 79 | Embedded Mission |
| 80 to 94 | Ascendant Network |
| 95 to 100 | Dominant Influence |

Hidden facts: exposure, evidence (0 to 4), the share of officers who follow the mission, the target's security strength, trust (global), British promise credibility (global), preparedness and the profile of the target AI.

### Drift per week

Support in force (shipments, route, cadres, rival play) adds 1.2 per support power. Instability adds 0.6 and 0.8 below stability 0.45 and 0.3, a defensive war 0.4, a confident government subtracts 0.4. Officers who follow the mission pull by 0.02 per point above a neutral 40. Terms, press, guarantees and a base agreement add 0.5, 0.5, 0.2 and 0.4. Counterintelligence subtracts 0.02 per point of security, the file 0.5, the office 0.4, escort 0.6, custody 0.4, a turned contact 0.4 and secured nodes 0.5. British overextension subtracts 0.8, a closed route 0.6, low credibility 0.6, a detained Lawrence 1.5. Local agents alone halve the positive terms. All values live in `common/script_constants/040_lawrence_of_arabia_constants.txt` under `lawrence_drift`.

### Confirmation windows

- Protectorate terms are offered after 30 days at 95 or after 60 days at 80 (hysteresis exits at 90 and 75).
- A treaty request unlocks after 60 days between 40 and 79.
- A mission without reach (below 20 for 120 days) ends as a restricted settlement.
- A campaign past 540 days ends as a restricted settlement.

## Intelligence with and without La Resistance

`lawrence_compute_security` gives every target a 0 to 100 strength. The fallback model counts stability, divisions, encryption and decryption technologies, security spirits, earlier preparedness and civil conflict. With La Resistance and an intelligence agency it adds agency upgrades, operatives, decryption progress against Britain and civilian intelligence over Britain. Decisions and outcomes are identical without the DLC.

## Target decisions

Visible rules hide finished stages so a phase shows three to five actions and never more than six.

| Decision | Role | Costs |
| --- | --- | --- |
| Set the Mission's Terms | opens `.4` | none |
| Take Custody of the Shipment | government keeps the shipment, small training | command power, support equipment |
| Open an Arab Liaison Office | lasting counterintelligence institution | political power, support equipment |
| Place Lawrence Under Escort | 150 days of lower reach | command power, support equipment |
| Build a Counterintelligence File | 45 days, evidence | political power, support equipment |
| Audit the Gold Ledger | starts the ledger mission | political power, command power |
| Turn a Contact, Feed Controlled Intelligence | double-game lane | political power, command power |
| Expose the Network | starts the exposure mission | political power, stability |
| Dismantle the Contact Network | starts the dismantle mission | command power, political power, support equipment |
| Secure the Officer Corps | starts the officers mission | army experience, command power |
| Expel the Mission | clean or reckless removal | political power |
| Detain the Mission | detention chain | command power, political power, divisions required |
| Play Britain Against a Rival, Balance Foreign Sponsors | real second patron | political power, command power |
| Preserve National Custody | sovereign armed partner | army experience, command power, political power |
| Seek an Independent Treaty | British answer through `.10` | political power |
| Offer an Independent Charter | personal route stage one | political power, stability |

Missions (at most two active): Trace the Gold Ledger (130 days, hold the capital and the main port for 42 days), Securing the Officer Corps (150 days, officers at or below 30 while the capital is held), Expose the Network (120 days, evidence 3, double-game ending when the contact is ready), Dismantle the Contact Network (150 days, hold three nodes for 56 days). Each has success, partial and failure outcomes and a retry delay. Held states are the capital, one coastal state and one state beside a British border or British subject, chosen at the start of each generation.

## British decisions

Authorize Gold and Arms (a paid shipment: infantry equipment, support equipment, political power, scaled by the size of the target, one at a time), Send Officer Cadres (army experience, command power, political power, a 120-day personnel commitment), Secure the Red Sea Route (convoys, fuel, command power) or Repair the Rail and Telegraph Link (trains, support equipment, political power, real infrastructure in two named states), Expand the Radio and Press Network, Promise Constitutional Guarantees, Tie Aid to Bases and Access (escrowed package the target accepts or refuses), Disavow the Mission. While Lawrence is detained: Attempt a Recovery Operation, Negotiate an Exchange (escrowed package, one exchange per target) and Disavow. Keep the Arms Route Open is the British mission opened by the route decisions.

The Desert Air Route and the favoured partner conference belong to Evolution II.

## Settlements

| Identity | Effect |
| --- | --- |
| British client | autonomy puppet under Britain, protectorate spirit, infrastructure in the capital, a registered guarantee is broken (credibility loss) |
| Independent British ally | mutual military access, British guarantee, faction join when Britain leads one, alliance spirit |
| Sovereign armed partner | partnership spirit, no British authority |
| Restricted mission | timed contacts spirit |
| Expelled | confidence spirit, preparedness, neighbour alarm, disorder spirit when the expulsion was reckless |
| Dismantled | exposed-network spirit, credibility loss, preparedness, news |
| Double-game victory | double-game spirit, credibility loss, British retaliation choice after 120 days |
| Defected | independent charter spirit, Lawrence recruited by the target, Chaos +5 once, Britain decides about local agents |

A settled country keeps `lawrence_settled` and is never drawn again.

## Character

`t_e_lawrence` is defined once in `common/characters/040_lawrence_of_arabia_characters.txt` as a corps commander (skill 2, trickster and politically connected). Britain recruits him once. Detention, expulsion, retirement and death retire him from the British roster, release and return recruit him again, and defection recruits him in the target. `global.lawrence_status` holds pending, active, detained, expelled, defected, dead, disavowed and retired. Death closes every personal route and Britain chooses through `.26` whether local agents continue at half strength.

## Exploit controls

One shipment pending at a time with a receipt serial per delivery, one detention and one exchange per target, escrow with exact refund for bases and exchange, one-shot flags for guarantees, rival play, sponsor balance and charter, cooldowns on turn, feed, recovery and every mission retry, confirmation windows, per-change bounds on Influence, a stale-chain guard on the pulse, generation ids on every receipt, and full cleanup in `lawrence_clear_target_state`.

## Achievements

- `chaos_redux_040_better_bargain`: as a player target, receive a shipment, keep Influence out of the Dominant band and finish as ally or armed partner.
- `chaos_redux_040_every_ledger_has_a_name`: as a player target, turn a contact, expose the network and dismantle it without a civil war.

Both are `is_ai = no` and track flags set at the outcome. Evolution achievements follow in the next section.

## Event-owned Chaos

Phase 1 owns one change: Lawrence defects from Britain, +5, once (`chaos_meter_history_reason.special.lawrence_defection`, 240). Phase 2 adds the first armed incident of a revolt network (5), the first government replacement (5), the established system (10), three networks dismantled (minus 10) and a recognised counter-bloc (minus 5). The federation outcomes use 244 to 246: British Arabia 10, the Independent Arab Federation 15 and Lawrence's Kingdom 15, each once when the federation forms. Evolution activation never changes Chaos.

## Evolutions

Evolution state is global (`global.lawrence_evolution`, 0 to 3). Stage n needs the Chaos tier n (200, 400, 600). A stage records one Event Log entry (type 40, actor the live target) only when `is_current_evolution_enabled` passes, so a disabled stage never sets state. Activation gives no Chaos.

- Active entry: the pulse of a live target calls `lawrence_try_evolution`. A ready and enabled stage waits an MTTH interval (base 90 days, faster in a British war or at high Chaos, slower when British credibility is low) and then activates.
- Evolved opening: before the first target, `lawrence_resolve_opening_evolution` activates every enabled stage whose requirements hold, each with its own log entry. Evolution I raises the starting Influence, officers and British support, adds one piece of evidence and schedules an incident ten days in. Evolution II recognises only existing partners and sends the first target a letter event that raises Influence by two for each partner. Nothing is conjured: with fewer than two nodes the stage waits.

### Evolution I: the Arab Revolt Network

Hidden `lawrence_cells` (0 to 100) grow with Influence, British funding and pro-British officers and shrink with security, held nodes, a counterintelligence file and exposure. From cells 25 an MTTH interval (base 100 days) opens one incident: arms and smuggling cache (`.90`), railway demolition (`.91`), officer clique (`.92`), local leaders (`.93`) or press (`.94`), weighted by coast, route state, officer share and press. Each has two answers with distinct costs. Demolition damages real infrastructure in the route state or the capital.

- Break the Revolt Cells (target decision and 180-day mission): hold the capital, the port and the route state, and cells fall by 3 a week, 5 with a file. Success collapses the cells, partial leaves cells at 30, failure sabotages a line.
- Fund the Revolt Network (Britain): cells plus 15 and faster growth for 90 days, exposure plus 10.
- Back a Government Replacement (Britain): Influence at least 80, cells at least 45, at least 55 officers in 100 following the mission, three divisions. The target becomes a British client under a 270-day provisional administration, no civil war and no unit loss, Chaos plus 5 once.
- A reckless expulsion with cells at 50 or more also fires a provincial revolt that damages infrastructure in two nodes.
- The first armed incident above cells 50 raises Chaos by 5 once.

A civil war split is not implemented. The spec requires a proven territorial and military split with capitals, forces and rollback, and the replacement route stays political.

### Evolution II: the British Arabian System

Nodes are settled clients and allies that still count plus Britain's own subjects in the registry (`global.lawrence_nodes`, rebuilt from the two arrays and Britain's subjects, never from a world scan). Six British institutions appear one stage at a time: Liaison Conference, then Arms Standardization Office and Oil and Transport Agreements, then Regional Intelligence Office, Desert Air Route and Joint Defense Charter. Each has a real effect:

| Institution | Effect |
| --- | --- |
| Liaison Conference | every node answers (contribute, name a price, refuse), the strongest contributor becomes the favoured partner and the rest grow resentful |
| Arms Standardization Office | nodes train faster, British arms shipments cost 20 percent less |
| Oil and Transport Agreements | Britain gains fuel, nodes build faster, subject nodes gain autonomy |
| Regional Intelligence Office | extra pressure on every target, closed when a target exposes the network in public |
| Desert Air Route | shipments arrive 20 days sooner and cannot be seized, needs an airbase |
| Joint Defense Charter | nodes join the existing British faction, military access in both directions |

Three institutions on at least two nodes establish the system (Chaos plus 10 once). The system collapses when nodes fall below two, Britain cannot act or credibility falls below 15. Nodes press for autonomy through Demand Greater Autonomy in the regional category.

The counter-bloc is founded by an independent registry government through Found an Arab Counter-Bloc. Up to two other candidates are invited and decide by their own AI, and with three members the bloc forms: members gain counterintelligence and preparedness, are no longer valid targets, and Britain decides through `.112` whether to recognise it and end the campaign (Chaos minus 5 once) or continue. Members may leave over time when Britain is credible and the member has no preparedness to hold it.

### Evolution log

Rows, titles, bodies and the summary of all three stages are wired in the main Evolutions tab, the History details, Event Details and the selected view.

## Evolution achievements

- `chaos_redux_040_promises_kept`: Britain with a registered guarantee, the system established, three partners and no broken guarantee when the campaign closes.
- `chaos_redux_040_desert_conference`: an independent player government in a bloc of three that Britain recognises.
- `chaos_redux_040_rails_ports_promises`: a sea route, a repaired rail link and the Desert Air Route together while a later target settles.
- `chaos_redux_040_gold_without_chains`: a player government that received at least two British shipments (`lawrence_aid_receipts`) ratifies or leads the Independent Arab Federation without being a British subject.
- `chaos_redux_040_uncrowned_kingdom`: the player government that hosts Lawrence after his defection calls the congress of the founding houses and forms the Arabian Union without a British overlord.

Both new achievements are `is_ai = no`. Gold Without Chains counts shipments only in the target that received them, so a government that joins as a dominion keeps its own receipts.

## Evolution III and the Federation

Evolution III is ready when the British Arabian System or a counter-bloc stands, at least three governments could be drawn into one congress and no federation exists (`lawrence_federation_is_ready`).
An evolved opening activates it after Evolution II with its own log entry.
Activation gives Chaos nothing and sends Britain the stance event `.130`.

### Britain's stance

| Stance | Effect |
| --- | --- |
| Sponsor | the British congress call opens, Britain's credibility rises by two |
| Stand aside | no British congress, British subjects may join other congresses, credibility rises by two |
| Oppose | British subjects cannot join a congress that Britain does not call, credibility falls by three |

### The three congress calls

All three live in `The Arabian Federation` decision category and are visible only while their conditions hold.
Each costs political power and command power (`lawrence_cost_federation`), builds its invitation list from the real arrays (`global.lawrence_nodes`, `global.lawrence_bloc_members`, `global.lawrence_independent_partners`) and sends `.120` to every invitee.
Players choose, AI invitees use `ai_chance` from their situation, and `.121` judges the congress after 30 days.

| Call | Caller | Invitees | Result |
| --- | --- | --- | --- |
| British Arabian Congress | Britain, after a sponsoring stance | Britain's nodes | British Arabia |
| Arab Congress | a counter-bloc member | the bloc | Independent Arab Federation |
| Congress of the Founding Houses | the country that hosts Lawrence after his defection, with trust at least 75, two settled targets, a standing bloc and either low British credibility or a disavowed Lawrence | the bloc and the independent partners | Lawrence's Kingdom |

### Core scoring, validation and the formation transaction

The core is the ratifier with the highest score from factories, divisions and stability, plus British backing for the British route, sovereign standing for the other routes and a large weight for a player so that a player is never absorbed into an AI core without consent.
The personal congress is always held in the host.
Validation runs before any mutation: a core exists, at least three ratified, Britain can still sponsor (British route), a sovereign core is not a subject, Lawrence is defected and free in the host (personal route) and no ratifier is at war with the core.
A failed validation changes nothing and stores the reason in `global.lawrence_fed_failure`, which the report `.133` states.
After a failed sovereign or personal congress the delegates keep a looser league (a timed spirit for one year) and the caller waits 180 days.

Formation (`lawrence_fed_form`) is one transaction.
The federation transforms the core country, so no new country tag exists and no tag collision is possible.
The three cosmetic identities `LAWF_BRITISH`, `LAWF_ARAB` and `LAWF_KINGDOM` are new tokens.
A search of this mod, the installed game and Kaiserreich found no other use of the prefix `LAWF`, so no collision exists.
AI members are annexed with their troops and their states become core territory of the federation.
A player member that is not the core stays a country as an autonomous dominion of the core, so nobody is stranded.
The campaign closes, Chaos is recorded once, the achievements are awarded, the super-event slot and the news are fired and the core receives the report `.135`.
When the core is later annexed the federation state is cleared by a one-flag check in `on_annex` and a new congress can be called.

### Federal Authority

One public value, 0 to 100, in four bands (fragile below 25, weak below 50, working below 75, strong from 75), shown in the decision category header with the band, trend and next threshold.
It starts at 45 in British Arabia, 30 in the Independent Federation and 40 in the Kingdom.
Each month a tick on the core adds the revenue baseline, minus one for Uneven Administration (minus two for Administrative Secession), minus one for Rival Commands, minus one for the political starting spirit, plus one when stability is above 60 percent and minus one when it is below 35 percent.
Four months in the fragile band worsen Uneven Administration into Administrative Secession and two months in the working band restore it.
Weak authority gives -2 percent stability and -5 percent political power, fragile more, working and strong give production and political power.

Federal decisions of the core:

| Decision | Cost | Effect |
| --- | --- | --- |
| Convene the Federal Council | political power | authority +10, 90 days |
| Collect Federal Revenue | political power, 3 percent stability | authority +5 and +1 monthly baseline, 180 days, up to 3 baselines |
| Reform the Federal Staff | army experience, command power | one step of Rival Commands, authority +5, 120 days |
| Open Regional Offices | political power, trains by factories | infrastructure in the capital and one founding state, authority +5, 120 days |
| Invite a Member Government | political power, command power | one willing independent government is invited as a dominion, authority at least 60 |

Representative AI scores (`040_lawrence_of_arabia_federation_mtth.txt`, scores are weights and not click chances):
council 90 at fragile, 60 at weak, 15 at working, 0 at strong;
staff reform 60 while Rival Commands remains (75 at war), otherwise 0;
revenue 35 when stable plus 15 when authority is weak or fragile, otherwise 0;
offices 35 at working or strong, 15 at weak;
invite 35 at strong, 15 at working, one third at war;
British congress 15 plus 35 with more than three nodes plus 35 with credibility above 70, one fifth in a war with a major;
Arab congress 0 below four members, 35 with four or more plus 15 for a neutral or communist government;
personal congress 60, 18 in a defensive war.
These come from the script by hand calculation because the probability tool takes only the focus adapter models.

### Starting spirits and their lifecycles

The federation holds at most three focus-owned spirits at once: administration, command and political.
The four Federal Authority band spirits are the mechanic's indicator and exactly one is active.

| Slot | Start | Resolved by | Final forms | Worsens to |
| --- | --- | --- | --- | --- |
| Administration | Uneven Administration | three steps from the customs line, census, regional offices, constituent congress, member guarantees, founding houses | Central, Charter or Imperial Liaison Administration, then Federation of Members or One Federal State | Administrative Secession |
| Command | Rival Commands | three steps from seniority, staff or war council, supply columns, staff reform decision, common defence charter, British mission, field government, repair standards | Unified Arab General Staff, Federal War Council, British Arabian Command or Lawrence's Field Household | none |
| Political | Promise Debt (British), Federal Mistrust (sovereign), Personal Settlement (kingdom) | the route's political focus | Imperial Compact or Equal Partnership, Charter Trust, Succession Settlement, then the late order | none |

### Focus tree

`lawrence_federation_focus_tree` (64 focuses, `common/national_focus/040_lawrence_of_arabia_federation_focus.txt`) is loaded onto the core with `load_focus_tree`.
It replaces the national tree of the transformed core, which is the carrier approach the spec accepts, and focuses that the core already completed stay completed.
The opening group is one provisional government.
Four lanes of choice follow: the political settlement of the route, the federal centre, the army and the economy.
The air, diplomacy and integration lanes open behind them.
Rewards are real: infrastructure, supply hubs, factories, radar, air bases, dockyards and anti-air in founding states, building slots, fuel, trains and trucks, equipment pools, a division template, technology bonuses, claims and cores on member states, guarantees, embassies, a faction, autonomy changes, a British release and a leader change to the council of the founding houses.
Values are in `lawrence_focus`, mostly multiples of 5.

| Branch family | Visible root | Lane | Search filter tags | Focus Navigation shortcut | Major fork or choice | Capstone or payoff | First-glance result | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Economy, oil | Federal Customs Line | x 0 to 4 | industry, stability, navy | Economy and Oil | none | Common Equipment Repair Standards | Pass | rails and ports join into oil |
| Army | Register the Member Armies | x 6 to 10 | army, manpower, research | Army | General Staff against War Council | Defend the Long Frontier | Pass | |
| Air and coast | Desert Airfields | x 12 to 16 | air, navy, industry | Air and Coast | convoy and port against communications | Air Liaison Schools | Pass | opens behind Register the Member Armies |
| British compact | Ratify the Imperial Compact | x 17 to 19 | political, army | none | Dominion against Protectorate, Voice against Equal Partnership | Pillar of British Strategy or Break with London | Pass | hidden unless the route is British |
| Sovereign congress | Convene the Constituent Congress | x 21 to 23 | political, trade | none | none | The Sovereign Arab Order | Pass | hidden unless the route is sovereign or broke with London |
| Personal union | The Personal Oath | x 25 to 27 | political, character | none | Crown Bound by Charter against Commander's State | Separate the State from the Man | Pass | hidden unless the route is the kingdom |
| Federal centre | Federal Census and Revenue Agreement | x 29 to 33 | internal affairs, industry | Federal Centre | Central State against Charter Federation, Federation of Members against One Federal State | A Federation of Members or One Federal State | Pass | |
| Diplomacy | Recognition Missions | x 35 to 41 | political, trade | Diplomacy | none | Regional Arbitration | Pass | |
| Integration | Voluntary Accession | x 41 to 45 | annexation, internal affairs | Integration | none | Staged Cores | Pass | |

The three political lanes carry no Focus Navigation entry because only one is visible.
The opening is the Charter shortcut.
`hoi4.focus_inspect` reported no crossings, no overlaps, no unresolved titles and three long connectors, all from the opening group to the three lane roots by design.

### Super-events

Slots 140 (British Arabia), 141 (Independent Arab Federation) and 142 (Lawrence's Kingdom) are wired in the shared getters for image, title, text and the button label.
There is no quote and no audio: the spec forbids an invented quote and no sourced quote or licensed audio exists yet.
The super-event is skipped when another super-event is already visible, and the news and report events still fire.
The Kingdom slot reuses the independent federation image as a stand-in.

### Not implemented

- Flags for `LAWF_BRITISH`, `LAWF_ARAB` and `LAWF_KINGDOM` (normal, medium, small) are missing.
- No grounded portraits for federation leaders exist and the head of state after the Lawrence settlement is the council with the placeholder portrait.
- Super-event quotes and audio are missing.
- The loose-league alternative to a formed federation is a timed spirit and not a separate faction.
- Counter-bloc members that join a British congress are not given negotiated protections beyond the autonomy changes of the focus tree.

## Assets

Reused existing art: report image of Lawrence (`GFX_report_event_lawrence`, provenance of the source photograph is not recorded in the repository and must be confirmed before release), arab congress report image and the decision category picture (`interface/040_lawrence_of_arabia.gfx`), news image `GFX_news_lawrence`. The client-reinforcement decision icon has no exact current decision mapping. Of the four remaining prompt-listed idea-icon subjects, British Mission and Exposed Network match live ideas that currently use generic art; Independent Partner and British Arabian System do not resolve to exact idea IDs in the Event 040 idea files. Fourteen current decision consumers, six idea consumers, and eight named focus nodes use dedicated aliases in their Event 040 `.gfx` files. Each focus icon has a matching `_shine` alias; the existing vanilla stand-in sprites and textures remain unchanged.

### Assets still needed

| Asset | Sprite name | gfx file | Where the DDS lives |
| --- | --- | --- | --- |
| Grounded portrait of T. E. Lawrence (corps commander and later roles), user-supplied HOI4-style final | `GFX_portrait_t_e_lawrence` | `interface/040_lawrence_of_arabia.gfx` | `gfx/leaders/` through the portrait workflow |
| Distinct 32x32 category icon (field notes, headcloth and liaison seal), separate from the installed category picture | Proposed `GFX_decision_category_040_lawrence`; no current category-icon consumer | No `.gfx` until an icon consumer exists | Proposed only: `gfx/interface/decisions/040_lawrence_of_arabia/decision_category_040_lawrence_category.dds` |
| Client reinforcement decision icon candidate | `GFX_decision_040_lawrence_client_reinforcement` | `alternative_for_review`; no exact live decision mapping | `docs/assets/040_lawrence_of_arabia/icons/alternative_for_review/decisions_20261011_s2/` |
| British Mission and Exposed Network idea icon candidates | Proposed aliases `GFX_idea_040_lawrence_british_mission` and `GFX_idea_040_lawrence_exposed_network`; wire only after dedicated art sample review | `interface/040_lawrence_idea_icons.gfx` | `gfx/interface/ideas/040_lawrence_of_arabia/` |
| Independent Partner and British Arabian System idea icon candidates | No exact current idea IDs; remain unwired pending mapping | None | `docs/assets/040_lawrence_of_arabia/ideas/alternative_for_review/` |
| Report images for the recall, a sabotage scene and the settlement reports | `GFX_report_event_040_<name>` | same | `gfx/event_pictures/040_lawrence_of_arabia/` |
| Flags of the three federation identities, normal, medium and small | tag files `LAWF_BRITISH`, `LAWF_ARAB`, `LAWF_KINGDOM` | none | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` |
| Super-event scene of Lawrence's Kingdom (the slot reuses the independent federation image) | `GFX_super_event_040_lawrence_kingdom_formed` | `interface/040_lawrence_of_arabia.gfx` | `gfx/event_pictures/040_lawrence_of_arabia/` |
| Super-event audio and a sourced quote for slots 140 to 142 | sound ids pending | pending | pending |
| Achievement triplets for Gold Without Chains, Desert Conference and Rails, Ports and Promises; the Uncrowned Kingdom triplet is installed | `GFX_achievement_chaos_redux_040_<id>` and `_grey`, `_not_eligible` | filename-convention achievement textures | `gfx/achievements/` |

### Focus icon registrations

| Focus ID | Dedicated sprite aliases | `.gfx` file | Runtime texture |
| --- | --- | --- | --- |
| `lawrence_fed_ratify_the_imperial_compact` | `GFX_focus_040_lawrence_british_compact` and `GFX_focus_040_lawrence_british_compact_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_british_compact.dds` |
| `lawrence_fed_convene_the_constituent_congress` | `GFX_focus_040_lawrence_sovereign_congress` and `GFX_focus_040_lawrence_sovereign_congress_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_sovereign_congress.dds` |
| `lawrence_fed_the_personal_oath` | `GFX_focus_040_lawrence_personal_settlement` and `GFX_focus_040_lawrence_personal_settlement_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_personal_settlement.dds` |
| `lawrence_fed_a_federal_cabinet` | `GFX_focus_040_lawrence_federal_administration` and `GFX_focus_040_lawrence_federal_administration_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_federal_administration.dds` |
| `lawrence_fed_oil_and_transport_convention` | `GFX_focus_040_lawrence_oil_rail_port_air_routes` and `GFX_focus_040_lawrence_oil_rail_port_air_routes_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_oil_rail_port_air_routes.dds` |
| `lawrence_fed_integrate_irregulars` | `GFX_focus_040_lawrence_army_irregular_integration` and `GFX_focus_040_lawrence_army_irregular_integration_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_army_irregular_integration.dds` |
| `lawrence_fed_recognition_beyond_the_region` | `GFX_focus_040_lawrence_recognition_accession` and `GFX_focus_040_lawrence_recognition_accession_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_recognition_accession.dds` |
| `lawrence_fed_an_arab_league` | `GFX_focus_040_lawrence_regional_order_capstones` and `GFX_focus_040_lawrence_regional_order_capstones_shine` | `interface/040_lawrence_focus_icons.gfx` | `gfx/interface/goals/040_lawrence_of_arabia/040_lawrence_focus_regional_order_capstones.dds` |

## Validation notes

Nothing was run in the game. The static checks are source review: brace balance, defined identifiers, localisation key coverage and the localisation audit. `hoi4.focus_inspect` ran once on the federation tree and returned no blockers. The `hoi4.script_validate` route returned invalid arguments twice for a path input and was not retried.

## Future plans

- A client reinforcement action with a target array of settled clients, so a client under attack can be helped at a cost without free units.
- Cairo and the Egyptian conditional target once the shared Egypt state is audited.
- Reaction events to later events (Great Embargo, Intel Leaked, Independence Wave) through narrow adapters.
