# Requirements and validation matrix

## How to read acceptance status

This matrix preserves 97 distinct requirements extracted from the complete user brief.
The source references point to the package parts that specify each requirement.
For gameplay, assets, native UI, persistence and multiplayer, those references are design coverage rather than completed implementation evidence.
A future coding parent must attach the actual source, artifact or runtime result before marking that requirement implemented.

The supplied-source reading gate, historical research and design mathematics have separate completed evidence below.
The planning package can be complete while the expressly future implementation and production work remains unperformed.
A missing planning rule or contradictory accepted design is a planning defect and must be resolved before delivery.

## Brief coverage

| Requirement | Material brief requirement | Testable acceptance | Package parts |
| --- | --- | --- | --- |
| B01 | Event identity is 108, original catalog ID 113, Wrestling Tournament, Minor Repeatable, To Be Reworked, Chaos 1, no assigned cluster | Registration, specs, final catalog and descriptions use the current identity consistently, with old export numbering reconciled explicitly | 01, 08, 09 |
| B02 | Each firing creates a fresh complete competition | Every committed opening has a distinct edition ID, new participants, preparation, draw, results, incidents, champion settlement and history, while reusing eligible careers | 01, 08, 09 |
| B03 | The competition is a living connected system | Candidate, preparation, injury, match, inquiry and career outcomes read and modify the same authoritative entrant and edition records | 01, 08, 09 |
| B04 | Six ordinary phases remain recognizable | Announcement/entry, preparation, lock/seeding, knockouts, final/award, history/return each have entry, exit, dates, player actions and retained records | 01, 08, 09 |
| B05 | Preparation permits several strategic actions and responses | The default schedule supports multiple meaningful camp and rest/incident decisions, publishes registration and first-bout dates, and does not become an instant single bonus | 01, 08, 09 |
| B06 | Post-lock expenditure cannot rewrite seeds or played matches | Any allowed post-lock action can affect only a permitted future condition and cannot mutate lock snapshots, pairings or committed result inputs | 01, 08, 09 |
| B07 | Repeatable editions cannot conflict | Natural, forced, duplicate and pending requests cannot create two active brackets, fees, firings, rewards or history openings | 01, 08, 09 |
| B08 | Prior editions remain inspectable during later preparation | Archived draw and selected details remain stable while an active edition updates its own records | 01, 08, 09 |
| B09 | International roster includes majors and minors | Eligible selection is not a hidden major-power-only pool, and admission or AI refusal has a recorded actual reason | 01, 08, 09 |
| B10 | Campaign eligibility reflects living authority, representation and relevant obstacles | Recheck existence, independence/autonomy, travel, medical/disciplinary eligibility and genuine owner state at each public commitment point, with meaningful blocked text | 01, 08, 09 |
| B11 | A country sends one chosen contender | A country has at most one accepted entrant per edition and a wrestler cannot be reserved or entered for two countries | 01, 08, 09 |
| B12 | Candidate selection is small, meaningful and variable | Multiple distinct candidates differ in profile, condition, record or risk, with credible alternatives and offers that vary across campaigns/editions without tab, cancel or reload rerolls | 01, 08, 09 |
| B13 | Veterans, challengers, specialists and surprise talent are supported | Candidate generation can supply those useful identities without requiring every country to use identical roles or stat profiles | 01, 08, 09 |
| B14 | All six attributes have distinct mechanical meaning | Strength, Technique, Endurance, Speed, Toughness and Adaptability are stored independently and each changes an appropriate training or match situation | 01, 02, 03, 06, 08 |
| B15 | Selection is informed while future outcomes remain uncertain | The player sees useful attribute comparisons, known reputation, record, condition, injury and preparation without future rolls or secret violations | 01, 02, 03, 06, 08 |
| B16 | Size alone is not optimal | At least one credible smaller technical/agile profile can counter a powerful opponent, with tradeoffs and nonzero failure chances | 01, 02, 03, 06, 08 |
| B17 | Returning champions and rematches exist | An eligible past champion can be offered again, actual previous rivals can meet through the fixed draw, and reporting recognizes the history | 01, 02, 03, 06, 08 |
| B18 | Career and national reputation develop without permanent dominance | Previous appearances, wins, losses, injuries, suspensions, reputation and rivalries affect later editions through bounded dated adjustments | 01, 02, 03, 06, 08 |
| B19 | Initial portrait production target is at least 80 usable identities | The asset plan contains 80 or more distinct identity/portrait production records, with statuses and expansion to supported candidate demand rather than a fabricated completion count | 05, 10, 13, asset prompt |
| B20 | Full brackets contain distinct faces for distinct entrants | A 32-person edition has 32 identity-appropriate nonduplicated portraits, and selection, qualifiers, main draw and archives do not use anonymous or unrelated substitutions | 05, 10, 13, asset prompt |
| B21 | Portrait library covers varied regions, physique, style, age and return | The roster coverage table has meaningful variation and historical availability, with shortages explicitly recorded | 05, 10, 13, asset prompt |
| B22 | Many portraits use correct real verifiable sources | Historical identities have correct-person source, author/archive/page, date, provenance, rights status and identity/framing review | 05, 10, 13, asset prompt |
| B23 | Grounded source gaps are honest blockers | Missing or uncertain historical faces are marked unresolved, with no invented likeness, unverified public-domain claim or unrelated photograph | 05, 10, 13, asset prompt |
| B24 | Ordinary, real, fictional and impossible identities have clear source modes | Each identity records classification and correct portrait production route before art assignment, with impossible creatures allowed fictional production | 05, 10, 13, asset prompt |
| B25 | Named wrestlers keep one stable face across consumers | A stable identity and portrait reference is used by selection, previews, bracket, reports, achievements and future appearances, with historical snapshot retained | 05, 10, 13, asset prompt |
| B26 | Portrait creator owns research through final portrait wiring | Every portrait task routes to `chaosx_portrait_creator`, with production status, provenance, crop, DDS, wiring and handoff, without claiming assets already exist | 05, 10, 13, asset prompt |
| B27 | Preparation offers all seven training directions | Strength, Technique, Conditioning, Speed/reaction, Opponent study, Rest/rehabilitation and Balanced camp each have distinct effect, cost, timing, risk and follow-up | 02, 03, 04, 06, 08, decision/mission prompt |
| B28 | Training effects and tradeoffs match direction | Strength can cause overwork/injury, technique counters power, conditioning supports long rounds, speed has sustained-grapple limits, scouting targets styles, rest preserves health and balanced training spreads smaller gains | 02, 03, 04, 06, 08, decision/mission prompt |
| B29 | Funding supports real preparation inputs | Coaching, facilities, travel, support, medicine and specialization scale with actual political, industrial/logistical/experience capacity and wartime opportunity cost | 02, 03, 04, 06, 08, decision/mission prompt |
| B30 | No standalone wrestling currency or giant training shop | Actions use fitting existing resources, staged opportunity and lifecycle, with concise focused visible choices | 02, 03, 04, 06, 08, decision/mission prompt |
| B31 | Investment helps without guaranteeing a title | Diminishing returns, condition/risk, matchup and random limits preserve loss chances at maximum legal investment | 02, 03, 04, 06, 08, decision/mission prompt |
| B32 | Small countries can compete through intelligent choices | Low-budget valid profiles have credible strategies and tournament win paths, while rich countries can fail through preparation or matchup errors | 02, 03, 04, 06, 08, decision/mission prompt |
| B33 | Baseline scandals are available before any evolution | Cheating, period enhancements, risky scientific preparation, sponsorship/political demands, injury/recovery and eligibility/travel/referee disputes exist at Chaos 1 with all four evolutions inactive | 02, 03, 04, 06, 08, decision/mission prompt |
| B34 | Baseline cheating contains meaningful varied cases | Bribery, compromised officials, illegal holds, fixing rumors, concealed help or suspect results can lead to clearing, punishment, local delay or wider exposure | 02, 03, 04, 06, 08, decision/mission prompt |
| B35 | Period enhancements trade benefit for health and sanctions | A short-lived benefit has period-fit access, injury/recovery/DQ/disgrace risks and a competitive clean alternative | 02, 03, 04, 06, 08, decision/mission prompt |
| B36 | Experimental preparation uses actual technology access | Ordinary devices fit the setting, exceptional capabilities require actual sponsor-owned existing science, and wrestling cannot conjure the program | 02, 03, 04, 06, 08, decision/mission prompt |
| B37 | Patronage and politics create choice rather than automatic benefits | Reckless demands, publicity, special treatment and politically vital victory can be accepted, rejected, investigated, concealed or addressed where sensible | 02, 03, 04, 06, 08, decision/mission prompt |
| B38 | Injuries and recovery change readiness and eligibility | Fatigue, strains, accidents, manageable recovery and severe inability have dated effects, tactical meaning and replacement only before lock | 02, 03, 04, 06, 08, decision/mission prompt |
| B39 | Allegations and proven wrongdoing stay distinct | An unproven complaint does not always destroy an innocent entrant, and investigation can clear, substantiate, fail or remain unresolved | 02, 03, 04, 06, 08, decision/mission prompt |
| B40 | Responses have real time, reputation, diplomatic or competitive cost | Costs are quoted before action, consumed once, and produce appropriate response, delay, sanction or public exposure | 02, 03, 04, 06, 08, decision/mission prompt |
| B41 | Honest competition remains viable | Clean entrants retain credible success at baseline and evolved levels, and AI considers long-term health, evidence, reputation and war priorities instead of choosing maximum strength | 02, 03, 04, 06, 08, decision/mission prompt |
| B42 | Literal state-backed seeded elimination bracket | Separate event-owned native GUI renders actual flags, identities, seed numbers, pairings, outcomes and future advancement paths from tournament records | 01, 03, 05, 08 |
| B43 | Typical 16/32 draws adapt to real field | Main draw policy handles supported smaller fields and more than available spaces, including arbitrary applicant counts rather than only exact powers of two | 01, 03, 05, 08 |
| B44 | Excess applicants are not silently ignored | Published eligibility/admission and recorded qualification give every accepted applicant a stated entry path or recorded exclusion reason | 01, 03, 05, 08 |
| B45 | Byes are fair and legitimate | Byes follow a published seed-based rule, occupy real paths and have distinct non-bout records without fake defeated opponents | 01, 03, 05, 08 |
| B46 | Seeding combines record, form, quality, reputation and preparation | Defined bounded inputs determine final ranking with deterministic published tie handling and a lock snapshot | 01, 03, 05, 08 |
| B47 | Leading seeds are separated appropriately | Seeds 1/2 occupy opposite halves, next leaders separate across quarters or suitable sections, and normal top seeds do not face each other in round one | 01, 03, 05, 08 |
| B48 | Rest of draw mixes contenders, qualifiers and lower seeds | A complete participant-to-leaf mapping contains every admitted wrestler once and gives qualifiers real stable paths | 01, 03, 05, 08 |
| B49 | Seeds are advantage rather than outcome | Ordinary favorite scenarios have credible advantage while unseeded or weak-reputation candidates have nonzero possible win/title paths | 01, 03, 05, 08 |
| B50 | Published draw is immutable | Withdrawals, DQs, new careers, rivalry requests, science access and evolved corruption cannot reseed, reorder or regenerate locked survivors | 01, 03, 05, 08 |
| B51 | Withdrawals/DQs/inability follow explicit advancement rules | Every affected node records walkover or announced consistent outcome, handles both entrants unavailable, and never strands an ancestor node | 01, 03, 05, 08 |
| B52 | Replacement is limited to pre-lock | Nominee replacement preserves identity-specific gains and leaves remaining time/costs explicit, with no later entrant inserted after lock in the current early design | 01, 03, 05, 08 |
| B53 | Window entry points and durable access | Announcement, tournament decisions and later notifications open the same window, eliminated players and spectators retain access, and completed brackets remain reviewable | 03, 05, 08, 09 |
| B54 | Complete progression is readable at supported fields | Full bracket via scrolling/round selection shows connected path from entry rounds through semis/final and highlighted title route | 03, 05, 08, 09 |
| B55 | Every entrant has identity and status | Opening seed, snapshotted flag/affiliation, wrestler name, distinctive portrait and current official status are shown consistently | 03, 05, 08, 09 |
| B56 | Every result and next match is understandable | Completed node shows participants, winner/loser, decisive result and official amendment, with next entrants and expected date | 03, 05, 08, 09 |
| B57 | Bye, withdrawal, DQ and upset explanations differ | Distinct result classes and concise reason text appear in bracket and reports rather than every advance displaying as a victory | 03, 05, 08, 09 |
| B58 | Selectable profile and match details expose known facts | Selection reveals known record, preparation, current condition and actual match history, with own entrant highlighted | 03, 05, 08, 09 |
| B59 | Historical compact view preserves important results | Prior champions, major upsets, rivals and sanctions have stable compact entries and archive detail without stale active selection | 03, 05, 08, 09 |
| B60 | Bracket updates immediately from authoritative outcomes | Commit once then publish every linked row/path/status, with same player/AI record and no extra GUI-side randomization | 03, 05, 08, 09 |
| B61 | Player chooses meaningful pre-match approach | Overpower early, technical counters, conserve energy and balanced approach use candidate/opponent information and preparation without bypassing AI fairness | 02, 03, 06, 08 |
| B62 | Outcomes reflect attributes, fatigue, readiness, style, preparation and controlled randomness | Declared equations and complete candidate outcomes respond appropriately to varied profiles and evolving round condition | 02, 03, 06, 08 |
| B63 | Round attrition changes later prospects | Long earlier bouts, readiness loss, injury and Endurance/Toughness matter to late rounds, with bounded recovery between scheduled matches | 02, 03, 06, 08 |
| B64 | Strong favorites can lose and rooted upsets are uncommon | Probability scenarios prove credible ordinary favorite advantage, nonzero upset floor/ceiling, and circumstance-dependent underdog gains without invincible reputation | 02, 03, 06, 08 |
| B65 | Multiple legitimate result types exist | Convincing win, narrow decision, surprise pin/submission, long referee decision, DQ and walkover have differentiated records and reporting | 02, 03, 06, 08 |
| B66 | Adjudication is local and does not rewrite unrelated bouts | Inquiry can amend one official status or sanction while preserving immutable original receipts and legitimately played unrelated results | 02, 03, 06, 08 |
| B67 | Player elimination does not end the global tournament | Early loss removes participant authority while reports, spectating, underdog follow and title progression continue | 02, 03, 06, 08 |
| B68 | Live scandals have sensible outcomes | Illegal assistance, drugs, biased official or unsafe treatment can produce success/failure/unproven inquiry, bout loss, DQ, suspension, title dispute, false-accuser embarrassment or public spectacle | 02, 03, 06, 08 |
| B69 | Loud accusation does not automatically win | Complaint evidence, investigator outcome and rulebook decide the sanction rather than claimant nation or player status | 02, 03, 06, 08 |
| B70 | A completed valid edition has one authoritative champion | Final result, settlement, champion record, title count, visible standings and reward agree, including late inquiry, winner injury, DQ and double-unavailability cases | 03, 05, 07, 08 |
| B71 | Champion reward is meaningful and scales appropriately | Prestige/political recognition varies with field, beaten opponents, rivalry and campaign state through bounded authored scaling | 03, 05, 07, 08 |
| B72 | Defenses and giant-killing minors receive distinct recognition | Legitimate title defense and first minor-country champion defeating favorites satisfy defined separate evidence and reward criteria | 03, 05, 07, 08 |
| B73 | Later cheating affects standing without erasing the entire competition | A tainted champion can lose prestige/status under consistent rules while original bout records and unrelated results remain retained | 03, 05, 07, 08 |
| B74 | History snapshots period identity and affiliation | Archive uses name, portrait, flag, country/cosmetic identity and affiliation captured for that edition, even after annexation, ideology/name change, portrait update or career retirement | 03, 05, 07, 08 |
| B75 | Past consequences affect later editions safely | Rivalry, injury, suspension, record and reputation influence future admission, preparation and seed ranking without unfinished brackets or stale targets | 03, 05, 07, 08 |
| B76 | Four evolution tracks are mutations rather than phases | They have separate enable/prerequisite/pacing/log contexts and can occur in any valid order or never, without counting baseline stages as evolutions | 04, 06, 08, 09 |
| B77 | National Obsession at Chaos 200+ | Existing major/rival/champion political stakes influence likelihood, with cautious versus promotional choices and bounded loss backlash, overtraining, spending, supporter and referee consequences | 04, 06, 08, 09 |
| B78 | The Fixed Match at Chaos 400+ | High prestige/stakes/sponsors enable organized corruption choices, possible multi-country scandal, local official sanctions, ranking/reputation/diplomatic consequences, and honest resistance | 04, 06, 08, 09 |
| B79 | Enhanced Athletes at Chaos 600+ | Actual sponsoring medical/biological/industrial/scientific access enables extreme preparation with specialization, weakness, recovery/injury/exposure/DQ risks and human clean win paths | 04, 06, 08, 09 |
| B80 | Open Division at Chaos 800+ and existing supported being | Admission occurs only for an existing valid eligible actor from an owner system, with meaningful identity/portrait, ability to obey/compete and announced safety handling | 04, 06, 08, 09 |
| B81 | Human exceptional entrants retain correct division | Human Spartans enter ordinary division at any time, mythological Age of Heroes entrants require Open Division, and human clones are not misclassified from a nonhuman country tag | 04, 06, 08, 09 |
| B82 | Nonhuman styles have genuine strengths and exploitable weaknesses | Zombies, golems and other admitted beings differ mechanically, can lose to trained humans, and retain controlled safety/withdrawal outcomes | 04, 06, 08, 09 |
| B83 | Wrestling does not create unrelated crises to populate the field | No new outbreak, clone army, alien force, science institution, creature program, owner character or automatic unrelated world-end is spawned by invitation or evolution | 04, 06, 08, 09 |
| B84 | Explicit owner connections stay additive | Event 002 zombies, Event 019 special families, compatible clones/aliens, advanced science/Kruger and Event 111 Sparta use actual origin/capability/entrant records and leave owner systems intact | 04, 06, 08, 09 |
| B85 | Shared harm and other consequences are counted once | Genuine extra civilian/unit harm enters the owning shared subsystem once, while bracket injury or prestige is not fabricated as external casualties | 04, 06, 08, 09 |
| B86 | Player controls candidate, funding, preparation, tactics and important responses | Every accepted player action has clear requirement, cost, result and lock boundary, and needed AI equivalent | 02, 03, 06, 08, 09 |
| B87 | AI uses legitimate informed strategic choices | Candidate/funding/training/tactics/scandal policies use known profile, opponent, war and economy, avoid constant maximal spending or permanent one-person nomination, and share rules | 02, 03, 06, 08, 09 |
| B88 | Player and AI share exact seeding, ties, eligibility and upset rules | Actor control changes neither match equation nor draw/result commit logic, with scenario fixtures that differ only by control flag | 02, 03, 06, 08, 09 |
| B89 | Predictable pacing, persistence and multiplayer synchronization | One field/draw/result per node/champion persists through save/reload, and all clients/spectators render the same records with no local rerolls | 02, 03, 06, 08, 09 |
| B90 | Duplicate awards/resolution and stale identities are prevented | Repeated callbacks/clicks, simultaneous clients, load, stale selections and owner annexation cannot repay/award/reseed/reserve twice or read another edition | 02, 03, 06, 08, 09 |
| B91 | Writing reflects observed bout, stakes, identity and history | Technical win, upset, corruption and monstrous entrance use concrete appropriate facts and distinct tone, with serious injury handled seriously | 05, 09, coding prompt, asset prompt, decision/mission prompt, achievement prompt |
| B92 | GUI and preparation cooperate without extra small-action screens | Native bracket offers progression/profile/tactics while decisions supply concise preparation controls, without duplicated gameplay or a separate full character-management interface | 05, 09, coding prompt, asset prompt, decision/mission prompt, achievement prompt |
| B93 | Visual assets and event-owned sound/animation have clear handoffs | Portraits, match/scandal illustrations, exceptional reveals and any actual sound/animation consumer have owner, source mode, runtime path, state, evidence and parent integration | 05, 09, coding prompt, asset prompt, decision/mission prompt, achievement prompt |
| B94 | Full specs thoroughly expand accepted idea | Numbered specs settle real mechanics, timing, actions, match rules, ownership, AI, assets, acceptance, risks and coding prompts without silent simplification | 00 through 13, all five implementation prompts and package artifacts |
| B95 | Required supplied sources and skills are fully read before writing | Actual source ledger covers every supplied instance and archive requirement, with no skipped, truncated, assumed equal or unreported inaccessible source | 12 and Source Coverage.json |
| B96 | Provided subagents are used honestly and mapped for future work | Actual bounded planning agents are identified as actual, future canonical owner map states inputs, scope, dependencies, outputs and review, and no unavailable native role/MCP use is fabricated | 09, 12 and final review dispositions below |
| B97 | Limitations and simplifications are reported honestly | Mathematical checks, sourced research, plans, unavailable native evidence, future assets and unresolved feasibility are separately labelled, with any deviation explicit | 00, 09, 10, 11, 12 and final report |

