# 097 Collaboration
## Part 1: Core identity and the global grant

## Catalog identity

| Field | Design |
| --- | --- |
| Event | 097, Collaboration |
| Type | Minor Repeatable |
| Status | To Be Reworked |
| Minimum Chaos level | 1 |
| Cluster | Intelligence |
| Cluster role | Medium member |

The event gives every valid country prepared collaborators inside every other valid country. Countries remain responsible for declaring and winning their wars. Their enemies are simply less united, and successful occupiers inherit people willing to help administer the conquered territory.

The central rule remains easy to communicate: everyone has collaborators everywhere. A country benefits from its networks abroad while facing the same danger at home. Good relations provide no exemption. Neither do democracy, faction membership, subject status, neutrality, or having no intelligence agency.

The event changes the existing collaboration mechanic. It does not introduce a resource to accumulate or spend, a second intelligence agency, an administration minigame, or a diplomatic agreement between the participating governments.

## The moment it happens

The first manifestation is a worldwide discovery. Ministries learn that apparently loyal local figures have already made arrangements with foreign powers. Foreign intelligence services discover useful contacts they never recruited. Several rival powers can receive promising approaches from different people inside the same country.

The player receives a short report explaining the actual mechanical change and its reciprocal danger. Acknowledging this report does not accept or refuse the effect. The global grant has already happened. Leaving the report open cannot protect the player's country, delay another country's benefit, or create an advantage in multiplayer.

The report should convey uneasy opportunity rather than international friendship. Its humor comes from the absurd universality of the situation. An ally can sincerely promise military assistance while its future occupation administration quietly waits next door.

## What one layer means

At baseline, one firing adds **10 percentage points of native prepared collaboration** to every valid directed country pair.

Use the notation C(A, B) for collaboration that country A has prepared inside country B. A is the prospective occupier. B is the country whose officials or inhabitants may collaborate. C(A, B) is separate from C(B, A).

For the nominal native scale of 0 to 100, the grant is:

`C_after(A, B) = min(native maximum, C_before(A, B) + grant)`

The 100-point scale is the design's normalized presentation. Implementation must use the installed engine's actual units and verified upper bound. The event never increases the meaningful native maximum.

The same grant is offered in both directions. Final values do not have to be equal. A country that previously invested in a collaboration operation retains that advantage.

For example, if A has 45 collaboration inside B and B has 10 inside A, a baseline firing leaves them at 55 and 20. It does not equalize both values at 55 or overwrite both with 10. A pair at 95 gains only the remaining 5. A pair already at the native maximum gains nothing further.

The event never resets existing native collaboration, replaces it with a global total, or awards a fresh full layer for every enemy separately when a country capitulates.

## Country eligibility

Eligibility is a technical question about a living political country and the native mechanic. It is not a judgment about ideology or plausibility.

Include ordinary majors and minors, player and AI countries, faction members, subjects, overlords, countries at peace, and countries already at war. Include unusual Chaos Redux countries when they are actual political countries supported by the native collaboration and occupation systems. An unusual name, ideology, species, or origin alone is not a reason to exempt a country.

Exclude self-pairs, nonexistent dormant tags, and administrative helper scopes that are not countries in the playable world. An exiled or capitulated country participates whenever the native backend supports its current identity. A lack of an agency or operatives must not become an eligibility gate.

If a particular special-country backend cannot support native collaboration, the implementation must identify the exact incompatibility. It must not quietly exclude all special countries with a broad classifier or replace their grants with generic surrender modifiers.

A firing takes one snapshot of eligible countries. Both directions are evaluated from that same snapshot. A country released afterward joins the next firing. It receives no retrospective grant for every earlier occurrence. A dormant claimant that becomes a real country through Event 095 follows this same rule.

## What collaboration changes

Prepared collaboration should retain the native benefits associated with weakening an opponent's determination to continue fighting and preparing administration after conquest. The first firing therefore makes future wars easier to conclude and makes the eventual occupation more manageable.

There are three distinct stages of play:

1. **Before conquest:** A has a prepared network inside B.
2. **During and after conquest:** Eligible occupied territory receives the benefits appropriate to native collaboration and the active evolution.
3. **Government formation:** A may use the normal collaboration-government route when its actual requirements are met.

Prepared collaboration is not itself ownership, compliance in every state, or an installed government. It does not grant A a claim, core, war goal, military access, B's factories, or the ability to command B's army. It also does not dissolve B's faction or determine the result of a peace conference.

At baseline, use the native timing of collaboration conversion. Do not promise that merely moving across a border instantly produces the post-capitulation compliance benefit. Evolution II adds a specifically defined earlier administrative effect.

## War remains a war

A strong collaboration network makes a successful campaign more effective. It is not a substitute for fighting one. An untouched opponent does not surrender because the world received a layer of collaboration. An enemy's divisions do not disappear, turn friendly, or open a corridor through the front.

A country can continue resisting through military success, protecting important territory, and recovering from a threatened defeat. It does not need a special anti-Collaboration button to remain playable. Ordinary counterintelligence and occupation mechanics retain their normal behavior wherever they actually affect native collaboration. The event does not invent a universal purge that erases every opponent's networks.

Existing native collaboration governments are not destroyed or converted when a new firing occurs. Their own active countries can receive new networks on the same basis as other eligible countries. Being someone's client does not make a country immune to future foreign influence.

## Player-facing complexity

The player tracks existing native collaboration and compliance where those values already matter. A report may state the amount added and the current evolution, but the event does not add a persistent dashboard of network budgets, loyalties, administrative capacity, or preparedness points.

No event-specific national spirit is required for the core effect. A permanent country-wide surrender penalty would apply too broadly and would obscure which foreign network is responsible. The design keeps the benefit attached to the real relationship between a prospective occupier and its target.

## Boundaries of the promise

Native collaboration governments can become available before Evolution IV through ordinary play. Event 097 must not lock an existing native feature behind its own evolution. Evolution IV makes forming these governments much easier after a qualifying defeat. It is an accelerator, not the first permission for countries that already possess that permission.

Native limitations that would exclude democracies from receiving the event or using its intended evolved government route are implementation problems to resolve. They are not authorization to change the universal concept. Broadly enabling democratic aggression, puppeting, or unrelated diplomatic actions is also outside the event's purpose.
