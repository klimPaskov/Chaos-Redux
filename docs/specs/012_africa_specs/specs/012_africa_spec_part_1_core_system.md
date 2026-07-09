# 012 Africa spec part 1, core event system

## Design promise

Africa is a continent-unification event where a valid African-capital country becomes the public face of a new continental project. The fantasy is simple on the map and complicated in play. The chosen state can claim the language of continental unity early, but real control must pass through protection, diplomacy, faction management, local legitimacy, war preparation, resistance, integration, and late unification crises.

The public phrase `Africa is one` is a rallying concept, not an instant annexation button. The event should let the chosen country feel enormous without making it immediately own the continent. The player should be tempted by fast conquest, rewarded for careful League building, and punished when stronger African countries decide that unity means domination.

## Start package

The event fires once and selects one valid country whose capital state is in Africa. The selection should prefer countries that are alive, playable, not already a special terminal chaos country, and able to receive a focus tree or country package. The event can still select a subject, dominion, or minor state if it has an African capital and can plausibly become the carrier of the continental fantasy.

The opening package gives the selected country a cosmetic identity, a visible continental claim fantasy, a new focus tree, the Charter League system, early protection decisions, and a staged integration layer. The initial map should not become a flat block of instant cores. The player should see that Africa can be united, then spend the campaign proving that the claim has enough force behind it.

## RSA-in-Allies special branch

If South Africa is selected while it is in the Allies, the event should create a civil war instead of giving the existing Allied government the full continental package. The continental side receives the Africa package. The Allied-aligned side keeps the old international ties and fights to keep the country inside the imperial war order.

If the continental side wins, the Allies should make peace with Africa through a clean settlement path. The result should not force permanent global war if the civil war is resolved. If the Allied side wins, the Africa event should not silently vanish. It should leave a broken underground movement, a later reactivation chance through evolution, or a route where the defeated movement can reappear if chaos rises and anti-colonial wars spread.

## Public country identity

The selected country should receive direct country names that remain readable on the map. `Africa`, `African Union`, `United Africa`, `African Federation`, `African Commune`, `African Empire`, `African Sultanate`, and ideology-shaped variants are valid direction labels. Names that sound like offices or administrative boards are not valid map names.

The package can use institutions named Charter League, Integration Office, Liberation Committee, Pan-African Congress, Continental Command, Diaspora Bureau, or Resource Board. Those names should live inside decisions, focuses, advisors, spirits, and GUI labels. They should not replace the country name.

## Core values

The event should revolve around four visible values.

| Value | Player meaning | Typical sources | Consequences |
| --- | --- | --- | --- |
| Continental legitimacy | Whether the unifier is believed to speak for Africa | defending African countries, winning anti-colonial wars, respecting autonomy, diaspora success | unlocks League votes, integration offers, recognition, and post-unification content |
| League cohesion | Whether League members trust the project | aid, fair burden sharing, defensive victories, low domination pressure | keeps members in the faction and improves joint defense |
| Integration pressure | How much the unifier pushes members toward absorption | focuses, decisions, high legitimacy, occupation success, coercive routes | can create cores, subjects, federated members, rival blocs, or wars |
| Colonial panic | How alarmed outside powers become | liberations, seizure of ports, resource nationalization, post-unification claims | unlocks sanctions, ultimatums, expeditionary plans, and Scramble for Africa reactions |

These values should change through focuses, decisions, missions, wars, state control, AI actions, and evolutions. They should appear in a decision category header, mechanic tooltip, or scripted GUI panel. The player should understand why each value moved without seeing hidden future branches.

## Baseline flow

1. The selected country receives the Africa identity package and a public continental claim frame.
2. The Charter League opens as a defensive anti-colonial project, not as an annexation engine.
3. Existing African states receive early contact events, invitation logic, defensive offers, and influence states.
4. African countries already fighting colonisers can be supported, guaranteed, supplied, or pulled into the League through intervention.
5. Stronger African countries evaluate the unifier and can stay outside, join as equals, form rival blocs, or prepare war.
6. Colonial powers with African holdings receive colonial panic and can try sanctions, guarantees, expeditionary forces, or breakaway sponsorship.
7. Integration opens in stages after legitimacy and League cohesion exist. Annexation and coring require missions and local work.
8. Full continent control triggers the Scramble for Africa reaction package.
9. A fully unified, highly chaotic campaign can unlock the world-end route only after other continent unifiers exist.

## Regional structure

Africa should be divided into playable regions for decisions, focus unlocks, and integration missions. The exact HOI4 state ids belong to implementation, but the design should use these region groups.

| Region group | Purpose |
| --- | --- |
| Nile and Nubia | Sudan, Egypt-adjacent African states, old Nile corridor restorations, river logistics |
| Maghreb and Sahara | North African coastal states, desert routes, Garamantes and caravan powers |
| Western Sahel | Mali, Songhai, Kanem-Bornu, Hausa, Sokoto, Mossi, Futa routes |
| Guinea Coast | Benin, Oyo, Asante, Dahomey, coastal trade states, anti-port interventions |
| Central Forest and Congo Basin | Kongo, Loango, Kuba, Luba, Lunda, river control, forest high-chaos route gates |
| Horn and Red Sea | Aksum, Ethiopia variants, Adal, Harar, Somalia and Red Sea coastal state paths |
| Swahili and Indian Ocean | Kilwa, Zanzibar, Mombasa, Lamu, Comoros, Madagascar, Indian Ocean trade |
| Great Lakes | Buganda, Bunyoro, Rwanda, Burundi, lake corridor politics |
| Southern Plateau | Great Zimbabwe, Mutapa, Rozwi, Barotse, Mapungubwe, resource routes |
| Southern Cape and Highveld | RSA branch, Zulu, Xhosa, Basotho, Swazi, Tswana, settler reactions |

## Tone direction

The baseline should feel researched, proud, unstable, and ambitious. It should not read like a sterile administrative federation. The player should see crowds, rail depots, ports, old capitals, militia camps, League congresses, returning diaspora ships, resource convoys, and local rulers deciding whether this new Africa is liberation or a new overlord.

Humour belongs in leader flavor, absurd high-chaos branches, regnal names, strange units, and hidden routes. The grounded baseline should still leave room for sharp irony and strange local rumours, but it should not turn African politics into a joke.

## Leader-name flavor policy

The required source-language strings are preserved as leader, king, court, council, or regnal flavor. They should not be used in file names, ids, tags, sprite names, event namespaces, or asset names.

Required strings from the user concept:

- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

Additional obscene names should be sourced later with native-speaker or lexicon review. The design intent is that the player sees strange untranslated ruler names, while the joke remains hidden from ordinary English-facing text. The package should not rely on the joke. It should appear as occasional court flavor, monarch regnal lists, high-chaos pretender names, and rare leader pools.
