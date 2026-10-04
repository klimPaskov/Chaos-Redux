# Camps, forced labor and repression implementation execution

Disposition: unresolved until the acceptance evidence below is complete.
Acceptance basis: the user's instruction to implement the complete rework, using `accepted_implementation.md` as the design baseline.
This document is the implementation plan and a live gap record; current source changes and source-only tests do not establish full completion.

## Scope and boundaries

The package owns its administration variables, site registry, occupation receipts, country modules, decisions, native ledger window, localization, icons and documentation.
It calls existing Chaos Redux APIs for territorial losses, exact civilian accounting, event presentation and country context, but does not edit their shared definitions.
The monthly processor remains bounded to registered countries and sites; no new recurring world iteration is authorized.
The user approved a package-owned delayed country timer on 2026-09-26 for the Chaos Meter disabled setting.
The timer calls the existing month-guarded recipient for each eligible registered country and stops after exclusion; its source contract is documented in `docs/camp_administration_dispatch.md`.
The user also chose an explicit paid German exact-cohort transfer after cutover on 2026-09-26.
The decision must use an identified living occupation row, measure one source debit and destination credit, bind state-88 custody, then pay and record consequences only after the exact receipt succeeds.
The old whole-state-population request cannot remain callable from this decision; the separate dated Łódź automatic path stays intact.
The user subsequently chose one national transfer order using the oldest eligible registered source rather than separate map-target entries; the bounded selector and dynamic source name are package-owned.
Detention, forced labor, penal labor and killing centers keep distinct roles, eligibility, output and consequences.
No protected-group selector, casualty reward, technical weapon procedure, or agent-run live game test is in scope.

## Source and acceptance order

1. Audit the existing package by identifier against the accepted contract, offline wiki, installed vanilla documentation and vanilla precedents.
2. Inspect populated vanilla country decisions and occupation windows with the HOI4 MCP, then render the current Administration, Locations and Records routes with explicit country, date, values and mutually valid panel states.
3. Archive four clean reference images for Administration, Locations, Records and material shortage, with render provenance and an image-region to native-element map.
4. Implement the native 900×540 ledger window from those references, with each tab, label, value, row, selection mark, contextual action, hover, tooltip and state independently wired.
5. Reconcile one automatic monthly policy and payment processor, the finite local workforce and occupation ledgers, country authority, economic output and bounded institutional awards.
6. Reconcile legacy decision and mission identifiers with administration; retire duplicated purchases and routine timers after migration and retain explicit authority, inspection, evidence, crisis, closure, review and redress choices.
7. Run source scenarios, historical control scenarios, MCP domain inspections and image-level GUI comparisons before scoped audits and a package-only diff review.
8. Commit only a complete, coherent package plan; an incomplete evidence or movement requirement remains an explicit blocker, not a completion claim.

## Native interface contract

The entry point and consumer remain `repression_ledger_window` in the existing decision category, at 900×540.
Administration exposes national priority, mandate, spending ceiling, reserves, monthly operating result, one economic slot and one institutional slot.
Locations exposes the complete filtered registry, a selected site, its custody role, surviving and assigned people, capacity and support, and only actions valid for that site.
Records exposes separate native rows and values for death causes, original responsible authority, site and territorial losses, evidence, review and long-term institutional history.
The source must not pack independent values into one synthetic text element or use a single image as a button, list or state.
Actions show the current quote, requirements, blocking reason and consequences in the hover tooltip; routine maintenance has no confirmation event or recurring notification.
Material crisis, exposure, reform and aftermath may use a notification if it carries a player decision or lasting consequence.
The 1280×720, 1920×1080 and 125% fixtures must cover normal, hovered, selected, disabled, shortage, empty/full registry, long name, large number and scroll boundary states; each rendered image and click region must be checked and repaired.

## Administration and economy contract

The national priority, mandate and spending ceiling commit a monthly allowance before optional work.
Maintenance is paid first from protected reserves; the economic and institutional slots then compete for the remainder without duplicate debit.
Work requires surviving, supported, exclusively assigned people and matching state opportunity.
The developed ceilings are 40% of participating industry, 25% national industry, 40% relevant construction and 40% local extraction until a named scenario supports a central tuning change.
The economic slot may complete durable infrastructure without deleting it on reform or capture.
The institutional slot requires continuing payment, valid authority, records and a qualifying site; completion awards a one-use 50–100% bonus in an eligible research category, no category stacking and at most two awards per calendar year.
Deaths do not advance either slot or award research.
Source scenarios must test zero/small/developed/overstretched staffing, reserve exhaustion, interruption, duplicate payment, completion and a stable twelve-month pulse.

