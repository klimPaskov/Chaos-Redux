# CBRN takeover status - 2026-10-06

Status: supported source fixes and assigned graphics repairs are reviewed and committed; the CBRN workstream remains incomplete for the accepted requirements and evidence gates listed below.
This is the final handoff of this pass, including recovery after the agent-host restart.
The user owns live-game validation through the orchestrator.

## Commits of this pass

| Commit | Outcome |
| --- | --- |
| `affec7c4e58438610069302272425a8dabe253df` | Rename the three surviving armored-delivery category consumers without changing bonuses, remove 63 orphan sprites and 108 unreferenced tank textures, preserve shared survivors, correct the installed 79-unit roster. |
| `e08c6fadfeca19934617a2fe6a98f13e178f906a` | Restore The Air Is Still Breathable and The Antidote Arrived with real war/state tracking, losses and disqualifiers, reject the inherited weaker wind candidate, shorten wording, preserve shared hunks, and reduce one large atmospheric jump to its highest news notice. |
| `0154ecfd7552c1624bc85730b2b20a23ba4cf680` | Replace four occupation modifiers and the chemical air raid icon with reviewed native-sized glyphs. |
| `a52882984bf676386561c806fe754def5349818f` | Replace five protection modifier scenes with reviewed 32x32 orange/grey glyphs. |
| `1384e2132a049ecc0fa211ec96cba046572080b2` | Replace four ground-raid map scenes with reviewed 32x32 glyphs and remove the orphan Cycle Agent sprite/texture. |
| `f824eaa5217e88f1099aaad3fb37ff4088113795` | Initialize ten consumed temporary helper outputs, add twenty lifetime regression cases and clarify seven decision/achievement strings. |
| `5235dfa23ae8c76241fea5fdd83a3167d3309e86` | Reframe six historical advisor cards from approved masters and preserve the dossier template. |
| `fe0025208e92872edfb5677795b17b1534f3d774` | Prove the idle recording's source, correct the unsupported blanket license claim and document actual country-level selection routing. |
| `1af5699b3be26a8fad48c6786511f10de3f9ef9e` | Give nine agent MIO badges distinct art, recenter the incapacitating payload badge and retire the shared orphan texture. |
| `c9ae7bb592513c77f78bf70cd3e12aefbf733194` | Replace four mastery strips with isolated objects and exact paired grey frames at their actual consumer paths. |
| `38ae4996e662ba98451bdd5774045d811dadfec6` | Replace twenty-one technology textures and give Biowarfare Basics a dedicated icon. |
| `c595ccd47c7d381adc12a3abf817328d1a9a7f1f` | Replace eight biological and mechanical project icons with transparent native-sized blueprint drawings. |
| `dc3c4cd0c007602c453615e3022ddd277d80723e` | Replace four medical projects and the cloning vat, and separate Sarin/Soman research apparatus from bomb art. |
| `afd107c82625b71da5a1d4a532fbe6a5793e89a6` | Preserve immediate civilian-loss and nested attribution outputs on the two achievement paths, extending the regression to twenty-eight cases. |
| `cc5f0e876c0401cb33b22856eecbe0e5dac0c7f4` | Replace eight duplicate/muddy ability icons with distinct native-sized bronze reliefs. |
| `9225f02da2364dfd36a6fc588cbaec42f634a24d` | Repair thirty-one system strings, shorten occupation actions, move state identity into descriptions and bind two displayed percentages to their existing constants. |
| `8450deaf874cfe98f8a9e9586ed1de5b8a79c007` | Repair ten trait medals and wire four distinct agent-ribbon variants through surgical shared-registry repoints. |
| `ec17eb536703b4973b026ee3c43b437f3e4d49e1` | Repair seven remaining decision/doctrine/designer textures and preserve full row/achievement-art evidence. |
| `350a6a451eb21468885b0ec5ac5bdd89778f5c8c` | Require durable pre-call asset requests and per-subject source lineage in the existing asset skill. |
| `1a4af3a4d24c039b42c03ede936882eb1ae01b74` | Finish thirty-one counters/texticons, preserve twenty-six first frames, apply eight texture repoints and the support frame count, and retire eight unreferenced shared textures. |

All commits use the isolated-index/commit-tree/compare-and-swap workflow and the required co-author footer.
The unrelated shared achievement-registry additions and test-country documentation changes remain outside these commits.
The parent reviewed the published source and registry hunks, and checked exact doctrine/unit equality after reversing the category rename.

