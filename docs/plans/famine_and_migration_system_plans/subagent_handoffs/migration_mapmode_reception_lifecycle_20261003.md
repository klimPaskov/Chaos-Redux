# Migration mapmode reception lifecycle audit

Date: 2026-10-03.
Mode: read-only source/MCP audit; this new handoff is the only file written by this worker.
No gameplay, GUI, GFX, localisation, existing documentation, baseline, staging or commit changes were made by this worker.
The first-host implementation is committed in `59ee4eb62`, with documentation checkpoint `58efb2247`; unrelated shared-tree commits and edits were preserved.
The full famine/migration goal remains incomplete.

Disposition: current-layer audit complete at source level; parent-applied capacity label correction independently source-checked; bounded incoming-front intent presentation plan accepted and queued for parent implementation/review, not implemented here.
Acceptance basis: the user requires two independent comprehensive start-available mapmodes, and the parent accepted the confirmed incoming-front gap and a narrow identity-preserving receiver-state intent plan on 2026-10-03 within that request.
No new mapmode, GUI, asset family, public value, population/capacity guarantee or route proof is proposed.

## Source identity and exact read locations

Paths are repository-relative unless prefixed with the installed game path.
Hashes bind the audited source snapshot, not native execution.

| Source | Relevant lines | SHA-256 |
| --- | --- | --- |
| `common/map_modes/chaosx_state_map_modes.txt` | Famine 390–569; migration 571–921 | `CA8FAC1EB0048319189BAFC43568ABE11A2FA0ED30B62FB2C8611A052B69A888` |
| `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` before parent display fix | Migration role/detail/identity/status 648–1154; capacity 837–849 | `F50E68EF4D157709B333207A8290AF0A440BA94353B7FA63C4CE406C1F539329` |
| Same scripted localisation after parent display fix | Capacity delegates to strict owner trigger at 837–847; later lines shift by one | `8088F09235A754776AF4DFED86FB5187671A1E341672BE7EB7A938ACFEC9C468` |
| `localisation/english/chaosx_map_modes_l_english.yml` | Famine 131–152; migration 154–233 | `1943DACAE6526EB7B707CF31624CBD06D19B42920F219B1D48FACADA60379AE6` |
| `common/scripted_effects/migration_presentation_effects.txt` | Record/clear helpers 15–457; refresh 459–996; transit/readiness 760–839 | `C2B7E9A43EF63A336F7B5E216BA733D74B6A9A2B98CE25CF6FAE71DD30489C50` |
| Paired `migration_presentation_effects.md` | Complete 175-line helper/projection contract | `3E4AF9B851626A3DC36ADD0B8CC4FCB8FE888520C42A36FA6F322AB4BD9D757F` |
| `common/scripted_effects/humanitarian_corridor_effects.txt` | Prepare 82–311; submit 313–381; accept 383–471; record/pass 573–706; cleanup 1075–1232 | `2FB40A4A239374B40A05D935419B1A744C6DDD6A41B977011493BE0B2A02211B` |
| `common/scripted_triggers/humanitarian_corridor_triggers.txt` | Front/current-row/headroom/offer interfaces 98–401 | `A580C3D9852927B3FB0BB2195A8BB894D4533ADD5750F4B5834022DB8DE8BE50` |
| `common/scripted_effects/migration_reception_preparation_effects.txt` | Paid effect 5–221 | `C3830BF545A9F9F68C3BE34F7EA326D2A53F9185126B716FE02703D90907DBA9` |
| `common/scripted_triggers/migration_reception_preparation_triggers.txt` | Visibility/target/meaningful change 13–110 | `C22AE4A5E1930223CCA94F004D95BFC3872CD0C521B458EA97B80480DFAE1910` |
| `common/decisions/migration_decisions.txt` | Accept/reject 1201–1242; native preparation target 1243–1280; local integration 1895–1941 | `66D5DACCB52B11787A53A899B748B2E8F5427E0A8B46A4B303E8BB6A37A01D2F` |
| `common/scripted_effects/migration_core_effects.txt` | Exact movement projection 827–946; reception 1000–1106; outcome/return/integration 1111–1244 | `13AEFF3FD29089A97D778D89894588E107EBF8AAF906DE3D231CAE23DB6063CA` |
| `common/scripted_effects/migration_capacity_effects.txt` | Candidate/service registration 10–77; dirty setter 56–63 | `62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B` |
| `common/scripted_triggers/migration_core_triggers.txt` | Strict capacity 349–361 | `00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE` |
| `common/script_constants/state_map_modes_constants.txt` | Migration palette 280–399 | `D2B15FBCB7162E0AB31D5D8FE61B24EFB2FDEBDE516577C030F17FC19ACF09A2` |

