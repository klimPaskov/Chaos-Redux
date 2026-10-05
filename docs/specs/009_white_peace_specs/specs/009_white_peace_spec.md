# Event 009 — White Peace

## Core identity

**White Peace** is a repeatable de-escalation event for wars that have become noise rather than story. It does not erase the war system, reward a winner, or impose a new order. It finds wars that are safe to soften and forces a status-quo settlement between the selected participants.

The event belongs to the **Peace** cluster, cluster ID `4`. It is intentionally low-impact at the base level. Its job is to remove small, stale, or low-stakes wars that clutter the campaign without rewriting the main balance of power.

The event is not a negotiation the player can refuse. It is a settlement note, a neutral exchange, a line going quiet, or a set of diplomats arriving after both staffs have already run out of useful demands. The popup uses one acknowledgement option only.

## Playable promise

The player should feel that the world occasionally exhales. The event is still part of Chaos Redux, so it must not become a reliable peace button or a way to protect the player from consequences. It should feel like a rare diplomatic interruption produced by the exhaustion of too many wars.

The promise is:

- If there are no active wars, the event is unavailable.
- If there are active wars but none are safe, the event is unavailable.
- If there are a few small wars, it can occasionally end one minor-versus-minor pair.
- If wars multiply across the world, its dynamic weight rises, but it stays below ordinary event prominence in most campaigns.
- If the event evolves, each firing can settle more or touch larger actors, but the event itself becomes less likely to be selected.
- The event should never become a general-purpose world pacifier.

## Normal firing shape

The base event selects one valid minor country at war, then selects one valid enemy minor country from one of its active wars. The effect applies a no-gain, no-loss white peace between those two countries only.

The selected countries receive short-term diplomatic memory so the same pair is not immediately selected again, and nearby war-cleanup systems can avoid pushing them back into a random war loop. The event should not remove ordinary focus claims, scripted war goals, or scripted story state unless another system explicitly marks those goals as safe to clear.

The baseline event should not settle whole factions, whole alliances, or whole theaters. It is a pair-level cleanup tool.

### Player-facing framing

Use restrained, bureaucratic, slightly eerie writing. The silence should feel almost unnatural in a mod built around escalation.

Good tone:

- terse diplomatic cables;
- neutral consulates forwarding identical notes;
- exhausted generals accepting a line drawn before anyone claims victory;
- quiet border posts receiving orders to stop firing;
- newspapers struggling to report an event with no triumph and no defeat.

Avoid:

- heroic peace rhetoric;
- utopian diplomacy;
- comedic surrender jokes;
- “the map changed” framing;
- implying the player chose peace when the event is forced.

## Event stages and evolutions

White Peace has baseline behavior and three global evolution stages. These stages are not ordinary follow-up steps. They are escalation rules that alter what a future firing can do.

| Stage | Working evolution name | Public idea | Main gameplay change | Selection-pressure effect |
| --- | --- | --- | --- | --- |
| Base | Minor White Peace | One minor pair signs a no-gain settlement. | Settles one safe minor-versus-minor pair. | Uses the full dynamic cap for the current environment. |
| I | Repeated Minor Settlements | The machinery of quiet settlements begins repeating. | One firing can settle several minor pairs when safe. | Dynamic cap is multiplied down so stronger effects do not become common. |
| II | Major-Country Settlement | A major power can be pulled into a no-gain exit. | A rare branch can settle a major country with one enemy participant or narrow enemy side. | Stronger multiplier penalty; major branch remains uncommon even when eligible. |
| III | Broad Diplomatic Settlement | Separate minor-country frontiers fall quiet under the same terms. | Can settle up to five separate isolated minor wars. | Strongest multiplier penalty; this stage is impactful but rare. |

The event can reach a higher stage before White Peace has settled a war if existing war-pressure thresholds are already met. The matching Event Settings evolution and Chaos tier gate must also be enabled. A disabled stage does not regain gameplay access through an older global unlock flag.

### Evolution stage I — Repeated Minor Settlements

Stage I represents separate minor-country wars falling quiet under the same terms. It does not mean that every belligerent wants peace; it means several isolated wars can end during one event chain.

Unlock pressure should look at:

