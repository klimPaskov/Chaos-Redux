# Event 12 Africa asset-production prompt

Create the visual asset packages required by the Event 12 Africa specification. This is asset production, processing, conversion, manifest, contact-sheet, and GFX handoff work. It is not gameplay implementation.

## Required sources

Read:

- `specs/012_africa_spec_part_6_presentation_achievements_assets.md`
- `specs/012_africa_spec_part_7_host_country_playbooks.md`
- `specs/012_africa_spec_part_8_focus_route_deepening.md`
- `specs/012_africa_spec_part_9_priority_member_country_packages.md`
- `matrices/012_africa_asset_animation_matrix.csv`
- `matrices/012_africa_asset_animation_matrix_notes.md`
- `matrices/012_africa_host_country_playbook_matrix.csv`
- `matrices/012_africa_priority_member_package_matrix.csv`
- `matrices/012_africa_polity_catalog.csv`
- all three research notes
- the repository asset and frame-animation skills

Inspect the matching repository reference folder before creating each asset type.

The asset matrix contains 239 release-ledger rows. The required Event 012 packages are installed, including nine 3D model packages, 18 full frame-animation packages, six promoted Tier A visual and runtime packages, 16 historical male sourced placeholder portraits, six fictional male portraits, and three no-person evolution images. Controlled-pool and optional rows retain explicit dispositions rather than representing missing required outputs.

## Routing

Split production by source mode.

Use the sourced visual asset worker for real leaders, historical flags, attested symbols, real architecture-dependent imagery, and archival photographs that must depict real material.

Use the generated event-art worker for fictional and alternate-history report, news, and super-event scenes, fictional leaders and councils, fictional flags, high-chaos actors, UI panel art, faction emblems, and portrait frames.

Use the icon artist for focus, idea, national spirit, decision, achievement, technology, strange-unit, and small animated GUI icons.

Do not ask one worker to cover mixed sourced and generated packages without a clear split.

## Required deliverables

For every selected row from the asset matrix, produce or record:

- source file
- processed PNG preview
- final DDS or final HOI4 flag triplet
- target dimensions
- stable filename and sprite name
- final game folder
- manifest entry
- source, author, archive, date, and license notes when sourced
- generation prompt and source-mode rationale when generated
- GFX handoff with the target `.gfx` file and ready-to-review sprite information
- contact sheet for large families
- status as complete, blocked, or needs user review

Do not mark an item complete when only a source image or prompt exists.

## Priority order

1. Charter GUI static package, primary Charter values, and four route-commitment values.
2. Host overlay motif kits, first-proof state kit, regional controls, and selected-member states.
3. Entry, protection, congress, restoration, diaspora, corridor, League, Africa is one, and Scramble presentation images.
4. Host constitutional flags, Charter League emblem, portrait frames, and core leader portraits or institutional presentation records.
5. Focus, idea, and decision icon families required by the first implementable route tranche.
6. The seven constitutional dilemma state families and postwar review family.
7. The 16 priority-member visual packages and their distinct-mechanic icons.
8. Other Tier A restored-polity packages selected for implementation, with the six promoted packages already installed on existing carriers.
9. Achievement icons.
10. High-chaos actors and strange-unit packages.
11. Continent-unifier and terminal identity packages.

Prioritisation does not remove later rows. Record every controlled-pool or optional row with its explicit disposition.

## Host and country visual rules

A country-specific host overlay should communicate the starting problem without rebuilding the entire interface. Use the six reusable motif kits for treaty sovereignty, invasion and resistance, federal amalgamation, concession and resource control, land settlement, and corridor or island play. Add the selected host emblem or flag only where it remains readable.

The first-proof state kit must show active, succeeded, failed, recovery, and recovered states. The post-unification host legacy card should preserve the origin country without placing its flag over the whole continental identity.

Priority-member packages need direct flags, a leader portrait or institutional emblem and text, route identity variants when government changes, and a compact icon family for the distinct mechanic. Do not turn every prose detail into a new asset. Reuse the package’s coherent visual language.

## Historical and identity safeguards

- Do not generate real historical leaders.
- Do not invent an attested historical flag when a reliable source exists.
- Record uncertainty when no direct flag or portrait source can be verified.
- Do not replace all polity flags with one generic pan-African design.
- Keep public country names direct and readable.
- Never use the required obscene ruler strings in filenames, paths, sprite names, tags, or technical identifiers.
- For one-person fictional portraits, record apparent gender presentation and require a matching regional name pool and leader metadata.
- Use institutional names, emblems, and text for councils, crowds, committees, and symbolic bodies rather than council or group portraits.
- Keep nonhuman actors visibly nonhuman. Do not turn a human African ethnic identity into an animal or supernatural caricature.

## Icon rules

Focus, idea, decision, achievement, and technology icons are separate asset types. Do not satisfy one type by resizing another. Every final focus needs its own 94x86 icon assignment even when it belongs to a coordinated family.

The 78 route-payoff rows are focus roles, not necessarily 78 one-to-one focus icons. Assign icons to the final implemented focuses after the focus structure is fixed. The route capstone seals, route commitment values, and crisis icons remain separate UI and decision assets.

Transparent icons need real transparency, no checkerboard, no white halo, no opaque square, and no generated text.

## Animation rules

For every approved animated row or state-driven addition:

- write an animation brief and frame plan
- approve a static fallback first
- create separate real source frames
- normalise scale and anchor mechanically
- build a horizontal frame-sheet PNG and DDS
- create a preview GIF only for review
- record frame count, frame size, sheet size, frames per second, looping, play-on-show behaviour, state trigger, and target GUI surface

Do not create final motion by shifting, scaling, rotating, warping, blurring, recolouring, changing opacity, or adding a glow to one still image.

Grounded route seals and ordinary country packages should remain mostly static. Motion is appropriate for active proof progress, withdrawal or deadlock warnings, commander crisis, Covenant obligations, high-chaos reveal, and major completed-state activation.

## Image treatment

Report images are 210x176 and use the project report-card treatment. News images are 397x153 and black and white. Super-event images are 457x328 with a strong central subject and enough contrast for the UI.

Use period-authentic 1936 to 1945 clothing, transport, architecture, and photographic presentation where the scene belongs to the normal timeline. Avoid modern props, film stills, reenactments, readable generated text, and generic map-only compositions.

## Completion report

Return:

- files created
- matrix rows completed
- source-mode decisions
- final paths and sprite names
- manifests and handoffs written
- animations completed with frame evidence
- blocked and needs-review items
- controlled-pool or review items still open, with no required model, animation, portrait, or super-event media package missing
- no claim of full Event 12 completion
