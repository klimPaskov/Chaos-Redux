# Legacy dismantlement cutover: custody and payment handoff

Disposition: implemented in package-owned source, with engine acceptance unresolved; the external UWR caller has a separate source receipt handoff and unresolved native acceptance.
Acceptance basis: the user's approved administration contract and instruction to reconcile legacy decisions and missions while preserving exact finite custody.

## Scope and source behavior

The generic selected-site action, German Auschwitz order, Japanese experimental-site shutdown, Soviet Gulag closure, and British, American, French, Italian and Belgian colonial orders now check their actual selected sites before any source-level resource debit or timed mission start.
The country orders share their availability and execution readiness predicates, and the paid national orders use the same site collectors at start and completion.
An empty colonial network can still take a national sunset action, while any responsible active site outside current actor or subject control blocks the payment.
French inherited-site selection recognizes the existing legacy, North African and other colonial pools independent of current controller, then requires actor or subject control; the collector uses that same predicate from the registered site array.

The shared site start helper refuses an initialized site with closed status, invalid authority or inconsistent aligned custody rows.
The shared completion helper returns `camp_rework_dismantlement_completion_accepted = 0` until an actual eligible site has passed the guarded release and destructive cleanup.
For an initialized voluntarily closed site, completion requires zero living detainees; a closed site with reconciled live rows cannot bypass release by entering the dismantlement path.
Enemy liberation retains its distinct closure path and must still reconcile rows before the event option appears.
The base site closure and integration history wrapper now require reconciled rows before marking closure, releasing survivors or writing a closure history entry.
The older genocide-crisis liberation reward and public report are conditional on the accepted completion receipt.
The discovery option now excludes already closed and dismantled sites and requires valid rows for initialized sites.
Its effect rechecks the same war, control, site and row trigger at execution, so a popup left open through a control or war change cannot demolish the site or grant rewards.
The enemy-completion branch separately requires current actor control of an open site, and the temporary liberation marker is cleared before later effects in that chain.

Country mission outcomes and relief or reform rewards require valid completion receipts, so a site that becomes unavailable after the paid start does not certify a successful closure.
The colonial bulk helper preflights all selected sites and checks each completion receipt before the five country callbacks grant success.
French legacy closure writes dismantled markers and evidence resolution only after that receipt.
The bulk completion helpers also recheck every responsible active site, including those no longer collected because control changed after the paid start; a French legacy timer cannot convert that omission into a successful national closure.

The USA `usa_security_authority_sunset` mission is explicitly removed when a civil administration review supersedes emergency relocation, whether that review starts from the player action or the automatic monthly branch.
The package-owned cancellation helper clears the emergency authority flags without running the mission's success or failure outcome; the mission also cancels if its authority disappears or the country becomes a special Chaos actor.
Annexation and special-country terminal cleanup invoke the same helper and remove outstanding USA court-review and redress missions before site closure.
The timeout outcome itself now requires active emergency authority, no termination flag, no civil review and a nonspecial country, so a stale callback cannot award or punish the superseded route.
The 33rd restricted civil scenario checks both civil callers, both terminal callers, the mission backstop and the guarded timeout wrapper; the engine's exact cancellation timing remains unproved.
The [matched USA sunset probability audit](ai_evidence/usa_sunset_terminal_probability_2026-09-27.md) finds unchanged zero AI willingness in a complete same-file 25-mission pool and five bounded fixtures; its score-only adapter cannot model an already active mission's cancellation or timeout.
Current raw source hashes for that USA terminal correction are `a7a2956cdfc612bfa60b6b18207f3de7e02487835b9a45fa031de727b89527ab` for the colonial decisions, `114b1f55c93974a0a9cb2d2864c7996f9bc74da4642902fd28f4ce133926ab01` for the colonial effects, `2154fa8740ca35dd0ec7b9e69af0eaf9cb4aee98b722772c997b1c4b2d980163` for the civil effects and `31d7e6165709fbdb101553addb087ac694086753f319d7559d92c99f609d39e2` for the integration effects.
The prior decision source was reconstructed by removing only the added mission `cancel_trigger` line from the current file; its hash `300054da1fd1902a1205daadde588161caec9ebe302ba861455d0013e37cbc0b` matches the independently recorded pre-edit decision hash, and the copy is archived at `ai_evidence/usa_sunset_mission_before_terminal_cancel_2026-09-27.txt`.
Installed `documentation/effects_documentation.md` lines 6083–6090, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, states that `remove_mission` skips complete and timeout effects; installed `documentation/triggers_documentation.md` lines 3022–3028, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, documents `has_active_mission`.
The offline `Decision modding` Missions section lines 464–479, SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, covers mission timeouts and cancellation; installed vanilla `common/decisions/ENG.txt` lines 4294–4303, SHA-256 `83351419122bbc4f4a7fa693dbe7658396c1781b5aea28b5d100a0dd3b8d1fef`, removes an active mission from a decision effect.

## Verification and limits

The restricted source evaluator in `foundation_source_tests.py` passes 34 scenario groups, including an inconsistent 10-thousand/9-thousand custody row, a closed site with live survivors, a genuine zero-custody completion, enemy liberation option and execution rejection after invalid custody, closure, lost control or ended war, a zero-site colonial sunset, foreign-controlled and invalid-row British/French starts, twelve discovered-site report-selector cases, a first-release/physical-retry case, exact-cost acceptance for seven fixed-price closure decisions, the native selected-site closure's exclusive locked/active states, monthly mission-cancel isolation and the site timer grace.
`major_countries_source_tests.py` passes 14 groups, `civil_scenarios.py` passes 33 scenarios, the dispatch calendar model passes, and occupation unit tests pass 63 cases.
These execute selected production helpers with mocked engine primitives and do not prove live Clausewitz transaction or event execution.

