# Event 018 definition-based acceptance report

Date: 2026-07-12  
Validation mode: static implementation evidence, deterministic arithmetic, asset inspection, and the supplied initialization log  
Runtime boundary: the user explicitly waived launching Hearts of Iron IV. No live gameplay, combat, GUI-scale, or audio-playback session was run.

## Evidence contract

- **Definition pass** means the final script has a complete, reachable path and its deterministic state transitions or arithmetic satisfy the scenario.
- **Asset pass** means every required source/runtime/registration surface exists and the final contact sheet or runtime image was visually inspected.
- **Log support** means the supplied `error.log` contains no Event 018-named diagnostic. The log is an older initialization snapshot and is not current gameplay proof.
- A live-engine observation is not inferred from static evidence. The skipped live checks are listed explicitly at the end of this report.

## Scenario results

### Baseline safe field

**Definition pass.** The entry path selects an eligible country and a valid owned-and-controlled state, initializes one persistent field record, and applies exactly one independent integer resource roll. Resource type is uniform over the six standard strategic resources through the integer range 1 through 6. Amount is 80 through 120 inclusive, with arithmetic mean 100. The six resource additions remain separate from preexisting state resources. Careful development, safety, contract, suspension, settlement, and exact closure all exist without any evolution gate, so the complete baseline remains playable when Evolutions I through IV are disabled. Every suspension path finalizes a live maximum-extraction interval before its own clock begins, while resumption of a preserved Maximum Shifts posture starts a new interval and cannot count suspended days.

### Repeat enrichment and duplicate rolls

**Definition pass.** A repeat firing assigns nonzero weights to both a fresh eligible state and an eligible persistent field. Enrichment does not reinitialize the record. Every independent roll calls the same six-way selector and adds to the selected resource ledger, so duplicate rolls add to the existing amount and different rolls create a multi-resource field. Discovery and roll counts increase independently. Follow-up discovery text is selected from the enrichment state rather than replaying the initial tutorial copy.

### Exact closure subtraction

**Definition pass.** `resources_found_complete_full_seal` first proves that each live state resource can cover its matching Event 018 ledger, copies and negates each ledger value, subtracts the six values, zeros the six live ledgers, and then closes the field. It does not subtract the saved preexisting snapshot. Deterministic example:

| Resource | Preexisting | Event 018 addition | Before closure | After closure |
| --- | ---: | ---: | ---: | ---: |
| Aluminium | 8 | 120 | 128 | 8 |
| Chromium | 2 | 40 | 42 | 2 |
| Oil | 12 | 90 | 102 | 12 |
| Rubber | 0 | 80 | 80 | 0 |
| Steel | 25 | 200 | 225 | 25 |
| Tungsten | 4 | 0 | 4 | 4 |

The successful path clears active status before unregistering selection, permanently closes the state, permanently blocks Evolution IV for that field, and contains no retaliation call. A failed reversibility proof subtracts nothing and exposes reconciliation instead of pretending closure succeeded.

### Concession ownership transfer

**Definition pass.** `resources_found_handle_field_ownership_transfer` removes the old owner's registry entry, preserves the state-local six-resource ledger and physical field history, binds the current legal owner once, and marks contracts, concessions, commissions, and political rights for separate review. It does not call field initialization or grant the initial discovery reward again. Removed buyers, sponsors, claimants, and owners have bounded cleanup paths.

### Border dispute and state transfer

**Definition pass.** Claimant selection requires a real claim or mapped dispute. The sequence advances through competing survey, customs or road confrontation, armed patrol, a locked frontier mission, and limited border war only under the military gate. Owner victory, claimant victory, settlement, ceasefire, stalemate, and commission off-ramps are distinct. Claimant victory transfers the state and then calls the same ownership-transfer helper, preserving the field ledger while reopening diplomatic rights for review.

### Foreign-interest strategic scoring