## Independence, startup and current layers

There are two separate dedicated definitions, `famine_state_map_mode` and `migration_state_map_mode`, in the shared physical mapmode file.
Neither definition has category/problem/incident visibility gating.
Both have STATE top/bottom layers, evaluated through FROM, `far_text = country`, `near_text = state` and daily refresh.
Installed mapmode documentation states that scripted definitions are added to the faction-mapmode family and specifies automatic button/name/tooltip keys.
Both selected/deselected button sprites exist in `interface/mapmodes_interface.gfx` lines 56–69, and all four referenced DDS files exist.
This establishes start-available source wiring, not observed button rendering.

Famine stays independent: its fill uses stable/strain/acute/famine/catastrophic stage; its border priority is verified blockade, delivered relief, proven relief route, then current food pressure, with catastrophic highlighting.
It is not combined with migration intent, flow, reception or transfer context.

The migration bottom role priority is trapped, overcrowded, organized operation, live displacement origin, preparation-to-leave, mission return readiness, actual return, actual resettlement, policy-classified transit reception, actual reception, then neutral.
`GetMigrationStateMapModeRole` mirrors that order.
The top priority is trapped obligation, overcrowding, closed/violent/forced-return border policy on a relevant state context, known terminal failed evacuation corridor, pending evacuation offer, accepted/operating/manual mission corridor, positive reception load, then live flight intensity.
Overlaps deliberately preserve trapped/overcrowded priority; authorized tooltip status exposes secondary corridor context.

Current palette families already include preparation yellow, corridor-offer yellow, accepted-corridor blue, reception blue, transit cyan, return/readiness green and failed corridor red.
No new art or color family is needed to add an intent-qualified endpoint label using existing families.
Any prospective use of preparation yellow must have a distinct qualitative label such as reception requested/prepared, not reuse the origin phrase “Preparing to leave.”

Categories remain separate and problem-gated in their respective category files.
The accepted Part 6 presentation names exactly Food Security, Food Reserves and Relief Access for famine, and Displacement Load, Reception Capacity and Border Policy for migration.
The category/header bindings were consulted only as source context; no GUI layout audit, change or visual certification was performed.

## Existing selector fields and lifecycle coverage

