# Event 006 installed-tag and vanilla-identity audit handoff (superseded evidence)

Audit date: 2026-07-15
Mode: read-only audit; parent agent owns all implementation and migration work
Status: superseded by the parent reconciliation and generated 2026-07-15 tag audit

> The tables below preserve at-time `103/90` and `128/78` counts, replacement-
> pool hashes, and other first-pass evidence; do not reuse them as current
> ledgers. The accepted current result is **102 custom `X`-shell rows, 91
> registered vanilla-tag reuse rows (89 unique carriers), and 13 non-selectable
> overlays**. There are **191 unique nonblank carrier tags**, with only `CHU`
> and `BIA` intentionally shared. Current identity, binding, and safety
> evidence is
> `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`,
> `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`,
> and `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md`;
> the dated tag audits remain environment snapshots. `IW-153` reuses vanilla
> `POK`; it does not retain `FWX`. `IW-162` Kachin State uses `IBX` because
> `GFX` is HOI4's engine-reserved graphics namespace.

## Historical binding result (superseded first-pass table)

The 206 Event 006 package rows should resolve as follows:

| Representation | Count | Binding meaning |
| --- | ---: | --- |
| Custom Event 006 country whose tag ends in X | 103 | The identity is demonstrably distinct from vanilla and may retain or receive a collision-free X tag. |
| Registered vanilla-tag reuse | 90 | The country already exists as a stable vanilla tag. Event 006 may instantiate that tag only when it is not living and must origin-gate all Event 006 content. |
| Non-selectable vanilla route/formable overlay | 13 | The identity already exists as a vanilla cosmetic, dynamic-country route, ideology route, autonomy identity, or formable. Event 006 adds a package after the vanilla route exists; it does not register or create another country. |
| Total | 206 | All package rows have one representation. |

This changes 12 of the 128 proposed custom-X rows into registered vanilla-tag reuses and 13 into overlays. The remaining 103 custom-X rows include the genuinely distinct identities and the three installed-mod collision replacements listed below.

The vanilla-tree safety review correctly classified several exact tags as high-collision. The user’s binding identity rule means that those rows cannot evade the collision by retaining a duplicate X country. Their high-collision findings are therefore mandatory compatibility-patch and origin-gating obligations, detailed in the reuse table below. A reuse is not complete merely because the Event 006 tree is gated.

## Source universe and method

The audit compared the Event 006 candidate matrix and current registry against:

- vanilla at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV;
- all 122 direct mod directories under C:/Program Files (x86)/Steam/steamapps/workshop/content/394360;
- the sibling mods agentic_hoi4_modding, chaos_redux_music, and slop_redux;
- Chaos Redux itself, so the replacement pool cannot consume another project reservation.

Required offline references were consulted before repository inspection: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Country creation. Relevant vanilla documentation in the documentation directory was consulted in parallel, including script concepts, effects, and triggers.

The exact scan produced:

- 7,981 literal external/vanilla country-tag registration records, representing 2,262 unique literal tags;
- 986 top-level country-tag alias records, representing 840 unique alias identifiers;
- direct literal set_cosmetic_tag calls for every one of the 128 then-resolved Event 006 custom tags;
- exact three-character base localisation keys, flag filenames, and country-history filenames;
- 676 possible [A-Z][A-Z]X candidate tags;
- 206 unique provisional_new_tag reservations in the Event 006 candidate matrix, of which 128 then resolved as new tags and 78 as registered reuse;
- 457 conservative replacement candidates after external surfaces, Chaos Redux use, and all 206 matrix reservations were excluded.

The 457-tag safe pool has canonical comma-separated UTF-8/no-BOM/no-trailing-newline SHA-256:

0da72ee363870ba939534ca7d57f908af9bd967e167a6746e2a83eb832464655

The candidate matrix SHA-256 was:

b860c7dd9546b64bfa6a6d1e2575f8eb7bc728103be0df1ecf8d344606ade8dc

## Installed-mod collision dispositions

