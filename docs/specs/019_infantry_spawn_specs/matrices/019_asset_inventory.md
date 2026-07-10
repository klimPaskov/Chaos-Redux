# Event 19 Asset Inventory

All filenames and sprite names below are proposed working identifiers. The asset producer must preserve any final identifiers registered by implementation.

## Event and report images

| Asset | Type | Target | Source mode | Direction | Proposed identifier |
| --- | --- | ---: | --- | --- | --- |
| Initial manifestation | report event image | 210 by 176 | generated period documentary | recruits, horses, trucks, guns, and improvised camps in one readable scene | `report_event_019_infantry_spawn_manifestation` |
| Organized muster | report event image | 210 by 176 | generated period documentary | coherent columns and staff maps with unexplained origin | `report_event_019_infantry_spawn_organized` |
| Arsenal lottery | report event image | 210 by 176 | generated period documentary | mismatched serious vehicles and infantry at a rail yard | `report_event_019_infantry_spawn_arsenal` |
| Claimant emergence | report event image | 210 by 176 | generated period documentary | frightening commander reviewing impossible mixed formation | `report_event_019_infantry_spawn_claimant` |
| Anomalous muster | report event image | 210 by 176 | generated fictional period documentary | ordinary soldiers beside bounded zombie, ghost, or golem visual cues | `report_event_019_infantry_spawn_anomalous` |
| Derivative release family set | news or report images | 397 by 153 or 210 by 176 | generated | zombie, ghost, and golem regional revolts | family-specific identifiers |
| Derivative defeat family set | report images | 210 by 176 | generated | containment and aftermath without parent-event imagery | family-specific identifiers |

Every report image receives the project report-card processing and sepia treatment.

## Decision and idea icons

| Family | Needed icons | Type and size | Direction |
| --- | --- | --- | --- |
| Category | one baseline category icon | decision category pattern | ranks of incompatible soldiers around a muster seal |
| Audit | audit, census, equipment ledger | decision 32 by 32 | roster, tags, crates, officer lists |
| Integration | territorial role, standardization, emergency integration | decision 32 by 32 | unit markers, training, hurried deployment |
| Supply | rail corridor, depot, relocation | decision 32 by 32 | train, depot, route, convoy |
| Demobilization | supervised demobilization, breakup, disarm | decision 32 by 32 | stacked rifles, opened formation mark, guarded depot |
| Requests | field, mobile, territorial, firepower, anything, anomalous | decision 32 by 32 | distinct request silhouettes at tiny scale |
| Claimant | command, counter-command, arrest, retirement, takeover | decision 32 by 32 | epaulette, split command baton, guarded portrait |
| Anomalous | cantonment, liaison, restriction, sustainment, seal breach | decision 32 by 32 | seal, barrier, family-neutral anomaly symbols |
| Core values | Muster Control, Army Congestion, Claimant Influence, Anomalous Saturation | idea or UI icons 64 by 64 | distinct consistent symbols and color identities |
| Temporary burdens | supply strain, command confusion, training saturation, equipment debt | idea icons 64 by 64 | strong central symbolic art |

Decision, idea, and focus icons require separate source artwork designed for their target size. They cannot be resized versions of one another.

## Scripted GUI assets

| Asset | State variants | Target | Animation |
| --- | --- | --- | --- |
| Muster Board background | static | final GUI dimensions after layout | no |
| Overview header | inactive, active, critical | layout-specific | critical can use seal pulse overlay |
| Formation lot card | normal, selected, locked, resolved, dangerous | layout-specific | no |
| Quality and coherence markers | four bands each | small UI | no |
| Command portrait frame | normal, demand, critical, revolt | 156 by 210 frame-compatible | critical border animated |
| Registry family card | unavailable, available, active, contained, breach | layout-specific | active emblem can animate |
| Cost and warning markers | met, missing, cooldown, invalid target | small UI | no |

## Animated packages

| Package | Frames | Frame target | FPS | Loop | Required deliverables |
| --- | ---: | --- | ---: | --- | --- |
| Muster seal pulse | 8 | determined by category or GUI layout | 6 to 8 | yes | source frames, processed frames, sheet PNG and DDS, static fallback, GIF preview, contact sheet |
| Critical command border | 8 | portrait-frame dimensions | 5 to 7 | yes while critical | same full package |
| Anomalous registry emblem | 10 | determined by registry tab | 4 to 6 | yes | same full package |

Every frame must be a real generated or edited source frame. Local transform-only motion is forbidden.

## Claimant portraits

- 20 fictional generated portraits at 156 by 210.
- 10 male-presenting and 10 female-presenting.
- Exact slot directions are in `019_possessed_general_matrix.md`.
- Static only.
- Each manifest entry records presentation and matching name-pool requirement.

## Derivative country flags and portraits

| Family | Base flags | Route flags | Leader assets |
| --- | --- | --- | --- |
| Zombie derivative | normal, medium, small | claimant, collective, species command when visually distinct | claimant reuse plus generated alternate leader or council |
| Ghost derivative | normal, medium, small | same route logic | claimant reuse plus generated spectral leader or council |
| Golem derivative | normal, medium, small | same route logic | claimant reuse plus generated master-builder or construct council |

Flags are fictional generated art and need separate intentional route designs, not recolors.

## Derivative focus icon families

Each focus tree route needs icon coverage. The exact final focus count belongs to implementation, but the asset prompt should plan coordinated icon families for:

- opening survival
- hierarchy claimant route
- hierarchy collective route
- hierarchy species-command route
- sustainment and economy
- reinforcement and military method
- former-parent war
- regional expansion
- integration
- family transformation
- late regional predator payoff

Focus icons are 94 by 86 and need focus-specific source art.

## Achievement assets

Every achievement in `019_achievement_matrix.md` needs:

- completed 64 by 64 source and DDS
- grey variant
- not-eligible variant using the project overlay
- root achievement filenames matching final achievement IDs

## Reference folders

Asset workers must inspect the matching project reference folders before generation:

- report event images
- news event images
- decisions
- ideas
- focuses
- achievements
- flags

## Asset completion standard

No asset is complete without:

- source PNG
- processed PNG
- final DDS or TGA as required
- correct dimensions
- manifest entry
- proposed or final sprite name
- GFX handoff
- contact sheet for multi-asset groups
- source mode and prompt or source record
- static fallback and frame data for animation
