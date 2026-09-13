# Event 045 AI, balance, achievements, assets, and writing direction

## AI goals

AI should make the event dangerous without behaving as if escalation is always the correct choice.

Regional AI tries to secure its principal objective, preserve the capital and supply network, obtain useful support, and avoid a settlement that destroys its viability. Outside AI chooses between containment and exploitation according to strategic interest and current capability.

Every weighted surface requires a dedicated probability audit before and after implementation changes.

## Regional AI factors

Regional countries consider:

- principal and secondary claim value
- relative army strength
- manpower and equipment reserves
- supply access and rail control
- capital safety
- current war support and stability
- number of fronts
- surrender progress
- available sponsors
- faction and guarantee ties
- ideology and strategic posture
- prior peace and claim memories
- escalation stage
- enabled Evolutions
- The Offensive and other aggression modifiers

Balkan AI is more willing than normal to call allies, activate a valid claim, accept material support, and intervene when its own registered interest is threatened. It is not more willing to commit suicide.

A country near defeat should accept a settlement that preserves government viability when no credible rescue exists. A country with a supplied army, a secure capital, and an imminent sponsor may continue fighting.

## Outside AI factors

Outside powers consider:

- ideology and relations with each camp
- faction and guarantee commitments
- rival powers already supporting the opposite camp
- strategic access to ports, railways, the Straits, or the Mediterranean
- distance and theater reach
- navy, air, convoy, fuel, and equipment capacity
- current war load
- stability and war support
- escalation stage and irreversible floor
- likelihood that containment partners will cooperate
- whether direct intervention creates a new major-power war

Containment becomes more likely when the outside power has limited regional interests, is overextended, faces high escalation, or has credible partners for a conference. Exploitation becomes more likely when a rival has committed first, a guarantee is meaningful, access is available, and the preferred camp can survive.

## AI hard blocks

AI must not:

- select a dead or invalid target
- support a camp that no longer exists
- send aid without a viable route
- guarantee a country it cannot plausibly defend
- invite a country into a faction when ordinary faction rules reject it
- create an opening war between same-faction allies
- activate a disabled Evolution path
- demand an unregistered territorial claim
- reject peace indefinitely after complete military defeat
- trigger direct intervention without forces, access, or war support
- treat special Chaos or nonhuman actors as ordinary Balkan governments

## Balance principles

### Opening viability

The opening should be coherent and survivable, not equal. The camp builder may apply a short event-owned mobilization package only when a valid small country would otherwise enter with no usable force. Such support must scale from its territory, manpower, industry, and opponents. It must not be a free army reward detached from the war.

### Escalation anti-farming

- Aid uses cumulative support tiers.
- Entry, guarantee, faction, and intervention sources record one-shot proofs.
- Repeated opening and closing of transit cannot farm gains or losses.
- A broken armistice records one violation per country and armistice generation.
- Stage reports fire once per upward threshold.
- Maximum stage is stored separately from current stage.

### Decision impact

Every major action changes a campaign choice, map objective, support relationship, settlement term, or escalation state. Tiny isolated modifiers do not count as complete actions.

### Event duration

The event can resolve quickly when one camp collapses or a credible conference succeeds. It can remain active for years when it becomes a wider war. There is no fixed total timer.

### Performance

Processing should be event driven through registered participants, sponsors, claims, and active missions. Do not scan every country every day. Use bounded pulses and owner-local hooks for facts that cannot be captured directly.

## Achievement set

All names below are working labels. Final wording must follow the achievement localisation style and source rules.

### `chaosx_achievement_045_keep_it_regional`

- Working label: Keep It Regional
- Eligible player: original Balkan participant
- Unlock: reach a settlement with the player's government independent and not defeated, maximum escalation below European Crisis, no direct outside-major entry, and at least three opening participants
- Disqualifiers: Force Trigger Mode where achievements are disabled, player changes away from the tracked country, subject status at settlement, or invalid event generation
- Difficulty: Medium
- Why it is not trivial: the player must win or compromise before foreign commitments cross the first outside-power threshold
- Icon direction: a contained flame inside a Balkan frontier outline, designed as a 64x64 achievement image

### `chaosx_achievement_045_the_conference_holds`

- Working label: The Conference Holds
- Eligible player: outside power that was not an opening participant
- Unlock: the conflict reaches European Crisis, the player leads or materially supports a containment conference with at least two cooperating outside powers, an armistice-line mission succeeds, and no hostile major-power pair enters direct war
- Disqualifiers: player directly joins a linked war, player sends an exploitative military commitment after the conference begins, or armistice failure
- Difficulty: Hard
- Icon direction: a conference table holding down a burning border map without generated text

