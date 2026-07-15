# Event 006 installed country-tag and vanilla-reuse audit

Audit date: 2026-07-15

## Binding result

- Candidate registry rows: **206**.
- Reserved Event 006 tags scanned: **102**.
- Registered vanilla-tag reuse rows: **91**.
- Non-selectable vanilla route-overlay rows: **13**.
- Engine-reserved three-character namespaces excluded: **GFX**.
- Installed Workshop directories scanned: **122**.
- Workshop directories containing country-tag definitions: **37**.
- External and vanilla country-tag definitions parsed: **7981**.
- External and vanilla alias/cosmetic/history/localisation/flag tag uses parsed: **69474**.
- Other Chaos Redux country-tag definitions parsed: **48**.
- Other Chaos Redux alias/cosmetic/history/localisation/flag tag uses parsed: **965**.
- Reserved-tag collisions: **0**.
- Packages with exact or state-word-normalized vanilla identity matches requiring reuse review: **0**.
- Packages with fuzzy identity matches requiring manual review: **9**.
- Collision-free unused `??X` replacement candidates: **453**.

## Reserved-tag collisions

No reserved Event 006 tag collides with the scanned installed registries.

## Vanilla identity comparison

| Event 006 package | Proposed identity/tag | Vanilla candidate | Confidence |
| --- | --- | --- | --- |
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
| IW-205 | Amazonian confederation / `HWX` | Danubian Confederation / cosmetic_tag `HUN_EMPIRE` | manual_review (0.8444) |
| IW-205 | Amazonian confederation / `HWX` | Antillean Confederation / cosmetic_tag `antilles` | manual_review (0.8261) |
| IW-206 | Maroon republic / `HXX` | Roman Republic / country_tag `PAP` | manual_review (0.8276) |
| IW-206 | Maroon republic / `HXX` | Oromo Republic / country_tag `ORO` | manual_review (0.8276) |

Exact and `exact_after_state_words` matches are binding blockers until the identity is either switched to the vanilla tag or documented as a distinct polity. `manual_review` matches are discovery leads, not automatic remaps.

## Reused-tag validation

- Registry rows already marked as reused: **91**.
- Reused rows whose tag is present in vanilla: **91**.
- Reused rows absent from vanilla but registered by Chaos Redux or installed mods: **0**.

## Shared resolved-tag review

- `BIA`: IW-096 Benin Kingdom, IW-107 Biafran regional state
- `CHU`: IW-043 Volga Bulgaria, IW-046 Chuvashia

Shared tags require mutually exclusive package reservation and package-specific readiness/origin gates.

## Safe replacement pool

The following tags end in `X` and were unused by vanilla, Chaos Redux, and every scanned installed mod at audit time. They are candidates only; a remap must update every gameplay, localisation, history, asset, manifest, scenario, specification, documentation, and catalog reference together.

