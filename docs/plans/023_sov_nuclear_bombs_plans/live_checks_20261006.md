# Event 023 live checks for Claude

Baseline: `qa_001_fresh_head.hoi4`, read with the save-inspection skill.
It is a plain-text USA save at `1936.1.1.12`, game `Operation Postern v1.19.2.0.a729 (2bce)`.
SOV capital is state 219, and the bounded SOV inspection found no active `sov_nuclear_bombs` state.
The inspector commands were `info`, `find ... sov_nuclear_bombs|chaos_meter_value --in countries/SOV`, and `get ... countries/SOV/capital --depth 1`.
This observation describes that baseline only.
Run independent branches from this baseline for destructive war and custody tests.
No agent launched the game or changed the save.

## Opening and prose

Load the baseline and enter `tag SOV`.
Enable the Chaos Meter in Settings if it is disabled.
Run `eval_effect set_variable = { global.chaos_meter_value = 200 }`, then `event chaosx.nr23.1 SOV`, and advance one day.
Choose each doctrine on a separate branch.
Expect exactly 100 event bombs, one opening choice and one primary posture spirit, with baseline Readiness/Integrity Party 35/96, Military 47/84, Scientific 27/98 and Dispersed 43/78.
Inspect the four short doctrine descriptions and the state orders on the map.
Force the root twice before answering the opening and once afterward.
Expect one queued opening, then an explanation that the programme is already open or awaiting a decision, without another grant.
On a separate branch, disable the Chaos Meter and run `event chaosx.nr23.1 USA`.
Expect one explanation on the invoking country rather than silence.

## Posture lifecycle

In the active baseline branch, set the named evolution inputs for an isolated presentation probe using `eval_effect set_country_flag = sov_nuclear_bombs_evolution_ii_active`, then `e SOV sov_nuclear_bombs_refresh_posture`.
Repeat with `sov_nuclear_bombs_evolution_iii_active` and `sov_nuclear_bombs_evolution_iv_active`.
Expect Coercive, Retaliatory and Unrestrained respectively, without stacking old spirits.
Run `eval_effect set_variable = { sov_nuclear_bombs_integrity = 19 }`, then the refresh helper, and expect Broken Chain.
Set Integrity to 30 and refresh, and expect the attained-stage posture to return.
Use the actual moratorium and reactivation decisions on a separate branch, and expect the moratorium spirit only while its flag holds.
Suspending release orders must not apply that spirit.
These flag probes check presentation only.
Also run an incremental campaign through the ordinary evolution pulse at Chaos 400/600/800/1000 and its required world gates, confirming log rows, exact grants and the same spirit changes without the probe flags.

## Doctrine work and phase budget

At Evolution I or higher, open custody through the command board.
Supply the normal security resources, take the one doctrine-specific development, and advance 90 days.
Expect the selected development in the primary spirit description and no permanent extra idea.
Party development requires a threatened capital, Military permits delegated retaliation, Scientific veto blocks a capital or densely populated combat endpoint, and Dispersed regional command can delegate with a surviving secure depot after Moscow falls.
Reform doctrine through the ordinary reform decision and expect the old development note and behavior to clear.
Compare strike preparation Party 12 days / Military 4 days / other 7 days, Military crew training 60 days / other 90 days, and Scientific assembly 150 days / other 120 days.
Compare technical test outcomes across doctrines without claiming a distribution from one run.
Check that inactive, obsolete or unaffordable projects cannot be bought and that the ordinary panel remains short, with map selectors on the map.

## Reactor occupation, replacement and recapture

Use an Evolution I opening at Chaos 400 on a separate baseline branch, finish its two queued reactors, and record their state IDs from the map.
Declare a test war using `eval_effect declare_war_on = { target = GER type = annex_everything }` with SOV selected.
Let an enemy occupy one registered reactor state, or use `eval_effect <STATE_ID> = { set_state_controller = GER }` for the exact state fixture.
Expect the effective reactor count to fall and one 10-Readiness loss, with no device transfer caused by reactor ownership alone.
Invoke `e SOV sov_nuclear_bombs_refresh_effective_reactor_capacity` again while occupation continues and expect no second loss.
Queue and finish a replacement through the normal map decision.
Recapture the original using `eval_effect <STATE_ID> = { set_state_controller = SOV }` or ordinary combat.
Expect physical controlled sites to rise, but effective event capacity to stay within the current entitlement.
Change ownership while retaining control on a separate branch with `setowner GER <STATE_ID>`, then reconcile through the ordinary territorial seam.
Expect the site to contribute no Soviet capacity until ownership and control are both restored.
Inspect production tooltips and compare batch quotes before and after reactor loss, at Readiness 74/75, and with an enemy-held neighbouring state of the assembly site.
Actual completed batch amounts must match the displayed quote and preserve the existing AI inventory ceiling.

## Arsenal servicing and an attack during work

