# Event 12 Africa polity catalog notes

## Catalog purpose

`012_africa_polity_catalog.csv` contains 215 candidate identities.

The catalog is intentionally broader than the expected implementation. It gives the implementation team enough material to build a continent that contains regional states, old kingdoms, sultanates, city-states, confederations, trade powers, pastoral polities, island powers, sacred centres, and high-chaos actors.

The catalog should not be implemented as 215 equal countries.

## Package tiers

### Tier A

Tier A candidates can support a major country package.

A Tier A package normally needs:

- distinct public identity
- route-aware name variants
- full flag set
- leader or collective body
- starting ideas
- starting forces
- reinforcement path
- focus overlay or bespoke tree branch
- decision family
- AI route plan
- asset package
- League and rival-bloc behaviour
- integration outcome
- postwar handling

### Tier B

Tier B candidates can support a regional member package.

A Tier B package normally needs:

- direct public name
- flag set
- leader or court
- one regional identity mechanic
- several decisions or missions
- starting forces when expected to fight
- AI behaviour
- integration and autonomy outcomes
- regional asset family

### Tier C

Tier C candidates are rare restorations, local autonomy packages, city-states, smaller kingdoms, or flavour-rich subjects.

A Tier C identity may use:

- a compact country package
- a shared regional focus overlay
- a regional decision family
- a special leader or court
- one strong local mechanic
- a rare reveal condition
- a federal or autonomous member state rather than a fully independent long-lived country

Tier C is not permission to create an empty tag.

## Regional counts

| Region | Candidate count |
| --- | ---: |
| Maghreb and Sahara | 21 |
| West Atlantic and western Sahel | 34 |
| Gulf of Guinea and central western Sahel | 29 |
| Congo Basin and Angola | 22 |
| Nile, Horn, and Ethiopian highlands | 28 |
| Great Lakes and East African interior | 14 |
| Swahili coast and western Indian Ocean | 18 |
| Southern Africa | 29 |
| Madagascar and nearby islands | 12 |
| High chaos | 8 |
| Total | 215 |

## Selection rules

The final implementation should choose packages through regional needs and route interaction.

A balanced first implementation should include:

- at least 3 Tier A anchors in West Africa
- at least 2 Tier A anchors in Central Africa
- at least 3 Tier A anchors in North-East and East Africa
- at least 3 Tier A anchors in Southern Africa
- at least 1 Tier A island package
- at least 1 Saharan anchor
- at least 1 Great Lakes monarchy
- at least 1 Swahili coastal power
- at least 1 restored polity capable of leading a rival bloc
- several Tier B members in every region
- a smaller number of Tier C identities tied to local congress outcomes

The implementation can expand later. It should not fill every state with a restoration simply because a candidate exists.

## Overlap groups

The `overlap_group` field identifies candidates that compete for territory, legitimacy, institutions, or political inheritance.

Examples:

- `nubian_web` contains Kush, Meroe, Nobatia, Makuria, Alodia, and Nubia
- `zimbabwe_web` contains Mapungubwe, Great Zimbabwe, Torwa, Mutapa, Rozwi, and Butua
- `yoruba_web` contains Oyo, Ife, Ijebu, Owo, Egba, Ijesha, and Ondo
- `akan_web` contains Bono, Denkyira, Akwamu, Asante, Fante, Akyem, and Baoulé
- `luba_lunda` contains Luba, Lunda, and Kazembe
- `kongo_web` contains Kongo, Loango, Kakongo, and Ngoyo
- `swahili_coast` contains major coastal and port identities
- `madagascar_web` contains the major island political identities

An overlap group should use one or more of these outcomes:

- one winner and several autonomous regions
- a federation
- a dynastic settlement
- a congress settlement
- mutually exclusive restorations
- a modern republic that recognises historical regions
- a rival-bloc conflict
- a high-chaos fusion

Do not grant simultaneous full cores to every identity in one overlap group.

## Public-name rules

The `public_name` column is a readable map identity.

Final ideology variants can use:

- Kingdom of X
- Sultanate of X
- Republic of X
- X Union
- X Commune
- X Federation
- X Empire

Avoid public names built from:

- Authority
- Office
- Mission
- Board
- Bureau
- Compact
- Secretariat
- Committee
- Command

Those terms can name internal institutions.

## Historical basis and confidence

The catalog combines:

- major historical polities with strong source anchors
- regional historical polities needing deeper state and symbol research
- archaeological or civilisational identities that need careful political framing
- living or surviving monarchical and traditional identities
- fictional high-chaos actors

`research_status` and `source_anchor` must be read before implementation.

A row marked specialist review required should not receive final borders, flags, leaders, or claims from memory alone.

## Technical naming

`candidate_key` values are neutral planning keys.

They are not guaranteed final country tags or cosmetic-tag identifiers.

Final technical identifiers must:

- avoid conflicts
- use stable lowercase snake_case where allowed
- avoid raw obscene strings
- avoid final unresearched super-event titles
- preserve public-name readability separately in localisation

## Implementation staging

### Stage 1

Build the host package, Charter League, regional overlays, and 20 to 30 priority polities.

### Stage 2

Add another 30 to 50 Tier B and Tier C packages through congress outcomes, rival blocs, and regional restoration routes.

### Stage 3

Add high-chaos identities and rare restoration webs after grounded integration works.

### Stage 4

Expand only where the completion audit finds regional gaps. Do not add tags for count alone.

## Acceptance rule

The catalog succeeds when Africa feels politically plural during unification.

It fails when:

- every country is an identical subject
- every restored polity has the same tree
- every region uses the same units and decisions
- historical identities appear only as names
- the unifier can annex all candidates without negotiation
- high-chaos actors replace human politics before the grounded routes matter
