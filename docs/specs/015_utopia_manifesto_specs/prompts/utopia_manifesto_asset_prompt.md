# Asset prompt for Event 015, `utopia_manifesto`

Use this prompt with `chaos-redux-event-assets` and the appropriate asset subagents.

Read the event spec files first:

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_1_core.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_2_focus_tree.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_decisions_mechanics.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_ai_assets_acceptance.md`

## General constraints

- Use generated art for fictional, symbolic, alternate-history, and UI assets.
- Do not generate real leader portraits.
- Do not replace the base flag of the accepting country during the early route.
- Use event-scoped final folders where engine rules allow them.
- Create source PNGs, processed PNGs, final DDS or TGA files, manifest entries, contact sheets where useful, and `gfx_handoff.md`.
- Use separate source art for focus, idea, decision, category, and achievement icons. Do not resize one icon type into another.
- Inspect the relevant reference folders before creating assets.
- Animated assets must follow `chaos-redux-frame-animation`, with real source frames, static fallbacks, frame sheets, preview GIFs for review only, and `.gfx` handoff notes.

## Reference folders to inspect

Use the matching reference folders under:

- `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/focuses`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`
- `.agents/skills/chaos-redux-event-assets/assets/flags`

## Final package folder

Working docs folder:

`docs/assets/015_utopia_manifesto/`

Final gameplay folders should be event-scoped where possible, for example:

- `gfx/event_pictures/015_utopia_manifesto/`
- `gfx/interface/ideas/015_utopia_manifesto/`
- `gfx/interface/goals/015_utopia_manifesto/`
- `gfx/interface/decisions/015_utopia_manifesto/`
- `gfx/interface/utopia_manifesto/`
- `gfx/super_events/015_utopia_manifesto/`

Flags are root-convention exceptions and should use normal HOI4 flag paths when cosmetic tags are implemented.

## Report and super-event images

| Asset id | Type | Size | Source mode | Direction | Suggested sprite |
| --- | --- | --- | --- | --- | --- |
| `report_event_utopia_manifesto_found` | report event image | 210x176 | generated documentary-style | a small country's reformers, soldiers, teachers, or townspeople reading an old manuscript. The manuscript is central, with an island or storehouse motif secondary. No readable generated text | `GFX_report_event_utopia_manifesto_found` |
| `super_event_utopia_new_utopia` | super-event image | 457x328 | generated | public civic square or harbor proclamation with common stores, banners, and a small country becoming a visible model. Period-authentic, 1936 to 1945 technology and clothing | `GFX_super_event_utopia_new_utopia` |
| `super_event_utopia_marked_bounds` | super-event image | 457x328 | generated | boundary surveyors, guarded settlers, boundary posts, old manuscript symbolism, uneasy neighbors. Period-authentic, no modern props | `GFX_super_event_utopia_marked_bounds` |
| `news_event_utopia_boundary_crisis` | news image | 397x153 | generated | black-and-white period news image of boundary markers and a tense frontier inspection | `GFX_news_event_utopia_boundary_crisis` |

Report images must receive the local report-card treatment. News images must be black and white.

## Idea and national spirit icons

Target size: 64x64.

Use generated icon art. Suggested ids:

- `idea_utopia_found_manifesto`
- `idea_utopia_unproven_common_stores`
- `idea_utopia_common_store_network`
- `idea_utopia_empty_stores`
- `idea_utopia_vocation_confusion`
- `idea_utopia_vocation_accord`
- `idea_utopia_compulsory_assignments`
- `idea_utopia_household_councils`
- `idea_utopia_storekeeper_commission`
- `idea_utopia_guild_congress`
- `idea_utopia_civic_wardens`
- `idea_utopia_marked_bounds_doctrine`
- `idea_utopia_utopian_league`
- `idea_utopia_foreign_laughter`
- `idea_utopia_feared_doctrine`

Visual motifs:

- open manuscript and island seal
- common warehouse shelves without readable labels
- balanced scales with bread, tools, or hands
- craft tools and apprentices
- household council benches
- surveyor compass and boundary stakes
- harbor and storehouse
- civic guards with shields or armbands

## Decision category and decision icons

Decision category icons:

- `decision_category_utopia_ledger`, 32x32 or existing category size pattern, open ledger plus island seal
- `decision_category_utopia_league`, if separate category used, clasped hands around storehouse or harbor

Decision icons, target 32x32:

- `decision_utopia_household_census`
- `decision_utopia_common_storehouse`
- `decision_utopia_storehouse_audit`
- `decision_utopia_open_stores`
- `decision_utopia_collect_petitions`
- `decision_utopia_fund_apprenticeships`
- `decision_utopia_urgent_service`
- `decision_utopia_rural_rotation`
- `decision_utopia_household_guard`
- `decision_utopia_guard_shore`
- `decision_utopia_just_cause_review`
- `decision_utopia_boundary_arbitration`
- `decision_utopia_mark_needed_district`
- `decision_utopia_settlement_charter`
- `decision_utopia_common_administration`
- `decision_utopia_local_store`
- `decision_utopia_local_households`
- `decision_utopia_boundary_wardens`
- `decision_utopia_storehouse_aid`
- `decision_utopia_send_magistrates`
- `decision_utopia_recognize_friend`
- `decision_utopia_league_aid_corridor`
- `decision_utopia_renunciation_vote`

## Focus icon families

Target size: 94x86.

The focus tree has 85 to 115 focuses. Create a coordinated focus icon pack with enough unique icons and motif variants to avoid repetition. Every final focus needs an icon assignment. Suggested families:

- opening manuscript and translation icons
- public reading and household census icons
- common stores and warehouses
- rural rotation and harvest
- useful arts, craft tools, iron, linen, glass
- vocation petitions and apprenticeships
- public lectures and scholars
- councils and plain laws
- storekeeper audits and ledgers
- guild congress and craft militias
- civic wardens and household guards
- harbor watch and fortified shore
- inland rail ring and supply hubs
- arbitration halls and boundary census
- settlement charters and common administration
- local households and integration
- Treasury Abroad and hired companies
- Friends and Neighbors diplomacy
- Utopian League and common reserves
- New Utopia proclamation
- Marked Bounds and boundary stakes
- reform exit and renunciation

## Scripted GUI assets

Create a Utopian Ledger GUI pack:

- background panel, suggested 700x500 or implementation-confirmed size
- header plate
- meter frames for Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion
- meter fill variants or neutral fills if implementation handles color in GUI
- target cards for state project, country relation, and League member
- warning panel
- normal, hover, selected, locked, disabled, and warning button states
- close and open buttons if existing UI assets cannot be reused
- small icons for each vocation track

## Animated assets

Use `chaos-redux-frame-animation`.

| Asset | Size | Frames | FPS | Loop | State logic | Static fallback |
| --- | --- | --- | --- | --- | --- | --- |
| `utopia_ledger_seal` | 64x64 or confirmed category seal size | 8 | 8 | yes | available important action | `GFX_utopia_ledger_seal` |
| `utopia_overreach_warning` | 64x64 | 8 | 8 | yes | Overreach high or Marked Bounds route | `GFX_utopia_overreach_warning` |
| `utopia_storehouse_fill` | 64x16 or confirmed meter strip | 6 to 8 | 8 | yes | active storehouse mission | `GFX_utopia_storehouse_fill` |
| `utopia_new_utopia_seal` | 96x96 or focus companion size | 10 | 8 | yes | proclamation available | `GFX_utopia_new_utopia_seal` |
| `utopia_marked_bounds_seal` | 96x96 | 10 | 8 | yes | Marked Bounds route active | `GFX_utopia_marked_bounds_seal` |

Do not create final animation by moving or recoloring one still. Each frame needs real source art.

## Flags and cosmetic identity

Early route keeps original country flag.

Generate fictional flag designs for these cosmetic identities if implemented:

- `UTO_new_utopia`
- `UTO_utopian_republic`
- `UTO_utopian_commonwealth`
- `UTO_utopian_league`
- `UTO_marked_bounds_state`

Each needs normal, medium, and small flag sizes. Use clean, readable symbols such as crescent island, open hand, storehouse, simple star, boundary ring, or ledger seal. Avoid readable text.

## Collective leader portraits

Generate fictional institutional portraits only if the implementation uses collective leaders:

- Council of Households
- Storekeeper Directorate
- Guild Congress
- Civic Wardens
- Boundary Surveyorate

Target leader portrait size: 156x210. These are collective or institutional portraits, not personal leaders. Do not assign random personal names to institutional portraits.

## Achievements

Achievement icons are listed in `prompts/utopia_manifesto_achievement_prompt.md`. Completed icons are 64x64. Grey and not-eligible variants should be produced if the achievement system requires them.

## Manifest and handoff

Write:

- `docs/assets/015_utopia_manifesto/manifest.md`
- `docs/assets/015_utopia_manifesto/gfx_handoff.md`
- contact sheets for icons and animated frames
- validation notes for size, transparency, DDS or TGA placement, and source mode

