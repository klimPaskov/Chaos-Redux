# Event 016 final lifecycle pre-implementation review — 2026-09-02

## Status and ownership

This is a bounded read-only pre-implementation audit, not an Event 016 completion claim.
Only this handoff is authored.
Gameplay, localisation, assets, and concurrent work are unchanged.
The binding source is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
The contract remains accepted; the corrections below implement its existing continuity and closure requirements and do not introduce any family, evolution, country, focus, meter, GUI, super-event, or achievement.
The actual KRG lifecycle file is `common/scripted_effects/016_brilliant_scientist_country_effects.txt`; there is no separate `016_brilliant_scientist_kruger_state_effects.txt`.

| Surface | Current audit status |
| --- | --- |
| Directorate project lifecycle | Source-present with stage-match and changed-stage reward guards; transfer report identity remains defective (F2). This is not an exhaustive certification of every family payoff. |
| Exactly four evolutions | Four incident paths and scheduler are present; mixed enabled/disabled prefire state needs correction (F6). |
| Canonical Kruger transfer and obligations | Source-present transaction and portable-history machinery; prevalidation mutation and report identity require correction (F1–F2). |
| Containment and permanent departure | Source-present terminal routes; host-reaction cleanup is incomplete (F3). |
| Foreign operations and confirmed death | Source-present start/outcome/settlement machinery; terminal transient relationships need cleanup (F5). |
| KRG formation | Verified territory-plan path and exact snapshot inheritance are present; same-tag takeover omits the sovereignty reaction cleanup used by KRG release (F4). |
| MCP event evidence | Inspect/render calls completed for 27 bounded selectors; initial helperless graph, later full graph with unresolved diagnostics, and unavailable old comparison baseline prevent a clean lifecycle proof. |
| Weighted validation | Pending specialist baseline through parent; no weight changes or independent balance certification here. |

## Actionable findings

### F1 — Transfer mutates the DHR expedition before validating the transfer

Evidence: `common/scripted_effects/016_brilliant_scientist_effects.txt:2936`, helper `brilliant_scientist_transfer_kruger_atomically`.
It first removes `dhrondan_kruger_expedition_mission` and calls `dhrondan_fail_expedition` whenever the expedition flag exists.
Only afterward does it initialize the committed result and enter `limit = { brilliant_scientist_transfer_inputs_are_valid = yes }`.
The input trigger is in `common/scripted_triggers/016_brilliant_scientist_triggers.txt:153`.
Its prerequisites include the valid recipient pointer, current host, transfer readiness, no active scientist assignment, no transaction lock, and no world end.

Meaningful source scenario: a host with an expedition in progress invokes the transfer helper with an invalid or absent recipient, or with another readiness gate false.
The helper returns committed zero but has already destroyed the expedition.
This contradicts the helper's own atomicity contract even if most current user-facing callers precheck recipient eligibility.

Minimal intended remediation: initialize the output first, perform all validation, then cancel the expedition inside the validated commit branch before nationality transfer.
A rejected transaction must leave the expedition, roles, and pending obligations unchanged.
Preserve the intended valid-transfer expedition failure semantics.

### F2 — Pending breakthrough identity is reused as a history-loop iterator

Evidence: `common/scripted_effects/016_brilliant_scientist_effects.txt:3017` snapshots the active report's family into temporary `brilliant_scientist_transfer_breakthrough_family`.
Recipient restoration at lines 3166, 3171, 3176, and 3181 uses the same temporary variable as the `for_each_loop.value` iterator for reported, pending, public, and classified history arrays.
Line 3189 then writes that variable to `brilliant_scientist_last_breakthrough_project_family`, paired with the separately saved pending stage, and queues `chaosx.nr16.6`.

Vanilla `documentation/effects_documentation.md:4279` explicitly documents `for_each_loop.value` as the temporary variable receiving the current array value.
The source therefore aliases a durable-in-chain snapshot with subsequent iterator writes.

Meaningful source scenario: an active family A report transfers alongside nonempty historical arrays ending in family B.
The recipient's report family can become B while its stage still belongs to A.
This is a source-level identity corruption risk, not evidence that a particular in-game reward has already duplicated.

