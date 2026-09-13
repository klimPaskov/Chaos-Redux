# Event 045 implementation acceptance criteria

## Identity and registration

- Event ID `45`, entry `chaosx.nr45.1`, Minor Fire-Once, and Chaos level `1` remain aligned across registration, localisation, Event Details, docs, and catalog.
- Event 045 is registered in the Wars cluster with High member severity.
- The event stays disabled in the default reworked-event allowlist until every required surface is ready.
- Invalid automatic selection shows `N/A`, not a misleading zero weight.

## Opening validity and transaction

- At least three valid ordinary regional governments are required.
- Every participant has a current geographic, claim, guarantee, faction, ideology, or strategic connection to the selected dispute.
- Two camps are the normal opening.
- A three-sided opening requires a proven conflict graph and no missing hostile edge.
- Same-faction governments are not placed in opposing opening camps.
- Special Chaos and actual nonhuman countries are excluded from ordinary camp construction.
- Dead, capitulated, territoryless, and nonviable actors fail closed.
- The opening transaction either creates the complete valid war graph or rolls back all temporary setup.
- The outbreak begins immediately after successful setup.

## Balkan War Escalation

- Exactly one persistent public custom value exists.
- The meter uses the accepted 0 to 100 range and five named stages.
- Time alone never raises escalation.
- Every increase and decrease has a material cause and repeat guard.
- Support uses cumulative tiers rather than one reward per click.
- The Powder Keg Explodes requires direct opposing major or major-faction war proof.
- Another World War requires wider-war proof and cannot be reached by score alone.
- Irreversible floors apply after direct major commitments where the spec requires them.
- Latest cause, next threshold, and missing proof display correctly.

## Claims and settlements

- One maintained registry supplies regional interests and claim groups.
- Exact state groups are verified with installed map data and HOI4 map tools.
- No generic occupation-to-claim shortcut exists.
- Other event-owned claims are read without duplicate ownership.
- Settlement terms depend on active claims, occupation, surviving governments, and event state.
- Status quo, limited revision, corridor, justified subject, verified partition, frozen armistice, and wider-war continuation routes have distinct validity rules.
- Peace cleanup removes temporary war goals, decisions, missions, and settlement targets.
- Only defined postwar memories remain.

## Decisions and missions

- One ordinary decision category and one static category picture are used.
- The category exposes three to five primary actions in normal phases, never more than six.
- Active missions stay between one and three.
- Country lists use selected-target presentation.
- Every action has at most four spendable cost types and correct texticons.
- Costs and requirements match the action and are not hidden in effects.
- Missions require concrete state, unit, supply, rail, port, corridor, occupation, or diplomatic work.
- Success, partial success, and failure use distinct logic.
- AI has an equivalent route for every meaningful human action.
- Obsolete and invalid actions clean up after role, target, war, or lifecycle changes.

## Evolutions

- Evolution I requires 200 or more Chaos, separate pacing, and broader registered ambitions.
- Evolution II requires 400 or more Chaos, severe proven weakening, and a valid provider-backed actor.
- Evolution III requires 600 or more Chaos and a concrete former-ally dispute.
- Evolution state itself changes no Chaos.
- Disabled Evolutions do not set recorded flags, create actors, open decisions, or unlock later stages.
- Each Evolution appears correctly in the main Evolutions tab, related-history view, and Event Details catalog.
- Evolution actor, tier, stage, event identity, date, and enabled state remain aligned.

## AI and probability

- Every weighted surface has a baseline P45 scenario audit.
- Owner-selected balance changes receive a same-scenario `hoi4.probability_compare` pass.
- Invalid actions and targets evaluate to unavailable or zero.
- Regional AI weighs survival, supply, claims, sponsors, capital security, and settlement feasibility.
- Outside AI weighs ideology, rivalry, access, reserves, current war load, guarantees, factions, and containment partners.
- Complete defeat prevents endless AI settlement refusal.

## Shared systems and Chaos

- Generic wars, peace, deaths, annexations, puppeting, and faction changes use their existing shared sources.
- Event 045 does not duplicate those Chaos changes.
- Any event-owned Chaos source is separately defined, one-shot or bounded, and logged through Chaos History.
- Shared Deaths, migration, famine, and civilian routing use their own owner contracts when consequences reach them.
- The event does not add a broad recurring whole-world scan.

## Presentation and assets

- Opening outbreak and verified world-war handoff each have a distinct complete super-event package.
- The final stage is presented as a wider-war handoff, not a terminal world end.
- Quotes and cultural references are verified and not invented.
- Audio is licensed, musical, unique unless reuse is explicitly approved, settings-aware, and documented.
- Required report art, category art, decision icons, mission icons, and six achievement triplets are final and wired.
- No placeholder, unrelated reuse, primitive local drawing, or opaque-square alpha failure remains.
- No unrequested portrait, flag, 3D model, custom tag, or dedicated scripted GUI is added.

## Achievements

- All six achievement definitions, trackers, disqualifiers, localisation, icon triplets, and persistence rules exist.
- Achievements read the event's gameplay ledgers rather than duplicate registries.
- Invalid generations and false origin states cannot unlock achievements.
- Delayed and post-handoff achievements survive save and reload.

## Logs, docs, and catalog

- History records the event once with a meaningful actor context.
- Event Details explains the premise, public escalation stages, and three Evolutions without implementation notes or hidden spoilers.
- Stage reports and Evolution logs do not duplicate ordinary history entries.
- Event docs, super-event research, audio catalog, asset provenance, completion report, and source package are aligned.
- The authoritative workbook is updated after final player-facing wording exists.
- The three catalog CSV snapshots are regenerated and not edited directly.

## Required final scenarios

- normal two-camp opening
- justified three-sided opening
- insufficient candidates
- all candidates in one faction
- fragmented Yugoslav region
- opening rollback after one late validation failure
- contained regional settlement
- Evolution I claim settlement
- Evolution II provider-backed fragmentation
- Evolution III former-ally rupture
- direct major intervention and escalation floor
- score threshold without proof
- verified Another World War origin
- rejection of false origin during a pre-existing global war
- each Evolution disabled
- every achievement positive and main negative case
- save and reload during opening, Evolution, armistice, settlement, and post-handoff tracking

The implementation is incomplete while any criterion above is missing, simplified, unwired, unaudited, or supported only by a placeholder.
