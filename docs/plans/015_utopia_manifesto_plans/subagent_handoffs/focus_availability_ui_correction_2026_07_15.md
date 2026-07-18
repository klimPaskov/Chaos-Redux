# Event 15 Focus Availability UI Correction

Date: 2026-07-15

Role: `chaosx_focus_tree_auditor` with narrow implementation authority

Scope: Event 15 focus source, Event 15 focus localisation, and this audit handoff

## Verdict

**PASS**

The reopened P1 focus UI finding is corrected. All 94 player-visible `available` blocks and all five `bypass` blocks now use a current `custom_override_tooltip` wrapper with one focus-specific public requirement key. The complete original predicate inside every block is preserved. All 15 `allow_branch` blocks are unchanged.

No focus-owned P0, P1, P2, or P3 finding remains after the correction.

## Reopened finding and correction

### FAV-UI-001, P1

Before this pass, all 94 `available` blocks and five `bypass` blocks exposed raw scripted-trigger names, internal flags, or variable comparisons through the focus UI.

The correction uses this structure:

```txt
available = {
	custom_override_tooltip = {
		tooltip = <focus_id>_available_tt
		<complete original predicate>
	}
}
```

The five constitutional-correction bypasses use the same structure with `<focus_id>_bypass_tt`. They remain readable because each bypass represents a public constitutional outcome. No bypass was hidden.

`custom_override_tooltip` is the current official trigger-documentation form. It replaces the rendered details of its contained trigger while preserving the trigger result. A hidden wrapper was not added around the predicate because the override wrapper already owns the complete public display.

