# Event 067 Acceptance Criteria and Design Limits

## Completion standard

Event 067 is complete only when the full accepted lifecycle works across event logic, decisions, character ownership, civil war, country package, focus tree, AI, Event Logs, Event Details, cluster membership, manual scenario, world-end branch, assets, super-events, localisation, documentation, and the authoritative catalog workbook.

A popup, a strong commander, or a basic civil war does not satisfy this specification by itself.

## Required source inspection before implementation

The implementation agent must read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-event-assets`
- `chaos-redux-super-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- relevant Event 065 and Event 019 documentation and implementation
- shared Event Logs and Event Details documentation
- triggerable scenario documentation
- world-end registry documentation
- the current authoritative event catalog workbook
- relevant offline Paradox wiki pages
- current vanilla documentation
- at least one current vanilla commander, civil-war, character, decision, focus-tree, focus-inlay, and scripted-GUI precedent

The implementation must use the installed HOI4 MCP routes for event, probability, focus, and GUI surfaces.

## Event identity acceptance

- Entry event uses `chaosx.nr067.1`.
- Event type is Minor Fire-Once.
- Minimum Chaos level is 1.
- Event ID is displayed as `067` where padded IDs are used.
- Event is a High member of Military Preparation.
- Event fires once per campaign.
- A manual scenario consumes the unique character opportunity without fabricating a natural event firing.
- The event is unavailable when no valid host exists.
- The event does not target actual nonhuman countries or invalid special actors.

## Character acceptance

- One canonical fictional male Generalissimo exists.
- He does not replace an existing commander.
- He has the maximum current supported level and four commander attributes.
- He receives every safe positive applicable general and field marshal trait.
- Excluded traits are documented in a trait audit.
- He has maximum useful command capacity.
- He remains available for direct command after becoming ruler.
- Peaceful submission and civil-war transfer do not create a clone.
- Save and reload preserve the same character ownership.
- Ordinary sickness, wounds, retirement, or generic death cannot invalidate the event premise.
- Event-owned successful removal can disable him permanently.

## Baseline acceptance

- The selected host receives the commander immediately.
- He begins loyal and makes no political demand.
- Initial command authority is Theater Command.
- Hidden pre-evolution service record is bounded.
- Military use can affect later Influence without creating an instant high-stage crisis.
- A player can use him before Chaos 200 without political demands.
- Evolution I disabled leaves him as a loyal commander.

## Influence acceptance

- Generalissimo Influence is the only public persistent crisis value.
- Value is clamped from 0 to 100.
- Public bands and thresholds agree across decisions, tooltips, events, and GUI.
- Formal command authority is qualitative, not a second meter.
- Hidden components are not shown as a raw ledger.
- Major military outcomes use one-time guards.
- Small battles and state cycling cannot farm Influence.
- Peace and reserve status can reduce Influence.
- Counterweights impose meaningful costs.
- Stable managed coexistence is possible.
- Influence does not inevitably rise during long peace with restricted authority.

## Evolution acceptance

### Evolution I

- Requires Chaos 200 or higher when entered normally.
- Uses paced MTTH or equivalent dynamic pacing.
- Logs one evolution entry with host actor.
- Unlocks visible Influence, demands, and command management.
- Does not add Chaos merely for activation.

### Evolution II

- Requires Chaos 400 or higher and sufficient influence or network state.
- Uses paced entry.
- Unlocks state-wide network, institutional demands, deeper counterweights, and coercive removal.
- Logs one evolution entry.
- Does not add Chaos merely for activation.

### Evolution III

- Requires Chaos 600 or higher and high Influence.
- Uses paced entry.
- Produces a final ultimatum after a short visible interval.
- Logs one evolution entry.
- Does not start revolt until the player refuses or removal fails.

### Evolved opening

- Initial firing at Chaos 200, 400, or 600 uses the correct evolved opening.
- The player still receives a meaningful reaction window.
- Disabled evolutions do not set later unlock flags.

## Decision and mission acceptance

