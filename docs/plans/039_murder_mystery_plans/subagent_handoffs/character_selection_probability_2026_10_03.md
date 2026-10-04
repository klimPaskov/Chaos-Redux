# Event 039 Character Selection Probability Baseline

Audit date: 2026-10-03.

Status: source review complete. Probability and event-structure conclusions remain unresolved because the required HOI4 MCP routes are not exposed in this session.

This is a read-only baseline handoff for the opening ruler selection and founder First Knife selection. It does not certify the full Event039 implementation. No gameplay source, localisation, workbook, or other source file was changed. Nothing was staged or committed, and Hearts of Iron IV was not launched.

## Audited surfaces and baseline identity

1. Opening host selector: `murder_mystery_prepare_opening_package`, called by `chaosx.nr39.1`, writes `murder_mystery_opening_leader_character` from the `random_character` block at source lines 334-336. Its downstream opening transaction registers that pointer and later retires it during successor installation at lines 351-359 and 443-457.
2. Founder selector: `murder_mystery_create_assassin_state_candidate`, called by `chaosx.nr39.32`, creates `MURDER_MYSTERY_FIRST_KNIFE_NAME` as the country leader at lines 1565-1570, then writes `murder_mystery_first_knife_character` from the `random_character` block at lines 1595-1598. The selected character receives the First Knife flag and is later used as the registered and capturable target at lines 1600-1612, 695-702, and 761-767.

The exact baseline source is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\039_murder_mystery_plans\validation\character_safety_2026_10_03\039_murder_mystery_integration_effects.txt.before`.

The live source `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\039_murder_mystery_integration_effects.txt` and the named before snapshot were both 110,911 bytes and had SHA-256 `98928E7645082F7CC453FAD74FAE4DFDDA2D75381A5A266D569D5B9A3BADDFEC` when checked. They were byte-identical at audit time.

The same file also contains a foreign-leader selector at line 846 and an inheritance selector at line 1178. Both are out of this audit scope. The inheritance pool remains explicitly unaudited. The founder event option `chaosx.nr39.32.a` has adjacent `ai_chance = { base = 100 }` at `events\039_murder_mystery.txt:350`. It controls event-option willingness, not which character the native selector chooses, and was not evaluated as a separate surface here.

## MCP route attempt and evidence limits

The audit began with the required call attempt to `mcp__hoi4_agent_tools__hoi4_probability_inspect`, using the mod-relative source object `{ path: "common/scripted_effects/039_murder_mystery_integration_effects.txt" }`. The route was not callable because `tools.mcp__hoi4_agent_tools__hoi4_probability_inspect` was `undefined` in the connected tool inventory. This was a missing route, not a timeout, so there was no narrower retry to make.

The same inventory check found no callable `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_render`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup` routes. The available Blender HOI4 tools are a separate namespace and do not provide this evidence.

No probability adapter result, event graph, source revision from MCP, scenario hash, comparison ID, artifact URI, or rendered evidence path exists for this baseline. Local documentation was read directly because the reference MCP routes were absent. Those source reads do not replace the missing MCP analysis.

## Exact source facts and documented behavior

Both selectors use `random_character` in country scope with only `limit = { is_country_leader = yes }`. Neither block declares a numeric base, multiplier, modifier trace, threshold, rank score, or normalization rule. These are random-character selection clauses, not AI score races, click probabilities, MTTH timing distributions, or declared custom weighted pools.

The offline wiki describes `random_character` as selecting a random recruited character in the scoped country that meets the limit, and describes `every_character` as iterating over every such character. The installed effects documentation identifies both as COUNTRY-scope effects. It says country-scope `add_country_leader_trait` and `remove_country_leader_trait` act on the scoped country's leader. Installed trigger documentation lists `has_trait` as valid in CHARACTER scope.

There is a material documentation conflict on the current predicate. Offline `Triggers - Hearts of Iron 4 Wiki.md`, lines 2034-2035, distinguishes `can_be_country_leader` as active or non-active and describes `is_country_leader` as the active country leader. Installed `triggers_documentation.md`, lines 5408-5414, says `is_country_leader` checks that the current character is a country leader but does not specify active versus non-active. The parent-provided audit premise says the predicate admits non-ruling political leaders. With the probability and runtime inspection routes absent, that premise cannot be confirmed or rejected from this audit. Do not treat the offline wiki wording as proof of current installed-engine behavior.

