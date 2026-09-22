# Achievement implementation and art prompt: Event 074

Implement all five achievements from `docs/specs/074_japan_lands_in_usa_specs/`.
Read design Parts 1, 3, 5 and 8, the capability and acceptance files, current `AGENTS.md`, the events skill, asset skill, subagents skill and existing achievement patterns.
Working audit output belongs under `docs/plans/074_japan_lands_in_usa_plans/`.
The following contract is repeated here so the coding and asset specialists can receive a context-complete task.
Part 8 remains the design authority if an accepted later revision changes this copy.

Inspect `common/achievements/chaos_redux_achievements.txt` and its current framework before adding any IDs.
Check the five proposed IDs for collisions.
Implement the actual tracking, final names and descriptions, normal eligibility and all disqualifiers below.
Do not replace compound requirements with a check for the event flag, tier selection or initial free territory.
Keep later achievement tracking distinct from exceptional supply and campaign-operation cleanup.

## Shared and individual contracts


The labels below describe the intended accomplishment and are not final achievement titles.
The technical IDs are proposed and require a repository collision check before registration.
Final names and descriptions must accurately reflect the implemented predicates.

An achievement requires a genuinely committed, nondebug Event 074 episode and the normal Chaos Redux achievement eligibility rules.
A debug grant, preview event, failed placement, fabricated history entry, or a canceled root cannot establish eligibility.
Use only disqualifiers the shared achievement framework can actually enforce.
Do not promise perfect detection of all console manipulation, save editing, or external mods.

Track only the relevant participating country and the small episode registry.
Record the opening footprint and initial conditions once, before the landing changes them.
Continuous-hold counters reset when their stated conditions break.
A later evolution does not reset the original landing date.
No achievement grants extra divisions, resources, territory, Chaos, or a second special landing.

### A01: Connect the Pacific coast

Proposed ID: `chaosx_074_connect_pacific_coast`.
Eligible country: Japan.
Visibility: visible.
Difficulty: very hard.

During the same Japanese-American war, control the relevant coastal territory of California, Oregon, and Washington, retain at least one working port in each, and maintain a continuous Japanese-controlled land connection between the three operating regions for 60 days.
At least two of the qualifying ports must lie outside the frozen initial footprint and must have been taken through subsequent normal combat.
The United States must not already have capitulated before the event's opening.

A large tier III opening therefore does not unlock the achievement by itself.
Its player still has to gain additional territory, connect the coast, and hold that result.
If the active map lacks one of the required named mainland regions, disable this achievement with a clear compatibility reason instead of substituting unrelated states.

Tracking needs the original footprint, three resolved region profiles, qualifying external port captures, connection state, and a 60-day continuous hold.
Icon direction is a simple three-point coastal chain with one strong connecting motif, readable at 64 × 64.
The final description should emphasize the connected and sustained campaign, not merely control of three names.

### A02: Turn a losing war into an American defeat

Proposed ID: `chaosx_074_reverse_the_war`.
Eligible country: Japan.
Visibility: hidden until the opening condition is known.
Difficulty: exceptional.

At the instant before the landing, Japan must have at least 50 percent surrender progress or enemy control over at least 25 percent of its validated original home-core territory by the chosen consistent measure.
The implementation must select and document the measure before release.
Use surrender progress as the baseline supported route and enable the territory route only after its home-core snapshot and denominator are verified.
The United States must be uncapitulated at that instant.

After the event, the United States must capitulate in the continuing war while Japan directly controls the original American capital location and a connected operating area on the Pacific mainland.
Japan must still exist and must have fielded the opening grant.
A different country taking the American capital does not satisfy the direct-control condition.

This does not claim that the event alone caused the capitulation.
It recognizes Japan converting an objectively poor opening position into a material continental result.
Tracking requires the prelanding condition snapshot, the original American capital, actual opening issue, continuing war identity or validated bilateral continuity, capitulation transition, and Japanese control predicates.
Icon direction is a damaged military dispatch beneath a clearly advancing campaign marker.

### A03: Defeat the large landing promptly

Proposed ID: `chaosx_074_recover_western_coast`.
Eligible country: United States.
Visibility: visible.
Difficulty: very hard.

