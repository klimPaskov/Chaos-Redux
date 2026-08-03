# Historical portrait placeholder workflow update

Date: 2026-08-03

Status: reusable asset rule updated; no runtime portrait files were changed in this flag-error tranche.

The event-assets skill now treats a sourced historical portrait as a temporary original-source placeholder. The required sequence is an attributed archival source, an explicit head-and-shoulders crop with decoded-pixel evidence, deterministic `156x210` processing, an independent identity/crop/provenance audit, and DDS conversion. The original source is retained in the durable `docs/assets/portraits/` evidence queue and is never overwritten.

An HOI4-style ImageGen repaint is not required for historical portraits and must not be performed unless the user explicitly requests that additional art pass. Fictional high-chaos portraits retain their separate generated-portrait rules. Placeholder manifests must use the status `historical_source_placeholder` so a later stylized replacement is distinguishable from a source or provenance failure.

No advisor art was created or authorized by this update, and no gameplay, `.gfx`, localisation, portrait DDS, or source image was changed.
