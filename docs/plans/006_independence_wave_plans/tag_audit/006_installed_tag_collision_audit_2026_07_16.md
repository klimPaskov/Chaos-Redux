# Event 006 installed country-tag and vanilla-reuse audit

Audit date: 2026-07-16

## Binding result

- Candidate registry rows: **206**.
- Reserved Event 006 country tags scanned: **102**.
- Event 006 formable/cosmetic identity tags scanned: **4**.
- Unique Event 006-owned identifiers checked together: **106**.
- Registered vanilla-tag reuse rows: **91**, using **89** unique vanilla tags.
- Non-selectable vanilla route-overlay rows: **13**.
- Engine-, offline-wiki-, or OS-reserved three-character namespaces excluded: **AND, AUX, CON, GFX, LOG, NOT, NUL, NUM, OOB, PRN, RED, TAG**.
- Installed Workshop directories scanned: **122**.
- Workshop directories containing country-tag definitions: **37**.
- Embedded ZIP archives scanned without extraction: **8**.
- Embedded ZIP archives containing tag-bearing surfaces: **1**.
- Country-tag definitions parsed from embedded ZIP archives: **0**.
- Alias/cosmetic/history/localisation/flag surfaces parsed from embedded ZIP archives: **10**.
- Sibling local mod directories scanned: **3** (agentic_hoi4_modding, chaos_redux_music, slop_redux).
- Sibling local mods containing country-tag or extended tag surfaces: **0**.
- Literal country-tag definitions parsed from sibling local mods: **0**.
- Alias/cosmetic/history/localisation/flag surfaces parsed from sibling local mods: **0**.
- External and vanilla country-tag definitions parsed: **7981**.
- External and vanilla alias/cosmetic/history/localisation/flag tag uses parsed: **69484**.
- Other Chaos Redux country-tag definitions parsed: **49**.
- Other Chaos Redux alias/cosmetic/history/localisation/flag tag uses parsed: **963**.
- Reserved-tag collisions: **0**.
- Packages with exact or state-word-normalized vanilla identity matches requiring reuse review: **0**.
- Packages with fuzzy identity matches requiring manual review: **16**.
- Recorded manual identity dispositions: **18**.
- Collision-free unused `??X` replacement candidates: **448**.

## Reserved-tag collisions

No Event 006-owned country, formable, or cosmetic identifier collides with the scanned installed registries.

## Event 006 formable and cosmetic identities

| Family | Identity | Tag |
| --- | --- | --- |
| FORM-01 | Celtic Congress | `KCX` |
| FORM-02 | North Atlantic Union | `NUX` |
| FORM-03 | Confederation of the Low Countries | `LCX` |
| FORM-04 | Rhenish League | `RLX` |

All four tags are X-ending, unique against the 102 country reservations, present in the reviewed cosmetic registry, and used by an exact Event 006 `set_cosmetic_tag` adapter.

## Vanilla identity comparison

