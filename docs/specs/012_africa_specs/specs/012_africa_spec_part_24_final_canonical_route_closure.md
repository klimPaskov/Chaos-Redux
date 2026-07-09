# 012 Africa spec part 24, final canonical route closure

This file is the final-pass route closure layer. It does not replace the earlier route parts. It tells the implementation agent how to treat the route packs as one coherent focus tree, how route systems should talk to each other, and which remaining route surfaces must not be left shallow.

## Canonical route contract

The Africa unifier focus tree should feel like a living country project, not a reward ladder. The route packs from parts 6, 9, and 17 are the source tree structure. This final closure adds cross-route dependencies, route state handoffs, and branch completion rules.

| Route family | Main promise | Required visible state | Decision system affected | AI route note | Asset motif |
| --- | --- | --- | --- | --- | --- |
| Shared opening | A country receives the continental claim and must prove it can survive the burden | New identity, early legitimacy, League founding path, African capital validation | League founding, first support missions, RSA civil war branch when relevant | AI should stabilize before hard expansion unless high chaos or war pressure is high | Continental seal, railway map, congress hall |
| Federal Charter | Build Africa through negotiated membership and staged federation | League cohesion, member confidence, autonomy promises, consent projects | Charter League target missions, regional integration projects | Preferred by democratic, non-aligned, and cautious AI | Charter, clasped shields, ports and rail |
| Revolutionary Congress | Break colonial holdings through mass politics and anti-colonial war | Revolutionary legitimacy, liberation pressure, sponsor suspicion | Intervention, strike support, anti-colonial courts, liberated member routing | Communist, socialist, and high tension AI can choose it | Red and green banners, printing press, workers and rifles |
| Crown of the Continent | Restore regal continental symbolism without turning the name joke into the event core | Regnal legitimacy, court pressure, restored polities, ruler flavor pool | Coronation missions, palace diplomacy, subject oath projects | Neutrality or monarchist AI only with high legitimacy | Crowns, stools, stelae, regalia |
| Continental Command | Unify by army planning and command control | Command obedience, officer integration, regional army districts | War preparation, depot missions, coercive annexation risk | Fascist, military, and desperate AI can choose it | Staff maps only as props, field columns, depots |
| Sacred Soil | Grounded spiritual and rural route that remains human unless high chaos opens | Land stewardship, local legitimacy, anti-extractive policy, rural militia | Sacred land projects, forest protection, settlement mediation | Conservative or rural AI can choose normal route | Forest edges, rivers, shrines, fields |
| Black Star Return | Diaspora return through ports, settlement, industry, and culture | Returnee capacity, shipping lane safety, reception confidence | Diaspora lanes, settlement missions, industrial cadres | AI only if stable, has ports, and is not losing a naval war | Black star, ships, dock cranes, workshops |
| Deep Green Covenant | High-chaos nature and nonhuman route with strict safety boundaries | Disaster pressure, nonhuman tags, fictional disease pressure, blowback | Nature demands, disaster retaliation, fictional biowarfare pressure | Player-only by default, rare AI only by explicit high-chaos rule | Storm forest, animal silhouettes, impossible rain |
| Post-unification world route | Africa moves from continent unifier to global chaos pole | Scramble reaction, continent unifier diplomacy, world-end gate | Outside-power reaction trees, continent unifier diplomacy, The World route | AI should almost never pursue terminal world route unless world collapse is already active | Globe, continent emblems, fractured treaties |

## Opening route completion

The opening lane must do four things before any hard route can dominate.

1. Select and validate the Africa unifier.
2. Give the unifier a public continental fantasy through claims or claim-like direction.
3. Start the Charter League or equivalent anti-colonial system.
4. Create the first visible tradeoff between consensual integration, revolutionary pressure, royal restoration, command unification, sacred rural legitimacy, and diaspora return.

The implementation should not let the player rush from event fire to full continent cores. The earliest route should give claims, public ambition, first League tools, defensive intervention, and internal problems.

### Opening anchor focus groups

