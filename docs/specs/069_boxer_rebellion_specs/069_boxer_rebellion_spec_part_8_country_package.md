# A durable Boxer government

A Boxer government emerges when the movement can maintain territory, institutions, and an army beyond a temporary local seizure.
Its central problem is how to turn a collection of societies into a state without losing the local support that made the uprising possible.
It must also decide which foreign relationships it rejects and which forms of learning, trade, and diplomacy it can accept under its own control.

## Activation conditions

The normal route requires at least two viable connected stronghold states or an equivalently reviewed connected territorial package, a functioning administrative center, sustained recruitment and supply, and a successful 90-day institutional hold.
Boxer Strength should normally be at least 65, but that value is only one requirement.
A movement with no territory, equipment, or administration cannot become a durable state because its meter is high.

The territory must be held through actual control, an accepted Chinese transfer, or a supported country-creation process arising from the conflict.
A state which is merely reported as sympathetic is not transferred automatically.
Its former owner, current controller, and any relevant settlement commitments must be considered separately.

Use `BOXER_CARRIER` only as a semantic placeholder in planning.
It is not an engine tag.
The implementation must first search the installed vanilla definitions, the Chaos Redux registry, Workshop mods, and local mods for a compatible carrier and naming conflicts.
No three-character tag is declared available by this package.

The Event 006 collections are active views, while its registry also tracks dormant reservations.
Membership in one of those collections does not authorize loading that event's country package.
A reused carrier needs Event 069 origin, identity, territory, and readiness proof.
An already living country with meaningful content must not be overwritten because its tag appears convenient.

## Country setup transaction

The activation process establishes owned territory and a valid capital before capital-dependent setup.
It records the creating origin, applies the appropriate country content, and transfers or creates only the assets authorized by the activation record.
The player can explicitly choose to continue as the new country when the supported handover route is offered.
Player transfer is never automatic merely because the player supported the movement.

| Surface | Required behavior |
| --- | --- |
| Territory | Only the actual founding strongholds and agreed transfers, with one receipt per state |
| Capital | A secure administrative center with a valid alternate if the preferred city is unavailable |
| Initial cores | Only reviewed founding homeland states whose local authority supports the new state |
| Further Chinese territory | Claims, agreements, or integration objectives according to Part 9, not instant cores everywhere |
| Army | Existing accepted formations plus fully funded recruits, with no duplicate ownership |
| Equipment | Finite local, captured, or donated allocations, reconciled before transfer |
| Navy and air force | No free fleet or air force. Existing lawful transfers need separate evidence |
| Industry | Buildings already present in transferred states, without a second founding reward |
| Supply | Actual ports, railways, hubs, infrastructure, and access arrangements |
| Technology | A reviewed modest starting set consistent with functioning weapons and workshops |
| Diplomacy | Actual sponsors, opponents, guarantees, subjects, and current wars |
| Event state | The same crisis instance, Strength, Pressure, interests, and commitments |

A state transfer preserves its civilian history and shared crisis records.
Recruitment does not count as death.
Captured equipment does not reappear in the donor's stockpile when the new country is activated.
Untransferred formations remain with their actual owner.

## Initial political and economic position

The proposed starting anchors for a genuinely new country are 50 Political Power, 25 Command Power, 35 Stability, and 65 War Support.
The final setup may adjust those values from the actual founding agreement and recent results.
These anchors do not reset the resources or political condition of an existing country receiving an overlay.

The default institutional identity is a non-aligned coalition of societies.
This is a deliberate design classification for the fictional revived movement, not a claim that historical Boxers followed a modern HOI4 ideology.
An existing Chinese sponsor keeps its current ideology unless it later makes an explicit political choice.

A new Boxer state begins with two research slots.
A successful education and industrial program can support a third, and a substantial later state can earn a fourth.
Slots are indivisible engine counts and therefore exceptions to the numerical tuning preference.
A small rural enclave cannot unlock a major research establishment through one unconditional focus.

Starting technology must support the actual inherited or funded equipment.
The package should know how to operate its basic rifles and workshops, but it should not inherit every advanced technology researched by a former owner.
The implementation must enumerate the real current technology IDs and test all references.
Air, naval, and advanced research access follows later industrial and educational capacity.

Laws must be legal for the current country state.
A movement emerging in wartime does not receive every maximum mobilization law as a free founding package.
The political and military routes provide the means to change recruitment, economy, and trade policy through actual conditions and costs.

## Institutions and character roles

The founding leader is an institutional council unless a properly sourced, period-valid individual is selected during the country research pass.
Do not resurrect a leader from the historical 1900 rebellion without an explicitly separate supernatural premise.
Do not invent a realistic historical-looking person to fill a missing source slot.

