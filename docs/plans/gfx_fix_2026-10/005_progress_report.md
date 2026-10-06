# Event 005 graphics repair progress, 2026-10-06

## Completion boundary

The complete 303-row Event 005 graphics task is incomplete.
This tranche installs 163 reviewed runtime textures: 162 focus/legacy textures and one fictional leader portrait.
The original review rows are counted separately from their expanded focus slots: 50 have reviewed source-asset repairs, one is blocked by a legacy sprite mapping, five are blocked by grounded painted finals, and 247 are not independently closed by this tranche.
`005_issue_dispositions.json` retains all 303 original findings and their individual dispositions.
Source-asset implementation does not mean final MCP or live-game acceptance.
Riga's additional size/subject finding is outside the original 303 rows and does not inflate that original-row completion count.
Previously committed shared edge repairs remain credited to `77bbd81e1`. their existence alone does not close the remaining subject, framing, duplicate or portrait findings.

## Installed packages and commits

| Package | Findings and result | Focused commit | Evidence |
| --- | --- | --- | --- |
| Kazakhstan | Twenty original findings reviewed, including prior accepted repairs. eight residual runtime textures repaired with intact flag ribbons, detached-fragment removal and crisp edges. | `bbe5309cb` | [Kazakhstan report](005_kaz_report.md) |
| Caucasus | Eight original findings addressed. four specific generated focus subjects plus six matching legacy/focus framing replacements. | `7bf1ebd4e` | [Caucasus report](005_caucasus_report.md) |
| BBH | All 47 focus textures are distinct. the birth identity is framed, commune seals are blank and the bespoke endgame design is retained. | `cd1b9e221` | [BBH report](005_bbh_report.md) |
| AOX | All 47 focus textures have original subject art. the birth anchor-star is reserved for Birth and Extreme Path uses physical harbor lamps. | `d860ea329` | [AOX report](005_aox_report.md) |
| Baltic | Forty focus and ten legacy textures installed. Two focus textures retained. All 42 active focuses are distinct and 94x86. Eight generated subjects include Riga, and four header normalizations preserve every pixel. | `f5f0c7c4c`, `fbd3887dd` | [Baltic report](005_baltic_report.md) |
| MFR portrait | One fictional arsenal chairman replaces the near-duplicate Construction Board composition. five attributed grounded source packages remain withheld from runtime. | `7dfaa3229` | [Portrait report](005_portraits_report.md) |

Caucasus independent audit and installed manifest reconciliation are in `ab5cd3baf`.
The follow-up independent audit covers all 47 BBH icons, all 47 AOX icons and the Baltic package in [005_focus_graphics_audit.md](005_focus_graphics_audit.md).
The generated sources, rejected candidates, exact prompts, PNGs, source/consumer crosswalks and conversion receipts are preserved under `docs/assets/005_soviet_collapse/gfx_fix_<family>/`.
The grounded portrait archives are under `docs/assets/portraits/005_soviet_collapse/gfx_fix_2026-10/`.
Only exact owned paths were committed through temporary-index, commit-tree and compare-and-swap publication. unrelated working-tree and index content was retained.

## Design decisions and acceptance basis

The user explicitly requested these subject, framing, transparency and identity repairs and granted G6 authority to improve weak visual design.
The specific accepted choices and rejected candidates are recorded in `docs/plans/005_soviet_collapse_plans/agent_decisions_2026-10-05.md` and the per-family reports.
All generated icon subjects were tied to the current focus name, description and completion reward.
No gameplay reward, route, AI weight, event, decision or GUI script changed.
The sole player-text change is `Riga?s` to `Riga's` in the Riga focus description, committed as `b313c2a8d` with an isolated one-character hunk and preserved shared-file/index bytes.
Parent review rejected BBH circled-A tokens, medieval free-city imagery, AOX neon arcs, a UI-selector endgame, incorrect Baltic flag candidates, clipped frames and pseudo-writing in the Caucasus talks.
The accepted replacements use period objects, blank documents and seals, correct local flags where called for and true native transparency.
No visual-content fallback or generic substitute was used for the installed packages.
The retained BBH endgame and proportional framing corrections preserve approved existing artwork.
The withheld grounded crops are archival inputs with unresolved framing or identity limits, not accepted final portraits.

## Validation evidence and limits

Every installed texture was guarded against its captured original hash before promotion and checked against its approved PNG after promotion.
The national-focus outputs use exact 94x86 uncompressed BGRA DDS consumers. all installed DDS pixels match their approved processed PNGs.
MFR uses the existing 156x210 portrait consumer and opaque alpha.
The parent reviewed native checker/dark sheets and source-resolution revisions, and an independent read-only auditor reviewed source-to-focus mappings and DDS proofs.
Kazakhstan has matching successful before/after MCP focus rasters.
AOX, BBH, Baltic and Caucasus retain successful baseline inspection/raster evidence, but their final raster calls returned `Transport closed`. the failed results are retained and no final engine-render acceptance is claimed.
A later Caucasus inspection parsed forty nodes but failed overall on `game:common/national_focus/TSR_lingguang_incident_joint_branch.txt:469`, `SOURCE_UNEXPECTED_RIGHT_BRACE`. that current diagnostic remains unresolved outside the owned artwork surface.
Focus connector-detour and generic continuous-focus localisation warnings remain open where listed in the reports.
No Hearts of Iron IV process or desktop window was launched.