For the founder surface, source-level identity is not tied together: the script creates the named First Knife ruler, but separately flags and saves whichever character `random_character` returns. The later country-level check at integration-effects line 1667 checks for a country leader named First Knife. It does not compare that ruler's character pointer with `murder_mystery_first_knife_character`. If non-ruling leaders are eligible as stated in the task premise, the wrong character can receive the First Knife flag and target identity while the named First Knife ruler still satisfies the separate country-level name check. This is a conditional source-risk finding, not an observed engine outcome.

For the opening surface, the saved pointer is passed to the target registry and is the character retired after successor verification. If the selector can return a non-ruling political leader, the transaction can retire that character instead of the sitting ruler. The effect source has no separate equality check tying the saved pointer to the current ruler.

## Scenario matrix

The scenario IDs below were supplied for this audit. None could be submitted to the unavailable adapter. Candidate-pool completeness is therefore incomplete for every scenario, and all selection results are unresolved. No candidate IDs, scenario fixture, live country roster, or external-factor map was provided.

| Scenario ID | Surface | Candidate pool and external factors | Result |
| --- | --- | --- | --- |
| `RULING_ONE_ROLE` | Opening and founder | The fixture would need every recruited character in the scoped country and proof that exactly one meets the installed predicate. No character roster or predicate result was available. | Unresolved. No exact or bounded selection probability. |
| `RULING_WITH_OPPOSITION` | Opening and founder | The fixture would need the sitting ruler and every recruited non-ruling political leader, with their roles and eligibility at the call. The exact candidates are not supplied. | Unresolved. The local references conflict on whether the predicate includes non-ruling leaders. |
| `FOUNDER_WITH_COPIED_ROSTER` | Founder only | The fixture would need the complete recruited roster after dynamic-country creation, including the newly created First Knife and any copied or transferred characters. The source also performs character nationality changes and a DLC-conditional operative setup before selection, but the runtime roster is not supplied. | Unresolved. Pool and external factors incomplete. |
| `NO_RULING_LEADER` | Opening only | The fixture would need all recruited characters despite the absence of a current ruler, to establish whether any can satisfy the installed predicate. No roster or runtime result is available. | Unresolved. No conclusion about zero-match behavior or fallback. |
| `DUPLICATE_ANCHOR_FAIL_CLOSED` | Post-patch acceptance scenario for both selectors | The baseline has no ruler-anchor marker. A post-patch fixture must identify the ruler and every other character carrying that marker, then verify that a match count other than exactly one commits no target. | Not applicable to baseline and not evaluated. Required in the after-patch audit. |

No scenario supplied a date, scheduled state change, quantified uncertain input, seed, repeated cadence, or terminal-state schedule. These selectors are point selections per invocation, but invocation frequency and campaign-state changes were not modeled. `probability_simulate` was not appropriate because no uncertain-input distribution or seed was declared. `probability_sequence` was not appropriate because these are not a complete declared custom pool with cadence and transitions. A numeric sensitivity sweep has no source-level tuning parameter here. The required tools were also unavailable.

## Results by evidence class

- Exact source facts: two in-scope selectors use `is_country_leader = yes`. Neither supplies explicit numeric weights or a character-pointer equality check. The founder creates the named First Knife before the random selector.
- Local documentation evidence: the effects and triggers support the proposed country-to-character marker traversal at the documented scope level. The offline wiki and installed docs do not agree on the active-leader meaning of `is_country_leader`.
- Score-only result: none. No AI score or modifier trace was returned by MCP.
- Exact, bounded, or sampled probability result: none.
- Unresolved probability result: all five requested scenario IDs, actual candidate sets, normalized shares, and distribution properties.
- Ranking, threshold, sensitivity, rank reversal, starvation, and dominance results: unavailable. The source clauses declare no ranked score, and no adapter result enumerated eligible characters. Do not infer uniform selection or candidate probabilities from the word “random.”
- AI validity: not applicable to the two native identity selectors. The adjacent `chaosx.nr39.32.a` event-option score was excluded as a distinct surface.
- Repetition and exploit risk: no repetition rate was measured. Conditional on the task's non-ruling-eligibility premise, selecting an opposition leader can misidentify and retire or capture the wrong character. The risk is identity corruption, not a demonstrated numeric-weight exploit.

