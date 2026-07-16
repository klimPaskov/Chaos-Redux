# Event 012 host first-proof exactness handoff

## Scope and implementation status

This tranche owns only the Event 012 first-proof ledger and exact target contract:

- `common/scripted_triggers/012_africa_proof_triggers.txt`
- `common/scripted_effects/012_africa_proof_effects.txt`

Every one of the 51 matrix rows now has an explicit country-partner allow-list, an exact installed-map homeland registry, and at least one bounded full-result action sequence. Country actions cannot use an unrelated African target. State and region actions cannot use acquired territory. The only external state actions are the named dossier cases: Dahomey in Oyo/Edo state 558, Senegal/FWA's inland council, French Equatorial Africa's inland council, the Ruanda-Urundi counterpart, and Mauritania's physical Dakar port in Senegalese state 272.

Primary partial, failure, or cancellation still ends the first mandate and opens the existing recovery contract. Auxiliary actions remain retryable. Partner-corridor and physical-state-corridor credits remain separate arrays and separate minima.

## Exact map and registry evidence

The state lists were rebound against the installed vanilla histories under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/`. All 113 state IDs referenced by the homeland trigger exist in the installed build. The 52 original tags used by the partner allow-lists all exist in vanilla or Chaos Redux country-tag files.

The Event 6 source of truth is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`:

| Playbook | Installed evidence | First-proof representation |
|---|---|---|
| Gold Coast | Asante is bound to broad Ghana state 274; Fante has no distinct current state | state 274 plus Asante and northern-authority seats |
| Sierra Leone | colony and protectorate share state 700 | state 700 plus colony and protectorate seats |
| Uganda | Buganda is bound to state 548; Bunyoro and Ankole are rejected as non-distinct substates | state 548 plus Buganda, Bunyoro, and Ankole/Busoga seats |
| Togo | both former mandate zones share state 777 | state 777 plus British- and French-mandate seats |
| Cameroon | both former mandate zones share state 773 | state 773 plus British- and French-mandate seats |
| Equatorial Guinea | Bioko and Rio Muni share state 297 | state 297 plus Bioko and Rio Muni seats |
| Eritrea | highland and lowland institutions share state 550 | state 550 plus highland and lowland seats |
| Comoros | FAX is confirmed on the single Comoro Islands state 708 | state 708 plus Grande Comore, Anjouan, Mohéli, and Mayotte seats; state 708 port transport remains separately mandatory |

The named seats are country flags awarded only after the relevant exact state action resolves in full. They do not inflate the distinct-state array.

Physical evidence remains live rather than historical:

- rail-state evidence requires the operational project flag and a live capital-to-state railway;
- `connect_member_capitals` evidence requires a live capital-to-capital railway;
- river and lake evidence requires a state in the curated Event 012 waterway registry;
- port evidence requires an existing coastal naval-base site and the operational port flag.

Installed port history was checked for the witness sites, including 268, 269, 272, 274, 296, 297, 446, 447, 458, 543, 544, 546, 550, 559, 700, 705, 708, 773, 776, 844, and 897. Mauritania states 557 and 786 contain no naval base. Its proof therefore targets the real Dakar naval base in Senegalese state 272; no paper Mauritanian port or unrelated fallback state is admitted.

## One exact launch witness per matrix row

The sequences below assume each listed action resolves in full. A bracketed state list is one deliberate region selection. Unless a country target is written before the state, the state action targets the host itself.

