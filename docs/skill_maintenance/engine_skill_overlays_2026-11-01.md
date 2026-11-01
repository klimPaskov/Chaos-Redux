# Engine skill overlays, 2026-11-01

Decision P10, option A. Nine Chaos Redux engine skills and the new `chaos-redux-investigate` are generated from the Agentic HOI4 Modding Kit at `55b9721` plus overlays in `.claude/skill-overlays/`. The baseline for "old" is the Chaos Redux commit `f8c3566590`.

## Method

- Each old Chaos Redux file was compared with the same-named kit file after the name mapping. The unit is a non-blank line with whitespace collapsed. Blank lines, rules, code fences and table separators are ignored.
- A root `SKILL.md` line is covered only by a root kit line. A kit reference file does not cover a root line.
- Any old line with no identical mapped kit line went to the overlay, grouped under `### In <original section>` in the old order. Code blocks and tables are kept whole.
- A line whose point the kit states in other words keeps the Chaos Redux wording and ends with `(Chaos Redux wording differs from the kit)`. A code block or table gets a label line before it. The kit version stays in the generated body, so both versions exist.
- Classes were assigned by reviewing every line, starting from a similarity ratio, so they are judgements:
  - **Wording differs:** the kit has a counterpart.
  - **Generic candidate:** states an engine fact without naming a Chaos Redux file, system or event, so it can be backported to the kit.
  - **Chaos Redux-specific:** everything else, including structure labels such as `**Rules that recur**` and the Contents entry for the Chaos Redux section.
  - **Headings:** the changed title and section headings, counted separately.

A sentence-level proof checked 3,690 old lines and 5,161 sentences of the nine existing skills: every sentence is in the generated skill, either in the kit body or in the overlay. A deliberately deleted sentence was reported as missing.

## Counts (overlay lines, before the corrections below)

| Skill | Chaos Redux-specific | Generic candidates | Wording differs | Headings | Total |
|---|---|---|---|---|---|
| ai-strategies | 11 | 0 | 8 | 2 | 21 |
| characters-leaders | 9 | 0 | 7 | 2 | 18 |
| diplomacy-war | 10 | 0 | 7 | 2 | 19 |
| equipment | 11 | 0 | 9 | 2 | 22 |
| ideas-modifiers | 11 | 8 | 13 | 2 | 34 |
| map-states | 12 | 0 | 10 | 2 | 24 |
| mtth | 3 | 0 | 1 | 2 | 6 |
| technology-doctrines | 17 | 4 | 6 | 2 | 29 |
| units-divisions | 19 | 0 | 6 | 2 | 27 |
| **Total** | **103** | **12** | **67** | **18** | **200** |

`map-states` also keeps `references/state-ledgers.md` (11,844 bytes) whole as a Chaos Redux-only reference file, because the kit has no counterpart. `investigate` has one authored line, a note that Chaos Redux has no `hoi4-live-playtest` and that live testing is only `chaos-redux-debug-playtest` when the user names it.

## Corrections: six old lines removed

These old Chaos Redux lines state something the installed 1.19.3 game contradicts. The kit text that replaced them, which stays in the generated skill, was checked against vanilla on 2026-10-31. The old lines were removed from the overlays, because keeping them would leave two contradictory rules in one skill.

| Skill | Old Chaos Redux line | Vanilla 1.19.3 shows |
|---|---|---|
| ai-strategies (`strategy-token-catalog.md`) | `force_concentration_factor` adds to `FORCE_CONCENTRATION_UNIT_RATIO_BASE` | That define does not exist. `common/defines/00_defines.lua` has `NAI.AIFC_UNIT_RATIO_BASE = 0.15` |
| map-states (`map-geometry.md`) | `weatherpositions.txt` sizes `small\|large` | `map/weatherpositions.txt` has 452 `big` and 136 `small` rows, no `large` |
| map-states | `add_building_construction` crashes on `supply_node` | Vanilla uses `add_building_construction = { type = supply_node ... }` 72 times. Only `rail_way` has no such use |
| map-states (common mistakes) | Item 7, the same claim for `supply_node` | As above |
| equipment | Equipment `type` values come from `_documentation.md` | They are the 38 entries of `script_enum_equipment_category` in `common/script_enums.txt` |
| equipment (`production-and-stockpile.md`) | Special project prototypes are covered by `special_projects_documentation.md` | Its keys appear in no vanilla file. The per-folder `documentation.md` files describe what vanilla uses |

## Wording differences by kind (67 lines before the corrections)

- 17 are the `GAME`, `WIKI` and "Root:" sentences with the concrete Steam path, where the kit says "the installed Hearts of Iron IV folder named in `CLAUDE.md`". These are redundant.
- 10 are wiki page references in an older style (ideas-modifiers 7, diplomacy-war 1, map-states 2). The kit names the snapshot's actual file names.
- 5 are tool-argument spellings, such as `mode = compare` against `mode: "compare"`.
- 6 were the corrections above.
- 6 are intro sentences ("Guidance for ... in Chaos Redux" against "Generic guidance ...").
- 23 are other restatements, mostly numbered "Rules that recur" items that rephrase a kit bullet and add a Chaos Redux clause.

## Generic candidates to backport to the kit (12)

- ideas-modifiers, Dynamic modifiers (8 lines):
  - A state-side `scope =` restricts the beneficiary.
  - Anchor values with `ROOT`.
  - Compute once in the source state.
  - Match holder, id and scope in every add, check and removal.
  - Source review does not prove that same-id bindings coexist.
  - The binding lifecycle.
  - The `my_flag_@THIS` receipt.
- technology-doctrines (4 lines):
  - The engine's global 70x70 connector line item.
  - Card size follows the vanilla rule and `force_use_small_tech_layout`.
  - The limits of `hoi4.tech_render view = folder`.
  - The special-project locked-card pattern.

## Maintainer decisions (2026-11-01)

The maintainer chose the recommended option for each question.

1. **Wording differences: keep the kit wording where it says the same thing.** 37 of the 59 remaining marked lines were deleted from the overlays. They are the path sentences, the old-style wiki references, the tool-argument spellings, the intro sentences and one line the kit states in full. A line counted as the same when it matched its kit counterpart after those style differences were normalised (similarity at least 0.93), or it was one of four intro or subset lines checked by hand. The 22 kept lines add a Chaos Redux clause to the kit rule, so they stay with their marker. `CLAUDE.md` names the game folder, so the path sentences lost nothing. 30 `### In` headings left empty were removed.
2. **Generic candidates: backport to the kit.** Done in kit pull request #37 (`3119ee9`). The eight dynamic-modifier lines became seven kit rules, and three of the four technology lines were already in the kit. The snapshot now pins `3119ee9`, and those 11 overlay lines are removed. The technology line that says not to set `force_use_small_tech_layout` stays, because it is a Chaos Redux layout choice; the kit now explains the consequence.
3. **Structure labels: keep.** The Contents entry and the labels such as `**Rules that recur**` stay. They organise the Chaos Redux section and cost a few bytes.
