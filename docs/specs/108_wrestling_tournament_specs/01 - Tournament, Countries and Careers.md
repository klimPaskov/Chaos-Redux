# A champion chosen before the competition

Each edition begins with an international invitation and ends with a championship record that can be opened during later editions.
A country backs one identifiable wrestler through a common preparation period and a published knockout competition.
The tournament belongs to the shared campaign, so an eliminated player, a spectator country and every AI participant see the same entrants, pairings and results.
This implements the brief's core idea, six phases, selection and continuing careers.

## The competition's identity

Use an alternate-history international invitational with a published common grappling rulebook.
The draw is a single championship with one representative per country.
It permits a pin, submission or refereed decision and has its own entry, medical and conduct rules.
It is not presented as a reconstruction of a particular Olympic competition.
Historical entrants retain their documented background, but their participation and campaign results belong to the game's alternate history.
The research register separates facts about a person from invented tournament incidents.

The ordinary division accepts human contestants who can understand and obey the competition's rules.
A known weight or physique informs Strength, Speed, Endurance and matchup descriptions without creating an automatic weight-based victory.
Weigh-in disputes concern declared identity, fitness, concealed equipment or an announced safety restriction.
They must not invent a new weight class after the entrant has paid and prepared.
Open Division changes admission only through its evolution and a rulebook published before roster lock.

The tournament's international office is an event-owned administrative record.
It is not a newly created country, faction or political authority.
The venue is an existing suitable state and host country selected from the campaign.
The host provides setting, travel context and a place for public reporting.
It does not own the authoritative arrays or decide opponents to favor its wrestler.

## One edition at a time

An edition receives a monotonic ID before any country can register.
Its invitation, accepted countries, contestant identities, schedule, rules, seed line, match records, incidents and awards all carry that ID.
An active-edition guard is acquired before the shared event-fired handler records the opening.
The same opening cannot therefore count twice when two countries' event timers select it together.

Ordinary selection makes Event 108 unavailable while an edition is active or in its recovery interval.
A forced request encountering that guard opens the existing tournament and reports why a new one cannot start.
It creates no second edition, fee, reward, weight reduction or history entry.
If the implementation retains one explicit pending manual request, it must be a single coalesced request checked after the recovery date, with no firing or payment before a new opening actually commits.
Automatic selections are never accumulated into a backlog.

The existing repeatable-event weight, cap reduction and recovery system continues to own selection frequency.
The tournament additionally requires 180 days after the previous edition's archival settlement before the next announcement.
This interval is a recovery anchor for careers and national investment, not a new countdown attached to every country.
Prior brackets stay available throughout it and throughout the next preparation period.

## The ordinary six-phase rhythm

| Phase | Default dates from announcement | What the country does | What becomes fixed |
| --- | --- | --- | --- |
| Announcement and entry | Day 0 to day 20 | Reads the rulebook, chooses participation, reviews candidates and nominates a provisional wrestler | Edition ID, entry deadline, official preparation start and earliest competition date |
| Preparation | Day 20 to day 110 | Completes several camps, changes funding, rests, studies and responds to incidents | Each accepted action's paid quote, opportunity cost and completion date |
| Roster lock and seeding | Day 110 | Confirms the already selected eligible wrestler and receives the draw | Entrants, opening seeds, tree positions, advancement paths and division rules |
| Knockout rounds | Earliest competition slot day 120, then five-day round intervals. The first actual contest depends on the locked field | Chooses tactics and limited recovery, follows qualifiers and the main draw | Each committed result and its advancement receipt |
| Final and award | Last scheduled round, followed by a ten-day settlement window | Sees the result, resolves any pending timely inquiry and receives recognition | Original final result, award settlement and championship standing |
| History and return | After settlement | Reviews the full edition, careers, sanctions and rivalries | Archived presentation identities and completed edition records |

The official preparation period begins together for all entrants after registration closes.
The invitation window therefore does not give the first AI respondent an extra camp cycle.
Selection before day 20 reserves a candidate but does not grant training gains.
Late registration is not allowed after the announced deadline.
An interested country can still observe the competition.

The 90-day preparation anchor is calculated at announcement from transport disruption, expected international breadth, available institutions and returning-edition experience.
Use a normal range of 70 to 110 days in five-day steps.
Long-distance or disrupted travel can add ten days, while a mature host organization can remove ten.
A major war affecting several travel routes can add five to ten without banning every belligerent.
The published deadline then stays fixed when those factors change.

