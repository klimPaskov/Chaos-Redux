---
name: chaos-redux-comfyui-portraits
description: Use for grounded source-placeholder portraits and provider-backed final character portraits in Chaos Redux, including source handoff, mode selection, ComfyUI execution for styled outputs, output review, DDS conversion, and replacement state.
---

# Chaos Redux ComfyUI portraits

This skill defines the grounded source-placeholder path and owns provider-backed production where the selected portrait mode requires it. For a grounded historical or otherwise real-person portrait, an explicit source-placeholder request preserves the attributed source without creating a provider job or executing ComfyUI. Provider-backed styled output remains required only when the user explicitly requests it or the task calls for a styled final; fictional high-chaos portraits continue to use their provider-backed text-to-image route. This skill does not replace the asset skill's source ownership, evidence, or standard DDS requirements.

## Source of truth

When a provider workflow is requested, read `docs/systems/comfyui_portrait_pipeline/upstream-lock.json` before selecting a workflow or changing defaults. The lock records the current default branch, exact upstream commit, workflow hashes, model manifest hash, and verified defaults for `https://github.com/klimPaskov/comfyui-hoi4-portraits`. Read the matching upstream document at that exact commit when setup or execution behavior is needed; do not use a copied or floating workflow snapshot.

The current upstream workflow ids are `hoi4_portrait_flux2_klein_9b_source`, `hoi4_portrait_processing_only`, and `hoi4_portrait_flux2_klein_9b_text_to_image`. The product ids are `source`, `processing_only`, and `text_to_image`; migrated aliases `full_power` and `esrgan_only` resolve to `source` and `processing_only`. Use the API graph for Cloud or local automation and the editor graph for a human or browser-controlled RunPod session.

The locked provider defaults are the `hoi4_portrait,` prefix, LoRA strength `0.7`, Euler sampling, eight steps, CFG `5`, `832x1120` master output, and `156x210` game output. Verify these values against the lock and upstream graph before every workflow revision.

## Provider persistence

The selected provider is stored in `.codex/config.toml` under `[portrait_pipeline]` with `enabled`, `provider`, `provider_status`, `workflow_repository`, `workflow_branch`, `workflow_commit`, `preferred_workflow`, and non-secret route fields. On first configuration ask for Comfy Cloud, RunPod, or Local when feasible; `disabled` is not a valid Chaos Redux state. Do not ask again when the stored provider is available. Ask again only for an explicit provider change, corrupt or permanently unusable configuration, removed credentials, or a direct reconfiguration request.

The baseline configuration selects Cloud with `needs_authorization` until the official connection is completed. The Cloud MCP entry uses the verified streamable HTTP route `https://cloud.comfy.org/mcp`; complete authorization with the client’s MCP login flow and keep tokens or API keys outside the repository.

Provider skills own provider setup and execution details: use `chaos-redux-comfyui-cloud` for Cloud MCP, `chaos-redux-comfyui-local` for local REST/WebSocket execution and hardware/model checks, and `chaos-redux-comfyui-runpod` for an existing pod and browser-controlled editor execution.

Deferred authorization, subscription, model import, Hugging Face access, workflow installation, reachability, and temporary availability use the explicit status values in the job schema. They never become a styled-portrait success claim.

Provider persistence and setup apply only to provider-backed modes; an explicit grounded source-placeholder request must not trigger provider configuration, upload, or execution.

## Portrait job contract

For every provider-backed replacement or generated portrait job, read and validate the job against `docs/systems/comfyui_portrait_pipeline/portrait-job.schema.json`. A provider job must provide the source path, source classification, workflow, restoration and background choices, exact runtime DDS path, runtime basename, sprite name, character file, character id, and persisted provider. Never guess a mod root, tag, character key, output name, or sprite name.

Do not create or validate a provider job for an explicitly requested grounded source-placeholder mode.

For a provider-backed grounded replacement, use `source` for damaged, low-quality, or difficult sources when restoration is needed, and `processing_only` for a clean source or a source-processing-only request. Use `text_to_image` only for an explicitly authorized fictional high-chaos or impossible subject without a source portrait. Respect an explicit user workflow choice and do not enable restoration automatically when it harms likeness.