## Simplifications, omissions and blockers

The two legacy Baltic Warroom normal/shine aliases still point to Home Guard in `interface/005_soviet_collapse.gfx`.
Their proper separate texture is installed, and the active focus-prefixed Warroom alias is correct.
The user expressly limits `.gfx` changes to size/frame-count changes, so the narrow two-path exception remains awaiting a reply to the asynchronous question. no exception is inferred from silence.
The concrete two-line proposal is retained in `005_baltic_legacy_alias_proposed.patch`, with no shared-registry mutation.
AAX, TAN, UKR, AZR and KYR require source review and user-supplied HOI4-style painted finals. their runtime portraits remain unchanged.
Their current visible defects are not closed.
Final MCP rendering for the packages named above is blocked by the closed transport.

The fourteen untouched major placeholder-tree packages are ARD, ADX, DHC, GAC, KHC, FEV, FTH, IMX, IUL, NLC, SDZ, UDC, SZA and UWD.
Further unresolved focus findings include AEX, ANX, CFR, MFR, DSC, ICD, IKX, ILX, IJX, INX, NRF, PRA, SOG, TNC, the smaller IMX route, Ukraine, Belarus, Moldova, Central Asia, internal republics and the generic/breakaway families.
Other original findings include faction logos, idea icons, decision icons and category pictures, including reconstruction/arsenal/factory categories.
The row-level disposition file is the authoritative remaining list. these groups are a navigation aid rather than a reduced scope.

## Exact orchestrator live checks

Use separate paused 1936 USA graphics fixtures at 1920x1080 and UI scale 1 for each tree.
Set Chaos Tier 3 before inspecting the hidden high-chaos branches, using `effect set_global_flag = { flag = chaos_tier value = 3 }` in the graphics fixture.
Run each command, open the national-focus view, inspect all branches at normal and close zoom, and hover available, unavailable and shine states.

| Command | Expected visible result |
| --- | --- |
| `effect load_focus_tree = { tree = BBH_soviet_collapse_focus_tree }` | Forty-seven distinct subjects. broad framed Birth, blank League seals and anti-protectorate wax disk, period free-city gate and retained bespoke endgame. |
| `effect load_focus_tree = { tree = AOX_soviet_collapse_focus_tree }` | Forty-seven distinct subjects. anchor-star only on Birth, physical red harbor lamps on Extreme Path and fortified harbor endgame, with no neon arcs or UI selector. |
| `effect load_focus_tree = { tree = soviet_collapse_baltic_focus_tree }` | Consistent 42-icon framing. shields/rifles for Defense Compact, map-table officers for War Room, architectural seals for the rotating capitals, coastal battery/forest for the Estonian guard and accurate Baltic flag bands. |
| `effect load_focus_tree = { tree = soviet_collapse_caucasus_focus_tree }` | A period mountain gun, cabinet caps/map, three city seals/blank treaty and guarded ridge road are distinct. Oil for Recognition, The Passes Vote and Foreign Border Guarantees have intact margins and comparable framing. |
| `effect load_focus_tree = { tree = soviet_collapse_kazakhstan_focus_tree }` | League Cavalry School ribbons have no colored rim or detached dash. southern flags have no floating fragments. engineers and Turkish radio subjects retain crisp outlines. |

Expect stable anchors, intact subjects and clean transparency on the actual game background in every tested focus state.
For Baltic country branches, use `tag EST`, run the Baltic load-tree command and inspect the Estonian pair, then repeat with `tag LAT` for Riga Corridor Switchyards and Latvian Port Guard Boards, and `tag LIT` for the Lithuanian pair.
Those six focuses use tag-specific `allow_branch` blocks and cannot all be reviewed in the USA fixture.
For all Caucasus country branches, use a fixture where GEO, AZR and ARM exist, select each tag and run the Caucasus load-tree command.
In a separate plain 1936 graphics fixture, `effect SOV = { release = GEO release = AZR release = ARM }` supplies those three countries before `tag GEO`, `tag AZR` or `tag ARM`.
The target eight Caucasus findings also include common branches, which are inspected in the same focus views.
For the portrait fixture, run `effect set_politics = { ruling_party = neutrality }`, then `effect create_country_leader = { name = "The Arsenal Board" picture = GFX_portrait_MFR_arsenal_board ideology = despotism traits = { } }`.
Inspect politics and diplomacy at normal scale. expect one painted industrial chairman, a brass caliper, closed book and pale arsenal office, without clipped neighboring figures or baked lettering.
In an Event 005 session with MFR and CFR present, compare their portraits and expect different faces and governing-body compositions.
The five grounded portraits and blocked legacy Baltic alias are expected to retain their explicitly reported defects. those checks cannot be counted as completed fixes.

## Skills

Used: `chaos-redux-event-assets`, `chaos-redux-focus-trees`, `chaos-redux-events` for ownership, `chaos-redux-subagents`, official `imagegen`, `chaos-redux-shared-git-commit` and official `skill-creator`.
Updated the generic event-assets alpha-validation rule in `36cbc48ae`: faint alpha residue at a canvas edge is distinguished from visible clipping, and visibly clipped art requires restoration rather than merely shrinking the damaged image.
No event-specific design was placed in a skill.