## Recommended patch and required after-pass

For both `murder_mystery_prepare_opening_package` and `murder_mystery_create_assassin_state_candidate` in `common\scripted_effects\039_murder_mystery_integration_effects.txt`, apply the parent-proposed ruler anchor: add the temporary zero-modifier country-leader marker in COUNTRY scope, traverse `every_character` with `has_trait = <marker>`, count matches, and save the event target only when the count is exactly one. Zero or multiple matches must fail the owning transaction closed. Remove the marker from the current country leader immediately after the traversal and before target registration or any later step.

For the founder, perform the anchor only after creating `MURDER_MYSTERY_FIRST_KNIFE_NAME`, and ensure the registered pointer is the newly created current ruler. The existing country-level name check is not a substitute for pointer identity. The marker identifier was not supplied in this baseline request, so its uniqueness, trait definition, zero-modifier behavior, and collision surface remain unverified. The duplicate-marker scenario should also confirm that no off-ruler marker is left behind to poison a later attempt.

After the owner patch, rerun the same five named scenarios through `hoi4.probability_inspect` first, then `hoi4.probability_evaluate` for each applicable exact or bounded trace. Use `hoi4.probability_sweep` only if a numeric sensitivity or threshold is introduced, render an unresolved or comparison view when useful, and run `hoi4.probability_compare` against the immutable before snapshot with the identical saved scenario set. Also use `hoi4.event_inspect` and `hoi4.event_render` for the opening and founder event chain. Do not compare the current source to itself or report exact selection probabilities unless the adapter supplies a complete pool and resolves the external factors.

## Local references and skipped analyses

