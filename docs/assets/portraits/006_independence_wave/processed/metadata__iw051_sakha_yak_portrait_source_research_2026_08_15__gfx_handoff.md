# IW-051 portrait wiring handoff

Status: NOT READY FOR RUNTIME WIRING.

The source package is archival evidence and crop-review material only. No DDS was created, no portrait-specific `.gfx` entry was added, and no vanilla character, country, history, event, gameplay, or localisation file was modified.

The exact installed-vanilla consumers are:

- `YAK_pavel_pevznyak` -> `GFX_portrait_Pavel_Pevznyak` -> current generic `gfx/leaders/Asia/Portrait_Asia_Generic_2.dds`.
- `YAK_anatoly_pepelyayev` -> `GFX_portrait_Anatoly_Pepelyayev` -> current generic `gfx/leaders/Asia/Portrait_Asia_Generic_1.dds`.

Pavel Pevznyak has a source-backed 1936 role/date fit and is the only candidate that clears the identity/source/role gates. Anatoly Pepelyayev has a source-backed identity and public-domain record but fails the 1936 YAK officeholder gate; do not promote him without an explicit parent decision supported by a defensible alternate-history appointment source.

The parent must review `metadata__iw051_sakha_yak_portrait_source_research_2026_08_15__manifest.json`, the source provenance contracts, and the role/date review before any future runtime wiring. Any future styled final must be supplied by the user after their RunPod workflow; the agent did not and will not operate RunPod.