## Design-check evidence and limits

The active specification folder does not contain `Design Math Check.py`; the job-specific original remains only in the ignored import snapshot and was assigned to the probability auditor. The separate read-only handoff at [107/108 probability review](../../plans/108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md) reports that the original calculator was inspected and run on 10 October 2026. Its results are abstract design mathematics, not native game validation.
Other counts below are explicitly identified as claims from the immutable imported completion review. This documentation cleanup did not rerun the math checker or audit formulas.

| Check | Reported result | What remains outside this evidence |
| --- | --- | --- |
| Fields 2 through 512 | All 511 field sizes passed exact seed permutation, opposite halves, leading-four quarters and fair highest-seed byes | Native arrays, chunk execution, GUI and actual supported maximum |
| Intact knockout conservation | Every tested field has N-1 contested bouts and no empty-versus-empty opening pair | Later withdrawals, source invalidity and adjudication require implementation fixtures |
| Qualifiers | Every tested field above 32 has N-32 contested qualifiers and 32 unique survivors | Native qualifier display and actual match resolution |
| Reference probability | Symmetry, monotonicity and .04 to .96 bounds passed for integer score differences from -200 through 200 | Native fixed-point lookup and engine random persistence |
| Published probability examples | Delta 0, 12, 24, 40, 60 yield 50.00%,71.26%,85.03%,92.83%,95.38% | Full tournament title probabilities or measured AI behavior |
| Vacancy primitive | Double absence produces no winner and one real entrant advances against absence | Complete multi-node medical, inquiry and retry lifecycle |
| Reserved calendar under field shrink | 130,816 registered-to-locked pairs from 2 through 512 preserve named round dates, five-day spacing and the final date | Actual scheduled callback execution, exceptional delays and source loss |
| Official-bias coupling | The assigned probability handoff reports 2,807 score/bias contexts with nonnegative bands, exact total weight and exact biased winner weight. Official-dependent methods exclude pins and submissions | The calculator's ±6 offsets are test inputs, not a selected cap. Bias magnitude and native implementation remain unresolved |
| All-upset propagation | Selected fields from 3 through 512 preserve identity, unique advancement, original leaves and N-1 contests when every weaker seed wins | Multi-round stochastic campaign balance |
| Independent completion-auditor mathematics | A separate check confirmed the seed and qualifier invariants, approach row sums, method row sums, investigation pools and baseline full incident pool | It remains independent design arithmetic, not native validation |
| Portrait backlog arithmetic | The imported completion review reports 80 explicit work items, 24 researched people and 56 unresolved distinct-person tasks across 22 research contexts | Zero accepted finished assets in that review. Exact worldwide candidate and retained archive demand was not enumerated |
| Supplied-source coverage | The immutable source receipt reports 133 text/config instances, 91 distinct contents, 50 families and 5 ZIP instances processed before drafting | This is the archived intake report. It does not establish current tool exposure or a present checkout scan |

