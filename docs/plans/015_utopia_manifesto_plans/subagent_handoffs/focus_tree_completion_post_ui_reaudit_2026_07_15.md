# Event 15 Focus Tree Completion Post-UI Reaudit

Date: 2026-07-15

Role: `chaosx_focus_tree_auditor`

Audit target: Event 15 focus completion after availability and bypass UI correction

## Verdict

**PASS**

Focus-owned finding inventory:

- P0: **0**
- P1: **0**
- P2: **0**
- P3: **0**

The previously passing 124-focus implementation reopened on one P1 UI defect because 94 availability blocks and five bypass blocks could show internal script predicates to the player. That defect is closed. Every affected block now has a unique, specific public requirement tooltip. All original predicates remain exact, all 15 hidden-route and crisis `allow_branch` blocks remain exact, and no graph, reward, route, AI, or layout regression was introduced.

This verdict is limited to the Event 15 focus-tree scope. It does not replace package-level decision, country, event-completion, documentation-curation, or parent-integration verdicts.

## Audited source snapshot

| Artifact | SHA-256 |
| --- | --- |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `3212C0C22215873835E569B0AA3ECD51D239EC12F650CA5D0C01372F300E6EC8` |
| `localisation/english/015_utopia_manifesto_focus_l_english.yml` | `2D56D34A3D4DF0D5E3B5A83727AAA5C7DF73CE47614748DA242E9F2D98E43E2E` |

Regression signatures:

- 99 unwrapped availability and bypass predicates: `F55EDE976197B9C07B918654A61E455DD56730EC9922585D768B8F218EDD4D4A`
- 15 `allow_branch` blocks: `6E94E901E4E7A1F6E0A93F8B1773063C3BAF071A5D2E9DEF31ADC5D834A03572`

The before and after signatures match for both sets. Replacing every new wrapper with its captured original block reconstructs the complete pre-correction focus source exactly.

## Fresh structural audit

- Focuses: **124**
- Unique ids: **124**
- Root: `utopia_manifesto_recover_the_manuscript`
- Prerequisite references: **174**
- Reachable from root: **124/124**
- Missing prerequisite ids: **0**
- Cycles: **0**
- Mutual-exclusion references: **68**
- Missing mutual-exclusion ids: **0**
- Asymmetric mutual exclusions: **0**
- Duplicate coordinates: **0**
- Non-downward prerequisite edges: **0**
- Coordinate span: `x = -2..52`, `y = 0..16`
- Completion rewards: **124/124**
- AI weights: **124/124**

## Post-UI acceptance matrix

| Requirement | Result | Evidence |
| --- | ---: | --- |
| Complete topology and structural reachability | PASS | 124 of 124 nodes reachable, 174 prerequisite references, one root, no missing ids, no cycles |
| Five public interpretation routes | PASS | Route predicates are unchanged and the five route openers retain their mutual exclusions and correction bypasses |
| Hidden humanist route remains hidden until valid | PASS | All 15 `allow_branch` blocks match the pre-correction aggregate and exact token comparison |
| Route correction and shared rejoin | PASS | Five public bypass outcomes remain exact and now have readable constitutional wording |
| Availability UI | PASS | 94 of 94 availability blocks use unique `custom_override_tooltip` keys |
| Bypass UI | PASS | 5 of 5 bypass blocks use unique readable `custom_override_tooltip` keys |
| No internal trigger or flag leakage | PASS | Zero internal script tokens occur in the 99 public tooltip values |
| Predicate semantics | PASS | All 99 unwrapped predicate streams match the captured pre-correction source |
| Rewards and idea lifecycle | PASS | Exact source reconstruction proves all completion rewards and helper calls are unchanged |
| Paid institutional and military growth | PASS | Affordability predicates are unchanged and now receive focus-specific public summaries |
| Island, archipelago, lease, and project proof | PASS | Five variant predicates and project proof remain exact, with geography-specific public requirements |
| League, Necessary Ground, and stewardship proof | PASS | External and stewardship predicates remain exact, with specific public-state wording |
| Formation and post-formation branch | PASS | Formation predicates and all post-formation availability checks remain exact |
| AI | PASS | 124 of 124 focuses retain one `ai_will_do` block and the complete source outside wrappers is unchanged |
| Focus titles and descriptions | PASS | 124 of 124 titles and 124 of 124 descriptions resolve |
| Requirement localisation | PASS | 99 references, 99 definitions, 99 unique values, no duplicates or empty entries |
| Localisation format | PASS | UTF-8 BOM `EFBBBF`, no `:0`, no semicolons, no em dashes |

## Route and shared-branch UI coverage

| Surface | Availability tooltips | Bypass tooltips | Result |
| --- | ---: | ---: | ---: |
| Consent of Households | 9 | 1 | PASS |
| Common Table | 9 | 1 | PASS |
| Guardians of Measure | 9 | 1 | PASS |
| Closed Island | 8 | 1 | PASS |
| The Joke Understood | 8 | 1 | PASS |
| Opening and shared branches | 51 | 0 | PASS |
| **Total** | **94** | **5** | **PASS** |

The Joke Understood public strings do not alter visibility. They are reachable only after the unchanged `allow_branch` logic exposes their focuses.

## Regression review against the prior focus completion verdict

The prior completion re-audit passed the focus scope after closing route refresh, constitutional correction access, lifecycle-slot, state-aware AI, island-variant, paid-growth, formation, and asset-reference defects.

This pass did not edit any line responsible for those systems. Exact reconstruction of the old focus source from the new wrapper blocks confirms that:

- the 124-focus graph is identical
- all prerequisites and mutual exclusions are identical
- all coordinates and layout controls are identical
- all 124 reward blocks are identical
- all 124 AI blocks are identical
- all 15 dynamic branch controls are identical
- all affordability, route, crisis, island, League, stewardship, and formation predicates are identical

The only gameplay-file delta is the public tooltip wrapper around each existing predicate.

## Localisation quality review

The 99 strings describe the live requirement represented by each focus. The review found:

- 99 distinct values
- no generic shared fallback sentence
- no script ids, flags, variables, constants, or tuning language
- route wording tied to the affected institution
- Ledger wording using public states such as Stable, Pressing, Surplus, Severe, Existential, One-Year Security, and Two-Year Security
- project wording tied to the chosen geography and completed material proof
- crisis wording tied to an active crisis, a recorded correction, or a settled charter
- external wording tied to eligible partners, a resolved case, stewardship, or a functioning network
- no implementation-history phrasing

## Render and MCP evidence boundary

No `hoi4.focus_*` capability is exposed in this session. A fresh engine-render artifact was therefore not produced.

This does not weaken the UI correction proof. The correction changes no focus position, prerequisite, branch-visibility condition, reward, or AI field. The current 124-node static audit remains clean, and the complete non-wrapper source is exact against the captured pre-correction source. The earlier render limitation remains recorded in the prior completion handoff.

## Completion statement

The Event 15 focus tree is completion-ready within focus scope at the audited hashes above. The reopened availability and bypass UI defect is fully corrected, and the fresh post-correction audit contains no P0 through P3 focus finding.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none
- Implementation omissions: none
- Fallbacks: none
- Focus-owned blockers: none
- Skipped validation: fresh MCP focus inspection and engine render, because no `hoi4.focus_*` capability is exposed

