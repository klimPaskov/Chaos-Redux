---
name: chaos-redux-native-raids
description: Use when implementing or auditing native Hearts of Iron IV raid types, especially raid outcome dispatch, target validation, and native costs.
---

# Chaos Redux Native Raids

Use this skill for `common/raids/` definitions and effects launched by their `success_levels`.
Use `chaos-redux-events` for any event chain or log integration and `chaos-redux-decisions-missions` for a separate decision or mission surface.

## Read the engine contract

After the required `AGENTS.md` and offline wiki reading, inspect the installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md`, the relevant vanilla raid files, and the installed effects and triggers documentation for any helpers used.
Treat the installed documentation as the authority for native fields and scope, and retain the vanilla precedent used in the handoff.

## Scope and dispatch

- In raid preflight (`allowed`, `visible`, `show_target`, `available`, `launchable`, and AI selection), the evaluated scope is the actor country; `FROM` refers to the target country when applicable.
- In `success_levels`, both `actor_effects` and `victim_effects` begin in `RAID_INSTANCE` scope; their names organize outcome UI, not scope. Enter `var:actor_country`, `var:victim_country`, or `var:target_state` explicitly before country or state effects. `ROOT` remains the raid instance inside those nested blocks.
- If an existing country helper needs the actor country as `ROOT`, fire an immediate hidden actor `country_event` from `var:actor_country`. Save the necessary actor, victim, and target scopes as regular event targets in the originating chain before firing it. Regular event targets carry into events fired by that chain; temporary variables do not. Recheck the pointers in the receiving event before applying effects.
- For outcome dispatch across several raid types, use disjoint marker families with an exact-one selection check, or separate fixed hidden event IDs. Do not use one country or global pending scalar to identify a raid: concurrent raids can overwrite it.

## Cost and final gate

- Put equipment required to create a raid in native `essential_equipment`; the installed raid documentation says it is collected after creation. Put Command Power allocation in native `command_power`. Do not debit those resources again in scripted outcome effects or add a scripted refund for the same payment.
- At resolution, recheck the exact target and current policy that authorize the effect, including the actor, victim, state, and province where relevant. If the final gate can reject the effect, make the outcome tooltip conditional or neutral; do not promise an impact that may not occur.
- Do not promise cancellation refunds or resource recovery without verified engine behavior for that precise case.

## Evidence and handoff

Check every preflight and outcome branch against the source definition, call sites, event target lifecycle, native cost fields, tooltips, and a vanilla precedent. Use the available HOI4 MCP domain routes for any in-scope event or weighted behavior required by `AGENTS.md`, retaining scenario, revision, coverage, and unresolved findings; report an unavailable route precisely and do not substitute source review for engine evidence. Record any unverified runtime behavior as uncertainty for the parent and leave live-game validation to the user. Do not introduce a fallback or simplification without the required approval.
