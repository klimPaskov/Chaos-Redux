# Event 062 acceptance scenarios

## Purpose

These scenarios are implementation acceptance criteria. Source-only reasoning is not enough where the repository requires MCP or live game evidence.

## Event availability and selection

### AB-ACC-001 No factions

**Setup:** no valid faction exists.

**Pass:** Event 62 is unavailable, Event Details shows an appropriate unavailable state, normal manual trigger does not create targets, cluster firing skips the member with a clear reason.

### AB-ACC-002 One valid faction

**Setup:** exactly one faction passes all Event 62 gates.

**Pass:** event remains unavailable because one normal firing must affect multiple factions.

### AB-ACC-003 Two bilateral factions

**Setup:** two valid factions each contain a leader and one ordinary partner.

**Pass:** both factions can be affected, each partner is expelled, each transaction remains independent, and no duplicate war is created.

### AB-ACC-004 Mixed valid pool

**Setup:** eight factions, three invalid through cooldown, subject conflict, or special-actor rules.

**Pass:** selector draws only from the five valid factions and never retries an invalid faction after the bounded replacement pool is exhausted.

### AB-ACC-005 Fresh faction grace

**Setup:** a faction formed `90` days earlier.

**Pass:** faction is excluded until the central grace period ends.

### AB-ACC-006 Repeat cooldown

**Setup:** a faction resolved Event 62 `300` days earlier.

**Pass:** faction is not selected. After the configured cooldown, it becomes eligible if all other gates pass.

## Victim selection

### AB-ACC-010 Clear weakest member

**Setup:** one member is clearly weakest in divisions, manpower, equipment, industry, territory, contribution, and war position.

**Pass:** probability evidence ranks it first. Selection remains weighted and reproducible under a declared seed.

### AB-ACC-011 Strategic hinge protection

**Setup:** a weak member controls the only supplied port and rail corridor for an active front.

**Pass:** strategic utility reduces its victim priority compared with a similarly weak nonessential member.

### AB-ACC-012 High-contribution casualty case

**Setup:** one damaged member has high contribution, another has low losses and negligible contribution.

**Pass:** loss history alone does not force selection of the high-contribution country.

### AB-ACC-013 Strong core member

**Setup:** the strongest nonleader has poor leader relations.

**Pass:** core protection remains material. It can become a rare target only when the full adjusted score supports it.

### AB-ACC-014 Human victim

**Setup:** player country is the valid weakest member and has no protection.

**Pass:** player can be selected, receives the victim event, inherits all crisis tools, and no AI-only effect is required to survive.

### AB-ACC-015 Human protection

**Setup:** same player was a victim within `1,095` days.

**Pass:** player country is invalid as a victim until protection ends.

## Political units and subjects

### AB-ACC-020 Overlord bundle

**Setup:** an overlord and two subjects belong to the same faction.

**Pass:** they form one political unit for size, target count, and side choice.

### AB-ACC-021 Opposing subject preference

**Setup:** a subject has strong victim relations but its overlord stays loyalist.

**Pass:** subject does not defect independently. Event 62 can request owner-controlled independence only at the proper Evolution and waits for proof.

### AB-ACC-022 Subject release success

**Setup:** subject-release owner accepts an Evolution II request.

**Pass:** independence completes before side assignment, no subject-overlord war contradiction remains, and the released country receives one role receipt.

### AB-ACC-023 Subject release failure

**Setup:** owner rejects or cannot resolve independence.

**Pass:** subject remains with overlord. No partial side change or duplicate faction membership occurs.

## War graph and diplomacy

### AB-ACC-030 Immediate legal war

**Setup:** loyalists and victim share no active war and no blocking diplomacy remains.

**Pass:** expulsion occurs once, delayed revalidation passes, one legal conflict begins, and correct countries join each side.

### AB-ACC-031 Shared war separation

**Setup:** loyalists and victim currently share a war side against a third country.

**Pass:** event uses a verified separation route before hostility. No country is simultaneously ally and enemy in the same war.

### AB-ACC-032 Shared war cannot separate

**Setup:** no safe engine route exists.

**Pass:** armed-expulsion-pending-war state begins, no illegal declaration occurs, the declaration mission rechecks boundedly, and the crisis can still settle or launch later.

### AB-ACC-033 Existing loyalist-victim war

**Setup:** selected countries are already at war on matching sides.

**Pass:** event attaches context to the existing war and does not create a duplicate.

### AB-ACC-034 Expeditionary forces

**Setup:** loyalist controls victim expeditionary forces and victim controls loyalist forces.

**Pass:** forces return or follow a verified safe precedent before war. No unit ownership corruption occurs.

### AB-ACC-035 Withdrawal access

**Setup:** victim divisions stand inside loyalist territory at expulsion.

**Pass:** temporary withdrawal access or another verified route prevents immediate trapping. Access ends cleanly after the window.