**Definition pass.** Invite Strategic Bids performs one bounded country scan only when the paid project completes. The six standard resources are scored independently from the field ledger and each candidate's live deficit, imports, consumption, and domestic extraction. The shared component includes field scale, diversity, Developed Yield, global significance, suspension, commission constraints, and owner weakness. Candidate-specific access, opinion, claim, existing-partner rivalry, war demand, major status, factory capacity, and overextension then select the highest country at or above the centralized minimum. The selector contains no random-country fallback and equal scores keep deterministic iteration order.

The recorded arithmetic fixtures remain:

| Candidate profile | Score | Result |
| --- | ---: | --- |
| Neighboring wartime importer with a material deficit | 70.1 | Selected over weaker bidders |
| Modest same-continent buyer | 25.2 | Qualifies |
| Distant resource-abundant major | 0 | Rejected |
| Same modest buyer while the field is suspended under commission | 3.2 | Rejected below 20 |

### Mutually exclusive field-output stages

**Definition pass.** Every common field refresh removes all six stage modifiers, reconstructs the durable field stage, and adds exactly one visible state-output identity. Suspension takes presentation priority without destroying the underlying development stage. Exact closure and cave conversion clear the family without replacement. The six selected-field value helpers place exact 20, 40, 60, and 80 values in the higher band for Developed Yield, Excavation Depth, Workforce Safety, Foreign Pressure, Subsurface Disturbance, and Breach Pressure.

### Complete field record and Closed history

**Definition pass.** The compact panel exposes state, current recorded owner and controller, discovery count, six-resource composition, posture, durable stage, five named bands for each field value, contract, commission, and explicit operating/restricted/suspended/sealing/closed status. Disturbance and Breach remain hidden until their respective Evolution II and III reveal flags. Exact sealing stores the reversed six-resource ledger and a bounded last-closed pointer, removes the state from the active array, and switches to a separate history container consuming `GFX_018_resource_field_closed`. The parent field-management category accepts that history trigger and remains visible when no active field survives. No effect assigns the closed pointer back to `resources_found_selected_field`; cycling and projects therefore continue to reject the permanently closed state.

### Evolution II safety comparison

**Definition pass.** Incident loss uses:

`risk = clamp(100 - safety + disturbance + breach, 25, 250)`

then applies the incident base loss, a real-population component, evacuation reduction, and concealment increase before the exact population-loss helper and shared Deaths cause 16. For an underground attack with `state_population_k = 1000`, disturbance 40, breach 0, and no evacuation or concealment:

| Owner profile | Safety | Risk | Base-risk loss | Population component | Requested loss |
| --- | ---: | ---: | ---: | ---: | ---: |
| Careful | 90 | 50 | 750 | 150 | 900 |
| Exploitative | 30 | 110 | 1,650 | 150 | 1,800 |

Restricted workings also lengthen evolution timing by factor 1.75, while safety projects raise the visible safety value and reduce later risks. Concealment multiplies requested losses by 1.25 and records its own consequences.

### Evolution III successful full seal

**Definition pass.** The pre-fire path independently adds 120 through 200 of each standard resource, for a total range of 720 through 1,200 and mean 960. Public breach, settlement attacks, transport disruption, city intrusion, hunts, evacuation, partial sealing, and full sealing are separate reachable stages. Full sealing requires suspension, population security or evacuation, engineering preparation, surface containment, and its timed operation. Success invokes the exact closure path above, permanently blocks Evolution IV, and does not schedule hidden retaliation.

### Maximum 30-division breach

**Definition pass.** Starting strength is `6 + floor(score / 5)`, clamped to 6 through 30. The recorded deterministic profiles cover cautious 6 to 10, developed or dangerous 11 to 18, heavy exploitation 19 to 24, and extreme repeated or military exploitation 25 to 30. The extreme profile reaches exactly 30 and cannot exceed it. The origin is recorded before transfer and is forced to zero future captured-state capacity. Emergence and the bounded adjacency refresh both declare war on every valid current or newly adjacent land actor once.

### Captured-resource capacity and denial

