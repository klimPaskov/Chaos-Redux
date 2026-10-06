# Event 010 Death accepted design decisions

Date: 2026-10-05.

Status: accepted design changes and implementation dispositions for the Event 010 release repair. The parent explicitly authorized these G6 and G7 decisions in the resumed task; the dated record preserves that acceptance basis after the earlier worker context was lost.

## Accepted design changes

| Surface | Accepted decision and reason | Disposition |
| --- | --- | --- |
| Public Death focus route | Require separate AND prerequisite blocks for the Shroud endpoint `death_island_pattern`, Hunger endpoint `death_mainland_smell`, and Census endpoint `death_first_ghost_muster`. This matches the accepted three-lane convergence. Shroud focuses bypass after public reveal without running rewards, and Public Death bypasses only after a successful Instant Outbreak. | Implemented in `common/national_focus/010_death_focus_tree.txt`; current focus inspect has 26 nodes and zero blocking diagnostics, with a rendered crop confirming three incoming connectors. Live bypass timing remains user-owned. |
| Instant Outbreak island route | Do not set natural evolution flags for the manual scenario. After successful mainland revelation, `death_instant_outbreak_started` opens the island-spread route directly, so the scenario can continue through ordinary spread without claiming that natural Second Shore or another evolution fired. | Implemented through `death_can_spread_to_islands` and the post-reveal success branch in `common/scripted_effects/010_death_effects.txt`. The scenario adapter cannot represent the required DTH focus/evolution state; live progression remains unverified. |
| No Graves Needed | Replace the unused focus flag's narrative-only outcome with a one-time addition to the shared soul-power pool equal to the current cost of one weak ghost host. A separate earmarked budget would misstate how the pool works; ordinary spread or host decisions can spend the addition first. | Implemented by `death_award_no_graves_muster_reserve`. Localisation says the amount enters the shared pool and does not promise a protected host. |
| Wasteland Roads | Apply the existing focus progress bonus to the one valid border state selected for withering during each public spread pulse. The focus now has a live reader in the shared wither path. | Implemented in `death_try_wither`. At low pressure, the base gain plus Wasteland Roads and Every Road Slows reaches the 3-point threshold in one pulse; adding State Without State gives 4. The target still must pass the valid, unoccupied border-state trigger. No AI weight changed. |
| Seal Names in Iron | Replace the old national exposure-only purchase and proposed ghost-spawn scaling with 120-day protection from border withering in one living-controlled recaptured wasteland state. No state-local ghost-spawner consumes a spawn-scale value, so tying the purchase to one would advertise a mechanic with no consumer. Add a separate 180-day state cooldown and spread pressure +2 if Death retakes the state while the seal holds; retain exposure -2 and mourning debt -1. Paid costs are 35 PP, 150 support equipment, and 3 trains through the Black Friday sale table. A landing or military attack can still retake the state. | Implemented in `010_death_decisions.txt`, `010_death_triggers.txt`, `010_death_effects.txt`, `010_death_constants.txt`, localisation, and the single authorized shared Black Friday quote hunk. The historical `death_consumed_state` marker persists after recapture and already blocks ordinary state-consuming wither. The border-withering eligibility change deliberately applies the existing hazard and daily division damage to living-controlled recaptured wasteland next to active Death land. Applying a seal removes that state from the border hazard for 120 days, and the existing daily DTH-neighbor pulse reapplies it after the timed flag expires. Pressure backlash runs in `death_apply_active_wasteland_state` before cleanup on the actual Death control-change path. |
| Survey the Wasteland | Replace the supplied-division gate with an acting-country-owned division present in the selected state plus paid field transport stores. No native current-supply predicate could be verified in installed trigger docs, the offline wiki, or the approved Kaiserreich source. Do not infer supply from infrastructure, supply nodes, organization, or reserves priority. | Implemented presence through `death_state_has_player_division` and the shared target/effect guard. The supplied-status mechanic is explicitly superseded and remains blocked; current player copy describes the division's escort and field transport without claiming it is supplied. |
| Dead-Zone Outpost field work | Replace the specification's native supply-connection/engineer/temporary-construction-burden requirement with an acting-country-owned division present in the selected surveyed recaptured state and the existing paid Army XP, support-equipment, truck, and train stores. No documented native supply-connection predicate could be verified, and the current effect creates an outpost modifier rather than a construction burden. Keep copy about guarded field delivery and the state outpost; do not claim a tested supply connection. | Implemented in `death_is_valid_dead_zone_outpost_target`, using `death_state_has_player_division` and the shared candidate/effect guard. The unsupported supply-connection requirement is explicitly superseded; the four resource payments remain sale-aware and aligned. |
| Decision cost bundles | Cap each action at four total spendable types, including the separate custodial-capacity payment. Joint Coastal Patrol uses command power, fuel, convoys, and support equipment; Last Shores Response uses command power, Army XP, fuel, and trucks; Transit Custodianship setup uses custodial capacity, support equipment, trucks, and fuel, with upkeep using the last three. Patrol and Transit dropped trains; Last Shores Response dropped convoys and support equipment; Transit dropped command power because custodial capacity already pays for the staffed state policy. | Implemented consistently in Event 010 affordability triggers, payment effects, and sale-aware price consumers. The shared Event 026 quote producer still initializes unused Death quote variables; no shared owner rows were deleted. Inline cost rows now show at most three values, and each hover retains the complete applied payment. |
| Mainland reveal reporting | Keep valid quiet-origin startup silent, schedule the `.2/.3` missing-island report pair at most once per country, and emit one identical `.4` world news item per campaign with aggregate consumed-state and population totals. A major news event must use `major = yes` to reach all countries. | Implemented in `events/010_death.txt` and `death_emit_mainland_reveal_news`. The native news-event broadcast behavior is source-checked; visual and live delivery remain unresolved. |
| Launch failure and acknowledgement | The hidden Settings root and the Instant Outbreak dispatcher report blocked launches through the single Death-owned `.5` failure event. Preserve the first reason while one `.5` is pending for that country, refuse a second launch from that country until acknowledgement, and claim `chaosx_manual_event_failure_shown` so the generic Settings failure does not add a second popup. Prioritize defeated, then any active world-end, then active Death; a missing origin/route reports that no territory changed hands. Valid quiet-origin startup stays silent. Schedule the generic `.6` success acknowledgement only when the Death launch success flag is set at all four intensities; set the maximum-use flag only after successful maximum intensity. | Implemented in `events/010_death.txt`, `common/scripted_effects/010_death_effects.txt`, and the Death-only branch of `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`. No other scenario branch or shared selector changed. |
| Six Continents achievement | Count unique continents reached by Last Shores footholds, not the number of foothold states. Retain the per-foothold count for soul-budget scaling. | Implemented through seven one-time continent flags and `death_world_end_unique_continents`; achievement text now names six distinct continents. |
| Defeat aftermath | Evaluate whether defeat qualifies for super-event 64 before clearing the world-end and reveal flags, then carry that decision through teardown. | Implemented with `death_defeat_super_event_pending` in `death_finish_defeat`. |

