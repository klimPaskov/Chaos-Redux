# Event 42 acceptance matrix

## Completion rule

Event 42 is complete only when every Required row passes or is explicitly removed from the accepted design with user approval. A source-only review cannot replace required HOI4 MCP or live owner-system evidence.

| ID | Surface | Acceptance requirement | Evidence | Priority |
| --- | --- | --- | --- | --- |
| E42-001 | Event identity | Entry root remains `chaosx.nr42.1` | Event inspect and source path | Required |
| E42-002 | Registration | Registered as Minor Repeatable | Event registry and Events tab | Required |
| E42-003 | Chaos level | Registered and displayed as level 1 | Event Details and workbook | Required |
| E42-004 | Default state | Added to reworked default-enabled allowlist only after implementation readiness | Startup state and Events tab | Required |
| E42-005 | Recipient validity | Uses event-owned trigger with shared ordinary-country classifiers | Trigger inspection | Required |
| E42-006 | Recipient fairness | Every valid country has equal raw weight | Probability scenario E42_RECIPIENT_01 | Required |
| E42-007 | Player eligibility | Player minors and majors remain eligible under identical rules | Probability evaluation | Required |
| E42-008 | Subject eligibility | Ordinary subjects remain eligible | Trigger test | Required |
| E42-009 | Special exclusion | Special Chaos and actual nonhuman countries are excluded | Probability scenario E42_RECIPIENT_02 | Required |
| E42-010 | Land requirement | Recipient owns and controls at least one valid landing state | Trigger test | Required |
| E42-011 | No-target state | Event shows `N/A` and queues nothing when no recipient exists | Event Details and manual test | Required |
| E42-012 | Repeat recipient | Completed prior history does not reduce selection weight | Probability scenario E42_RECIPIENT_03 | Required |
| E42-013 | Active-chain exclusion | Only unresolved recipient chains are temporarily excluded | Source and sequence test | Required |
| E42-014 | Manifest snapshot | Recipient, magnitude, families, quantities, tokens, reports, provenance, and evolved slots persist | Save and reload test | Required |
| E42-015 | One grant | Main delivery applies stockpile exactly once | Before and after stockpile evidence | Required |
| E42-016 | Report isolation | Delayed reports never grant equipment | Save and reload duplicate test | Required |
| E42-017 | Pacing isolation | Reports do not advance event pacing | Timer and history inspection | Required |
| E42-018 | History isolation | One Event 42 history row per delivery | Event Log evidence | Required |
| E42-019 | Magnitude range | Every package is Enormous, Colossal, or Impossible | Manifest evidence | Required |
| E42-020 | Magnitude ordering | Later evolutions increase large-package probability | Probability scenario E42_MAGNITUDE_02 | Required |
| E42-021 | No recipient scaling | Factories, manpower, army, stockpile, and major status never reduce quantity | Source and cross-country comparison | Required |
| E42-022 | Anchor family | Every manifest has one visible anchor family | Seeded manifest set | Required |
| E42-023 | Support families | Every manifest meets stage family-count band | Probability and simulation evidence | Required |
| E42-024 | Mismatch | Every valid manifest includes awkward equipment when a technical mismatch exists | Probability scenario E42_FAMILY_02 | Required |
| E42-025 | Technical reroll | Invalid token rerolls without shrinking family count or value | Pool-mask test | Required |
| E42-026 | Conventional registry | Every grantable token or variant has a documented safe consumer | Registry audit | Required |
| E42-027 | Designer tanks | No empty chassis is granted as a finished tank | DLC configuration tests | Required |
| E42-028 | Designer aircraft | No empty airframe is granted as a finished aircraft | DLC configuration tests | Required |
| E42-029 | DLC paths | Active and inactive designer DLC paths both work | Multi-configuration evidence | Required |
| E42-030 | Baseline technology | Baseline stays mostly recognizable with controlled advanced results | Probability scenario E42_TECH_01 | Required |
| E42-031 | Evolution I pool | Mechanized, amphibious, specialized armor, expanded aircraft, and advanced artillery work | Manifest coverage | Required |
| E42-032 | Evolution I technology | Advanced outcomes dominate peer outcomes without removing peer results | Probability scenario E42_TECH_02 | Required |
| E42-033 | Evolution II pool | Highest safe conventional equipment can appear regardless of recipient research | Manifest tests | Required |
| E42-034 | Evolution pacing | Each evolution uses normal paced activation and records once | Event and evolution inspect | Required |
| E42-035 | Evolved first firing | First delivery uses already-active evolution | Event-chain test | Required |
| E42-036 | Disabled evolutions | Disabled stage sets no recorded flag and unlocks no content | Enable-state tests | Required |
| E42-037 | No retroactive conversion | Existing equipment is unchanged when a stage activates | Stockpile comparison | Required |
| E42-038 | Nuclear chance | Chance follows audited Chaos bands and cap | Probability scenario E42_NUCLEAR_01 | Required |
| E42-039 | Nuclear quantity | Cache quantities follow magnitude bands and ignore recipient size | Probability scenario E42_NUCLEAR_02 | Required |
| E42-040 | Physical bombs | Positive stockpile is added through existing nuclear system | Stockpile evidence | Required |
| E42-041 | Launch proof | Recipient without research can conduct a valid ordinary strike | Engine and in-game evidence | Required |
| E42-042 | Production denial | Nuclear receipt grants no production, facility, project, research, missile, or thermonuclear access | Before and after capability audit | Required |
| E42-043 | Finite access | Event-only launch access closes when finite stockpile is gone | Depletion test | Required |
| E42-044 | Shared nuclear consequences | Use enters nuclear, fallout, Deaths, Air Cleanliness, Condemnation, and Chaos once | Cross-system evidence | Required |
| E42-045 | Special registry | Every Evolution III candidate has a complete audit row | Registry documentation | Required |
| E42-046 | No invented family | Every special token already exists in repository | Definition paths | Required |
| E42-047 | Physical grant proof | Every allowlisted token can be added and retained | Stockpile test | Required |
| E42-048 | Real consumer | Every allowlisted token has a fielding or payload consumer | Consumer path and test | Required |
| E42-049 | Minimum receipt | Compatibility opens only use needed for received stockpile | Capability comparison | Required |
| E42-050 | Production isolation | Compatibility receipt cannot manufacture special equipment | Production test | Required |
| E42-051 | Source fired state | Receipt does not alter owner event fired count, weight, or cap | Pre-state and post-state comparison | Required |
| E42-052 | Source evolutions | Receipt does not record or unlock owner evolutions | Evolution comparison | Required |
| E42-053 | Source countries | Receipt does not create or transform owner countries | Country-state comparison | Required |
| E42-054 | Source threat | Receipt does not set owner world-threat or terminal flags | Global-flag comparison | Required |
| E42-055 | Source projects | Receipt does not complete owner projects or facilities | Project and state comparison | Required |
| E42-056 | Source presentation | Receipt does not show owner super-events or focus routes | UI and flag comparison | Required |
| E42-057 | Source later firing | Owner event can later fire without duplicate templates or broken lifecycle | Integration test | Required |
| E42-058 | Special AI | Every allowlisted family has bounded AI use | Probability and AI test | Required |
| E42-059 | Special quantity | Quantity follows real battalion or payload semantics | Registry math and stockpile evidence | Required |
| E42-060 | Clone balance | Clone reserve manpower cannot create uncontrolled runaway gain | Longitudinal balance test | Required |
| E42-061 | Landing report count | Three to seven reports are queued | Probability scenario E42_REPORT_01 | Required |
| E42-062 | One-state chain | Seven reports can resolve safely in one state | Scenario E42_REPORT_02 | Required |
| E42-063 | State persistence | Saved report targets do not reroll after reload | Save and reload evidence | Required |
| E42-064 | State modifier merge | Repeated-state modifiers refresh or merge within cap | One-state test | Required |
| E42-065 | Accident bounds | Recovery accident has visible cause and small bounded loss | Seeded rare outcome test | Required |
| E42-066 | Provenance coherence | One firing uses one consistent hidden signature | Report-chain text audit | Required |
| E42-067 | AI equality | AI receives identical package distribution | Probability comparison | Required |
| E42-068 | No free enablers | AI gets no free manpower, fuel, bases, supply, doctrine, research, commanders, or divisions | Effect audit | Required |
| E42-069 | AI conventional use | AI can reorganize without deleting or wasting all stockpile | Time-progression test | Required |
| E42-070 | AI nuclear use | Shared nuclear AI sees finite weapons without production access | AI scenario test | Required |
| E42-071 | First skyfall Chaos | First successful manifestation adds +2 once | Chaos history evidence | Required |
| E42-072 | Nuclear proliferation Chaos | First genuinely new Event 42 nuclear actor adds guarded +10 or +5 | Chaos history evidence | Required |
| E42-073 | Special escape Chaos | First fieldable owner-event escape adds guarded +5 or +10 | Chaos history evidence | Required |
| E42-074 | Evolution Chaos | Evolution activation adds zero | Chaos comparison | Required |
| E42-075 | Repeat Chaos | Ordinary repeat delivery adds zero direct Event 42 Chaos | Chaos comparison | Required |
| E42-076 | Shared consequence isolation | Weapon use is not double-counted by Event 42 | Chaos, deaths, contamination, and condemnation logs | Required |
| E42-077 | Cluster assignment | Event 42 is a Low Various Anomalies member | Registry, UI, and workbook | Required |
| E42-078 | Cluster ID integrity | Uses authoritative assigned cluster ID | Workbook and source registry | Required |
| E42-079 | Independent eligibility | Event remains independently eligible at level 1 | Event and cluster tests | Required |
| E42-080 | One cluster delivery | Root or member transaction creates at most one package | Cluster event-chain test | Required |
| E42-081 | Cluster skip reason | No valid recipient creates a visible member skip reason | Cluster history | Required |
| E42-082 | Cluster pacing | Cluster counts as one pacing event | Timer evidence | Required |
| E42-083 | Actor mapping | Event Log actor is the recipient country | History row | Required |
| E42-084 | Detail wording | Event Details describes premise without hidden internals | Localisation audit | Required |
| E42-085 | Evolution details | Three stage-specific detail entries exist | Event Details and Evolutions tab | Required |
| E42-086 | Localisation completeness | No raw keys or placeholder instruction text | Localisation auditor | Required |
| E42-087 | Report assets | Six final report DDS files are wired to correct conditions | Asset manifest and UI review | Required |
| E42-088 | Achievement assets | Three complete icon triplets are wired | Achievement UI review | Required |
| E42-089 | Tiny Arsenal State | Eligibility, timing, division growth, capital, and major victory work | Achievement test | Required |
| E42-090 | Nuclear Lottery | Receipt and pre-production nuclear strike work | Achievement test | Required |
| E42-091 | Borrowed Nightmare | Exact special family is materially used before owner event fires | Owner callback test | Required |
| E42-092 | Achievement safeguards | Tag switch, debug, duplicate grant, annexation, and overwrite exploits fail | Negative tests | Required |
| E42-093 | Documentation | Permanent event, cluster, compatibility, achievement, and asset docs agree | Documentation audit | Required |
| E42-094 | Workbook | Authoritative XLSX contains final player-facing wording and metadata | Workbook review | Required |
| E42-095 | CSV export | Export script regenerates all three catalog snapshots | Export result | Required |
| E42-096 | Probability audit | All named weighted scenarios have evidence | Auditor handoff | Required |
| E42-097 | Probability compare | Final weighted patch is compared against baseline scenarios | `hoi4.probability_compare` evidence | Required |
| E42-098 | Improvement loop | Real planner pass is completed and dispositioned | Plan or closure handoff | Required |
| E42-099 | Completion audit | Event completion auditor reports no unresolved mapped requirement | Auditor report | Required |
| E42-100 | Blocker report | Every remaining blocker or simplification is explicit | Final completion report | Required |

## Required completion report sections

The final implementation report should include:

- files changed
- event registration and lifecycle
- manifest and quantity behavior
- recipient probability evidence
- evolution evidence
- nuclear launch and production-denial evidence
- special-equipment allowlist and excluded rows
- owner-event isolation evidence
- AI behavior
- Chaos accounting
- cluster behavior
- Event Log and Event Details
- achievements
- assets
- documentation and workbook
- meaningful task-specific validation
- planner and auditor dispositions
- simplifications, omissions, and blockers