**Definition pass.** Every non-origin controlled state sums current oil, aluminium, rubber, tungsten, steel, and chromium, repeatedly subtracts 10 to implement floor division, and caps at 10. Prepared denial delays activation by 30 days and subtracts three capacity on the first successful activation, clamped at zero. It is consumed once and does not mutate the geological or Event 018 ledgers.

| Total strategic resources | Base capacity | Capacity after one denial | Origin capacity |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 |
| 10 | 1 | 0 | 0 |
| 19 | 1 | 0 | 0 |
| 20 | 2 | 0 | 0 |
| 48 | 4 | 1 | 0 |
| 99 | 9 | 6 | 0 |
| 100 | 10 | 7 | 0 |
| 150 | 10 | 7 | 0 |

### Activation interruption, capacity loss, and Unfed Broods

**Definition pass.** Activation requires 30 days of continuous DHO control. The state-control hook cancels activation on recapture. An active anchor lost by DHO starts a 21-day grace period. Recapture before expiry restores support. Expiry removes that anchor's exact capacity from the country total and refreshes the live division count. Divisions above capacity receive `cave_unfed_broods` instead of being deleted. A destroyed division lowers the refreshed live count and opens one sequential spawn slot. Ordinary spawning is one division per 30 days; the terminal form uses 15 days. Anchor cleanup removes cave and denial identities without deleting the underlying resource ledger.

### Cave route behavior and multi-front AI

**Definition pass.** The final tree permits exactly one hierarchy, one cumulative doctrine, and one cumulative adaptation route. Stone, Burrow, and Scree focus rewards swap cumulative spirits and change spawn/template preference, target selection, transport disruption, strongpoint behavior, spawn pacing, or map objectives. The rich-route helper compares every land-reachable enemy resource state and stores the deterministic maximum standard-resource total; no weighted random draw can select a poorer state. Persistent resource, strongpoint, transport, continental-capital, origin, anchor, and world-end targets are consumed by supported `front_unit_request`, `force_concentration_target_weight`, `front_control`, garrison, conquer, contain, production, and role-ratio strategies. Ordinary countries at war with DHO increase anti-tank and CAS production and anti-tank role demand. DHO maintains origin/anchor requests while route-specific strategies request units on distinct reachable objectives.

Definition balance from the unit and country modifiers, using the game's 4 km/h infantry baseline and the shared Slow Blood reduction:

| Template | Effective movement |
| --- | ---: |
| Feeding Guard | 0.65 km/h |
| Stone Phalanx | 0.91 km/h |
| War-Brood | 1.43 km/h |
| Scree Pack | 1.43 km/h |
| Burrow Column | 1.82 km/h |

All cave battalions require zero manpower and declare no equipment need. Their locked templates set `force_allow_recruiting = no`; all divisions enter through the scripted opening or capacity spawner. High hardness and armor punish ordinary infantry, while dedicated hard attack and piercing remain the intended counter. No ordinary cave market, faction, manpower, equipment, naval, air, or training path is enabled.

### World-end chaos and continent gate

**Definition pass.** World-end verification requires the Event 018 setting, Evolution IV, a living DHO host, no active or disabled competing world end, chaos strictly greater than 1,000, a stored valid origin, exact equality between eligible/scanned/owned/controlled origin-continent state counts, and at least one valid distant foothold candidate. The exact condition must remain continuously valid for 60 days. Verification completion sets only its durable completion marker and notice. `resources_found_cave_begin_world_end` has one caller: completion of `DHO_the_world_opens_below`, which rechecks every terminal input before writing the shared state once, suspending incompatible Event 018 progression, changing DHO to the World Below, accelerating terminal spawning, emitting display 83/audio 55 once, and creating footholds.

### Cross-continent foothold validity

**Definition pass.** Candidate selection excludes the origin continent, impassable states, the cave country, and states whose transfer would delete their owner by requiring current ownership and control by the owner and more than one owned state. Selection is independently performed for each valid non-origin continent and weighted by total resources, resource diversity, industry, transport, and Event 018 field value. The effect transfers only the chosen state, creates the stronger local foothold and brood allocation, and refreshes wars against its new land neighbors.

