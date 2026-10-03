# Event 021 dynamic country tag capacity audit

Disposition: blocked for an engine-qualified capacity guarantee; the local source and collision audit is complete. The handoff records a collision-free declaration candidate, but does not claim that it is an engine-validated tag bank or sufficient in a live Maximum scenario.

Acceptance basis: the parent assignment requires Event 021 Maximum to commit every eligible normal human country and explicitly disallows a safe multi-state same-tag fallback. The accepted Event 021 dynamic-front repair records the same user requirement and assigns native dynamic-tag capacity as a separate prerequisite. The candidate namespace below is an audit finding, not a newly accepted design decision.

## Findings

Vanilla declares `dynamic_tags = yes` followed by D01 through D75 in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\country_tags\zz_dynamic_countries.txt`. Its line 1 comment says the following tags are used for temporary civil wars. The file has 75 unique dynamic tag declarations and SHA-256 `C1AA62189ACD4D6D767E98596DE3A82BD285F2C0B829BF19310A7D16B1218FA4`.

The installed documentation does not state a numeric maximum for dynamic-country tags or expose a free-tag count. The offline Country creation page says that a file-local `dynamic_tags = yes` marks subsequent country definitions in that file as dynamic, and warns that an insufficient dynamic-country pool can crash the game. It also gives approximate minimum counts of 10 medium and 20 small dynamic tags for generated flags. These are source/documentation findings, not runtime confirmation that a large additive file is safe.

There is a material documentation conflict: installed `documentation\triggers_documentation.md:5462-5469` describes `is_dynamic_country` as recognizing D01-D50, while the installed vanilla country-tag file and its comment define D01-D75 as dynamic. The offline wiki describes marker-based, file-local dynamic tags. Until the live engine route resolves this conflict, arbitrary new identifiers cannot be certified to behave correctly under the trigger or across consumers.

Event 021's mandatory front rows are not a count of native dynamic identities. `event021_parent_build_front_plan` records a `host_remnant` row whose actor is the existing government, plus a primary row. An ordinary primary row uses actor type `ordinary_claimant` and its engine path makes one `start_civil_war` call, so the ordinary primary consumes one newly allocated dynamic identity per ordinary target. The complete Event 006 primary is recorded as `event006_carrier` and uses its selected package carrier. The mandatory-front value of two for ordinary targets represents host plus primary; it must not be multiplied as two dynamic tag births. The same-tag route also retains the existing country identity.

Additional ordinary-claimant children can each consume another dynamic identity when selected under the live available-front envelope. The envelope's configured stage cap reaches 16, but that is spare front capacity, not a certified count of dynamic tag births: plan rows have different actor types, and only new ordinary claimants require a new native dynamic identity. The narrow same-tag topology remains for one-state or unsafe all-island countries; it must not be used to route a safe multi-state target around pool exhaustion.

The current `random_civil_war_is_normal_human_country` trigger only requires an existing, not-actually-nonhuman country. It does not exclude dynamic countries. Therefore the 1,213 unique non-dynamic tag identities counted across installed registries are not a proven upper bound on Maximum's eligible roster. Existing dynamic countries may themselves qualify, and other vanilla/mod systems can consume or reserve the same global dynamic pool.

The registry audit found 2,498 unregistered three-character letter-plus-two-digit tag IDs in the full A01-Z99 pattern after excluding existing D01-D75 and Workshop G01. The wholly free M01-Z99 subrange contains 1,386 IDs, which is collision-free in the scanned registries. Neither declaration count proves sufficient or insufficient capacity for the live transaction. A01-Z99 is a source-level namespace candidate only: it is not proven to be recognized as dynamic by `is_dynamic_country`, and all dynamic identifiers share one engine pool rather than an Event 021-private pool.

The previous `2 × 1,213 + 75 + 16 = 2,517` calculation is withdrawn as a dynamic-identity bound. It incorrectly treated the host and primary front rows as two new dynamic countries and treated the full spare-front cap as dynamic births. A correct transaction demand count must classify the frozen plan by actor type: count each new `ordinary_claimant` identity, including optional ordinary children, and add all already allocated or reserved dynamic identities in the shared engine pool. Do not count `host_remnant`, `event006_carrier`, or `same_tag_claimant` rows as new Event 021 dynamic tag allocations. The actual roster can include dynamic countries, optional ordinary-child count is scenario-state dependent, and external `reserve_dynamic_country` state may be absent from the live country roster. No corrected numeric pool sufficiency bound is certified here.

No safe affirmative Maximum capacity conclusion is available from the current exact contract. `start_civil_war` uses the shared dynamic-country mechanism; `create_dynamic_country` and `reserve_dynamic_country` are also used by vanilla, Chaos Redux, and multiple installed Workshop mods. The effect documentation defines creation and reservation behavior but gives no API for total/free dynamic slots. The installed `is_dynamic_country` trigger wording may not recognize added tag IDs. The current Event 021 front ledger is not a substitute for native dynamic-tag availability.

## Country package coverage checklist

- [x] Country-tag declaration inventory: vanilla, active Chaos Redux, all 23 installed Workshop roots, and every sibling directory under the local mod parent were scanned under `common\country_tags\**\*.txt`.
- [x] Dynamic tag declarations: all marker files found; every dynamic tag ID in the scanned roots belongs to D01-D75, with overlapping declarations across mods.
- [x] Candidate tag collision check: no M01-Z99 identifiers were declared; A01-Z99 has only the known D01-D75 and G01 exclusions.
- [x] Maximum front-row/source review: ordinary mandatory rows are existing `host_remnant` plus one `ordinary_claimant`; Event 006 primary uses an `event006_carrier`; additional ordinary children may consume extra dynamic identities under the live front envelope.
- [ ] Engine-qualified tag extension behavior: blocked by MCP timeouts and the `is_dynamic_country` documentation conflict.
- [ ] Runtime free/reserved slot count: not established; no documented free-slot counter, and empty reserved identities cannot be enumerated from `is_dynamic_country` alone.
- [ ] Map/state setup, capitals, supply, ownership, and victory points: outside this bounded tag-capacity audit; no map conclusion is claimed.
- [ ] Politics, parties, leaders, portraits, flags, advisors, focuses, ideas, decisions, military, industry, technology, and AI: not audited as country packages in this bounded assignment. The flag note above is only the wiki's dynamic-tag rendering requirement.
- [ ] Event 021 MCP inspect/render: attempted but no artifact returned; source-only review is not engine evidence.

## Collision inventory and coverage

The scanner covered 33 roots: installed vanilla, Chaos Redux, 23 Workshop ID directories, and eight sibling directories under the local mod parent. It read 52 `common\country_tags` text files, found 3,511 three-character alphanumeric declarations and 1,288 unique tag identifiers, and found 670 identifiers declared in more than one root. There were no same-root duplicate identifiers, malformed or non-uppercase tag keys, unreadable registry files, or M01-Z99 declarations. The 670 overlaps include expected vanilla identities reused by overhaul mods and the duplicated Chaos Redux/Chaos Redux QA package; an overlap is not by itself an active-load-order error.

The SHA-256 of the deterministic sorted manifest consisting of each scanned absolute file path and that file's SHA-256 is `C755665492A54C31B93EAD140B381BFA8B3006426B53BFD3D439A60A154BA383` (52 files). This inventory hash records the exact scan inputs; active mod load order was not available and is not inferred.

| Source root | Country-tag files | Declarations |
| --- | ---: | ---: |
| Vanilla HOI4 | 2 | 439 |
| Chaos Redux | 11 | 171 |
| Workshop 1314446921 | 4 | 97 |
| Workshop 1521695605 | 2 | 332 |
| Workshop 1532883122 | 3 | 397 |
| Workshop 2076426030 | 4 | 406 |
| Workshop 2265420196 | 2 | 424 |
| Workshop 2541335727 | 1 | 241 |
| Workshop 2898278820 | 2 | 267 |
| Workshop 2941794727 | 3 | 83 |
| Workshop 3103846888 | 1 | 6 |
| Workshop 3199436992 | 1 | 3 |
| Workshop 3249341121 | 1 | 1 |
| Workshop 3365515312 | 2 | 401 |
| Workshop 820260968 | 1 | 71 |
| Local sibling `atlantis_the_seventh_ring` | 1 | 1 |
| Local sibling `chaos_redux_qa` | 11 | 171 |

The other ten Workshop roots had no `common\country_tags` directory: 1360299796, 2013056623, 2195460708, 2677872257, 2903857354, 2924972770, 2936314314, 3291386312, 3368794044, and 3469310112. The other six local sibling directories had no country-tag files: `3d_pipeline`, `agentic_hoi4_modding`, `chaos_redux_music`, `docs`, `ireland`, and `ireland_total_overhaul`. All eight local `.mod` descriptors point to their matching sibling directory beneath the audited mod parent. No registry root or file was unreadable.

Workshop G01 is declared at `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\country_tags\r56_countries.txt:10`; it is excluded from the candidate range. Several Workshop mods repeat D01-D75 (one declares 50, others 70 or 75), but these are the same tag identities and do not add unique capacity. Current Chaos Redux has no `dynamic_tags = yes` marker in its 11 country-tag files; Event 021 currently relies on the engine's shared pool.

The dynamic-creator scan over `.txt` files under `common`, `history`, and `events` also found shared-pool use beyond Event 021. Vanilla had 6 files with `reserve_dynamic_country`, 22 with `create_dynamic_country`, and 105 with `start_civil_war`; Chaos Redux had 2, 10, and 10 respectively. Workshop examples include 1521695605 (15/16/11 files), 3365515312 (26/33/56), and 820260968 (8/27/160). Counts are files containing each token, not counts of runtime actors. They demonstrate that a free declaration range is not private to Event 021.

## File surface checklist and evidence

| Source | Path, lines, SHA-256 | Finding |
| --- | --- | --- |
| Vanilla dynamic tags | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\country_tags\zz_dynamic_countries.txt:1-76`; `C1AA62189ACD4D6D767E98596DE3A82BD285F2C0B829BF19310A7D16B1218FA4` | `dynamic_tags = yes`; D01-D75 only. |
| Installed effects documentation | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:3033-3044,6367-6378,8030-8070`; `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` | `create_dynamic_country`, `reserve_dynamic_country`, and `start_civil_war`; no pool-size/free-slot API documented. |
| Installed trigger documentation | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:5462-5469`; `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` | `is_dynamic_country` documentation says D01-D50, conflicting with the 75 vanilla declarations. |
| Offline Country creation wiki | `paradox_wiki\Country creation - Hearts of Iron 4 Wiki.md:64-66,482`; `0C0E57915A7D1EEF9DDEEBE91C7329E18F4F224AF98AC33FAC5EDD35E3AAA35D` | Numeric tag syntax, file-local dynamic marker, insufficient-pool crash warning, approximate medium/small flag counts. |
| Offline Effects wiki | `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:913-916,1020-1028`; `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` | Reservation and dynamic-country effect semantics; reserve protects against recycling and is relevant even without an extant country. |
| Event 021 front reservation and Maximum envelope | `common\scripted_effects\021_random_civil_war_parent_effects.txt:422-458,7637-7657`; current SHA-256 `0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61` | Two ordinary mandatory front rows mean existing host plus primary; Maximum derives row demand from the roster and adds normal spare front capacity. |
| Event 021 host/primary plan rows | Same file, lines 1929-2015; same SHA-256 above | Host row is `host_remnant`; ordinary primary row is `ordinary_claimant`; Event 006 changes the primary row type to `event006_carrier`. |
| Event 021 primary and additional civil-war paths | Same file, lines 4261-4405 and 4475-4574; same SHA-256 above | Ordinary primary has one `start_civil_war` birth; secondary/optional ordinary-claimant children can add births. Front-row count alone does not establish tag demand. |
| Event 021 normal-human eligibility | `common\scripted_triggers\021_random_civil_war_triggers.txt:37-40`; `F8123906ED70709FEE419B6BD0988186474715AF810193AA90960CC8E3AEB170` | Existing and not actual nonhuman; does not exclude dynamic countries. |
| Event 021 scenario eligibility and same-tag front test | `common\scripted_triggers\021_random_civil_war_parent_triggers.txt:401-467,491-501`; `57BD2B2DC3169D6105380A29667A8892528B0D4DFB98A4CF37B6854B78AAFA46` | Maximum eligible roster follows the normal-human predicate; same-tag is a separate route. |
| Event 021 cap constants | `common\script_constants\021_random_civil_war_constants.txt:302-318`; `FBA1DBB902F05E96C9926FFA5C21961CC671094ABC74038C503D8CB516809BEA` | Configured active-front cap reaches 16 at World Collapse. |
| Same-tag limitation in source | `common\scripted_effects\021_random_civil_war_parent_effects.txt:7126-7129`; same SHA-256 above | Current comment restricts this topology to one-state/all-island countries; do not use it as a multi-state capacity fallback. |
| Accepted dynamic-front repair | `docs\plans\021_random_civil_war_plans\event021_dynamic_front_ledger_repair_2026-10-03.md:4,20,125-126`; `55E932593E0EDA00F841351745371A9E6C5B87889BD911D18C1832F00C28BFEC` | Maximum's front envelope is already dynamic; the plan explicitly says it does not prove native tag capacity and assigns this audit. |
| Prior Maximum preflight handoff | `docs\plans\021_random_civil_war_plans\subagent_handoffs\scenario_maximum_preflight_commit_repair_2026-09-19.md`; `097DC368ED774A9C80074BC9345CA45FDA3C897FF16213290B72CF48799313E9` | Prior preflight/commit repair is not a tag-capacity certificate. |

