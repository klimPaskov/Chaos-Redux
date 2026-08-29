# Event 023 technology and DLC integration notes

## Purpose

Event 23 begins with Soviet scientists completing a usable atomic arsenal. The implementation must make that premise mechanically true in the current installed version of Hearts of Iron IV without granting unrelated technology or creating a separate nuclear combat system.

This file defines the required result. Exact technology IDs, project IDs, equipment tokens, raid definitions, reactor buildings, delivery rules, and DLC branches must be verified during implementation.

## Minimum atomic capability

At opening, the Soviet Union must receive the minimum verified current-vanilla capability required to:

- Own the granted atomic bombs.
- Produce more atomic bombs through the current nuclear economy.
- Build or use current reactors when Event 23 grants reactor entitlements.
- Prepare and execute at least one current-vanilla nuclear delivery route.
- Expose the stockpile and capability correctly to shared nuclear systems.

This may require one or more verified technology, special-project, facility, resource, or country-state changes.

The event should grant only what the premise proves. It should not grant broad nuclear research bonuses, unrelated electronics, jet aircraft, rockets, thermonuclear weapons, missile systems, or every upstream technology when a narrower verified route exists.

## Existing Soviet progress

Before granting capability, inspect the current Soviet state.

Possible cases:

- The Soviet Union already has the full required atomic capability.
- It has some upstream research but lacks the final weapon project.
- It has the weapon capability but lacks a valid delivery force.
- It has reactors and production already.
- A separate event or mod system has granted an equivalent capability.

Event 23 should union the required missing capability with existing progress. It must not remove technology, reset project state, replace current stockpile, or erase player investment.

## Special-project route

If the installed game and enabled DLC use a special-project path for nuclear weapons:

- Inspect the current project database and facility requirements.
- Complete or grant the narrow atomic weapon result needed by Event 23.
- Preserve existing project history and unrelated project progress.
- Do not create a fake Event 23 project entry when the current system can record the verified vanilla result.
- Ensure later Event 23 production and delivery decisions detect the real completed capability.

If project completion normally creates a report or reward, avoid duplicating that reward unless the current engine requires it for capability state.

The implementation report should state exactly which vanilla project state was changed and why.

## Non-special-project route

If a supported configuration uses a direct technology route:

- Grant the exact required atomic technology or technologies.
- Preserve mutually exclusive technology branches.
- Avoid granting thermonuclear or missile technology.
- Verify that the stockpile and delivery route recognize the grant.

The route must be based on installed documentation and vanilla examples. Do not infer identifiers from old versions.

## Reactor handling

Event 23 uses cumulative free reactor entitlements at Evolutions I through IV.

Required behavior:

- Baseline grants no free reactor.
- Evolution I cumulative entitlement: 2.
- Evolution II cumulative entitlement: 4.
- Evolution III cumulative entitlement: 6.
- Evolution IV cumulative entitlement: 8.
- A queued entitlement can be placed only in a valid Soviet-owned and controlled state.
- A state in active combat, under transfer, or occupied is invalid.
- Site preference should favor secure interior states with infrastructure and defense.
- Placement should use the current verified reactor building or project route.
- Invalid placement does not convert into another building or reward.
- Annexation or reloading cannot duplicate an entitlement.

If the current nuclear system treats reactors through facility slots, special projects, or another mechanism, the implementation may adapt the entitlement to that verified surface while preserving the stated cumulative capacity and no-substitution rule.

## Bomb production

The opening and evolution grants are event-owned stockpile transactions.

Further development decisions should use current nuclear production rules where possible.

Required result:

- Reactors or the verified production source create nuclear progress.
- Device assembly consumes or commits that progress through the current system.
- The resulting bombs enter the authoritative operational stockpile.
- Event 23 does not maintain a second independent bomb count.
- Production respects Atomic Moratorium, storage capacity, and posture reserve caps.
- Existing stockpile from other sources remains usable and accounted.

If current vanilla exposes no script-safe way to convert production progress into a bounded Event 23 batch, the scripted-system architect should design a narrow adapter and document the exact limitation. No unrelated equipment should substitute for nuclear bombs.

## Delivery route

Event 23 must use at least one verified current-vanilla route.

Possible surfaces to inspect include:

- Strategic bomber nuclear strike rules.
- Nuclear raid definitions.
- Air superiority, range, and access requirements.
- Missile or rocket delivery when separately unlocked.
- DLC-specific raid or facility behavior.