Minimal intended remediation: use a dedicated pending-family snapshot and a distinct copy iterator.
Trace transfer with pending family A and public/classified history B/C; assert exact pending family/stage, history counts, and one queued report.
Also trace empty history arrays and no pending report.

### F3 — Nonsovereign permanent departure does not clear host-reaction obligations

Evidence: `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:218`, `brilliant_scientist_finalize_nonsovereign_departure`, calls evolution, role, old-host, foreign, and breakthrough cleanup but not `brilliant_scientist_clear_host_reaction_state_on_terminal_exit`.
The existing terminal helper at `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt:154` clears both country-pending and canonical-character-pending reaction state while preserving resolved receipts.
The old-host reconciliation helper at `016_brilliant_scientist_effects.txt:1259` does not replace that responsibility.
The finalizer is used at containment lines 286, 320, 332, and 371.

Meaningful source scenario: facility, custody, or foreign-reaction obligations are pending when release, confinement, shutdown, or the noncountry crisis path ends hosting.
The pending country and character obligations survive.
Events `chaosx.nr16.7`, `.8`, and `.9` require a current host, so the stale obligations are generally stranded rather than self-cleaned by their delayed events.

Minimal intended remediation: invoke the existing terminal reaction helper in the finalizer before losing the canonical character/current-host scope.
Preserve resolved response history.
Assert all pending reaction flags/variables clear after each terminal route without clearing career-once receipts.

### F4 — Same-tag sovereignty retains delayed host-only reactions

Evidence: `common/scripted_effects/016_brilliant_scientist_country_effects.txt:660`, `brilliant_scientist_initialize_current_kruger_state`, calls `brilliant_scientist_clear_host_reaction_state_after_sovereignty` at line 680.
The separate same-tag path `brilliant_scientist_transform_host_into_kruger_state` at line 1061 does not call it.
The existing cleanup helper's explicit purpose at `host_reaction_effects.txt:161` is to prevent former-host `.7/.8` obligations from replaying as sovereign events.

Meaningful source scenario: an eligible institutional takeover commits while `.7` or `.8` is queued.
The host retains its tag, canonical character, and current-host flag.
The queued host-reaction event can therefore still satisfy its current-host trigger after sovereignty.
This differs from fixed-tag KRG formation.

Minimal intended remediation: apply the existing sovereignty reaction cleanup to the same-tag carrier at the equivalent post-inheritance point.
For split KRG formation, also explicitly dispose of the former host's country-pending reaction state after any required snapshot/copy; clearing the new KRG carrier and character alone does not clear the old country's flags.
Do not erase unrelated project or permanent foreign receipts.

### F5 — Confirmed death and split sovereignty leave transient foreign relationships

Evidence: `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:911`, `brilliant_scientist_foreign_commit_confirmed_death`, removes roles, reconciles the host, clears terminal host reactions, retires the character, and clears facility/current-host pointers.
It does not call the transient relationship cleanup at line 1191, `brilliant_scientist_clear_foreign_relationships`.
That helper clears active controlled-access/joint-laboratory/protection flags, reciprocal partner flags, and global partner/site pointers.
Ordinary transfer (`016_brilliant_scientist_effects.txt:3029`) and nonsovereign containment (`containment_effects.txt:222`) already invoke it.
Split formation `brilliant_scientist_form_kruger_state_from_verified_plan` (`country_effects.txt:931`) also reconciles and departs the old host without this transient cleanup.

Meaningful source scenario: controlled access, a joint laboratory, or a protection framework is active when a successful assassination confirms death, or when the laboratory becomes a separate KRG country.
The former host/partner flags and saved global relationship pointers remain live.
The actor's `brilliant_scientist_foreign_finish_operation` at line 234 settles operation bookkeeping; it does not remove those relationships.

Minimal intended remediation: close or deliberately transfer the existing transient relationship contract at the terminal/split transition.
For death, use the existing transient cleanup only after checking its context cleanup does not remove anything still needed by the assassination's settlement.
Preserve permanent observation, resolved-target, detection, result, provenance, and operation-history arrays.
Do not use broad resets or erase learned technology.
For sovereignty, retain only relationships explicitly supported by the accepted inheritance design; do not leave an unowned global pointer.