- The crisis category shows no more than six primary actions.
- Normal phase target is three to five decisions.
- No more than three missions are active.
- Every decision uses at most four spendable cost types.
- Command power cost never exceeds 60.
- Costs use matching texticons.
- State requirements name the current states or regions.
- Missions require active player action.
- Mission durations fit difficulty.
- Success and failure use distinct effects.
- Obsolete decisions hide and clean up.
- AI has an equivalent path for every player action.
- Concessions provide real value.
- Counterweights impose real military or political cost.
- No decision can be farmed through repeated authority cycling.

## Removal acceptance

- Negotiated retirement is practical only at low Influence.
- Dismissal can fail without revolt before the final ultimatum.
- Failed arrest causes revolt immediately.
- Failed capture causes revolt immediately.
- Failed assassination causes revolt immediately.
- Failed final removal causes revolt immediately.
- The player sees the failure consequence before confirming.
- Success chance responds to preparation, Influence, authority, officer network, capital security, loyal reserve, and intelligence.
- Successful removal ends the crisis permanently.
- Method-specific aftermath is meaningful.
- Successful removal blocks normal world-end readiness.
- Removal chance and AI use are probability-audited.

## Civil-war acceptance

- The revolt begins in the same consequence chain as the failed operation or refusal.
- One dynamic junta side is created.
- The Generalissimo transfers to the junta once.
- He becomes junta leader and remains commander.
- Army share scales with Influence and hidden network state.
- Government counterweights reduce junta strength.
- Divisions are transferred or created without duplication.
- Emergency units debit real manpower and equipment.
- Stockpiles are divided without duplication.
- Factories follow territory.
- Navy and air splits occur only when relevant.
- Territory is coherent and supply-aware.
- Both sides receive valid capitals.
- One-state and invalid hosts are excluded from normal target selection.
- External wars, factions, and subjects remain coherent.
- Low and high Influence civil wars are materially different.
- The setup survives save and reload.

## Peaceful submission acceptance

- No second country is created.
- Generalissimo becomes ruler and remains commander.
- Influence closes.
- Command Cohesion opens.
- The dedicated focus tree loads.
- Starting junta ideas apply.
- Existing technology, cores, claims, forces, and stockpiles remain.
- Incompatible old political content closes safely.
- The Personal Command opening flag applies.
- Ruler super-event fires once.

## Junta country acceptance

- Dynamic civil-war identity preserves host readability.
- No fixed tag is created without proven need and collision audit.
- Junta uses normal civilian systems.
- Junta is not marked actual nonhuman.
- Starting ideas have complete lifecycles.
- Command Cohesion is the only visible post-takeover custom value.
- Starting technology and laws are valid.
- Starting army is usable.
- Reinforcement decisions consume real resources.
- Navy and air content appear only when relevant.
- No new custom unit family is introduced.
- No 3D model or counter package is required.

## Focus-tree acceptance

- Full route architecture from Part 5 is implemented.
- Opening reaches meaningful choices quickly.
- Three political structures are real routes.
- Three military strategies are real routes.
- Economy and logistics are real routes.
- Internal government is a real route family.
- Three foreign-policy routes are real routes.
- Postwar integration is complete.
- World-end extension remains hidden before launch.
- Naval and air branches use relevance gates.
- Political, military, industry, diplomacy, expansion, and special content are visually distinct.
- No branch is a one-focus or two-focus label.
- Focuses unlock decisions, missions, state changes, units, advisers, identities, or diplomacy.
- Idea upgrades replace spirit spam.
- Search filters are correct.
- Focus Navigation covers separate major regions.
- Focus inlay is readable and does not cover tree content.
- Route-specific AI exists.
- Route coverage table is complete.
- `hoi4.focus_inspect`, `hoi4.focus_render`, and focus rewrite comparison are used.
- `chaosx_focus_tree_auditor` completes a final review.

## Command Cohesion acceptance

- Influence is no longer active after takeover.
- Cohesion is clamped from 0 to 100.
- Cohesion changes focus and decision access.
- Military victories, officer settlement, supply, route choices, and failures change it.
- Low Cohesion creates pressure without causing repeated automatic civil wars.
- High Cohesion enables the strongest government and international actions.
- AI actively manages the value.

## AI acceptance