| Context | Actual cached producer and map reads | Current coverage and limit |
| --- | --- | --- |
| Pending evacuation origin | Prepare/submit writes origin contract, `humanitarian_corridor_offer_pending`, operation evacuation, status offer_pending, generation, cohort and preparation receipt; map top/status getter read these fields | Source endpoint covered, usually trapped-first fill/border; authorized corridor text says awaiting response. No arrival is claimed. |
| Real pending incoming front | Receiver COUNTRY carries offer origin/front/requester/cohort/operation/generation/deadline; receiver STATE has no new request-intent projection | Dedicated map does not read the receiver offer-front mirror. Quiet front remains neutral with “No sustained movement,” even for its owner/controller. Genuine gap. |
| Paid-prepared front before consent | Successful paid helper installs genuine shelter/medical proof and `migration_reception_candidate_active`, recalculates owner capacity and opens policy; no reception load or state arrival flag | Candidate/service fields are not map role/detail inputs. Quiet front still neutral; paid services are not falsely shown as arrivals. Genuine intent gap persists. |
| Accepted before passage | Accept writes status accepted and response/operation flags on origin, then clears host COUNTRY offer mirror; no front population/load/destination bind | Origin accepted status covered; front remains neutral. Accepted consent is not arrival. Genuine intent gap persists. |
| Actual arrival | Exact finalizer writes state/country reception delta, `migration_reception_context_active`, positive `migration_state_reception_load`, `migration_projection_last_role/cohort/generation/reception_share` | Reception/host/destination role and pressure border covered; only measured survivor credit supplies these fields. Ordinary passage terminal clears corridor, not permanent arrival ledgers. |
| Declined/expired/invalidated origin | Cleanup snapshots exact `humanitarian_corridor_last_terminal_status` plus last terminal operation before clearing live contract | Authorized status getter and failed border cover the terminal. Trapped priority may mask border color; tooltip still exposes terminal status. No false disappearance of source obligations. |
| Declined/expired front | No arrival/load was ever credited; paid service receipts persist after real payment | Returning to neutral is truthful, but there is no incoming intent context to clear/show currently. Future intent cleanup must never erase real paid services or other receptions. |
| Return | Exact finalizer records voluntary/forced-return role; `migration_record_state_return_projection` writes returned amount/context; hosted readiness receipt is independently recorded | Actual return green role/destination and authorized return type are covered. Primary readiness specifically requires mission-return subject plus return context; the standalone presentation readiness flag is not consumed by the map role. Native targeted return actions/mission are separate coverage. |
| Resettlement | Exact survivor/outcome projection writes state resettled amount/context and last role | Resettlement role/destination and authorized identity/count are covered without another population grant. |
| Integration | COUNTRY integration API records national integrated amount; targeted decision debits exact reception and records receiving-state achievement evidence | Map currently provides authorized owner-national integration context with explicit destination-unknown fallback. No current producer sets `migration_projection_last_role` to local-integration in the audited source; that specific getter branch is not a proven local-map path. Do not fabricate a state integration destination from a country total. |
| Transit | Exact finalizer records hosted transit projection/role; presentation derives `migration_presentation_transit` from positive identity-bearing receipt; actual reception load remains authoritative | Primary map transit classification requires positive reception load/context plus owner border policy transit_only. A transit receipt under a different current policy is generic reception, with authorized latest-transit identity. Map does not consume the presentation transit flag directly. This is a narrower classification limit, not proof of missing arrival. |
| Deportation | Actual forced transaction records last role deportation; pressure/source endpoints record deportation cause; arrival/exodus/trapped ledgers remain separate | Authorized flow/source identify forced deportation, while public map uses truthful generic origin/host/reception/trapped role and does not disclose foreign headcounts/cause details. No distinct new deportation color/art family is necessary. |

Selectors use exact state-local fields: origin role from trapped/prepared/mission/live flight; host role from positive reception; destination role from positive reception/resettled/returned counters; departure/arrival share from latest measured projections; flow identity from last role with explicit cause/outcome/owner-national fallbacks; corridor status/generation/route from evacuation-only origin fields and known terminal operation provenance.
`GetMigrationStateMapModeDetail` authorizes numeric detail only for owner/controller ROOT and an actual relevant state context, positive load, current cohort or evacuation contract/terminal.
Its public fallback contains only the qualitative role.
The detailed template reads state load from FROM and national capacity/integration/resettlement from FROM.owner, not controller or an origin requester's country.
Incoming requester/third-party viewers do not obtain front headcount/capacity from the current public tooltip.
Map color and tooltip paths contain no global cohort-array traversal or population mutation.

## Native targeted-action coverage: inventoried before calling a gap

`migration_open_reception` is a real native state-targeted action: `state_target = any_controlled_state`, `on_map_mode = map_and_decisions_view`, existing open-border icon and exact target helper.
Offline Decision modding lines 576–610 explains that state-targeted decisions draw icons above their targets while the decision menu is open and that this mode draws both map and list entries.
Installed decision documentation lines 12–55 establishes the actor/FROM scopes, refresh cadence and controlled-state domain; vanilla `AFG.txt` lines 477–489 provides a concrete state-target plus map-and-list precedent.

While the receiver's category is revealed and setup can meaningfully improve services/policy, the exact pending front is selectable/identified by that native target icon.
This is receiver-only action coverage, not a universal persistent custom-map endpoint overlay, and not an arrival or route proof.
A quiet first tiny request remains hidden by existing category thresholds.
Once the paid configuration is installed and policy open, `migration_reception_preparation_can_change_state` is false, so that state stops matching the preparation target.
Accept/reject are untargeted COUNTRY decisions with no front state-target/on-map declaration.
Their text identifies origin/front for the receiver, but does not supply persistent endpoint role/color/tooltip coverage in the dedicated map after preparation.
Thus existing icons narrow but do not eliminate the confirmed paid-prepared/accepted-before-pass map gap.

