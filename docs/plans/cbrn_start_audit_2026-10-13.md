# CBRN starting-position audit, 13 October 2026

This is the current D1–D4 work report for the owner's restoration plan.
The owner explicitly authorized these four items on 13 October 2026, prohibited questions, pushes and game launches, and required exact historical restoration wherever earlier content exists.
Historical knowledge, a usable research staff, an offensive programme, manufactured delivery equipment, and an abstract game stockpile are separate claims in this audit.
The historical bookmarks are 1 January 1936 and 14 August 1939, both at noon, from the installed `common/bookmarks/the_gathering_storm.txt` and `blitzkrieg.txt`.

## D1: starting breakthroughs

Implemented in `aa75244feb4062279c64e4d89f725481f414011b`.
`33b6946dd923b9fc90fbf29bc5798dce3c76a76f` removed the British and American `add_breakthrough_progress` bodies and changed their constants from 0.6 and 0.5 to zero.
Their grant bodies are restored exactly from `33b6946dd^`, with their existing constant references retained.
The owner explicitly requests 1.0, so Britain, America and the USSR receive that value rather than the earlier fractional values.
Japan's 1.0 was already present before and after that commit and remains unchanged.
Germany, Britain and France receive one chemical breakthrough through the same native effect and central constants.
No earlier chemical-specialty grant was removed by the identified change; those three grants implement D1's explicit request.
Both bookmarks use these grants, with the existing global one-time guard preventing duplicate application.

