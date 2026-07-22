# Event 15 focus-tree visual and adjacent audit — 2026-07-22

## Scope and evidence

This is a read-only focus-tree audit of `utopia_manifesto_tree` in
`common/national_focus/015_utopia_manifesto_focus_tree.txt`. No gameplay,
localisation, GFX, or AI source was changed by this audit.

The source SHA-256 is `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05`.
The HOI4 focus-tool layout hash is
`8cc2570d47404d970db419482fdf84f00c62160f39e8e9f314796b5db8a96cac`.

MCP evidence:

- `hoi4.focus_inspect`: `FOCUS_INSPECTED`, 124 focuses, 174 prerequisite connectors,
  source revision `3b1f4b5152a931e59b148f19599f14b392698c53f4f6f89dcfa90cf76291dd07`.
- `hoi4.focus_render`: HTML/SVG/JSON artifacts with the same layout hash.
- `hoi4.focus_raster`: PNG review artifact, SHA-256
  `9875a6aa24c216068a1b4e1e5e91907cfd65fb821f1c080b98305b813d2d14e1`; SVG SHA-256
  `085fccd18508b71bebd1f7e8e394c4593cd87b704e375e97a435a83480a2a1f5`.

Artifact links (workspace `mod_chaos_redux_ea3b2d67c2c0`):

- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9875a6aa24c216068a1b4e1e5e91907cfd65fb821f1c080b98305b813d2d14e1/05d16b50a9a2310b3994f6b7b01e4444b650bd8b5585ecfb2aae6ff37da023b9/utopia_manifesto_tree.focus.png`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/085fccd18508b71bebd1f7e8e394c4593cd87b704e375e97a435a83480a2a1f5/348c171f7dcd970c3b50b62f5ef77869295b65741d1c6df9cec7a17f19476487/utopia_manifesto_tree.focus.svg`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92fd2ca2324f598083ecc14ccf886f4d5bcdb950d2bc7bb05dafc1c9c9d3bd1f/b397a0bf0f1412933a7b1594f08ff4b31f858599a827803ead6fff9e07ef9b66/utopia_manifesto_tree.focus.html`
- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ad9263c4b42a4752e1a9d5f484d23515f974fec93af44965dc68837afffa1cd/110aea5dd3df502d7e37e849a6be2f761039e4eb74a7cd6cc21f47437126a1b5/focus-inspect.3b1f4b5152a931e5.json`

## Route coverage

| Spec surface | Source section / representative IDs | Count | Audit result |
| --- | --- | ---: | --- |
| Opening survey and founding institutions | `recover_the_manuscript` through `the_country_as_a_question` (lines 46–255) | 8 | Present; single centered trunk. |
| Consent of Households | `household_gives_consent` through `commonwealth_by_consent` (lines 257–572) | 10 | Present; route lock and consent-aware AI are wired. |
| Common Table | `nothing_private_in_necessity` through `union_of_tables` (lines 573–906) | 10 | Present; council autonomy/central-plan fork is reciprocal. |
| Guardians of Measure | `country_measured` through `perfect_measure` (lines 907–1256) | 10 | Present; useful-freedom/exact-obedience fork is reciprocal. |
| Closed Island | `one_island_one_measure` through `perfect_island` (lines 1257–1569) | 9 | Present; service, penal works, colonies, channel, and island capstone. |
| Hidden humanist/joke route | `read_island_as_a_mirror` through `good_place_that_admits_its_limits` (lines 1570–1872) | 8 | Present and gated by `allow_branch`; reconnects by route correction. |
| Callings and education | `every_hand_knows_the_soil` through `a_nation_of_many_skills` (lines 1873–2064) | 7 | Present; optional support branch. |
| Common stores/productive abundance | `the_capital_store` through `surplus_beyond_the_shore` (lines 2065–2273) | 7 | Present; reserve and surplus ladder. |
| Garden settlements/island project | `homes_near_work` through `the_island_made_real` (lines 2274–2650) | 11 | Present; five mutually exclusive variants, including leased island. |
| Defense without waste | `the_citizen_watch` through `commonwealth_defense_compact` (lines 2651–2929) | 8 | Present; no-glory/necessary-victory fork and compact. |
| Foreign Commonwealth | `show_the_stores` through `the_regional_commonwealth` (lines 2930–3135) | 7 | Present; external network and reserve/defense convergence. |
| Necessary Ground | `survey_what_we_lack` through `a_commonwealth_of_places` (lines 3136–3358) | 8 | Present; need fork and associate proof. |
| Stewardship/status | `stewardship_obligations` through `status_by_consent` (lines 3359–3524) | 6 | Present; charter/status proof branch. |
| Constitutional crisis/correction | `the_founding_crisis` through `a_settled_interim_charter` (lines 3525–3834) | 7 | Present; hidden until crisis, five reciprocal correction choices, visibility refresh. |
| Formation/post-formation | `proof_of_the_commonwealth` through `plenty_in_an_age_of_chaos` (lines 3835–4119) | 8 | Present; domestic/external proof gate and post-formation play. |

