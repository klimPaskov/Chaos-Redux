# Event 005 Caucasus graphics repair

Disposition: all eight named Caucasus graphics findings are implemented in source assets; post-change MCP acceptance remains blocked by the closed transport.
The full Event 005 graphics task is incomplete.
Acceptance basis: the user's graphics table, cross-cutting style rules and G6 authority to replace weak or repeated artwork.

Ten runtime DDS files change: four original per-focus subjects and matching legacy/focus framing corrections for three subjects.
Exact paths, original/output hashes, complete candidate lineage, source/prompt roles and validation are in `005_caucasus_evidence.json` beside this report and `docs/assets/005_soviet_collapse/gfx_fix_caucasus/installed_repairs.json`.
All outputs remain 94x86; sprite names and normal/shine registrations are unchanged.
No `.gfx`, focus logic, localisation, AI, country setup, spreadsheet or CSV changes are needed.

| Original review finding | Outcome |
| --- | --- |
| Direct Black Sea or Caspian Routes fringe (severity 2) | Earlier shared edge repair retained after current native inspection. |
| Direct Oil for Recognition crop (severity 2) | Complete retained composition fitted inward and centered; legacy and focus copies match. |
| Direct The Passes Vote crop (severity 3) | Retained composition fitted inward with clear canvas margins; both aliases match. |
| Defense Compact / Tbilisi Talks / Ridge duplicate (severity 2) | Defense shield retained only for its intended role; talks gets three city seals and a blank treaty, ridge gets a guarded mountain road and compact seal. |
| Mountain Artillery Schools / Border War Cabinet duplicate (severity 2) | Distinct period mountain gun and officers' caps/map-table compositions replace the riflemen reuse. |
| Focus Oil for Recognition crop/fringe (severity 3) | Matching framed copy fits its canvas; prior neutral-edge repair is preserved. |
| Focus Black Sea/Caspian Routes and listed family fringe tail (severity 3) | Current repaired family reviewed; no repeated erosion applied to already-clean artwork. |
| Focus Foreign Border Guarantees undersized badge (severity 3) | Existing globe/flags artwork enlarged proportionally and centered, including its legacy Foreign Missions alias. |

The four source-art subjects were generated with native ImageGen transparency, preserving every source/edit candidate and exact prompt.
The talks source's pseudo-writing was rejected and removed through a focused ImageGen edit; the final scroll is blank.
Source-edge checks distinguished isolated alpha-1 residue from real clipping; no visible source detail was cropped away, and no blanket alpha erosion or background-removal fallback was used.
Framing repairs preserve aspect ratio and retained paint rather than stretching the image.

The parent reviewed all native/new-art and framing comparisons on dark, light and checker backgrounds, then the full registered family after installation.
`005_caucasus_new_art_review.png` shows the four before/source/PNG/decoded-DDS comparisons; `005_caucasus_framing_review.png` shows the three retained subjects before and after reframing.
All ten installed DDSs independently passed exact PNG pixel equality and required legacy BGRA decoding.
The lowest mean alpha across surviving subject pixels is 223.955/255.
The new artillery and cabinet icons are no longer duplicate riflemen, and the two compact follow-ups no longer repeat the defense shield.

The initial parent `hoi4.focus_raster` returned a valid 40-focus tree and decoded PNG/crops; its artifact hashes and full baseline are retained.
The later worker inspect returned 40 focuses but overall validation false, with `SOURCE_UNEXPECTED_RIGHT_BRACE` at `game:common/national_focus/TSR_lingguang_incident_joint_branch.txt:469` in its source inventory.
The worker's narrow raster returned an empty result without artifacts.
The parent's matching post-change raster request for Oil for Recognition, The Passes Vote and Foreign Border Guarantees returned `Transport closed`.
No final MCP validation pass or equivalent engine evidence is claimed from the source/pixel checks.
The exact failed result is retained in `005_caucasus_evidence.json`.

Reference citations are the offline focus Icon section (lines 303–382, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`), offline Graphical asset modding spriteType (lines 30–99, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`), installed regular/shine declarations in `interface/goals.gfx` and `interface/goals_shine.gfx`, and the installed load_focus_tree documentation (lines 4771–4786, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`).
The artist's exact vanilla style references, source revisions, paths and scope are recorded in the manifest.

No visual-content simplification or substitute art is used for these eight findings.
The final MCP render and live consumer acceptance remain incomplete checks, and other Event 005 trees remain open.

## Exact orchestrator live checks

Use a paused 1936 USA graphics fixture at 1920x1080 and UI scale 1.
Run `effect load_focus_tree = { tree = soviet_collapse_caucasus_focus_tree }` and open the focus view.
Inspect Mountain Artillery Schools, The Border War Cabinet, Tbilisi/Baku/Yerevan Talks, and The Compact Holds the Ridge at normal and close zoom.
Expected: four visibly different, readable subjects with intact frames, a period gun instead of riflemen, caps/map for the cabinet, a blank treaty with three city seals, and a guarded ridge road.
Inspect Oil for Recognition and The Passes Vote for clear canvas margins, and Foreign Border Guarantees for a centered badge at a comparable scale to its neighbours.
Check locked, available/shine and hover-detail icon states for stable anchors, clean transparency and no missing sprite.
No gameplay reward or AI change is expected from this tranche.

Skills used: `chaos-redux-event-assets`, `chaos-redux-focus-trees`, `chaos-redux-subagents`, `imagegen` and `chaos-redux-shared-git-commit`.
The generic alpha-residue lesson was captured separately with `skill-creator`; no event-specific design was added to a skill.