Face a realized tier II or III opening, recover every initially occupied port, remove all Japanese control from the frozen initial footprint, and deny all Japanese Pacific mainland access for 30 continuous days.
Complete the entire condition within 240 days of the original landing.
The United States must never capitulate during the episode.
At least 90 percent of the authorized opening army must have been materially issued before this achievement can become eligible.

Legitimate allied liberation can help recover the footprint, but the United States must still exist on its original side of the war and the recovered area must not be controlled by a neutral third party.
A port disappearing from the event registry through a bug does not count as recovery.
Expiring Japanese support while leaving its army and occupation intact does not qualify.

Tracking needs realized tier, actual issued force, the original footprint and ports, current legal recovery, the absence-of-access hold, and an absolute 240-day deadline.
Icon direction is a reclaimed port entrance with a clear defensive barrier removed from the channel.

### A04: Defend the mainland, then reach Japan

Proposed ID: `chaosx_074_from_defense_to_tokyo`.
Eligible country: United States.
Visibility: visible.
Difficulty: exceptional.

Survive a realized tier III invasion with at least three working opening ports across at least two Pacific mainland states.
Achieve the full recovery condition used by A03 without its 240-day limit, then directly control Japan's original capital location within 730 days of the original landing while the original bilateral war is still continuing.
The United States must not capitulate at any point in the episode.
The Japanese capital cannot already be under American control when the event begins.

The name of the proposed technical ID does not force the final text to say Tokyo if a supported alternate setup starts with a different capital.
Resolve and snapshot the actual capital location.
The final achievement description must use the implemented original-capital condition.

Tracking needs the realized geographic gate, original Japanese capital, prior recovery receipt, continuing war, American noncapitulation, direct control, and the absolute deadline.
Icon direction is a restrained outbound campaign arrow connecting two distinct coast symbols.
It must remain visually different from the coastal-connection icon.

### A05: Save an isolated inland expedition

Proposed ID: `chaosx_074_restore_isolated_expedition`.
Eligible country: Japan.
Visibility: hidden until the isolated state begins.
Difficulty: exceptional.

First capture and hold a qualifying inland operating objective outside the original landing footprint through normal combat.
Then lose every working Pacific mainland access point while retaining that inland objective and an actual Japanese land force in its connected operating area for 30 continuous days.
Special support ends under the ordinary 30-day access-loss rule.
Within 60 days of the first loss of all access, retake a valid Pacific port through normal combat and reconnect it to the inland position.
Maintain the restored land connection for a further 30 continuous days.

No new scripted entry point, replayed landing grant, or debug-created force may provide the recovery.
The original bilateral war must remain active.
A retained empty inland province without a field army does not qualify.
The capability review must establish an observable force-presence predicate without inventing persistent division identity.

The player is rewarded for saving a real isolated expedition after exceptional support has ended.
This is deliberately difficult and must not be made easy by permanent local-supply immunity or a free second landing.
Tracking needs the qualifying inland objective, connected force presence, first all-access-loss date, the 30-day isolation hold, normal port recovery, restored connection, and the second hold.
Icon direction is an inland formation marker reconnecting to a small port after a broken line.

## Achievement image package

Each achievement needs one original transparent color subject and the prescribed final color, gray, and not-eligible tiles.
Reuse the unchanged project templates `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png`.
Use `process_achievement_icons.py` for the complete three-state production path.
Do not generate three unrelated drawings or send the finished tiles through a generic icon conversion that discards the template treatment.

Final files belong directly under `gfx/achievements/` and use the exact validated achievement ID:
`<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds`.
There are five subjects and fifteen runtime achievement tiles.
Source subjects, processing records, and native-size contact sheets remain in the asset evidence workspace until promotion is complete.



## Completion handoff

The implementation specialist owns exact predicates, hooks, hold counters, absolute clocks, once-only unlocks, missing-map compatibility behavior and final localisation.
The icon specialist owns accepted original subjects, unchanged templates, all three final states, valid DDS bytes and consumer filenames.
Coordinate the final ID before exporting art.
Do not write a final achievement title from a technical ID without the writing review.

Deliver one coverage row per achievement with eligible actors, opening snapshot, progress conditions, disqualifiers, terminal behavior, hidden/visible state, final localisation keys, final three icon files and actual test evidence.
Exercise each positive and negative route, including the prior free-territory case, expired deadlines, another country's control and support closure.
Where the chosen predicate is not supported, mark that exact capability blocked and resolve it without reducing the achievement to a trivial unlock.