Total coverage is 124/124 focuses. All parent references resolve. No duplicate
coordinates were found, and every prerequisite parent is above its child.
The nine multi-focus prerequisite groups use same-block OR semantics for
intentional route alternatives and separate blocks for required proof layers
(for example `proof_of_the_commonwealth`, `the_first_associate`, and
`commonwealth_defense_compact`); no accidental OR/AND inversion was found.

Static graph leaves are `a_nation_of_many_skills`, `surplus_beyond_the_shore`,
`end_the_auxiliary_contract`, `commonwealth_defense_compact`,
`the_regional_commonwealth`, `a_commonwealth_of_places`, `status_by_consent`,
`a_settled_interim_charter`, `the_regional_proclamation`, and
`plenty_in_an_age_of_chaos`. Most are intentional optional support or terminal
nodes: formation is state-gated by `utopia_manifesto_can_form_current_route`
rather than by a direct parent edge. The two lower support endpoints
(`the_regional_commonwealth`/`a_commonwealth_of_places`) and the crisis bridge
(`a_settled_interim_charter`) deserve a runtime reachability check because the
architecture guide describes foreign/commonwealth, stewardship, associates,
and crisis lanes as converging before final proof, while the static graph uses
flags and decisions for that convergence.

Mutual-exclusion audit: 23 focuses define 68 directed exclusion edges; every
edge has a reciprocal declaration. This includes the five political openers,
five island variants, route-correction choices, and the smaller two-way forks.

## Visual/layout findings

The authored layout is structurally valid but not engine-clean:

| Metric | Current value | Finding |
| --- | ---: | --- |
| Bounds | x=-2..52, y=0..16 | 55 columns × 17 rows; broad horizontal scrolling. |
| Render size | 9808 × 2092 | Readable only with substantial pan/zoom at default focus UI scale. |
| Connectors | 174 | All are resolved. |
| Crossings | 54 | 14 crossing diagnostics are blocking in the MCP validation. |
| Through-node intersections | 17 | Shared-lane convergence lines pass through unrelated nodes. |
| Long connectors | 21 | Two exposed consent-to-callings links exceed the tool threshold. |
| Same-row spacing | minimum 2 (required 2) | No spacing collision. |
| Duplicate coordinates | 0 | No clickable node overlap from coordinates. |

The exposed high-priority connector hotspots are:

1. Opening geometry around `the_first_common_store`, `agriculture_for_all`,
   `convene_the_interpretive_congress`, `an_interim_charter`,
   `homes_near_work`, `every_hand_knows_the_soil`, and `survey_what_we_lack`
   (source lines 181–254). The tool reports 7 crossing combinations here.
2. `household_gives_consent` → `free_callings` (12 columns) and
   `household_gives_consent` → `municipal_charters` (10 columns), source lines
   305–359.
3. Foreign Commonwealth versus Consent lower-lane links:
   `a_league_of_small_places` → `common_reserve_council`/
   `mutual_defense_without_mastery` crossing
   `paid_public_lectures` → `independent_need_review`, source lines 417–477.
