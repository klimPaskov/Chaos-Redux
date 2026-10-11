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
| 2 | Evolutions I and II, revolt cells, government replacement, British Arabian System, counter-bloc | see Phase 2 handoff |
| 3 | Evolution III, federation transaction, country package, Federal Authority, focus tree, super-events | see Phase 3 handoff |

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

Both are `is_ai = no` and track flags set at the outcome. The remaining spec achievements need Evolution II or III content and are listed in the later phase handoffs.

## Event-owned Chaos

Phase 1 owns one change: Lawrence defects from Britain, +5, once (`chaos_meter_history_reason.special.lawrence_defection`, 240). Reasons 241 to 248 are reserved for the evolution and federation outcomes of Phases 2 and 3. Evolution activation never changes Chaos.

## Assets

Reused existing art: report image of Lawrence (`GFX_report_event_lawrence`, provenance of the source photograph is not recorded in the repository and must be confirmed before release), arab congress report image and the decision category picture (`interface/040_lawrence_of_arabia.gfx`), news image `GFX_news_lawrence`. Decision icons reuse vanilla `GFX_decision_generic_*` sprites and idea pictures reuse vanilla `GFX_idea_generic_*` sprites.

### Assets still needed

| Asset | Sprite name | gfx file | Where the DDS lives |
| --- | --- | --- | --- |
| Grounded portrait of T. E. Lawrence (corps commander and later roles), user-supplied HOI4-style final | `GFX_portrait_t_e_lawrence` | `interface/040_lawrence_of_arabia.gfx` | `gfx/leaders/` through the portrait workflow |
| Decision category icon (headcloth, field notes, liaison seal) | `GFX_decision_category_040_lawrence` | `interface/040_lawrence_of_arabia.gfx` | `gfx/interface/decisions/040_lawrence_of_arabia/` |
| Target and British decision icons (custody of arms, ledger audit, guarded travel, turned contact, exposure, expulsion, charter, gold and arms package, officer cadres, Red Sea route, base agreement, recovery) | `GFX_decision_040_<name>` | same | same |
| Idea icons (British mission, independent partnership, exposed network, protectorate) | `GFX_idea_040_<name>` | same | `gfx/interface/ideas/040_lawrence_of_arabia/` |
| Achievement triplets for `chaos_redux_040_better_bargain` (rifle crate under a national lock) and `chaos_redux_040_every_ledger_has_a_name` (open ledger, marked payments, lens) | `GFX_achievement_chaos_redux_040_<id>` and `_grey`, `_not_eligible` | `interface/040_lawrence_of_arabia.gfx` | `gfx/achievements/` |
| Report images for the recall, a sabotage scene and the settlement reports | `GFX_report_event_040_<name>` | same | `gfx/event_pictures/040_lawrence_of_arabia/` |

## Validation notes

Nothing was run in the game. The static checks are source review: brace balance, defined identifiers, localisation key coverage and the localisation audit. The `hoi4.script_validate` route returned invalid arguments twice for a path input and was not retried.

## Future plans

- A client reinforcement action with a target array of settled clients, so a client under attack can be helped at a cost without free units.
- Cairo and the Egyptian conditional target once the shared Egypt state is audited.
- Reaction events to later events (Great Embargo, Intel Leaked, Independence Wave) through narrow adapters.