The implementation must identify:

- Required technology or project.
- Required unit or equipment.
- Required mission, raid, or effect.
- Range and access.
- Fuel.
- Air state or interception conditions.
- Exact target-state contract.
- How the result reports success or failure.
- How the weapon is consumed.

Event 23 can prepare crews, reserve a weapon, and build an authorization chain. It cannot grant free delivery aircraft or ignore the current delivery consumer.

## Missile boundary

Event 32 remains the owner of Missiles.

- Event 23 does not grant missile technology or equipment.
- Event 23 can detect a verified missile delivery route from Event 32 or vanilla.
- Missile access can change range, preparation time, interception, and AI target selection.
- The normal Event 23 target and authorization contract still applies.
- The shared strike adapter still owns consequences.

## Thermonuclear boundary

Event 23 grants atomic weapons only.

A thermonuclear weapon can enter Event 23 targeting only when another verified system has granted:

- The necessary technology or project.
- A compatible weapon stockpile.
- A valid delivery route.

Event 23 should pass the correct weapon class to shared consequences. It should not treat Evolution III or IV as thermonuclear research.

## Technology graph audit

If implementation adds, changes, completes, or grants technology or project state, use the mandatory technology workflow:

1. `hoi4.tech_inspect` to identify prerequisites, folders, exclusivity, unlocks, grants, bonuses, references, and missing assets.
2. `hoi4.tech_render` for the affected folder, project family, or capability surface.
3. Implement the narrow change.
4. `hoi4.tech_compare` against the pre-change source.
5. Record the exact result in the Event 23 handoff.

The audit should prove that:

- Atomic capability is granted.
- Thermonuclear and missile capability are not granted.
- Existing Soviet progress is preserved.
- No mutually exclusive technology branch is broken.
- Required icons and localisation exist.
- The delivery route recognizes the capability.

## DLC compatibility matrix

Implementation should build a matrix from the current installed game.

| Configuration | Atomic capability route | Reactor route | Delivery route | Required Event 23 adaptation | Status |
| --- | --- | --- | --- | --- | --- |
| Base supported game without optional nuclear project DLC | Verify | Verify | Verify | Define only after inspection | Pending implementation audit |
| Supported game with current nuclear special-project DLC | Verify | Verify | Verify | Define only after inspection | Pending implementation audit |
| Missile capability absent | Atomic delivery only | Normal | Verified nonmissile route | Event 23 remains fully playable | Required |
| Missile capability present from vanilla or Event 32 | Existing atomic route plus missile | Normal | Missile adapter if verified | Add route choice, no free missile grant | Optional integration |
| Thermonuclear capability absent | Atomic only | Normal | Atomic route | Thermonuclear profiles hidden | Required |
| Thermonuclear capability present from another system | Atomic plus verified thermonuclear | Normal | Compatible route | Pass correct class to shared adapter | Optional integration |

Do not label an unverified branch as a fallback. Every supported branch needs a real vanilla or Chaos Redux precedent.

## Focus-tree hooks

Event 23 does not create a new Soviet focus tree.

After inspecting the current Soviet tree, implementation may add narrow hooks when an existing focus clearly represents:

- Nuclear research.
- Reactor construction.
- Strategic bomber preparation.
- Rocket or missile development.
- Civil defense.
- Scientific institutions.
- Command centralization.

A hook can:

- Bypass an already completed requirement.
- Discount an Event 23 decision.
- Improve a test or command outcome.
- Add a reactor entitlement only if the specification and balance audit accept it.
- Unlock a verified delivery route sooner.

A hook cannot replace a focus reward, create a new route family, or make Event 23 inaccessible to a Soviet player who chose another valid route.

Any focus change requires focus inspection, rendering, layout review, filters, navigation, AI, and comparison through the focus-tree workflow.

## Technology and DLC acceptance

Completion evidence should include:

- Exact installed documentation and vanilla references used.
- Current atomic technology or project IDs.
- Exact reactor consumer.
- Exact delivery route.
- DLC conditions.
- Preexisting Soviet progress cases.
- Technology inspect, render, and compare evidence when touched.
- A successful baseline opening in every supported configuration.
- A successful test and combat strike through each supported delivery route.
- Confirmation that missile and thermonuclear capability are not granted by Event 23.
- Any unsupported configuration listed as a blocker with the exact reason.