| Event 006 row | Current tag and external surface | Decisive action |
| --- | --- | --- |
| IW-087 Fezzan | DIX is registered by Red Flood, Workshop 2815832636, at common/country_tags/00_countries.txt:106 as its United States Emergency Committee. Its history, localisation, and flags are also live. | Fezzan has no exact vanilla identity in the installed vanilla snapshot. Keep a distinct custom country and migrate DIX to HYX repository-wide. |
| IW-124 Basotho | ETX is a KaiserreduX Empire of Texas cosmetic at Workshop 2076426030/events/Texas.txt:7091 with localisation at localisation/KR_Texas_l_english.yml:209. The same base localisation is copied in Workshop 3325164444:209 and 3473395369:86. | Basotho has no exact vanilla identity in the installed vanilla snapshot. Keep a distinct custom country and migrate ETX to HZX repository-wide. |
| IW-157 West Papua | GAX is registered by TNO, Workshop 2438003901, at common/country_tags/00_countries.txt:582 for Galápagos, with base localisation at localisation/english/TNO_Ecuador_l_english.yml:32 and history/flags. | The current generic West Papua row must reuse WPG, so GAX is retired without a replacement. If later research creates a demonstrably distinct named people-and-district polity, assign a then-rechecked safe X tag, never GAX. |
| IW-161 Mon State | GEX is a dynamic alias in Kaiserreich, Workshop 1521695605/common/country_tag_aliases/tag_aliases.txt:124-126, targeting MAF_free_germany. It is also an alias in KaiserreduX, Workshop 2076426030, at lines 137-139, targeting current_german_exile_government. | Mon has no exact vanilla identity in the installed vanilla snapshot. Keep a distinct custom country and migrate GEX to IAX repository-wide. |
| IW-059 Mesopotamian Federation | CGX has vanilla flag assets at gfx/flags/CGX.tga and the medium/small variants. The same surface is copied by Workshop 1458561226, 1532883122, 1827273767, 2438003901, and 2931916970. No external runtime country registration was proven. | Treat the flag-only surface as a conservative collision. The row becomes the vanilla neo_mesopotamia overlay, so CGX is retired without a replacement. |

HYX, HZX, and IAX are the first three deterministic entries in the matrix-aware safe pool. Retired tags from rows converted to reuse or overlays remain reserved during this migration and are not recycled.

## Exact stable-tag reuses and mandatory compatibility work

No tag in this table has its own standalone tag-selected vanilla focus tree. That does not make reuse low-risk: vanilla events, decisions, AI, formables, and foreign focus trees directly address many of them. Every reuse must preserve vanilla country registration, common/countries data, history, characters, flags, and base localisation.

Common implementation requirements for all 12 rows:

1. Do not add another common/country_tags registration and do not replace a vanilla history/countries file.
2. The Event 006 package can instantiate the tag only when that tag has exists = no.
3. Set a package-specific Event 006 origin flag during the Event 006 creation chain.
4. Gate the Event 006 focus tree, decisions, events, AI, scripted effects, and route localisation with that package flag, never only tag = TAG or original_tag = TAG.
5. If a vanilla system may create, puppet, release, transfer to, or reconfigure the tag, add a branch for the Event 006-origin country. Preserve the unmodified vanilla branch for a normal vanilla-origin country.
6. A living vanilla country is never transformed, reloaded, re-coloured, re-localised, or assigned the Event 006 tree.

