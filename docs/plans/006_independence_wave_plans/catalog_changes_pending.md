# Event 006 catalog changes pending

The event catalog workbook is edited only by its owner. These are the Event 006 rows and fields that need updating from the implemented source; wording below is copied from the in-game localisation.

## 2026-10-04: foreign reactions (D3)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

New event rows (namespace `chaosx.nr6`):

| ID | Type | Title | Notes |
| --- | --- | --- | --- |
| `.64` | Hidden | (router) | Dispatches each foreign government's one reaction per wave; answers patron offers for AI new states |
| `.65` | Country | A New Neighbor | Neighbor profile: Watch the frontier / Recognize and open a liaison office / Sponsor border talks / Stand with the former host |
| `.66` | Country | A Shift in the Regional Balance | Regional profile: Withhold support / Guarantee its independence / Offer to mediate / Invest in the transit corridor |
| `.67` | Country | A Question of Precedent | Great-power profile: Abstain / Extend recognition and limited aid / Offer an arms channel / Organize containment |
| `.68` | Country | A Younger State | Earlier-wave profile: Stand aside / Recognize it and share our institutions / Send aid / Contest its standing |
| `.71` | Country | A Foreign Offer | New state answers a patron offer: Refuse the offer / Accept the offer / Accept a smaller arrangement |
| `.72` | Hidden | (deadline) | Closes a foreign reaction queue whose receipts outlived every answer |

Event details text: no change. The in-game Event Details text (`chaosx.events_log.window.event_details.independence_wave`) already says "Former hosts, neighboring powers, and rival movements decide whether to recognize or challenge them," which the foreign reactions now implement.

New Event 6 history entries (Event Log): recognition, guarantee, mediation, containment, aid; text in `localisation/english/006_independence_wave_foreign_reaction_l_english.yml` (`independence_wave.history.foreign.*`).

## 2026-10-04: remnant petitions (D4)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

| ID | Type | Title | Notes |
| --- | --- | --- | --- |
| `.69` | Country | A Petition for Protection | Recipient answers a remnant former host: Decline the petition / Guarantee the host |
| `.70` | Country | An Answer to Our Petition | Host learns whether the guarantee was given, declined or lapsed |

New decision for remnant former hosts: "Petition [recipient] for a Guarantee" in the category "A Foreign Guarantee".

New Event 6 history entry: remnant guarantee (`independence_wave.history.foreign.remnant_guarantee`).

## 2026-10-04: Iberian packages and FORM-07 (D7)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-013 Basque Country (NAV) and IW-015 Galicia (GLC) can now appear in Independence Waves.
- FORM-07 "Iberian Federation" can now be formed by CAT, NAV and GLC; the federation takes the name "Iberian Federation" and a new flag.

## 2026-10-04: Don Host package (D5)

Disposition: `accepted and queued` for the catalog owner; implementation is committed.

- IW-039 Don Host (DON) can now appear in Independence Waves, with Millerovo as its capital and Volgodonsk as optional territory; it never appears alongside Event 005's Don Host Republic, and it shares one wave slot with the Kuban package.