At registration close, the accepted-country count determines a full next-power-of-two tree and its reserved round slots, including any preliminary depth above a 32-place main draw.
The earliest competition slot is ten days after roster lock, then every later round slot is five days apart.
Publish each named round and final date then.
At lock, a smaller actual tree uses the trailing slots for its matching round sizes, leaving unneeded leading slots as rest.
This preserves every previously announced main-round and final date.
For example, 65 registered entrants reserve qualifier slots on default days 120 and 125, the round of 32 on day 130 and the final on day 150.
If only 32 remain at lock, their first expected contest is day 130.
If only two remain, they contest the already announced final on day 150.
The interface distinguishes the earliest competition slot, the first expected contest derived from the locked field and the first contest actually played.
No unused slot reopens training or shortens promised recovery.

One combined exceptional-delay allowance of up to ten days covers real common disruptions, inquiries and the permitted no-contest retry.
The reason, affected rounds, old date and new date are recorded.
An individual accusation can hold its own match within the available schedule tolerance but cannot repeatedly extend the whole tournament.
Time bought by investigation does not reopen training or seeding.

## Countries that can send a representative

Eligibility is evaluated at invitation, registration, nomination and lock.
The player sees the current failed requirement rather than an unexplained disabled button.

| Requirement | Admission rule | Relevant exception or consequence |
| --- | --- | --- |
| A living political representative | The country exists and has a functioning authority able to make the entry commitment | An existing recognized government in exile can use a consenting existing host route if its owner system supports that state |
| Sufficient representation | Independent countries qualify normally, while subjects require their existing autonomy and representation rules to permit a national delegation | Do not count an overlord's support as permission to reuse the same wrestler for two countries |
| A viable journey and venue | There is a plausible current route from the delegation to the host, or an approved already available host arrangement | A specific blockade, quarantine or closed route may prevent travel, with a recorded reason |
| An eligible candidate | At least two usable candidate identities are available for a meaningful selection, with a distinct portrait for each | A production defect is a content blocker to repair, not a balancing reason to exclude a country |
| Medical and conduct admission | The candidate can participate under the announced rules and is not serving a relevant suspension | Manageable injuries can be accepted with disclosed penalties, while severe injuries require recovery or substitution before lock |
| Compatible actor classification | Human delegations are eligible in the ordinary division, including unusual but genuinely human actors | Actual nonhuman candidates require Open Division and a valid existing owner record |

War status is a cost and journey consideration rather than a blanket exclusion.
Low industry, minor-power status, unfamiliar ideology and a poor prior record are not exclusion criteria.
Country AI may decline because its resources or war needs make participation unattractive.
That is a visible choice with a recorded reason, not a hidden omission from the eligible pool.

An existing special country is not automatically a nonhuman country.
Use the shared classifiers and then an entrant-specific owner adapter.
The inspected shared trigger distinguishes these two concepts, as documented in `12 - Source and Repository Evidence.md`, R02.
Do not infer an individual wrestler's species or eligibility solely from the country's flag or tag.

## Host and route handling

Choose the venue from a bounded set of existing eligible host states with safe public access and sufficient ordinary facilities.
Prefer a neutral or broadly accessible host, then compare current disruption, regional rotation and prior hosting.
A major is not automatically preferred over a minor.
The venue selector must retain its candidate set, selected state, country, reason and revision.
It grants no state, building or institution.

If the venue is lost before lock, move to the next valid existing host and apply the one common delay if needed.
After lock, first attempt the same bounded relocation with all entrants and paths preserved.
If the campaign offers no valid venue or surviving field, close the edition as interrupted or void with no fabricated champion.
The archive explains where it stopped.
Ordinary spending already consumed by camps remains spent, while unused reserved capacity and refundable travel commitments settle once.

## The small candidate pool

A participating country normally sees three candidates and always needs at least two before it can make its first nomination.
The candidates must differ in a useful combination of profile, health, age band, record, preparation needs and risk.
A default pool should make at least two choices credible for that country's current budget and campaign situation.
Three differently named versions of the same stat profile fail this requirement.

Typical pool roles are a returning veteran, a technical specialist and an emerging local contender.
These are selection patterns, not mandatory personality classes.
A country with a hurt returning champion might instead receive two established alternatives and the recovering champion.
A small country can have an outstanding technician even when it cannot afford the most elaborate support team.

Generate the edition's candidate offers once from the eligible identity registry and retain their reservation records.
Opening the window, changing tabs, reloading or cancelling a selection does not refresh the pool.
Each identity can be offered to only one country at a time within an edition.
Country changes between campaigns follow the person's documented representation or a clearly fictional identity's authored origin and allegiance rules.
A historical person's nationality is not reassigned for regional coverage.

