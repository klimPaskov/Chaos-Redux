# WP3 pipeline capability handoff

Owner: section 3 pipeline lead for tool changes; WP3 retains package source repair and evidence.
Disposition: `blocked` for unsupported material recipes; other repairs continue with the existing validated routes.

## Planned material recipes the shared validator cannot express

`textures/conventions.py` supports six fixed classes and enforces each class's G/A bounds.
Declaring a class wet only exempts its mean-A limit; it does not override its G/A ranges.
The WP3 plan requires nonmetal jaw/blood/parasite G≈180–220 and A up to 200, matte corpse/bone gloss around 42–80, and demonic skin G≤32.
Those values cannot pass the current skin G110–160/A120–160 recipe.
Classifying wet flesh as steel or dead skin as fur would give a false material identity and is not permitted.
The undead instruction for constant G32 also conflicts with the shared constant-G rejection and needs an explicit approved source-backed interpretation.
Needed: a provenance-aware regional recipe route for the accepted WP3 values, preserving explicit metal masks and real provider roughness/metalness/detail rather than weakening unrelated gates.
The root requested the validated route from the orchestrator; no answer or tool-owner patch is assumed.

## BC1 runtime diffuse and material preview binding

The production texture route requires BC1 diffuse for opaque units.
`bind_existing_pdx_material` rejects that format with `Require verified uncompressed A8R8G8B8/BGRA or alpha-capable BC3/BC7 DDS.`
WP3 retained production BC1 and prepared a preview-only BC3 representation with exactly identical decoded RGB across every mip, verified by the shared DDS reader.
Current registered specular and normal inputs remain explicit; preview copies and their hashes are separate from runtime files.
Needed: the pipeline owner should make the verified material binding route accept the production opaque BC1 family directly, or document the validated pixel-equivalent preview route.
WP3 does not patch the shared binder.

## Native Blender path length

The current Blender bridge failed to open a 279-character staged normal path that PowerShell could list and hash.
It successfully opened a 216-character copy inside the same approved job, whose SHA-256 was identical.
This is an observed input-path limitation on this installation, not a claim about every Windows filesystem API.
Keep preview input paths short, check them inside the actual consumer, and retain original/copy hashes and purpose.
Do not rename runtime assets or substitute unverified files to work around a preview path issue.

## Existing-model repair intake

The mutant package had no `job.yaml`, so native export stopped after writing a candidate with `Delivery gate needs the existing job profile.`
WP3 created a complete new repair intake from the accepted task and actual calibrated source, without changing the pre-existing zombie job or any shared configuration.
The retry passes its delivery gate; the rejected attempt stays outside runtime.
Other package repairs should check for a complete job profile before export instead of treating a working checkpoint as the whole intake.

## Reusable guidance disposition

These observations are package-independent workflow guidance for the pipeline/skill owner.
They are retained here because the task assigns shared tool edits to section 3 and limits WP3's ownership to its package.
Any skill update should carry only the reusable route, format, path and intake rules, with no event-specific source or model context.

## Animated-checkpoint material retention

The locked material binder verified the current mutant DDS inputs but rejected its copied checkpoint after save/reopen with `changed sections: ['actions']; object deltas: {}`.
Source checkpoint SHA is `96e0ad277bdf66d4165366d97e0de01b4cc18029ad032b130e6a2432052372d4`; rejected material-copy SHA is `10f41b4636fb2a4d7dbe0a656f8ab3c5a5c9260e4df62a1cd836d3186fa8ca92`.
The exact diagnostic is retained at `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/logs/adapter/6f47c873f7f14c01a3e81070bbf88d86.result.json`, SHA `365b1e4fd3961f38b76217ab33824336431665a26bc5283f86424582fc2d75d6`.
Both source and native reimport previews remain magenta; correctly staged files and DDS hashes do not prove rendered binding.
WP3 kept the failed material copy and attack outside runtime, without retrying or weakening the retention check.
Needed: the pipeline owner should inspect the before/after action fingerprints and preserve all intended action data through non-destructive material binding and save/reopen.
The diagnosed section difference is recorded as an unresolved retention failure; WP3 does not infer a cause or patch the shared tool.
