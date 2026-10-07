# 3D Model, Animation, Unit Audio, and Counter Prompt: Event 039 Murder Mystery

Build the complete runtime visual and sound package for the Event 39 Assassin Forces family. Read `AGENTS.md`, `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, Part 9, Part 14, the asset prompt, and the live unit, entity, mesh, animation, audio, and counter precedents.

## Scope

Mandatory model jobs:

1. Assassin infantry family, one humanoid source model with supported variants for Assassin Cadre, Shadow Company, Master Assassin, and a clearly distinct Silent Guard presentation
2. Mechanized Assassin vehicle, one distinct late-game light mechanized or armored transport model

Saboteur Cell is support-only and needs icon and sound coverage, not a standalone map model unless a real consumer is later accepted.

## Identity

Use practical 1930s to 1940s clandestine field equipment, compact communications, satchels, climbing or breaching gear, muted clothing, and period weapons. Avoid modern tactical equipment, fantasy armor, glowing effects, katanas, generic ninja costumes, real religious symbols, and real extremist insignia.

The vehicle should look like a plausible period reconnaissance or light transport conversion. It cannot resemble a modern stealth vehicle.

## Input-art rule

Each Meshy model job receives exactly one approved final input image. Use clean modern designed artwork made after period-source research. Show one subject, clear silhouette, full visible geometry, stable three-quarter perspective, simple background, and no text.

Never send Meshy a turnaround, collage, multi-view board, contact sheet, side-profile sheet, or several candidate images. Review and approve the one input before paid work.

## Provider route

Follow the current [3D model owner skill](../../../.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md) for gates, source eligibility, provider attempt limits, separated item-free body and held-item inputs, component completion, and Blender transitions.
Try rigging once per eligible model and animation once per required action; failed or unusable output moves to real Blender-authored rigs, weights and actions without paid retries or renewed approval.
Firearm-bearing bodies use weapon-free Meshy input and direct Blender rig, weapon, held-item and action work.
Preserve provider lineage, rejected candidates, modeled components, live authoring and review evidence.

## Vanilla crosswalk

Before modeling, inspect and record the exact installed vanilla humanoid mesh and entity that define axes, facing, origin, source geometry height, entity scale, ground contact, and effective runtime height. Inspect one exact vehicle precedent for orientation, scale, wheels or tracks, materials, actions, and entity binding.

Do not invent vanilla file names. Missing crosswalk evidence blocks production.

## Humanoid actions

Required skeletal actions:

- idle loop
- movement loop
- attack sequence with aim, discharge, recoil, and recovery
- death sequence with articulated collapse, impact, and settling

Record action name, semantic role, FPS, frame range, loop policy, root motion or in-place policy, ground contact, retarget route, static fallback, runtime binding, and evidence.

Final motion follows the provider or authorized live Blender route in the owner skill, with real role-specific articulated actions and deformation review.
Transform-only motion, static aliases, whole-rig rotations and unreviewed generated keyframes remain invalid.

## Vehicle actions

Provide idle or engine loop, movement with correct wheel or track behavior, attack only when a visible weapon consumer exists, and destruction or death behavior required by the entity precedent. Preserve ground contact and scale.

## Blender and conversion evidence

Use deterministic job roots and preserve:

- approved input image
- provider lineage and downloads
- source and checkpoint `.blend` files
- textures and materials
- rig and action inventory
- export files
- `.mesh` and `.anim` parser or reimport evidence
- runtime hashes
- entity scale and axis crosswalk
- runtime handoff paths and consumers

A provider preview or `.blend` file is not final.

## Unit audio

Research and prepare every audio role that the actual runtime consumers support:

- select
- acknowledge
- move
- attack
- retreat
- idle variation
- damage or suppression
- death or destruction
- vehicle engine and movement
- weapon, impact, equipment, and movement synchronization

Use only identified vanilla files or legitimate external sources with provenance and license. Preserve original downloads. Document creator, source URL, license, attribution, checksum, edit, final path, sound ID, consumer, variation, loop, volume, distance, and synchronization.

Recording, generation, synthesis, oscillators, primitive waveforms, placeholder sound, and unclear licenses are forbidden. Keep spoken command style restrained and host or route aware. Do not invent a stereotyped accent.

## Counters

Inspect the exact installed vanilla definition and DDS plus the matching skill-local family for every large counter, map counter, and template emblem. Sample the real vanilla green palette.

Produce distinct supported counters for Assassin Cadre, Shadow Company, Silent Guard, Master Assassin, Mechanized Assassin, and any Saboteur Cell surface the engine displays. Match canvas, frame order, alpha, border, silhouette, shading, contrast, and state behavior.

Reused counters, arbitrary green, and unreferenced imitation are blocked.

## Integration handoff

The parent implementation owns unit definitions, templates, Event 19 provider, CXT, technology, equipment, entities, asset wiring, and live gameplay. Supply exact files, hashes, action names, sound IDs, counter tokens, scale, material, entity, and consumer notes.

Do not edit unrelated gameplay, localisation, spreadsheets, or country logic.

## Acceptance

Complete only when both model families have approved source art, provider lineage, final meshes, materials, rigs, required actions, parser or reimport proof, runtime bindings, sourced audio, bespoke counters, and documentation. Missing final motion, guessed scale, one-view ambiguity, unsourced sound, or generic counters are blockers.