### F6 — Prefire evolved opening writes disabled lower-stage delivery and policy state

Evidence: `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt:537`, `brilliant_scientist_prepare_evolved_opening_runtime`, sets lower-stage personal delivered flags and policy flags using only the numeric highest prefire stage.
The three blocks do not test their individual stage's enabled state.
At line 570, a stage-IV opening marks stage III delivered; its secret branch sets `brilliant_scientist_forbidden_weaponization_authorized`.
By contrast, `brilliant_scientist_apply_disabled_evolution_safety` at line 30 clears disabled-stage policy state and the existing prefire chronology recorder in `016_brilliant_scientist_effects.txt:3330` checks stage enablement.
The numeric seeding helper at `evolution_effects.txt:169` likewise needs a targeted check against the accepted disabled-stage semantics.

Meaningful source scenario: stage IV is enabled, stage III is disabled, and the opening is secret.
The runtime preparation writes stage-III delivered and secret-project policy state after applying recorded-state safety.
A later synchronization may clear the authorization, so this audit does not claim that the forbidden decision is definitely clickable in that interval.
The unconditional disabled-stage delivery receipt itself is the concrete discrepancy.
The same issue applies to lower enabled/disabled combinations for stages I and II.

Minimal intended remediation: gate each lower-stage delivery/policy write by that stage's enablement and preserve the permitted safe-skip route.
Do not treat highest-stage selection as proof that every lower stage is enabled.
Verify all enabled, all disabled, only IV enabled, and III-disabled/IV-enabled openings, plus active-host progression using the same combinations.
No fifth evolution or replacement track is needed.

## Important non-findings and retained safeguards

- The current `events/016_dhrondan_country_events.txt` `chaosx.nr16.49` is not the stale unguarded-response flaw: option `.a` at line 54 and `.b` at line 80 require `dhrondan_compact_response_is_valid`; `.c` at line 100 requires its inverse.
- `dhrondan_clear_diplomatic_offer` exists in `common/scripted_effects/016_dhrondan_country_effects.txt:269`; an earlier graph's unresolved helper does not prove absent source.
- Project finish at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:61` checks the active family and stage, and applies stage output only after `brilliant_scientist_project_stage_changed`.
Cancellation at line 48 returns the saved active capacity delta and clears the receipt, so repeated cancellation does not repeatedly restore that capacity.
These are meaningful existing guards, not an exhaustive project-balance pass.
- Ordinary transfer reconstructs personal research and explicitly does not fabricate physical project sites or replay completion rewards (`016_brilliant_scientist_effects.txt:1975`).
Fixed-tag formation has separate exact-state inheritance.
- Temporal initialization is destructive, not additive: `016_brilliant_scientist_effects.txt:497–498` resets debt and clears target-use receipts, and the recipient path calls initialization at line 3067.
However `016_brilliant_scientist_triggers.txt:19` excludes prior host history, former hosts, transfers, and departures from recipient eligibility.
No supported debt-bearing never-host recipient route was established here.
KRG exact inheritance copies debt and target-use history (`country_effects.txt:241` and 346).
Do not transfer all old-host country debt into a new host merely because the canonical character moves.
If an external country grant can create those same receipts before first hosting, preserve that recipient's existing national state; that specific caller must be proven before promoting a patch.
- No new asset requirement was introduced, and no asset, portrait, model, focus-layout, GUI, achievement, or spreadsheet completion certification is made by this lifecycle audit.

## MCP evidence and exact limits

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Every selector below received both `hoi4.event_inspect` and `hoi4.event_render`.
The narrow shape was `selector: {kind: "event", eventId: "<id>"}`, inspect `mode: "trace"`, render `view: "options"`, `expandHelpers: true`, `maxDepth: 1`, and `maxNodes: 12`.

The first 22 selectors returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`, analysis mode `focused`, revision `24c4820507672f95115e5fd7e9c7d66a1c63bf637ee7f70f0e049b222ad48049`, graph hash `fe47f05d034265cb25dcc3fbdedf744c16e7cbc177ac515ecf6d168b45bc1668`, and zero indexed helpers.
Validation stated: “Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked.”
Source review is not substituted for that missing graph coverage.