## Independent parent capacity-display correction

The pre-fix `GetMigrationStateMapModeReceptionCapacityStatus` checked only owner raw `migration_reception_capacity_valid = 1`.
The dirty setter sets `migration_reception_capacity_dirty = 1` without clearing that raw flag.
The strict gameplay validity trigger additionally requires valid country, current schema, dirty zero, positive revision/capacity/candidate/safe-candidate counts and zero invalid candidates.
Therefore dirty or malformed source fixtures with a retained raw valid flag were mislabeled green “valid.”

Parent accepted and applied the narrow read-only selector delegation to `OWNER = { migration_reception_capacity_is_valid = yes }`.
No recalculation, capacity write, weight or payment occurs through that selector.
Before physical hash is `F50E68EF4D157709B333207A8290AF0A440BA94353B7FA63C4CE406C1F539329`; after physical hash is `8088F09235A754776AF4DFED86FB5187671A1E341672BE7EB7A938ACFEC9C468`.
The before predicate was independently parsed from committed `59ee4eb62`; current after delegation and strict source trigger were re-read.

Thirteen parsed-source checks used baseline schema 2, raw valid1, dirty0, revision1, capacity10000, candidate1/safe1/invalid0 and explicit native country-validity input, changing the named fact for each negative case.
All expected after results matched; these are source models, not engine rendering/execution.

| Fixture | Before raw predicate | After strict predicate |
| --- | --- | --- |
| Healthy complete baseline | Valid | Valid |
| Raw valid1 with dirty1 | Incorrectly valid | Unavailable |
| Schema absent | Incorrectly valid | Unavailable |
| Schema1 instead of current2 | Incorrectly valid | Unavailable |
| Revision absent | Incorrectly valid | Unavailable |
| Revision0 | Incorrectly valid | Unavailable |
| Capacity0 | Incorrectly valid | Unavailable |
| Capacity-1 | Incorrectly valid | Unavailable |
| Candidate count0 | Incorrectly valid | Unavailable |
| Safe candidate count0 | Incorrectly valid | Unavailable |
| Invalid candidate count1 | Incorrectly valid | Unavailable |
| Native country validity false, with stale raw fields supplied | Raw predicate does not check validity | Unavailable |
| Raw validity0 | Unavailable | Unavailable |

The missing/invalid-country fixture establishes source fail-closed behavior under explicit native validity input; it does not establish what a missing engine OWNER scope renders.
Numeric cached capacity display remains owner-authorized; the corrected status prevents treating stale cached numbers as current usable capacity.

## Additional current-selector source cases

Ten conditional fixtures ran the actual parsed primary-role and detail selectors with explicit state flags/vars and owner/viewer identities.
Pending country mirror alone, paid service/candidate fields alone and accepted-country state before passage all select role_none and public detail on a quiet front, including owner viewer.
Actual positive reception selects reception plus authorized detail for owner and public qualitative detail for a third party.
Refused trapped origin selects trapped plus authorized terminal detail.
Actual return selects return; policy transit-only with live reception selects transit; a positive transit presentation receipt under controlled policy selects generic reception; national integration alone selects neutral/public on an otherwise quiet state.
These confirm the source gap/classification boundaries, not custom-color or tooltip engine execution.

## Accepted bounded plan: receiver-state intent projection only

The parent accepted a narrow plan if it preserves older accepted plus newer pending contexts, cohort truth and privacy.
No source implementation is authorized to this audit worker.
The intended labels are reception requested, reception prepared and reception agreed/passage pending, never arrival, current host, bound destination or confirmed usable route.
The audience is the front's owner/controller only; requester/foreign/public viewers retain current qualitative public behavior and no new headcount, foreign capacity or intent disclosure.
Follow existing large/repeated/sustained reveal policy rather than letting an intent publication or map hover reveal a first tiny offer/category.
Both map buttons remain available at start; categories and their three canonical values remain unchanged.

### Helper/receipt plan

