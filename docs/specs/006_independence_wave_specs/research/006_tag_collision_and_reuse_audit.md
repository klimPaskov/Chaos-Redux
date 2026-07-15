# Event 6 tag collision and vanilla-identity audit

Audit lock date: 2026-07-15

## Accepted representation architecture

The 206 registry rows resolve to exactly one of three representations:

| Representation | Count | Event 6 rule |
| --- | ---: | --- |
| Custom Event 6 country | 102 | Register a collision-free three-character tag ending in `X`. |
| Registered vanilla-tag reuse | 91 | Instantiate the registered tag only while it is not living; preserve its country/history files and origin-gate all Event 6 content. |
| Non-selectable vanilla route overlay | 13 | Observe the exact vanilla cosmetic, dynamic country, formable, autonomy identity, or ideology route and add a safe package overlay. Do not create another country. |
| Total | 206 | Every registry row has one representation. |

The authoritative mappings are `matrices/006_candidate_country_registry.csv` and `research/006_package_research_resolution.csv`. Package binding and force records must use the same `resolved_tag`; overlay rows keep that field blank.

## Scan universe and method

The decisive audit scanned:

- the installed vanilla game;
- every one of the 122 direct mod directories under `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360`;
- the sibling local mods `agentic_hoi4_modding`, `chaos_redux_music`, and `slop_redux`;
- Chaos Redux country tags, aliases, cosmetic calls, country history, base country localisation, and flags.

The scan parsed 7,981 literal country-tag registration records representing 2,262 unique tags and 986 top-level alias records representing 840 unique aliases. It also checked literal `set_cosmetic_tag` calls, exact three-character base localisation keys, flag filenames, and country-history filenames. All 206 provisional Event 6 reservations remain excluded from the replacement pool even when their package later became a vanilla reuse or overlay.

No accepted custom Event 6 tag overlaps a tag or alias found in that installed universe or consumes the engine-reserved `GFX` graphics namespace. The post-migration identity comparison found `IW-153` Dayak federation equivalent to vanilla `POK`'s Dayak Republic of West Borneo identity; `FWX` was therefore retired and `IW-153` now reuses `POK`. A later installed mod can still consume a tag, so the audit must be rerun immediately before any later tag migration or final completion audit.

## Installed-mod collision migrations

| Package | Retired value | Locked representation |
| --- | --- | --- |
| `IW-087` Fezzan | `DIX`, registered by Red Flood | Custom `HYX` |
| `IW-124` Basotho | `ETX`, used as an Empire of Texas cosmetic by KaiserreduX and copies | Custom `HZX` |
| `IW-161` Mon State | `GEX`, a German-exile alias in Kaiserreich and KaiserreduX | Custom `IAX` |
| `IW-162` Kachin State | `GFX`, the engine-reserved graphics identifier namespace | Custom `IBX` |
| `IW-157` West Papua | `GAX`, registered for Galápagos by TNO | Reuse registered `WPG`; retire `GAX` |
| `IW-059` Mesopotamian Federation | `CGX`, occupied by vanilla and copied flag surfaces | Additive `neo_mesopotamia` formable overlay; retire `CGX` |

`HYX`, `HZX`, `IAX`, and `IBX` were the first deterministic safe values in the matrix-aware pool. Retired values and engine-reserved namespaces are not recycled.

## Registered-tag migrations and compatibility obligations

These thirteen packages no longer register duplicate Event 6 countries:

| Package | Retired Event 6 value | Registered tag | Required compatibility work |
| --- | --- | --- | --- |
| `IW-038` Ruthenia | `BLX` | `RUT` | Preserve the CZE release, OOB, player-switch, and RUT AI paths; branch them around a living Event 6-origin RUT. |
| `IW-042` Galicia-Lodomeria | `BPX` | `GAL` | Preserve registered GAL history and the idempotent CZE core interaction. |
| `IW-043` Volga Bulgaria | `BQX` | `CHU` | Use a package flag to distinguish it from `IW-046` Chuvashia and deliberately handle Idel-Ural eligibility. |
| `IW-096` Edo Kingdom of Benin | `DRX` | `BIA` | Use a package flag to distinguish it from `IW-107` Biafra; the two packages are mutually exclusive in `RG-NIGERIA-COARSE`. |
| `IW-133` Bengal | `FCX` | `BAN` | Preserve and branch the GOE, RAJ, and UK Bengal release or subject paths; unified Bengal remains formable-only. |
| `IW-150` Aceh | `FTX` | `ATJ` | Preserve and branch the Indonesian release route around a sovereign Event 6-origin Aceh. |
| `IW-153` Dayak federation | `FWX` | `POK` | Preserve POK history, characters, cores, Indonesian releasable membership, and character-transfer logic; keep the named-community restriction. |
| `IW-155` Bali | `FYX` | `BLI` | Preserve and branch Indonesian character-transfer logic so it cannot strip Event 6 characters. |
| `IW-157` West Papua | `GAX` | `WPG` | Preserve Japanese and Indonesian interactions and the named-community readiness restriction. |
| `IW-167` Champa | `GKX` | `CHM` | Preserve Japanese Indochina and Indonesian regional interactions. |
| `IW-171` Ryukyu | `GOX` | `OKN` | Preserve registered history and East Asian faction behavior. |
| `IW-172` Ainu State | `GPX` | `ANU` | Preserve the Japanese Ainu focus/event route and prevent it from silently puppeting or recreating an Event 6-origin ANU. |
| `IW-178` Papua | `GVX` | `PNG` | Preserve USA decolonisation, Japanese targeting, and Indonesian regional paths around a living Event 6-origin PNG. |

