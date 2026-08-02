# Fallout NZL vanilla AI-plan retirement audit

Status: BLOCKED for gameplay patch. No AI strategy-plan file was changed.

Scope: original-tag `NZL` strategy plans only. The dormant Fallout Lifeboat State package remains dormant. This handoff owns the AI-plan compatibility question and does not authorize changes to activation, allocation, focus, decisions, events, characters, assets, localisation, workbook, Independence Wave, or global Fallout transition files.

## Decision

An additive retirement or abort patch cannot be proven engine-safe from the available contracts, so no gameplay edit was made.

The narrow gate that would be correct if the vanilla plan definitions could be extended is `fallout_nzl_lifeboat_package_is_current = yes`. It is generation-bound and package-bound. It is not a tag-only gate and is false for ordinary NZL. The two Fallout plans already use it in both `enable` and route-switch `abort` logic in `common/ai_strategy_plans/fallout_consolidated_ai.txt:25-181`.

The required compatibility behavior would be an additional abort disjunct on all four live vanilla plans:

```text
abort = {
    OR = {
        <existing vanilla abort conditions, if any>
        fallout_nzl_lifeboat_package_is_current = yes
    }
}
```

That behavior must not apply before the current-generation package is active and must not disable ordinary NZL AI.

## Engine and documentation proof

Required sources were read before this audit:

- Repository `AGENTS.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md` and `.agents/skills/chaos-redux-events/SKILL.md`.
- Offline wiki core pages: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.
- Installed official documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, and `modifiers_documentation.md`.
- Vanilla precedents: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy_plans/NZL_alternate_strategy_plan.txt` and `NZL_historical_strategy_plan.txt`.

The offline AI reference states that `allowed` is evaluated only at game start, `enable` is checked daily, and `abort` is checked daily and must be false for a plan to be picked (`paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:289-304`). This supports the intended current-generation abort gate.

The offline loading reference states that base files load before mods, same-filename files overwrite the base file, and duplicate entries in different files have file-specific behavior. It explicitly warns that duplicate handling varies by database type and may prefer the first or last definition (`paradox_wiki/Modding - Hearts of Iron 4 Wiki.md:243-271`, `:352`). It does not define additive field-level merging for `common/ai_strategy_plans`.

The read-only CWTools AI-plan schema reference lists `name` and `enable` as required fields while `abort` is optional. This is a syntax/schema reference, not proof of duplicate merge behavior. The installed official effects documentation exposes `add_ai_strategy` only as “Adds strategy entry to country AI” (`documentation/effects_documentation.md:741-749`). There is no documented `add_ai_strategy_plan`, `remove_ai_strategy_plan`, or runtime plan-abort effect.

Therefore neither of the possible additive-looking approaches is proven safe:

1. A same-ID block in a later, different filename could replace the whole plan, coexist as a duplicate, or merge fields. The official loading reference says this behavior varies by file. A minimal block containing only `abort` could consequently lose required `name`/`enable`/focus/research fields or leave two competing plan objects.
2. A same-filename replacement would replace the full vanilla file. It would require copying the complete current vanilla plan definitions, which is disallowed here because it freezes stale plan content and creates an update-drift surface.

No runtime plan-removal effect is documented, and HOI4 was not launched per task instruction. This is a blocker, not evidence that the intended abort expression is wrong.

## Country-package coverage checklist

| Surface | Finding | Evidence |
| --- | --- | --- |
| Tag registration | PASS for carrier | Fallout uses existing `NZL`; no new tag is introduced. `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_pilot_spec.md` identifies `NZL` as the existing carrier. |
| Current package identity | PASS for narrow gate | `common/scripted_triggers/fallout_consolidated_triggers.txt:66-78` requires `tag = NZL`, active package/focus flags, current transition generation, current assignment identity, and initialized values. |
| Vanilla AI compatibility | BLOCKED | Four vanilla plans remain live. Their original definitions are not safely extensible without a full-file override or unproven duplicate merge. |
| Fallout AI plans | PASS for dormant source | `common/ai_strategy_plans/fallout_consolidated_ai.txt:25-181` has exactly `fallout_nzl_humanitarian_plan` and `fallout_nzl_isolation_plan`, both enabled only by the current package and `fallout_nzl_ai_override`, with route/current-package aborts. |
| Activation | DORMANT by design | `common/scripted_effects/fallout_consolidated_effects.txt:522` defines `fallout_nzl_activate_lifeboat_package`; repository search finds no caller outside the definition. |
| Ordinary NZL behavior | PRESERVED | No tag-only, `original_tag`-only, or global Fallout abort was added. |

## Live plan inventory

Only the enabled mod `mod/chaos_redux.mod` is present in `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/dlc_load.json`. The repository contains no other NZL original-tag plans outside the Fallout plans. Vanilla contributes four original-tag plans:

| Plan id | Source | `allowed` | `enable` can be true for ordinary NZL | Existing `abort` | Fallout gate |
| --- | --- | --- | --- | --- | --- |
| `NZL_historical` | `common/ai_strategy_plans/NZL_historical_strategy_plan.txt:1-108` in vanilla | `original_tag = NZL`, Together for Victory | Historical default, random historical flag, democratic historical game rule, or `britain_enforced_our_loyalty` | `is_subject = no` (`:26-27`) | Missing |
| `NZL_alternate_democratic` | `common/ai_strategy_plans/NZL_alternate_strategy_plan.txt:1-106` in vanilla | `original_tag = NZL`, Together for Victory | Historical default, random democratic alternate flag, or democratic alternate game rule | Empty block (`:25-26`) | Missing |
| `NZL_alternate_fascist` | same vanilla file `:107-213` | `original_tag = NZL`, Together for Victory | Historical default, random fascist flag, or fascist game rule | Empty block (`:131-132`) | Missing |
| `NZL_alternate_communist` | same vanilla file `:214-316` | `original_tag = NZL`, Together for Victory | Historical default, random communist flag, or communist game rule | Empty block (`:238-239`) | Missing |
| `fallout_nzl_humanitarian_plan` | `common/ai_strategy_plans/fallout_consolidated_ai.txt:25-100` | `original_tag = NZL` | Only current package, override flag, and humanitarian route/partner/no-war conditions | Aborts on stale package or isolation route (`:43-48`) | Present |
| `fallout_nzl_isolation_plan` | `common/ai_strategy_plans/fallout_consolidated_ai.txt:102-181` | `original_tag = NZL` | Only current package, override flag, and isolation route/war/security conditions | Aborts on stale package or humanitarian route (`:122-127`) | Present |

The four vanilla plans are the complete live original-tag inventory for the currently enabled mod set. Workshop copies were not treated as live because they are not enabled by the local `dlc_load.json`.

## File-surface checklist and stale/missing surfaces

| Surface | Status | Concrete path / identifier |
| --- | --- | --- |
| Vanilla plan source | READ-ONLY reference | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy_plans/NZL_alternate_strategy_plan.txt`; `NZL_historical_strategy_plan.txt` |
| Mod Fallout plan source | Reviewed, no edit | `common/ai_strategy_plans/fallout_consolidated_ai.txt` |
| Narrow current-generation trigger | Reviewed, no edit | `common/scripted_triggers/fallout_consolidated_triggers.txt:66-78`, `fallout_nzl_lifeboat_package_is_current` |
| Activation caller | Missing by design | `fallout_nzl_activate_lifeboat_package` has definition only at `common/scripted_effects/fallout_consolidated_effects.txt:522`; no caller was added |
| Runtime plan-removal effect | Missing from documented engine surface | Official `effects_documentation.md` documents `add_ai_strategy` but no plan-removal counterpart |
| Additive duplicate-plan proof | Missing | No official plan-specific merge contract, no local precedent, and no HOI4 run permitted |
| Compatibility file | Intentionally absent | Creating a minimal duplicate-ID file would be an unproven and potentially destructive override |
| Global fallback gate | Correctly absent | No broad `tag = NZL`, `original_tag = NZL`, `fallout_active`, or `world_end` abort was introduced |