Later selectors `.7/.8/.9/.31/.32` returned `EVENT_INSPECTED` / `EVENT_RENDERED`, analysis mode `full`, revision `e9eaf789ca42f8b6c599680c70d2e9074be8c115474bcb6c1773efbe4a37337b`, graph hash `ce90845bb97114e0f5e5974c162df6e2f99e964275a01a707f5a709d41e320b8`, and 18,839 indexed helpers.
Validation remained false with 3,947 blocking event-chain diagnostics across the full workspace.
Those counts are not 3,947 proven Event 016 defects.
The first full trace resource was retrievable but returned a byte-ranged payload; no claim of exhaustive artifact-diagnostic review is made.
The differing revisions must remain explicit rather than silently relabeling the earlier partial evidence as full.

Comparison attempts:
1. `before: {revision: "24c482..."}`, `after: {kind: "current"}`, `render: false`: tool bridge serialization failure, “failed to serialize JavaScript value: expected value at line 1 column 1.”
2. `before: {kind: "revision", revision: "24c482..."}`, `after: {kind: "current"}`, `render: false`: schema rejected `kind` at both `before` and `after`.
3. Accepted input shape `before: {revision: "24c4820507672f95115e5fd7e9c7d66a1c63bf637ee7f70f0e049b222ad48049"}`, `after: {revision: "24c4820507672f95115e5fd7e9c7d66a1c63bf637ee7f70f0e049b222ad48049"}`, `render: false`: returned `EVENT_REVISION_NOT_CACHED`, “Requested event graph revision is not cached,” no artifacts, validation false.
4. After the parent confirmed that omitted `after` means current, `before: {artifactUri: "<options JSON>"}`, `render: false` was tested using the actual [full-analysis options JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3fb35fdc810dd10e3be2e774510235f366e4de8ae277d5321fc75df6eec1488/fb1d94ac71955a44507c6261f02f0501de3e105ffd391e60c0498600eb484069/event-options-e9eaf789ca42.json), not its manifest.
The resource decoded as `schemaVersion: "event-render.v1"`, `graphSchemaVersion: 1`, with bounded nodes, edges, source hashes, and state accesses, but no full-graph wrapper.
Comparison returned `EVENT_GRAPH_ARTIFACT_INVALID`, “Event graph artifact uses an unsupported schema version.”
The inspected/rendered artifact lists contain trace-report JSON or render JSON/manifest/SVG/PNG, not an identified compare-compatible full event-graph artifact.
Resource discovery exposed only the generic artifact URI template and no separately listed event-graph resource.
A durable compare-compatible baseline remains a tooling blocker; do not label a render/report wrapper as that baseline.

No source patch exists in this audit, and no before/after lifecycle comparison is claimed.
The parent needs a retained full baseline and a post-patch comparison for the eventual implementation.