| Host row | Exact full-result witness sequence |
|---|---|
| Ethiopia | `deploy_volunteers(SUD at war)` → `connect_member_capitals(SUD)` |
| Egypt | `guarantee_sovereignty(SUD)` → `dispatch_charter_mission(SUD)` → `convene_regional_congress(446)` → `modernise_continental_port(446)` |
| Sudan | `expand_river_transport(551)` → `guarantee_regional_representation([549,551])` → `guarantee_sovereignty(EGY)` |
| Morocco | `settle_overlapping_claims(290)` → `dispatch_charter_mission(ALG)` |
| Algeria | `convene_regional_congress([459,460])` → `build_regional_rail_spine(513)` → `open_aid_corridor(TUN)` |
| Tunisia | `convene_regional_congress(458)` → `modernise_continental_port(458)` → `open_aid_corridor(ALG)` |
| Libya | `build_regional_rail_spine(449)` → `convene_regional_congress(448)` → `open_aid_corridor(TUN)` |
| Liberia | `resource_sovereignty_review(298)` → `guarantee_sovereignty(SIE)` → `open_aid_corridor(SIE)` |
| Nigeria | `build_regional_rail_spine(900)` → `guarantee_regional_representation([558,901,902])` → `open_aid_corridor(GHA)` |
| Gold Coast | `modernise_continental_port(274)` → `guarantee_regional_representation(274)` → `resource_sovereignty_review(274)` → `open_aid_corridor(IVO)` |
| Senegal and FWA | `open_aid_corridor(MLI)` → `guarantee_regional_representation(MLI:556)` → `modernise_continental_port(272)` |
| Sierra Leone | `settle_overlapping_claims(700)` → `modernise_continental_port(700)` → `open_aid_corridor(LIB)` |
| Belgian Congo | `expand_river_transport(295)` → `resource_sovereignty_review(295)` → `open_aid_corridor(ANG)` |
| Angola | `build_regional_rail_spine(796)` → `resource_sovereignty_review(540)` → `dispatch_charter_mission(COG)` |
| French Equatorial Africa | `open_aid_corridor(CMR)` → `guarantee_regional_representation(CMR:773)` → `expand_river_transport(772)` |
| Kenya | `settle_overlapping_claims(904)` → `build_regional_rail_spine(905)` → `open_aid_corridor(UGA)` |
| Uganda | `settle_overlapping_claims(548)` → `expand_river_transport(548)` → `open_aid_corridor(KEN)` |
| Tanganyika | `connect_member_capitals(KEN)` → `expand_river_transport(546)` → `open_aid_corridor(KEN)` → `settle_overlapping_claims(546)` |
| Somali territories | `hold_accession_referendum(ETH)` → `open_aid_corridor(ETH)` → `modernise_continental_port(559)` |
| Madagascar | `settle_overlapping_claims(543)` → `modernise_continental_port(543)` → `open_aid_corridor(MZB)` |
| South Africa | constitutional route: `convene_regional_congress(275)` → `guarantee_sovereignty(BOT)` → `settle_overlapping_claims(541)` → `build_regional_rail_spine(719)` → `connect_member_capitals(BOT)` |
| Southern Rhodesia | `settle_overlapping_claims(545)` → `connect_member_capitals(ZAM)` |
| Portuguese Guinea | `open_aid_corridor(SEN)` → `expand_river_transport(296)` → `modernise_continental_port(296)` → `guarantee_regional_representation(296)` |
| Cape Verde | `open_aid_corridor(SEN)` → `resource_sovereignty_review(702)` |
| Gambia | `dispatch_charter_mission(SEN)` → `expand_river_transport(701)` → `settle_overlapping_claims(701)` |
| Côte d’Ivoire | `connect_member_capitals(GHA)` → `resource_sovereignty_review(779)` |
| Dahomey | `settle_overlapping_claims(NGA:558)` → `modernise_continental_port(776)` |
| Togo | `settle_overlapping_claims(777)` establishes both mandate seats |
| French Sudan or Mali | `connect_member_capitals(SEN)` → `expand_river_transport(556)` |
| Mauritania | `open_aid_corridor(SEN)` → `modernise_continental_port(SEN:272)` |
| Niger | `open_aid_corridor(MLI)` → `expand_river_transport(781)` |
| Upper Volta | `dispatch_charter_mission(GHA)` → `guarantee_regional_representation(778)` |
| Chad | `expand_river_transport(774)` |
| Cameroon | `settle_overlapping_claims(773)` → `modernise_continental_port(773)` |
| Gabon | `connect_member_capitals(CMR)` → `resource_sovereignty_review(539)` |
| Equatorial Guinea | `guarantee_regional_representation(297)` → `modernise_continental_port(297)` → `open_aid_corridor(CMR)` |
| São Tomé and Príncipe | `open_aid_corridor(GAB)` → `modernise_continental_port(705)` → `settle_overlapping_claims(705)` |
| Ruanda-Urundi | Rwanda-host witness: `settle_overlapping_claims(768)` → `settle_overlapping_claims(BRD:769)` → `expand_river_transport(768)` |
| Northern Rhodesia | `resource_sovereignty_review(771)` → `build_regional_rail_spine(981)` → `connect_member_capitals(MZB)` |
| Nyasaland | `expand_river_transport(770)` → `settle_overlapping_claims(770)` |
| Mozambique | `open_aid_corridor(TZN)` → `modernise_continental_port(897)` → `settle_overlapping_claims(897)` |
| Bechuanaland | `dispatch_charter_mission(SAF)` → `guarantee_sovereignty(SAF)` → `connect_member_capitals(SAF)` |
| Basutoland | conditional scenario host: `dispatch_charter_mission(SAF)` → `guarantee_sovereignty(SAF)` |
| Swaziland | conditional scenario host: `resource_sovereignty_review(own controlled core capital)` |
| Eritrea | `dispatch_charter_mission(ETH)` → `modernise_continental_port(550)` → `guarantee_regional_representation(550)` |
| French Somaliland or Djibouti | `connect_member_capitals(ETH)` → `modernise_continental_port(268)` |
| Zanzibar | conditional scenario host: `hold_accession_referendum(TZN)` → `open_aid_corridor(TZN)` → `modernise_continental_port(own controlled core capital)` → `guarantee_regional_representation(own controlled core capital)` |
| Mauritius | `open_aid_corridor(MAD)` → `settle_overlapping_claims(707)` → `guarantee_regional_representation(707)` |
| Comoros | `guarantee_regional_representation(708)` → `modernise_continental_port(708)` |
| Seychelles | `offer_defence_charter(MAD)` |
| Réunion | `open_aid_corridor(MAD)` → `guarantee_regional_representation(706)` |