## Population, movement and responsibility contract

Every admitted person comes from a finite measured cohort.
An accepted death has exactly one physical population debit and one shared records receipt at the actual location, with cause and responsible authority preserved.
Survivor release or reform retires custody in place and never credits population or restores deaths.
Cross-state movement requires a separately identified origin cohort, one measured origin debit and destination credit for living people, a conservation receipt, and immutable original authority before the destination can record a later death.
The accepted design requires aligned authority-owned occupation rows so two original cohorts can share a destination without losing provenance.
The current source has those aligned rows, an occupation-to-occupation physical helper, origin-tagged custody rows, and exact state-88 custody preflight/bind/inverse helpers (`occupation/cross_state_movement_handoff.md` and `occupation/custody_origin_rows_handoff.md`). It also has `camp_occ_transfer_to_custody_exact` and the dated `camp_occ_try_lodz_auschwitz_transfer` caller inside `camp_occ_monthly_country`. The generic helper still ends in an occupation row and has no named caller; the custody path has no engine receipt/rollback or dated control proof.
Do not use the shared migration transfer API without its required cohort and reception proof, and do not infer casualties from a quota or edit shared Chaos Meter accounting.
Movement scenarios must test partial transfer, two origins at one destination, destination death, stale authority, insufficient headroom, partial credit and rollback, capture, annexation and release.

## Country and historical contract

Germany needs SS authority, occupied-territory campaign intake, distinct killing-center escalation and an Auschwitz/Mengele gate no earlier than 1943-05-30.
The historical control spans the wider Holocaust, including murder outside killing centers; the six-million benchmark is an external comparison, not an intake or death target.
Japan needs occupied-China labor, a Pingfang institution, army review, outbreak and evidence risks; combined Chinese occupation losses stay separate from institutional deaths.
The USSR needs Gulag and penal labor, paranoia, famine pressure and a finite survivor release with no manpower creation.
Britain needs domestic internment distinct from Raj detention and labor, with Raj autonomy and negotiated release; USA, France/Vichy, Italy and Belgium/Congo retain their distinct reviewed routes.
Chronology and cause calibration use the linked historical archives in the accepted contract and record model totals, source range, differences and attribution by dated control scenario.
Unrealistic state control, unavailable route gates or invented population cannot be used to produce a visually attractive historical figure.

## Decision, mission and AI cutover

The identifier inventory covers 84 legacy actions and 41 missions across `camp_repression_generic_decisions.txt`, `camp_repression_major_country_decisions.txt`, `camp_repression_colonial_country_decisions.txt` and `genocide_crisis_decisions.txt`, plus the newer administration decisions.
For each identifier, record whether it is retired on `camp_admin_initialized`, retained as an explicit choice, replaced by a bounded helper, or unresolved; inspect both availability and its effect and mission cancellation path.
Country migration cancels only routine missions with their cleanup helper; review, court, evidence, crisis, redress and closure timers retain their completion effects.
GUI and AI actions call the same trigger, quote, debit and effect helper so an automatic choice cannot evade cost or authority checks.
Every touched `ai_will_do`, mission score, focus or research selection and weighted pool requires a pre-edit `probability_inspect`, named GER/JAP/SOV/ENG–Raj and invalid-target scenarios, a sweep, then a matched `probability_compare` after the owner patch.
The generic decision adapter reports an incomplete pool, so its score output cannot be called an exact selection probability.

## Verification and audit gates

The source evaluators are useful for finite cohort, payment and date logic, but they are not HOI4 runtime or live-game evidence.
The mandatory MCP coverage is event inspection and rendering for the bounded monthly event and consequences, technology inspection for award categories, map inspection for approved movement endpoints, focus inspection for touched focus hooks, probability inspection/evaluation/sweep/comparison for weighted decisions, and GUI inspect/render/compare for the final layouts.
Capture source revision, scenario, fixture inputs, coverage status, artifact URI and unresolved findings for each route.
Run scoped decision/mission, country, localization, event-completion and AI probability audits after the final source edit, then review the package-only diff and all four reference/provenance artifacts.
Update the accepted spec and package documentation with implementation evidence and limitations; update the event catalog workbook only if player-facing event facts change, then export its CSVs with the repo tool.
The completion report names files, balance scenarios, visuals, assets, country routes, audit outcomes and every simplification or blocker.