The exact changed paths and their owning commits are recorded in `subagent_handoffs/2026-10-06_changed_files.json`.
Shared-file entries in that inventory refer only to the published CBRN hunks, not ownership of the rest of each file.
Gameplay surfaces include the achievement registry, CBRN achievement effects/triggers/constants/on-actions, chemical delivery events, contamination/exposure/consequence helpers, cleanup callers, units/tags/subdoctrines and the three narrow ordinary-news guards.
Presentation surfaces include dedicated and surgical shared GFX wiring, owned system localisation, final DDS families and their source/processing handoffs.
Documentation includes the achievements contract, requirement ledger, current system overview, testing evidence, design decisions, catalog-owner note and this status handoff.

## Source outcomes

The takeover's quote-context, scope, engine-read, scaled-rate, sabotage-country-gate, recovery, help, facility-preference, map-read and legacy-unit-removal fixes were re-read by the completion auditor.
They remain present in current source.
The two restored achievements have complete registry, trigger, tracking, localisation and existing icon-triplet wiring.
Protection research alone cannot unlock them.
Nerve containment counts the episode's initial and continuing chemical losses and cannot reset failed losses while contamination remains.
Controller changes invalidate that episode.
New-war relations prevent an earlier chemical attack from qualifying a later major war.
The lower atmospheric news calls are guarded by the next threshold, while every crossed/fired flag remains set.
Hidden maintenance and raid bridges directly produce no report windows, and each defective paid mask batch produces one report.
The shared threshold callback produces at most one ordinary news notice for a single threshold update, with four distinct milestones possible across the campaign.
No new periodic world scan or resource grant was introduced.

Decisions and reasons are recorded in `agent_decisions_2026-10-05.md`.
The mechanics contract is `docs/systems/cbrn_warfare/cbrn_achievements.md`.
The requirement ledger and current overview state thirteen active achievements and the two still-blocked accepted requirements.
The inherited BOM-only request placeholder was explicitly reviewed and removed.
The real October 3 startup-error artifact was retained as historical evidence, not current service health.
No workbook or exported CSV was edited.
Thirty-one system strings, including a standalone facility report description, receive plain prose, compact titles or dynamic percentage display.
The catalogue owner has a precise pending wording review in `catalog_changes_pending.md`, with all before/after values in the prose handoff JSON; no row is inferred from a stale CSV.

## Meaningful validation

The existing source suites pass 106 sabotage, 21 immediate-protection and 46 occupied/export cases.
The occupied suite's local parser was corrected to accept native bare advisor-token lists without changing the shared Event 026 VM.
Ten atmospheric boundary cases bind the actual next-threshold guards to the intended highest-notice behavior.
The report-colour audit reports zero reached coloured keys for the owned CBRN, biological, chemical and CBW report families.
The final prescribed audit also reports zero coloured keys after the facility-report prose change.
These are source checks, not native payment or combat proof.
The twenty-eight actual-source helper-output cases reproduce twenty-one faults with the old caller storage and pass with the corrected source.
They test class, air, nested attribution, immediate-loss arithmetic fragments and caller storage around cleanup, not full native contamination, loss caps or combat execution.

HOI4 routes are absent from the parent's tool inventory but exposed in specialist sessions.
Their reference and source routes returned installed-game and offline-wiki sections with exact revisions.
The direct event trace covers 59 roots and 189 nodes, without trace truncation, while helper/lifecycle coverage remains partial.
Event comparison returned graph-artifact-invalid and revision-not-cached errors.
Whole-file and scoped script validation remain partial with `valid = null`, unresolved helper/binding coverage and unchecked argument blocks.
The two doctrine files are an unsupported validator family with zero checked commands.
Supplemental lifetime-fix validation likewise returned partial results, without invalid findings but with unresolved argument blocks.
Final consequence validation checked 392 commands with zero findings, but retains nine unknown-scope roots and 259 unchecked argument blocks.
The adversarial source review found the two additional consumed outputs above and closed those concrete findings after repair; it found no remaining introduced impossible achievement gate or lost shared hunk.
Probability inspection returned bounded candidate inventories and twelve reconciliation rows, all with unresolved eligibility inputs.
The equal raw reconciliation scores of six are source scores, not measured click probabilities.
Timed aid/shortage/sale scenarios did not complete; native raid AI has no supported probability adapter.
No AI coefficient was changed on that evidence.
The technology worker's final focused inspection and asset render both returned `Transport closed`; current source references and parent art review do not replace that missing MCP result.

The current zero-capacity plague board was rendered and reviewed in full/cropped/annotated views without overlap or clipping.
The five-state, two-resolution baseline comparison timed out after 600 seconds without an artifact or task handle.
No full GUI acceptance or confirmed historical UI-worker routing is claimed.
Evidence is in `subagent_handoffs/2026-10-06_completion_audit.md` and its JSON manifest.

## Graphics review