### Regional defeat cleanup

**Definition pass.** Zero DHO-controlled states triggers the one-shot defeat resolver. It clears the active cave threat, country target, AI/anchor lifecycle, residual Evolution IV eligibility, and Event 018 restart paths. If the campaign lacks global or near-global evidence, it emits the regional containment path only. Every liberated anchor has a cleanup/restoration decision; the origin remains permanently excluded from rediscovery.

### Global defeat aftermath gate

**Definition pass.** Global aftermath is eligible only after Event 018 world end, a cross-continent foothold, or complete origin-continent conquest sustained through the centralized 365-day campaign threshold. The former 75-percent milestone is not sufficient. An incompatible world end blocks the classifier. Global defeat presentation, display 84/audio 56, and reconstruction are one-shot. Event `.99` is presented only after a qualifying country has at least three cleanup contributions, no remaining cleanup state, and no live cave threat; join, lead, and refuse are mutually exclusive and completing a commitment does not fire the choice again.

### Exact achievement evidence scenarios

**Definition pass.** The achievement predicates below are backed by immutable field, mission, state-control, spawn, cleanup, or terminal evidence rather than a loose final-state approximation.

| Scenario | Passing evidence | Negative fixture excluded |
| --- | --- | --- |
| Contract of the Century | One exact 365-day long-term contract review retains the same sovereign owner, field, and partner at Developed Yield 60 or above, Safety 60 or above, and Pressure below 80 | Any threshold lapse, suspension, occupation, public breach, border war, transfer, or invalid contract permanently disqualifies that review |
| No Claims Left Unsettled | A claimant-specific dispute first reaches Crisis pressure and armed/frontier stage, then one compensation, arbitration, commission, or demilitarization agreement survives 180 days | A quiet claim, annexed claimant, border war, transfer, occupation, renewed confrontation, commission collapse, or mixed claimant/field clock cannot qualify |
| Thirty From Below | The legal owner or physical controller snapshotted before transfer faces exactly 30 opening divisions and survives independent, uncapitulated, and in control of the recorded capital until regional defeat | A country that was neither owner nor controller, a 29- or 31-division value, cave continuation, capital loss, or World End cannot qualify |
| Ten From One State | The normal capacity-deficit spawner creates a brood from the exact active, nondisrupted, non-origin, capacity-10 anchor before World End | A capacity-10 marker without a spawn, origin spawn, direct Scree release, World-End foothold, or capacity 9/11 cannot qualify |
| The Last Shaft Closed | One ordinary country cleans three distinct states that completed normal non-origin anchor activation before World End, then the regional threat ends with no chamber left | Origin, activating-only sites, World-End footholds, generic restoration, or repeated cleanup of one credited state cannot enter the dedicated ledger |
| The Mountain That Moves | The named Stone Phalanx capstone is complete, a prepared major entered a qualifying cave war, that major capitulates to DHO, and the origin was never lost during the qualifying war | Phalanx Assault alone, an unprepared or non-major opponent, origin loss, or a World-End victory cannot qualify |
| The Front Has a Floor | The named Burrow War capstone is complete and a defended capital, supply hub, or level-3 fortified state adjacent to an active nondisrupted anchor is stored and captured by DHO during the exact 90-day mission | Burrow Approach alone, infrastructure alone, fort level 1/2, no defender, stale/different state, expiry, cancellation, defeat, or World-End transfer clears or fails the attempt |
| When the Hills Begin to Move | The named Scree Tide capstone is complete, then at least three deployed Scree Packs inside live capacity open a 180-day attempt and remain present when five different state captures plus two different country capitulations complete that same ledger | Pre-capstone releases, recaptures or repeat capitulations within one attempt, one/two packs, over-capacity state, split windows, expired counters, or fewer than three packs at the final hook cannot latch success |
| The Ground Is Quiet Again | Event 018 World End and its super-event historically fired, the ordinary-country contribution and reconstruction gates pass, and no DHO territory, chamber, or threat source remains | The 365-day near-global classifier without verified Event 018 World End is insufficient |