| Event 006 package | Proposed identity/tag | Vanilla candidate | Confidence |
| --- | --- | --- | --- |
| IW-018 | Sardinia / `ARX` | United States of Savoy and Sardinia / country_tag `SPM` | manual_review (1.0) |
| IW-018 | Sardinia / `ARX` | Sardinia-Piedmont / country_tag `SPM` | manual_review (1.0) |
| IW-018 | Sardinia / `ARX` | Sardinia Piedmont / country_tag `SPM` | manual_review (1.0) |
| IW-037 | Polesia / `BKX` | the United Kingdom of Polynesia / cosmetic_tag `united_polynesia` | manual_review (0.875) |
| IW-037 | Polesia / `BKX` | United Kingdom of Polynesia / cosmetic_tag `united_polynesia` | manual_review (0.875) |
| IW-037 | Polesia / `BKX` | Polynesia / cosmetic_tag `united_polynesia` | manual_review (0.875) |
| IW-037 | Polesia / `BKX` | the Polynesian Empire / cosmetic_tag `united_polynesia` | manual_review (0.8235) |
| IW-037 | Polesia / `BKX` | Polynesian Empire / cosmetic_tag `united_polynesia` | manual_review (0.8235) |
| IW-037 | Polesia / `BKX` | Polynesian / cosmetic_tag `united_polynesia` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Socialist Republic of Kurdistan / country_tag `KUR` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Kurdistan / country_tag `KUR` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Kingdom of Kurdistan / country_tag `KUR` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | the Socialist Republic of Kurdistan / cosmetic_tag `IRQ_kurdistan_tag` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | the Kingdom of Kurdistan / cosmetic_tag `IRQ_kurdistan_tag` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Socialist Republic of Kurdistan / cosmetic_tag `IRQ_kurdistan_tag` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Kurdistan / cosmetic_tag `IRQ_kurdistan_tag` | manual_review (0.8235) |
| IW-061 | Luristan / `CIX` | Kingdom of Kurdistan / cosmetic_tag `IRQ_kurdistan_tag` | manual_review (0.8235) |
| IW-064 | Circassia / `CLX` | Circassian Realm / country_tag `KBK` | manual_review (0.9474) |
| IW-100 | Hausa Federation / `DVX` | Russian Federation / country_tag `SOV` | manual_review (0.8235) |
| IW-117 | Kilwa restoration / `EMX` | Showa Restoration / cosmetic_tag `JAP_showa_restoration` | manual_review (0.8235) |
| IW-144 | Dravidian federation / `FNX` | Arabian Federation / cosmetic_tag `ARA_UNIFIED` | manual_review (0.8421) |
| IW-159 | Shan federation / `GCX` | Russian Federation / country_tag `SOV` | manual_review (0.8485) |
| IW-163 | Chin state / `GGX` | China / country_tag `RNG` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | China / country_tag `PRC` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | China / country_tag `MAN` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | Republic of China / country_tag `CHI` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | China / country_tag `CHI` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | the Empire of China / cosmetic_tag `TSR_empire_of_china` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | Empire of China / cosmetic_tag `TSR_empire_of_china` | manual_review (0.8889) |
| IW-163 | Chin state / `GGX` | the People's Republic of China / cosmetic_tag `PRC_proclaimed` | manual_review (0.8889) |
| IW-169 | East Turkestan / `GMX` | Turkestan Autonomous Soviet Socialist Republic / country_tag `TMS` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | the Reichskommissariat Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Volkskommissariat Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Reichskommissariat Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Reichskommisariat Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Grand Duchy of Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Bundesstaat Turkestan / country_tag `RKT` | manual_review (1.0) |
| IW-169 | East Turkestan / `GMX` | Turkestan / cosmetic_tag `turkestan_united` | manual_review (1.0) |
| IW-174 | Aotearoa Maori state / `GRX` | People's Republic of Aotearoa / country_tag `NZL` | manual_review (1.0) |
| IW-190 | Pueblo federation / `HHX` | Costa del Pueblo / country_tag `COS` | manual_review (1.0) |
| IW-193 | Zapotec-Mixtec Oaxaca federation / `HKX` | the Huastec-Mixtec-Aztec-Mexican United People's Republic / cosmetic_tag `indigenous_mexico` | manual_review (1.0) |
| IW-193 | Zapotec-Mixtec Oaxaca federation / `HKX` | Huastec-Mixtec-Aztec-Mexican United People's Republic / cosmetic_tag `indigenous_mexico` | manual_review (1.0) |
| IW-203 | Patagonian state / `HUX` | Ymerodraeth Patagonia / country_tag `WLA` | manual_review (0.9474) |
| IW-203 | Patagonian state / `HUX` | Cymun Patagonia / country_tag `WLA` | manual_review (0.9474) |
| IW-203 | Patagonian state / `HUX` | the Kingdom of Araucanía and Patagonia / cosmetic_tag `kingdom_of_araucania_and_patagonia` | manual_review (0.9474) |
| IW-203 | Patagonian state / `HUX` | Kingdom of Araucanía and Patagonia / cosmetic_tag `kingdom_of_araucania_and_patagonia` | manual_review (0.9474) |
| IW-205 | Amazonian confederation / `HWX` | Danubian Confederation / cosmetic_tag `HUN_EMPIRE` | manual_review (0.8444) |
| IW-205 | Amazonian confederation / `HWX` | Antillean Confederation / cosmetic_tag `antilles` | manual_review (0.8261) |
| IW-206 | Maroon republic / `HXX` | Roman Republic / country_tag `PAP` | manual_review (0.8276) |
| IW-206 | Maroon republic / `HXX` | Oromo Republic / country_tag `ORO` | manual_review (0.8276) |