Before lock, a country can replace a nominee with another reserved eligible candidate.
Existing identity-specific gains stay with the wrestler who earned them.
Travel reservations can transfer only where the existing paid contract permits it.
Medical treatments, training gains, concealed violations and personal injuries do not move to the replacement.
The replacement receives only the remaining common preparation time.
After lock there are no replacement entrants.

## Six distinct attributes with two management meters

Store Strength, Technique, Endurance, Speed, Toughness and Adaptability independently on a 0 to 100 internal scale.
They influence different match situations and preparation choices.
Never collapse them into one hidden strength rating and describe the unused fields as flavor.

| Attribute | Information in a profile | Principal mechanical use |
| --- | --- | --- |
| Strength | Relative control and explosive power | Early pressure and physical control against the opponent's defenses |
| Technique | Holds, escapes and counters | Scoring efficiency, counterplay, submissions and resistance to crude pressure |
| Endurance | Sustained work over a long bout | Long-match performance and recovery between rounds |
| Speed | Reactions, entries and evasions | Sudden attacks and avoiding slow powerful opponents |
| Toughness | Ability to absorb strain and recover from minor knocks | Injury susceptibility and the effect of accumulated wear |
| Adaptability | Ability to recognize and answer unfamiliar approaches | Scouting benefit, tactical flexibility and unusual opponents |

The profile shows the same six traits through compact qualitative comparisons such as a clear strength, a relative weakness or an even matchup.
These phrases are writing directions rather than final strings.
Tooltips explain the consequence and relevant uncertainty without exposing the next result roll.
There is no six-bar numerical dashboard on another tab.

Readiness is the current ability to deliver prepared performance, from 0 to 100.
Strain is accumulated fatigue and overwork, from 0 to 100.
These are the two visible custom management meters for the entire mechanic.
Readiness can be high while Strain is also high, which describes a well-prepared athlete close to exhaustion.
Injury is a named condition with severity and an expected recovery date, not a third meter.
Reputation and recent form are qualitative career assessments backed by hidden records.
Seeds, wins, losses, dates, costs and days remaining are factual information rather than additional spendable or managed currencies.

## Careers across editions

The identity registry stores immutable identity ID, source mode, name key, portrait ID, origin, historical evidence where applicable and an authored availability interval.
Mutable career records hold appearances, actual bouts, official wins and losses, titles, title defenses, major upsets, reputation, recurring rivals, injuries, suspensions and last active date.
The edition record snapshots the representation and portrait used at that time.

Historical entrants need a researched age and activity check before ordinary admission.
A photograph existing before 1936 does not establish that its subject is alive, active or suitably fit in the campaign year.
Retired or older figures may become coaches or reference material if the accepted asset brief calls for them, but do not place them in the ordinary field merely to reach a portrait count.
Campaign divergence may change a living wrestler's later career, while their factual starting identity and source remain explicit.

At each new nomination window, apply a bounded age and inactivity adjustment to the career profile, then assess injuries and suspension dates.
Young emerging contestants gain consistency gradually, peak competitors retain their authored strengths, and older veterans increasingly trade recovery and speed for technique and adaptability.
No every-country daily aging scan is required.
Career adjustment uses the elapsed date once per identity and preserves the adjustment receipt across reload.

Permanent training improvement is deliberately small.
Most improvement in one edition is preparation and condition that decays between competitions.
The largest repeat advantage comes from experience, known style and reputation, all of which remain limited in seeding and match probability.
An old champion never becomes unbeatable through title accumulation.

Rivalries develop from actual close bouts, an upset, a repeat final or a substantiated personal controversy.
They modify reporting, public stakes and preparation choices.
They do not rewrite a published draw.
When rivals do not meet, the archive can still show their shared history without manufacturing a match.

## Returning and observing

All player countries can open the active edition and the archive once the competition has been announced.
Participant-specific controls require current ownership of that entry.
A spectator sees public profiles, the draw, dates, published allegations and official findings.
It cannot see another team's concealed treatment or unannounced tactic.

An eliminated participant loses training and match authority but keeps observation, history and any legitimate open inquiry response.
Notifications default to the country's own matches, important rivals, major adjudications and the final.
A follow mode can add the remaining rounds or a selected underdog's run without requiring every country to receive every bout popup.

At completion, restore ordinary country UI state, release event-owned reservations, close obsolete missions and remove temporary preparation modifiers.
Keep career records, title and sanction history, award receipts, the immutable draw and all published match records.
Cleanup of a current selection must never erase the wrestler or match currently being inspected in an older edition.
