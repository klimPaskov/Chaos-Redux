# Event 12 Africa achievement implementation prompt

Implement the Event 12 achievement package from `matrices/012_africa_achievement_matrix.csv` and `matrices/012_africa_achievement_matrix_notes.md` after the required gameplay routes exist.

## Authority

The matrix defines 44 achievement concepts with working keys, condition sets, disqualifiers, visibility, difficulty, tracking needs, icon direction, and design purpose. The expanded host, constitutional, and priority-member specifications provide the route facts those conditions must read.

Required supporting sources:

- `specs/012_africa_spec_part_7_host_country_playbooks.md`
- `specs/012_africa_spec_part_8_focus_route_deepening.md`
- `specs/012_africa_spec_part_9_priority_member_country_packages.md`
- `matrices/012_africa_host_country_playbook_matrix.csv`
- `matrices/012_africa_focus_route_payoff_matrix.csv`
- `matrices/012_africa_priority_member_package_matrix.csv`

Final titles and descriptions must be newly written localisation that follows the event writing rules. Do not copy working directions as final text.

## Implementation requirements

For each row:

- confirm the route, host proof, member package, or world-order mechanic exists
- register a stable achievement ID
- implement the exact unlock conditions and difficulty
- add persistent tracking for lifetime facts that cannot be inferred from the final state
- implement every disqualifier
- preserve the original Event 12 host and route commitment
- prevent incompatible route or tag-switch collection
- distinguish normal-play and forced-scenario eligibility
- add title and description localisation
- create completed, grey, and not-eligible 64x64 icons
- add interface wiring
- update documentation and the package disposition ledger
- record implemented, merged, queued, rejected, or superseded status

Do not weaken difficult conditions into automatic unlocks. Do not create one shallow achievement for every host or every restoration merely to increase the count. The 44-row matrix is the accepted package unless a later, reviewed design addendum changes it.

## Tracking rules

Track broken guarantees, coercive annexation, clause breaches, peaceful exits, voluntary returns, transport losses, historical restoration survival, negotiated union method, actor-rights clauses, high-chaos civilian targeting, continent sponsorship, terminal rival resolution, host proof completion, constitutional crisis outcomes, postwar constitutional review, and priority-member promotion when the final map cannot prove those facts.

Tracking must survive mechanic cleanup without leaving gameplay missions, selected targets, or temporary crisis flags active. Use dedicated achievement flags, counters, arrays, or documented helper effects.

## Origin and route rules

Preserve the original Event 12 host even after cosmetic changes, federation, integration, restoration, civil war, or formation of The World. Host-sensitive achievements must distinguish the 22 full host playbooks from compact signatures without making compact hosts ineligible by accident.

Constitutional achievements must verify the actual committed route and any lifetime breaches. A late cosmetic tag or postwar settlement cannot erase military emergency debt, coercive integration, abolished withdrawal rights, failed elections, broken crown guarantees, or confederal clause violations.

Restored-polity achievements must verify the correct Event 12 origin, package promotion, player control, and settlement method. Ordinary tag switching must not combine incompatible constitutional, restoration, or world-order achievements.

## Asset rules

Use the achievement icon direction in the matrix. Historical restoration motifs need source review. High-chaos and world-order icons may use generated fictional art. Final files belong directly under `gfx/achievements/` with exact registered IDs and the required grey and not-eligible variants.

Do not resize focus, idea, decision, host-overlay, or member-package icons into achievement icons.

## Validation

Test at least one valid and one invalid path for every achievement family. Test all lifetime disqualifiers that could be lost during cleanup. Confirm hidden achievements remain hidden, scenario restrictions work, tag switching cannot bypass origin, compact and full hosts are handled intentionally, route crises cannot be erased by late settlement, terminal achievements cannot coexist with an incompatible world-end state, and no row unlocks merely because Event 12 fired.

Return a route and host coverage table plus a disposition for all 44 rows. Report missing mechanics, missing icons, simplifications, and blocked conditions instead of claiming completion.
