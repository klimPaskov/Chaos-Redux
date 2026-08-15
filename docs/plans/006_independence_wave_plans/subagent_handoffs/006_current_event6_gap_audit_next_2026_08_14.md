# Event 006 current gap audit: IW-022 CRO-origin route preservation

Date: 2026-08-14.

Disposition: **NO SAFE IW-022 SOURCE PATCH FOUND / EVENT 006 REMAINS HOLD-PARTIAL**.

This read-only audit began from the requested post-`21d769e4f` worktree and closed against current descendant HEAD `0e1b9a57b2ba8c5b306340383cc1fbf516274225`. Concurrent worktree changes were preserved. No gameplay, asset, localisation, workbook, central-admission, or broad authority file was edited by this audit.

## Outcome

IW-022 is not a missing registered-tag compatibility adapter. It is one of the thirteen non-selectable vanilla route overlays.

The accepted registry row at `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:23` resolves IW-022 to `reuse_vanilla_dynamic_country_overlay`, `vanilla_route_overlay_only`, states `103|163`, and `RG-ADRIATIC-TRIESTE-DALMATIA`. Part 1 at `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:240` requires these thirteen rows to remain additive, receive no custom country registration, and never enter the selectable release pool.

The current acceptance checklist separates the two gates:

- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md:99` leaves all thirteen registered-tag compatibility adapters unchecked.
- The overlay gate is checked at line 100.
- Line 102 says IW-022 already has the bounded CRO-origin `dalmatia` adapter, that no exact overlay hook remains absent, and that overlay meaningful-tree, network, league, formable, symbol, save/load, and live-runtime evidence is intentionally not counted toward either unchecked gate.

Therefore an IW-022 gameplay patch cannot truthfully advance the registered-tag gate. Adding central dispatch, content attestation, Join order, package identity, flag or portrait ownership, network or League membership, a formable route, or a focus-tree replacement would contradict the accepted non-selectable overlay contract.

## Current IW-022 route-preservation receipt

### Vanilla creator route

Installed vanilla `common/national_focus/yugoslavia.txt:711-880` remains the authoritative creator surface. `YUG_devolved_croatia` creates a dynamic country with `original_tag = CRO` at lines 818-819, applies `set_cosmetic_tag = dalmatia` at line 821, transfers state 103 at line 822, and creates the vanilla Dalmatian division at line 850.

The Event 006 adapter observes that result after creation. It does not reproduce or override the vanilla creator block.

### Exact identity and additive lifecycle

| Surface | Current result | Source evidence |
| --- | --- | --- |
| Exact carrier identity | PASS, static | `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt:12-18` requires `exists = yes`, `is_dynamic_country = yes`, `original_tag = CRO`, and `has_cosmetic_tag = dalmatia`, while rejecting the package-owned permanent-loss flag. |
| Narrow carrier discovery | PASS, static | `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt:10-59` defines exactly `on_daily_D01` through `on_daily_D50`; there is no global daily, weekly, monthly, or on-game-start country iteration. |
| Additive initialization | PASS, static | `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt:252-273` initializes only overlay flags, three package values, anchor/profile variables, and the package idea lifecycle after the exact route exists. |
| Suspension and permanent route loss | PASS, static | The same effects file at lines 275-332 suspends and resumes package-owned state, and lines 186-201 remove the mission and overlay ideas, clear package-owned flags, reset hold progress, and make permanent identity loss terminal for this overlay. |
| Decisions and mission | PASS, source; AI evidence partial | `common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt` contains five decisions plus one activated mission, with six `ai_will_do` blocks. Five decisions spend command power, manpower, trains, infantry equipment, support equipment, or army experience through package effects. |
| Idea lifecycle | PASS, current source | `common/ideas/006_independence_wave_iw022_dalmatia_ideas.txt` contains four mutually refreshed lifecycle forms. A concurrent uncommitted repair mirrors static-field modifiers through file-scoped constants; this audit did not author, revert, or claim ownership of that change. |
| State mutation and identity mutation | PASS, absent | A scoped search across the seven IW-022 gameplay files found no `load_focus_tree`, `set_state_owner`, `transfer_state`, `set_cosmetic_tag`, `release`, `create_country`, `annex_country`, central package attestation, network membership, or League admission writer. |
| Event 006 focus attachment | Intentionally absent | No `independence_wave_iw022` reference exists in `common/national_focus/`. This preserves the currently selected carrier tree. It does not prove that a new shared-tree import would be safe. |
| Central admission | Intentionally absent | IW-022 remains non-selectable and outside the release planner, central attestation, SCN-008 selection, and deterministic Join surfaces. |
| New identity, rights, portraits, flags, or audio | Not authorized and not needed for this receipt | The adapter retains the vanilla dynamic carrier and shared icons. No identity or rights evidence was invented. |

Current scoped source counts are 144 constant lines, 112 trigger lines, 388 effect lines, 73 idea lines, 11 category lines, 174 decision/mission lines, and 61 on-action lines. The decision source exposes six weighted blocks. The hook table exposes fifty carrier-specific daily hooks.

The key source hashes observed in the final audit window were:

- trigger file: `DD59DE07FC68246F7CB8F211113B4E3A83B76642DF920184A4401495DFD35BA1`
- effect file: `5A805DC536D7531C42C5ED6A7113AF13A28D87351A0AAAD14F745865B31B9E93`
- decision file: `B7990702503CCB2C671D3C1763855DC3660D45292A23AB798DCB80F21E4B4AD6`

The source-only receipt supports the narrow conclusion that the current IW-022 adapter observes and preserves the vanilla CRO-origin `dalmatia` creation route. It does not prove a meaningful child focus tree, package admission, network membership, League play, a formable, or whole-event completion.

## Focus MCP evidence

Mandatory focus inspection against merged vanilla `game:common/national_focus/yugoslavia.txt` succeeded at revision `80b70f0b20c2ae2918809fc8a8d84ab466c6af5ab98c8fad72bd456fc9c13e8c`.

- `hoi4.focus_inspect`: `FOCUS_INSPECTED`, one `yugoslavian_focus` tree, 118 focuses, 164 connectors, and the source location for `YUG_devolved_croatia`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb2750a68d7d6e926f3083b501873e0554e630f7a21a8832c3c1093908e50d09/055f4ec86e69936e78768b0a8cc6ebede8cec7e54f9f6367384860bf63f204d5/focus-inspect.80b70f0b20c2ae29.json`.
- `hoi4.focus_render`: `FOCUS_RENDERED`, layout hash `ef27dc4be4d8456b27a2105d5cb6bb0f3a98d27022f1f19d625f247fb1c411ad`; authoritative JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a292997c63099855139dfadef1b3ad15bcd86fbab9f394796ec1c7af77b4cf88/2ee73cd140bdb21be6b56fcea79adfc5aecb2cf73a7f5c311dbabd41cb3531a7/yugoslavian_focus.focus.json`.

The MCP focus diagnostics are dominated by vanilla icon-resolution and legacy layout findings, including the `YUG_devolved_croatia` icon lookup. They do not identify an IW-022 Event 006 source defect, because Event 006 does not own or override this vanilla tree.

## Event MCP evidence

All twelve current Event 006 event files received file-scoped `hoi4.event_inspect` and `hoi4.event_render` calls. Every inspection returned `EVENT_INSPECTED_PARTIAL`; every render returned `EVENT_RENDERED_PARTIAL`. They share current event graph revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`, and zero blocking diagnostics.