Exact and `exact_after_state_words` matches are binding blockers until the identity is either switched to the vanilla tag or documented as a distinct polity. `manual_review` matches are discovery leads, not automatic remaps.

## Manual vanilla-identity dispositions

- **IW-011 Faroe Islands / `AKX`** against unrelated vanilla country names containing Islands: `false_generic_token_match` / `scenario_variant_only`. The generated lead shares only the generic geographic word islands; no vanilla Faroe country or cosmetic identity is registered. Required action: Retain AKX only for its accepted scenario variant after full package readiness; never treat the state name alone as country-content proof.
- **IW-018 Sardinia / `ARX`** against SPM / Sardinia-Piedmont: `distinct_polity_reviewed` / `no_identity_block`. ARX is the compact island polity; SPM includes Piedmont and participates in wider mainland content. Required action: Keep the final ARX package and territory limited to the researched Sardinian island identity.
- **IW-019 Sicily / `ASX`** against TTS / Two Sicilies: `distinct_polity_reviewed` / `no_identity_block`. ASX is the compact island polity; TTS includes the mainland south and its wider core and content package. Required action: Keep the final ASX package and territory limited to the researched Sicilian island identity.
- **IW-037 Polesia / `BKX`** against united_polynesia / Polynesia: `false_fuzzy_match` / `no_identity_block`. Polesia is the eastern European marsh region; Polynesia is an unrelated Pacific identity. Required action: Retain BKX only after its ordinary package readiness and installed-state proofs pass.
- **IW-061 Luristan / `CIX`** against KUR / Kurdistan: `false_fuzzy_match` / `disabled_by_map_binding`. Luristan is a distinct western Iranian region; the string resemblance to Kurdistan does not establish identity equivalence. Required action: Keep CIX disabled until the installed map supplies a unique researched Luristan state.
- **IW-064 Circassia / `CLX`** against KBK / Circassian Realm: `distinct_polity_reviewed` / `no_identity_block`. CLX is the researched northwest-Caucasus and Krasnodar split; KBK is Kabardino-Balkaria with different geography and content. Required action: Keep the final CLX territory and institutions distinct from the registered KBK package.
- **IW-100 Hausa Federation / `DVX`** against SOK / Hausa-Fulani Republic of Sokoto: `distinct_formable_reviewed` / `route_or_formable_only`. DVX is a broader negotiated Hausa federal route rather than the Sokoto state; the generated Russian Federation lead is only a string false positive. Required action: If the design narrows to Sokoto use a guarded additive SOK route and retire DVX.
- **IW-117 Kilwa restoration / `EMX`** against Showa Restoration: `false_fuzzy_match` / `disabled_by_map_binding`. Kilwa and Showa are unrelated identities whose route labels share only restoration. Required action: Keep EMX disabled until a unique researched Kilwa coastal state exists.
- **IW-144 Dravidian federation / `FNX`** against Arabian Federation: `false_fuzzy_match` / `route_or_formable_only`. Dravidian and Arabian are unrelated identities whose proposed names share only federation. Required action: Retain FNX only as the accepted negotiated route or formable after member and territory research passes.
- **IW-159 Shan federation / `GCX`** against Russian Federation: `false_fuzzy_match` / `no_identity_block`. Shan and Russian are unrelated identities whose proposed names share only federation. Required action: Retain GCX only after its full package content and exact installed-state proofs pass.
- **IW-163 Chin state / `GGX`** against CHI and PRC / China: `false_fuzzy_match` / `specific_variant_disabled`. Chin is a distinct named community; the string resemblance to China is not identity equivalence, but a generic broad-state package is not accepted. Required action: Keep GGX disabled until a named Chin district and community package is researched and bound.
- **IW-169 East Turkestan / `GMX`** against TMS and RKT / Turkestan plus turkestan_united: `blocked_pending_distinct_identity` / `high_chaos_disabled`. The working identity is related to vanilla Turkestan content and also occupies the SIK Xinjiang space; a separate carrier cannot be justified by the directional label alone. Required action: Keep GMX disabled until research proves an identity and route distinct from SIK and the vanilla Turkestan formable; otherwise implement an additive vanilla-carrier route and retire GMX.
- **IW-174 Aotearoa Maori state / `GRX`** against NZL / People's Republic of Aotearoa: `blocked_pending_distinct_identity` / `specific_variant_disabled`. The working label overlaps a vanilla NZL route identity. Only a researched consent-based iwi-led polity with distinct institutions and territory can justify a separate carrier. Required action: Keep GRX disabled; if the final package is not institutionally and territorially distinct use an additive NZL overlay and retire GRX.
- **IW-190 Pueblo federation / `HHX`** against COS / Costa del Pueblo: `false_cross_language_token_match` / `specific_variant_disabled`. The generated lead uses pueblo as the Spanish word for people and is unrelated to the Pueblo peoples; the accepted package is still too broad for automatic release. Required action: Keep HHX disabled until named Pueblo member communities and a current-map package are researched.
- **IW-193 Zapotec-Mixtec Oaxaca federation / `HKX`** against MEX / indigenous_mexico including Mixtec: `blocked_pending_distinct_identity` / `specific_variant_disabled`. The proposed federation overlaps a vanilla Mexican indigenous route that explicitly includes Mixtec identity; an Oaxaca anchor alone does not prove a separate country package. Required action: Keep HKX disabled until a distinct consent-based Zapotec-Mixtec institution is researched; otherwise use an additive MEX route and retire HKX.
- **IW-203 Patagonian state / `HUX`** against WLA / Patagonia identities and CHL / Araucania and Patagonia: `blocked_pending_distinct_identity` / `high_chaos_disabled`. Patagonian State is too generic to prove distinction from vanilla Welsh Patagonian and Araucania-and-Patagonia identities. Required action: Keep HUX disabled until a specifically civic non-Welsh and non-Araucania-claimant identity is accepted; otherwise use the matching vanilla carrier or overlay and retire HUX.
- **IW-205 Amazonian confederation / `HWX`** against Danubian and Antillean Confederations: `false_fuzzy_match` / `specific_variant_disabled`. The vanilla leads share only confederation and are geographically unrelated; the accepted package still requires named river peoples. Required action: Keep HWX disabled until named member peoples and a current-map binding are researched.
- **IW-206 Maroon republic / `HXX`** against Roman Republic and Oromo Republic: `false_fuzzy_match` / `specific_variant_disabled`. The vanilla leads share only republic and are unrelated; the accepted package requires a specifically named Maroon community and territory. Required action: Keep HXX disabled until a named community package and current-map binding are researched.