At Evolution I, the 175-device intact arsenal and two reactors provide a natural over-capacity fixture because two reactors support 100 devices.
Open production, inspect Service the Arsenal's first-hover inventory/capacity quote, and take it with sufficient command power, trains and fuel.
Expect one debit of those three resources and Readiness down by 8, with other nuclear projects locked during the 60-day mission.
After completion, expect the held Readiness to return once, Integrity up by 8, 180 days without overload wear, and a 360-day completion cooldown.
Repeated completion-helper calls must not restore Readiness again.
Advance past stabilization and confirm overload wear returns if inventory remains above capacity.
On another branch, receive an actual enemy nuclear strike during service or command development.
Expect the unfinished mission to end before retaliation selection, supplies to stay spent, no development/stabilization award, and service-held Readiness to return once.
Party and Scientific AI without release authority must return to custody for authority, rather than sit on an unusable retaliation board.
Military/Dispersed with a completed command development must still be able to delegate after selecting a retaliation target.

## Public demonstrations, detection and news

Field at least ten deployed strategic bombers, a controlled air base, fuel and the required technology through the native aircraft production/deployment UI.
Complete crew certification, survey a remote map state and prepare a public test.
On three separate branches choose observers, advance notice and announcement afterward.
Expect one presentation choice, one successful outcome report naming the presentation, and the first public-test news only.
Observer results add 16 credibility and 4 Integrity, notice 12 credibility, afterward 8 credibility, with the existing demonstration Readiness gain and repeat-test reduction.
Inspect foreign report behavior over multiple runs for softer observer alarm, stronger notice guarantees and stronger unannounced air defence.
Cancel a prepared public test and prepare another, and expect no stale choice.
Repeat a completed demonstration in the same campaign and expect no second news 230.
For a secret test with a foreign overflight incident, the incident's observer answer must still reveal a successful test without duplicate world news.
Check clean, partial, failed and non-yield accident outcomes for one technical report per action and one device debit only.

## Ultimata, native raids and release

At Evolution II, select a valid nonnuclear enemy state, send a private signal, issue a public ultimatum and refuse from the target country's report.
Return to SOV, complete a demonstration, then renew the same demand.
Expect the same named state and government, a usable enforcement window, and no repeated news 231.
Confirm no final authorization against a nuclear major below Evolution IV's full first-use gate, including a 1100-Chaos campaign lacking the severe strategic-loss conditions.
When every severe condition holds, expect selection, preparation, certification and a separate final authorization, followed by exactly one native callback and no duplicated shared blast consequences.
Try a human vanilla nuclear raid, inspect stockpile draw timing, cancel another raid to inspect refund timing, and confirm Event 23 books expenditure without a permanent accounting dispute.
After an enemy strike, a genuine Soviet response may produce news 233 once.
A second offensive Soviet strike without enemy use must not be described as retaliation.
Any Soviet combat use disqualifies The Bomb Never Fell.

## Collapse custody and deferred risk

On an active Dispersed branch, start Event 5 with `event chaosx.nr5.1 SOV` and choose its ordinary dissolution route that transfers registered depots.
Observe the physical-custody report, secure a breakaway depot, and complete its technical, command and delivery stages through the normal decisions.
Expect one successor world news naming that breakaway and depot, with no operational grant from territorial transfer alone.
Reopen its board or complete delivery at another depot and expect no second successor headline for that actor.
Test return, refused joint custody, refused Soviet recall by force, and accepted foreign removal, including loss of the depot or rail route before the reply.
For the reserved-depot case, save during an Event 23 pending native request before Event 5 transfers its source depot.
Expect the reserved receipt to remain untouched, the 25% Dispersed loss risk to defer, and one risk resolution only after the exact request closes.
Save and reload that state and verify no duplicate callback, refund, missing-device move or successor headline.

## Missile link, exchange and assets

On a branch with a genuinely completed Event 32 nuclear integration, keep an active missile site and its reserve/readiness/control requirements satisfied, then remove the Soviet bomber force.
Expect no lost-delivery Readiness erosion while the verified missile capability remains valid, but Event 23 bomber release stays blocked.
Disable the special-warhead evolution or lose the missile site and expect that exception to end.
Plain atomic technology and bombs without a missile programme must never qualify.
Run a multi-major exchange through the existing receipt chain and inspect response-window shortening, warning/hotline choices, stand-down expiry and the nonterminal super-event 108 picture/audio.
Inspect the delivery-preparation and device-disablement decision icons at native scale, Broken Chain's red/black medal frame, and all seven achievement color/grey/red-X triplets.
No cropped subject, checkerboard matte, halo, raw key or panel overflow is accepted.
The game should retain the same stable sprite aliases and paths.

## AI and persistence

Use `observe` for a controlled Event 23 campaign and save after at least one proof-test and assembly opportunity.
Expect finite audits, affordable optional developments/service, no paid command-board navigation, no vanilla Soviet AI raids while Event 23 is active, no major first use below the severe IV gate, and no range-only retaliation deadlock.
A single observer run is evidence of behavior, not a probability distribution.
Use `savecheck` at a reservation, service, reactor-loss and custody milestone and compare the resulting text saves with the bundled read-only inspector.
The orchestrator records executed setup/actions/results and routes any confirmed failure as a numbered 023 finding.