### `chaosx_achievement_045_every_map_is_temporary`

- Working label: Every Map Is Temporary
- Eligible player: original Balkan participant
- Unlock: Evolution I activates, the player settles at least two registered claims through a negotiated or imposed regional settlement, no acquired state lies outside the maintained claim registry, and the event does not reach Another World War
- Disqualifiers: unregistered annexation by the player, event handoff before regional settlement, or player government destruction
- Difficulty: Hard
- Icon direction: layered treaty maps with two clearly different border lines and a wax seal

### `chaosx_achievement_045_no_friends_left`

- Working label: No Friends Left
- Eligible player: original participant that began with at least one camp ally
- Unlock: Evolution III creates a war against a former ally, the player survives independent with its capital, and the event reaches a settlement or wider-war handoff while the player remains active
- Disqualifiers: player becomes a subject, loses its capital permanently before resolution, or never enters the former-ally war
- Difficulty: Hard
- Icon direction: two broken alliance clasps around one surviving flagpole with no actual national flag

### `chaosx_achievement_045_a_very_small_incident`

- Working label: A Very Small Incident
- Eligible player: original participant in an absurd-frontier-incident opening
- Unlock: Event 045 becomes the verified origin of Another World War and the player survives for a defined post-handoff period
- Disqualifiers: pre-existing global war blocks origin proof, player country is annexed, or the opening cause was not the absurd incident family
- Difficulty: Very Hard
- Icon direction: a tiny broken border marker casting an oversized world shadow

### `chaosx_achievement_045_the_entente_reversed`

- Working label: The Entente Reversed
- Eligible player: Balkan participant or regional mediator
- Unlock: a settlement is signed by at least four surviving Balkan governments, at least two signatories began on opposing camps, every signatory remains independent, and none is annexed through the settlement
- Disqualifiers: fewer than four valid signatories, annexation of a signatory, or world-war handoff before agreement
- Difficulty: Hard
- Icon direction: four distinct hands around a Balkan pact document, no readable generated text

Each achievement requires tracking, localisation, three achievement-state assets where the engine pattern requires them, docs, and completion audit.

## Asset inventory

### Super-event images

1. Opening outbreak image
2. Another World War handoff image

The second image is used only when the final stage proof is met.

### Report and news images

- additional Balkan entrant
- foreign arms and volunteers
- guarantee or faction enforcement
- direct major intervention
- armistice or settlement

A smaller reusable report family may be used when the images remain distinct enough to communicate the stage cause.

### Decision category picture

One static picture showing a Balkan frontier rail junction, crowded mobilization, border barriers, and a visible route toward a port or mountain pass. It must contain no fake controls, meters, or generated text.

### Decision and mission icons

- regional claim
- arms shipment
- volunteers or military mission
- strategic corridor
- mediation
- armistice
- allied occupation dispute
- regional mobilization
- transit access
- guarantee
- faction invitation
- sanctions
- direct intervention
- rail-line mission
- port-corridor mission
- armistice-line mission
- Straits mission

Each icon family is designed for its own consumer. Decision and mission icons are not resized achievement art.

### Achievement icons

Six independent 64x64 completed icons plus the required grey and not-eligible variants according to the current achievement consumer.

## Asset source direction

The opening and report art may use sourced period photographs when the subject is real historical mobilization, diplomacy, or frontier activity. A fictional alternate-history composition may use generated 1936-1945 documentary-style art. The source mode must be recorded for each image.

Icons use native transparent ImageGen output and preserve alpha. The category picture and super-event scenes use the full-canvas treatment required by their inspected consumers.

No visual should joke about casualties. The restrained humour belongs in the recurrence and diplomatic framing.

## Super-event writing direction

### Opening

- Viewpoint: Europe learns that several Balkan armies are already moving
- Visible facts: regional camps, mobilization, frontier claims, and foreign governments watching
- Tone: restrained dark humour followed by immediate seriousness
- Uncertainty: whether outside powers will contain or exploit the war
- Avoid: generic map-change language, jokes about victims, and unsourced famous quotations

### Another World War

- Viewpoint: the regional origin has become a multi-major or multi-faction conflict
- Visible facts: direct major-power war and fronts outside the original theater
- Tone: grave and concise
- Uncertainty: none about the scale, but the eventual settlement remains open
- Avoid: treating the result as a terminal world end

The often-attributed Bismarck remark about a foolish event in the Balkans is not approved as a final quote because its provenance is uncertain. A text researcher may reconsider it only after finding a reliable original source. The final quote, cultural remark, and button wording require separate research.
