# Event 032 native raid parity audit, 2026-10-03

Disposition: source-contract audit delivered, native adapter acceptance blocked, MCP verification incomplete because explicit-workspace calls remain outstanding.
Role: `chaosx_scripted_system_architect`.
Parent owns integration and every gameplay patch.
User authority: the bounded read-only audit request and full Event 032 specification authorization, with the latest instruction retaining the original boundaries.
Only this handoff is written.
No gameplay, weighted logic, localisation, assets, workbook, skills, index, or Git history is changed.

## Finding

The installed documented native raid API cannot prove Event 032's exact launch-state contract for its supported multi-site operations.
This is a concrete API parity failure, independently of the missing Event 032 raid definition.
The installed raid documentation lists only `actor_country`, `victim_country`, `target_state`, and `target_province` as RaidInstance dynamic pointers.
Its `starting_point` selects source kinds and building types, and `launchable_from` evaluates the source controller country.
Neither supplies a documented source state/province pointer, a per-state source predicate, or the list of participating source states.
Installed effects, triggers, dynamic-variable documentation and vanilla raid precedents did not reveal an additional source accessor.

Consequently the native route cannot authenticate that the actual source is `missiles_operation_launch_site`, exclude another rocket site controlled by the same country, or prove the several site allocations used by saturation.
Checking that the actor has a valid selected site only proves a valid site exists.
Saving that selected site from a country variable at resolution records the scripted selection, not the engine's actual source.
Treating the source controller country as the launch state loses the identity required by part 8 lines 402 and 408.
Deleting other rocket sites, disabling multi-site behavior, substituting a source singleton, or claiming an undocumented `FROM`/`PREV` pointer would change the accepted design or invent capability.

Part 8 lines 411-433 and part 2 lines 466-493 explicitly support the complete scripted adapter when native parity fails.
This finding supplies a documented reason for that choice.
It does not prove that the current scripted implementation satisfies every operation requirement or that any campaign behavior has been tested.
No native raid implementation is recommended under the currently documented API.

## Parity matrix

| Acceptance requirement | Attainable native capability | Remaining constraint |
| --- | --- | --- |
| Exact launch state | Native rocket-site source kind exists | No documented exact source-state/province accessor or per-state restriction, including in outcomes. Multi-site custody and capacity cannot be authenticated. This is the decisive parity failure. |
| Exact target state | `var:target_state` and applicable `var:target_province`, target type and gates | Achievable wiring through regular event targets, with current controller revalidation. Intended native target must remain distinct from scripted drift impact. |
| Exact reserve receipt | Event 032 can reserve its logical variables through its existing operation API | Native `essential_equipment` consumes equipment/nukes, not the logical reserve variable. No documented creation, commitment, or cancellation effect hook binds that existing receipt to one native instance. |
| Exact payload receipt | Fixed raid types can declare payload equipment or `nukes`, with `nuke_type` | Collected at creation/preparation. Bridge must reconstruct the exact paid lot without testing the post-collection stockpile as if it were unpaid. Existing scripted payload debit must not run again. Dynamic per-operation native cost and a native payment receipt accessor are unproven. |
| Exact outcome | Four exact native branches: failure, limited_success, success, critical_success | Event 032 has ten guidance results and bounded drift/self/site impacts. A second guidance draw changes the combined model. Four callbacks alone do not establish equivalence to those results. |
| Actor and victim | Explicit RaidInstance actor/victim pointers | Supported through an immediate actor country event. Entering actor scope inside the callback does not change callback ROOT. |
| Cleanup | Chain-local regular targets auto-expire and receiving event can settle script records | No documented cancellation callback, instance ID, source pointer, or connection to abandoned preparation. Source capture, cancellation, stale callbacks and instance reuse remain unproven. |
| AI route | Native `ai_will_do`, target bindings, minimum success gate and success factors exist | Native AI can select a target, but documented selection does not freeze the exact Event 032 operation/site receipt. Exposed probability schema has no named native-raid adapter. Numeric parity and runtime selection remain unresolved. |

## Authoritative engine and vanilla evidence

Use the exact file revisions in the inventory below.

- Installed `common\\raids\\_documentation.md` lines 90-126 define visibility, preparation, launch and `launchable_from`.
  Lines 119-126 explicitly make the latter a country controlling the source, including fleet ownership.
  Lines 138-143 define starting-point kinds, building types and faction-building permission.
  Lines 548-557 enumerate the four RaidInstance dynamic pointers.