Common rules for every reuse:

1. Never register the tag again or replace its vanilla `common/countries`, history, characters, flags, or base localisation.
2. It is a candidate only while `exists = no` and while its package-specific readiness and reservation checks pass.
3. Set Event 6 origin and package flags inside the synchronized creation chain before assigning content.
4. Gate focuses, decisions, events, AI, mechanics, identity changes, and localisation by the package flag, not by tag alone.
5. Preserve the normal vanilla branch whenever the package flag is absent.

The shared resolved tags are intentionally limited to `CHU` (`IW-043`/`IW-046`) and `BIA` (`IW-096`/`IW-107`). Allocation must reserve their tags and reservation groups before release, so both variants cannot enter one wave.

## Thirteen exact vanilla overlays

Overlay rows are not selectable release candidates and receive no custom country registration, history file, standalone country file, independent flag package, or tag-selected Event 6 tree.

| Package | Exact vanilla carrier or route |
| --- | --- |
| `IW-005` Flanders | `BEL` with `BEL_flanders` cosmetic |
| `IW-022` Dalmatia | Dynamic country with `original_tag = CRO` and `dalmatia` cosmetic |
| `IW-025` Vojvodina | Dynamic country with `original_tag = HUN` and `vojvodina` cosmetic |
| `IW-035` Livonia | `LIT` with `LIVONIA` cosmetic |
| `IW-059` Mesopotamian Federation | Carrier that completed the vanilla `neo_mesopotamia` formable |
| `IW-085` Cyrenaica | `LBA` under the applicable Italian autonomy identity; independent release remains suppressed |
| `IW-101` Kongo | `COG` with `COG_kingdom_of_kongo` cosmetic |
| `IW-102` Kuba | `COG` with `COG_kingdom_of_kuba` cosmetic |
| `IW-105` Loango | `COG` with `COG_kingdom_of_loango` cosmetic |
| `IW-156` Moluccan Federation | Democratic `TNE`, the United States of Maluku identity |
| `IW-196` Caribbean Federation | Carrier that completed the vanilla `antilles` formable |
| `IW-197` Mapuche Federation | `CHL` with `CHL_mapuche_state` cosmetic |
| `IW-204` Araucania and Patagonia | Carrier with `kingdom_of_araucania_and_patagonia` cosmetic |

An overlay activates once per carrier through a narrow route completion or package hook. It must preserve the carrier's existing focus tree, history, cores, state transfers, autonomy, global flags, and formable effects. Merely setting the cosmetic tag is not an implementation of a vanilla formable. A global daily, weekly, or monthly country iteration is neither required nor authorised.

## Distinct identities retained as custom countries

Vanilla resemblance alone does not make two identities equivalent. Sardinia remains distinct from Sardinia-Piedmont, Sicily from the Two Sicilies, the researched northwest-Caucasus Circassian package from Kabardino-Balkaria, a negotiated Hausa federation from Sokoto, an iwi-led Māori federation from an ideology-name variant of New Zealand, and a civic Patagonian state from Y Wladfa. These packages remain custom only while their exact identity and territory research supports that distinction. The generic Dayak row did not meet that distinction and was moved to `POK` reuse.

## Completion gate

This audit locks identifiers and representations; it does not by itself complete the thirteen vanilla compatibility branches or the thirteen additive overlay adapters. Any reuse without origin gating, or any overlay that creates a duplicate country, remains incomplete. The implementation-time report is `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_15.md`; the initial read-only handoff is preserved as superseded evidence at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_installed_tag_and_vanilla_identity_audit_handoff.md`.