The shared graph counts are 9,499 events, 14,688 options, 1,060 entries, 8,266 unresolved nodes, 7,641 terminals, 37,070 edges, 28,177 state accesses, and 2,127 non-blocking issues. The partial result means the file-scoped view is bounded within the large merged game/mod graph; it is not a whole-event completion receipt.

| Event file | Selected render nodes | Inspect artifact | Render manifest |
| --- | ---: | --- | --- |
| `006_independence_wave.txt` | 73 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf858339007c67cfc3a5e3bddb06f6d3037286d562c80d7d71a48d313e63f446/8fae3f58b96e7d854059003fc5ac280d2a55f5c6702918368ae548acad5806ad/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca341c1964c4cba1b4ac1dcdeae11ee950bec0b1f9b08dc7ce96e64b7a4308fa/e4e4386b6d9f76ba6e6d5ae3838ba8bc4aaa99639a42eb1e5b86bb59e9bc823f/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_join.txt` | 13 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4cb837a7ec9ff73fe001bf92434c74059159dcd33bfe83a228d1f668b04b535/0aea8b80cda48ebeae9296f8bf34b5a2c6ab712e393cb266cbb11ee95aaf1abe/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3be574b2a816588ff8ca2969cd21445090ee60a854c011512354296db98cb49/31bfd09f64d5b98fc1249c2f9c9f2c574230df191e957c72b8f96f731df49aee/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_scenario.txt` | 10 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51760bb325a7b7a124ede63f1b474bcde8af0cde7aff6f6c1eeed5e03c2531c5/9a252eeff56191b7505b027bb0538a6c7fdd109df1af8a0ca9bb9a90d563eb12/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba16c8165cfeed9031254543e3b84c8008f11df5c9e51785fe4c7bf0e2986056/e1b20d7af026eaf4f12ae7fc551402b5f5342db4f68de704931c97b63bd2d9f6/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_rhineland_bavaria.txt` | 36 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85cc3af6e8f11b50052f314bb9e102ace44534039eacaf0f7a4ac2f151f5e9ab/e3ab3d67bf5c1bd20926bea54ae834eb659b22fee0977c51ddffb5f4f28b4360/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcb09e07396296c59c6da11b428d2e608a11325e7616b69666f10bb300498e63/35acf8db0b855ea6b2228189faa9e2313b1e4cde34e51e8abbc5ac58d7f12187/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_wallonia_frisia.txt` | 15 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a0c538c2f4cafe9d01b3b05bdfc31fe971de70bed3533c216cb00de12c3d4bd/f36f99e07005e76f60dd2ebb9a4a02f22d24a410f0e49c3065602460e5d0e18c/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e25e505dbe8da48f7ccd546e5caaf046fdb6d4acbe498831b209fc6ef9280702/7a62196ebd0cab849e33f090346922d69f1636fd9f73591f4fda28dc13f95350/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_mediterranean.txt` | 50 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11a7a861178aa19eb156944fec139b5db4920c0092c5973c46d568152cfa1fc3/75f83aca781bbfeff3bc035598779affec86190ab8c9fe66c704d7a2fc715f4d/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b233f3827619d31ad0b5f40637a9a23a26a043a899b2c1b3fb1f065da93ce70/f23bb8ec5e6d0c01b1062af4f0c5ef805b8a917e96257e00c306651476538a6e/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_form01_02_04.txt` | 39 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad08eee6a57a2516725d8f58ca6d235cf22d2cc8a94a5762d1ce8f8e94d919fc/b67a32db372261a9e9126dc2824a0f1218b85400396534515881caddbdfa5b86/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d5cabd1b309a30f1802dacd698683e21aceef731aff05a54627c7200d31f3c4/4f9db8e3316daca64c1f81d412ea952f0bd95c7b5f763e9dc8ba5425e42225a8/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_form05.txt` | 27 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a23c95363dd572bb448869a29fa2002e968f679cde0a08649b51f4df7b10cb13/ee5f0ffa415bc182aa0330b2370359b490d039959243d2bf5d9b6390370adf55/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44ed1c4fb75188ddf315ecac91c852b2f30dfb766ec1160a48431bbd7f5b7b2a/a1999d686e477802aa716a95042a30383529cf0186a0a316cd6d2b91309263b9/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_form16_events.txt` | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/826829ab41f9d4ef2789096519a2c142a4233ad43e3075c6eb49f4ff1bbb0d93/64f42660b52d94e44f4e20dd3a32b94b03249ac665dcf65950c99b001ff54bb7/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8938fa2fe67f9a96aa2d3a03863cc38ca21f072fe80155c1438473964de894c9/d29905b46c49f85887de34fdf5ecc0135481ed2a7195f0c60fe89217dbde6435/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_iw043_iw058.txt` | 205 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c30b797a87e3dc614cf4d206cfc63d2adc2894a2f63d158d8793774add164a8/00528dcd67c72b3076e399ee56c15b28ed002838a705b1e0fe61fd7e8a5222b3/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb39910008a4f5731b6a10edc082c68a5653fcba59096c5282bb8d7f6f9449e6/a5e2bafdf53acec174d4d10c190966832e476980bbb25e3f7c741a0965cb915f/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_iw093_iw098.txt` | 40 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9e41074824d006dc88e9e2d4901336a16e7de9bc32f9774e6bd0111ab903b18/de39f15c4e6ce393c5dff092455fa40ff526db741ea816a468c4e632441a20a4/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ba640f938e36d9f912bfd39dd8968eb07cca79c04c3ebecf2ba762ae2826ac7/aacf413257f3530c902043f429867f30e94e08b15334637c6ab876966a90e8a4/event-overview-741883f50501-manifest.json` |
| `006_independence_wave_evolution_incidents.txt` | 25 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b801772ed2623c3373731e65bd4039c85a63c9383c2328c7a2b4fbc2932378b3/090fd187e7a866d1dc461a7cbad700f8829f4345510761547748ee9bad05efd3/event-scan-741883f50501.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec97bf4a10c9f0d5e3b2b42e2c41d3ddccfe0f710d45557c59d88fb75f7f5a09/f7f6934512d5b1ae5cb21e81819edfbb56a6d8954faf3fe54d62bab8de166791/event-overview-741883f50501-manifest.json` |

