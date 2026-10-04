# Event 012 catalog changes pending

The workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is edited only by its owner; this file lists the exact Event 012 changes the workbook needs.
After the workbook update, run `python .tools/export_event_catalog_csv.py` from the mod root; never edit the CSV exports directly.
Every field must match the in-game wording quoted here.

Disposition: `accepted and queued` (basis: the takeover's catalog-alignment item; the workbook is outside this owner's write scope).

## Event 012 row (ID 12, "Africa Is One")

| Field | Change | In-game source |
| --- | --- | --- |
| Details | Replace with: "An African government has started pulling the continent together with aid, guarantees, liberation deals, and a common Charter. Other countries can join, bargain, walk away, or build a rival camp. If the project keeps its promises, regional congresses and constitutional settlements can turn the idea into roads, armies, laws, and a fierce argument over who carries the cost. Once the continent is consolidated, its government can proclaim the Gods of Africa: great powers are asked for tribute, defiance is punished, loyal partners are protected, and every account is settled when the continent is secured." | `chaosx.events_log.window.event_details.africa` in `localisation/english/012_african_union_l_english.yml` |
| Evo I, Evo II, Evo III | No change. Evo III already names "strange new actors"; the strange formations (gorilla heavy infantry, pan sappers, stone cohorts, riverborn, forest giants, oracle recon, plague carriers, disaster wardens) are available through Actions 74-76, the focus routes and the Tier A packages now that their models are installed. | `docs/events/012_africa/strange_forces.md` |
| Status | Keep "Needs Testing". | |

## Gods of Africa facts for the catalog notes (if the workbook keeps per-event notes)

- Final settlement: every surviving participant is graded Favored, Respected, Distrusted, or Enemy from its whole tribute record (fulfilled-demand ratio and streaks, measured material sent, voluntary, emergency and late-campaign help, war, occupation, broken agreements, defiance, reconciliation, and Africa's doctrine).
  In-game wording: `africa.event_log.gods.continental_settlement.detail` in `localisation/english/012_africa_event_log_l_english.yml` ("Each surviving participant is remembered as Favored, Respected, Distrusted, or Enemy according to its conduct, and Favored and Respected governments are owed equipment and fuel from Africa's own stocks.").
- Material delivery: Favored and Respected governments are owed infantry equipment and fuel scaled to the material they sent and to Africa's Strength; the settling government delivers it in batches through "Deliver settlement support" (`gods_of_africa_settlement_delivery_name`).
- Broken agreements: only a broken agreement (agreed tribute terms, protection compact, accepted reconciliation, renewed recognition) is a treaty breach (`chaosx.nr12.616.t` "An Agreement Broken by War").

## Achievements, news event, and super-event

| Item | Catalog surface | Status |
| --- | --- | --- |
| Four Gods achievements: Long Obedience, Survive Defiance, Continental Provision, The Careful Gambler | Achievement rows or notes for Event 012, using the names and descriptions in `localisation/english/012_africa_achievements_l_english.yml` (`africa_gods_*_NAME`, `_DESC`) | `implemented`; add the rows. |
| Gods activation news event | Event 012 notes: "Africa Proclaims the Gods of Africa" (`chaosx.nr12.617.t`) | `implemented`; add the note. |
| Gods global-credibility super-event | Super-event slot for Event 012 | `blocked` on audio (agent decision L17): no unique licensed track is archived in the repository. Add nothing until it ships. |

## Gods of Africa diplomatic demands (agent decision L25)

If the workbook keeps per-event notes for Event 012, add these facts in the in-game wording:

- Recognition: "Recognition improves relations both ways, each recognising major power adds to Africa's Strength, and the world order remembers who recognised Africa." (`gods_of_africa_focus_recognize_voice_tt`)
- Territory: "Africa can demand that a foreign government hand back, by name, up to 3 African core states it controls. This demand comes before any request for material." (`gods_of_africa_focus_return_soil_tt`)
- End support: "Africa can demand that a foreign government withdraw the guarantee, military access or volunteers it gives a country Africa is fighting." (`gods_of_africa_focus_end_sponsorship_tt`)
- Security Oaths: "With Evolution III and Continental Strength or more, Africa can also demand military access, a non-aggression pact, or a guarantee of its independence from a free government outside its faction that does not already give it." (`gods_of_africa_focus_security_oaths_tt`)
- The family once shown as "security access" no longer exists under that name; it is "an end to our support for Africa's enemies".

## Gods of Africa punishments and the final ultimatum (agent decision L26)

If the workbook keeps per-event notes for Event 012, add these facts in the in-game wording:

- The Last Sentence: "Once Africa's Strength, Chaos and a participant's Wrath and record all reach their extreme gates, Africa delivers its final ultimatum: within 60 days the participant must hand back Africa's land and make peace, or pay an extraordinary settlement. Refusal or the deadline brings disaster and waves of civilian deaths across up to 3 of its states." (`gods_of_africa_focus_last_sentence_tt`)
- New report event "Africa's Final Ultimatum" (`chaosx.nr12.618.t`) and host report "Arms for the Offender's Enemies" (`chaosx.nr12.619.t`).
- New Event 012 log entries: "Africa Strikes [country] Across the Nation", "Africa's Final Ultimatum to [country]", "Catastrophe Falls on [country]" (`africa.event_log.gods.*` in `localisation/english/012_africa_event_log_l_english.yml`).

## Gods of Africa focus payoffs (agent decision L27)

If the workbook keeps per-event notes for Event 012, add these facts in the in-game wording:

- New focus "No Sanctuary for Occupiers" (`gods_of_africa_focus_no_sanctuary_for_occupiers`): "Africa can lay claim to the African core states a foreign government owns, gain a war goal to take them back, and arm the African claimant of that land."
- New decisions "Send the African Expedition", "Pledge a Final Shipment", "Speak for Africa at the Council" and "No Sanctuary for Occupiers"; new reports "The African Expedition Arrives" (`chaosx.nr12.620.t`) and "Africa Claims Its Land" (`chaosx.nr12.621.t`).

## Gods of Africa continuing support (agent decision L28)

If the workbook keeps per-event notes for Event 012, add: "Sign the Support Agreement" (`gods_of_africa_sign_support_agreement`): "The first instalment of [amount] leaves our stocks now, and each later one every 30 days. The agreement becomes agreed terms: an instalment we cannot pay on its day breaks it."