| Working focus group | Purpose | Must unlock | Must not do |
| --- | --- | --- | --- |
| `opening_continental_claim` | Publicly declares the unifier identity | Cosmetic identity, basic claims, first legitimacy value | Instant annexation, full cores, continent-wide free factories |
| `opening_league_call` | Opens Charter League membership | League category, first target selectors, anti-colonial intervention | Forced entry for all African countries |
| `opening_home_front` | Shows the cost of becoming the unifier | Early ideas, stability stress, manpower and logistics pressure | Permanent dead debuffs |
| `opening_route_congress` | Opens route choice | Mutually exclusive route gates and compatible support branches | Hidden route spoilers |
| `opening_rsa_special_case` | Handles RSA-in-Allies civil war | Continental side and loyalist side packages | Simple tag flip when RSA is Allied |

## Cross-route interaction rules

Routes should interact. They should not be isolated columns.

Federal Charter can use Black Star ports to raise confidence. Revolutionary Congress can use diaspora media networks, but its coercive rhetoric should lower some member confidence. Crown of the Continent can restore polities faster, but those polities should demand autonomy and symbolic recognition. Continental Command can win wars quickly, but it should create refusal, rival blocs, and resistance if used as the main integration method. Sacred Soil can calm rural resistance and lower extraction penalties, but it should slow heavy industry unless the player pays a cost. Deep Green can turn disaster pressure into power, but every use creates blowback and makes normal diplomacy worse.

## Focus route closure requirements

Every implemented route needs all of these surfaces.

| Requirement | Acceptance standard |
| --- | --- |
| Route lock | The route should have a visible commitment point and route flags that close incompatible branches |
| Branch payoff | The route must change map play, diplomacy, military rules, League behavior, or integration outcomes |
| Idea lifecycle | Route ideas must upgrade, worsen, or be removed through focuses, missions, or failures |
| Decision unlocks | Each route unlocks at least one decision family that keeps mattering after the focus completes |
| AI weights | AI route choice should depend on ideology, war state, legitimacy, stability, equipment, ports, and chaos |
| Assets | Route icon motifs, national spirit icons, decision icons, and leader or council portraits must be assigned |
| Achievements | At least one difficult achievement should touch each major route family |
| Cleanup | Route invalidation, tag change, civil war, defeat, and world-end state must hide obsolete route decisions |

## Late-route convergence

The tree should allow convergence after the major route has proven itself. Convergence does not mean every route becomes the same. It means the unifier can use shared continental tools while keeping route-specific prices.

| Convergence tool | Federal price | Revolutionary price | Crown price | Command price | Sacred price | Black Star price | Deep Green price |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Continental army standard | Member vote | Congress approval | Court oath | Command order | Rural guard pact | Returnee training cadre | Nonhuman allies cannot use normal standard |
| Regional integration project | Autonomy guarantee | Liberation tribunal | Regnal settlement | Security district | Land compact | Settlement reception quota | Disaster safety gate |
| Outside-power response | Joint diplomatic front | Anti-colonial escalation | Royal envoy web | Military ultimatum | Spiritual protest and rural sanctions | Diaspora lobbying | Impossible weather threat |
| Post-unification world route | Requires member consent | Requires revolutionary legitimacy | Requires dynastic legitimacy | Requires command obedience | Requires land stewardship | Requires returnee capacity | Requires high-chaos world collapse |

## Route failure states

Failure states should keep the tree alive.

Federal failure can create rival federal blocs or member exits. Revolutionary failure can create splinter congresses, exhausted liberated members, or foreign-backed counter-blocs. Crown failure can create succession disputes, restored polity refusals, or pretender courts. Command failure can create rogue regional commands, coercive resistance, or League collapse. Sacred failure can create rural revolt, extraction sabotage, or route lockout. Black Star failure can create reception backlash, shipping losses, or foreign surveillance. Deep Green failure can spread disaster pressure to the unifier and reveal containment decisions.

## Final focus implementation note

The implementation agent owns the final exact focus count and coordinates. The spec requires route depth and interactions, not exact coordinates. The final tree must still produce a route coverage table that maps every route family in this file to implemented focus branches, decision categories, ideas, AI behavior, assets, and achievements.