For a Burundi host, the Ruanda-Urundi witness is the exact inverse: settle state 769 at home, settle RWA state 768 through the named counterpart, and establish the registered Lake Tanganyika route in state 769.

South Africa also has a distinct wartime witness: full `contain_regional_secession_war` against one regional war actor, a physical rail project in a non-capital South African state, and a second distinct external African actor. The constitutional witness above instead requires the explicit neighbouring guarantee and land/citizenship settlement.

## External host-binding dependencies

Three rows have exact proof logic but no current-map host binding in Event 6:

- HZX Basotho: `disabled_no_unique_current_state`
- EUX Eswatini: `disabled_no_unique_current_state`
- ELX Zanzibar: `scenario_only_unbound`

The proof trigger deliberately accepts only each living host's own controlled core capital for these rows. It does not borrow South African, Tanganyikan, or other acquired territory. Their witness sequences are executable when a scenario or later package creates the host, but they cannot be selected as current-map Event 12 hosts until Event 6 or a map package supplies an authoritative binding. Resolving those bindings is outside this tranche and no fallback was introduced.

## Validation evidence and remaining risk

- Parsed 51 profile blocks and 51 distinct matrix keys.
- Parsed 51 unique country-partner branches and 51 unique homeland-state branches.
- Confirmed every referenced state ID and original tag exists in the installed vanilla/mod sources.
- Confirmed all 48 corridor-requiring profiles occur exactly once in the partner-only, state-only, or both-minima tables; the three profiles without corridor requirements are Morocco, Togo, and Swaziland.
- Compared all 51 witness rows against their executable profile: every action is admitted, every country target is in the row allow-list, every unprefixed state is in the row homeland registry, and every primary, actor, region, corridor, domestic-settlement, and reform minimum is met.
- Confirmed the seven state-rail witnesses use installed non-capital states: Algeria 513, Libya 449, Nigeria 900, Angola 796, Kenya 905, South Africa 719, and Northern Rhodesia 981.
- Checked the curated river/lake registry against every water-route witness and the installed naval-base histories against every port witness.
- The HOI4 map MCP could not build its workspace model because the installed map exceeded its fixed 500,000-domain-record ceiling by 21 records (`MAP_MODEL_BUDGET_BLOCKED`). Direct vanilla state histories and the Event 6 installed-map binding registry provided the authoritative evidence instead.

No gameplay simplification or generic target fallback was used. The only unresolved items are the three external Event 6 host bindings listed above.
