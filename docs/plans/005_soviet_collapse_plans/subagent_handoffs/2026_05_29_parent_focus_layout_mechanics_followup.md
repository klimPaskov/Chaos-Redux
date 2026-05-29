# Parent Focus Layout And Mechanics Follow-Up

Date: 2026-05-29

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_ukraine_focus_l_english.yml`

## Gameplay Follow-Up

- Ukraine League focuses now unlock existing Soviet Collapse mechanics instead of only giving detached rewards.
- League training and arsenal focuses unlock the League unit deployment decisions.
- League charter, League of Equals, Kyiv command, border arbitration, and security-zone focuses now expose the arbitration, anti-client, external-border, arms-board, and security-zone decision paths through existing scripted flags and triggers.
- The Ukraine League branch now has prerequisite flow through arsenal/training, League foundation, diplomatic arbitration, front command, and security-zone mandates instead of ending in loose side focuses.

## Layout Follow-Up

Resolved the 21 exact focus-on-pathline hits reported by the focus layout subagent. Additional parent-owned coordinate cleanup covered Ukraine, Belarus, Baltic, Caucasus, Moldova, Kazakhstan, and dense custom splinter routes.

## Validation

Parser/topology audit:

- Focuses parsed: 1506
- Duplicate focus ids: 0
- Missing prerequisites: 0
- Duplicate coordinates per tree: 0
- Same-row `dx = 1` crowding pairs: 0
- Exact focus-on-pathline hits: 0
- Bad `continuous_focus_position` values under 1000: 0
- Duplicate `available` blocks in touched focus files: 0

Other checks:

- `git diff --check` passed for touched focus, localisation, and handoff files.
- Edited localisation files kept UTF-8 BOM.

## Remaining Risks

No remaining exact focus-on-pathline collisions were found by the mechanical audit. A full visual review in-game can still reveal subjective route-line density because the HOI4 focus UI routes lines differently from a straight-segment parser.
