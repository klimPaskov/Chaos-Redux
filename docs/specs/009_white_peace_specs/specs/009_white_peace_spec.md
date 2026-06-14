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
| III | Broad Diplomatic Settlement | A circular of armistice notes moves through too many wars at once. | Can settle several valid wars or a larger safe segment of one war. | Strongest multiplier penalty; this stage is impactful but rare. |

The event can unlock a higher stage even before White Peace has fired in the campaign if the world already has enough war pressure. In that case, the first firing uses the evolved opening rules. If White Peace has already fired, the stage immediately changes future runtime selection and branch weights; there is no persistent actor that needs a retroactive focus path or decision category.

### Evolution stage I — Repeated Minor Settlements

Stage I represents diplomats, neutral mail routes, staff officers, and exhausted border commands learning that the first settlement worked. It does not mean everyone wants peace; it means the event can now clean several small fires in one pacing incident.

Unlock pressure should look at:

- several active wars at once;
- several valid minor pairs;
- at least one prior White Peace firing, or severe war clutter before the first firing;
- recent failure to find a safe settlement despite high active-war count;
- Peace cluster availability over repeated checks.

When a stage I firing selects the multi-settlement branch, it should either:

1. pick one war with several safe minor participants and settle several pairings from that war, or
2. pick several separate safe minor wars and resolve one pair from each.

The branch must cap its reach. Suggested cap: two pairs at early stage I, three pairs when war pressure is high. It should never perform an unbounded loop through every possible pair.

### Evolution stage II — Major-Country Settlement

Stage II does not convert White Peace into a major-event spectacle. It only adds the possibility that a major country can be part of a status-quo exit when the world has too many wars or a particular large war has become stagnant.

This branch should remain rarer than minor settlement even after the stage unlocks. It must not fire on wars that carry obvious scripted significance, major crisis flags, nonhuman threat participation, civil conflict state, or near-capitulation conditions.

Safe major-country settlements should usually target a narrow relationship:

- one major and one enemy country;
- one major and a small enemy participant;
- one major and a narrow enemy side only when the implementation can prove that the side segment is safe.

It should not automatically dissolve a global alliance war just because one major is tired.

### Evolution stage III — Broad Diplomatic Settlement

Stage III exists for the late campaign state where the world has too many active conflicts and the war list itself becomes a chaos source. It is not meant to restore normality. It removes clutter in a way that still leaves important wars alive.

Valid branch shapes:

- settle up to three separate safe minor wars;
- settle up to five safe minor pairs from one overcrowded war;
- settle one narrow major-country relationship plus one or two minor pairs in the same war;
- settle several minor countries out of the same war while keeping major war leaders and protected scripted actors untouched.

Stage III should not perform a total peace conference substitute. If the selected war is too scripted, too close to capitulation, or too tied to other Chaos Redux mechanics, the broad branch should fall back to a smaller valid branch or skip the firing cleanly.

## Forced settlement behavior

The popup has a single acknowledgement option. No actor receives a “continue the war” option. The event should not present itself as a choice.

The effect should happen in the option block rather than only in the immediate block so the player can read what happened before accepting the popup. For AI-only settlements, the event may resolve through a hidden notification path or direct effect, but the history log must still record the settlement.

Recommended option tone:

- “Let the guns fall silent.”
- “No one claims victory.”
- “The line goes quiet.”
- “The note is already signed.”

Use one option per displayed event, not parallel accept/decline options.

## Settlement effects

Base settlement effects:

- apply white peace between the selected countries;
- mark both countries with a short recent-settlement flag;
- mark the pair with a short pair-cooldown if pair tracking is available;
- add a modest temporary opinion modifier between the two countries;
- reduce Chaos by a small amount, normally `-1` for a single minor pair;
- write one event-history entry;
- count the firing as one repeatable event and one Peace cluster incident when the cluster path fired.

Multi-settlement effects:

- apply the same pair-level effects to each safe pair;
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

Cautious candidates:

- a minor that has a major ally but is fighting another minor directly;
- a subject country whose overlord is not the intended settled actor;
- a war where one side has occupied a few noncapital states;
- a major-country pair at stage II or III only;
- a war that has many participants but a narrow pair can be safely separated.

Forbidden candidates:

- civil conflict pairs;
- countries marked by event-specific or scripted-war protection flags;
- countries in active existential-threat mechanics or nonhuman-country roles;
- wars in which either selected country has capitulated;
- pairs where the effect would obviously strand subjects, overlords, or faction leaders in invalid war state;
- pairs whose capitals are occupied by the intended enemy;
- wars where a focus, decision, or event chain has marked the war as protected until its resolution;
- countries that recently received a White Peace settlement with each other.

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

> White Peace searches for safe wars that can end without conquest, indemnity, or scripted-story damage. At first it settles one minor country pair. Later evolutions can settle several minor pairs, rarely include a major country, or issue broader diplomatic settlements when the world has too many wars. Its selection weight rises with active wars and valid minor-war candidates, but repeated firings and higher evolutions keep it from becoming common.

Recommended evolution-summary text:

- **Repeated Minor Settlements** — one firing can quiet several minor fronts.
- **Major-Country Settlement** — a rare settlement can involve a major country when the war is safe.
- **Broad Diplomatic Settlement** — a late-stage firing can remove a larger portion of war clutter without touching protected wars.

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

**Title direction:** A Note Without Demands

**Description direction:** A neutral consular channel delivers identical terms to both governments. The papers name no victor, no indemnity, and no border change. Staff officers are ordered to hold the same line they held before the first shot mattered.

**Option direction:** Let the guns fall silent.

### Stage I popup variant

**Title direction:** Tables in Several Rooms

**Description direction:** More than one minor front receives the same formula: no claims, no reparations, and no ceremony. The notices move faster than the newspapers can explain them.

**Option direction:** No one claims victory.

### Stage II popup variant

**Title direction:** A Major Power Steps Back

**Description direction:** A major government signs away one part of its war without procession or triumph. Diplomats call it prudence. Officers call it an order. The border posts call it quiet.

**Option direction:** The order has already been given.

### Stage III popup variant

**Title direction:** The Armistice Circular

**Description direction:** A diplomatic circular passes through several capitals, carrying the same thin formula from front to front. Not a treaty of friendship, not a surrender, not a settlement of old hatred. Just enough paper to make guns stop.

**Option direction:** The line goes quiet.

## Report and news presentation

A normal report-event image is enough for this event. The visual should be restrained: a document table, a radio room, border officers lowering weapons, or diplomats in a dim corridor. It should not show a grand treaty hall or cheering crowd.

If a later implementation adds a news popup for stage III only, use a black-and-white news image showing newspaper bundles, telegraph offices, or a quiet border checkpoint rather than a triumphant peace conference.

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
| `achievement_white_peace_no_winner` | No Winner, No Spoils | Have a White Peace settlement end a war where neither selected country has lost its capital and both survive at least 180 days afterward. | Visible |
| `achievement_white_peace_chain_of_tables` | A Chain of Tables | In one campaign, see several separate minor pairs settled before any major-country settlement branch fires. | Hidden |
| `achievement_white_peace_silence_of_giants` | Silence of Giants | Be part of a major-country settlement after a long war without receiving conquered territory from that war. | Hidden |
| `achievement_white_peace_the_circular` | The Circular Reaches Every Desk | Have a broad diplomatic settlement end at least three separate safe conflicts or five safe pairs from one firing. | Hidden |

Achievement implementation must track that the settlement came from Event 009 and not from ordinary peace conferences or scripted peace events.

## Asset coverage

Required asset directions:

- one report event image, `210x176`, period-documentary style, likely generated unless a public-domain/source image clearly fits;
- optional stage III news image, `397x153`, black-and-white, if the implementation adds news presentation;
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
7. Base firing settles exactly one safe minor-versus-minor pair.
8. Stage I can settle several safe minor pairs but stays capped.
9. Stage II can rarely involve a major country only when safety gates pass.
10. Stage III can settle a broader safe segment but cannot erase protected wars.
11. The popup has no continue-war option.
12. Candidate selection excludes protected scripted content, civil conflict, nonhuman/special threat actors, near-capitulation cases, and recent pair repeats.
13. Event log, event detail, evolution detail, cluster detail, and localisation agree.
14. Report image and achievement icon needs are handed off.
15. Implementation validation includes no-war, one-minor-war, many-minor-war, major-war, protected-war, repeated-firing, and high-evolution test cases.