The checker intentionally does not imitate an entire game implementation.
It proves useful properties of the declared design, while the future tests below address actual game-side risks.

## Interacting implementation review fixtures

These rows preserve useful behavior scenarios. Check them through source and meaningful local tests, and use relevant exposed tools when useful. If optional native inspection/rendering or live runtime evidence is unavailable, record that limit rather than treating it as a general completion gate; agents must not launch HOI4 or wait for user testing.

| Fixture | Required setup and observation | Pass condition |
| --- | --- | --- |
| V01 Opening concurrency | Natural selection, forced request, stale request and two simultaneous controllers at entry and cooldown | One accepted edition and firing receipt, no double fee, repeatable-cap reduction or history opening |
| V02 Candidate conservation | Every supported eligible country, three normal candidates, a constrained two-person pool and overlapping human/extraordinary alternatives | Unique person reservations, one nominee per delegation, stable offers and correct actual portrait demand |
| V03 Arbitrary fields | N=0, 1, 2, 3, 5, 12, 15, 16, 17, 31, 32, 33, 47, 63, 64, 65, 128, 257 and the enumerated supported maximum | Explicit small-field closure or unique seed tree, honest byes, complete qualifiers and terminating branches |
| V04 Calendar shrink | Registered 65 to locked 32, 65 to 2, 33 to 17 and any field to 1 | Trailing matching round dates preserved, unused slots are rest, first expected and actual contest dates distinguished, no training reopened |
| V05 Replacement boundary | Replace a trained, injured or suspected nominee before lock, then try after lock | New person receives only remaining opportunity, no transferred gains or hidden wrongdoing, no post-lock admission |
| V06 Payments and capacity | Exactly enough PP/equipment, just below, changed discounts, capacity lost between quote and confirmation, native civilian reservation before/after callback | One actual payment and one reservation owner, clear current quote, inclusive affordability, exact unused refund once |
| V07 Camps and recovery | All seven directions, repeated third specialization, caps, low Readiness, Strain 60/80, 15-day fit and shortened final recovery | Distinct meaningful effects and medical gates, no cancelled full reward or repeated completion roll |
| V08 Match freeze and official bias | Two actual entrants, stale tactic request, both bias signs, neutralized official, middle-band dependent winner, and signed winner-advantage boundaries exactly 0, 12 and 24 | One frozen pair and input set, one winner draw, the correct disjoint method bin at each boundary, referee-only dependent method and unchanged tree |
| V09 Vacancy paths | Single and double withdrawal, DQ, vanished actor, one/two empty successors, sole finalist and no finalists | No phantom opponent or winner, correctly typed advance, explicit vacant title and no duplicate award |
| V10 Retry and common disruption | No contest, repeated no contest, venue loss and inquiry competing for the same 10-day allowance | One same-entrant retry, preserved attempts/attrition, bounded consistent downstream dates and safe interrupted closure when required |
| V11 Timely and late inquiry | Proof before the bout, after bout before successor freeze, after freeze, during settlement and after ratification | Only lawful original-opponent correction before freeze, later prospective sanctions, truthful title amendment and no unrelated replay or second prize |
| V12 Sponsoring country disappears | Before lock, after arrival/lock, before award and after archive, including later tag reuse | Actual representation rechecked, only eligible arrived athlete may continue unsponsored, no annexer authority or misdirected payment |
| V13 Owner programs and species | Actual human clone, nonhuman clone, alien contact without population, valid source population, lost lab service, completed biological alteration, human Spartan and actual mythic figure | Source and species handled independently, actual capability needed, no program or creature spawn to fill the bracket |
| V14 Evolutions | Each threshold's adjacent values, first high-Chaos opening, independent active unlocks, late Open unlock after lock and Chaos falling afterward | Four independent tracks, actual relevant context and valid shared pacing, current committed tree preserved |
| V15 Chaos accounting | Ordinary entry/win/injury, real public disorder, proven network, serious evolved incident, shared casualties and later containment | Part 04's complete source map and caps, no generic double count, no repeated positive or reversal receipt |
| V16 AI strategy | Peace, urgent war, poor country, strong returning champion, near-equal challenger, severe injury and weak evidence | Legal varied choices, spending discipline, plausible recovery and no omniscient hidden tactic or crime knowledge |
| V17 Spectator access | Nonparticipant, eliminated player, country/controller change and old stale window | Full public competition continues, private data withheld, no unauthorized mutation or spending |
| V18 Historical snapshots | Changed country name/flag, annexation, tag reuse, athlete retirement and approved portrait version change | Old edition identity and assets remain stable, current facts are separately labeled and full qualifiers remain available |
| V19 Native UI | Full window at 1920 x 1080 scale 1, 1366 x 768 and 2560 x 1440 scale 1.25, long text, all status and error states | Real connected dynamic tree, readable controls, correct selected identity, at most six primary actions and exactly two numerical management meters |
| V20 Production and animation | Complete candidate source manifest, full 32-person bracket, repeated returning person, required scenes/icons and true frame sequence | Every distinct entrant has its own accepted portrait, stable identity across consumers, actual runtime files, animation frames and static fallback. Optional audio only with proven source/use and native binding |
| V21 Achievements | Every Part 07 positive and negative boundary, clean allegation, actual hidden aid, walkover, late title amendment and absent country | Exact multi-condition predicates, correct triplets, no easy or duplicate unlock, no second title payment |
| V22 Save and multiplayer | Save/load during entry, camp payment, lock construction, qualifiers, frozen match, inquiry, award and archive. Compare actual observers and controller types | Same authoritative IDs, state, outcomes and receipts with no reroll, dropped pending job or copied secret view |
| V23 Repeat and migration | New edition while old archive is selected, schema migration with active event, stale old callbacks and extreme archive page | Safe versioned migration, one active edition, old jobs rejected, history retained, no reset or silent reconstruction of a played tree |
| V24 Shared integration and documentation | Actual default registration, fired handler, log, evolution details, CXT exposure, final text, canonical workbook and regenerated exports | All consumers describe actual implementation and correct identity, registration is idempotent, no premature Playable claim |

