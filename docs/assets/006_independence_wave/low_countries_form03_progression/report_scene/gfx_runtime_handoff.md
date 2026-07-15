# FORM-03 report-scene GFX and runtime handoff

## Exact runtime binding

- Sprite: GFX_report_event_006_form03_charter_convention
- Final DDS: gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds
- Owning registration: interface/006_independence_wave_event_pictures.gfx
- Texture size: 210x176
- Texture format: one-level legacy uncompressed 32-bit BGRA with alpha

The existing registered definition is:

    spriteType = {
        name = "GFX_report_event_006_form03_charter_convention"
        texturefile = "gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds"
    }

No sprite or path rename is proposed.

## Live consumers

events/006_independence_wave.txt currently points every FORM-03 event from chaosx.nr6.300 through chaosx.nr6.308 to this exact sprite:

- chaosx.nr6.300: provisional Charter of Languages and Works opening report
- chaosx.nr6.301: federal-service language convention
- chaosx.nr6.302: sovereign associate constitutional answer
- chaosx.nr6.303: sovereign corridor protocol
- chaosx.nr6.304: late associate accession terms
- chaosx.nr6.305: member ratification or withdrawal report
- chaosx.nr6.306: full compact ratification
- chaosx.nr6.307: stored compromise outcome
- chaosx.nr6.308: charter rupture and reopening terms

This broad consumer set is visually coherent because the scene shows the shared constitutional table and public-works plan package behind all nine reports.

## Asset records

- Submanifest: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md
- Prompt and provenance: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/prompts/report_event_006_form03_charter_convention_prompt.md
- Technical metadata: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/metadata/report_event_006_form03_charter_convention_metadata.json
- Checksums: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/checksums.sha256
- Native review: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/review/report_event_006_form03_charter_convention_native_review.png
- Enlarged review: docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/review/report_event_006_form03_charter_convention_enlarged_nearest_review.png

The main agent does not need to edit the GFX registration or event picture fields unless a later rename is deliberately accepted.