The Event 021 source hash above is the current local source identity read during this audit. Older source hashes and MCP artifacts in prior handoffs are historical evidence and were not substituted for current MCP inspection.

## MCP route evidence and exact blockers

The live schemas for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, and `hoi4.event_render` were exposed and inspected. No HOI4 health/version route was exposed in the connected tool inventory. No helper expansion, job, native task, or game launch was used.

- `reference_context` with an eight-source limit and an exact dynamic-tag question did not return during the bounded wait; a retry with limit 2 also remained pending beyond 60 seconds and was stopped.
- Three narrow `reference_search` requests for `dynamic_tags = yes`, D01-D75, and civil-war tag requirements did not return during the bounded wait and were stopped.
- `source_lookup` for `dynamic_tags` with five definitions/60 lines returned `timed out awaiting tools/call after 600s`. A narrower one-definition/ten-line retry remained pending beyond 60 seconds and was stopped.
- `reference_read` was not called because context/search did not return a revision-bound source ID; fabricating those required arguments would not be valid evidence.
- Read-only `event_inspect` (`state_flow`, selector `{ kind: event, eventId: chaosx.nr21.1 }`, depth 1, 32 nodes, 64 edges, helpers disabled) and `event_render` (`overview`, same selector, 32 nodes) both remained pending beyond 60 seconds and were stopped. No current revision, diagnostics, render, or artifact URI was returned.