- The same document lines 167-186 state that essential equipment is a creation precondition and is collected after creation.
  Additional equipment is also collected after creation.
  Essential and additional entries use their maximum rather than additive quantities.
  Nuke type is explicit.
  Lines 31 and 147-148 describe Command Power allocation.
- Lines 237-301 put both actor and victim effects in RaidInstance scope.
  The split controls outcome UI, not execution scope.
  Lines 241 and 300-301 define four outcome levels and explain that failure, critical failure and disaster refer to the same worst branch.
- Lines 66-80 describe native AI and target bindings.
  Lines 411-461 permit custom success modifiers using MTTH formulas, but their documented scopes are country, target state, character and unit.
  The documented limitation on sampling several sources prevents assuming a custom success modifier can inspect an unavailable source-site scope.
- Installed `documentation\\effects_documentation.md` lines 450-454 and 5216-5271 list RaidInstance experience/damage/history operations.
  Lines 5273-5286 describe a state effect with RaidInstance ROOT, not a source-site accessor.
  Installed `documentation\\triggers_documentation.md` lines 519-522 list hidden and meta trigger support for RaidInstance.
  Supported target labels for unrelated effects do not establish the meaning of an undocumented raid source pointer.
- Vanilla `common\\raids\\nuclear_raids.txt` lines 246-416 implement `nuclear_missile_strike`.
  It uses the Gotterdammerung gate at 285-287, province targeting at 307-309, assigned `nuclear_missile_equipment` at 312-317, one nuke at 318-320, rocket-site source kind at 322-326, native AI at 251-281 and four outcomes at 356-415.
  Lines 386-389 and 408-410 call `launch_nuke` with the exact target province and `use_nuke = no`.
  They do not debit the nuke again.
- Vanilla `thermonuclear_missile_strike` at 845-932 uses the same source kind and explicitly sets `nuke_type = thermonuclear_bomb` at 922.
  These precedents require existing engine missile units/equipment.
  They are not evidence that Event 032's logical reserve has become native equipment or that an equipment-free native missile raid works.
- Installed `launch_nuke` documentation at 4745-4760 supports state/province, controller selection, use_nuke and nuke_type.
  It contains no launch-site field.
  The documentation's `provinve` spelling is a documentation typo, while vanilla uses `province`.
- Offline `Data structures` lines 263-316 establish regular/global event-target lifetime.
  Offline `Scopes` lines 250-266 and `Event modding` lines 24-32 establish event country ROOT and regular-target carryover.
  Installed save/has/clear target sections are listed below.
  No Paradox website was used.

Additional negative-evidence search covered installed markdown documentation, installed vanilla `common\\raids` text, and installed `common\\on_actions`.
Search terms included `source_state`, `source_province`, `launch_state`, `launch_province`, `starting_state`, `starting_province`, `raid_source`, `create_raid`, `cancel_raid`, `launch_raid`, and `on_raid`.
No matching source accessor or script creation/cancellation route was found.
This is bounded evidence for the installed documented scripting surface, not a claim about undocumented engine internals.

## Chaos Redux precedents and current integration

`common\\raids\\cbrn_chemical_air_raids.txt` lines 711-773 implement `chemical_sarin_rocket_strike`.
Lines 755-759 use exact-state targeting, guided/ballistic engine missile requirements, native nerve payload collection and a rocket-site starting kind.
Each of the four outcome branches at 768-771 saves actor, target state, victim, agent, route, outcome and payload-tier regular targets, then fires `cbrn_chemical_air_bridge.1` immediately from the actor country.

`events\\cbrn_chemical_air_bridge_events.txt` lines 45-95 check all pointers, actor identity, victim existence, current target controller, war, and exact-one marker families.
Transient inputs are reconstructed in the actor event before calling the shared consequence resolver.
The bridge explicitly makes no extra payment or refund.
This proves a reusable source pattern for country ROOT and exact payload/outcome dispatch.
It does not prove exact launch-site binding.

`common\\raids\\cbrn_chemical_land_raids.txt` lines 150-160 and `events\\cbrn_land_raid_bridge_events.txt` lines 113-124 use the same chain-local bridge pattern.
`common\\raids\\cbrn_doomsday_raids.txt` lines 1-12 and 76-80 describe paid native lots.
`events\\cbrn_doomsday_raid_bridge.txt` lines 1-53 demonstrate the immediate actor-root gateway.
Doomsday gameplay is a precedent only and remains excluded from Event 032.