Use named coherent scenarios and preserve actual source and tool evidence.
Do not claim a pass merely because a synthetic preview forces the intended condition or a tool reports no parser error.

## Rolling review dispositions

The immutable imported completion review reports five actionable issues from its first complete core review.
It records that the prior parent accepted and integrated all five within the earlier planning scope. This current import preserves that historical claim without renewing acceptance beyond Part 00.

| Finding | Earlier correction as recorded in the immutable receipt | Integration reported by the earlier author |
| --- | --- | --- |
| R01 Official-biased winner could later receive a decisive pin | One coupled clean/biased threshold draw, official-dependent middle band restricted to narrow or long referee decision | Parts 03, 04, 06 and technical handoff, plus the delivered bias mathematics |
| R02 Additional candidates could be counted as additional delegations | Distinct delegation set determines maximum field, unique reserved candidate union determines portrait demand | Parts 05, 10, 13 and technical handoff |
| R03 First contest date conflicted with preserving published rounds after field shrink | Keep earliest competition slot, reserved named round dates, first expected contest and first actual contest separate. Align a smaller locked tree to trailing matching slots | Parts 01, 03, 05 and technical handoff, plus calendar mathematics |
| R04 Required animation could be silently omitted | Required genuine frame sequence remains a production gate with static usability fallback. The licensed short cue is explicitly optional | Parts 05, 09 and asset prompt |
| R05 Research links pointed outside the delivered folder | Make Part 10 self-contained and use the included Part 13 backlog | Parts 10, 13 and package link validation |