Fourteen glyph textures are reviewed and committed in the three graphics tranches above.
Twenty-one painted technology replacements, nine distinct agent MIO badges, the recentered air-payload badge, eight blueprint projects and four mastery reward strips are reviewed and committed.
The mastery strips reproduce twenty isolated objects and their exact grey counterparts, with the existing medallion frame visible.
The parent caught unconsumed prefixed export paths and a detached antenna fragment before publication; final exports use the four actual consumer paths and the fragment is removed.
The six historical advisor cards are reviewed and committed, using already-approved masters with bounded crop/lighting corrections and the exact dossier-paper template.
Seven medical/program/cloning projects and eight ability reliefs are also reviewed and committed.
All ten trait medals and seven smaller repairs are reviewed, wired and committed.
The thirty-one counter/texticon outputs are reviewed, wired and committed, including the twenty-six exact first frames, reconnaissance large/map frames, flat instruments and the compact two-frame support-equipment icon.
All thirty-one DDS outputs decode exactly to their processed PNGs, with matching target dimensions, and all twenty-six accepted first-frame snapshots match after DDS decoding.
Seven hand-authored candidate pictograms were rejected after the source-lineage check and are retained only as evidence.
Host-restart recovery found eight final subject/layer requests missing, including the infantry X; fresh native-alpha ImageGen edits preserve their intended designs with exact requests saved before each call.
The final skull preserves source-derived eye/nose openings and keeps the infantry X behind them.
Eight old shared tank/category texticons are retired only after their eight consumers are repointed and engine-source searches find no remaining reference.
The primary handoff maps every assigned primary owner-table row, with fourteen earlier glyphs and forty-four later textures distinguished from the separate portrait, technology, trait and counter packages.
All thirteen registered achievement triplets are inspected and retained, while the two unsupported triplets remain unregistered.
Generated sources and review evidence remain under `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/` and `2026-10-06_gfx_tech_counters/` while these packages are active.
The separate trait evidence workspace is `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/`.
No grounded portrait generation or RunPod operation is authorized or performed by the agent.

## Simplifications, omissions, and blockers

No weaker achievement substitute or accepted removal has been inferred.
No Wind Is Friendly remains blocked because exact forecast failure and recovery of the affected army are unproved.
Unbroken Supply Corridor remains blocked because exact assigned-army supply and linked offensive-objective proof are unavailable.
The rejected wind candidate is preserved as evidence under the handoffs folder and is not loaded by the game.

The battalion idle breath has been matched exactly to the archived primbal source at 275,796 mono 44,100Hz samples, gain one and zero residual.
The provenance specialist could not establish an original-to-derived source/license crosswalk for the other eight shipped sounds.
The shipped audio and animation timing remain intact, without an arbitrary recovery-set swap.
Country-level infantry selection routes do not provide a distinct battalion selection voice when ordinary and CBRN infantry share that country.
That native consumer limit is documented without replacing the shipped recordings or claiming animation events solve selection.

The troop technology replacement contains no baked Roman numeral, following the user's direct no-text requirement over the graphics plan's suggested numeral.
The native title/year supplies tier identification.
Equipment and raid aliases retain their declared shared technology texture paths; wide native equipment-card presentation still needs consumer review.

Native raid reservation/refund ownership, displayed-versus-deducted costs, genuine blocked refunds, CXT facility construction, combined division statistics, contamination map colours and full board/decision presentation remain native acceptance gates.
These limits prevent a workstream-complete verdict.

## Baseline save and orchestrator checks

The read-only save inspector confirms `qa_001_fresh_head.hoi4` is HOI4txt, USA, 1936.1.1.12, version Operation Postern 1.19.2.0.a729.
USA has `cbrn_achievement_start_country_eligible`, policy 2 and military respiratory protection 55.
Its global flags contain neither the ordinary atmospheric news-fired flags nor the queried Fallout terminal/disabled flags.
The save was not modified or copied into Git.

1. From the baseline, open Warfare Help and Civil Defence.
Check the three policies, dynamic prices/durations, readable cost rows and shortened audit action names.
Research or doctrine selection alone must leave both restored achievements locked.

2. Use `e chaosx_test`, advance at least one hour, then use the Test Directorate's player-triggered resource, equipment, research and package actions as needed.
Inspect both facilities, the three armored-delivery roles and their category label, the surviving support roster, both CBRN research folders and doctrine branches.
Expect no removed chemical-tank company or obsolete category label.
Verify last-card scroll reach, art, native card sizes, colour/grey mastery states and combined division-stat caps.
The facility trace is still guarded and must be retired together with its caller only after the native construction outcome is resolved.

3. Prepare one cylinder, projector, artillery and armored chemical raid, plus one biological raid in its proper category, with legal origin supply, intelligence and assigned divisions.
Measure real payload stock before preparation, after reservation, launch, cancellation and resolution.
Repeat target loss, war end, shortage and sale-expiry cases.
Expect one payment, at most one return of unused payload, no uncharged strike and no duplicate credit.