Current Event 032 already freezes actor, intended country/state, launch-site ID, guidance/readiness/control snapshots and lineage in `missiles_create_operation_receipt` at operations-effects lines 2140-2167.
It marks participating site allocations at 2169-2177, reserves resources at 2180-2213, and runs preflight at 2215-2252.
The actual logical debit and refund are `missiles_reserve_for_operation` and `missiles_refund_operation_reserve` in `032_missiles_effects.txt` lines 552-581.
The operation trigger contract at operations-triggers lines 9-92 validates the selected target, target state, controlled site, active receipt and commitment.

Current `missiles_resolve_operation` at operations-effects lines 4439-4475 consumes special payload, selects guidance and impact, resolves interception, applies consequences, records incident/achievement receipts, queues warnings and cleans up.
It cannot be called unchanged by a paid native outcome.
`missiles_commit_operation` at 4477-4493 resolves synchronously.
Keeping that call and adding native callbacks would execute resolution twice.
Cleanup at 4506-4578 clears only site allocations matching the active operation ID and clears operation pointers, arrays and flags.
It is scripted receipt cleanup, not native instance cancellation.

Chemical/biological payload debit and dispatch are at 2856-3049.
Nuclear and thermonuclear consumption uses `add_nuclear_bombs` at 2950-2959, followed by `launch_nuke` with `use_nuke = no` at 3051-3091.
Native payload receipt adoption would have to bypass the scripted debit while retaining the owner resolver and release proof.
A capability gate that rereads stockpile after native payment can falsely reject the final paid payload.
Thermonuclear-specific native collection is documented, while equivalence of the current shared `num_of_nukes`/`add_nuclear_bombs` scripted debit to the native thermonuclear stockpile is not established by this audit.

Parent changes were re-read after the resume.
`chaosx.nr32.1` remains the entry.
Immediate country receivers `.5` and `.6` at event lines 21-49 bind global-recipient and scenario setup to country ROOT.
They introduce no raid callback.
The first report retains the Event 16 owner helper call.
Event 23 arsenal ownership and Event 76 testing ownership stay outside the audit's write scope.

No Event 032 definition or outcome bridge was found under `common\\raids` and `events`.
The earlier missing-consumer claim is an implementation fact.
It is not the reason for this native parity verdict.
Current `asset_audit.md` lines 106-111 already distinguishes this fact from the pending parity review.

## Minimal integration map if the API becomes sufficient

These are conditional parent touchpoints, not an implementation request or scaffold.
Do not create helper definitions without working call sites, and do not register an acceptance-blocked native route.

| Proposed or reused helper | Scope and ROOT | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| Reuse `missiles_preflight_operation` and `missiles_create_operation_receipt` | Actor country, actor ROOT | Selected actor/target/sites, profile, payload, lineage | Frozen operation and exact logical reserve receipt | Existing operation entry path, after a verifiable native source-binding contract exists |
| Proposed `missiles_native_callback_context_is_valid` | Actor country event, actor ROOT | Chain actor/victim/state markers, fixed type/outcome/payload, verifiable operation identity and actual launch source | Boolean only, fail closed, no default actor/site fallback | Immediate hidden actor receiver invoked by every native outcome |
| Proposed `missiles_adopt_native_payload_receipt` | Actor country event, actor ROOT | Fixed paid lot/type/outcome and authenticated native receipt | Existing payload consumed amount and proof, no equipment/nuke debit or refund | Authenticated callback receiver before payload dispatch |
| Proposed `missiles_resolve_native_outcome` | Actor country event, actor ROOT | Accepted native outcome and complete frozen operation | One consequence transaction, incident and achievement evidence, warning and cleanup | Immediate receiver, replacing synchronous scripted resolution for that exact operation |
| Reuse `missiles_dispatch_special_payload` and `missiles_cleanup_operation` | Actor country, actor ROOT | Proven paid payload and actual impact, authenticated operation ID | Owner consequences and bounded exact-ID cleanup | Native resolver only after all missing contracts are supplied |

Minimum source surfaces would be `common\\raids\\032_missiles_raids.txt`, the current operation effects and triggers plus matching markdown docs, an unused documented hidden Event 032 receiver ID in `events\\032_missile_crisis.txt`, existing constants, and event-owned localisation/GFX/documentation for real native consumers.
The ordinary decision category remains singular.
Any direct decision call-site change requires its owning skill and parent review.
No central MCP router, wrapper skill, custom equipment economy, GUI, models, terminal branch, or periodic scanner is needed or authorized.

No constants were added.
Reuse existing operation/payload/guidance/result enums and tuning.
Conditional helpers must default to rejected with no payment, dispatch or fallback scope when any native source, receipt, type or outcome input is absent or ambiguous.
A future native type would need explicit tables for preparation, cooldown, CP allocation, fixed native payload quantity and outcome mapping.
Native literal fields need verified parser support before using script constants.
Where only file-local numeric aliases work, document the alias and its authoritative shared tuning entry.
Do not introduce tuning targets during this audit.