## Current implementation evidence and unresolved gates

The country institution processor now makes payment a prerequisite for completion and pauses for a category or annual award limit; source scenarios exercise those conditions.
The Soviet wartime industry award now checks its actual `industry` bonus category during the monthly payment gate; a focused source scenario checks that a held industry bonus pauses work while an unrelated engineers bonus does not.
Germany's three legacy experiment ideas no longer grant continuous special-project or biowarfare-facility speed, so the paid, bounded program is the source of research bonuses; their remaining political, stability and military effects still need scenario review.
The German dated census now uses cumulative intake, a fully released site closes automatic intake, and a site with a killing role cannot refill through the ordinary camp census; source scenarios exercise finite release and the role gate. A detention site can still admit before a separately paid role conversion, so dated transfer capacity depends on the actual surviving site population.
The state-88 Kraków-area detention setup is implemented in source as a one-time post-cutover GER decision and guarded AI monthly call, with Nazi wartime authority, 1943-05-30 or later, current control, an empty site/authority slot, development spending and a separately checked 25 PP debit.
It registers only a base detention site and a `site_established` history row; AI can raise development spending for this context when its budget rules permit. The guarded monthly source calls paid radical mandate, detention setup and paid Locations killing-role conversion in that order, with later retries when an earlier gate fails.
The decision reuses `GFX_decision_germany_ss_camp_administration` from `interface/camp_repression_rework.gfx` and its existing DDS under `gfx/interface/camp_repression/icons/`; no new art or independent provenance is claimed.
The registered-country package now has its own hidden 28-day timer, which calls the same month-guarded recipient even when Chaos Meter is disabled; source/calendar tests cover that path, while engine scheduling remains unproved.
The setup is an implemented source bridge, not engine acceptance of the state-88 killing role, a route-valid 1944 occupation-to-custody transfer, or Holocaust-scale historical calibration.
The legacy cutover gates six generic, seventeen major and thirteen colonial routine purchases after initialization, cancels six major and seven colonial routine missions, and retains explicit crisis, evidence, review, release and redress choices; the separate generic retirement brings routine mission removals to fifteen. All fifteen retired mission cancellation effects have an initialized-country guard, including the two generic completion callbacks, so removal cannot award their legacy completion outcome even if the engine invokes cancellation. The major cleanup clears German project, Japanese bureau and Soviet cycle markers without calling the legacy cancel helpers that could levy policy penalties or grant relief. The eight genocide-crisis identifiers have dispositions: six replaced after cutover, Soviet food confiscation retained as a distinct famine crisis, and the German transfer retained as a post-administration paid exact-cohort choice under the user's 2026-09-26 decision. The old pre-initialization whole-state transfer is retired. The matched AI comparison remains open.
The old four-slot Ledger execute effects have no direct caller in the current common, interface or event sources; their shared prepared-action helper nevertheless rejects execution once administration is initialized, preventing a future stale caller from bypassing the retirement guards.
The Soviet finite census replaces the old deportation registration action, while the famine-pressure choice still needs an administration-native equivalent before its legacy decision can be retired without erasing that route.
The occupation ledger has aligned authority-owned cohort rows, immutable original-state provenance, a guarded survivor-transfer helper, and actual-location later-death attribution. The foundation tracks origin-tagged site custody rows for local admissions and imported survivors, with exact destination preflight/bind/inverse helpers and row-aware death/release consumption. The dated Łódź caller uses the separate occupation-to-custody transaction, not the generic occupation-to-occupation helper. It reserves one proven living state-87 row in the August–September 1944 window when GER controls states 87 and 88 and the destination has a supported operational killing role; its once-only flag prevents a second reservation, while a pending remainder may continue into September. At most twelve monthly waves are bounded by the live row, paid undamaged throughput and resident/share headroom, with pending and throughput reduced only after exact receipts. A valid destination bind can request measured arrival-phase violence against the bound custody row; the month receives one history summary if any wave commits. The optional Mengele experiment marker is not a preflight or bind requirement. Successful commit clears `camp_admin_import_bind_pending_inverse`. Natural 1944 availability of the killing role and site support, engine receipt/rollback, and dated control remain unverified. The historical benchmark in `occupation/historical_benchmark_2026-09-25.md` shows that the restricted wider German envelope remains about 3.64 million below six million; the separate dated source-control sensitivity is not an engine scenario.
Four clean HOI4-style Administration, Locations, Records and material-shortage reference PNGs are archived with hashes, synthetic-fixture provenance and native-element mapping under `references/`.
The native GUI source now splits summary, program, site, cause, history and shortage fields into independently named text elements, keeps rows and buttons native, and removes selected-mark click interception by using transparent container marks.
Populated 1920×1080, 1280×720 and 125% Administration, Locations, Records, shortage and role-picker images are archived under `mcp/after/`, fifteen normal-state screenshots in all. The synthetic fixtures have valid mutually exclusive panel visibility, no unresolved displayed localization key, and no hard GUI render diagnostic; the support-ratio cache and explicit Germany fixture resolved defects exposed by earlier images. The parent visually reviewed the fifteen images and the Locations and Records click regions, including the selected-row marker, six visible list rows and a seventh scroll row. Native locked action controls were added after the first Locations matrix because the stress render showed a disabled action with an active-looking state. Post-edit Locations MCP SVGs at all three scales and a 125% long-name, large-number, scrolled, hovered and disabled stress case returned `GUI_RENDERED` without hard diagnostics; their local previews were visually inspected. The empty-list and filter-hover case also fit. These extra PNG previews are derived from MCP SVGs; remaining tooltip/click-region combinations and full-list extremes are still open.
The required populated vanilla decisions and occupation windows did not both yield usable MCP images, and the original Locations before-image is unavailable. The MCP GUI route does not expose a source-revision `gui_compare` operation; the current comparison is manual and artifact based.
Earlier map MCP artifacts inspected Northern Hungary state 43, Łódź state 87 and the mod-designated Auschwitz site in state 88 with province metadata, but did not prove dated German control or a valid occupation-to-custody transfer. State 88's history filename and localization disagree, so it is described as the mod-designated site rather than presumed exact geography. Earlier technology MCP bonus-coverage inspection found `industry`, `support_tech` and `engineers_tech` categories with 43, 38 and five covered technologies respectively; it did not execute meta-generated awards. The earlier broad map, technology and GER focus reads timed out after 180 seconds; a later focused state-88 map inspect returned source geography evidence with unrelated position/locator validation failure. The post-setup hidden-event scan remains partial, and the explicit ledger GUI inspect returned an artifact with `validation.passed = false` and non-blocking overlap findings. Exact artifacts and limits are in `occupation/cross_state_movement_handoff.md`. Focus, event and probability route coverage remains partial, and source checks cannot replace those engine routes.
Parsed-source checks pass 16 foundation scenarios, 14 major-country scenarios, 27 civil scenarios and 58 focused occupation scenarios covering accounting, cross-state transfer, custody origin, the historical envelope, the dated bounded caller and four state-88 setup assertions. They exercise a modeled twelve-month pulse, payment/reserves, exclusive assignment, conservation, finite release, chronology, award limits, a one-budget route, German home-origin exclusion and setup gating, but mock engine primitives and do not prove engine behavior.
The foundation evaluator now loads the existing UI constants and history helper because shortage-onset recording introduces that production dependency; its scenarios still pass.
The scoped localisation audit found no unresolved direct GUI keys or scoped scripted-localisation names after the source edit; the free-resume quote and Records unit wording were corrected. The new German setup cost, blocked-cost and cost-hover keys are present with the same 25 PP constant as the debit, and its tooltip distinguishes the Development budget policy from the PP payment. The Records retention caption refers to lasting loss totals because the detailed history list rolls off after 96 entries. Exact visual fixture review found readable labels and no clipping in the fifteen archived normal states, while the remaining edge and tooltip matrix is open; three current-source Records render attempts timed out and cannot validate the new history label.
The event-completion audit returned only partial MCP lifecycle coverage and found two stale documents. `docs/events/germany_mengele/overview.md` now states the actual 1943-05-30 whole-chain gate, and `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md` now describes finite in-place liberation and marks its old decision audit as historical evidence rather than current completion.
Event 22's separate concentration-camps spec/catalog handoff is not automatically accepted by this national-administration contract; its existing Spain event row remains a distinct unresolved design linkage rather than silently rewritten spreadsheet content.