| Selector | Inspect mode | Trace artifact | Render artifact |
| --- | --- | --- | --- |
| chaosx.nr16.1 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2bc82ff44006de5fd43146abce81e3c8304daefc8fc4a1c4a36da3e285541783/449dd64ce0ae821ce505b2e1e9569f5925ad7c1d733ec02182e09b6067cc9e55/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2be07ca74d2bf85514ccd9b84a8a411584e3644905adceadf316a298aef4442/2f55ba943eab8bfb95726fb0057f639e98f7967fa340399a97cc9b682eccfa51/event-options-24c482050767-manifest.json) |
| chaosx.nr16.6 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee6f088deb52fcb7ff2ec272ef4d11ce147fc34b5ccbed036be9c0a082708d53/69eb9b947c022e40c3efbb53cbd39e835d667cc755aae614176f934bc1a6a58c/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70f5771e75fb61a599924b60071f335ffba2a2a782d0d3825786069c69dbf2ae/d5b1e72628204ee57ac82430369222bca7beca4e9c14301f03da90bc30055f3a/event-options-24c482050767-manifest.json) |
| chaosx.nr16.13 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d88cc344f2c95fb9e277bbf7d053c5b7a23b6ec55a4128c525334ccf6463be02/ae00fd1a062db9c34a616e647a9958108f1426a92bd55892fb176d0b2188162c/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7766f03c390c4634b3184043781e3e666184cba8056343fbdfda60b5a0dd98b7/a8cd8e9556cd8b29886178fedc9c39994f07e639ebc69e768d67d37d8c3b1f53/event-options-24c482050767-manifest.json) |
| chaosx.nr16.21 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2df49908e7fdffe0f545e001aa86acb0be322cfadd7560c591e0cf9144d08a8/c2c500c9578d5e496fb2ed67e7c94c9fda245a733f813c3875ce04218c6a84ac/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eca3bba4aaf88c416630f9477db4538fd7896b7061446c757991edc33e85e16b/3ecabddb6a57fd83d8fbb53d901bbeeafbac4af97580b7e09a59f297a140cb76/event-options-24c482050767-manifest.json) |
| chaosx.nr16.22 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29b4ac7abbfb7b9fae76df26d803ca5e2dc4492b886d4f39b753a2ab37502820/c3a8a3c9364fa7ecfeab2f537025c11ed1b65cd0564e6212c775d6eca67e3902/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8581b555e1505424ffd471fc75082a6978024864055ab20818f747b6ab164639/c0b8e539987eb8289cd2e8a5a4338d97e0c91c9452ee4a792f824ee9373e577c/event-options-24c482050767-manifest.json) |
| chaosx.nr16.23 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04fad02ab7eedd60ef1d85bb8ca6919ea466fc22200120d62c8d60df8bc1ae9a/4d4cbd80f0bbfbe77db83bea50d6aa96d72b333baf6c81d7f036a64467c535d9/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02588512b617362ad24c7f99fccdf184268f7fd36755299a26e2417ca113d2ad/00c4bf01b12d2e068389a33707d65ff0ab954da3a59c3733bc2bc7d14cafdd43/event-options-24c482050767-manifest.json) |
| chaosx.nr16.24 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b331f61370ad35e11993d9a1ed8014d3ace997bb8bc240ec1d18baca04f5bb8d/5ee3f59305839be96ba21bbad5753cf3cea457f6d4b09dcdda242aac56bfc0ad/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/735ea9f7c95f1d660b81877cee34b636a1aa62f83daa21d305ff4d8e3413947c/2c8dbf55b9b0906ad4c1094901e78aaaa9108a6d99057ad0da750869c43759ff/event-options-24c482050767-manifest.json) |
| chaosx.nr16.90 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30a379af25b94e4f5acb45c4bd06368a2b21ad2bbf22149b84997aaff29e5ca9/42ab7dca7a4490431b9a69c0fb5585ae6c0e08eed1e850b6bf273794c49adf27/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8812aa27f00b8a993aeecfb3d8e41071dfda00806529b16009eab0d8c4d31947/53a4ccb29edec93c0d7c2e6e9868f0b2cbedc5cea03923606297e5b8555a261d/event-options-24c482050767-manifest.json) |
| chaosx.nr16.30 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcf6e9c48f3d15e055083dfd8c560178a366c3c621824745f8f1ceac5b409554/f422030b84bc2c4df7c14801ac09da07ab1542e8ba4dab8a0f46ebb9427715bb/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79b8425e5ac1cfaaa58533dc6ba0a10670d7caeb5038be2dbc437343fc024653/0a6e4ba44dcb6e29f84f8403c5dcd9be2b16ea6f45afffdec759cda5e5f7342e/event-options-24c482050767-manifest.json) |
| chaosx.nr16.100 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed9796864f9fa783eea19d2ce2dc0e593491a52f5eae7e72ee24ac7ffccefe1f/9aa54f7a113b6ad786f704e0ac8dbc5a63e65d58e5144565b379acfb90e61193/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c72c4a6e789f0697227392aa1f428a3521b9b03e5197742a0e40e34e7b1fd932/1a4bcee5b2c6f2d608cb0fae085ce85da0efa786512f61b57db20b8dc37cf3c7/event-options-24c482050767-manifest.json) |
| chaosx.nr16.110 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7adf1df5ac4135f6a37e1b36ec1cf852cc706b1f6d0afcf4b91f9ceb2634596b/cd792c50c91711c6cc2f5e4f22bc4c27daba636d84c7789b4435439dea605f41/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47c0ac2b9c4e79345cb6bfac083ad3e33fc6d56bfe66955e7c2df4043df4e869/39fba2bcdf0b22b50159cd37a7f16a66ad587448a1cac12343dc0519830495d9/event-options-24c482050767-manifest.json) |
| chaosx.nr16.120 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d23a016b6c17cc6a73ffcf9deb8d7c9b398fc531d1c5a20abb3d4a11dff7062/5bcb39b9fcf601ddf45152264a9440a4cddb0705cbff26e90eb1f444c4ab1747/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23eecbde25d694f605b67a224da357e7cce586a493077d7b042c574bffc89ebe/41bdd532ec1376d4060f6da47e3f94003bdbe998c5183da82a2919657d23cf93/event-options-24c482050767-manifest.json) |
| chaosx.nr16.130 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45f50d2d50438a3485c7a0c1a1a1832fed6fe8a718ab5a96e4badab4eeeeb9e4/553693fb991efbae9bdbd58b8a3939e1427c76d8d293baae28c680d15b0bfc24/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ed75e1938dae8dd8862110faeb275262af1069698d860295112a46972aecdb4/7310de848b32cda4055f332c2063c79045ead9d8805f793824210704244291de/event-options-24c482050767-manifest.json) |
| chaosx.nr16.140 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de184a408aeb0ccbc97b259addd5b1502c3c676e79eb8a1b62205941561f7569/10ba24b7f4c1a5e929a3e006aa312d3b586b42c62a287d34b345f33e17cc19d9/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4c6751c5001f82c0cce1714e1a640b632c6a464230511851ae53d7265f5075d/428fb5150a4e0c59a00a2eb972ee01f8643898fb0a752b4e204deb7ba4b9b22d/event-options-24c482050767-manifest.json) |
| chaosx.nr16.150 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/011277efed35286ee3bbdfdc95b78fcfb90433b3b025ae54268f4ca0583aaecf/97c5c4cc587d2dd6a9b791835b4c81857d3ffdb1f72a253885d18dd9471869e0/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8811567716e3fd2f6850a048b33f889e3a61f7446321c436b72a459b439e3da/dbf38b8095004fca5c3c79703f6ed02ff4413da9c589e9f3906fc4933006a24f/event-options-24c482050767-manifest.json) |
| chaosx.nr16.160 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccc29194e1a7e5f63d2d35eed9592230e7293cbb43441e809f520665f0c0e832/91e8a39065cd62a9b5c7a310cd97e3fe4783eb75927c61a3fca4f4e5afcf33c9/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5b951bdc93b50c4a63bb91d114e0b5c25447a8f1ee0843a9cbded0e1361f4e4/1b3c96fd1016324167d897ef08f9b3b0df3ffa5c289de42cd1f09e47bf869e26/event-options-24c482050767-manifest.json) |
| chaosx.nr16.170 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec0e1c40cf829638b2926b8923c0b7e6c215d65effca2faafa050c8a1d53941d/60e3174115dcb4376f11b0e65faccceaa8de49ae7ba2863876891702c6e07dd6/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd56946e77197eb11ac4a91006cd654e0c4a9c2d8b4063d90f2cadb4d46c42ce/9e5cfefd92d55b86b372693f427d5a10d7a595be7bd93daf34933752c2d3cd3c/event-options-24c482050767-manifest.json) |
| chaosx.nr16.180 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7c7ba3fcef68aa2c6af26e46162bddeace6a1de7d1cdf0c575b42b7bd203d08/26d443fdaf5f3f9bac860ee09f780c808bec83df22c7c0c0cd63c158db58e7d6/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7b71d2b47dbd716fb84d05fd6f5588b649f117946aaabcbc4d136360f0176f3/a3d7ddfb819a7c1487a74b700c4903397d60e4861944d958ac3e9bf347b6fc3f/event-options-24c482050767-manifest.json) |
| chaosx.nr16.190 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c157ac6d76485244cc9ff13155fd1d7da0658186c140bbafc5c67ec374aa8b1/f99d062829e2183a636c345914a87ff5d59452ada0f74c2e4e54a9eed7076357/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e8c46905d40a6a5949bb95bd678f375077e494840fbb6f13d714f6770b09895/35bdac253bed6143cef7c9b688448acdff3ec959aba0f5bdc275fe458aa53046/event-options-24c482050767-manifest.json) |
| chaosx.nr16.193 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbd5d44c6b19474b5377eadb038ab862e20775716d6b04ee51c60a1fd876b5be/3d332c4735cf00dafb4ba5eba3a7af48c142f4505a0696c6b05900233a220d0a/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f6a7849a05c3077acac21e505db0ddcf1ae6e73ded9a7a739e3f6c92bbbb92f/ae82c4b35c8d4664737ec9ac4e9aab13e90a1aeaf6d2771414d672298a6af2c7/event-options-24c482050767-manifest.json) |
| chaosx.nr16.49 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0ae8221d8a89209d2be7a1c460cd85748e4ed6319c5cd3121f92af5c7bd715b/3e9f5167b1c6d766d18a57cb91f9831f5990647d7f547b301a9ca86ba438e303/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e65cf52951a9f9aaf464bc4523489f01f5460c5e465bcd6bb7d9bb873b4f7f0/ad66ccc732fef5a7bdf28024e83cb6d7b1e73813eeb5ecaf74a8919279ddc639/event-options-24c482050767-manifest.json) |
| chaosx.brilliant_scientist_krg.1 | focused | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57053ef4fecd1b837c58b9e902a4cfee8f7e178600c7901183bfa376bdb97fb3/55458ebb88e904492cc167c3c5c4dced3b35ee095f0c88fe7701f1c47e504ce2/event-trace-24c482050767.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/707e6a092b2bacb5aa048f352a5251caaf0057aad9c104db8277b5d2f4422bee/d6107095a7cf49fe211bfee78bfb9eb515b47e81284d56ad21354ecefba5b4ce/event-options-24c482050767-manifest.json) |
| chaosx.nr16.7 | full | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d19d445f49ebdf0a9f8be1c285cd78565bc3ab6e94bf9325a9c9ff9bf6696b71/baf9c4d467814735de10c01b48699c54242a96c1e361447a16c4b0766e72af34/event-trace-e9eaf789ca42.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/934a5629f6456c9b764d04195f13055c9d47f961fe247796c9e86dc4653403d5/bceedc5baac2d13949822c2760866bade9b9d989de6be10fae42959c0fd120de/event-options-e9eaf789ca42-manifest.json) |
| chaosx.nr16.8 | full | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bc9821375f6acccc4cda5c9d2b3d18eb81dd90dc78becbdd69c4c1eda772cbb/6a103d6f8a1f3e329f4d5b422b2224f3bdf5f9b1de45a021db515eaef9f0f0f2/event-trace-e9eaf789ca42.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d69047597c7b27ae743aa497b843ab643b1c59cfa22e28372a3059154d197f7/c7e862b7b4edaaec0ccfa621b61fdf5e8fc1791d9ee60627387300253abcdaa1/event-options-e9eaf789ca42-manifest.json) |
| chaosx.nr16.9 | full | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/334dd401883c8b95bc4be3ea6a5cdca5798ed1df850cb663100ccc0df359a21e/7e7e8cce5b443636cff1b8990708518002c5b31c81102b2e4f23ae48197d1d5b/event-trace-e9eaf789ca42.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e22a197f85ce67d72c4200e5279ad7168ba68dbeffb6cb2e20707cb776d011cd/d93ca0f29fe51277984fb8952b55a244da19baad2c8d8e0cec1958af0a9e72e8/event-options-e9eaf789ca42-manifest.json) |
| chaosx.nr16.31 | full | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c3658dd2e37e37e81793ea8967c79e292e0625463947050e5dbea2f9104d8dc/7d1733fa7fde942c9c257be2aea1b9a36443a60cca1c437585d589f05b42c78c/event-trace-e9eaf789ca42.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e11afe265c00e2c328b5d4665b76f2c151bfc3de94a80c88234ddfd763ea23ed/ecb1a47e4315b6f6961ff853aeca89d077d289ff6f7bc9dfa88b10016a897333/event-options-e9eaf789ca42-manifest.json) |
| chaosx.nr16.32 | full | [inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/922d78e999a78e6c80de80ef269f5009c07582d8452f4e0fe47905c275673037/c86dc23c5c2e3c0ad6eb2a784e7dd94cf40fde17a8722adbb77704abd262f577/event-trace-e9eaf789ca42.json) | [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5c61f68e130f341f94ad0ab025feac4ad57f4a3dfe123b39515205a9c81ee62/0c937423d51528f2348729af4964765d17489b3d43636b7daf4342e253fb00a3/event-options-e9eaf789ca42-manifest.json) |