## Improvement proof gates

| Gate | Definition-based disposition |
| --- | --- |
| PG-01 equipmentless broods | Complete by unit/template/spawn/capacity definition audit. Live combat and reinforcement observation was waived. |
| PG-02 capacity and denial | Complete by the boundary table, one-shot denial trace, activation/grace/spawn lifecycle trace, and ledger-preservation audit. |
| PG-03 combat and route AI | Complete by cumulative route audit, unit-stat balance table, reachable observation events, target consumption, origin/anchor requests, and ordinary anti-armor strategies. Live battle observation was waived. |
| PG-04 baseline/evolutions/closure | Complete by package arithmetic, safety comparison, global evolution-row guards, transfer traces, and exact six-ledger inverse. |
| PG-05 terminal and aftermath | Complete by exact truth-table gates, one-shot terminal/defeat/reconstruction flags, valid foothold selection, and bounded cleanup. |
| PG-06 UI/assets/text | Complete by static evidence. The selected-field package supplies the full durable record, five real-frame animation families at 10/10/12/12/12 frames, five required static fallbacks, Suspended, and a live history-only Closed consumer. All 65 focus icons, 36 unique idea/state icons, 39 action-family plus 5 category icons, 5 category pictures, and 15 achievement triplets are registered and inspected. The final localisation audit proves the four Event Details controls remain usable while unrevealed title/body/summary content and the Stage IV portrait stay chronology-masked. Live scale, playback, and unlock observation was waived. |

## Supplied error-log evidence

The inspected file is `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`. It is a 68-line, `no_game_date` initialization log last written at 2026-07-11 16:58:09. It contains no Event 018, DHO, Resource Field, or Event 018 audio diagnostic. Event 018 audio IDs 54 through 56 have complete named registrations and files. Some Event 018 files in the final worktree postdate the log, so this is supporting negative loader evidence only. The log's workshop-descriptor and anonymous shared-sound lines do not name or resolve to an Event 018 surface and are not used as Event 018 acceptance evidence.

## Fresh closure audits

- `final_event_completion_reaudit_handoff.md` returned PASS after comparing the full package to the latest gameplay, AI, achievement, focus, decision, terminal, asset, text, and documentation surfaces.
- `ui_localisation_reaudit_handoff.md` returned PASS after the missing research-bonus label, player-facing process language, and deterministic status-box wrapping were repaired and re-read. The final three status lines are 111, 69, and 111 pixels at their widest in vanilla `hoi_16mbs`, within the 158-pixel box.
- `asset_audio_reaudit_handoff.md` returned PASS after the consolidated super-event registration row was corrected to `interface/chaosx_super_events.gfx` and the current manifest hash was verified against the live definitions.

## Explicitly skipped live validation

At the user's direction, the following were not executed in Hearts of Iron IV:

- 6-, 18-, and 30-brood live spawn/combat/reinforcement observations;
- Stone/Burrow/Scree battle matrices against infantry, anti-tank, armor, terrain, and low supply;
- live multi-front AI observation and origin-retention observation;
- live state-transfer, mission-timeout, occupation, and terminal-campaign playthroughs;
- selected-field GUI inspection at multiple UI scales and live animation/fallback switching;
- in-engine super-event music playback and loudness transition checks;
- in-engine achievement unlock attempts.

These are skipped task-specific validations, not claimed engine results. Final acceptance uses the deterministic definitions, audits, asset inspections, and the supplied log boundary authorized by the user.

## Simplifications, fallbacks, omissions, and blockers

No gameplay simplification or fallback is accepted in this report. The static UI textures are deliberate accessibility fallbacks paired with real multi-frame source animation, not substitutes for missing animation. Asset, localisation, workbook, and improvement-loop blockers are closed. The fresh event-completion, selected-field UI and localisation, and asset and audio audits all returned PASS after the inconsistencies they found were repaired and re-read. No acceptance checkpoint remains open.