## Map, state, politics, and country package findings

These surfaces are outside this AI-only ownership and were not edited:

- Map/state assignment remains an activation blocker. The accepted package states are `284`, `1079`, `723`, `1080`, and `1081`, while Samoa state `726` and the Aotearoa overlap require current dispositions. Evidence: `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md` and `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_pilot_spec.md`.
- Politics and leaders are package-owned only after activation. `fallout_nzl_activate_lifeboat_package` sets the Lifeboat Parliament and democratic politics, but no caller exists. No party, leader, or character file was touched.
- Flags/cosmetic identities, advisors, portraits, ideas, decisions, focus tree, starting forces, technology, industry, supply, and production are all outside this narrow compatibility audit. Existing surfaces remain dormant behind `fallout_nzl_lifeboat_package_is_current`; the radio advisor asset and allocator/conflict receipts remain documented blockers in the current Fallout handoffs.
- The package's own two AI plans reference all route focus ids and advisor idea ids, but their activation is correctly impossible while the package is stale or absent.

## AI and playability conclusion

Before a future activation caller is added, the parent must choose one engine-proven compatibility path:

1. Maintain a synchronized full replacement of the two vanilla NZL plan files with the extra current-package abort disjuncts, accepting and documenting update drift. This is not permitted in this task because it copies stale whole-plan content.
2. Obtain an official or runtime-proven field-merge/plan-removal mechanism for duplicate AI-plan ids, then add only the narrow compatibility blocks.
3. Redesign the activation boundary so vanilla plan arbitration is not part of the package contract, with explicit design approval. This cannot be inferred here and would not be a fallback.

Until one path is accepted and proven, the package must remain dormant. The Fallout plans themselves must retain the existing generation-bound `enable`/`abort` conditions. Ordinary NZL AI must continue unchanged outside the current package identity.

## Validation and limits

Performed:

- Read the required repository guidance, skills, offline wiki pages, and official documentation.
- Enumerated all `original_tag = NZL` plan definitions in the enabled mod and installed vanilla files.
- Confirmed exactly four vanilla plans and two Fallout plans, with no duplicate NZL plan ids in the mod.
- Compared each vanilla `allowed`, `enable`, and `abort` block and confirmed the three alternate plans have empty abort blocks while historical aborts only on `is_subject = no`.
- Confirmed `fallout_nzl_lifeboat_package_is_current` is current-generation and package-bound, and confirmed the activation effect has no caller.
- Confirmed the local enabled-mod manifest contains only `mod/chaos_redux.mod`.
- Confirmed no gameplay file was edited.

Not performed:

- No HOI4 launch or `aiview` run, per task instruction.
- No live plan-arbitration observation.
- No assumptions were made about duplicate AI-plan merge order or field-level overlay.

## Parent follow-up

Keep this blocker handoff attached to the Fallout NZL package until an engine-safe compatibility path is proven. Do not approve an activation caller while the four vanilla plans can remain eligible. If a future patch chooses full vanilla-file replacement, recapture the current vanilla plan source and update all four plan blocks together, then re-audit against the package trigger and ordinary NZL continuation requirements.