The binding curated cases remain disabled: IW-169 must be distinct from SIK and vanilla Turkestan content, IW-174 from NZL's Aotearoa route, IW-193 from MEX's indigenous route, and IW-203 from WLA and Araucania-and-Patagonia identities. If that proof cannot be made, their separate tags must be retired in favor of additive vanilla-carrier content.

## Reused-tag validation

- Registry rows already marked as reused: **91**.
- Reused rows whose tag is present in vanilla: **91**.
- Reused rows absent from vanilla but registered by Chaos Redux or installed mods: **0**.

## Shared resolved-tag review

- `BIA`: IW-096 Benin Kingdom, IW-107 Biafran regional state
- `CHU`: IW-043 Volga Bulgaria, IW-046 Chuvashia

Shared tags require mutually exclusive package reservation and package-specific readiness/origin gates.

## Shared BIA and CHU fail-closed review

| Tag | Package | Reservation group | Exact wrapper | Content attested | Scenario blocked | Runtime status |
| --- | --- | --- | --- | --- | --- | --- |
| `BIA` | IW-096 Benin Kingdom | `RG-NIGERIA-COARSE` | False | False | True | `fail_closed` |
| `BIA` | IW-107 Biafran regional state | `RG-NIGERIA-COARSE` | False | False | False | `fail_closed` |
| `CHU` | IW-043 Volga Bulgaria | `RG-MIDDLE-VOLGA-KAZAN` | False | False | False | `fail_closed` |
| `CHU` | IW-046 Chuvashia | `RG-MIDDLE-VOLGA-KAZAN` | False | False | False | `fail_closed` |