## Weighted surfaces for the parent's exact specialist baseline

Per the parent's instruction, this audit does not spawn a second broad probability auditor.
The existing tranche4 Bio/Portal/DHR-rebellion pass does not certify these tranche5 surfaces.
Route any affected surface below through `chaosx_ai_probability_auditor` before a weight/weighted-target patch and compare the same named scenarios afterward.
The suggested corrections above do not require changing balance targets.

- Transfer/host obligations: `events/016_brilliant_scientist_host_reaction_events.txt`, `chaosx.nr16.7/.8/.9`; baseline normal host, pending transfer, terminal departure, and same-tag sovereignty eligibility.
- Evolutions: `events/016_brilliant_scientist_evolutions.txt`, `chaosx.nr16.21/.22/.23/.24/.90`; `common/mtth/016_brilliant_scientist_mtth.txt`; `common/decisions/016_brilliant_scientist_evolution_missions.txt`; use all enabled, all disabled, only IV enabled, and III-disabled/IV-enabled, for both active and prefire openings.
- Foreign operations: `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:324`, `brilliant_scientist_foreign_calculate_operation_outcome`, including randomized success/detection at lines 617 and 623; `common/mtth/016_brilliant_scientist_foreign_mtth.txt`; foreign event options `chaosx.nr16.100/.110/.120/.130/.140/.150/.160/.170/.180/.190` and `common/decisions/016_brilliant_scientist_foreign_decisions.txt`.
Priority scenarios are ordinary versus continuity-protected assassination, detected versus undetected result, pending operation with host loss, active relationship plus confirmed death, and active relationship plus KRG split.
- Containment/formations: `events/016_brilliant_scientist_containment_events.txt` `.30/.31/.32`, `common/decisions/016_brilliant_scientist_containment_decisions.txt`, and formation choices in `events/016_brilliant_scientist_kruger_state_events.txt`.
Use valid/invalid territory plan, pending host reactions, and already-active sovereignty.
- Directorate stage choice/incident weights remain an independent closure obligation in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, and `events/016_brilliant_scientist_project_incident_events.txt`.
No full family-by-family probability claim was made here.