For every provider job, the positive prompt describes only the visible person. It begins with `hoi4_portrait,`, omits the subject's name, and contains no game/style instruction, background instruction, lighting or rendering instruction, restoration instruction, or unsupported biography. Preserve the final prompt alone in the matching TXT file in the durable source archive; a temporary source placeholder may retain the pending prompt without claiming a styled result.

## Ownership and review

`chaosx_asset_source_researcher` owns real-person source acquisition, authorization, attribution, date, archive, license, source hash, exact crop evidence, and the immutable source package. For a provider-backed styled or generated route it also owns the person-only prompt. It stops after the source handoff and must not repaint, filter, genericize, upload, or call a sourced portrait final.

`chaosx_portrait_creator` owns provider execution for provider-backed final fictional or grounded character portraits, including workflow selection, source upload, prompt and LoRA settings, master/game output retrieval, output hashes, source-to-result comparison, framing and identity review evidence, standard PNG processing, DDS conversion, and the portrait handoff. It does not execute a provider job for an explicit source-placeholder request and must not edit character files, `.gfx`, GUI, events, focuses, decisions, localisation, country setup, or gameplay.

For a grounded person, provider-backed styling must preserve identity, age, asymmetry, expression, gaze, head direction, hair, facial hair, clothing, framing, and role-specific HOI4 references. When source-placeholder mode is explicitly requested, do not upload or execute the source through a provider; use the exact source-placeholder sequence below and keep the runtime state `replacement_pending`. For a fictional high-chaos subject, use the text-to-image workflow and retain the classification, role, gender presentation, name-pool requirement, and extraordinary invented motif. The general generated-event-art subagent does not own final character portraits.

The parent agent owns final runtime wiring and completion. A grounded source-placeholder portrait is complete as `source_placeholder` only after the unchanged source, exact crop, deterministic `156x210` fit, DDS conversion, and independent identity/framing/provenance review pass; `replacement_pending` records that no styled result is being claimed. A provider-backed or fictional portrait is final only after its `832x1120` master and `156x210` output are downloaded, decoded, hash-recorded, visually compared with the source and role references, converted to DDS, and passed through the independent review gate. A successful provider request, queued job, or preview alone is not success.

## Grounded source-placeholder mode

When the user explicitly requests source-placeholder mode for a grounded historical or otherwise real-person portrait, preserve the unchanged attributed source, create the explicit head-and-shoulders crop with JSON equality evidence, fit it deterministically to `156x210`, pass independent identity/framing/provenance review, convert it to DDS, and wire it as `source_placeholder` with `replacement_pending`. Do not create a provider job, select a provider workflow, upload the source, or execute ComfyUI for this mode. Never repaint, style-transfer, recolour, retouch, filter, or substitute a generated face. Use `styled_final` only for provider-backed output requested or required by the task and passed through independent review.

## Durable source and fallback

Store the full-resolution source master in its original format at `docs/assets/portraits/<event_id>_<event_slug>/`; add a lossless PNG copy only when a processor requires one, and add the matching `.txt` only for a provider-backed generated or explicitly styled portrait. The source archive is durable and must not be removed with a temporary event workspace. No runtime `.gfx`, character, GUI, event, focus, decision, or idea reference may point into it.

For source-placeholder mode, use the asset skill's Pillow crop utility with JSON equality evidence, resize the crop deterministically to `156x210`, convert it through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and wire the runtime state as `source_placeholder` with `replacement_pending`; no provider prompt or job is required. If a styled route was explicitly requested or required but the provider is unavailable, retain the same source placeholder and pending state until the reviewed provider replacement exists. Never apply an improvised filter or substitute a generated face.

## Required handoff

For a source-placeholder handoff, list the source classification, unchanged source path and hash, exact crop evidence, deterministic `156x210` candidate, DDS path and hash, identity/framing/provenance review, runtime `source_placeholder` and `replacement_pending` state, and any admission hold. For a provider-backed handoff, list the job manifest, provider and status, locked upstream commit, selected workflow, person-only prompt path and hash, returned job id, master and game output paths and hashes, identity/framing review, and any setup or provider blocker. Every handoff must state each file changed and each skipped validation. Runtime wiring is a parent-owned follow-up, not an implicit side effect of this skill.