- several active wars at once;
- several valid minor pairs;
- at least one prior White Peace firing, or severe war clutter before the first firing;
- recent failure to find a safe settlement despite high active-war count;
- Peace cluster availability over repeated checks.

When Stage I selects the multi-settlement branch, it settles several separate safe one-on-one minor wars and applies the same terms to each pair. It never settles several pairs from one multi-country war.

The branch must cap its reach. Suggested cap: two pairs at early stage I, three pairs when war pressure is high. It should never perform an unbounded loop through every possible pair.

### Evolution stage II — Major-Country Settlement

Stage II does not convert White Peace into a major-event spectacle. It only adds the possibility that a major country can be part of a status-quo exit when the world has too many wars or a particular large war has become stagnant.

This branch should remain rarer than minor settlement even after the stage unlocks. It must not fire on wars that carry obvious scripted significance, major crisis flags, nonhuman threat participation, civil conflict state, or near-capitulation conditions.

Safe major-country settlements are limited to an isolated two-country war:

- at least one selected country is major;
- neither selected country has another active enemy;
- both selected countries pass every country and pair safety gate.

It should not automatically dissolve a global alliance war just because one major is tired.

### Evolution stage III — Broad Diplomatic Settlement

Stage III exists for the late campaign state where the world has too many active conflicts and the war list itself becomes a chaos source. It is not meant to restore normality. It removes clutter in a way that still leaves important wars alive.

The valid Stage III branch shape is:

- settle up to five separate safe one-on-one minor wars.

Stage III is not a total peace conference substitute. A candidate that is too scripted, too close to capitulation, or tied to other Chaos Redux mechanics is rejected before selection. A branch that settles fewer wars than planned reports only the number of completed settlements.

## Forced settlement behavior

The hidden entry applies each valid settlement immediately. Every human-controlled participant in the affected wars receives one acknowledgement report after the peace has taken effect. Participants in a multi-war chain see the same aggregate result, once per country. No actor receives a “continue the war” option, and the report does not present the completed settlement as a choice.

When every settled participant is AI, one global news report informs observers after the settlement. If at least one affected participant is human-controlled, each affected human receives the aggregate report and no observer-news copy is sent. The event-history record must reflect a successful peace, not an open report option.

Recommended option tone:

- “Let the guns fall silent.”
- “No one claims victory.”
- “The line goes quiet.”
- “The note is already signed.”

Use one option per displayed event, not parallel accept/decline options.

## Settlement effects

Base settlement effects:

- apply white peace between the selected countries in an isolated one-on-one war;
- mark both countries with a short recent-settlement flag;
- mark the pair with a short pair-cooldown if pair tracking is available;
- add a modest temporary opinion modifier between the two countries;
- reduce Chaos by a small amount, normally `-1` for a single minor pair;
- write one event-history entry;
- count the firing as one repeatable event and one Peace cluster incident when the cluster path fired.

Multi-settlement effects:

- apply the same effects to each selected pair from a separate isolated war;
- cap Chaos reduction so the event cannot erase the consequences of a war-heavy world;
- write one history entry summarizing the primary settlement and count of additional settlements;
- optionally write compact internal debug metadata for validation, not player-facing spam.

Major-country settlement effects:

- use a stronger but still restrained Chaos reduction, normally `-2` or `-3` depending on war importance;
- set longer recent-settlement memory on the major actor;
- avoid clearing scripted wargoals unless a specific helper marks them safe;
- add relation memory but not enough to create artificial alliances.

Broad-settlement effects:

- scale by settled pair count but cap the final Chaos reduction;
- suggested cap: `-3` at stage III, with an optional `-4` only if many wars were active and several separate wars ended;
- add a world-news style notification only if the implementation already has a normal-news pattern for repeatable events; otherwise use the ordinary report/event popup and history entry.

## Dynamic weight design intent

White Peace must usually be less likely than ordinary events. It should sit below the default `1000` weight in most campaigns, even when a valid minor war exists. Its weight should rise when the world has many wars, especially many safe minor war pairs, but the environmental cap must never exceed `1500` before repeatable decay is applied.