## Files changed

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_availability_ui_correction_2026_07_15.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_tree_completion_post_ui_reaudit_2026_07_15.md`

No decision, League, country-package, event, idea, asset, scripted effect, scripted trigger, or AI-strategy file was edited.

## Source snapshot and hashes

| Artifact | Before correction SHA-256 | After correction SHA-256 |
| --- | --- | --- |
| Event 15 focus source | `71B11D239FF3D380CDF5E9BAB3E0D50825E8E604D22671228B7BDE97AC1F1514` | `3212C0C22215873835E569B0AA3ECD51D239EC12F650CA5D0C01372F300E6EC8` |
| Event 15 focus localisation | `A5DCA82C2FF5C9187B8421FD31E599F196F99BD4B5582B0EFC838D47D58B7766` | `2D56D34A3D4DF0D5E3B5A83727AAA5C7DF73CE47614748DA242E9F2D98E43E2E` |

Semantic aggregate hashes:

- All 99 unwrapped availability and bypass predicates before and after: `F55EDE976197B9C07B918654A61E455DD56730EC9922585D768B8F218EDD4D4A`
- All 15 `allow_branch` blocks before and after: `6E94E901E4E7A1F6E0A93F8B1773063C3BAF071A5D2E9DEF31ADC5D834A03572`

The semantic aggregates are built from ordered block kind, focus id, and Clausewitz tokens. The current source was also mechanically unwrapped and reconstructed. That reconstruction equals the complete pre-correction focus file exactly. This proves that prerequisites, mutual exclusions, coordinates, rewards, AI, costs, and every other non-wrapper line are unchanged.

## UI coverage

| Focus cluster | Readable availability keys |
| --- | ---: |
| Opening and first common store | 1 |
| Consent of Households | 9 |
| Common Table | 9 |
| Guardians of Measure | 9 |
| Closed Island | 8 |
| The Joke Understood | 8 |
| Callings and education | 3 |
| Common stores | 5 |
| District and city network | 2 |
| Island project variants and proof | 7 |
| Commonwealth Guard and external war conduct | 6 |
| League and external network | 5 |
| Necessary Ground and stewardship | 7 |
| Constitutional crisis and correction | 7 |
| Formation and post-formation | 8 |
| **Total** | **94** |

The five readable bypass keys are:

- `utopia_manifesto_household_gives_consent_bypass_tt`
- `utopia_manifesto_nothing_private_in_necessity_bypass_tt`
- `utopia_manifesto_country_measured_bypass_tt`
- `utopia_manifesto_one_island_one_measure_bypass_tt`
- `utopia_manifesto_read_island_as_a_mirror_bypass_tt`

There are 98 distinct affected focus ids because `utopia_manifesto_read_island_as_a_mirror` has both an availability predicate and a constitutional-correction bypass.

## Localisation approach

All 99 public strings are unique and specific to their focus. They describe the current world state through:

- the active public interpretation
- the Commonwealth Ledger and its public states
- manpower, support equipment, political authority, and Commonwealth Guard capacity
- island geography and completed project proof
- constitutional crisis or correction state
- Necessary Ground cases, stewardship, associates, League partners, and external network proof
- completed Commonwealth formation and post-formation obligations

The strings do not expose script flags, trigger ids, variable names, constants, tuning tiers, or implementation history. They contain no generic one-size requirement text. The hidden humanist route is still controlled only by the unchanged `allow_branch` predicates. Its availability text can render only after the branch itself has become visible.

## Validation results

| Check | Required | Result |
| --- | ---: | ---: |
| Focus blocks | 124 | 124 |
| Unique focus ids | 124 | 124 |
| `ai_will_do` blocks | 124 | 124 |
| Completion rewards | 124 | 124 |
| `available` blocks | 94 | 94 |
| Readable availability wrappers | 94 | 94 |
| `bypass` blocks | 5 | 5 |
| Readable bypass wrappers | 5 | 5 |
| `allow_branch` blocks | 15 | 15 |
| Changed `allow_branch` predicates | 0 | 0 |
| Changed availability or bypass predicates | 0 | 0 |
| Public requirement key references | 99 | 99 |
| Missing public requirement localisation | 0 | 0 |
| Duplicate public requirement keys | 0 | 0 |
| Duplicate public requirement values | 0 | 0 |
| Internal tokens in public requirement values | 0 | 0 |
| Missing focus titles | 0 | 0 |
| Missing focus descriptions | 0 | 0 |
| Localisation BOM | UTF-8 BOM | `EFBBBF` |
| Semicolons or em dashes in focus localisation | 0 | 0 |
| `:0` localisation keys | 0 | 0 |

Fresh graph facts after the correction:

- 124 focuses
- 174 prerequisite references
- one root, `utopia_manifesto_recover_the_manuscript`
- 124 of 124 focuses structurally reachable
- zero missing prerequisite references
- zero cycles
- zero missing mutual-exclusion references
- zero asymmetric mutual exclusions
- zero duplicate coordinates
- zero non-downward prerequisite edges
- coordinate span `x = -2..52`, `y = 0..16`

## Required references used

Skills:

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`

Offline Paradox wiki references:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National Focus Modding

Official documentation and vanilla precedents:

- `documentation/script_concept_documentation.md`
- `documentation/triggers_documentation.md`
- `documentation/loc_formatter_documentation.md`
- `documentation/loc_objects_documentation.md`
- current vanilla `custom_override_tooltip` focus availability examples
- current vanilla readable bypass and deliberately hidden bypass examples

The Event 15 accepted focus architecture, route matrix, completion matrix, AI matrix, localisation acceptance, and prior focus completion handoffs were reviewed before the correction.

## Validation not available

No `hoi4.focus_*` capability is exposed in this session, so a fresh MCP focus inspection or engine render could not be produced. This UI-only correction does not change coordinates, prerequisites, branch visibility, rewards, or connector geometry. The exact source reconstruction and fresh 124-node graph audit cover every gameplay and layout field touched by regression risk.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none
- Implementation omissions: none
- Fallbacks: none
- Focus-owned blockers: none
- Skipped validation: fresh MCP focus inspection and engine render, because no `hoi4.focus_*` capability is exposed

