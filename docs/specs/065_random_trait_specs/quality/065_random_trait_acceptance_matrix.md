# Event 065 Acceptance Matrix

## Use

Every row is pass or fail.

A row can be marked blocked only with the exact missing tool, source, environment, or user decision.

Source inspection alone cannot pass a row that requires runtime, render, probability, multiplayer, save, asset, workbook, or user evidence.

| ID | Area | Setup | Expected result | Evidence | Owner |
| --- | --- | --- | --- | --- | --- |
| A01 | Catalog identity | Inspect runtime constants, event file, docs, and workbook. | Every surface identifies Event 65 as Random Trait, Minor Repeatable, Chaos level 1. | Source diff and workbook export. | Main agent and spreadsheet worker |
| A02 | Normal enablement | Start a normal campaign before the rework reaches testing status. | Event 65 remains disabled from ordinary automatic firing. | Pool inspection and campaign log. | Main agent |
| A03 | Repeatable registration | Inspect shared event-pool initialization. | Event 65 appears exactly once in the repeatable minor pool. | Event inspection and array dump. | Main agent |
| A04 | Baseline boundary | Set raw Chaos to 199 with no higher manifested Evolution and force the production root. | Each eligible leader receives one accepted trait with uniform weights. | Counter dump and sampled leader inspection. | Main agent |
| A05 | Evolution I lower boundary | Set raw Chaos to 200, enable Evolution I, and force the production root. | Evolution I manifests and each eligible leader receives two accepted traits. | Evolution history, counters, and leader inspection. | Main agent |
| A06 | Evolution I upper boundary | Set raw Chaos to 399 with Evolution I manifested. | Each eligible leader still receives two accepted traits with uniform weights. | Counter dump and probability artifact. | Main agent and probability auditor |
| A07 | Evolution II lower boundary | Set raw Chaos to 400, enable Evolution II, and force the production root. | Evolution II manifests and each eligible leader receives three accepted traits with 100 and 125 weights. | Evolution history, counters, and probability artifact. | Main agent and probability auditor |
| A08 | Evolution II upper boundary | Set raw Chaos to 599 with Evolution II manifested. | Each eligible leader receives three accepted traits and no Evolution III weight applies. | Counter dump and probability artifact. | Main agent and probability auditor |
| A09 | Evolution III lower boundary | Set raw Chaos to 600, enable Evolution III, and force the production root. | Evolution III manifests and each eligible leader receives five accepted traits with 100 and 150 weights. | Evolution history, counters, and probability artifact. | Main agent and probability auditor |
| A10 | Higher Chaos bands | Set raw Chaos to 800 and then 1000 after Evolution III has manifested. | Event 65 remains at five traits and does not invent a higher form. | Counter dump. | Main agent |
| A11 | Disabled Evolution I | Set raw Chaos to 250 with Evolution I disabled and no prior manifestation. | The event uses baseline and grants one trait. | Settings state and counters. | Main agent |
| A12 | Disabled Evolution II | Set raw Chaos to 450 with Evolution II disabled and Evolution I enabled. | The event uses Evolution I and grants two uniform traits. | Settings state and counters. | Main agent |
| A13 | Direct Evolution III jump | Set raw Chaos to 650, enable Evolution III, and begin from baseline. | The event grants five traits, records Evolution III only, and gives only the Evolution III manifestation Chaos. | History, milestone flags, and counters. | Main agent |
| A14 | Evolution persistence | Manifest Evolution II, reduce raw Chaos below 400, and fire again. | The manifested Evolution II form remains active when it is enabled. | Evolution state and counters. | Main agent |
| A15 | Later re-enable | Disable Evolution III at 650, fire, enable it, and fire again. | The first firing uses the highest lower form, and the later firing can manifest Evolution III. | Settings, history, and counters. | Main agent |
| A16 | All eligible countries | Use a world with majors, minors, subjects, civil-war tags, governments in exile, dynamic countries, and special Chaos countries. | Every existing country with an active political leader is processed. | Country coverage report. | Main agent |
| A17 | Non-existing tags | Inspect unused and unspawned tags during a forced firing. | They do not create targets or reports. | Coverage report and log. | Main agent |
| A18 | No active leader | Use an existing country with no active political leader. | The country is counted as skipped and receives no trait application error. | Counters and error log. | Main agent |
| A19 | Human and AI parity | Compare a human country and AI country with the same eligible test pool. | Both use the same distribution and stage count. | Counter dump and probability comparison. | Main agent and probability auditor |
| A20 | AI report suppression | Run an Evolution III world firing with many AI countries. | AI countries receive traits without visible report queues. | Event queue inspection and error log. | Main agent |
| A21 | Human report timing | Leave a human report open while inspecting the leader. | The traits and direct Chaos already exist before acknowledgment. | Leader state and milestone state. | Main agent |
| A22 | Two-player multiplayer | Fire Event 65 in a two-client session. | Both clients observe the same world trait state and receive their own committed result report. | Multiplayer screenshots and checksum or desync log. | Main agent and user |
| A23 | Report independence | Close one multiplayer report and leave the other open. | Neither action changes any trait, global counter, or other player report. | State comparison. | Main agent and user |
| A24 | Existing trait preservation | Give a leader several native traits before firing. | Every original trait remains after Event 65. | Before and after leader inspection. | Main agent |
| A25 | Existing trait collision | Restrict the debug pool so the first proposal is a currently owned trait. | The proposal is rejected and another eligible trait fills the slot. | Collision counter and final traits. | Main agent |
| A26 | Prior Event 65 ledger collision | Grant a source trait through Event 65, remove the visible trait through a test helper, and fire again. | The ledger blocks the same source ID and a different trait is selected. | Ledger dump and final traits. | Main agent |
| A27 | Same-firing collision | Force the same source proposal for two slots. | The second proposal is rejected and does not consume the slot. | Collision counter and final slot list. | Main agent |
| A28 | Distinct stage grants | Use a test pool with at least five unowned entries and force Evolution III. | Five distinct source IDs are accepted. | Stored registry indexes and leader inspection. | Main agent |
| A29 | Near saturation | Use a leader with only two eligible source traits and force Evolution III. | Both remaining traits are added, the actual count is two, and near saturation is reported. | Counters and report render. | Main agent |
| A30 | Full saturation | Use a leader with no eligible source trait. | No trait is added, saturation is counted, and the report does not claim success for that leader. | Counters and report render. | Main agent |
| A31 | World zero result | Create a debug world where every leader is saturated or absent. | No direct Chaos milestone is awarded and the history row records a zero result. | History, counters, and milestone flags. | Main agent |
| A32 | Target invalidation | Invalidate a saved leader role during the debug execution path. | The target is counted as invalidated and does not create a partial slot success. | Counters and error log. | Main agent |
| A33 | Leader after firing | Replace the player leader after Event 65 finishes. | The new leader receives no retroactive trait. | Leader inspection. | Main agent |
| A34 | Leader return | Grant Event 65 traits, remove the leader from office, then restore the same recipient. | The same recipient retains traits and the Event 65 ledger. | Before and after inspection. | Main agent |
| A35 | Separate copied character | Create a separate clone or copied character through a supported test route. | The copy uses a separate ledger unless engine identity proves it is the same role object. | Identity evidence and ledger dump. | Main agent |
| A36 | Shared role identity | Expose the exact same role object through more than one country scope in a test case. | The role receives one stage package, not one package per duplicate exposure. | Role identity evidence and counters. | Main agent |
| A37 | Uniform baseline | Evaluate every eligible source trait in a declared baseline profile. | Each has equal weight before recipient exclusions. | Exact probability evaluation. | Probability auditor |
| A38 | Uniform Evolution I | Evaluate every eligible source trait at Evolution I. | Each has equal weight before recipient exclusions. | Exact probability evaluation. | Probability auditor |
| A39 | Evolution II ratio | Evaluate one ordinary and one featured trait in the same eligible set. | The featured trait has exactly 1.25 times the ordinary entry weight. | Exact probability evaluation. | Probability auditor |
| A40 | Evolution III ratio | Evaluate one ordinary and one featured trait in the same eligible set. | The featured trait has exactly 1.50 times the ordinary entry weight. | Exact probability evaluation. | Probability auditor |
| A41 | Non-stacking featured reasons | Use a trait tagged powerful, rare, and Chaos Redux. | It receives one featured weight and no stacked multiplier. | Manifest and exact probability evaluation. | Probability auditor |
| A42 | Ordinary mass floor | Evaluate every supported content profile at Evolution II and Evolution III. | Ordinary class mass meets the relative floors defined in Part 2. | Probability matrix and rendered comparison. | Probability auditor |
| A43 | Conditional renormalization | Remove several owned traits from the eligible set. | Remaining probabilities equal their weights divided by the remaining total. | Exact probability evaluation. | Probability auditor |
| A44 | Near-saturation fairness | Leave a small mixed ordinary and featured eligible set. | Every remaining trait has positive probability with the correct weight ratio. | Exact evaluation and sweep. | Probability auditor |
| A45 | Direct and cluster parity | Run direct and cluster paths from identical declared state and seed. | Trait mechanics, stage, pool, and accepted results match, apart from source logging. | Event and probability compare artifacts. | Main agent and probability auditor |
| A46 | Registry completeness | Run generator check mode against current vanilla and Chaos Redux roots. | Every final loaded country-leader trait is included once or has an evidence-backed technical exclusion. | Generator report and manifest. | Main agent |
| A47 | Load-order override | Create or identify a trait ID overridden by Chaos Redux. | The final loaded definition appears once and the override chain is recorded. | Manifest row and source comparison. | Main agent |
| A48 | Repeated runtime entry | Inject a duplicate registry branch in a test copy. | Check mode fails and names the duplicate source ID. | Generator test output. | Main agent |
| A49 | New source trait | Add a temporary test trait to a scanned root without regenerating. | Check mode fails because committed outputs are stale. | Generator test output. | Main agent |
| A50 | Stable indexes | Regenerate after adding a new trait whose source order sorts earlier than existing entries. | Existing indexes remain unchanged and the new index appends. | Index-history diff. | Main agent |
| A51 | Retired index | Remove a temporary test trait after it received an index. | Its index becomes retired and is not reused by another source ID. | Index-history diff. | Main agent |
| A52 | Missing source localisation | Use a valid test trait without normal name localisation. | It stays in the pool and the Event 65 report uses a readable fallback, never a raw key. | Manifest and rendered report. | Main agent and localisation auditor |
| A53 | Third-party trait exclusion | Enable an unrelated mod with an extra trait outside declared roots. | The trait is not imported into the promised vanilla and Chaos Redux registry. | Generator source report. | Main agent |
| A54 | No-DLC profile | Build and fire under the supported no-DLC profile. | The active pool contains every loaded valid entry, excludes absent definitions explicitly, and does not error. | Registry report, probability artifact, and game log. | Main agent and probability auditor |
| A55 | Full-DLC profile | Build and fire with the full supported DLC set. | The active pool expands to every loaded valid entry and passes all weight rules. | Registry report, probability artifact, and game log. | Main agent and probability auditor |
| A56 | Chaos Redux source coverage | Add or identify several Chaos Redux country-leader traits. | Every one appears in the registry and receives one featured classification through origin. | Manifest and probability evaluation. | Main agent and probability auditor |
| A57 | Technical failure policy | Use a controlled invalid trait effect in a test copy. | The failure is counted, does not consume a success slot, and does not silently shrink the production pool. | Counter dump and error log. | Main agent |
| A58 | Manifest exclusion visibility | Mark a test source as technically excluded with evidence. | The exclusion appears in the manifest, summary, and completion audit. | Generated docs and audit. | Main agent and completion auditor |
| A59 | Baseline Chaos milestone | Run the first successful baseline manifestation. | Direct Chaos increases by two once. | Before and after Chaos state. | Main agent |
| A60 | Evolution I Chaos milestone | Run the first successful Evolution I manifestation. | Direct Chaos increases by three once. | Before and after Chaos state. | Main agent |
| A61 | Evolution II Chaos milestone | Run the first successful Evolution II manifestation. | Direct Chaos increases by five once. | Before and after Chaos state. | Main agent |
| A62 | Evolution III Chaos milestone | Run the first successful Evolution III manifestation. | Direct Chaos increases by eight once. | Before and after Chaos state. | Main agent |
| A63 | Milestone repeat guard | Fire the same successful form several times. | Its direct manifestation Chaos is awarded only on the first success. | Milestone flags and Chaos history. | Main agent |
| A64 | Bypassed lower milestones | Begin at Evolution III and later alter settings to expose a lower form. | Lower milestones remain bypassed and do not award retroactive Chaos. | Milestone flags and Chaos history. | Main agent |
| A65 | Cluster member metadata | Inspect Randomizations member loading. | Event 65 is optional, Medium danger, and uses the planned 60 percent participation constant. | Cluster inspection. | Main agent |
| A66 | Cluster participation skip | Force the optional roll to skip Event 65. | No traits, Event 65 direct Chaos, or Event 65 history row are created, and the member result records participation skip. | Cluster result and history. | Main agent |
| A67 | Cluster successful member | Force Event 65 participation through the production cluster path. | One global mutation and one member outcome occur. | Cluster result, counters, and history. | Main agent |
| A68 | Cluster ID collision | Reserve cluster ID 9 in a test branch before Event 65 integration. | The implementation collision check blocks reuse and requires a new unused ID. | Collision report. | Main agent and spreadsheet worker |
| A69 | Event history | Run one successful direct firing. | One global Event 65 history row appears with correct date, form, counts, and source. | Event Log render and source evidence. | Main agent |
| A70 | Global actor handling | Inspect the Event 65 history row. | It uses the shared global or no-actor presentation and does not blame a random country. | Event Log render. | Main agent and localisation auditor |
| A71 | Evolution history | Manifest each Evolution through a successful firing. | Each manifested form records once, and threshold eligibility alone records nothing. | Evolution history render and flags. | Main agent |
| A72 | Event Details | Open Event 65 details after implementation. | The panel matches grant counts, complete-pool rule, duplicate redraw, repeat behavior, Evolutions, pool size, and cluster metadata. | Details render. | Main agent and localisation auditor |
| A73 | Player report result list | Give the local leader five accepted traits at Evolution III. | The report shows all five localized names without raw IDs or clipping. | Rendered report at supported scales. | Main agent and localisation auditor |
| A74 | Report grammar | Test zero, one, two, three, and five local grants plus singular and plural global counts. | Every report state uses correct grammar and does not claim a failed grant succeeded. | Rendered report set. | Localisation auditor |
| A75 | Report option safety | Inspect and click the report option. | Only report cleanup occurs and no trait, Chaos, history, or Evolution logic changes. | Event inspection and state comparison. | Main agent |
| A76 | Report asset metadata | Inspect the final runtime DDS. | It is readable, opaque, `210x176`, in the correct path, and linked by the expected sprite. | Asset manifest and metadata. | Asset worker |
| A77 | Report asset render | Open Event 65 in game at supported UI scale. | The image is legible, correctly cropped, and stylistically consistent with report events. | Screenshot evidence. | Asset worker and user |
| A78 | Save and load | Save after a firing and reload. | Traits, ledgers, Evolution state, milestone state, repeat weight, and cluster history persist. | Before and after state dump. | Main agent and user |
| A79 | Registry update migration | Load a test save after adding new source traits and regenerating. | Old indexes retain identity and new traits become eligible without rerolling old grants. | Migration report and save test. | Main agent |
| A80 | Performance ordinary world | Profile a normal 1936-style world at baseline and Evolution III. | Execution is bounded and does not create a sustained stall. | Profiler or reproducible timing evidence. | Main agent |
| A81 | Performance high-tag world | Profile a late-game high-tag world at Evolution III. | Execution remains bounded and avoids visible AI event backlog or multiplayer timeout. | Profiler, queue inspection, and log. | Main agent |
| A82 | Shared-file regression | Run focused tests for every shared event-system and cluster file changed. | Unrelated registered events, logs, settings, and clusters still work. | Regression checklist and artifacts. | Main agent and completion auditor |
| A83 | Workbook source of truth | Inspect the final catalog change history. | The authoritative XLSX was edited and CSV snapshots were exported, not hand-edited as final source. | Workbook diff and export command. | Spreadsheet worker |
| A84 | Cross-surface alignment | Compare source, docs, workbook, event report, Event Details, event log, Evolution history, and cluster UI. | Names, counts, thresholds, weights, status, and cluster data agree. | Alignment report. | Documentation and spreadsheet worker |
| A85 | Improvement loop | Run the Event 65 improvement-loop planner near completion. | An addendum is integrated or a closure handoff records why the design is complete. | Handoff path. | Improvement-loop planner |
| A86 | Completion audit | Run the Event 65 completion auditor after all changes. | The audit returns pass or needs user review with no unresolved source blocker. | Completion audit report. | Completion auditor |
| A87 | User acceptance status | Complete the planned in-game and multiplayer review. | The event remains Needs Testing until the user accepts it, then the user-approved status change is recorded. | User test evidence and status diff. | User |

## Exit rule

Event 65 can move from `To Be Reworked` to `Needs Testing` after all non-user rows pass or have an accepted needs-user-review status.

It can move to `Available` only after the user-owned rows pass.
