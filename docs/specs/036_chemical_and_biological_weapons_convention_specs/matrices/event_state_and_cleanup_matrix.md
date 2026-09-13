# Event state and cleanup matrix

| State owner | Created by | Normal persistence | Invalidated by | Required cleanup |
| --- | --- | --- | --- | --- |
| Event 036 active flag | Canonical entry | Campaign | Never during ordinary play | None beyond event disable handling |
| Membership generation | Canonical entry or structural reconstruction | Until replaced | New valid generation | Clear stale country receipts and rebuild arrays |
| Country posture | Opening response or revision | Until next valid change | Annexation, invalid actor, new generation migration | Remove old modifier, AI strategy, and registry row atomically |
| Covert preparation | Covert decision | Until ended or exposed | Exposure, accession, invalid country | Hide decisions, preserve evidence, update posture memory |
| Convention coordinator | Opening setup | Until invalid | Annexation, invalid diplomacy, loss of all membership | Transfer to valid member or triggering ordinary country |
| Convention Standing | Membership-changing transaction | Until recalculated | Accession, withdrawal, expulsion, reconstruction | Replace qualitative state once |
| Active agenda | Scheduler | Until resolution or invalidation | Vote, sponsor loss, capability loss, convention pause | Clear target, deadline, support state, and visible decisions |
| Treaty response receipt | National response | Permanent treaty history | New treaty version | Preserve history, close old response action |
| Treaty ratification | Successful national response and global adoption | Until withdrawal, repeal, or replacement | Treaty repeal, incompatible posture, invalid country | Remove future benefits and obligations, preserve history |
| Evolution state | Evolution event | Campaign | Disabled evolution blocks activation only | Never clear an activated evolution |
| First-use policy | Opening or treaty response | Until valid public revision | Posture change, policy treaty, withdrawal | Replace policy and AI strategy atomically |
| Doctrine integration | Doctrine mission | Until loss or reversal | Capability loss, withdrawal, failed obligations | Downgrade or remove related modifier |
| Active project ID | Program selection | Until completion or cancellation | Completion, normal availability, charter repeal | Clear project decisions, progress, targets, and active participants |
| Project progress | Contributions | Until project ends | Completion, cancellation, charter repeal | Preserve history, reset active value |
| Participant receipt | First valid contribution | Project and lifetime history | Membership invalidity removes active access only | Preserve historical record and share |
| Contribution mission | Country decision | Until completion or cancellation | Project pause, cancellation, invalid country | Prevent progress and duplicate refunds |
| Project pause | Quorum loss | Until quorum returns or charter repeals | Resume, cancellation, repeal | Hide contributions and preserve progress during pause |
| Project completion history | Atomic completion | Campaign | Never | Prevent reselection and duplicate grant |
| Project cancellation history | Normal availability or repeal | Campaign | Never | Prevent stale progress restoration |
| Opposition Leader | Opposition strength resolution | Until invalid or displaced | Accession, annexation, loss of criteria | Transfer leadership and target arrays |
| One-time normalization flag | Opening source adjustment | Campaign | Never | Prevent repeat application |
| Chaos milestone flag | Concrete norm outcome | Campaign | Never | Prevent farming through repeal and reratification |
| Achievement snapshots | Relevant event | Campaign | Achievement framework rules | Preserve exact route and disqualifier proof |

## Invalid-country cleanup order

1. Remove country from active agenda target lists.
2. Cancel or fail country missions without applying duplicate results.
3. Remove active membership registry entry.
4. Preserve historical posture, treaty, action, and contribution records.
5. Recalculate standing.
6. Transfer coordinator or Opposition Leader when needed.
7. Recheck project quorum and recipient list.
8. Clear selected-target flags and event targets.