| Event 006 row | Vanilla identity and exact evidence | Required compatibility and gating |
| --- | --- | --- |
| IW-038 Ruthenia, BLX | Reuse RUT. Registry common/country_tags/00_countries.txt:370. | The CZE release/player-switch chain at events/MUN_Czechoslovakia.txt:5712-5757 and 5801-5877 must not release, reload an OOB into, or switch the player to an already-living Event 006 RUT. Branch on the Event 006 package flag while leaving the normal CZE route intact. Review common/ai_strategy/RUT.txt:1-58: its CZE-origin assumptions must be gated away from Event 006 RUT unless they are explicitly adopted. |
| IW-042 Galicia-Lodomeria, BPX | Reuse GAL. Registry :371; vanilla identity is Galicia and Lodomeria. | The CZE core grant at common/national_focus/czechoslovakia_mu.txt:1650 is same-identity and idempotent, so it may remain. Origin-gate Event 006 content and do not replace GAL history. No direct vanilla creation chain was found. |
| IW-043 Volga Bulgaria, BQX | Reuse CHU as its Neo Volga-Bulgaria route. Registry :240; exact ideology localisation is in countries_l_english.yml:3905-3916. | IW-043 and IW-046 Chuvashia share CHU and the RG-MIDDLE-VOLGA-KAZAN reservation group; package-specific flags, not the tag alone, must select identity, content, and localisation. Preserve or deliberately accept CHU eligibility for Idel-Ural at common/decisions/formable_nation_decisions.txt:13939-13976. If that formable is not intended for Event 006 Volga Bulgaria, exclude only the IW-043 package flag without altering normal CHU. |
| IW-096 Edo Kingdom of Benin, DRX | Reuse BIA, not DAH. Registry :265; BIA neutrality is Edo Kingdom of Benin at localisation/english/countries_l_english.yml:4538-4540. | IW-096 and IW-107 Biafra share BIA and RG-NIGERIA-COARSE, so they must be mutually exclusive and use separate package flags for tree, identity, and follow-up content. Do not overwrite the BIA history file. DAH remains modern Benin/Dahomey and retains its French and South African systems. |
| IW-133 Bengal, FCX | Reuse BAN. Registry :115; State of Bengal/Bengal People's Republic localisation is at countries_l_english.yml:1929-1943. | Patch the GOE/RAJ/UK paths at common/national_focus/india_goe.txt:15353-15377 and 15695-15706, common/decisions/RAJ_GOE.txt:2098-2113, and common/national_focus/uk.txt:3402-3428 so an existing Event 006 BAN is treated as a sovereign counterpart, not recreated, silently puppeted, or used as proof that a vanilla route already completed. Preserve the normal vanilla release path when the Event 006 flag is absent. |
| IW-150 Aceh, FTX | Reuse ATJ. Registry :377. | The INS release route at common/national_focus/indonesia.txt:2588-2621 must branch around an already-living Event 006 Aceh rather than release or reconfigure it. Indonesian Union eligibility may remain when ATJ actually has the relevant subject relationship; it must not itself claim an independent Event 006 ATJ. |
| IW-155 Bali, FYX | Reuse BLI. Registry :376. | Guard the BLI-directed character-transfer logic at common/scripted_effects/INS_scripted_effects.txt:169-180 so it does not strip or overwrite Event 006 package characters. Preserve its normal behavior for vanilla-origin BLI. Indonesian Union eligibility remains relationship-dependent. |
| IW-157 generic West Papua, GAX | Reuse WPG. Registry :355. | Review Japan's WPG targeting at common/national_focus/japan.txt:14137-14214 and 14418-14432 and INS decisions at common/decisions/INS.txt:4664-4685. Direct war targeting may remain if deliberately intended for the same identity; any release, annexation, or internal-state assumptions must branch for a sovereign Event 006-origin WPG. The generic row cannot retain an X tag. |
| IW-167 Champa Restoration, GKX | Reuse CHM. Registry :350. | Review Japan's Indochina targeting at common/national_focus/japan.txt:13622-13847 and INS decisions at common/decisions/INS.txt:4664-4685. Preserve ordinary vanilla behavior, but branch any effect that assumes CHM is an uncreated regional release rather than a living Event 006 country. |
| IW-171 Ryukyu, GOX | Reuse OKN. Registry :345. | No direct vanilla decision/event creation chain was found. Preserve the East Asian faction behavior at common/factions/rules/joining_rules.txt:906-943 and gate the Event 006 tree/AI with the package flag. |
| IW-172 generic Ainu state, GPX | Reuse ANU. Registry :346. | Japan's Ainu route at common/national_focus/japan.txt:18796-18840 and events/SEA_Japan.txt:11727-11753 can transfer all ANU cores and puppet ANU. It must branch when ANU already exists with the Event 006 package flag; it may negotiate, target, or interact as designed, but may not silently recreate, puppet, or overwrite it. Preserve the vanilla branch for normal ANU. |
| IW-178 generic Papua federation, GVX | Reuse PNG. Registry :126. | The USA decolonisation decision at common/decisions/USA.txt:3007-3027 must not create or reconfigure an existing Event 006 PNG. Review Japan's targeting at common/national_focus/japan.txt:13172-13202 and the INS regional decisions for living-country assumptions. Preserve normal vanilla paths when the Event 006 flag is absent. |

The high-collision findings for RUT, CHU, BAN, ATJ, ANU, and PNG are therefore not rejected; they are converted into explicit compatibility work. If those branches are not implemented, the corresponding reuse is incomplete.

## Thirteen exact vanilla overlays

These rows are not countries in the Event 006 selectable-country registry. They receive no X registration, country-history file, standalone common/countries file, independent flag package, or Event 006 tag-selected focus tree. Event 006 observes the vanilla carrier after the vanilla route succeeds, sets a one-time Event 006 overlay/package flag, and adds only additive mechanics. It does not bypass the vanilla route's core grants, global flags, state transfers, autonomy, or dynamic-country creation.