Both shared-tag pairs use one reservation group per tag, so the frozen planner cannot select both identities together. None has both an exact package wrapper and static content attestation; the legacy generic content-ready flag has zero grants. They therefore remain fail-closed until separate package-specific origin, identity, localisation, content, and audit gates are implemented.

## Safe replacement pool

The following tags end in `X` and were unused by vanilla, Chaos Redux, and every scanned installed mod at audit time. They are candidates only; a remap must update every gameplay, localisation, history, asset, manifest, scenario, specification, documentation, and catalog reference together.

`IDX IEX IFX IGX IHX IIX IJX IKX ILX IMX INX IOX IPX IQX IRX ISX ITX IUX IVX IWX IXX IYX IZX JAX JBX JCX JDX JEX JFX JHX JIX JJX JKX JLX JMX JNX JOX JPX JQX JRX JSX JTX JUX JVX JWX JXX JYX JZX KAX KBX KDX KEX KFX KGX KHX KIX KJX KKX KLX KMX KNX KOX KPX KQX KRX KSX KUX KVX KWX KXX KYX KZX LAX LBX LDX LEX LFX LGX LHX LIX LJX LKX LLX LMX LNX LOX LPX LQX LRX LSX LTX LVX LWX LXX LYX LZX MBX MCX MDX MFX MGX MHX MIX MJX MKX MLX MMX MNX MOX MPX MQX MRX MSX MTX MUX MVX MWX MXX MYX MZX NBX NCX NDX NEX NFX NGX NHX NIX NJX NKX NLX NMX NNX NOX NPX NQX NRX NSX NTX NVX NWX NXX NYX NZX OAX OBX OCX ODX OEX OFX OGX OHX OIX OJX OKX OLX OMX ONX OOX OPX OQX ORX OSX OTX OUX OVX OWX OXX OYX OZX PAX PBX PCX PDX PEX PFX PGX PIX PJX PKX PLX PMX PNX POX PPX PQX PRX PSX PTX PUX PVX PWX PXX PYX PZX QAX QBX QCX QDX QEX QFX QGX QHX QIX QJX QKX QLX QMX QNX QOX QPX QQX QRX QSX QTX QUX QVX QWX QXX QYX QZX RAX RBX RCX RDX REX RFX RGX RHX RIX RJX RKX RMX RNX ROX RPX RQX RRX RSX RTX RUX RVX RWX RXX RYX RZX SBX SCX SDX SFX SGX SIX SJX SKX SLX SMX SNX SOX SPX SQX SRX SSX STX SUX SVX SWX SXX SYX SZX TAX TBX TCX TDX TFX TGX THX TIX TJX TKX TLX TNX TOX TPX TQX TRX TSX TTX TUX TVX TWX TXX TYX TZX UAX UBX UCX UDX UEX UFX UGX UHX UIX UJX UKX ULX UMX UNX UOX UPX UQX URX USX UTX UUX UVX UWX UXX UYX UZX VAX VBX VCX VDX VEX VFX VGX VHX VJX VKX VLX VMX VNX VOX VPX VQX VRX VSX VTX VUX VVX VWX VXX VYX VZX WAX WBX WCX WDX WEX WFX WGX WHX WIX WJX WKX WLX WMX WNX WOX WPX WQX WRX WSX WTX WUX WVX WWX WXX WYX WZX XAX XBX XCX XDX XEX XFX XGX XHX XIX XJX XKX XLX XMX XNX XOX XPX XQX XRX XSX XTX XUX XVX XWX XXX XYX XZX YAX YBX YCX YDX YEX YFX YGX YHX YIX YJX YKX YLX YMX YNX YOX YPX YQX YRX YSX YTX YUX YVX YWX YXX YYX YZX ZAX ZBX ZCX ZDX ZEX ZFX ZGX ZHX ZIX ZJX ZKX ZLX ZMX ZNX ZOX ZPX ZQX ZRX ZSX ZTX ZUX ZVX ZWX ZXX ZYX ZZX`

## Scope and limitations