4. The lower convergence line `a_ring_of_social_cities` →
   `proof_of_the_commonwealth` crosses or passes through
   `independent_need_review`, `constitution_of_provision`, and
   `voluntary_commonwealth_league`, source lines 479–534.

These are not safe one-node corrections: the affected endpoints are all
authored fixed coordinates and the connectors belong to shared support lanes.
A future cleanup should be a reviewed multi-node lane pass (with a before/after
MCP inspect and render), not an isolated coordinate tweak.

## Icon coverage

| Surface | Result |
| --- | ---: |
| Focuses with an icon | 124/124 |
| Unique focus icon IDs | 74 |
| Base `.gfx` sprite definitions | 74/74 |
| `_shine` sprite definitions | 74/74 |
| Referenced DDS textures | 74/74 |
| DDS dimensions/mode | 94×86 RGBA for all 74 |

`interface/015_utopia_manifesto.gfx` contains unique sprite names and all base
and shine pairs. Reuse is thematic rather than accidental: the most-used
families are assemblies/auditors/settlement-charter/ring-councils (four each),
then grain/guild-charter/friends/councils/common-administration/measures/
guarded-settlement/registers/island-compact/crisis-rations (three each).
No missing or dangling icon reference was found.

## Localisation and reward mismatch audit

- All 124 focus title keys and all 124 `_desc` keys resolve to non-empty English
  strings. No duplicate Event 15 localisation keys were found across the nine
  Event 15-owned localisation files.
- All 99 focus-local `tooltip =` references resolve.
- Focus names describe their adjacent mechanics (for example the five island
  variant names, the two defense fork names, and the formation/post-formation
  names); no name/reward contradiction was found.
- Every focus has a `completion_reward`. Repeated signatures are expected
  payment/ledger helper patterns; route-specific flags, decision unlocks,
  variant commits, growth helpers, and formation flags distinguish the branches.

## AI behavior

All 124 focuses define `ai_will_do`:

| Base factor | Focus count |
| --- | ---: |
| `@utopia_ai_high` | 74 |
| `@utopia_ai_normal` | 30 |
| `@utopia_ai_urgent` | 10 |
| `@utopia_ai_low` | 5 |
| `@utopia_ai_hidden` | 2 |
| `@utopia_ai_strong` / `assertive` / `elevated` | 1 each |

There are 22 modifier blocks. The five openers and five crisis correction
choices use the route-preference/avoidance scripted triggers in
`common/scripted_triggers/015_utopia_manifesto_triggers.txt`; the AI strategy
package defines 12 state-aware plans in
`common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`. No missing AI block,
route trigger, or syntax-level AI gap was found. A remaining runtime risk is
that most optional support focuses intentionally use static base factors; route
distribution should be checked in representative AI scenarios after any layout
pass.

## Missing, simplified, or blocked content

No required route, focus, icon, localisation key, exclusion edge, or AI block is
missing in the current source. No gameplay simplification was introduced by
this audit.

The current MCP validation is nevertheless **not clean** because of the 14
blocking crossing diagnostics listed above. The audit did not patch them because
remediation spans several shared lanes and would be a layout redesign rather
than a narrow prerequisite/icon/AI fix. Runtime click bounds, hover overflow,
and hidden-branch visibility after each state-changing effect were not executed
in a live game; `utopia_manifesto_refresh_focus_visibility` does call
`mark_focus_tree_layout_dirty` in `common/scripted_effects/015_utopia_manifesto_effects.txt:1011–1019`,
which covers the dynamic `allow_branch` routes.

## Recommended priority

1. Treat the MCP crossing failure and 9808-pixel width as the next focus-tree
   task: perform a deliberate multi-node shared-lane layout pass and re-run
   inspect/render/raster. Preserve route IDs, prerequisites, exclusions, and
   source-bound planning metadata.
2. After geometry is accepted, run runtime scenarios for each of the five
   opener routes, the hidden crisis branch, and all five island variants to
   confirm visibility and clickable bounds.
3. Consider additional icon differentiation only if the visual review finds a
   thematic family ambiguous; current icon reuse is internally coherent.

### Changed files

Only this audit handoff was added. No gameplay or asset files were changed.