- Target selection uses named scenarios.
- Demand selection uses valid candidate pools.
- AI understands wartime value and political risk.
- AI prepares removal when appropriate.
- AI does not choose near-impossible coercive removal without emergency reason.
- AI final-ultimatum choices compare submission, civil-war strength, and removal chance.
- Junta AI protects supply, capital, and the Generalissimo.
- Government AI protects legal command and loyal reserves.
- Focus AI uses route-specific factors.
- World-end AI distinguishes civilian, aligned junta, rival junta, and emergency-government paths.
- Every changed weight receives before-and-after probability comparison.

## Manual scenario acceptance

- Scenario ID `SCN-015` is confirmed free before registration.
- Scenario name is Generalissimo's Coup.
- Four scenario types exist.
- Low, Medium, High, and Maximum intensity work for every type.
- Current player is targeted when valid.
- Scenario bypasses normal Chaos, date, event history, and evolution prerequisites.
- Scenario sets no world-end flag.
- Immediate-war type starts the civil war during setup.
- Invalid hosts are blocked by the same launch and button gate.
- Launch is one-time.
- Scenario setup clears its bypass state.
- Natural Event 067 cannot fire later and create a duplicate character.
- Scenario launch does not count as a normal pacing event.

## World-end acceptance

- Public Event Details row exists.
- Independent toggle persists.
- Branch requires Chaos 1000 or higher.
- Branch requires an active or victorious canonical Generalissimo state.
- Successful permanent removal blocks readiness.
- Launch sets shared and event-owned world-end flags.
- Launch fires the correct super-event and audio.
- Automatic event firing stops after successful launch.
- Country roster is bounded.
- No recurring whole-world scan is added.
- Stable civilian states can resist.
- Weak military-heavy states can undergo peaceful coup or split command.
- One-state countries avoid invalid civil wars.
- Original Generalissimo remains uniquely strongest.
- Foreign military rulers reuse valid existing commanders.
- International Command has membership gates.
- Rival military blocs can form.
- Civil Authority Compact has membership gates.
- Coup support and intervention have costs and failure states.
- Generic Chaos sources are not duplicated.
- Save and reload preserve actor and bloc state.

## Event Logs and Event Details acceptance

- Natural firing creates one history row.
- Host actor displays correctly.
- Three evolution entries display stage, tier, actor, date, and event.
- Event Details evolution catalog shows no fake history metadata.
- Event Details shows public world-end row and toggle.
- Events row shows `N/A` with no valid host.
- Event is disabled by default until implementation is genuinely ready.
- Cluster history records fired or skipped status.
- Scenario launch does not fabricate natural history.
- Civil-war and resolution outcomes appear in the event's detail history where supported.

## Assets acceptance

- Fictional Generalissimo portrait complete and wired.
- Portrait shows no real-person substitution.
- Five category picture states complete.
- Report and news art complete.
- Two super-event images complete.
- Trait, idea, decision, mission, focus, faction, inlay, and achievement icons complete.
- Three flat flag families complete in all sizes.
- Every icon family has separate source art for its UI type.
- Transparent assets retain alpha.
- No opaque square, white halo, fake checkerboard, or generated text remains.
- No temporary asset path is used at runtime.
- Asset manifest and permanent provenance record are complete.
- Temporary `docs/assets/067_generalissimo/` workspace is deleted only after all runtime assets are reconciled.

## Super-event acceptance

- Ruler super-event fires on peaceful submission or junta victory.
- World-end super-event fires only on world-end launch.
- Each uses a unique slot or deliberately verified slot state.
- Each has unique image and unique audio.
- Final title, description, button, and quote fit the same role.
- Quotes are sourced and attributed.
- Audio title, creator or composer, recording source, license, duration, source, and edit are documented.
- Final WAV files are in `sound/067_generalissimo/`.
- Base sound and volume wrappers are wired.
- `play_current_super_event_sound = yes` is used.
- Music catalog is updated.
- No placeholder, default, generated tone, or undocumented audio remains.

## Achievement acceptance

- All eight planned achievements are implemented or a missing item is reported as incomplete.
- Unlock conditions and disqualifiers are tracked.
- Scenario and debug bypasses cannot grant unintended achievements.
- Civil-war contribution and no-foreign-help conditions are measured reliably.
- Every achievement has completed, grey, and not-eligible icon states.
- Localisation is final and player-facing.
- Achievement documentation is aligned.

## Catalog acceptance

The authoritative workbook must be updated. CSV exports are regenerated from it.