The normal repeatable recovery system still applies. White Peace should recover like other repeatable events, and its repeated firings should reduce the recoverable cap through the normal repeatable decay model. The dynamic cap only controls the maximum value the event can recover toward under the current war environment.

The implementation should treat selection weight as:

```text
live_weight = min(recovered_repeatable_weight, effective_dynamic_cap)

effective_dynamic_cap = floor(environment_cap * repeatable_decay_multiplier)

environment_cap <= 1500
```

This preserves repeatable-event recovery while allowing the event to become more or less likely as war clutter changes.

## What should make the event more likely

The event should become more likely when:

- there are many active wars;
- there are many safe minor-versus-minor candidate pairs;
- several wars involve minor countries without major allies;
- the Peace cluster has had valid candidates for repeated checks without firing;
- the event has not fired for a long time and the normal repeatable recovery has had time to rebuild;
- a war has dragged on long enough to feel stale, if war age can be tracked safely.

## What should make the event less likely

The event should become less likely when:

- there are only one or two small wars;
- safe candidate count is low;
- most wars involve majors, scripted crises, civil conflict, nonhuman countries, or protected event chains;
- the event is already at a higher evolution stage;
- White Peace fired recently and the repeatable decay/recovery system has not rebuilt its weight;
- the same countries have already been affected recently.

High Chaos should not by itself make White Peace common. Chaos can unlock stronger stages and is often correlated with war pressure, but war count and valid candidate pressure should be the main drivers.

## Targeting philosophy

Candidate selection should prefer settlements that remove noise and avoid settlements that rewrite intended content.

Preferred candidates:

- two minor countries;
- both still exist and are active war participants;
- neither is close to capitulation;
- neither has enemy control of its capital;
- neither is an event-protected special actor;
- neither is in a civil conflict with the other;
- no obvious story, focus, or scripted-war protection is present;
- the war has not just started;
- both countries can plausibly stop fighting without changing ownership.
- each selected country has no active enemy country other than its proposed partner.

Cautious candidates:

- a minor that has a major ally but is fighting another minor directly;
- a subject country whose overlord is not the intended settled actor;
- a war where one side has occupied a few noncapital states;
- a major-country pair at stage II or III only, with no third-country war participants.

Forbidden candidates:

- civil conflict pairs;
- countries marked by event-specific or scripted-war protection flags;
- countries in active existential-threat mechanics or nonhuman-country roles;
- wars in which either selected country has capitulated;
- pairs where the effect would obviously strand subjects, overlords, or faction leaders in invalid war state;
- pairs whose capitals are occupied by the intended enemy;
- wars where a focus, decision, or event chain has marked the war as protected until its resolution;
- countries that recently received a White Peace settlement with each other.
- any war where either selected country has another active enemy country.

## Accepted whole-war safety boundary

On 2026-10-05, the parent accepted an isolated one-on-one war boundary under the user's G6 design-authority instruction. The parent directed this restriction because Event 009 cannot prove that a nominal country pair is isolated from other participants in the engine's war state. The 1v1 gate requires each selected country to have no active enemy country besides its proposed partner.

Stage I and Stage III continue to settle multiple separate safe wars, with each settlement limited to one isolated country pair. The prior proposal to settle several pairs within one overcrowded, multi-country war is rejected because the affected third-country participants cannot be proven safe through this target model. This is a documented design change and does not claim that the one-war route remains supported.

On 2026-10-05, the parent also accepted the shared Event Settings evolution contract for White Peace. A stage's existing war-pressure threshold remains required, and the matching `is_current_evolution_enabled` event/tier gate must also pass before its behavior or weight is available. A disabled Stage I, Stage II, or Stage III branch stays disabled even if a global unlock flag was set earlier. The base isolated minor settlement remains available when every evolution is disabled.

The parent also accepted a 181-day country cooldown around the 180-day No Winner check. This one-day margin prevents a different settlement from restoring a cleared survival watch at the delayed event's day-180 boundary.

## Safe-war protection standard

Add a reusable opt-out pattern for other events and scripted content:

- country flag: `white_peace_protected_country`;
- pair flag or country memory: `recent_white_peace_with_<target>` if the implementation can safely encode the target;
- war-context flag when an event chain owns the war;
- scripted trigger: `can_country_be_white_peace_target`;
- scripted trigger: `can_pair_receive_white_peace`;
- scripted effect: `mark_recent_white_peace_pair`;
- documentation entry explaining how future events can protect their wars.

