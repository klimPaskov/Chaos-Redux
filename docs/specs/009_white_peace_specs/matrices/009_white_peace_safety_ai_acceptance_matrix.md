# Event 009 — Safety, AI, and Acceptance Matrices

## Candidate veto matrix

| Condition | Base | Stage I | Stage II | Stage III | Rationale |
| --- | --- | --- | --- | --- | --- |
| No active war | Veto | Veto | Veto | Veto | Event is unavailable. |
| No safe pair | Veto | Veto | Veto | Veto | War count alone is not enough. |
| Minor vs minor, no protected flags | Allow | Allow | Allow | Allow | Core event identity. |
| Minor vs minor, same pair recently settled | Veto | Veto | Veto | Veto | Prevents loops. |
| Minor vs minor, one capital occupied by the other | Veto | Veto | Veto | Veto | Avoids robbing a clear victory. |
| Civil conflict pair | Veto | Veto | Veto | Veto | Too likely to break internal war logic. |
| Subject vs overlord | Veto | Veto | Veto | Veto | Too likely to break subject state. |
| Subject involved but not direct overlord war | Veto by default | Cautious only if proven safe | Cautious | Cautious | Requires explicit scope safety. |
| Either participant has capitulated | Veto | Veto | Veto | Veto | Invalid actor state. |
| Either participant marked protected | Veto | Veto | Veto | Veto | Scripted content override. |
| Either participant is a special crisis/threat actor | Veto | Veto | Veto | Veto | Preserve major mechanics. |
| Faction leader involved | Veto | Veto | Cautious | Cautious | Can alter too much war state. |
| Major country involved | Veto | Veto | Cautious allow | Cautious allow | Only evolved branches can touch majors. |
| War has several minor participants | Single pair | Multi-pair possible | Multi-pair possible | Broad possible | Higher stages can clean larger war clutter. |
| War has scripted owner flag | Veto | Veto | Veto | Veto | Explicit protection wins. |

## Branch behavior matrix

| Branch | Required stage | Required candidate | Max recommended effects | Skip/fallback behavior |
| --- | --- | --- | --- | --- |
| Single minor pair | Base | One Tier A minor pair | One pair, Chaos `-1` | Skip if no Tier A pair. |
| Multi minor, one war | I | One war with several Tier A pairs | Two to three pairs | Fall back to single minor if only one safe pair. |
| Multi minor, separate wars | I | Several Tier A pairs from separate wars | Two to three wars | Fall back to one war or single pair. |
| Major-country narrow settlement | II | One Tier B major relationship | One major relationship, Chaos `-2/-3` | Fall back to minor branches if major unsafe. |
| Broad separate-war settlement | III | Several Tier A/B safe pairs across separate wars | Three conflicts or capped pairs | Fall back to multi minor. |
| Broad one-war segment | III | One overcrowded war with many safe minor participants | Up to five pairs | Keep protected leaders untouched. |

## Dynamic weight acceptance matrix

| Scenario | Expected weight state | Pass condition |
| --- | --- | --- |
| No wars | unavailable | Event has no live weight. |
| One safe minor war | low | Dynamic cap below `1000`, usually around `250–400`. |
| Three safe minor wars | moderate | Cap rises but usually stays below `1000`. |
| Six or more active wars with safe pairs | high | Cap can compete with default events but still not exceed `1500`. |
| Higher evolution stage | lower than same environment at lower stage | Stage multiplier reduces cap. |
| After one firing | lower than before firing | Normal repeatable decay applied. |
| Protected wars only | unavailable | Active wars do not create weight without safe pairs. |
| Major wars only at base | unavailable or no major branch | No major settlement before stage II. |

## AI and player fairness matrix

| Actor situation | Expected handling |
| --- | --- |
| Player-controlled minor in a safe stale minor war | Can be selected; event is forced. |
| Player-controlled minor near victory | Excluded by capital/near-capitulation safety. |
| Player-controlled major before stage II | Excluded. |
| Player-controlled major at stage II/III | Possible only through rare major branch and safety gates. |
| AI minor in low-stakes stale war | Preferred candidate. |
| AI major in scripted conflict | Protected/excluded. |
| Subject country in overlord-linked war | Excluded unless implementation can prove safe. |
| Faction leader in alliance war | Excluded or cautious only at higher stage. |

## Exploit and abuse checks

| Risk | Prevention |
| --- | --- |
| Player declares small wars hoping Event 009 ends them | Low base weight, repeatable decay, no guarantee, recent-pair memory. |
| Player uses event to dodge defeat | capital occupation and near-capitulation vetoes. |
| Same pair cycles through random war and White Peace | pair memory; Random War should respect recent peace flags if integrated. |
| Protected story wars end unexpectedly | explicit protected-war triggers and flags. |
| Broad settlement ends too much | branch caps, protected actor vetoes, stage multiplier. |
| Major countries get too many escapes | stage II/III only, lower branch weights, longer recent-major memory. |
| Chaos drops too much | capped direct Chaos reduction. |
| Event becomes common at high chaos | weight driven by valid wars, not chaos alone; evolution multipliers reduce selection. |

## Required helper map

| Helper | Scope | Purpose | Output/side effect |
| --- | --- | --- | --- |
| `prepare_white_peace_runtime_context` | global/root | Build candidate counts and select primary branch context. | Saves event targets or temp candidates; sets availability variables. |
| `calculate_white_peace_dynamic_cap` | global/root | Calculate environment cap and effective cap. | Sets variables used by event picker and detail UI. |
| `can_country_be_white_peace_target` | country | Reusable country-level veto trigger. | yes/no. |
| `can_pair_receive_white_peace` | country with target | Pair-level veto trigger. | yes/no. |
| `score_white_peace_pair` | country with target | Candidate weighted score. | temp score variable. |
| `apply_white_peace_pair` | country with target | Execute pair-level white peace and memory. | peace effect, memory, relation, chaos contribution. |
| `mark_recent_white_peace_pair` | country with target | Prevent repeats. | timed flags or relationship memory. |
| `record_white_peace_evolution_if_needed` | global/root | Evolution unlock logging. | shared evolution log context. |
| `get_white_peace_skip_reason` | scripted loc/trigger | Compact UI status. | player-facing skip reason. |

## Files likely touched by implementation

The exact repo layout must be verified by the implementation agent, but the expected surfaces are:

- event script for Event `009`;
- event category registration in the random-event system;
- repeatable-event weight/cap helper logic;
- Peace cluster registration and member detail;
- scripted triggers for country and pair safety;
- scripted effects for runtime target selection, cap calculation, peace application, and memory;
- scripted localisation for event name, details, evolution details, cluster details, and skip reasons;
- English localisation for event popup and GUI text;
- event documentation under `docs/events/`;
- event catalog spreadsheet after final wording exists;
- asset manifest and report image / achievement icon handoff if assets are produced.

## Completion proof expected from implementation

The implementation report should include:

- dynamic cap examples from at least three scripted test states;
- proof that no-war and protected-war cases show unavailable;
- list of helpers created or reused;
- list of event targets and cleanup/memory flags;
- changed localisation keys;
- cluster ID `4` member registration evidence;
- evolution log entries created for stages I–III;
- event detail and catalog alignment notes;
- asset status;
- achievement tracking status;
- explicit simplification list if any branch, helper, asset, or achievement was deferred.