Use regular event targets for actor/victim/target and disjoint exact-one payload/type/outcome markers inside the actual callback chain.
Do not carry temporary variables across the country event.
Do not substitute a country/global pending scalar for native instance identity.
No persistent global target is needed for immediate dispatch.
A future native preparation, commitment, cancellation and source-loss contract must clear only the matching operation receipt and must never promise equipment recovery without engine evidence.

Migration requires one authoritative adapter per operation.
Preserve the full scripted route until every native parity gate is proven.
If a supported native route is later introduced, separate payment from resolution, preserve exact paid payload lots, suppress the scripted guidance draw when adopting a native outcome, avoid duplicate incident/death/condemnation records, and run matched named scenario comparisons through the read-only probability auditor.
The native four-level outcome mapping cannot silently replace ten guidance results.
Source-only architecture cannot determine the correct probability mapping.

## MCP evidence and limitations

Workspace ID on resumed calls: `mod_chaos_redux_ea3b2d67c2c0`.
Parent reported fresh trace identifier `trace9632ca4524de`.
That identifier was supplied by the parent and is not claimed as an artifact inspected by this subagent.

Before the resume, workspace discovery prevented useful live evidence.
The required probability auditor was spawned with no inherited context, read-only instructions and no report-file permission.
Agent `01a10017-d9e3-77d0-b9c0-6364f8bebc4a` returned the exact error `workspace routing discovery timed out`.
After resume, a second context-free probability auditor, `01a1003a-bd67-74b3-b18f-798010f0ef9b`, was given the explicit workspace ID and the same bounded no-write scope.
It returned a completed inline handoff stating that its initial explicit-workspace `hoi4.probability_inspect` on `common/raids/cbrn_chemical_air_raids.txt` remained pending when interrupted.
It received no error, artifact URI, revision, coverage report or scenario hash.
It confirmed that no dedicated native-raid adapter appears in the advertised choices, while recognition through generic source inspection remains unresolved.
It made no evaluate, sweep, compare, simulation, sequence or render claim and wrote no files.
Its observations of the sarin rocket raid's declared score and success-factor fields are source observations only.

Live metadata exposes reference_context/search/read, source_lookup, event inspect/render/compare and probability inspection.
The connected source_lookup schema available to this session does not expose the newer `view`, `keyPath`, occurrence or child-offset arguments.
No `hoi4.script_validate` tool is exposed in this session.
No native raid-specific inspect or named probability adapter is present in the exposed schema, but generic source recognition remains unresolved.
Do not pass a decision adapter as a substitute for native raid AI.

Initial event selector attempts used `id`.
Live validation rejected that key and required `eventId` for an event selector and `namespace` for a namespace selector.
Corrected event inspect, scope render and namespace compare were attempted with those fields and the explicit workspace.
The comparison has no immutable before snapshot supplied by this audit and no source edits.
It cannot establish a before/after implementation delta even if the route returns a cached graph.

Reference context, targeted raid search, vanilla nuclear source lookup and native-raid probability inspection were attempted with the explicit workspace.
At this write they have not returned a completed result.
When resuming the grouped explicit-workspace evidence call, the client returned `cell 1 belongs to a stale code-mode host generation`.
That is a client continuation failure and must not be described as a confirmed HOI4 server outage.
A fresh-host explicit-workspace `reference_search` for `launchable_from` was also attempted, without a completed result at handoff.
Reference_read cannot be issued against a fabricated document ID or revision.
Local documentation was read directly and hashed while awaiting revision-bound citations.
This is documentary evidence, not MCP or runtime proof.
No artifact URI, source revision, analysis completeness, helper coverage or normalized probability is claimed from an unfinished call.

## Meaningful validation and skipped validation

Completed source checks compared all eight native acceptance requirements to installed raid fields, vanilla nuclear/thermonuclear rocket-site precedents, current CBRN bridges and current Event 032 payment/resolution/cleanup.
The counterexample is a country controlling several rocket states with one frozen selected site.
The exposed native controller gate and target pointers cannot distinguish which source state actually launched.
Additional checks identified double payload debit and duplicate guidance/resolution risks from calling the existing resolver unchanged.