`ICX IDX IEX IFX IGX IHX IIX IJX IKX ILX IMX INX IOX IPX IQX IRX ISX ITX IUX IVX IWX IXX IYX IZX JAX JBX JCX JDX JEX JFX JHX JIX JJX JKX JLX JMX JNX JOX JPX JQX JRX JSX JTX JUX JVX JWX JXX JYX JZX KAX KBX KCX KDX KEX KFX KGX KHX KIX KJX KKX KLX KMX KNX KOX KPX KQX KRX KSX KUX KVX KWX KXX KYX KZX LAX LBX LCX LDX LEX LFX LGX LHX LIX LJX LKX LLX LMX LNX LOX LPX LQX LRX LSX LTX LVX LWX LXX LYX LZX MBX MCX MDX MFX MGX MHX MIX MJX MKX MLX MMX MNX MOX MPX MQX MRX MSX MTX MUX MVX MWX MXX MYX MZX NBX NCX NDX NEX NFX NGX NHX NIX NJX NKX NLX NMX NNX NOX NPX NQX NRX NSX NTX NUX NVX NWX NXX NYX NZX OAX OBX OCX ODX OEX OFX OGX OHX OIX OJX OKX OLX OMX ONX OOX OPX OQX ORX OSX OTX OUX OVX OWX OXX OYX OZX PAX PBX PCX PDX PEX PFX PGX PIX PJX PKX PLX PMX PNX POX PPX PQX PRX PSX PTX PUX PVX PWX PXX PYX PZX QAX QBX QCX QDX QEX QFX QGX QHX QIX QJX QKX QLX QMX QNX QOX QPX QQX QRX QSX QTX QUX QVX QWX QXX QYX QZX RAX RBX RCX RDX REX RFX RGX RHX RIX RJX RKX RLX RMX RNX ROX RPX RQX RRX RSX RTX RUX RVX RWX RXX RYX RZX SBX SCX SDX SFX SGX SIX SJX SKX SLX SMX SNX SOX SPX SQX SRX SSX STX SUX SVX SWX SXX SYX SZX TAX TBX TCX TDX TFX TGX THX TIX TJX TKX TLX TNX TOX TPX TQX TRX TSX TTX TUX TVX TWX TXX TYX TZX UAX UBX UCX UDX UEX UFX UGX UHX UIX UJX UKX ULX UMX UNX UOX UPX UQX URX USX UTX UUX UVX UWX UXX UYX UZX VAX VBX VCX VDX VEX VFX VGX VHX VJX VKX VLX VMX VNX VOX VPX VQX VRX VSX VTX VUX VVX VWX VXX VYX VZX WAX WBX WCX WDX WEX WFX WGX WHX WIX WJX WKX WLX WMX WNX WOX WPX WQX WRX WSX WTX WUX WVX WWX WXX WYX WZX XAX XBX XCX XDX XEX XFX XGX XHX XIX XJX XKX XLX XMX XNX XOX XPX XQX XRX XSX XTX XUX XVX XWX XXX XYX XZX YAX YBX YCX YDX YEX YFX YGX YHX YIX YJX YKX YLX YMX YNX YOX YPX YQX YRX YSX YTX YUX YVX YWX YXX YYX YZX ZAX ZBX ZCX ZDX ZEX ZFX ZGX ZHX ZIX ZJX ZKX ZLX ZMX ZNX ZOX ZPX ZQX ZRX ZSX ZTX ZUX ZVX ZWX ZXX ZYX ZZX`

## Scope and limitations

- The audit parses country definitions, `common/country_tag_aliases`, top-level three-character cosmetic-country blocks, concrete `set_cosmetic_tag` call sites, country-history filenames, exact three-character base localisation keys, and three-character HOI4 flag filenames.
- Engine-reserved three-character namespaces are excluded before collision scoring or replacement-pool generation; `GFX` is reserved for HOI4 sprite and interface identifiers.
- The scan is intentionally over-inclusive: it audits every installed Workshop directory, not only enabled playset mods.
- Identity comparison uses vanilla country-definition basenames and English localisation. Exact matches block acceptance; fuzzy matches require historical/manual review and may represent related but distinct polities.
- Cosmetic tags have no single engine registry, so call sites, localisation, and flags are treated as collision evidence. A localisation-only hit can be over-inclusive but is safer than silently taking another mod's route identity.
- Tags constructed dynamically through meta effects, scripted localisation, non-text archives, or filenames outside the standard HOI4 folders require manual review; no such construction should be assumed collision-free.
- This report does not rename tags. It is the evidence gate for a reviewed repository-wide migration.

## Input fingerprints

- Event 006 tag registry SHA-256: `0aad27d03f0c9f71e220423df5d0e0cbd16ed2619f8a9d341a35b28ce29ee423`
- Candidate matrix SHA-256: `6c14ba0fd9158ccdc22339025a34e56d82ed7a3c9af699f079d2a41c2347af1f`