If the repository already has a different naming convention for event-protection flags, follow that convention and map the spec names to the existing pattern.

## Cluster role

Cluster ID `4` is the Peace cluster. White Peace is its first low-impact member. The cluster should present this event as de-escalation, ceasefire, settlement, and cleanup logic rather than as a dramatic transformation.

Cluster behavior:

- White Peace remains a normal repeatable event that can be selected from the event pool.
- If cluster logic is invoked, the cluster firing still counts as one global pacing incident.
- Multi-settlement branches inside White Peace do not count as several event firings.
- Future Peace cluster events can use the same dynamic peace-pressure helpers.
- The cluster detail row should show whether safe settlement candidates exist and why the cluster is skipped when no safe candidate exists.

## Event log and detail window

The history entry should show the primary country as actor. If the event-log system supports a secondary actor, record the partner too. If it does not, keep the partner in the popup and use generic history detail text rather than a leaking event target.

Recommended event-detail text:

> Independent countries lay down their arms after a war yields no land worth holding and no payment worth demanding. Their former borders return, and soldiers withdraw from the front while other wars continue elsewhere.

Recommended evolution-summary text:

- **Repeated Minor Settlements**: separate minor wars fall quiet across more than one frontier.
- **Major-Country Settlement**: a rare settlement can involve a major country when the war is safe.
- **Broad Diplomatic Settlement**: a wider group of separate minor wars ends under the same no-gain terms.

## Localisation style guide

Key phrase set:

- “status-quo settlement”
- “no claims, no indemnities”
- “neutral note”
- “silent border”
- “the line goes quiet”
- “no one claims victory”
- “the same flags over the same towns”
- “the war has ended without a winner”

Avoid:

- “peace has triumphed”
- “the conflict is resolved forever”
- “both sides agree happily”
- “the player accepted”
- “newly reworked”
- “dynamic cap” in player-facing text.

Dynamic values such as pair count or primary actor names can appear in tooltips and event details if the existing localisation pipeline supports them cleanly. Do not expose raw trigger lists or candidate-scoring internals to the player.

## Normal event text directions

### Base popup

**Title direction:** No Gains from the War

**Description direction:** Name the two countries. Their armies return behind the lines they held before the war, and neither country gains land or demands payment.

**Option direction:** Acknowledge the armistice after the settlement has taken effect.

### Stage I popup variant

**Title direction:** Several Minor Wars End

**Description direction:** Describe soldiers leaving their posts across several separate frontiers. State that the old borders hold and no indemnity changes hands.

**Option direction:** Acknowledge the separate armistices after they have taken effect.

### Stage II popup variant

**Title direction:** A Major Front Falls Silent

**Description direction:** A major government ends one isolated war with a smaller neighbor. The old border holds, and neither country receives payment.

**Option direction:** Acknowledge the armistice after the settlement has taken effect.

### Stage III popup variant

**Title direction:** Armistices Across Several Fronts

**Description direction:** Describe several separate minor wars ending at once. Armies return behind their former lines, and no country gains territory or an indemnity.

**Option direction:** Acknowledge the separate armistices after they have taken effect.

## Report and news presentation

The player report uses one restrained period scene of border soldiers lowering their weapons. It should not show a grand treaty hall or a cheering crowd.

When every participant in a successful chain is AI-controlled, one global news event reports the outcome to observers. Use a separate black-and-white news image at `397x153` that shows a quiet border checkpoint rather than a triumphant peace conference.

## Animation pass

Static presentation is stronger for the base event. The event should feel like silence, not spectacle. No animated popup, animated leader portrait, or animated route emblem is needed for the source spec.

If the Peace cluster later receives a dedicated de-escalation interface, a subtle animated document seal or muted telegraph pulse could be planned then. That is outside the current event package.

## AI behavior

The event does not ask AI countries to accept or refuse. AI behavior lives in candidate selection, branch weighting, and safety vetoes.

AI-relevant goals:

