---
name: chaos-redux-comfyui
description: "Use for complete Chaos Redux character portrait production: grounded-source research and explicit source-placeholder mode, optional provider-backed HOI4-style styled finals, fictional ImageGen portraits, processing, DDS conversion, portrait wiring, manifests, and handoffs."
---

# Chaos Redux portrait production

`chaosx_portrait_creator` owns every character portrait from brief to installed runtime asset.

1. Inspect matching installed-vanilla portrait references and lock the runtime basename, dimensions, role, and consumers.
2. Classify the subject. Grounded people and institutions require attributed Internet source research; fictional or impossible subjects use native ImageGen.
3. For a grounded portrait, name the mode in the brief or manifest. `source_placeholder` mode preserves the unchanged attributed source, explicit head-and-shoulders crop, deterministic `156x210` resize, DDS wiring, and identity; no HOI4 repaint is required. A provider-backed `styled_final` is optional and starts only after the user explicitly requests it: the user runs RunPod and supplies the output, while the worker validates and installs it. For that branch, retain the locked workflow revision, provider/job evidence, output hashes, and independent identity/framing/provenance review; a queued job or preview is not `styled_final`. Never open, operate, configure, queue, or monitor RunPod, and do not mark `replacement_pending` unless that styled-final request remains outstanding.
4. For a fictional or impossible portrait, invoke native ImageGen, review the full-resolution result against the brief and vanilla references, and retain prompt/source evidence.
5. Process the approved portrait, convert it to the required PNG/DDS variants, preserve stable runtime identifiers, update portrait-specific `.gfx` and existing character portrait references, and write the manifest and handoff.

Never generate or substitute the identity of a real or grounded person. If no defensible grounded source exists, mark the portrait blocked. Do not edit unrelated gameplay, localisation, or UI.
