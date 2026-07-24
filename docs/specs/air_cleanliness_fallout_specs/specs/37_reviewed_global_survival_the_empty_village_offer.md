# The Empty Village Offer

## Event identity

The Empty Village Offer is a Year 2 settlement event for a country that has survived the first generation of refugee and specialist decisions. A remote settlement still has roofs, a road, and a damaged field ledger, but its former population is gone or scattered. The country must decide who receives the empty rooms and who is allowed to speak for the land.

The event is a relationship and migration chain. It records population movement and settlement legitimacy in country-owned ledgers. It does not create a tag, a character, or a new country. A later successor allocator may read the settlement memory only after a live conflict ledger proves that no native country or dynamic tag owns the land.

## Opening situation

The candidate state is selected deterministically by the lowest valid native state id. It must be controlled by the player country, have a durable Fallout state row, carry a produced Air Winter snapshot, retain some population, and remain remote, scarred, ash-damaged, or dead-city grade. The state must not be a major urban category. A surviving infrastructure or industrial building proves that the village can be repaired rather than merely described.

The opening report should show empty rooms, a public well, a frost-broken field, and a road marker covered by ash. The voice is a local registrar who has read the names on the last census and now has to decide whether an empty place is an invitation, a military reserve, or a border warning. The text should name the selected state's climate and nearby route when scripted localisation can do so. It should avoid generic apocalypse language and avoid treating migration as an abstract population number.

## Player branches

| Branch | Government-aware direction | Immediate sacrifice | Intended identity |
| --- | --- | --- | --- |
| Resettle refugee families | Democratic or neutral governments | Food, Medicine, Recognition, and Cohesion | A civic settlement that keeps family names, school records, and property claims visible. |
| Grant veteran allotments | Fascist or neutral governments | Food, Medicine, Recognition, and Cohesion | A guarded settlement built around service, patrol roads, and veteran land grants. |
| Charter a mixed village | Democratic or communist governments | Food, Medicine, Recognition, and Cohesion | Refugees, local survivors, and returning workers share a water rota and council. |
| Keep the village as a border buffer | Fascist or communist governments | Food, Medicine, Recognition, and Cohesion | A lightly settled frontier reserve that values warning time and access denial over growth. |

The option text should sound like the institution making the offer. Civic text should be careful and concrete. Veteran text should be terse and duty-focused without celebrating coercion. The mixed-village option should carry guarded hope and arguments over language, land, and old borders. The buffer option should use official understatement that makes the cost of leaving rooms empty visible through the effects.

## Result grading

The country freezes Food, Medicine, Recognition, Cohesion, the settlement, land-legitimacy, border-security, and integration ledgers, plus the current generation and target state. A weighted viability score uses the four ledgers, the country resources, Cohesion, and the selected state's Air Winter values. Each branch has a success floor and a partial floor. The result arrives after 42 days and applies a branch-specific state modifier for 360 days.

Success raises Adaptation, Reclamation, and Supply Access while reducing Exposure. Refugee, veteran, and mixed success moves a bounded migration ledger and adds a measured manpower reserve. Refugee and mixed success change the selected state to a rural category. Veteran success changes it to rural and adds a border-security memory. Buffer success changes the selected state to pastoral, improves warning memory, and deliberately moves less population.

Partial success preserves the settlement attempt but leaves unresolved claims. It improves Reclamation and Supply Access by less, raises Exposure through unfinished works, and records a smaller migration ledger. Failure damages infrastructure or an industrial complex, lowers Reclamation and Supply Access, raises Exposure, applies a temporary failure modifier, and routes a proportionate population loss through the Deaths system.

## Five-hundred-day callback

The callback asks whether the village has become a home, a garrison, a divided council, or an empty roadblock. It arrives 540 days after the result. Success closes the settlement memory with durable land and integration values. Partial success keeps a usable route but leaves a live grievance. Failure applies a second bounded Deaths loss, closes the memory as a warning, and leaves the country with a settlement ledger that future migration and border events can read.

The callback must update the same selected state. It applies Adaptation, Reclamation, Supply Access, and Exposure changes, uses a callback-specific dynamic modifier, and records a state flag before cleanup. Cleanup releases both delayed-result receipts only after their exact event tokens are authenticated.

## AI policy

AI chooses deterministically from branch weights. Democratic AI prefers refugee families unless Recognition is low, then it prefers a mixed village. Neutral AI prefers the branch with the highest Food and Cohesion reserve. Fascist AI prefers veteran allotments when border security is weak and otherwise keeps a buffer. Communist AI prefers a mixed village when Cohesion is stable and a buffer when the selected state's Exposure is high. Every hidden resolution uses the same frozen ledgers and callback path as the human lane.

## Memory and follow-up use

The chain writes settlement, land-legitimacy, border-security, integration, veteran, and migration ledgers. It writes a branch memory and result state flag but does not allocate a tag or a native character. Later events may use the memory for the Empty Village Offer follow-up, a refugee property dispute, a veteran patrol institution, a border commission, or a successor conflict. Any tag or country creation must wait for a live conflict ledger and a proven player-country preservation step.

## Assets and localisation direction

Use one dedicated generated report image showing the empty village, its well, field, frost, ash, and road marker. It must be a period-authentic alternate-history report illustration with no readable text, flags, or modern objects. Keep the source PNG, processed PNG, DDS, prompt, manifest, and `.gfx` handoff in the event asset workspace while this tranche remains dormant.

Write concrete state and government-aware localisation for the opening, four policies, twelve branch and outcome result descriptions, the callback, and fifteen Event Log payloads. The text must contain no em dashes or semicolons. Do not reveal hidden viability values or describe implementation history.

## Review boundary

The chain remains dormant until the Fallout scheduler, host authority, save recovery, blackout ownership, multiplayer delivery, and runtime Event Log path are proven. It counts as seven defined but uncountable blocks in the release-floor ledger. Native state-population relocation is not claimed. The migration ledger and manpower effect are the bounded engine-safe representation for this tranche.
