# Event 035 tooltip helper lifetime review

Disposition: implemented for source-level output lifetime and scope; native tooltip rendering remains unresolved.

Review scope: `common/scripted_effects/035_great_depression_decision_effects.txt::great_depression_prepare_action_tooltip_values`, its callers in `common/decisions/035_great_depression_decisions.txt`, and the matching Event 035 localisation fields. This review made no gameplay edits.

## Findings

The temporary-output concern was valid for the earlier helper form. The event skill says values first created as temporary variables inside a scripted effect may disappear after that helper returns, and the offline Data structures section states the same call-frame caveat. Caller-preinitializing every value at every decision site would add needless repetition here.

The current helper at `common/scripted_effects/035_great_depression_decision_effects.txt:175` writes 37 constant-derived display fields as regular country variables. Those values are stable display data, so this is the minimal safe cross-return storage choice. The other `great_depression_tt_doctrine_drift` value is a caller-owned temporary set by individual decision effects and is outside these 37 outputs; leave it unchanged.

The 100 call sites are all direct country-level decision or mission effect blocks: 85 `complete_effect` blocks and 15 mission `timeout_effect` blocks. None of the calls is nested inside a target-country or target-state scope. The targeted decisions enter `FROM` only for target-specific outcome effects, after the helper call. Decision modding documents that `ROOT` remains the country taking a targeted decision while `FROM` is its target; the mission section says `timeout_effect` executes for the country. Therefore the helper's current-scope write belongs to the acting country that the tooltip reads as `ROOT`.

All 37 helper-output fields are referenced only in `localisation/english/035_great_depression_l_english.yml`, and all those reads are explicitly `ROOT`-qualified. No live gameplay assignment to these 37 fields exists outside the helper. The separate historical `before/` probability-audit snapshot still contains the earlier temporary-variable form and is evidence only, not a live consumer.

`great_depression_refresh_costs` calls the helper at its start (`common/scripted_effects/035_great_depression_effects.txt:409-412`), before recalculating country-specific cost quotes. The 37 outputs are constant-derived, so this ordering does not stale a dynamic quote. The refresh path is reached from country runtime initialization and from pressure, exposure, supplier, and conference quote paths. Conference quote loops run the refresh in each quoted country's scope, so each quote country owns its cache; its own later decision tooltip reads that cache through `ROOT`.

The proposed regular-cache pattern is sound from source scope and lifetime evidence. No alternate storage pattern is needed. If runtime evidence later shows that the engine evaluates these decision effects in a way that makes persistent cache writes unsafe, that would require a separately reviewed display calculation strategy; repeated per-caller preinitialization is not a good fallback.

## Evidence and limits

- Repository guidance: `.agents/skills/chaos-redux-events/SKILL.md:169-181`, especially the helper-output lifetime rule.
- Offline wiki Data structures: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443` covers temporary-variable lifetime across scripted-effect returns; lines 444 onward describe country scoping and explicit scope prefixes. MCP `hoi4.reference_read` returned the Variable types section at lines 435-443, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Offline wiki Decision modding: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:465-475` says mission timeout effects execute for the country; lines 513 and 535-536 define `ROOT` as the decision-taking country and `FROM` as the target for targeted decisions. The decision reference context reported source revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- Offline wiki Localisation: `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:729-792` explains that temporary values calculated in scripted-localisation triggers are scoped to that localisation use. The decision reference context reported revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Installed game documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1-46` documents country decision scopes and targeted-trigger scopes. MCP `hoi4.reference_read` returned this section at lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
- Source audit: 100 helper calls, split 85 `complete_effect` and 15 `timeout_effect`; all 37 helper outputs have `ROOT`-qualified localisation reads and no other live-source assignments.
- The targeted `hoi4.reference_search` call remained pending and was terminated; the relevant offline wiki sections were read directly at the cited local paths, and their local SHA-256 hashes match the reference revisions above. No web wiki was used.

Source review cannot establish whether native decision tooltip evaluation executes, suppresses, or renders these effect writes as expected. The parent reports its source tests passing; this handoff does not claim native runtime rendering or UI validation.