Consequently there is no current MCP event inspection/render evidence and no revision-bound MCP reference evidence in this handoff. The direct local documentation reads above are source evidence only and are not an MCP or in-game substitute. The exact engine interpretation of arbitrary added tag IDs and the current free/reserved pool remain unresolved.

## Proposed bounded implementation for parent review

The source-level candidate is one dedicated file under `common\country_tags` beginning with its own `dynamic_tags = yes` marker, with unique IDs drawn only from the audited free letter-plus-two-digit set. Each entry must map to an existing generic country definition rather than introduce a historical or playable country package. Vanilla already reuses generic D-country definition paths for multiple dynamic tags. Do not edit vanilla's tag file, and do not substitute same-tag takeover for a safe multi-state target.

Before choosing an actual range or declaring it sufficient, the parent needs a current engine/MCP answer to the D01-D50 versus D01-D75 conflict and evidence that the added identifiers are recognized as dynamic. Capacity must be checked against the frozen plan's new `ordinary_claimant` rows, current allocated/reserved dynamic identities, and any optional ordinary children allowed by the live spare-front envelope. The added tags would be globally allocatable to the other systems found in the source scan, so a private Event 021 allocation cannot be inferred from an unused prefix. If that full capacity cannot be established, keep Maximum unresolved/blocked rather than silently truncating its roster or changing safe multi-state targets into same-tag contests.

## Remaining package scope and completion limits

This audit did not inspect state ownership, capitals, victory points, supply, country history, military setup, parties, leaders, portraits, advisors, flags/assets, focuses, decisions, ideas, technology, industry, AI behavior, or campaign survival. It made no source/gameplay/assets/index changes and did not launch HOI4. No weighted surface was patched, so no probability compare was required. The full Event 021 goal remains open; this handoff only resolves the installed country-tag registry inventory and documents the native dynamic-tag contract limits.
