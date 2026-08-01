# Event 12 Africa asset and animation matrix notes

## Purpose

`012_africa_asset_animation_matrix.csv` records 239 visual work items with explicit release-candidate dispositions. It covers presentation images, the Charter interface, animation, idea icons, decision icons, focus icon families, constitutional identities, portrait frames, Tier A restored polities, strange units, and continent-unifier packages.

The matrix is a planning ledger. Actual asset production must split work by source mode and asset type. It does not authorise one worker to generate, source, process, and wire everything in one pass.

## Coverage summary

| Family | Rows |
| --- | ---: |
| Restored polity Tier A packages | 52 |
| Focus icon families | 42 |
| Decision icons | 30 |
| Idea and national spirit icons | 24 |
| Charter GUI static assets | 12 |
| Event report images | 10 |
| Animated GUI sprites | 10 |
| Strange unit identity packages | 10 |
| Host constitutional identities | 7 |
| Other continent and terminal identity packages | 7 |
| News images | 6 |
| Portrait frames | 5 |
| Super-event images | 4 |
| Host-country overlay and proof-state kits | 8 |
| Constitutional route dilemma state families | 7 |
| Post-unification constitutional review family | 1 |
| Priority-member promotion and distinct-mechanic families | 2 |
| Route commitment values and capstone seals | 2 |

## Revision additions

The 20 added rows communicate the expanded country and route design. They do not multiply assets in proportion to prose.

- Six reusable host-problem motif kits cover treaty, invasion, federal, concession, land, and corridor or island openings.
- One proof-state kit covers active, failed, recovery, and completed host mandates.
- One post-unification host legacy card preserves the origin country without placing its flag over the whole continental interface.
- Seven constitutional dilemma families show deadlock, election, succession, planning balance, commander loyalty, confederal ratification, and Covenant obligation states.
- One postwar constitutional review family communicates demobilisation and institutional settlement.
- Two priority-member families handle promotion status and the sixteen distinct package mechanics.
- Two route families cover the four cross-route commitment values and the seven capstone seals.

Every added animation candidate is state-driven and requires a static fallback. Grounded content stays mostly static. Motion is reserved for active proof progress, crisis warnings, the Covenant, and completed-state activation.

## Source routing

Use the sourced visual asset worker for:

- real historical leaders
- historical flags
- historically attested symbols
- archival photographs that must depict a real person, place, object, or event
- source documentation and licensing

Use the generated event-art worker for:

- fictional and alternate-history report, news, and super-event scenes
- fictional leaders and councils
- fictional flags and faction emblems
- high-chaos actors
- UI panel art and portrait frames

Use the icon artist for:

- focus icons
- idea and national spirit icons
- decision and decision-category icons
- achievement icons
- technology and strange-unit icons
- animated small sprites when requested

Historical polity packages can be mixed. Source the attested material, then generate only the alternate-history variants that require invention. The manifest must identify which part came from which mode.

## Tier A polity standard

Every Tier A row is a package, not a promise that one flag completes the country. A complete Tier A visual package may require:

- normal, medium, and small flags
- ideology or route variants where the public identity changes
- leader, council, advisor, commander, and high-command portraits
- a faction or court emblem
- focus, idea, decision, and achievement motifs
- report or news imagery for major reveal moments
- sourced-symbol notes
- generated-variant notes
- gender presentation and matching name-pool instructions for fictional one-person portraits

Tier B and Tier C polities remain in the polity catalog. Asset work for them should be promoted only when implementation selects them for a real tag, persistent subject, or visible restoration.

## Icon separation

Focus, idea, decision, achievement, and technology icons are different assets even when they share a subject. Do not resize a focus icon into a decision or spirit icon.

Each final focus must receive a distinct 94x86 icon assignment. The 42 focus rows are coordinated families, not a license to reuse one file for an entire branch.

## Animation standard

Every animated item, including the 10 original animation rows and any approved state-driven addition, requires:

- a written brief
- a frame plan
- one approved static fallback
- separately generated, sourced, or provided source frames
- processed frames at one exact size and anchor
- a horizontal frame-sheet PNG
- a frame-sheet DDS
- a preview GIF for review only
- a contact sheet when practical
- manifest and GFX handoff entries
- a verified state trigger and target GUI surface

No final animation may be produced by shifting, scaling, rotating, warping, blurring, recolouring, changing opacity, or adding a local glow to one still image.

## Flag and name discipline

Country names remain direct public country names. Asset filenames and sprite identifiers use stable technical slugs. The user-mandated obscene ruler strings never enter filenames, paths, sprite names, tags, or script identifiers.

Historical flags must be sourced or designed from documented motifs with uncertainty recorded. Fictional route flags may be generated. Ideology variants need distinct intentional designs rather than palette swaps.

## Super-event boundary

The matrix reserves images for four super-event roles. Image work can begin from the direction in the package, but title, button, quote, and audio remain blocked until the dedicated research workflow verifies them. A completed super-event needs the final image, audio, text, slot, settings-aware playback, docs, and catalog alignment.

## Validation handoff

Before implementation completion, verify:

- every visible asset in the final script has a row, manifest entry, final file, and wiring handoff
- every final focus has an icon
- every implemented country identity has all required flag sizes
- every fictional one-person portrait has a matching gendered name pool
- every sourced asset has source and license notes
- every generated asset has a prompt and source evidence
- every animation has real source frames and a static fallback
- no placeholder, copied, resized-across-type, or undocumented visible asset is presented as final

## Release-candidate disposition vocabulary

The `status` column is a row-level release-candidate disposition, not a generic production wish list. Every row must use one of the following values and must remain truthful to the current filesystem, `.gfx` registrations, and runtime gates.

- `installed_runtime`: the final runtime file and its registered consumer are present in the current worktree.
- `installed_dormant`: the final runtime file and registration are present, but the owning package or super-event remains behind an explicit promotion, presentation, or readiness gate.
- `deferred_runtime_gated`: the surface has a documented runtime path, but the owning mechanic is intentionally closed until its readiness flag or acceptance barrier is true.
- `deferred_controlled_pool`: the row remains an accepted controlled-pool or optional family item and has no release-candidate runtime consumer that can be truthfully claimed as complete.
- `deferred_model_required`: the row cannot be released before a real model, entity, or model-dependent formation package exists.
- `deferred_unique_package_required`: the row belongs to a unique continent-scale or other bespoke package whose political, identity, presentation, and runtime surfaces are not yet complete.
- `pending_runtime_blocker`: a release-candidate consumer expects the row now, but the exact final file or registration is absent. This value is not used when a dormant gate intentionally explains the absence.

The current 2026-08-01 matrix contains 239 rows with these authoritative counts: `installed_runtime` 50, `installed_dormant` 21, `deferred_runtime_gated` 12, `deferred_controlled_pool` 133, `deferred_model_required` 16, and `deferred_unique_package_required` 7. The historical `pending_runtime_blocker` taxonomy is absent from the current matrix; no row is classified with that status.

The shared `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` now mirrors these six statuses for all 239 `asset_item` rows in matrix order, preserving its UTF-8 BOM. The ledger carries only matrix-status evidence in this reconciliation and does not add independent binary, GFX, visual, or live-consumer proof.

The current matrix retains two suggested-filename aliases that do not erase installed runtime evidence: the Africa-is-one news and super-event rows omit the `africa_` segment in their suggested filenames. The Charter header has no remaining path drift; its exact registered/runtime file is `gfx/interface/012_africa/charter_header_plate.dds`. The registered `.gfx` paths remain authoritative.
