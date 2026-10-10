# Requirement coverage

“Developed” means the parts contain a substantive design treatment.
It does not mean implemented code, produced assets, or a live test.
Gate numbers refer to the [parent review gates](../../../plans/090_deal_with_the_devil_plans/review/2026-10-02_parent_review.md).

## Brief reconciliation

The 10 Oct 2026 spec audit compared every section of the [original brief](../../../plans/090_deal_with_the_devil_plans/sources/090_original_user_brief.txt) with the parts.
This closes G01 for the brief; reconciliation with current owner interfaces remains under G06 and G07.

| Brief sections | Where | Result |
| --- | --- | --- |
| Catalog entry, concept replacement, core idea | Part 1 | Covered; Event 161 duplicate and legacy `events/090_kamikaze.txt` handled at implementation |
| Design rules, what the player sees, hidden internal progression | Parts 1, 2, 12 | Covered; no meter, counter, contract window or secret-phase GUI |
| Host selection | Part 1 | Covered; one-state hosts are open question 1 |
| The first visit | Part 1 | Covered |
| Dynamic offer selection and the seven offer families | Parts 3, 4; offer index | Covered by 21 variants; category repetition rule restored in Part 3 |
| Number of main deals, side bargains | Part 2 | Covered |
| First refusal, repeated clean refusal | Part 2 | Corrected to the brief's four-visit pattern with a less generous final visit and shorter deadline (the 2 Oct draft used five invitations) |
| Refusal after accepting deals, punitive offers | Part 2 | Restored: delayed retaliation from an accepted institution, then a punitive offer, then settlement (the 2 Oct draft had dropped retaliation) |
| Accepted-deal progression (one to five deals) | Parts 2, 5 | Covered; foreign opinion signs at two deals and influence moving at four deals added |
| Hidden signs before the reveal | Part 5 | Covered by six incident patterns |
| Leader portrait transformation | Part 5 | Covered; personal deals advance one extra stage, capped at four |
| Discovering the danger | Part 5 | Covered; discovery sources map to the four safeguards |
| Breaking away, loopholes and counterplay | Parts 3, 4, 5 | Covered; one settlement event per institution |
| Open manifestation after total refusal | Part 6 | Covered; opening defensive bonus and host emergency tools added |
| Manifestation after partial acceptance | Part 6 | Covered; safeguards shape the footprint |
| Peaceful possession | Parts 2, 6 | Covered |
| Mephistophelean country identity | Parts 1, 6, 12 | Covered as one Dominion package with origin cosmetic variants |
| Mephistopheles as a character | Parts 1, 12 | Covered |
| Shared focus tree and the three opening paths | Parts 6, 7 | Covered; brief names kept as branch names |
| Common political branch, hidden liberation route | Part 7 | Covered; liberation bases are the surviving safeguards |
| Demon army branch and its three approaches | Part 8 | Covered |
| Economy and research branch | Parts 7, 8 | Covered |
| Foreign bargains, client states, Infernal faction | Part 9 | Covered |
| Baseline progression | Part 10 | Covered |
| Evolution I: The Offer Learns | Part 10 | Developed by the audit (arrangement adapts event; pre-fire demonstration); previously only gestured at |
| Evolution II: Possession Moves | Part 10 | Developed by the audit (influence moves; three leader-change outcomes); previously missing |
| Evolutions III and IV | Part 10 | Covered |
| Evolution pacing | Part 10 | Covered |
| World-end route | Part 10 | Covered; world-threat registration at ratification added |
| Brilliant Scientist, Doctor Wu, Time Traveler | Part 10 | Covered; each can be an Outside Witness |
| Disease, Research Failure, economic and military crises, other supernatural events | Parts 4, 10 | Covered; system connection table added |
| AI behavior, balance rules | Part 11 | Covered; punitive offer and adaptation AI added |
| Presentation, visual assets, focus-tree layout | Parts 7, 12; asset manifest | Covered |
| Starting military package (three origins) | Parts 6, 8 | Covered |
| Defeat and aftermath | Part 10 | Developed by the audit: one final attempt to move into an existing host; defeat super-event for a Compact-wide war |
| Rare variants (all eight) | Part 2 | Developed by the audit; resistant minister, divided cabinet and the leader who bargains back were previously missing |
| Failure handling and cleanup | Parts 2, 6, 9, 10 | Covered as rules; implementation and save/reload tests outstanding (G10) |
| Research direction | Part 12 voice; super-event research at implementation | Faust and Marlowe sources, quotes and audio require verification before use |

## Implementation coverage

| Requirement | Design location | State |
| --- | --- | --- |
| One-state separate country | Parts 1, 6 | Open question 1; G02 |
| Portrait overlays and successors | Part 5 | Developed; renderer and alignment gate G03 |
| Formation transfer in revolts | Part 6 | Developed; G04 |
| Custom 3D units, rigs, animation, sound, counters | Parts 8, 12; asset manifest | Requirements developed; G05, G08, G09 |
| Specialist and medical interfaces | Parts 4, 10; ownership map | Hooks developed; G06 |
| Terminal metric and arbitration | Part 10 | Developed; G07 |
| AI policy | Part 11 | Developed; needs seeded trials |
| Chaos accounting | Part 11; Chaos impact map | Proposed tuning; owner reconciliation |
| Spoiler-free ordinary UI | Parts 1, 5, 12; scenarios | Developed; needs a UI walkthrough |
| Achievements | Part 12 | Eight proposed |
| Live campaign acceptance | Acceptance scenarios | G10 |