| Proposed helper | Scope and inputs | Outputs/default and side effects | Call site |
| --- | --- | --- | --- |
| `migration_record_reception_front_intent` | Actual receiver STATE; validated origin/front, requester/receiver IDs, positive exact cohort ID and corridor generation, phase requested/prepared/accepted | Caller-declared result0/1; idempotent identity-only receipt and cached qualitative phase; no people/load/capacity/route writes | Real successful offer submit, paid setup success, successful inner acceptance |
| `migration_clear_reception_front_intent` | Actual receiver STATE; exact retiring origin/generation/actors/cohort | Removes only matching intent identity; preserves other intent records and actual services/reception/history | Measured passage, decline/expiry/invalid/control/war cleanup |
| `migration_refresh_reception_front_intent_projection` | Actual receiver STATE and its private identity records | Cached qualitative phase/active flag, no public numeric meter; ignores malformed/stale/unsafe/unrevealed records | Only the above transaction/lifecycle seams and existing exact front callbacks |
| Read-only intent predicate/getter | FROM receiver STATE, ROOT viewer | Authorised qualitative phase or neutral; current owner/control and exact selected identity proof only | Existing migration map role/detail/top or bottom branch |

Do not reuse `migration_presentation_record_preparing_projection`, `migration_evacuation_prepared` or arrival/reception flags for incoming intent.
The preparing projection is an origin outflow phase and has production/speed consequences; incoming intent must not apply those modifiers.
Store no population, amount, capacity, reserve, reception load or physical destination in the new presentation receipt.
Internal identity metadata may include origin STATE, corridor generation, requester COUNTRY, receiving COUNTRY, cohort ID and phase enum; phase is not a fourth public value.
Use `migration_*` identifiers and shared internal enum constants, not an event or third mapmode.

### Why a lone latest-generation slot is insufficient

Acceptance clears the receiving COUNTRY's pending offer mirror while the accepted origin contract can remain live until passage/terminal.
Another origin may then submit a new pending request to that same front before the older accepted passage executes.
Country pending mirrors cannot reconstruct the old accepted front after the new request ends.
A lone overwritten state generation would lose that survivor, and clearing all intent at one terminal would erase another real contract.

Use front-local identity-only receipts for simultaneous live contracts, with every append/update/remove aligned and keyed by exact origin/generation/actors/cohort.
This is presentation metadata, not a parallel population/cohort ledger.
Refresh cached qualitative flags only at validated owner boundaries; never scan those records or global cohort arrays during map hover/color refresh.
Choose deterministic qualifying phase priority and tie-breaking, preserving actual trapped/overcrowded/arrival role priority and showing intent as an authorized secondary context when another real role wins.
Removal of the selected record must recompute from surviving valid local records rather than infer a survivor from country totals or guess a route.
Do not add an arbitrary first-entry/unique-only/capped-record fallback; implementation must verify a complete installed iterator or keep an unfinished/invalid cache neutral and report the limitation.
No new world registry or recurring scan is required.

### Exact publication gates and writer locations

Requested: after a real successful EVAC `humanitarian_corridor_submit_offer`, with complete current country mirror, fresh live-cohort validation and actual front owned/controlled by the known receiving actor.
Require positive generation/cohort/origin IDs, full offer/live-row identity agreement, current preparation-safe food/native route/hazard/actor/relation facts and the existing reveal qualification.
Do not publish from a pressure request, candidate flag, unknown food receipt, unsubmitted preparation, relief-only operation or amount alone.

Prepared: after `migration_prepare_reception_services` returns genuine success1 for the exact pending front/generation and current validated row, while existing service/policy result and full current headroom checks pass.
Refund/rejected/unchanged setup must not advance phase; an older valid prepared/accepted record for another identity must survive.
A policy-only meaningful paid setup is still genuine preparation when its existing receipts and strict full offer gate pass.

Accepted: inside successful inner `humanitarian_corridor_accept_offer` acknowledgment, before host mirror deletion, after its fresh resolver/current front/strict whole amount/actor checks.
Carry requester/receiver explicitly rather than ambient ROOT.
This publishes consent intent only, not route binding, reserve delivery, host load or movement proof.

Passed: clear the matching receiver intent from `humanitarian_corridor_record_evacuation` only after measured full debit, survivors/credit, conservation, cohort and generation receipt validation.
Do not wait for a manual 90-day mission terminal; actual arrival already has authoritative reception projection and must not keep a passage-pending intent.
Ordinary passage's immediate terminal cleanup remains idempotent.