This is the owner's starting-balance policy, not a claim that the British and American wartime offensive biological programmes existed in January 1936.
The [U.S. Army programme history](https://history.army.mil/portals/143/Images/Publications/catalog/10-1.pdf) dates the American wartime organization to 1942 and Camp Detrick to 1943.
The [Imperial War Museums Porton Down record](https://film.iwmcollections.org.uk/record/25572) places the British biological team in 1940.
No completed anthrax project or biological payload stockpile is inferred from a breakthrough point.

## D2: historical knowledge and staff corrections

Implemented in `06854613105439614eb6111e1e91a51096e9e808`.
Germany's unconditional `tabun = 1` line is restored from `33b6946dd^`.
The offending commit is `33b6946dd`, which removed that line and substituted a date-gated grant.
The owner's explicit request takes precedence over the discovery date: this grants knowledge at January 1936 even though the [Max Planck Institute history](https://www.mpiwg-berlin.mpg.de/KWG/projects.htm) places discovery in late 1936.
No tabun stockpile is granted.
The same institutional history dates sarin to 1938, supporting a knowledge-only German grant for the 1939 bookmark.
The sarin project remains a separate production-development route; no sarin lots or completed project are granted.

The U.S. `phosgene` and `livens_projector_tech` grants apply to both bookmarks.
`aded4d2dd` introduced the later-bookmark phosgene grant without an earlier unconditional American line to restore.
The [U.S. defence history](https://www.denix.osd.mil/rcwmprogram/history/) records phosgene knowledge and production during the First World War, retained interwar stocks, and Livens standardization in 1924.
The 1937 phosgene plant upgrade is not the first discovery of the agent.
Existing U.S. mustard reserves remain 240 abstract lots in 1936 and 320 in 1939; the latter is the previously accepted game allocation associated with renewed production, not a conversion from historical tonnage.

Japan receives lewisite knowledge at both starts.
The [Operation Lewisite report reproduced by an institutional conference paper](https://www.irpa.net/irpa10/cdrom/00280.pdf), pages 3–4, documents pre-1937 manufacture and its subsequent expansion.
Japan receives phosgene knowledge in 1939, supported by the former Army's agent categories in the [Japanese Cabinet Office record](https://wwwa.cao.go.jp/acw/en/heiki.html) and the [U.S. Army interwar history](https://www.usanca.army.mil/Portals/114/CWMD_Journal/CWMD%20Journal%20Issue%208.pdf).
Those records do not establish a precise January 1936 phosgene entitlement, so none is invented.
The precise first Japanese phosgene date remains uncertain; the 1939 knowledge grant is a bookmark-level inference from the established wartime programme.
No extra Japanese agent or filled-payload lots are created.

The imported-mask profiles skip domestic `basic_gas_masks`, while `gas_mask_equipment_1` is inactive until unlocked.
Offline Effects line 2253 states that the producer must have the equipment unlocked for a stockpile grant to succeed.
`726103283` introduced the imported-mask profile without an explicit producer, and `33b6946dd` introduced the historical reconciliation with the same missing producer context.
Neither supplies an earlier working producer line to restore.
It preserves domestic producers for countries with the technology and supplies `producer = ENG` for imported basic crates, after Britain has received the technology.
This keeps the existing issue/reserve quantities and avoids granting importers a domestic industry.
The British producer token is game stockpile bookkeeping, not a historical assertion that all these countries imported from Britain; exact national shipment provenance is unavailable.
The ordinary fixed-profile route is outside these two historical bookmark reconciliations.

Poland receives mustard knowledge at both bookmarks.
The [Polish Army Land Forces Museum's interwar exhibit](https://muzeumwl.pl/en/polish-army-between-1914-and-1939/) documents chemical-war preparations and a mustard canister.
This supports knowledge; it does not supply a defensible stock quantity, filled payload count or factory allocation.

The 67-character A11 roster, skill and trait restoration remains the research-potential policy for living scientists.
No career or programme locks are reintroduced.
Two people were deceased by the 1939 bookmark: [John Scott Haldane](https://catalogues.royalsociety.org/CalmView/Record.aspx?id=NA2292&src=CalmView.Persons), who died on 15 March 1936, and [Ivan Velikanov](https://academic.oup.com/book/4364/chapter-abstract/146298118), executed in April 1938, corroborated by the [Institute for the History of Science and Technology record](https://ihst.ru/projects/sohist/repress/kom/1938/velikanov.htm).
Startup retires them when the selected bookmark is after their deaths.
They retain their January 1936 roles, ratings, traits, original portraits and original identity tokens.
This is a bookmark correction; no periodic death or recruitment hook is added.
All 67 are recruited in history, with 65 remaining available at the 1939 start.

The seven chemical reserves are existing game abstractions.
There is no real-world mass-per-lot conversion from which exact historical national inventory could be calculated.
Their presence is consistent with the established chemical capabilities of those states; their exact sizes are retained rather than rewritten as invented historical quantities.
[Italian chemical use in the 1935–36 Ethiopian war](https://history.state.gov/historicaldocuments/frus1936v03/d85) confirms Italy's capability at the first bookmark.
The [Italian Ministry of Defence institutional history](https://www.difesa.it/smd/entimi/scuolanbc/la-storia/34082.html) documents its interwar chemical service.
The [WHO historical survey](https://iris.who.int/bitstream/handle/10665/42611/9241546158.pdf?sequence=1), page 148, describes phosgene and mustard as the main chemical stockpiles at the outbreak of the Second World War.

## D3: Japan's initial authorization

Implemented in `aa75244feb4062279c64e4d89f725481f414011b`.
Japan starts at `constant:cbrn_use_policy.unrestricted_authorization` through the existing `cbrn_set_use_policy` setter, and records its peak policy and unrestricted history receipt.
The initializer only supplies a default when the variable is absent and preserves valid unrestricted level 5.
The battlefield, strategic and extreme-use policy triggers therefore all pass for Japan at startup.
No earlier Japan-specific unrestricted initialization was found in the startup-helper history.
This is D3's requested addition, rather than a claimed restoration.
Other countries retain their existing initial authorization.

## D4: CBRN traits

The offending historical balance commit is `33b6946dd923b9fc90fbf29bc5798dce3c76a76f`.
All 31 current constants that exist in its parent `4efc01fc87f1137e98c864f928dd5603e6b7d2f1` match that parent exactly, including the stronger offensive and medical factors.
The comparison includes unchanged condemnation/detection constants as well as the restored values; it does not describe 31 separate balance changes.
Five biological/medical operational tooltip bodies also match the parent exactly.
The two chemical tooltips retain their accurate current wording with the restored numbers because the old bodies advertised retired readiness-gain and readiness-expenditure mechanics.
Those readiness clauses and the retired generic programme-director office are not restored: they have no current operational consumer, and rebuilding those retired systems is outside this trait correction.
This is a limit on full historical restoration, not a claim of byte-exact whole-file restoration.
The newer aerobiology and three defensive appointments had no stronger earlier version; their own CBRN consumers receive stronger values under D4's explicit authorization.

| Trait | Earlier/current weak bonus | Implemented CBRN bonus |
| --- | --- | --- |
| Operations Specialist / Expert / Genius | 1% / 3% / 4% general planning speed | 20% / 30% / 40% less chemical/biological death and medical saturation in controlled states, and less preparation for all five HQ orders |
| Chemical Operations Commander | Four cylinder abilities and 30% HQ preparation reduction | Same abilities/preparation, plus Chemical Projector Battery +25% soft attack and breakthrough |
| Biological Operations Veteran | One generic defence skill level | Medical Countermeasure and Biosecurity Assault Detachments +30% organisation and defence |
| Hazard Warfare Veteran | One generic logistics skill level | Ten CBRN regimental components consume 25% less supply |
| Protected Assault Expert | 5% less general out-of-supply penalty | Chaos Battalion and Biosecurity Assault Detachment +25% soft attack and breakthrough |
| Theatre Containment Organizer | One army-group command slot | Same slot, plus Mask/Decontamination and Medical Detachments +25% defence |

Only the highest appointed Operations rank applies; hiring multiple ranks or duplicate rank-3 officers does not multiply these staff bonuses.
The existing preparation and response floors remain in the consumers.
The new staff tooltip percentages read the same three shared constants that drive gameplay.
The stat bonuses name existing consolidated CBRN sub-unit tokens, with no new unit, technology, icon, country package or periodic hook.
Unchanged native AI blocks retain their former appointment scores.
The [commander guide](../systems/cbrn_warfare/cbrn_commander_progression.md), [historical advisor guide](../systems/cbrn_warfare/cbrn_historical_advisors.md), [doctrine guide](../systems/cbrn_warfare/chaos_warfare_doctrine.md), and existing [CBRN effect registry](../../common/scripted_effects/cbrn_scripted_effects.md) describe the consumers and tooltip bindings.
Chemical contamination and medical-saturation outputs are initialized in their caller so the nested advisor effects return into the later action calculation.

The architect's 21 actual-source subset scenarios checked no staff, each rank, mixed ranks, duplicate ranks, removal/defaults, controller routing and nested temporary outputs.
An unadjusted ten-day HQ preparation resolves to seven days with the commander alone, then six/five/five days with specialist/expert/genius under the existing floor.
Genius plus Medical Pioneer produces raw chemical 0.42 and biological medical 0.39 factors before the combined response floor.
The existing chemical receipt regression passed 43 tests across 89 production helpers in the specialist's review.
The parent additionally checked every named unit modifier against the unique consolidated definition and rechecked the historical constants and five exact tooltip bodies against Git.
These are source checks; native modifier aggregation, field-marshal inheritance and tooltip rendering were not observed in game.

The independent probability auditor checked the restored spread factors against both source revisions and the actual lifecycle formula.
The scenarios hold environment, countermeasures and containment neutral, use no repeated-seed bonus, and condition on an eligible target already selected for an attempt.
The two weights sum to 100, so the normalized share equals the spread weight; this is not an unconditional state-selection or campaign forecast.

| Named scenario | Before spread / no spread | After spread / no spread |
| --- | --- | --- |
| JAP 1936, Ishii, fictional game anthrax intensity 50 | 28.05 / 71.95 | 38.50 / 61.50 |
| JAP 1943, Ishii + Kitano, same intensity | 28.611 / 71.389 | 50.05 / 49.95 |
| USA 1943, Baldwin + Olson, same intensity | 28.05 / 71.95 | 34.375 / 65.625 |
| JAP 1943, Ishii + Kitano, fictional plague intensity 100 | 80 / 20 | 80 / 20 |
| No hired offensive advisor control | 27.5 / 72.5 | 27.5 / 72.5 |

The paired Japanese stack is 1.40 × 1.30 = 1.82, restoring a meaningful strength increase; the existing 80% cap retains a positive no-spread branch.
Scenario dates do not grant or hire advisors: doctrine, capability and project appointment requirements must also be satisfied.
The immutable before/current fixture hashes were checked by the independent auditor; the probability fixture SHA-256 is `79bbe8aefae55db727c226056038e2dafc7a70ae019030cbb0e9ea92117bb260`.
The baseline is `aa75244feb4062279c64e4d89f725481f414011b`, and the historical restoration source remains `33b6946dd^`.

The probability inspector's initial `direct_random` discovery found no surface; its one corrected `random_list` inventory found the four dynamic lifecycle entries and reported `poolComplete = false` with unresolved runtime weights.
The calculations above come from the actual source, not an MCP scenario evaluation.
The corrected inventory artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19ddbc55b21a597a6e013e8dd3f82b74100f3354164890f329f3f7b3cb8975f0/66aa00cab9b7aedef15f8add684b5b5c240fd2e5295b6792473731c16fe82e1f/probability-inspect-4c1ad9bf8864.json`, source revision `dffe1506fb7e112e23372e9861187d0594249143d99072c34437a2fa930b3ea6`.
No further analyzer retry was attempted against those unchanged unresolved inputs.

## Complete country coverage

The source inventory covered all 617 registered country tags in the combined installed-game and current mod tag registries.
All country-history files were searched for CBRN technology, equipment and staff grants; the ordinary national setup is dispatched by 25 explicit helpers, and 41 countries have mask profiles.
There are 42 distinct tags in their union because Liberia's support-equipment setup has no mask-profile row.
The table below covers every tag with a CBRN or related compatibility startup entitlement.
All amounts are game lots; the U.S. mustard pair means 1936/1939.
All other listed stock and technology entries apply at both starts where the country exists.
The two technology columns show the union of the country's helper and mask-profile technology grants, including the fitting/filter technologies awarded by the improved-mask completion effect.

Technology abbreviations: M1 basic masks, M2 improved masks, Fit civil fitting/registration, Filters military filter standardization, W1 portable anemometer, W2 meteorological stations, H pathogen handling, B surveillance, L Livens projectors, Cl chlorine, P phosgene, M mustard, Le lewisite, GA tabun, GB sarin.
`Import` means a protective stock entitlement without domestic mask-production research.
`Support` is Liberia's conventional support-equipment compatibility grant.
Civilian/military protective research is not an offensive-agent or biological bomb entitlement.

| Tag | 1936 technologies | 1939 technologies | Chemical agent lots | Military mask issue / reserve | Scientists 1936 / 1939 |
| --- | --- | --- | --- | --- | --- |
| ARG | Import | Import | None | 25% / 25% | 0 / 0 |
| AST | M1 W1 | M1 W1 | None | 25% / 25% | 3 / 3 |
| AUS | M1 | M1 | None | 25% / 25% | 0 / 0 |
| BEL | M1 Fit M2 Filters H W1 | M1 Fit M2 Filters H W1 | None | 25% / 25% | 0 / 0 |
| BRA | Import | Import | None | 25% / 25% | 0 / 0 |
| BUL | M1 | M1 | None | 25% / 25% | 0 / 0 |
| CAN | M1 H W1 | M1 H W1 | None | 25% / 25% | 3 / 3 |
| CHI | Import | Import | None | 25% / 25% | 0 / 0 |
| CHL | Import | Import | None | 25% / 25% | 0 / 0 |
| CZE | M1 H W1 | M1 H W1 | None | 25% / 25% | 0 / 0 |
| DEN | M1 | M1 | None | 25% / 25% | 0 / 0 |
| ENG | M1 B Cl Fit M2 L W2 Filters M H P W1 | M1 B Cl Fit M2 L W2 Filters M H P W1 | Cl 720; P 480; M 840 | 75% / 25% | 14 / 13 |
| FIN | M1 | M1 | None | 25% / 25% | 0 / 0 |
| FRA | M1 Cl Fit M2 L W2 Filters M H P W1 | M1 Cl Fit M2 L W2 Filters M H P W1 | Cl 540; P 540; M 840 | 75% / 25% | 2 / 2 |
| GER | M1 B Cl Fit M2 L W2 Filters M H P W1 GA | M1 B Cl Fit M2 L W2 Filters M H P W1 GB GA | Cl 360; P 600; M 720 | 75% / 25% | 15 / 15 |
| GRE | M1 | M1 | None | 25% / 25% | 0 / 0 |
| GXC | Import | Import | None | 25% / 25% | 0 / 0 |
| HOL | M1 Fit M2 Filters H W1 | M1 Fit M2 Filters H W1 | None | 25% / 25% | 0 / 0 |
| HUN | M1 | M1 | None | 25% / 25% | 0 / 0 |
| ITA | M1 Cl L M H W1 | M1 Cl L M H W1 | Cl 480; M 360 | 100% / 25% | 0 / 0 |
| JAP | M1 B Cl Le L M H W1 | M1 B Cl Le L M H P W1 | Cl 480; M 420 | 50% / 25% | 4 / 4 |
| LIB | Support | Support | None | None | 0 / 0 |
| MAN | Import | Import | None | 25% / 25% | 0 / 0 |
| MEX | Import | Import | None | 25% / 25% | 0 / 0 |
| NOR | M1 | M1 | None | 25% / 25% | 0 / 0 |
| NZL | M1 W1 | M1 W1 | None | 25% / 25% | 0 / 0 |
| POL | M1 M W1 | M1 M W1 | None | 25% / 25% | 3 / 3 |
| POR | M1 | M1 | None | 25% / 25% | 0 / 0 |
| PRC | Import | Import | None | 25% / 25% | 0 / 0 |
| RAJ | M1 W1 | M1 W1 | None | 25% / 25% | 0 / 0 |
| ROM | M1 | M1 | None | 25% / 25% | 0 / 0 |
| SAF | M1 W1 | M1 W1 | None | 25% / 25% | 0 / 0 |
| SHX | Import | Import | None | 25% / 25% | 0 / 0 |
| SIK | Import | Import | None | 25% / 25% | 0 / 0 |
| SOV | M1 Cl L W2 M H P W1 | M1 Cl L W2 M H P W1 | Cl 720; P 480; M 960 | 75% / 25% | 9 / 8 |
| SPR | M1 M W1 | M1 M W1 | None | 25% / 25% | 0 / 0 |
| SWE | M1 | M1 | None | 25% / 25% | 0 / 0 |
| TUR | M1 | M1 | None | 25% / 25% | 0 / 0 |
| USA | M1 B Cl Le L W2 M H P W1 | M1 B Cl Le L W2 M H P W1 | Cl 360; M 240/320; Le 600 | 75% / 25% | 14 / 14 |
| XSM | Import | Import | None | 25% / 25% | 0 / 0 |
| YUG | M1 | M1 | None | 25% / 25% | 0 / 0 |
| YUN | Import | Import | None | 25% / 25% | 0 / 0 |

No biological payload lots, filled chemical shell lots, filled air payload lots, chemical aircraft, projectors, or agent-specific cylinders are added by these historical country helpers.
Knowledge unlocks allow later construction, filling and production through the existing routes; they do not manufacture delivery equipment.
The agent lot definitions and their enums already exist, and every granted lot is unlocked by a granted technology before its stock call.
Germany's GA/GB knowledge has no matching free stock call.
The mask issue targets and separate 25% replacement reserves scale to each bookmark's own deployed force.
ENG alone additionally has the sourced 1939 civilian receipt and existing respirator production line; France's existing 1939 respirator line is retained.
MAN and RAJ have biological facilities but no completed biological payload project; that distinction is preserved.
Austria and Czechoslovakia have guarded grant definitions but no dated direct state owner in the 1939 state-source pass.

The direct state-history owner pass identified 90 tags in 1936 and 85 in 1939 before any DLC-dependent ownership effects.
This pass applies dated `owner` entries; it does not execute conditional history effects, country politics or game loading.
The registry check still covers every tag regardless of that ownership estimate, and native `exists = yes` guards decide whether individual grants apply.
Every remaining source-owner tag has no custom CBRN startup technology, payload lot, scientist, or mask-profile entitlement in this dispatcher.
They were inspected as the default group rather than receiving a copied or invented national programme:

- 1936.1.1.12: AFA, AFG, ALB, BHU, BOL, BRM, COL, COS, CUB, DOM, ECU, ELS, EST, ETH, GUA, HAI, HON, ICE, INS, IRE, IRQ, JOR, KUW, LAT, LEB, LIT, LUX, MAL, MEN, MON, NEP, NIC, OMA, PAL, PAN, PAR, PER, PHI, PRU, SAU, SIA, SWI, SYR, TAN, TIB, URG, VEN, YEM.
- 1939.8.14.12: AFG, BHU, BOL, BRM, COL, COS, CUB, DOM, ECU, ELS, EST, GUA, HAI, HON, ICE, INS, IRE, IRQ, JOR, KUW, LAT, LEB, LIT, LUX, MAL, MEN, MON, NEP, NIC, OMA, PAL, PAN, PAR, PER, PHI, PRU, SAU, SIA, SLO, SWI, SYR, TAN, TIB, URG, VEN, YEM.

The remaining registered tags are dormant/releasable or event-owned in this source-owner pass.
They have no entitlement from the ordinary historical startup dispatcher, except future event-owned packages and debug setup that are outside a historical bookmark.
`UWR` explicitly holds advanced chemical and biological compatibility knowledge in its own Event 005 country history; it owns no state at either historical start and receives no historical stockpile through this dispatcher.
`CXT` receives its debug packages only through the existing player-triggered setup, rather than historical startup equipment grants.
Neither is converted into a historical national programme by this audit.
The complete remaining tag set is:

AAX, ABK, ABX, ACX, ADU, ADX, AEX, AFX, AGX, AJX, AKX, ALG, ALT, ANG, ANU, ANX, AOI, AOX, ARD, ARM, ARX, ASX, ASY, ATJ, ATX, AXS, AXT, AXU, AXV, AXW, AXX, AXY, AXZ, AZR, BAH, BAN, BAR, BAS, BAX, BAY, BBH, BBX, BEG, BFX, BHR, BHX, BIA, BJX, BKX, BLC, BLI, BLR, BLZ, BOS, BOT, BOU, BRD, BRI, BRN, BSK, BUK, BWX, BYA, CAM, CAR, CAT, CAY, CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH, CBL, CBV, CFR, CHA, CHM, CHR, CHU, CIN, CIP, CIX, CJX, CKK, CKX, CLX, CMR, COG, COR, COX, CPS, CPX, CQX, CRC, CRI, CRO, CSA, CSH, CUX, CVX, CWX, CXT, CXX, CYP, CYX, D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50, D51, D52, D53, D54, D55, D56, D57, D58, D59, D60, D61, D62, D63, D64, D65, D66, D67, D68, D69, D70, D71, D72, D73, D74, D75, DAG, DAH, DAX, DBX, DDR, DFX, DHC, DHO, DHR, DHX, DIP, DJI, DJX, DKX, DLX, DMX, DNX, DNZ, DON, DOX, DPX, DSC, DSX, DTH, DUX, DVX, DYX, DZX, EBX, EEX, EGY, EHX, ELX, EMX, ENX, EQG, EQX, ERI, ERX, ESX, EUX, EVE, EWX, EXX, EYX, EZO, FAX, FBX, FDX, FER, FEV, FIJ, FLX, FNX, FOR, FOX, FPX, FSA, FSM, FSX, FTH, FUX, FVX, FXX, GAB, GAC, GAL, GAM, GAR, GBA, GBX, GCX, GDC, GDL, GDX, GEN, GEO, GGX, GHA, GHX, GIX, GLC, GLX, GMX, GNA, GNB, GOW, GRN, GRX, GSM, GTX, GUM, GYA, GYX, GZX, HAN, HAR, HAW, HAX, HBC, HBX, HCX, HDX, HES, HEX, HFX, HGX, HHX, HKX, HMX, HPX, HQX, HRZ, HSX, HTX, HUX, HWX, HXX, HYD, HYX, HZX, IAS, IAX, IBX, ICD, ICX, IJX, IKX, ILX, IMO, IMX, INC, INU, INX, ISR, ITZ, IUL, IVO, JAM, JAN, JHX, JIX, JKX, JLX, JMX, JNX, JOX, JPX, KAL, KAR, KAS, KAT, KAZ, KBK, KEN, KHA, KHC, KHI, KHL, KHM, KKP, KLT, KMB, KOL, KOM, KOR, KOS, KRG, KSH, KUB, KUM, KUR, KYR, LAO, LBA, LBV, MAC, MAD, MAY, MEK, MEL, MFR, MIS, MLD, MLI, MLT, MLW, MNT, MOL, MOR, MPU, MQA, MQC, MQE, MQJ, MQN, MQO, MQT, MRT, MYS, MZB, NAH, NAV, NEN, NGA, NGR, NIR, NLC, NMB, NOA, NRF, NWF, NXM, OCC, OKN, ORO, OVO, PAK, PAP, PLU, PNG, POK, PRA, PRE, PSH, PSR, PUE, QAT, QEM, QUE, RAA, RAN, RAP, RAR, RAS, RCG, RCO, REV, RGB, RHD, RHI, RIF, RIG, RJP, RKA, RKB, RKC, RKG, RKH, RKI, RKK, RKL, RKM, RKN, RKO, RKT, RKU, RKV, RNA, RNG, ROA, RTA, RTX, RUS, RUT, RWA, SAB, SAM, SAR, SAX, SCO, SDL, SDZ, SEN, SER, SHL, SIC, SID, SIE, SIL, SIN, SKK, SLV, SMI, SND, SNG, SOG, SOK, SOL, SOM, SPM, SRL, SSI, SUD, SUR, SZA, TAH, TAJ, TAT, TAY, THU, TIG, TML, TMS, TNC, TNE, TOG, TOS, TRA, TRI, TTS, TUN, TZN, UAE, UBD, UDC, UDM, UGA, UKR, USB, UWD, UWR, UZB, VAN, VGE, VIN, VLA, VOL, WES, WGR, WIS, WLA, WLS, WPG, WUR, XIC, YAK, YAM, YUC, ZAM, ZIM, ZIN, ZZZ.

The 67-person roster's names, ratings and traits are listed in the maintained [scientist roster](../systems/cbrn_warfare/cbrn_historical_scientists.md).
Both definition files and all 67 history recruits were checked against the A11 restoration parent for scientist-role bodies and home-country assignments; D2 changes no role rating or trait.
The relevant institutional biography sources are retained in the [Allied source review](chaos_warfare_system_plans/subagent_handoffs/2026-09-27_scientist_sources_ast_can_eng_fra.md), [German/Japanese/Polish review](chaos_warfare_system_plans/subagent_handoffs/2026-09-27_scientist_sources_ger_jap_pol.md), and [Soviet/American review](chaos_warfare_system_plans/subagent_handoffs/2026-09-27_scientist_sources_sov_usa.md).
Those older reviews' career/programme gates are superseded by A11 and are not requirements of this audit.
Country science totals before/after the death correction are AST 3/3, CAN 3/3, ENG 14/13, FRA 2/2, GER 15/15, JAP 4/4, POL 3/3, SOV 9/8 and USA 14/14.
The birth/death and later-service distinction is preserved; no additional missing identity is established by the reviewed record.

## Engine references and checks

The connected `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup` and `script_validate` schemas were verified.
Technology reference context included both required source kinds, without omitted required sources.
The relevant sections were actually read through the working reference routes:

- Installed `documentation/effects_documentation.md`, lines 807–814 (`add_breakthrough_progress`) and 7805–7819 (`set_technology`), revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, line 3180 (`add_breakthrough_progress`), revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- Offline `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md`, lines 61–80, revision `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee`.

The source-lookup call for `add_breakthrough_progress` timed out after 600 seconds.
The file-mode script-validation request for `common/scripted_effects/chaosx_startup_history_effects.txt` also timed out after 600 seconds.
The specialist's initial and narrower source-route requests had the same delivery failure; no further unchanged retry is justified.
Those results are unavailable checks, not passes.
Fresh service behavior or a corrected route addressing the timeout would justify a later attempt.
Local reference and source checks supplied the permitted alternative:

- Installed `history/countries/GER - Germany.txt`, lines 19–32, revision `5e903c2b485b48d8bba38adbe0b6fd5cadc868df4a575d526a1ef2dac4ab66d7`, demonstrates the native `value = 1.0` breakthrough grant.
- Installed effects documentation, lines 6436–6447, documents country-scoped `retire_character`; offline Effects line 2736 documents removal of all held roles.
- Installed effects documentation, lines 1252–1265, documents stockpile grants and optional producer; producer and imported-model behavior remain separate semantics from syntax validation.

The local D1/D3 checks evaluated both selected dates, confirmed all seven specialty amounts, compared the restored British/American grant bodies with the parent blob, traced Japan's setter and later initializer, and confirmed one-time dispatch.
The D2 checks compare starting technology grants against the actual equipment unlock definitions and verify the dated staff exclusions, without assuming discovery grants create finished stock.
No game was launched and no runtime behavior is claimed.


D4-specific engine reference evidence retained from the architect:

- `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, lines `[589, 630]`, revision `8ef3d5f9923026dd81f239944710b7331a8d06ad42e4345b32fce4e86dd95d98`; MCP search/read.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, lines `[216, 222]`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`; MCP search/read.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, lines `[1, 34]`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`; MCP search/read.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines `[[5012, 5018], [7820, 7827]]`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; MCP search/read.
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, lines `[911, 911]`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; MCP search/read.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines `[266, 267]`, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`; Direct local source; SHA-256 revision.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/unit_leader/00_traits.txt`, lines `[[1, 55], [2258, 2264]]`, revision `249ce6ee645cbd0270a8834ddc251c1f53ac981c979ac2a7c1852f929d850035`; Direct local source; SHA-256 revision.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_leader/00_traits.txt`, lines `[411, 425]`, revision `b629d44fde5fa93d176a1db04bdac83c53e51f55dd789359dca7a96ab4d25dc5`; Direct local source; SHA-256 revision.

The probability auditor read offline Effects lines 4516-4550 and installed effects documentation lines 5413-5430 for weighted `random_list` selection.
The D4 file-mode validation of `cbrn_hq_effects.txt` also timed out after one 600-second attempt, with no useful unchanged retry.

## Limits and unrequested changes

Exact historical quantities for every national stockpile are unavailable in the cited record, and the mod's abstract lots do not encode an archival mass conversion.
The 41 mask profiles use the owner's retained force-scaled military issue bands, not historically verified percentages for every army.
The British 1939 civilian receipt has its own [Hansard source](https://api.parliament.uk/historic-hansard/commons/1939/feb/02/air-raid-precautions); it is preserved with its existing crate abstraction.
The absence of a custom starting grant means no entitlement is demonstrated by this code, rather than proving a country had no chemical knowledge, public-health staff or protective equipment in real life.
The A11 research pool represents available alternate-history scientific potential, including people whose later wartime roles had not yet begun; it is not an assertion of a 1936 offensive appointment.
No art, audio, portrait, UI layout, report-event option count, unrelated event text, push or game launch is part of this change.
No restored wording was restyled.
The requested gameplay corrections are distinguished above from exact parent-content restoration.

No design fallback or reduced requested gameplay was introduced.
Historical inventory certainty, shipment provenance, the two retired readiness tooltip clauses, and unavailable engine observations remain explicitly limited as described above.
The parent reviewed D1–D4 integration; the country specialist reviewed D2 sources, the scripted-system architect implemented D4, and the independent probability auditor reviewed its changed spread surface.
Skills used: `chaos-redux-technology-doctrines`, `chaos-redux-characters-leaders`, `chaos-redux-equipment`, `chaos-redux-units-divisions`, `chaos-redux-ideas-modifiers`, `chaos-redux-events`, `chaos-redux-ai-strategies`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
No skills were created or updated.