The requested event comparison from pre-change revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2` to current revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b` returned `EVENT_REVISION_NOT_CACHED`, status `error`, with zero artifacts. The MCP blocker states that the requested event graph revision is not cached. No before-and-after event claim is made.

## Weighted-surface evidence

The IW-022 decision file has six `ai_will_do` blocks: five decision candidates and the watch mission. This pass correctly routed a current probability audit to `chaosx_ai_probability_auditor`, but the nested audit was interrupted by the parent before it returned evidence. Current probability status is therefore **PENDING / BLOCKED BY INTERRUPTED AUDIT**, not pass.

The 2026-08-03 audit remains historical source evidence that the adapter discovered five decision candidates and one mission candidate with incomplete pools. It is not promoted here as a fresh quantitative balance receipt. No weight, target, or balance change was proposed, so there is no owner patch and no same-scenario `hoi4.probability_compare` cycle.

## Current whole-event counts and accepted-plan disposition

The current allocator audit passed with:

- 149 publishers
- 126 automatic or high-chaos selectable packages
- 138 SCN-008 ranked selectable packages
- 40 runtime adapters
- 32 content-attested packages across 29 compatible reservation groups
- eight adapter-only fail-closed IDs: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179
- automatic ladder `3/4/5/7/10`, including 10 at World Collapse