The HOI4 MCP `chaosx_genocide.50` trace returned `EVENT_INSPECTED_PARTIAL` at revision `c1123483b63f502da6970c2d0d7e8c1029e4d95d23f235c69562c495612558e1`, with zero blocking diagnostics and no helper expansion.
The option render returned `EVENT_RENDERED_PARTIAL` at the same revision, PNG SHA256 `576458aa9fc8e2e94eec462609b7fa6c1639fee3a53689c39d3b9bf154761a10`.
These views recognize the event option but cannot prove its runtime custody guard or click effect.
The attempted full `hoi4.event_inspect` state-flow expansion for `chaosx_genocide.56` timed out after 180 seconds; the focused event view remains event-only with `helpers=0`, so helper execution is not MCP-verified.
`hoi4.map_inspect` returned `MAP_INSPECTED` for the state-88 and state-328 report anchors at revision `d78da5300e3f020c8b2f2a82a6f0323e308bdaceed61586df30825379f5a03d2`, with two selected states and no unknown province ids; [map artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1db89a96f6acddb28ed0a1e5e1baf5e46cd632c94249f9498cf7cf252aaa95a7/45e327bc7ceb30649255df4012dbf6e467dc034e16b35504559549ec7ced5a99/map-inspect.d78da5300e3f020c.json).
The map catalog does not prove any dated controller, institution flag or event firing.
The retained pre-administration discovery option can dismantle a camp building before a finite administration site and its custody rows exist; no finite survivor release or Administration Records liberation row can be proved for that branch.
The same pre-administration allowance exists in the shared legacy dismantlement start and completion triggers, so older paid or timed site closures also lack a finite custody release receipt unless their site has entered administration.
Its tooltip therefore promises release only for recorded survivors, and its option label promises dismantlement and record security, while the old crisis choice remains available.
Because event option visibility is fixed when the popup appears, selecting a liberation option after its war, control or custody gate changes is safely a no-op; publicizing the report instead would be an unapproved alternative action and remains unresolved.
All nine `chaosx_genocide.50` through `.58` report sprites resolve to installed DDS files, and their titles and descriptions resolve in the English localisation.
The `.52`, `.53` and `.55` descriptions describe records and investigation without asserting troop capture, because the same event ids can fire from domestic exposure without a discovered-state target.
The discovered-state dispatcher now chooses the named Auschwitz report only for state 88 with its laboratory/experiment marker, Pingfang only for state 328 with its biowarfare institution marker, Raj only for RAJ/PAK/BAN cores, Libya only for an LBA core, and Congo only for a COG core or its explicit concession-pool marker.
All other sites use the generic camp-records report, and domestic British, Italian and Belgian exposure without a discovered-state target also uses that generic report.
The existing first-discovery flag still limits each responsible country to one discoverer report, so a generic first discovery can preclude a later named-site report; this preserves the requested minimal-notification pattern but is not a complete per-site news history.

The final three-candidate GER/JAP/SOV `decision_ai_will_do` inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, revision `599f26622a1a1c180ea5e696aa7265ff52497f70a5f48786a9d6fb02e062b782`.
The four-scenario raw-score evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, 12 candidate rows and 11 unresolved items, scenario hash `21f01bb8b97bc33b31f57d8d964bb64ade9d765b0ef1c2839048593e3bb88321`.
The six-candidate colonial inspect at revision `920c04b2283c22cc812ecc5407b5718ed8c471a12af0a067aa306079e66298e8` returned `poolComplete=false`, four candidates and two unresolved ids.
Its four-scenario raw-score evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, 16 candidate rows and 18 unresolved items, scenario hash `f45cf6abec535a676a50abb49e217686c208195f7001032ba6cb15e4fa126623`.
Neither result supports exact AI choice probabilities or engine eligibility claims.

## External caller follow-up

`common/scripted_effects/005_soviet_collapse_effects.txt` contains a Soviet-collapse UWR aftermath caller around line 21967 that removes other package facilities and awards aftermath state around `camp_rework_complete_dismantlement`.
The bounded Event 005 caller was subsequently edited under the user's cross-package reconciliation request. Its current camp-obligation predicate covers a living ordinary concentration or Gulag camp co-located with UWR facilities as well as a marked experiment camp, requires accepted closure before facility/flag/stability effects, and refunds a rejected or stale native cost. Focused source cases cover valid and invalid living rows and a closed-empty facility-only case; the [receipt handoff](uwr_aftermath_receipt_handoff_2026-09-27.md) records the current code and limits. Native tooltip, click and physical survivor release remain unproved. The pre-administration zero-custody exception is a separate pending user choice in [the custody disposition](pre_administration_custody_disposition_2026-09-27.md).

The Soviet famine relief shortfall branch remains a pending user decision in `soviet_famine_relief_shortfall_proposal_2026-09-26.md`.
The legacy French `days_remove` closure has no cancellation callback, but its completion effect now calls the package-owned active-attempt cleanup after success or failure. A persistent finite custody receipt allows physical dismantlement to be rearmed after control returns without a second survivor release. The same cleanup is called by the five other country callbacks; engine timing and click/payment evidence remain unresolved.
The generic selected-site paid dismantlement dispatcher and mission subsequently gained a fourth native Locations action. Its five locked states, three-scale button/scroll images and click-region evidence are recorded in `mcp/locations_dismantle_native_2026-09-27.md`; actual tooltip/click/debit/mission execution remains unproved.
There is no package commit while native transaction evidence, dated historical calibration and the remaining attribution and pre-administration policies are unresolved.