## Source evidence and validation limits

Installed `triggers_documentation.md` revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` documents `any_state_division` at lines 1684–1692 as a state-scope division iterator and `divisions_in_state` at lines 2648–2662 as a count/type filter. Neither documents current division-supply status or ratio.

The offline Event modding page revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` states at line 149 that `major = yes` broadcasts news events to every country; installed vanilla `events/NewsEvents.txt` uses `major = yes` on `news.1` at line 14.

Vanilla Norway `common/decisions/NOR.txt:2415–2418` uses `any_state_division = { OWNER = { tag = ROOT ... } }` to check actor-owned divisions. This validates presence/ownership syntax only; it does not prove supply.

The approved Kaiserreich source search for native division-supply tokens found no predicate; its `common/scripted_effects/COS effects (Costa Rica).txt:175` match is a custom `COS_supplied_rebels` state flag, not a general native unit-supply test.

The current focus inspection reported 26 nodes and zero blocking diagnostics. Focus render showed three incoming connectors to Public Death; its layout hash and crop are recorded in the release handoff. The focus probability adapter could not represent completed focus IDs, reveal/bypass flags, evolution state, or required DTH external scopes; its evaluation and sweep are partial and do not establish final rankings or probabilities.

Current event inspection is partial, and the decision inspection did not return complete scenario coverage. The one-shot decision probability comparison is being attempted against identical named synthetic scenarios; any comparison result remains a source-model analysis rather than observed gameplay.