The immutable improvement receipt also records a source-mode finding for ordinary fictionally named contestants from grounded countries and says the earlier parent accepted its correction.
Grounded contestants require defensible sourced identity or an unresolved source-mode gate.
Image generation remains limited to the current asset contract's truly fictional high-Chaos or impossible/supernatural subjects.
Parts 05, 10, 13 and the asset prompt carry this boundary.

## Historical review dispositions

The following statements reproduce the disposition recorded by the prior planning-session author. They are preserved as history; the current import instruction does not renew blanket acceptance of every detail added beyond the immutable brief and the explicitly preserved design list in Part 00. See the current import handoff for the active acceptance basis and unresolved expansion claims.

The imported Part 11 stated that the prior parent accepted planning closure after the independent completion, improvement and technical reviews, and that the completion auditor had reported zero unresolved critical, high or medium planning findings. This is an archived planning disposition, not implementation acceptance or current user authorization.

| Review | Prior-session disposition as recorded in the immutable receipt | Current import treatment |
| --- | --- | --- |
| Completion auditor | All numbered parts and five prompts were reported reviewed, with 97 brief-coverage rows and R01 through R05 marked closed | Receipt preserved unchanged. Coverage is not current acceptance of every imported expansion or implementation evidence |
| Improvement planner | The prior author reports five findings accepted and promoted, with broad expansion stopped | Receipt preserved unchanged. The current parent-preserved list controls this cleanup; other author additions remain subject to disposition |
| Technical architect | The prior author reports the final technical and implementation contracts reviewed without a documentation contradiction | Receipt preserved unchanged. Proposed contracts do not prove current source behavior or present implementation feasibility |