| Role | Gameplay purpose | Identity and asset requirement |
| --- | --- | --- |
| Founding council | Represents the participating societies and chooses the first compact | Authenticated institutional source material with a clear explanation of what it represents |
| Civil administration representative | Supports local agreements, reconstruction, and integration | A verified available person or a defensible institution, with ownership checked |
| Command representative | Coordinates recruitment and regularization | A verified living commander or a legitimate transferred existing character |
| Arsenal and transport representative | Connects production, repairs, and supply | A sourced technical or institutional identity with appropriate role evidence |
| Diplomatic representative | Negotiates guarantees, recognition, and withdrawal | A sourced and available identity, not a duplicate of another country's active official |

A sourced historical object can represent institutional continuity when the portrait brief explicitly identifies it as an object.
It must not be captioned as a photograph of a fictional 1936 council or of people who were not present.
The exact source selection remains a production requirement.

Any individual character requires a name-variant search across the installed country, character, portrait, history, and localisation files.
An existing owner must release or transfer the character through a guarded process before another country recruits that person.
Missing identity or ownership evidence blocks that portrait and recruitment path.
No final character names or finished portrait assets are supplied by this planning package.

## Army identity

The early army is locally raised, unevenly equipped, and dependent on familiar routes.
Its strengths are local mobilization and willingness to defend a meaningful position.
Its weaknesses are sustained supply, centralized command, equipment variety, and operations far from supporting communities.

Use existing infantry and suitable cavalry battalions as the initial mechanical building blocks.
The five-battalion militia template is a design anchor, with actual requirements read from the installed game.
A later professional core can use verified standard infantry templates and support companies after the relevant equipment and training programs are complete.

The army branch should improve the country's real ability to sustain and coordinate formations.
Do not make an untrained rifle militia defeat tanks through a permanent universal attack multiplier.
Ritual operations are separate, bounded effects with their own conditions.

Starting models can use a verified period-appropriate installed Chinese infantry consumer when the ordinary battalion type remains unchanged.
The exact entity and its ownership need local inspection before reuse is confirmed.
A distinct division-template emblem is planned for the Boxer formations.
A genuinely new subunit would require a separate technology, equipment, counter, model, audio, and CXT package and cannot be introduced as an undocumented shortcut.

## Three event-owned spirit slots

At most three Event 069 national spirits may be active at once, including those created by its focus tree and settlement.
This cap does not delete unrelated vanilla or other-event ideas.
Do not evade it by scattering the same permanent institutional bonuses across hidden replacement ideas.

| Slot | Initial institution | Development | Failure or replacement | Mature outcome |
| --- | --- | --- | --- | --- |
| A Political compact | A loose assembly of societies | Negotiated civic federation, centralized command government, or religious governing council | Local withdrawal, contested leadership, or an amended compact | One route-specific governing institution |
| B Military organization | Emergency local levies | Accepted auxiliaries, coordinated regional forces, then a sustainable national core | Unfunded formations, failed regularization, or command disputes | One coherent military institution or legal local-militia settlement |
| C External obligations | Empty unless the founding settlement requires it | A specific protocol, restricted privilege, or temporary occupation commitment | Amended terms, moratorium, or a documented breach | Removed after obligations end, or replaced by one continuing agreement |

The initial economic weakness is represented primarily by actual industry, resources, transport, and equipment.
It does not require another permanent national spirit.
A ritual effect should use its correct temporary operational consumer and must not become a fourth permanent country-wide institution.

## Existing Chinese governments

A government that supports the Boxers can retain a permanent anti-foreign political route without becoming the new Boxer country.
Its continuing tools concern concession revision, control of foreign bases, protected trade, auxiliary regulation, and negotiation from a stronger position.
The route preserves the government's meaningful existing focus tree and political identity.

Use additive decisions and events as the guaranteed cross-country interface.
A safe focus connection may be added when the installed tree provides a verified integration path.
Do not replace an entire Chinese DLC or mod tree with a small generic Boxer tree to obtain that connection.
The dedicated tree in Part 9 belongs to the actual Event 069-created Boxer government or a separately approved deliberate transformation.

## Survival and closure

A surviving Boxer government continues to use ordinary civilian systems.
Its population is human, including when it follows a supernatural ritual route.
Register its event origin in the shared special-country classification where required, but do not classify it as nonhuman or exempt it from famine, migration, disease, or ordinary civilian consequences.

Defeat can dissolve its government, integrate its formations, or leave a legal regional institution under the settlement.
Every path preserves the ownership accounting and actual political result.
The end of the crisis does not delete a surviving country, its factories, completed research, or its legitimate focus progress.
