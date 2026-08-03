---
name: chaos-redux-comfyui-portraits
description: Use for provider-aware fictional high-chaos portraits or explicitly requested HOI4-style replacements in Chaos Redux, including source handoff, ComfyUI execution, output review, DDS conversion, and replacement state.
---

# Chaos Redux ComfyUI portraits

This skill owns provider-backed fictional high-chaos portraits and explicitly requested HOI4-style replacements. It is optional for grounded identities: their default runtime asset is the unchanged sourced placeholder workflow in `chaos-redux-event-assets`. This skill does not replace the asset skill's source ownership, evidence, or standard DDS requirements.

## Source of truth

When a provider workflow is requested, read `docs/systems/comfyui_portrait_pipeline/upstream-lock.json` before selecting a workflow or changing defaults. The lock records the current default branch, exact upstream commit, workflow hashes, model manifest hash, and verified defaults for `https://github.com/klimPaskov/comfyui-hoi4-portraits`. Read the matching upstream document at that exact commit when setup or execution behavior is needed; do not use a copied or floating workflow snapshot.

The supported provider workflow ids are `hoi4_portrait_flux2_klein_9b_full_power`, `hoi4_portrait_flux2_klein_9b_esrgan_only`, and `hoi4_portrait_flux2_klein_9b_text_to_image`. Use the API graph for Cloud or local automation and the editor graph for a human or browser-controlled RunPod session.

The locked provider defaults are the `hoi4_portrait,` prefix, LoRA strength `0.7`, Euler sampling, eight steps, CFG `5`, `832x1120` master output, and `156x210` game output. Verify these values against the lock and upstream graph before every workflow revision.

## Provider persistence

The selected provider is stored in `.codex/config.toml` under `[portrait_pipeline]` with `enabled`, `provider`, `provider_status`, `workflow_repository`, `workflow_commit`, and `preferred_workflow`. Valid Chaos Redux providers are `cloud`, `local`, and `runpod`; `disabled` is not a valid project state. Do not ask again when the stored provider is available. Ask again only for an explicit provider change, corrupt or permanently unusable configuration, removed credentials, or a direct reconfiguration request.

The baseline configuration selects Cloud with `needs_authorization` until the official connection is completed. The Cloud MCP entry uses the verified streamable HTTP route `https://cloud.comfy.org/mcp`; complete authorization with the client’s MCP login flow and keep tokens or API keys outside the repository.

Provider skills own provider setup and execution details: use `chaos-redux-comfyui-cloud` for Cloud MCP, `chaos-redux-comfyui-local` for local REST/WebSocket execution and hardware/model checks, and `chaos-redux-comfyui-runpod` for an existing pod and browser-controlled editor execution.

## Portrait job contract

For every provider-backed replacement or generated portrait job, read and validate the job against `docs/systems/comfyui_portrait_pipeline/portrait-job.schema.json`. A provider job must provide the source path, source classification, workflow, restoration and background choices, exact runtime DDS path, runtime basename, sprite name, character file, character id, and persisted provider. Never guess a mod root, tag, character key, output name, or sprite name.

For an explicitly requested grounded replacement, use `full_power` for damaged, low-quality, or difficult sources when the selected provider can support it, and `esrgan_only` for clean source portraits or a shorter route. Use `text_to_image` only for an explicitly authorized fictional high-chaos or impossible subject without a source portrait. Respect an explicit user workflow choice and do not enable restoration automatically when it harms likeness.

For a provider-backed generated or styled portrait, the positive prompt describes only the visible person. It begins with `hoi4_portrait,`, omits the subject's name, and contains no game/style instruction, background instruction, lighting or rendering instruction, restoration instruction, or unsupported biography. Preserve the final prompt alone in the matching TXT file in the durable source archive. A grounded source-only placeholder does not require a prompt TXT.

## Ownership and review

`chaosx_asset_source_researcher` owns real-person source acquisition, authorization, attribution, date, archive, license, source hash, exact crop evidence, and the immutable source package. It stops after the source handoff, adding a prompt only when a provider-backed generated or styled route is explicitly requested. It must not repaint, filter, genericize, or call a sourced portrait final.

`chaosx_portrait_creator` owns provider execution for fictional high-chaos portraits or explicitly requested replacements, including workflow selection, source upload, prompt and LoRA settings, master/game output retrieval, output hashes, source-to-result comparison, framing and identity review evidence, standard PNG processing, DDS conversion, and the portrait handoff. It must not edit character files, `.gfx`, GUI, events, focuses, decisions, localisation, country setup, or gameplay.

For a grounded person, an explicitly requested styled replacement must preserve identity, age, asymmetry, expression, gaze, head direction, hair, facial hair, clothing, framing, and role-specific HOI4 references; the default grounded runtime remains an unchanged sourced placeholder. For a fictional high-chaos subject, use the text-to-image workflow and retain the classification, role, gender presentation, name-pool requirement, and extraordinary invented motif. The general generated-event-art subagent does not own final character portraits.

The parent agent owns final runtime wiring and completion. A grounded source-only portrait is final after the unchanged source, exact head-and-shoulders crop, deterministic `156x210` fit, DDS conversion, and independent identity/framing/provenance review pass. A provider-backed replacement or fictional portrait is final only after its `832x1120` master and `156x210` output are downloaded, decoded, hash-recorded, visually compared with the source and role references, converted to DDS, and passed through the independent review gate. A successful provider request, queued job, or preview alone is not success.

## Grounded source-placeholder default

Do not create a provider job for a grounded identity unless a later explicit styled-replacement request exists. Keep the unchanged source in the durable archive, create the exact crop with JSON equality evidence, fit it deterministically to `156x210`, pass independent identity/framing/provenance review, convert it to DDS, and wire it as `source_placeholder`. In the provider job schema, use `source_status = source_placeholder` by default, `styled_final` only after an explicit replacement passes review, and `replacement_pending` only while that explicit request awaits provider execution or review.

## Durable source and fallback

Store the full-resolution source master in its original format at `docs/assets/portraits/<event_id>_<event_slug>/`; add a lossless PNG copy only when a processor requires one, and add the matching `.txt` only for a provider-backed generated or explicitly styled portrait. The source archive is durable and must not be removed with a temporary event workspace. No runtime `.gfx`, character, GUI, event, focus, decision, or idea reference may point into it.

For a grounded identity, provider availability does not block the default source-placeholder path: retain the unchanged source, create the exact head-and-shoulders crop with the asset skill's Pillow crop utility and JSON equality evidence, resize it deterministically to `156x210`, convert it through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and wire it as `source_placeholder` after independent review. If an explicitly requested styled replacement is pending because the provider is unavailable, retain the source and optional prompt, keep the source placeholder wired as `replacement_pending`, and never apply an improvised filter or substitute a generated face. The replacement remains optional and pending until reviewed.

## Required handoff

For a grounded source-only handoff, list the source classification, source path and hash, exact crop evidence, deterministic `156x210` candidate, DDS path and hash, identity/framing/provenance review, reviewer, final or placeholder state, and any blocker. For a provider-backed replacement or fictional portrait, list the job manifest, provider and status, locked upstream commit, selected workflow, prompt path and hash, returned job id, master and game output paths and hashes, identity/framing review, and any setup or provider blocker; include source and crop evidence when the provider job is source-backed. Every handoff must state each file changed and each skipped validation. Runtime wiring is a parent-owned follow-up, not an implicit side effect of this skill.