- do not rescue a losing AI from a legitimate nearly-won war;
- do not trap subjects or faction members in broken war state;
- do not end scripted crisis wars;
- do not repeatedly select the same pair;
- do not prefer majors unless the correct stage is unlocked;
- do not allow stage III to erase the main war story of a campaign.

Selection should be weighted toward stale, small, low-threat conflicts where the settlement reduces clutter. If a human-controlled minor is selected, the same safety rules apply. The event is allowed to affect players, but not through unsafe or protected wars.

## Achievements

White Peace can support a small set of difficult achievements because its evolved behavior creates rare campaign states. These achievements should not unlock simply because the event fired once.

Planned achievements:

| Working id | Title | Core challenge | Visibility |
| --- | --- | --- | --- |
| `achievement_white_peace_status_quo_ante` | Status Quo Ante | As a minor, have a prolonged war ended by White Peace while remaining independent and outside a major faction. | Visible |
| `achievement_white_peace_no_winner` | No Winner, No Spoils | Have both countries remain alive, independent, and uncapitulated for 180 days after their White Peace settlement. | Visible |
| `achievement_white_peace_chain_of_tables` | A Chain of Tables | Settle six separate minor wars before any major-country war is settled. | Hidden |
| `achievement_white_peace_silence_of_giants` | Silence of Giants | Be part of a major-country settlement after a long war without receiving conquered territory from that war. | Hidden |
| `achievement_white_peace_the_circular` | The Circular Reaches Every Desk | Have one broad settlement end at least three separate isolated minor wars. | Hidden |

Achievement implementation must track that the settlement came from Event 009 and not from ordinary peace conferences or scripted peace events.

## Asset coverage

Required asset directions:

- one report event image, `210x176`, period-documentary style, likely generated unless a public-domain/source image clearly fits;
- one AI-only global news image, `397x153`, black-and-white;
- five achievement icons, `64x64`, each with completed, grey, and not-eligible variants if the achievement system requires variants;
- no focus icons, leader portraits, flags, or country assets;
- no animated assets for the base spec.

The asset prompt in this package gives source mode and reference-folder instructions.

## Documentation requirements

The event doc should explain:

- what White Peace does;
- why it is repeatable and low-impact;
- how dynamic weight works in player-facing terms;
- which wars can be selected;
- why protected wars are excluded;
- how evolutions alter future firings;
- how the Peace cluster presents it;
- which assets and achievements exist;
- how repeated firing remains limited by repeatable recovery and dynamic caps.

The event catalog should mirror the in-game event detail and evolution detail wording after implementation.

## Acceptance criteria

The event is complete only when:

1. Event ID `9` is registered as a repeatable event and belongs to Peace cluster ID `4`.
2. It is unavailable when no active war exists or when no safe candidate pair exists.
3. It uses dynamic weight and dynamic cap logic; the environment cap never exceeds `1500`.
4. It usually has a lower chance than a default `1000` event in ordinary campaigns.
5. Higher evolution stages reduce selection likelihood even though they increase possible effect strength.
6. Normal repeatable recovery and repeatable firing decay still apply.
7. The hidden entry applies one valid settlement immediately before it sends a result report.
8. Base behavior settles exactly one isolated safe minor-country war.
9. Stage I can settle several separate isolated minor-country wars within its cap.
10. Stage II can rarely settle one isolated major-country war after the major stage is open.
11. Stage III can settle several separate isolated minor-country wars within its cap.
12. Every stage rejects a candidate when either country has another active enemy.
13. A forced invalid entry gives the player a plain report that names the reason and confirms no peace was imposed.
14. A successful chain sends one aggregate country report to each human-controlled participant, or one global news event when every settled participant is AI. A player receives at most one result popup for the chain.
15. The popup has no continue-war option and its text describes the actual result.
16. Candidate selection excludes protected scripted content, civil conflict, nonhuman/special threat actors, near-capitulation cases, and recent pair repeats.
17. Event log, event detail, evolution detail, cluster detail, and localisation agree.
18. Report and AI-news images and achievement icon needs are wired and documented.
19. Implementation validation includes no-war, forced major-locked, one isolated minor war, multiple isolated wars, a third-country war participant, major-war, protected-war, repeated-firing, and high-evolution cases.