Declined/expired/invalidated: clear matching front intent in existing exact corridor cleanup while origin/front/actors/generation/cohort IDs still exist; retain paid service/capacity receipts, other arrivals and surviving intent identities.
Control/war/annexation callbacks must invalidate the matching projection through their existing exact origin/front context, without inventing an attacker or counterpart.
Read-only map predicates must refuse a stale selected snapshot if current front ownership/control, actor existence, origin contract generation/status/cohort or operation no longer match.
Readers perform only local cached checks and at most an exact selected-origin scope lookup; no real resolver, food observer, country recalculation, registry scan or mutation belongs in hover.

### Privacy, palette and performance

Gate intent color/role/text to the actual front owner/controller viewer; keep public fallback unchanged.
Use an authorized qualitative intent line distinct from actual host/destination and latest arrival/share lines.
Never render a foreign request amount/capacity as part of this intent; no new numeric text is needed.
Reuse preparation/offer palette family for requested/prepared intent and, only if desired for consent, existing corridor palette without calling it a safe/open route.
A narrow legend clarification may explain that this is proposed reception, not arrival, but no art or map-tab family is necessary.
Keep real trapped/overcrowded/reception priority and expose overlapping intent only in authorized detail.
Do not alter famine layers, category reveal counts, timers, weights, service costs, route grants, population, map geometry or CXT grants.

### Required source/native acceptance matrix for implementation

| Case | Required result |
| --- | --- |
| Fresh revealed pending EVAC, exact actors/front/cohort/generation | Owner/controller qualitative request intent; no arrival/host/bind/route/load/capacity proof; public unchanged |
| First tiny unrevealed request | No category or intent visibility promotion solely from projection; real private metadata may remain hidden |
| Successful real paid preparation | Exact phase advances; existing canonical values unchanged |
| Refunded/unchanged setup | No phase advance or duplicate metadata; earlier other-context intent preserved |
| Accepted before physical pass | Agreed pending intent only; no population or host load |
| Measured actual passage | Matching intent clears, real reception/history persists, replay cannot clear another request |
| Decline/expiry/invalid/control change | Matching intent clears without reversing paid services or origin obligations |
| Older accepted plus newer pending at same front | Both identities retained; newest pending terminal cannot erase older accepted; older passage cannot erase newer pending; reproject surviving qualitative context |
| Receiving country simultaneously has independent outgoing contract | Incoming front and outgoing origin remain distinct; clearing either cannot clear other's role/intent/pulse |
| Direction reversed/new requester or new controller | Fresh identities required; stale prior cleanup cannot erase reversed newer context; no borrowed actor authority |
| Zero/negative IDs, misaligned metadata, ambiguous row or missing current proof | Neutral/no new projection; no implicit current-row fallback or repair |
| Old generation callback after a new generation | Exact identity mismatch leaves new receipt/actual ledgers untouched |
| Quiet front with another actual arrival role | Actual reception stays primary; authorized intent is secondary, not a replacement population/destination |
| Foreign/public viewer | No private intent, headcount, capacity or route-authority leak |

These are required plan cases, not executed source implementation or engine tests.

## Fresh MCP result and exact limits

Live exposed schemas for `hoi4.map_inspect`, `hoi4.map_render`, reference routes and source lookup were inspected.
Current map-render layer enum is province/state/strategic-region/terrain/continent/owner/controller/cores/claims/coast, with geographical overlays including supply-nodes/railways/adjacencies.
It has no custom mapmode, color/tooltip execution scenario parameter.
No GUI gate was met and no GUI route/layout work was performed.

One fresh representative lookup used actual installed province406 in state96 Wilejka and strategic region39 Eastern Poland:

```json
{"lookupOnly":true,"includeOverview":false,"stateIds":[96],"provinceIds":[406],"regionIds":[39],"query":"adjacency supply railway","queryLimit":1}
```