### AB-ACC-036 Outside guarantee

**Setup:** a third country guarantees the victim.

**Pass:** Event 62 preserves the outside guarantee unless an explicit legal rule changes it. Sponsor and intervention logic read the guarantee.

### AB-ACC-037 Target annexed during delay

**Setup:** victim ceases to exist between expulsion and delayed war launch.

**Pass:** declaration cancels, cleanup runs, betrayal memory remains, no invalid event target is used.

### AB-ACC-038 Leader annexed during delay

**Setup:** original leader ceases to exist.

**Pass:** a valid loyalist successor is selected from the snapshot or the conflict closes. No dead country declares war.

## Multi-victim cooperation

### AB-ACC-040 Two victims

**Setup:** one faction expels two valid members under Evolution I.

**Pass:** victims receive non-aggression, safe access, one liaison opportunity, and a shared settlement position. They do not attack each other automatically.

### AB-ACC-041 Poor victim relations

**Setup:** two victims strongly dislike each other.

**Pass:** basic non-aggression still prevents accidental war. Liaison acceptance and cohesion are lower. Separate peace remains possible.

### AB-ACC-042 Equipment pooling

**Setup:** one victim has surplus and one has shortage.

**Pass:** explicit donor decision transfers the correct paid amount once, respects reserve floors, and writes a receipt.

### AB-ACC-043 Successor compact

**Setup:** three surviving victims reach unified cohesion and peace.

**Pass:** a legal successor faction or pact forms once, chooses a valid leader, receives `365` day protection, and removes temporary liaison state.

## Decisions and missions

### AB-ACC-050 Category role variants

**Setup:** open the category as leader, retained member, victim, group leader, neutral member, and sponsor.

**Pass:** each role sees only relevant status and actions. No phase displays more than six primary actions or three missions.

### AB-ACC-051 Dynamic cost scaling

**Setup:** compare small, medium, and major countries taking the same action.

**Pass:** costs scale within documented floors and caps, show correct icons, and never contain more than four spendable types.

### AB-ACC-052 Unpayable action

**Setup:** country lacks one required resource.

**Pass:** action is blocked with concise exact reason. AI weight is zero.

### AB-ACC-053 Hold mission success

**Setup:** victim holds capital and route for the full objective.

**Pass:** mission auto-completes, cohesion and settlement leverage change once, achievement receipt updates.

### AB-ACC-054 Hold mission partial success

**Setup:** capital remains held but supply route fails.

**Pass:** partial result differs from success and failure. The player receives a meaningful follow-up.

### AB-ACC-055 Punitive mission failure

**Setup:** loyalist does not meet occupation or surrender proof before deadline.

**Pass:** loyalist cohesion falls, settlement pressure rises, and the mission cannot be farmed by restart or duplicate activation.

### AB-ACC-056 Armistice violation

**Setup:** accepted conference terms are broken by a proven signatory.

**Pass:** conference closes, violation memory records once, optional Event 62 Chaos source records once, renewed war uses shared Chaos normally.

## Evolution I

### AB-ACC-060 Pre-fire Evolution I

**Setup:** Chaos `200+`, Evolution enabled, enough valid factions and victims.

**Pass:** expanded faction or victim budget applies from the opening, and the Evolution logs only when expanded behavior occurs.

### AB-ACC-061 Evolution I disabled

**Setup:** same world state with Evolution I disabled.

**Pass:** baseline faction and victim caps apply. Structured liaison content does not open through the Evolution.

### AB-ACC-062 Threshold reached during active crisis

**Setup:** Chaos crosses `200` after baseline firing.

**Pass:** Evolution behavior waits for dynamic pacing and proof. No instant log occurs at the threshold.

## Evolution II

### AB-ACC-070 Valid split

**Setup:** six political units, two victims, two credible defectors, legal war graph.

**Pass:** side choices resolve, both sides remain viable, defectors move once, and Evolution II logs with the first actual split.

### AB-ACC-071 No tension proof

**Setup:** six highly cohesive members fighting one existential enemy.

**Pass:** no full split occurs solely because the timer ended. Baseline purge remains possible.

### AB-ACC-072 Neutral withdrawal

**Setup:** distant exhausted member cannot safely join either side.

**Pass:** neutral exit applies with truce and diplomatic isolation. It does not join the victim war.

### AB-ACC-073 Leader isolated

**Setup:** majority of core members defect legally.

**Pass:** original leader remains legal head of a rump faction, while the defecting coalition becomes the dominant opposing bloc. No unsafe direct leader expulsion occurs.

### AB-ACC-074 Evolution II disabled

**Setup:** valid split state with Evolution II disabled.

**Pass:** Event 62 side-switch actions and weights are zero. Other independent faction systems remain unaffected.

## Evolution III

### AB-ACC-080 Mutation budget

**Setup:** four large factions all qualify for full splits.