| Event 006 row | Vanilla representation | Exact overlay trigger/representation and preserved system |
| --- | --- | --- |
| IW-005 Flanders, AEX | BEL_flanders cosmetic | Observe BEL with has_cosmetic_tag = BEL_flanders after the GER decision at common/decisions/GER.txt:20116-20120. Localisation is countries_cosmetic_l_english.yml:2353-2364. Preserve the BEL tree at common/national_focus/belgium.txt:1-14; never convert a living BEL into a new Event 006 country. |
| IW-022 Dalmatia, ZZZ | Vanilla dynamic country | Observe the dynamic country with original_tag = CRO and has_cosmetic_tag = dalmatia created at common/national_focus/yugoslavia.txt:817-825. Localisation is countries_l_english.yml:3373-3389. Preserve the YUG creation path and tree at yugoslavia.txt:1-14. |
| IW-025 Vojvodina, AYX | Vanilla dynamic country | Observe the dynamic country with original_tag = HUN and has_cosmetic_tag = vojvodina created at yugoslavia.txt:1554-1575. Localisation is countries_l_english.yml:3403-3414. Preserve the YUG creation path and tree. |
| IW-035 Livonia, BIX | LIVONIA cosmetic on Lithuania | Observe LIT with has_cosmetic_tag = LIVONIA after common/national_focus/lithuania.txt:4633-4677 grants the relevant Estonia/Latvia cores. Localisation is countries_cosmetic_l_english.yml:1294-1304. Preserve the LIT tree at lithuania.txt:9-22. Do not map Livonia to UBD: UBD is the distinct Baltic-German state consumed by the GER decision at common/decisions/GER.txt:19233-19251 and 19321-19370. |
| IW-059 Mesopotamian Federation, CGX | neo_mesopotamia formable | Observe an allowed carrier with has_cosmetic_tag = neo_mesopotamia and the vanilla formed state after common/decisions/formable_nation_decisions.txt:17655-17838 completes. Localisation is countries_cosmetic_l_english.yml:3059-3073. Do not set only the cosmetic: that would bypass vanilla cores and neo_mesopotamia_formed_flag. |
| IW-085 Cyrenaica, DGX | LBA's Italian autonomy localisation identity | This is not a literal cosmetic tag. Observe original_tag = LBA with the applicable Italian overlord/autonomy relationship represented by countries_cosmetic_l_english.yml:204, 210, 330, and 338. Preserve LBA history, cores, and Italian coupling. Under the binding rule, an independent selectable Cyrenaica is suppressed; because LBA carries all Libya cores, a separate independent design requires explicit user approval as a design exception. |
| IW-101 Kongo, DWX | COG_kingdom_of_kongo cosmetic | Observe COG with the cosmetic set at common/national_focus/congo.txt:6195-6196. Localisation is countries_cosmetic_l_english.yml:2313-2315. Preserve the COG tree at congo.txt:9-22. |
| IW-102 Kuba, DXX | COG_kingdom_of_kuba cosmetic | Observe COG with the cosmetic set at congo.txt:6246-6247. Localisation is countries_cosmetic_l_english.yml:2317-2319. Preserve the COG tree. |
| IW-105 Loango, EAX | COG_kingdom_of_loango cosmetic | Observe COG with the cosmetic set at congo.txt:6303-6304. Localisation is countries_cosmetic_l_english.yml:2321-2323. Preserve the COG tree. |
| IW-156 Moluccan Federation, FZX | TNE democratic ideology route | Observe original_tag = TNE with democratic government, whose vanilla identity is United States of Maluku at countries_l_english.yml:5892-5893. Add the Event 006 package to that route without registering FZX or replacing TNE history and Indonesian regional coupling. |
| IW-196 Caribbean Federation, HNX | antilles formable | Observe an allowed carrier with has_cosmetic_tag = antilles and the vanilla formed state after formable_nation_decisions.txt:15536-15713 completes. The cosmetic is set at :15588 and localisation is countries_cosmetic_l_english.yml:2266-2277. Do not set only the cosmetic and bypass the member, core, and global-flag effects. RCO is rejected: it is Reichskommissariat Kolumbus at common/country_tags/00_countries.txt:300 and countries_l_english.yml:5176-5189. |
| IW-197 Mapuche Federation, HOX | CHL_mapuche_state cosmetic | Observe CHL with has_cosmetic_tag = CHL_mapuche_state, set at common/national_focus/chile.txt:3539 and common/on_actions/04_mtg_on_actions.txt:1157. Localisation is countries_cosmetic_l_english.yml:1769-1780. Preserve the CHL tree at chile.txt:12-25. |
| IW-204 Araucania and Patagonia Restoration, HVX | kingdom_of_araucania_and_patagonia cosmetic | Observe CHL with the cosmetic set at events/TOA_Chile.txt:3984. Localisation is countries_cosmetic_l_english.yml:1966-1971. Preserve the CHL tree and vanilla event chain. |