- The audit parses country definitions, `common/country_tag_aliases`, top-level three-character cosmetic-country blocks, concrete `set_cosmetic_tag` call sites, country-history filenames, exact three-character base localisation keys, and three-character HOI4 flag filenames.
- Engine-, wiki-, and OS-reserved three-character namespaces are excluded before collision scoring or replacement-pool generation. The offline wiki forbids `NOT`, `AND`, `TAG`, `OOB`, `LOG`, `NUM`, and `RED`; `GFX` is reserved for sprite/interface identifiers; `AUX`, `CON`, `NUL`, and `PRN` are Windows DOS device basenames.
- The scan is intentionally over-inclusive: it audits every installed Workshop directory, not only enabled playset mods, plus every sibling local mod directory beside Chaos Redux.
- ZIP members under standard HOI4 tag, alias, country, event, history, localisation, and flag paths are scanned in memory without extraction. The audit fails closed if an installed `.7z` or `.rar` archive is present.
- Identity comparison uses vanilla country-definition basenames and English localisation. Exact matches block acceptance; fuzzy matches require historical/manual review and may represent related but distinct polities.
- Cosmetic tags have no single engine registry, so call sites, localisation, and flags are treated as collision evidence. A localisation-only hit can be over-inclusive but is safer than silently taking another mod's route identity.
- Tags constructed dynamically through meta effects, scripted localisation, non-text archives, or filenames outside the standard HOI4 folders require manual review; no such construction should be assumed collision-free.
- This report does not rename tags. It is the evidence gate for a reviewed repository-wide migration.

## Input fingerprints

- Audit script SHA-256: `17fb39255f6d7a59d50c7c329ae59ea61fb6d6fcf4a0376faa910cab6896a605`
- Event 006 tag registry SHA-256: `81a5eb91c2f84cef458fa63750275dc8123574d858961a4b415c30d024d64461`
- Event 006 formable/cosmetic registry SHA-256: `673d7b9f8a5813f0481f8b79644865c24e6ef1ff5c65519653d6b0a78ca5f7df`
- Candidate matrix SHA-256: `5a9d5612e83689df591fbdad9aacf694debe34897e0cf2f19b5dfc4e3d8d51a8`
- Formable-family matrix SHA-256: `816162e3ffd6ce702bfcab591fc85bc49c875343a6d857fa80475e6c2af23169`
- Formable base-localisation inventory SHA-256: `b3576aa9071d60d1dd05857d5475da2996471ec0acd892449b3fe3ed1d3a8607`
- Manual identity dispositions SHA-256: `08fd0882fb52175b18229d0d85cfbf093e5dc50610f1ec3cb31363237457791c`
- Vanilla `00_countries.txt` SHA-256: `b3777a74b44bfb1b082817b2a1e9676f0c8cda45a0cbea75e55e2b703f3b73b6`
- Vanilla country localisation SHA-256: `31aad14d7e190da4f230c7b3fe16e4a087b8ea89951fede2743d5aec0f016706`
- Vanilla checksum manifest SHA-256: `771814d81faf7bae0f32819380c1114c61bbec1c897b060cecd1592f104f2b76`
- Parsed vanilla tag-surface inventory SHA-256: `57dfbe267a32983680c3fa385cce69e7e7a9cd52af06d8ec8bf8bb6508004d09`
- Parsed Workshop tag-surface inventory SHA-256: `c4e0f8f99a79be4459ad4a8c0068c9c4bf6319c594c2d8a0cc6c756a65035fb3`
- Parsed sibling-mod tag-surface inventory SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Parsed non-Event 006 Chaos Redux tag-surface inventory SHA-256: `cbf71bad63cfade6f8f4f3f9b02c39c83eabce4261723869b90bd9aaa7b7145d`
- ZIP archive content inventory SHA-256: `c190bac538705eeb79d7dd04e5f87c0fd59c7c7688856f30c419450d8029305c`
- Runtime attestation source SHA-256: `58936aaf298fa38a1ebb5e99706d0ff81c52334eb4342de50f8ed42ab12439f1`
- Package-origin wrapper source SHA-256: `bc1470ff76efeddee1f99292fdc4fdff4b42e22f561e991ad17f6d387bc9f64b`
- Scenario block source SHA-256: `d9a2e870945c4bab459f8d3eb243bb014e41af3a328d28204a175a4794f10823`