The current authority remains 161 unattested selectable rows out of 193 non-overlay rows. The country API audit passed with 242 broad unique tags, 191 resolved unique carriers, 34 Soviet carriers, 45 Africa carriers, zero missing, and zero duplicates. The SCN-008 static matrix passed all 32 mode/intensity cells and its eight recorded edge cases.

No accepted plan was promoted, rejected, or widened by this audit. The IW-022 adapter handoff remains `PARTIAL`, the IW-022 current route contract remains non-selectable, and the whole event remains `HOLD / PARTIAL`.

## Documentation and acceptance inconsistency

`docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:164` still says the thirteen overlay hooks remain implementation blockers and refers to seven other absent hooks. That wording is stale against the later/current acceptance checklist at lines 100-102, which says every exact overlay hook is implemented and none remains absent.

This audit does not edit broad authority documents. A documentation owner should reconcile that sentence without converting IW-022 into a registered-tag row or closing the registered-tag checkbox.

## Strongest next evidence gate

Do not patch IW-022.

The next tranche that can actually advance the unchecked registered-tag gate is a current read-only preservation audit of the newly present, dormant IW-153 POK compatibility boundary, without enabling the package or selecting a community identity.

Exact Event 006 files:

- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw153_pok_compatibility_adapter_2026_08_14.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw153_pok_compatibility_audit_2026_08_12.md`, which predates the new adapter and must be treated as baseline evidence only

Exact vanilla preservation surfaces:

- `history/countries/POK - Pontianak.txt`
- `common/characters/POK.txt`
- `history/countries/INS - Indonesia.txt` for `INS_releasables`
- `common/scripted_effects/INS_scripted_effects.txt` for `indonesia_transfer_POK`
- the POK core-state history and current installed state binding for state 334

The audit must verify that the new wrappers preserve POK history, characters, cores, Indonesian releasable membership, and the untouched `indonesia_transfer_POK` behavior while remaining `specific_community_variant_only`, unbound, and absent from central admission. It must not invent the named community, flag, portrait, leader, territory binding, or rights evidence. If the static preservation contract passes, the result may advance adapter evidence only; it cannot admit IW-153.

## Final blockers and no-completion statement

- No safe current IW-022 source defect was found.
- IW-022 cannot close the registered-tag compatibility gate because it is an overlay-only row explicitly excluded from that gate.
- Fresh IW-022 probability evidence did not complete because the routed auditor was interrupted.
- The event comparison baseline is unavailable in the MCP cache.
- The stale overlay-blocker wording remains for a documentation owner.
- IW-153 is the strongest next gate, but its new adapter still needs a current post-implementation preservation audit and must remain unbound and fail-closed.

This handoff is a bounded route-preservation audit, not an Event 006 completion claim, not an IW-022 package admission, and not acceptance of any new identity, rights, portrait, flag, audio, formable, network, League, or central-selection surface.