News, report, portrait, and super-event DDS repairs preserve decoded pixels and alpha. Original converted DDS files and hashes are archived under ignored `docs/assets/010_death/dds_container_repair/` and `docs/assets/portraits/010_death/zol_world_end/`; inherited master-art provenance remains unresolved, and no ImageGen or grounded-source claim is made.

## Older claims and catalog work

The old Event 010 supply-status requirement for Survey is superseded by the accepted acting-country-owned division plus paid field-transport design above. The old Seal Names concept of scaling a ghost spawn is superseded by state-local protection because no state-local ghost-spawner consumer exists.

The event catalog workbook was not edited in this repair. `catalog_changes_pending.md` lists the exact Event 010 detail, evolution, world-end, and triggerable-scenario fields awaiting workbook update and export.

## Currency display and durable asset evidence

All 34 custom-cost families retain at most three total inline values, and each full hover preserves the complete applied bundle at four or fewer types.
Custodial capacity counts as a spent type, so Transit setup spends capacity, support equipment, trucks and fuel; its upkeep spends the last three.
Capacity fee amounts are copied from their three shared tuning constants into display variables and used in names and hovers, avoiding independent literal 1/2/3 prices.
Both capacity and Soul power use dedicated 18-pixel native-alpha currency glyphs registered in `interface/010_death.gfx`.
The Soul-power full hover also includes its live quoted amount and payment timing.
The native sprite precedent is the installed `interface/texticons.gfx`; the offline Graphical asset modding spriteType section at lines 30-48 defines the texture registration form.
The new icon source masters, prompts, manifests, native-size reviews and original DDS repair archives are explicitly preserved as owned evidence despite the general `docs/assets/` ignore rule.
No art source or generated frame provenance is claimed for the inherited eight repaired DDS files beyond those archived bytes and exact pixel/alpha equality.

## Final cost parity correction

The parent found the truck quote still displayed for Transit setup and upkeep while those two affordability and payment helpers had accidentally lost the truck lines during cost consolidation.
The accepted four-type setup and three-type upkeep are retained by restoring the corresponding truck gate and debit.
Six Black Book/Herald purchases now also check their quoted Stability loss before payment, so a country below the fee cannot receive a clamped partial debit.
Equality remains eligible through `NOT = { has_stability < death_sale_price_check }`.
This is a G4 affordability repair; no numerical price or AI score changed.
Installed `triggers_documentation.md` lines 4800-4807, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, defines the country Stability comparison.
Offline `Triggers - Hearts of Iron 4 Wiki.md` line 729, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, explicitly accepts a variable for its amount.
Current MCP eligibility and cost-boundary runtime proof remain unresolved.

## Player-facing flag requirements

Final requirement review found the new Seal protection/cooldown flags and Instant Outbreak bypass lacked native tooltip text.
The same dictionary also lacked existing Black Book, Compact, coastal-crossing and focus conditions reachable through requirement helpers.
The owned flag-localisation file now gives 29 named conditions short player-readable text, with four focus requirements reusing the exact focus titles.
Visibility-only port-hide and internal mission activation flags remain outside displayed requirements.
No trigger, price, route or timing changed.

## Readable Black Atlas panes

Implemented in source under G5/G6: preserve the existing eleven summary values but split them into Seas, Fronts, Compact and Book tabs, with at most four visible mechanic values per pane.
Book remains conditional on the existing forbidden-method context; an unavailable Book view falls back to Seas.
Four native tab controls and one native close control stay within the five-action ceiling, and reopening resets the pane state.
This replaces the crowded current summary layout; it does not implement the separate unresolved broader map-dashboard proposal.
The UI worker owns the scoped reference, native layout and click-state wiring, plus bounded before/after MCP attempts and exact evidence gaps.
The seven inaccessible inherited overlap diagnostics cannot be waived without a production artifact.

The free Atlas opener hides while its view is open and has no 14-day re-enable lock, so Close and immediate reopening are functional navigation choices rather than a gameplay purchase.
Its human-only visibility and zero AI weight are retained.

The parent reviewed native-derived Seas and Book compositional references at 1040x472 before geometry changes.
The initial Seas reference had a touching population label/value pair; the corrected reference and native label/value controls share a value-column origin at 194px and a clear 12px gutter.
The reference is an intended layout, not a production MCP render or game screenshot.