The imported Part 11 says that the earlier parent standardized `first_actual_contest_date`, separated per-call outputs from durable receipts, tied frame animation to the committed winner/route and protected grounded portrait archives.
It also reports that its shortened recovery action kept the Part 02 disruption gate.
That receipt says the then-current AGENTS general-system CXT rule was added to Parts 08 and 09 and the coding prompt, with registration-only daily repair and player-triggered later debug content, and that the earlier specialists checked it. The current implementation contract is linked to the current owner under Part 08 and Part 09.

The immutable improvement receipt names five findings: I01 grounded source-mode clarity, I02 portable research references, I03 canonical first-contest field, I04 correct animation consumer and I05 durable portrait archive protection. It reports that the earlier parent accepted and promoted them. This import retains those edits but does not make that historical acceptance a new user decision. The separate partial-recovery correction is recorded there as the completion auditor's finding.

The imported review records report the package naming, prompt lengths and prose-style checks shown in their original files. They remain unchanged at [imported_review](../../plans/108_wrestling_tournament_plans/imported_review/), and their workspace paths are historical provenance rather than runtime dependencies.

No gameplay implementation or asset production is claimed by this matrix. Current source and workbook state remain with the parent. Relevant native tools should be used only when currently exposed and useful; otherwise use direct source review and meaningful local checks, and report material limits. No optional MCP route or live-game test is a general completion gate. Agents must not launch HOI4 or request or await user runtime evidence.
