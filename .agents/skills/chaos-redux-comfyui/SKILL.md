---
name: chaos-redux-comfyui
description: Use for sourced or grounded Chaos Redux character portraits that require the pinned RunPod ComfyUI route, user-supplied final output review, DDS replacement, and honest fallback state.
---

# Chaos Redux ComfyUI

Chaos Redux requires the pinned ComfyUI workflow through RunPod for every final sourced or grounded character portrait, but generation is user-owned. The agent prepares the locked job and placeholder; the user runs the RunPod workflow and drops in the final portraits. The agent then validates the supplied outputs and replaces the placeholder. The normal guidance is API-first and does not use computer control. Use browser or computer control only when the parent explicitly asks for help with the current user-run job. Non-sourced fictional or impossible portraits use native ImageGen under the parent brief and never use this workflow.

## Source and configuration

Read `docs/systems/comfyui_portrait_pipeline/upstream-lock.json` before every portrait job or workflow change. Use the exact locked repository branch and commit; never use a floating workflow or copied snapshot. The authorized product workflows are `source` and `processing_only`; `full_power` and `esrgan_only` are legacy aliases for those two. The upstream text-to-image graph is retained as provenance only and is not an authorized Chaos Redux route.

Chaos Redux persists one provider: `runpod`. The configuration in `.codex/config.toml` records the provider, `needs_runpod`/`ready` status, exact repository revision, preferred sourced workflow, RunPod workspace, API-first execution mode, and non-secret URL. RunPod credentials remain in a provider vault or scoped environment and never enter the repository.

Use the locked defaults: prompt prefix `hoi4_portrait,`; LoRA strength `0.7`; Euler; eight steps; CFG `5`; `832x1120` master; and `156x210` game output. Verify them against the locked upstream graph before execution.

## Source and production boundary

`chaosx_asset_source_researcher` owns real-person sourcing, authorization, attribution, source hash, crop evidence, durable storage, and the person-only prompt handoff. It stops before provider execution. `chaosx_portrait_creator` owns only sourced/grounded job validation, the user handoff, supplied-output retrieval or intake, identity/framing review, PNG processing, DDS conversion, placeholder replacement, and the handoff. It never queues or generates a RunPod job by itself. The parent owns character files, `.gfx`, gameplay, localisation, and final runtime wiring.

The ComfyUI job schema accepts only `grounded_source`. A job must identify the source path, workflow, RunPod provider, status, runtime basename, sprite, character file, character id, DDS path, prompt, and output evidence. Never guess any of these values. The prompt begins with `hoi4_portrait,`, describes only the visible person, omits the name, and contains no background, lighting, rendering, restoration, game-style, or unsupported biographical instruction.

Fictional, impossible, supernatural, or otherwise non-sourced portraits are not ComfyUI jobs. The parent uses native ImageGen, keeps the fictional classification and design brief, and performs the native ImageGen review/archive handoff. Do not send those subjects to `chaosx_portrait_creator`, a ComfyUI text-to-image graph, or a source-based fallback.

## User-owned generation

Give the user the API-format graph and the RunPod ComfyUI API steps when they want an API route. The user uploads the sourced image, sets the returned filename in `LoadImage.image`, performs the dry-run/no-spend validation, queues the job, retains the exact `prompt_id`, reviews the three current source candidates, selects one master/game pair, verifies dimensions and hashes, and drops the final PNGs into the controlled portrait job directory. The agent may validate the job and supplied files, but must not queue or generate the portrait unless the user explicitly changes that boundary for the current task. Queue emptiness or a returned request alone is not success.

Use background replacement only after the decoded styled result. Enable restoration only when the source needs it. Never upload a source through an unverified route, silently change providers, or treat a queued job as final.

## Computer control only on request

Do not open or control the RunPod browser or desktop by default. If the parent explicitly asks for computer control for the current user-run job, help with visible node titles and previews: load the editor graph, upload/select the source, preview the crop, enter the person-only prompt, verify the LoRA and strength, configure restoration/background order, observe the user's queue/history, and verify the user's downloaded outputs. Do not silently queue or generate a portrait. If computer control was not explicitly requested or is unavailable, provide the exact manual/API steps and do not claim generation.

## Fallback and durable archive

If the RunPod provider is unavailable for a grounded source portrait, preserve the unchanged source and prompt, create the exact head-and-shoulders crop, fit it deterministically to `156x210`, convert it with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and report `source_placeholder` plus `replacement_pending`. This is not styled completion. Never repaint, filter, recolour, substitute a generated face, or erase the source archive.

Store the full-resolution source and matching final prompt at `docs/assets/portraits/<event_id>_<event_slug>/` using the runtime basename. Runtime files must never reference that archive. Keep source, prompt, master, game output, DDS, hashes, review evidence, provider status, job id, locked commit, and every changed/skipped file in the handoff. A native ImageGen handoff follows its parent-owned gate, not this fallback.

## Completion gate

A sourced portrait is final only after the user supplies verified `832x1120` and `156x210` RunPod outputs, identity/framing/provenance review passes, the game PNG is converted to valid DDS, the supplied files replace the source placeholder, and the parent wires the exact runtime path. A provider status, preview, or source placeholder never proves final styled art.