## References, disposition, and next action

Offline wiki references consulted: Data structures (event targets and temporary variables), Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, and Character modding.
Vanilla references consulted: `documentation/effects_documentation.md` for `for_each_loop`, saved targets, and `set_nationality`; `triggers_documentation.md` for `has_event_target`; `script_concept_documentation.md` and `common/script_constants/documentation.md`; `common/decisions/_documentation.md`; `events/NSB_Poland.txt:1198` for nationality transfer followed by verified character presence; `common/decisions/_generic_decisions.txt:260` for a lifecycle cancellation predicate.
Skills used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-decisions-missions`.
They kept this review scoped to accepted design, required explicit disabled-stage and lifecycle evidence, and prevented source-only review from being labeled MCP proof.
No skill was created or updated.

Accepted-plan disposition: the final contract is retained unchanged.
F1–F6 are implementation gaps under that contract, queued to the parent for a bounded correction tranche.
The old `.49` response-guard finding is superseded by current source.
The temporal-debt portability suspicion is not accepted as a confirmed defect.
No unapproved fallback or design simplification was introduced by this audit.
The remaining omissions are validation coverage explicitly described above, not waived completion requirements.

Recommended next action: parent fixes F1–F6 in the existing lifecycle helpers, acquires exact weighted baselines only for changed weighted surfaces, then repeats the named source scenarios and full-graph inspect/render/compare against a retained baseline.
No game launch, log collection, or request for user-run tests was performed.