**Pass:** no more than three full splits and eighteen political-unit mutations occur.

### AB-ACC-081 Evolution log threshold

**Setup:** two large factions split and six units change side or withdraw.

**Pass:** Evolution III logs once. Super-event does not fire unless its stricter threshold is met.

### AB-ACC-082 Super-event threshold

**Setup:** three eight-unit factions split and twelve units move.

**Pass:** the one-time super-event fires with correct image, text, audio, settings volume, and history. The distinct `+5` Chaos source records once if retained after shared-source audit.

### AB-ACC-083 Super-event near miss

**Setup:** two large factions split and five units move.

**Pass:** no super-event and no world-order Chaos source.

### AB-ACC-084 Evolution III disabled

**Setup:** same collapse world with Evolution III disabled.

**Pass:** only enabled lower-Evolution behavior occurs. No large-faction bonus, Evolution III log, or super-event appears.

## System connections

### AB-ACC-090 Wars cluster firing

**Setup:** Wars cluster selects Event 62 and at least two valid factions exist.

**Pass:** cluster counts once for pacing, Event 62 applies its own effects and repeatable cap state, and cluster history records the member result.

### AB-ACC-091 Wars cluster skip

**Setup:** cluster selects Event 62 with one valid faction.

**Pass:** member skips with exact reason and no partial purge.

### AB-ACC-092 Random Civil War overlap

**Setup:** a victim is internally unstable and civil war owner accepts the request.

**Pass:** Random Civil War owns the split, Event 62 revalidates roles, and no duplicate civil war or army transfer occurs.

### AB-ACC-093 Third Balkan War overlap

**Setup:** selected faction is already inside an Event 45 owned former-ally split.

**Pass:** Event 62 does not duplicate the war. It selects another faction when possible or skips the overlapping transaction.

### AB-ACC-094 The Offensive comparison

**Setup:** run same seed with The Offensive inactive and active.

**Pass:** aggressive choices become more likely when legal and viable. Invalid actions remain impossible and hopeless settlement behavior remains rational.

### AB-ACC-095 Forced faction exit Chaos

**Setup:** one Event 62 expulsion with shared faction-leave Chaos enabled.

**Pass:** the forced hostile exit does not produce the ordinary negative faction-leave Chaos. War sources remain normal.

## Multiplayer and persistence

### AB-ACC-100 Two players in one faction

**Setup:** one player is leader, one player is victim.

**Pass:** both receive consistent role events. The transaction applies once and decisions remain role-correct.

### AB-ACC-101 Two player victims

**Setup:** two players are expelled together.

**Pass:** both receive the same victim-group identity, can coordinate, and cannot duplicate liaison creation.

### AB-ACC-102 Tag switch after selection

**Setup:** control switches from one country to another after roles are locked.

**Pass:** roles follow countries, not controllers. The new player inherits the country's active category.

### AB-ACC-103 Save during delayed war phase

**Setup:** save after expulsion and before revalidation, then reload.

**Pass:** one delayed phase completes, one war or pending-war state appears, and no receipt duplicates.

### AB-ACC-104 Save during settlement

**Setup:** save with an offer pending, then reload.

**Pass:** terms, signatories, mission timer, and selected target remain correct. Acceptance applies once.

## Cleanup

### AB-ACC-110 Ordinary settlement cleanup

**Pass:** category, missions, pending targets, temporary access, and ideas remove or transform. Durable memories remain.

### AB-ACC-111 Faction dissolves

**Pass:** active registry removes the transaction, ordinary wars remain, no stale faction leader target persists.

### AB-ACC-112 All victims destroyed

**Pass:** transaction closes, loyalist outcome records, no repeated cleanup or dead-country events occur.

### AB-ACC-113 Wider-war handoff

**Pass:** Event 62 stops micromanaging the war, preserves roles, and leaves ordinary war state untouched.

### AB-ACC-114 Long campaign leak check

**Setup:** fire Event 62 repeatedly across several years with different generations.

**Pass:** active arrays contain only current leaders, no stale country flags or selected targets remain, cooldowns expire correctly, and event processing does not grow without bound.

## Documentation and catalog acceptance

### AB-ACC-120 Event surfaces

**Pass:** event name, Event Details, history, Evolution rows, actor handling, Chaos level, enabled state, and cluster membership agree with implementation.

### AB-ACC-121 Catalog workbook

**Pass:** authoritative XLSX row contains the accepted player-facing details, three Evolutions, Minor Repeatable type, Chaos level 1, Wars cluster, High severity, and final status. CSV exports are regenerated, not edited directly.

### AB-ACC-122 Asset coverage

**Pass:** every accepted event picture, category picture, decision icon, mission icon, idea icon, achievement icon, and conditional super-event asset has a runtime consumer. No unapproved portrait, flag, focus icon, 3D model, counter, or animation was added.