Overlay activation must use a one-time per-carrier flag or equivalent narrow hook. A global daily/weekly/monthly country iteration is neither needed nor authorised.

## Vanilla resemblance reviewed and kept distinct

These are not duplicate vanilla identities and remain among the 103 custom-X countries:

| Event 006 row | Vanilla resemblance | Why the Event 006 identity remains distinct |
| --- | --- | --- |
| IW-018 Sardinia, ARX | SPM, Sardinia-Piedmont, registry :256 | Event 006 is the island polity; SPM includes Piedmont, has both Sardinian and mainland cores, and participates in wider Italian/Hungarian content. |
| IW-019 Sicily, ASX | TTS, Two Sicilies, registry :257 | Event 006 is the island polity; TTS includes the mainland south and its wider core/content package. |
| IW-064 Circassia, CLX | KBK fascist localisation Circassian Realm at countries_l_english.yml:3812-3813 | KBK is Kabardino-Balkaria with a different eastern/core geography; Event 006 requires the researched northwest-Caucasus/Krasnodar split. |
| IW-100 Hausa Federation, DVX | SOK democratic Hausa-Fulani Republic of Sokoto at countries_l_english.yml:4599-4600 | The accepted Event 006 design is a broader, negotiated Hausa federal formable, not the Hausa-Fulani Sokoto state. If the design is narrowed to Sokoto, it must instead become a SOK route. |
| IW-153 Dayak Federation, FWX | POK's Dayak Republic of West Borneo route | POK is Pontianak with Pontianak history, leader, cores, and Indonesian transfer logic. The Event 006 row is retained only for a separately researched named Dayak polity or river-region federation. |
| IW-174 Iwi-led Māori Federation, GRX | NZL communist People's Republic of Aotearoa at countries_l_english.yml:1145-1146 | The accepted package is an iwi-led congress/federal institution with community-specific governance, not merely communist New Zealand or a route-name substitution. Preserve the NZL tree. |
| IW-203 Patagonian State, HUX | WLA ideology names containing Patagonia at countries_l_english.yml:4500-4510 | WLA is Welsh Argentina/Y Wladfa; the Event 006 package is a civic Patagonian regional state, not a Welsh-colonial identity. |

Fezzan, Basotho, and Mon State were also searched directly across vanilla country tags, history, events, common script, and English localisation. No exact stable tag, cosmetic, dynamic route, formable, or ideology/autonomy identity was found for them.

## Safe replacement pool

This pool is intentionally conservative: it continues to reserve all 206 candidate-matrix provisional slots, including retired X values from rows converted to vanilla reuse or overlays. Exact localisation keys are case-sensitive; lowercase generic keys such as six and tfx do not occupy uppercase SIX and TFX.