Runtime behavior remains unverified for preparation visibility after gate closure, repeated instances, cancellation/refunds, source control change in flight, DLC availability, native equipment/model selection, exact stockpile type behavior and AI selection.
No game process or autonomous desktop test was launched.
No numeric probability/balance verdict is supplied.
No source or design simplification was implemented.
The only output is this report, and the parent owns acceptance, source reconciliation and final Event 032 completion claims.
No Git commit was created because this is the bounded audit handoff and parent-owned gameplay integration remains outside this write scope.
Skills used: `chaos-redux-native-raids`, `chaos-redux-events`, and `chaos-redux-subagents`.
No skill was created or updated.

## Source revision inventory

Paths are exact Windows paths.
Line spans refer to the inspected snapshot.
SHA-256 hashes are whole-file byte revisions captured during the audit.
The shared tree is dirty and the parent is actively editing, so later source hashes may differ.
Documentation hashes must not be treated as runtime build/version proof.

| Source path | Relevant line spans or search coverage | SHA-256 |
| --- | --- | --- |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\AGENTS.md` | all | `38e479cb75828ba888860be8bc3739f9286c0d925cc7d8de5ecd3b8dadec46cf` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-native-raids\SKILL.md` | 1-47 | `a573e7f44cdeeb95e8d9cbb6c7771752a75cfa13d08213689717a8e3f0be6a16` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md` | all | `11e4d05c369cb3c3ba93fab268f857834f4928a25b6df820c25ab3f688c6762b` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-subagents\SKILL.md` | all | `6e95d9a832afee35208f7058b742e6d4e7745b949e474c23fff9b7f6bbffca63` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\_documentation.md` | 66-80,90-186,237-301,411-461,544-557 | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\nuclear_raids.txt` | 246-416,845-932 | `966408c81eba9f5928ed352d5f95f6648977b23a8e12ce9aa2cd2cdbca76256f` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 450-454,1948-1956,4745-4760,5216-5284,6496-6512 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 519-522,3844-3851 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md` | 1-1384 token search | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-316 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 250-266 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\raids\cbrn_chemical_air_raids.txt` | 711-773 | `9aafc578ec8b7d53809cd86bfbee6d476f30478eefee579b82fb9c32e4667b09` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\raids\cbrn_chemical_land_raids.txt` | 1-30,87-160 | `334d20a74fdde5c96129d8383805726cc49ad335d4a0af1e1447588fc182caa0` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\raids\cbrn_doomsday_raids.txt` | 1-12,48-112 | `15bfcfb5315c46741bbe9a921280c74f67f5497e8563eb4f3166787430e188e1` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\events\cbrn_chemical_air_bridge_events.txt` | 1-98 | `f4a24615f6ad4651ec081e21dfb5539607a4ec4b8b71b81cfd508738ddb27427` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\events\cbrn_land_raid_bridge_events.txt` | 84-127 | `1c57c0e7674194b76bf9acb2034cd99ae925b9a22000d7ab35b286a93d6f6fc7` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\events\cbrn_doomsday_raid_bridge.txt` | 1-53 | `76f4a4e29a442288f7b22ff52365c010f161a9d71801e25e3cdee3a992d6981a` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\032_missiles_operations_effects.txt` | 2140-2298,2856-3107,4439-4578 | `a6b34365268cecb810ed035249d50a944e2fc7013608576cfa3413ba7d2b27af` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\032_missiles_effects.txt` | 552-581 | `a994309e775df1c6b82d7575b3a5c5731679f5c5846592426e3a6b1cadf96148` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\032_missiles_operations_triggers.txt` | 9-101,155-228 | `f39334f373e66876333999c1460c67bf29cb5d630c255f4d080512111a0f6098` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\events\032_missile_crisis.txt` | 1-80 | `50f45d5e42cfd6b3172542d25638cd270ba8df249523e49fe50383c6c7bb2602` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\032_missiles_specs\032_missiles_spec_part_8_implementation_contract.md` | 385-433 | `df0870503eabd9b6094b249e62f61fc9790302e699b2ff4eaa1a9716db217ffa` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\032_missiles_specs\032_missiles_spec_part_2_program_and_launch_sites.md` | 466-500 | `ead30740f2eb146ccd3768abc02e9be7bf8b5472a0ec059911b556582ce6562f` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\events\032_missiles\overview.md` | 15,59 | `a5b015eb7011a509b602071fd15ac0f90b0ac9d86d209f4a373936908ea5efdc` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\events\032_missiles\asset_audit.md` | 106-111 | `f85e5d855716e3fdbdc44c2a80f0c6557ff14afc1f30e0af56eed78e2141cff6` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 24-32 | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-246 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\032_missiles_operations_effects.md` | 1-31 | `afc673817f2562946b16ef858a3327ac3a00b5821d942fcb2b32be5679e561c7` |