Result: `status=ok`, `code=MAP_LOOKUP_COMPLETED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, one province/state/region inspected, no unknown province IDs, overview not rendered, queryMatchCount0.
Map revision/shared revision: `bcccf5a7783c4412afe1e1c4a25b41c4f90cb00ac485beef3e5396ed954d2f67`.
Lookup-only validation passed only its lookup-only check; full map validation was not requested.
The returned source inventory was capped at64 of2065 paths, explicitly `MCP_INLINE_FILES_TRUNCATED`.

Returned artifact, size240256 bytes, SHA-256 `5ff50dbcc4751d44ccac1e864d67b7c176bb3b43a365468f4f3ede5141764c72`:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ff50dbcc4751d44ccac1e864d67b7c176bb3b43a365468f4f3ede5141764c72/1bed48975995d6ced083cecb9ad0279338153900f5ca27295287b6fec0e0a864/map-lookup.bcccf5a7783c4412.984474afeaba046e.json`

Live `list_mcp_resource_templates({server:"hoi4_agent_tools"})` returned the artifact template with byte offset/length and metadata=manifest selectors.
No SDK, local client CLI, new tool script or server repair was used or invented.
One attempted call was the generic `tools.read_mcp_resource({server:"hoi4_agent_tools",uri:artifactUri+"?offset=0&length=12000"})`.
It returned `resources/read failed` / Mcp error `-32603: Artifact provenance manifest is unavailable`.
The parent correctly identified that the generic accessor contract restricts URI to a value returned by `list_mcp_resources`; a dynamic template/artifact link alone does not satisfy that contract.
That attempted accessor therefore is not evidence of a supported artifact read route; it must not be repeated on an unlisted URI.
The decision auditor was explicitly corrected not to repeat it.
Artifact body remains unread, with a contract-valid listed-resource accessor unresolved.

Consequently province/state/region lookup metadata succeeded, but artifact-level adjacency/supply/railway details and complete inventory were not established here.
The free-text query matched zero records and is not proof of a particular route/network connection.
The prior actual narrowed map timeout remains recorded in `current_mapmode_projection_audit_20261003.md`: lookupOnly/query64/queryLimit1 returned timed out awaiting tools/call after600s.
That prior real timeout is distinct from a caller ten-second yield; current lookup succeeded, so no timeout retry was needed or claimed in this audit.
No duplicate broad heavy map/reference batch was issued.
Source matrices are not custom-color, tooltip, route, visual alignment or engine execution evidence.

## Pertinent local reference evidence

Both offline wiki and installed documentation were read for the rules used; no Paradox wiki web access occurred.

| Reference | Exact sections | Revision evidence |
| --- | --- | --- |
| Installed `common/map_modes/documentation.md` | Complete scripted-mapmode scope/layers/buttons/tooltips/targets/daily-update example | SHA-256 `FE0A32E55F8F409DF104C9F386F607767D795193046E1DE509FAC75A46EC6392` |
| Offline `paradox_wiki/Map modding - Hearts of Iron 4 Wiki.md` | State/strategic region 150–169; map supply/railway source listing58 | SHA-256 `0AD59BDFC32A65CDE902D7FBF5D6DE5142656EFAE3529FFAC3CD0BE5F96011D4` |
| Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | State-target icon/FROM/on-map modes 576–610 | SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | ROOT/THIS/PREV/FROM/owner distinctions 260–265 | Direct local source sections read; installed mapmode scope contract is primary |
| Installed `common/decisions/_documentation.md` | Actor/target scope and update cadence 12–55 | Direct local source sections read |
| Installed `common/decisions/AFG.txt` | Actual native state-target/map-and-list precedent 477–489 | Direct local source block read |

State-ledger, subagents and decisions-missions skills were used; the decision guidance was relevant only to inventorying existing native target icons.
No scripted-GUI redesign/implementation gate was met.

## Completion boundary

The genuine receiver-front intent gap is confirmed after accounting for real native action coverage, not inferred from missing source alone.
Current arrival, outcome, terminal-origin, public/authorized and separate famine coverage is documented above with its exact classification limits.
No broad redesign, new asset/color family, unsupported route arrow, inferred integration destination, hidden capacity grant or fourth value is recommended.
The accepted incoming intent plan remains queued, not implemented; source/native validation and custom-map tooltip/color execution remain unresolved.
Parent owns the capacity selector edit and its commit; this worker independently checked that edit but changed no existing file.
No game, log or save was accessed or requested, and no completion claim is made for the full mechanic.
