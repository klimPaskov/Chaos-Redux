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