Required event row changes:

- Event 067 full player-facing details
- three evolution summaries
- world-end field
- Type Minor Fire-Once
- Chaos level 1
- Military Preparation cluster assignment
- High member severity
- implementation status after evidence supports it

Required cluster changes:

- Military Preparation row exists in the authoritative cluster source
- Event 067 included as High member
- cluster ID matches runtime registry

Required scenario changes:

- `SCN-015` Generalissimo's Coup
- four type descriptions
- four intensity descriptions
- status aligned with testing evidence

The implementation must never edit the three CSV exports directly.

## Localisation acceptance

- Final text follows the direction in Part 8.
- No planning labels are copied as final text without review.
- No hidden variables or future outcomes are spoiled.
- Costs and requirements are clear.
- Dynamic states and countries display correctly.
- Event Details and workbook wording match in-game text.
- No raw keys appear.
- English localisation is UTF-8 with BOM.
- Event, decision, focus, GUI, achievement, and super-event text avoids em dashes and semicolons.

## No-DLC acceptance

A no-DLC campaign can:

- receive the Generalissimo
- use him
- gain and reduce Influence
- receive all three evolutions
- grant and reject demands
- remove him through every method
- experience civil war
- submit peacefully
- use the full core focus tree
- manage Command Cohesion
- complete the manual scenario
- enter the world-end branch

DLC enhancements hide cleanly when unavailable.

## Multiplayer acceptance

- One normal Generalissimo exists worldwide.
- Target selection treats multiple players correctly.
- Only the host controller receives crisis actions.
- News and diplomacy reach other players as appropriate.
- Tag switching or control changes do not duplicate the interface.
- Scenario targets current player when valid.
- World-end actor processing remains global and bounded.

## Required audits before completion

- parent source review
- `chaosx_ai_probability_auditor`
- `chaosx_event_ui_worker` for the event-owned attached display and focus inlay
- `chaosx_focus_tree_auditor`
- `chaosx_decision_mission_auditor`
- `chaosx_country_package_auditor`
- `chaosx_localisation_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_spreadsheet_doc_worker`
- portrait and asset workers according to the asset prompt
- super-event text and audio researchers according to the super-event prompt
- mandatory near-completion `chaosx_improvement_loop_planner`

Every patch-capable subagent must write a handoff under the Event 067 plans folder.

## Mandatory improvement-loop closure

Near completion, the implementation agent must spawn `chaosx_improvement_loop_planner` with a complete context-free prompt.

The resulting addendum must be:

- implemented and folded into the specs
- queued with a reason
- rejected with a reason
- or recorded as a closure handoff

Completion is blocked while an accepted addendum remains unresolved.

## Required implementation report

The final implementation report must include:

- files changed
- event lifecycle implemented
- character and trait audit
- decisions and missions
- removal methods and chance scenarios
- civil-war strength and territory scenarios
- country package
- focus route coverage table
- Command Cohesion behavior
- AI and probability evidence
- manual scenario coverage
- world-end coverage
- Event Logs and Event Details
- cluster alignment
- assets and super-events
- achievements
- workbook and CSV export alignment
- no-DLC behavior
- multiplayer behavior
- remaining blockers
- simplifications or explicit statement that none were made

## Forbidden simplifications

The implementation must not substitute:

- an ordinary strong general for the maximum package
- an existing commander renamed as the Generalissimo
- separate ruler and commander clones
- one fixed 50 percent civil-war split
- one random block of rebel states
- free spawned divisions without resource accounting
- a fixed tag without collision audit
- a generic focus tree
- a short vertical focus chain
- a flat permanent army bonus instead of Influence and decisions
- an inevitable timed coup
- political-power-only countermeasures
- a full-screen GUI with little functional need
- default or reused super-event audio
- a generated real-person portrait
- placeholder flags or icons
- direct CSV edits
- a world-end that simply creates one larger civil war

## Explicit non-requirements

The accepted Event 067 design does not require:

- custom technology
- custom doctrine
- custom equipment
- custom sub-unit
- 3D model
- skeletal animation
- unit sound package
- bespoke unit counter
- formable nation
- exact-state formable puzzle
- animated portrait
- animated category picture

Adding one of these surfaces would require a separate accepted design reason. They should not be added as decoration.