Offline wiki files read directly, with local SHA-256 recorded as the available file revision:

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, lines 136-137 and 2940-2942, SHA-256 `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md`, lines 1757-1762, 2034-2035, and 2054, SHA-256 `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, lines 49-61 and 269, SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 263-305, SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.

Installed documentation read directly:

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 1008-1019, 3743-3761, 5343-5350, 5946-5957, and 6505-6512, SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, lines 3844-3851, 4951-4958, and 5408-5415, SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

Skipped or blocked analyses:

- Probability inspect, evaluate, sweep, compare, and render are blocked by the missing callable HOI4 probability routes. No analyzer evidence was substituted with hand arithmetic or a guessed uniform pool.
- Event inspect and render are blocked by the missing callable event routes. Source reading is not structural MCP evidence.
- The reference context, search, read, and source lookup routes are absent. The local wiki and installed documentation sections above were read directly, but no MCP source revision or indexed-use coverage exists.
- `murder_mystery_execute_foreign_leader_transaction` at line 846 and `murder_mystery_apply_limited_inheritance` at line 1178 were excluded by the parent-defined opening-plus-founder scope. The inheritance pool remains unaudited.
- The adjacent event-option `ai_chance` at `events\039_murder_mystery.txt:350` was not evaluated because this baseline is limited to character identity selection. It remains a separate score surface if the parent expands scope.
- No full Event039 balance certification, timing audit, route audit, or live-game behavior claim is made.

## After-patch source review and MCP compare attempt

Follow-up date: 2026-10-03.

This addendum records the owner's current founder-selection patch and the required after-inspect and comparison attempt. The earlier sections remain the immutable baseline report. The auditor made no gameplay, localisation, or workbook edits. Only this handoff was appended.

### MCP route recheck

After several live MCP discovery calls, a refreshed `ALL_TOOLS` inventory still exposed no `mcp__hoi4_agent_tools__hoi4_probability_inspect` or `mcp__hoi4_agent_tools__hoi4_probability_compare` callable. Both function checks returned `undefined`. The event-inspection and event-render routes also remained absent.

Server-scoped `list_mcp_resources({ server: "hoi4_agent_tools" })` and `list_mcp_resource_templates({ server: "hoi4_agent_tools" })` each returned `MCP startup failed: timed out handshaking with MCP server after 119.9999996s`. A narrower retry of `list_mcp_resources({ server: "hoi4_agent_tools" })` returned the same handshake timeout. A final tool-inventory refresh still showed no probability or structural routes.

Because `probability_inspect` was not callable, no after-inspect request or live schema was available. Because `probability_compare` was not callable, no before/after comparison request could be submitted. No scenario fixture, alias ID, candidate override, or guessed engine pool was sent. No after-source MCP artifact, revision, scenario hash, comparison ID, or rendered URI exists.

### Owner patch source facts

The preserved before source remains 110,911 bytes with SHA-256 `98928E7645082F7CC453FAD74FAE4DFDDA2D75381A5A266D569D5B9A3BADDFEC`. At the follow-up source capture, `common\scripted_effects\039_murder_mystery_integration_effects.txt` was 112,995 bytes with SHA-256 `A1B6954C774792052B8F3C3315D6CBD5362D8A22C0D3618FFB4D87785C9F9EE0`.

The opening selector at integration-effects lines 334-336 still contains the baseline `random_character` filter `is_country_leader = yes`. The before/after source diff contains no hunk in that block. The opening selection remains unchanged and is not covered by this founder-only patch audit.

The founder selector at current integration-effects lines 1595-1626 no longer calls `random_character`. It requires `has_country_leader = { name = MURDER_MYSTERY_FIRST_KNIFE_NAME ruling_only = yes }`, sets `murder_mystery_ruling_selection_authorized`, invokes `murder_mystery_capture_current_ruling_character`, and only after `murder_mystery_ruling_character_resolved` sets the First Knife character flag and saves `murder_mystery_first_knife_character`.

The helper `murder_mystery_capture_current_ruling_character` is in `common\scripted_effects\039_murder_mystery_character_effects.txt`, lines 13-51. It refuses to proceed when any recruited character already has the anchor trait. Otherwise it adds the trait through the country-scoped country-leader effect, iterates characters filtered by `is_country_leader = yes` and the anchor trait, increments a match counter, and saves a regular event target. It removes the trait from the current country leader before checking for exactly one match, a saved target, and that the saved character remains in the country's character roster. Zero or multiple matches do not set the resolved flag.

The anchor is defined in `common\country_leader\039_murder_mystery_character_traits.txt` as `murder_mystery_ruling_selection_anchor` with `random = no` and no modifier entries or icon declaration. `localisation\english\039_murder_mystery_l_english.yml` defines the temporary trait name and description keys `murder_mystery_ruling_selection_anchor` and `murder_mystery_ruling_selection_anchor_desc`.

One failure detail matters for `DUPLICATE_ANCHOR_FAIL_CLOSED`: an existing anchor anywhere in the recruited roster prevents the helper from adding, iterating, or removing an anchor. The helper therefore fails closed without saving a ruler target, and the pre-existing marker remains. Repeated invocations remain blocked until another owner-controlled cleanup or state reset removes that marker. This is source evidence only, not a scenario result.

The new character-effects file also defines `murder_mystery_install_movement_successor`, called by the integration transaction. The before snapshot already contains its call site and the route-specific successor identities, so this extraction does not add a new route or successor identity relative to the supplied baseline. This adjacent successor behavior is outside the probability comparison.

### Runtime target validation changes in the same after source

The integration source also contains owner-side transaction changes beyond the founder selector. It blocks repeated core capture after `murder_mystery_core_capture_committed`, verifies that the registered First Knife is recruited by the recorded Assassin State, and stores the committed target ID and generation.

`common\scripted_triggers\039_murder_mystery_character_triggers.txt` defines `murder_mystery_registration_character_is_recruited` and `murder_mystery_selected_character_is_recruited`. Each checks exact character identity through the relevant country's `any_character` roster. The runtime registration effect uses the registration predicate for named and opening-leader entries.

`murder_mystery_validate_selected_target` in `common\scripted_effects\039_murder_mystery_runtime_effects.txt` saves the validation actor before entering the owner scope. It validates that the registry owner is that actor, counts matching target-ID rows, and carries the row's used and generation values into selected state. Founder capture additionally requires the selected character to be recruited by the recorded owner, the recorded owner to be the Assassin State with `murder_mystery_first_knife_registered`, and the selected character to retain its First Knife flag. The target triggers require an unused row and a matching expected generation. Parallel target arrays must remain aligned.

These are exact source-level safeguards. They do not establish runtime character roster contents, effect-scope behavior, or probability results. No numeric selection weights were added by the founder patch. The remaining opening, foreign-leader, and inheritance `random_character` selectors were not compared as part of this scope.

### Same-scenario after status

The five saved scenario IDs remain `RULING_ONE_ROLE`, `RULING_WITH_OPPOSITION`, `FOUNDER_WITH_COPIED_ROSTER`, `NO_RULING_LEADER`, and `DUPLICATE_ANCHOR_FAIL_CLOSED`. None was submitted because the probability routes were unavailable. All five therefore remain MCP-unresolved, with no complete runtime roster or external-factor fixture and no exact, bounded, or sampled result.

At source level, the founder path is now gated by the named current-ruler query and the marker helper rather than by random character selection. `NO_RULING_LEADER` cannot authorize that helper through the named-ruler gate. `DUPLICATE_ANCHOR_FAIL_CLOSED` has the persistent-marker behavior described above. These are source traces only. They are not MCP evaluation, comparison, or engine proof.

### After-source hashes

- `common\scripted_effects\039_murder_mystery_integration_effects.txt`, 112,995 bytes, SHA-256 `A1B6954C774792052B8F3C3315D6CBD5362D8A22C0D3618FFB4D87785C9F9EE0`.
- `common\scripted_effects\039_murder_mystery_character_effects.txt`, 4,032 bytes, SHA-256 `6CFBB36AD146166532EAF76AD331F93E16821B24B59A00A172E32A1059B22B34`.
- `common\scripted_effects\039_murder_mystery_character_effects.md`, 3,452 bytes, SHA-256 `713E922B50AFA9C9A16745A561FE2159AB4071853246E104C61E54E97037A9B8`.
- `common\scripted_triggers\039_murder_mystery_character_triggers.txt`, 1,004 bytes, SHA-256 `DDB55A57B58A3BD45003EF4C7EE3E209C392110B61EAB937C0AD20773990BDF3`.
- `common\country_leader\039_murder_mystery_character_traits.txt`, 525 bytes, SHA-256 `B920BB855782B1BF78172DF2EB84DD122AD404195C52718FF6E0397F8AB5700A`.
- `common\scripted_effects\039_murder_mystery_runtime_effects.txt`, 140,557 bytes, SHA-256 `CB807179ED96C0B2C55743F7BE482CAF04B9EBBAA74CD6381EA18087FCD223E2`.
- `common\scripted_triggers\039_murder_mystery_runtime_triggers.txt`, 45,106 bytes, SHA-256 `A0DC14AB68F4F946C8006972011875EC0E00A187E476EA95BCF5CC4ED634D0DC`.
- `localisation\english\039_murder_mystery_l_english.yml`, 65,517 bytes, SHA-256 `8814F80B2646D5D202AFA98F85AB5C768EC700DB445DEC6D093457BB1D9C2CAD`.

MCP gap remains the only reason the required after-inspect and same-scenario compare are incomplete. This addendum makes no new MCP completeness claim and does not certify full Event039 balance or runtime behavior.

## Latest owner source revision captured

During final handoff verification, the integration source advanced from 112,995 bytes and SHA-256 `A1B6954C774792052B8F3C3315D6CBD5362D8A22C0D3618FFB4D87785C9F9EE0` to 113,685 bytes and SHA-256 `D48AEEC6EE032F110B6588E5CAA20AEAAED57EC9A482068330B566C303D11254`. The `A1B...` hash above is an earlier capture and is superseded by this revision for any future compare attempt.

The latest baseline diff still leaves the opening `random_character` block unchanged and retains the founder's current-ruler anchor. It also contains additional integration changes outside the founder selector and target-registry validation, including `murder_mystery_apply_live_central_capture_shock`, conditional permanent-resolution finalization, inheritance-test scheduling guards, and `murder_mystery_territorial_state_ever_created` registration.

Those extra changes affect post-capture event progression and state. They are not numeric weight edits, but they would be included in any whole-file comparison against the supplied before snapshot. This audit did not evaluate their balance or establish that a whole-file comparison isolates the founder-selector change.

The latest captured after source is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\039_murder_mystery_integration_effects.txt`, 113,685 bytes, SHA-256 `D48AEEC6EE032F110B6588E5CAA20AEAAED57EC9A482068330B566C303D11254`. Probability-inspect and same-scenario compare remain unperformed because their routes are absent and the server-scoped handshake retry timed out.