HYX HZX IAX IBX ICX IDX IEX IFX IGX IHX IIX IJX IKX ILX IMX INX IOX IPX IQX IRX ISX ITX IUX IVX IWX IXX IYX IZX JAX JBX JCX JDX JEX JFX JHX JIX JJX JKX JLX JMX JNX JOX JPX JQX JRX JSX JTX JUX JVX JWX JXX JYX JZX KAX KBX KCX KDX KEX KFX KGX KHX KIX KJX KKX KLX KMX KNX KOX KPX KQX KRX KSX KUX KVX KWX KXX KYX KZX LAX LBX LCX LDX LEX LFX LGX LHX LIX LJX LKX LLX LMX LNX LOX LPX LQX LRX LSX LTX LVX LWX LXX LYX LZX MBX MCX MDX MFX MGX MHX MIX MJX MKX MLX MMX MNX MOX MPX MQX MRX MSX MTX MUX MVX MWX MXX MYX MZX NBX NCX NDX NEX NFX NGX NHX NIX NJX NKX NLX NMX NNX NOX NPX NQX NRX NSX NTX NUX NVX NWX NXX NYX NZX OAX OBX OCX ODX OEX OFX OGX OHX OIX OJX OKX OLX OMX ONX OOX OPX OQX ORX OSX OTX OUX OVX OWX OXX OYX OZX PAX PBX PCX PDX PEX PFX PGX PIX PJX PKX PLX PMX PNX POX PPX PQX PRX PSX PTX PUX PVX PWX PXX PYX PZX QAX QBX QCX QDX QEX QFX QGX QHX QIX QJX QKX QLX QMX QNX QOX QPX QQX QRX QSX QTX QUX QVX QWX QXX QYX QZX RAX RBX RCX RDX REX RFX RGX RHX RIX RJX RKX RLX RMX RNX ROX RPX RQX RRX RSX RTX RUX RVX RWX RXX RYX RZX SBX SCX SDX SFX SGX SIX SJX SKX SLX SMX SNX SOX SPX SQX SRX SSX STX SUX SVX SWX SXX SYX SZX TAX TBX TCX TDX TFX TGX THX TIX TJX TKX TLX TNX TOX TPX TQX TRX TSX TTX TUX TVX TWX TXX TYX TZX UAX UBX UCX UDX UEX UFX UGX UHX UIX UJX UKX ULX UMX UNX UOX UPX UQX URX USX UTX UUX UVX UWX UXX UYX UZX VAX VBX VCX VDX VEX VFX VGX VHX VJX VKX VLX VMX VNX VOX VPX VQX VRX VSX VTX VUX VVX VWX VXX VYX VZX WAX WBX WCX WDX WEX WFX WGX WHX WIX WJX WKX WLX WMX WNX WOX WPX WQX WRX WSX WTX WUX WVX WWX WXX WYX WZX XAX XBX XCX XDX XEX XFX XGX XHX XIX XJX XKX XLX XMX XNX XOX XPX XQX XRX XSX XTX XUX XVX XWX XXX XYX XZX YAX YBX YCX YDX YEX YFX YGX YHX YIX YJX YKX YLX YMX YNX YOX YPX YQX YRX YSX YTX YUX YVX YWX YXX YYX YZX ZAX ZBX ZCX ZDX ZEX ZFX ZGX ZHX ZIX ZJX ZKX ZLX ZMX ZNX ZOX ZPX ZQX ZRX ZSX ZTX ZUX ZVX ZWX ZXX ZYX ZZX

## Representative inspection commands

The audit used native recursive enumeration plus ripgrep rather than relying on mod descriptors or an enabled playset. Representative checks were:

~~~powershell
rg -n --no-heading "^[A-Z]{3}\s*=" common/country_tags
rg -n --no-heading "^[A-Z]{3}\s*=\s*\{" common/country_tag_aliases
rg -n --no-heading "set_cosmetic_tag\s*=\s*[A-Z]{3}" common events
rg -n --no-heading "^(DIX|GAX|GEX|ETX|CGX)(:|_)" localisation
Get-ChildItem -Recurse -File -Filter "CGX.tga"
~~~

Brace-depth-aware parsing stripped comments and strings before accepting top-level assignments. Direct cosmetic-call parsing accepted literal scalar tags only. Vanilla identity review additionally searched country-definition basenames, English country and cosmetic localisation, formable decisions, focus-tree completion effects, events, on-actions, history/core geography, and direct/original-tag consumers.

## Limitations and implementation gate

- Cosmetic and route identities do not have one complete engine registry. The audit combined literal set_cosmetic_tag calls, ideology/autonomy localisation, focus/event effects, formable decisions, flags, and manual source review.
- Dynamically constructed identifiers inside meta effects, scripted localisation, packed archives, or nonstandard binary assets cannot be proven absent by literal parsing.
- No archives were decompressed and no symlinks were followed.
- The scan covers every installed Workshop directory, not merely the current playset. A later install can consume a currently safe tag, so the three chosen replacements should be rechecked immediately before their migration commit.
- The overlay architecture needs narrow event-chain hooks, decision completion hooks, or package-specific on-action calls. It must not introduce an unauthorised global daily, weekly, or monthly iteration.
- IW-085 independent Cyrenaica remains a design exception/blocker: the binding duplicate rule selects the LBA autonomy overlay, while a truly independent Cyrenaica cannot safely inherit LBA's full Libya identity and cores. Do not implement a separate country without explicit approval.

No gameplay, specification, tag-registry, localisation, asset, skill, or spreadsheet file was edited by this audit. This handoff is the only file created. No commit was made; the parent agent owns implementation, final audit, and the required plan commit.

## Skills used

- chaos-redux-subagents for bounded ownership, evidence, and handoff rules;
- chaos-redux-events for Event 006 integration context;
- chaos-redux-focus-trees in the vanilla tree-safety subaudit.