4. Exercise occupied distribution, export, emergency distribution, hospitals/utilities, protective aid, inspection/diplomacy and theater cleanup.
For ordinary and discounted variants, compare displayed costs to actual resources removed.
Shortage must block selection without a partial order.
A selected discounted commitment must remain owned after its sale ends.
Drive a real refused refund through each audit decision.
Expect one retry, write-off only of refused supplies/unconfirmed fee, retained delivered protection and reopened routes.

5. For The Air Is Still Breathable, use an eligible campaign-start country, raise real military protection to at least 75%, receive confirmed enemy chemical use during an active major war, retain protection, and remain standing when its marked major opponent capitulates.
Expect unlock only with low own chemical contribution and no offensive first use, civilian strategic use or doomsday use.
An earlier peacetime attack, an unrelated later war, unprotected exposure or country switching must not manufacture eligibility.

6. For The Antidote Arrived, issue advanced/sealed masks to both soldiers and civilians, receive nerve-agent exposure with at least 75% effective protection, and let the same state reach Severe or Catastrophic contamination.
Provide real medical care and cleanup, retain control, and reach zero contamination with civilian deaths below 1,000 and summed military loss below one percent.
Expect one unlock without an extra report.
Repeat exactly-at-loss-limit, underprotected repeated attack, continuing-death, failed-episode reset, control-loss and research-only cases.
Expect no false unlock.

7. In a disposable baseline branch, run this exact country-scope probe:

```text
e clr_global_flag = air_contamination_news_25_fired clr_global_flag = air_contamination_news_50_fired clr_global_flag = air_contamination_news_75_fired clr_global_flag = air_contamination_news_100_fired set_variable = { global.air_contamination_bp = 10000 } air_contamination_refresh_values = yes air_contamination_update_threshold_flags = yes
```

Expect one highest-threshold news notice, all four threshold/fired flags set, and no repeat on another call.
Call `e air_contamination_update_threshold_flags = yes` again while the clock remains paused to check the repeat guard before advancing time.
The terminal total also sets `air_contamination_irreversible`; existing Fallout intake may subsequently respond, so count ordinary threshold notices separately from its terminal presentation.
Ordinary 25%, 50% and 75% isolated crossings should each produce their appropriate first notice.
Use separate disposable baseline branches for those totals, substituting 2500, 5000 or 7500 in the same probe.
Refreshing values before the callback keeps the news description synchronized with the measured total.

8. Inspect the plague response category in pre-outbreak hidden, active unorganized, active organized, exhausted capacity and recovered/no-response states at 1920x1080 and 2560x1440, UI scale one.
Expect mutually exclusive capacity labels, the warning only when positive total capacity is fully committed, no overflow, clipping or overlap, and no category before a real outbreak.
The current zero-capacity MCP render does not prove the other states or ordinary decision-cost rows.

9. After a Fallout sweep, inspect Contamination map mode and its tooltip, then comparable chemical and biological states.
Expect live hazard colours even after the nuclear marker has been intentionally removed.
Inspect the repaired state icons, raid markers, technology art, doctrine medallions, advisor cards and inline/NATO counter frames in their actual consumers.
Check unit idle, movement, attack and death cue synchronization without changing the shipped audio set.
On limited biological-facility recovery and destruction outcomes, confirm the nominal tooltips show 40% and 50% from their respective constants, without a raw token.
Inspect the shortened occupation actions and their descriptions, confirming that the selected state's name is present and their availability/costs remain unchanged.

10. Exercise real state cleanup at serious, severe and catastrophic contamination, through both a theater assignment and an international cleanup mission.
Compare the reduction to the current displayed/constant-derived amount and confirm the state class, modifier and global Air Cleanliness contribution change together.
Run the explicit Settings contribution rebuild once on that disposable branch and verify it agrees with the state contributions without another news notice.
For immediate nerve releases, compare actual civilian losses with the episode counter and verify confirmed evidence reaches the current chemical-war gate.
The twenty-eight helper-frame tests cover storage/fragments, so these native outcomes remain separate acceptance checks.

## Skills and routing

Used events, decisions/missions, event-assets, subagents, save-inspection and shared-git-commit guidance.
The asset workers apply native ImageGen and canonical consumer references, and the portrait worker owns all portrait corrections.
The audio worker applies the 3D-pipeline sound/provenance contract.
The auditors apply scripted-GUI and MTTH/probability guidance, and the visual workers apply the official ImageGen skill.
The existing event-assets skill was updated through the skill maintainer with a generic pre-call request and subject-lineage rule after restart recovery exposed missing historical prompts.
The official skill validator passed in UTF-8 mode; this validates skill packaging, not future asset behavior or engine acceptance.
No event-specific material or provider/portrait authorization was added to the skill.
