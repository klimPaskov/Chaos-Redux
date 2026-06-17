# Achievement Prompt — Event 012 Africa

Use this prompt after implementing the Event 012 Africa mechanics. Achievements should reward mastery, rare routes, difficult coalition management, RSA branch success, high-chaos paths, and world-end preparation. Do not unlock achievements merely because Event 12 fired.

Every achievement needs localisation, tracking flags/variables, icon assets, disqualifiers, and documentation. Use the asset prompt for 64x64 achievement icons and variants.

## Achievement list

| ID | Working title | Visibility | Eligible player | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ach_africa_charter_without_chains` | Charter Without Chains | Visible | Africa unifier | Form United Africa through the Federal Congress route with at least 6 voluntary African members integrated and no forced integration wars against independent African states. | Any offensive war against an independent African member before they leave/resist; Green Covenant takeover. | Hard | Congress seal breaking chains without weapons. |
| `ach_africa_no_second_scramble` | No Second Scramble | Visible | Africa unifier | Trigger the Scramble for Africa crisis and force all outside colonial powers with African holdings to withdraw or accept treaty settlement without losing an African capital. | Losing unifier capital; using World Is One path before settlement. | Hard | Foreign map torn in half by African seal. |
| `ach_africa_paper_to_living` | From Paper to Living Land | Visible | Africa unifier | Convert all African paper cores into stable staged cores through regional integration missions, with Paper-Core Burden below danger threshold at completion. | Instant core fallback, skipped integration, active major regional rebellion. | Very hard | Stack of stamped papers turning into a living city/railway. |
| `ach_africa_one_but_not_alone` | One, But Not Alone | Visible | Africa unifier | Fully unify Africa while retaining at least 5 loyal regional authorities or autonomous members until the final integration choice. | Direct annexation of all members before final focus; cohesion collapse. | Hard | Many regional seals orbiting a central African seal. |
| `ach_africa_rsa_the_union_breaks` | The Union Breaks First | Visible | RSA branch player | If RSA is selected while in the Allies, win as the Continental Proclamation side and trigger Allied peace with Africa. | Leaving Allies before the branch fires through exploit; Allied peace not triggered. | Hard | Split South African parliament with continental banner. |
| `ach_africa_the_allies_sign` | The Allies Sign | Hidden | Africa unifier/RSA branch | Win the RSA civil war as Continental Proclamation and force a treaty with the Allies while keeping Johannesburg/Pretoria, Cape Town, and Durban controlled. | Losing any required city at peace; using console/manual treaty. | Very hard | Allied pen signing under African seal. |
| `ach_africa_elephants_remember` | The Elephants Remember | Hidden | Africa unifier | Unlock elephant or high-chaos heavy animal logistics units through Evolution II/Green Covenant and use them to win a major battle or capture a required regional capital. | Creating elephant units through debug; not completing the focus/decision chain. | Medium-hard | Armoured elephant silhouette with railway badge. |
| `ach_africa_ananse_wrote_the_orders` | Ananse Wrote the Orders | Hidden | Green Covenant/Ananse route | Use the Ananse Web intelligence route to make a colonising power abandon, misdirect, or lose a key operation, then win the linked campaign. | Literal low-effort spy decision without mission outcome; no coloniser target. | Hard | Web over telegrams and masks. |
| `ach_africa_mami_wata_takes_the_port` | The Tide Took the Port | Hidden | Green Covenant/coastal route | Use the Mami Wata/Tidemark route to secure or defend a major port during a Scramble or anti-colonial war. | No high-chaos route; port captured by ordinary event without tide decision/mission. | Hard | Sea-spirit wave curling around a port crane. |
| `ach_africa_forest_guardian_pact` | Do Not Cut the Forest | Hidden | Green Covenant/Congo route | Form a pact with the Forest Guardian/nonhuman actor and defeat an outside extractor/coloniser in the Congo Basin without annexing the nonhuman actor through ordinary integration. | Treating nonhuman actor as ordinary annexed subject; failed pact. | Hard | Forest canopy with watchful eyes. |
| `ach_africa_mansa_musa_would_need_a_bigger_caravan` | A Bigger Caravan | Visible | West African or Crown route | Through the Crown Congress or regional trade route, rebuild a Sahel/West African trade network linking coastal ports, inland rail, and Timbuktu/Gao/Niger corridor before full unification. | No relevant regional control; pure military route only. | Medium-hard | Gold caravan crossing rails. |
| `ach_africa_not_a_map_colour` | Not a Map Colour | Visible | Africa unifier | Unify Africa without using instant full-core shortcuts: every region must have completed at least one trust, administration, or referendum mission before final union. | Any final core conversion without mission history. | Very hard | Paintbrush blocked by charter seal. |
| `ach_africa_congress_over_command` | Congress Over Command | Visible | Federal route | Keep Continental General Staff influence below dominance threshold while defeating at least one major colonising power. | Military route lock-in or emergency command dictatorship. | Hard | Ballot box over command baton. |
| `ach_africa_command_over_congress` | Command Over Congress | Visible | General Staff route | Win the Scramble for Africa crisis through the Continental General Staff route while keeping League Cohesion above collapse. | Cohesion collapse or majority member exit. | Hard | Command baton holding many regional cords together. |
| `ach_africa_return_passages` | Return Passages | Visible | Any unifier with diaspora branch | Complete the diaspora return settlement, officer school, and technical mission chains without triggering a major domestic backlash. | Cancelling the return program after first tier; backlash crisis unresolved. | Medium | Ship manifest, tools, books, officer cap. |
| `ach_africa_the_old_thrones_vote` | The Old Thrones Vote | Hidden | Crown Congress route | Complete the Crown Congress route by winning a legitimacy contest without forcing all regional monarchic/royal authorities by war. | Military coup route, legitimacy failure. | Hard | Crown above ballot circle. |
| `ach_africa_every_capital_heard_the_drum` | Every Capital Heard the Drum | Visible | Africa unifier | Have every major African regional authority represented in the Continental Congress UI before final unification. | Missing region; direct annexation path. | Very hard | Drum sound rings across regional seals. |
| `ach_africa_world_school` | The World School | Hidden | Unified Africa | Sponsor at least three other continental unifier movements to successful post-unification paths before pursuing any cross-continental union. | Annexing/sabotaging sponsored unifier before success. | Very hard | African seal teaching three smaller continent seals. |
| `ach_africa_afro_asian_vector` | Afro-Asian Vector | Hidden | Unified Africa | Form an Afro-Asian or African-Middle Eastern/Asian dynamic union after Africa and the Asian/Middle Eastern unifier secure their regions. | Using a static cosmetic rename without dynamic conditions. | Very hard | Two continental standards crossing over ocean. |
| `ach_africa_afro_eurasian_question` | The Afro-Eurasian Question | Hidden | Unified Africa | Form Afro-Eurasian Union after Africa, Europe, and Asia have secured their continents through the post-unification routes. | Missing one continental route; forcing annex through debug. | Extreme | Three continent seals merging into one impossible standard. |
| `ach_africa_world_is_one` | The World Is One | Secret | Unified Africa world-end route | Trigger the terminal World Is One scenario only after all continent unifiers exist, complete post-unification paths, unlock their world-end route, and extreme chaos is active. | Any missing continent unifier; earlier world-end branch; manual bypass. | Extreme/terminal | World globe made of continent seals under final charter. |
| `ach_africa_no_false_beasts` | No False Beasts | Hidden/meta QA achievement if system supports | Any | Complete a Green Covenant/nonhuman route where all nonhuman actors are explicitly nonhuman/supernatural and no human African country is assigned an animal identity. | Any unsafe localisation/identity pairing. | QA/hidden | Human congress seal beside separate forest spirit seal. |

## Implementation tracking notes

- Achievements that require “no instant core shortcut” need flags on every region when a valid integration mission completes.
- Achievements tied to voluntary members need to distinguish voluntary accession from forced integration after war.
- RSA achievements must confirm RSA was in the Allies at branch start.
- Nonhuman achievements must check shared nonhuman classification and that ordinary country integration did not run on those actors.
- World-end achievement must verify every continent unifier’s own post-unification and world-end unlock flags, not only their existence.
- Dynamic union achievements must check the union’s actual dynamic name/identity branch, not a cosmetic rename alone.

## Icon production notes

Use `chaosx_icon_artist` for achievement icons. Each completed icon is 64x64. Create grey and not-eligible variants if the existing achievement system requires them. Do not derive achievement icons by resizing focus or idea icons; they need their own achievement composition.

## Documentation notes

When achievements are implemented, update the Event 012 documentation and any achievement registry/docs. The completion report must list all implemented achievements, any staged/queued achievements, and any disqualifier logic omitted or simplified.


## Revision 2 expansion requirements

Also implement the expanded source files:

- `specs/012_africa_niche_polities_and_subjects.md`
- `specs/012_africa_high_chaos_absurd_paths.md`
- `matrices/012_africa_expanded_subject_matrix.md`
- `matrices/012_africa_absurd_high_chaos_routes_matrix.md`

The implementation must add the Legacy Authority Lane, Authority Register decisions, Integration Temperature/trust/resistance model, Priority A historical authorities, as many Priority B authorities as needed for regional depth, and high-chaos Covenant actors with explicit nonhuman/supernatural classification. Do not collapse this into generic modifiers, placeholder tags, or one broad “native authority” subject.


## Revision 2 achievement additions

Add these achievement designs:

| Working id | Title | Core unlock | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- |
| africa_forest_votes_no | The Forest Votes No | Defeat a colonial Scramble offensive after Gorilla Nation issues Tree Line Ultimatum without losing protected forest capitals. | no Gorilla Nation, no Scramble offensive, protected capital lost | hard/hidden | gorilla hand over broken survey chain |
| africa_who_gave_them_a_microphone | Who Gave Them a Microphone? | Use Hyena Radio Dominion to misdirect three colonial offensives and survive fake-news backlash. | League Cohesion collapse, Hyena rogue takeover | hard/secret | hyena silhouette and radio microphone |
| africa_gentle_veto | The Gentle Veto | Use Bonobo Kinship Congress to prevent war between a human authority and nonhuman Covenant actor. | war fires anyway, Bonobo actor destroyed | medium-hard/hidden | open hand/branch with peace seal |
| africa_bird_was_right | The Bird Was Right | Bird of the Walls predicts a major invasion/offensive and Africa defeats it within the warning window. | false omen, warning ignored | hard | stone bird over air-warning beam |
| africa_no_ivory_treasury | No Ivory Treasury | Complete Great Herd route without exploitative ivory/resource decisions and defeat a colonial forest holder. | any ivory exploitation flag | hard | elephant and broken coin |
| africa_treaty_with_teeth | A Treaty With Teeth | Bind Crocodile Admiralty and Mami Wata Tidemark, then force colonial port abandonment through warning chain. | port taken by normal conquest before warning completes | hard/hidden | crocodile eye and tidal seal |
| africa_world_has_roots | The World Has Roots | Complete World Root Mandate after unified Africa and at least two other continent unifiers complete post-unification paths. | World Root route not chosen, other unifiers absent | very hard/secret | baobab roots wrapping globe |

## Archive and Bestiary achievement additions

Implement the additional Archive/Bestiary achievements listed below and in this prompt:

- `ACH_AFR_ARCHIVE_OF_OLD_SEATS`
- `ACH_AFR_NO_COUNTERFEIT_CROWNS`
- `ACH_AFR_THE_FOREST_SIGNED_BACK`
- `ACH_AFR_BAOBAB_FILIBUSTER`
- `ACH_AFR_KILWA_TO_KUSH_LEDGER`
- `ACH_AFR_OLD_SEATS_NEW_UNION`
- `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES`

Add tracking flags/variables for peaceful dossier maturation, forgery disqualifiers, nonhuman loyalty, monument/state retention, old-seat chamber status, and World Is One + impossible-signatory conditions. Achievement icons are part of the asset prompt.

## Archive and Bestiary achievement detail table

## Archive and Bestiary achievements addendum

| ID | Title | Difficulty | Visibility | Unlock direction | Disqualifiers | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `ACH_AFR_ARCHIVE_OF_OLD_SEATS` | Archive of Old Seats | Hard | Visible | As Africa unifier, peacefully settle at least 12 historical dossiers across at least 5 macro-regions before full African unification. | Any direct Archive settlement. | Open archive cabinet with continent-shaped seals. |
| `ACH_AFR_NO_COUNTERFEIT_CROWNS` | No Counterfeit Crowns | Very hard | Visible | Fully unify Africa through the respectful Archive route, complete the Archive guard mission, and keep Old-Seat Legitimacy at least 48. | Any direct Archive settlement, failed direct Archive seal, exposed forged lineage, or Counterfeit Crowns super-event. | Clean seal beside broken false crown. |
| `ACH_AFR_THE_FOREST_SIGNED_BACK` | The Forest Signed Back | Hard | Hidden | Recognize Gorilla Highlands, Chimpanzee Telegraph, and Okapi Forest, bind all three actors to the Charter, secure at least three Bestiary habitat seats, complete their actor actions, and keep them loyal through unification. | Direct Archive settlement or counterfeit exposure. | Forest council seal with nonhuman silhouettes. |
| `ACH_AFR_BAOBAB_FILIBUSTER` | Baobab Filibuster | Medium-hard | Hidden | Recognize the Baobab Senate, bind it to the Charter, complete Bestiary containment, convene Baobab memory arbitration, keep the Baobab Senate intact, and still complete unification. | Baobab Senate capitulation or counterfeit exposure. | Ancient tree over a parliamentary desk. |
| `ACH_AFR_KILWA_TO_KUSH_LEDGER` | Kilwa to Kush Ledger | Hard | Visible | Complete the Archive guard mission and settle the Kush/Meroe, Aksum, Kilwa or Swahili Coast, and Great Zimbabwe dossier chain in the same run. | Missing any required dossier settlement. | Coral port, stone enclosure, stela, and pyramid in one ledger. |
| `ACH_AFR_OLD_SEATS_NEW_UNION` | Old Seats, New Union | Very hard | Hidden | Proclaim a dynamic cross-continent union while the respectful Archive route, Continental Register, Old-Seat Legitimacy at least 48, and peaceful macro-regional dossier settlements remain intact. | Direct Archive settlement, forced central seal route, or counterfeit exposure. | Continental union seal surrounded by small old-seat emblems. |
| `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES` | The Charter Has Too Many Signatures | Extreme | Secret | Reach the World Is One branch with human old seats, all Bestiary package outcomes, nonhuman delegations, and at least one supernatural court still recognized. | Missing continent-unifier certification, historical dossier threshold, or any Bestiary package outcome. | Overcrowded treaty page with human, animal, and impossible marks. |
