# 02. Influence, starting conditions, and commitment

## The score

The takeover threshold is 100 Influence. The opening score is between 0 and 45. Scores are independent for every participant-target pair. A sponsor's Influence in one country cannot be spent, transferred, or copied into another country. Rival losses do not automatically become the attacker's gains.

Influence represents the sponsor's ability to determine the target's foreign and domestic decisions. It is not identical to opinion, party popularity, intelligence network strength, economic output, or autonomy. Those values affect entry conditions and action outcomes while retaining their normal game meanings.

Use quarter-point output precision for action gains and losses. Show whole numbers when exact and at most two decimal places otherwise. Integer anchors in this specification follow the project's five-point tuning convention. Fractions produced by compatibility and saturation are calculated results, not separately tuned arbitrary values.

## Initial position

Start with 5 and add the following contributions. Apply family caps, then clamp the total to 0–45. Read all contributions from the same registration snapshot. No later periodic reseeding is allowed.

| Evidence family | Contribution | Family bound and interpretation |
| --- | --- | --- |
| Political compatibility | Same ruling ideology group +15. Sponsor's ideology has at least 50% popularity in the target +5. Verified compatible ruling subideology or party relationship +5. | Maximum +20. The same native popularity value is not counted again as a separate historical campaign. |
| Target's opinion of sponsor | At least +50 gives +10. +10 through +49 gives +5. -1 through -49 gives -5. At most -50 gives -10. Other values give 0. | One directional reading. Sponsor's own opinion is not a second bonus. |
| Diplomatic security ties | Same faction +10. Sponsor already guarantees target +5. | Maximum +15. Relations created by Event 79 opening do not exist and cannot qualify. |
| Economic connection | A verified current bilateral trade flow or an established paid economic cooperation record gives +5. | Maximum +5. A faction relation is not proof of bilateral trade. |
| Military cooperation | A verified current military mission, qualifying equipment assistance, attaché, or valid deployed volunteer cooperation gives +5. | Maximum +5. Military access alone is insufficient. |
| Existing political campaign | An independently recorded bilateral political influence program predating registration gives +5. | Maximum +5. Do not infer this solely from matching ideology or popularity. |
| Intelligence presence | Verified meaningful operational presence in the target gives +5. | Maximum +5. Use a documented provider threshold, proposed network strength 25 where that value exists. |
| Historical relationship | A sourced, date-valid relationship adapter can give +5 or -5. | Default 0. Contemporary diplomacy overrides a stale historical interpretation. |
| Active hostility | Direct war gives -15. Otherwise an active hostile war goal gives -10. Otherwise an active territorial claim or core dispute gives -5. | Use only the strongest penalty, not all three. |

Every nonzero contribution needs a visible reason in the expanded breakdown. Reasons can be combined for readability, but the displayed sum must match the authoritative seed. The 45 cap is stated openly.

The historical adapter must name its dates, evidence, and invalidation conditions. No permanent bonuses for a favorite major, continent, culture, or player status are permitted. This package supplies the adapter contract but approves no country-pair historical bonuses without completed evidence.

## Compatibility during the campaign

Compatibility is recalculated at positive action completion using the sponsor ideology pledged when that action started and the target's current political state. An ongoing action does not silently change the ideology it was promoting because the sponsor changes government halfway through it.

| Current target position toward the pledged ideology | Political compatibility C |
| --- | --- |
| Same ruling group and pledged ideology popularity at least 50% | 1.25 |
| Same ruling group, popularity below 50% | 1.00 |
| Different ruling group, pledged ideology popularity at least 25% | 0.75 |
| Different ruling group, popularity below 25% | 0.50 |

Political actions use C. Economic actions use the greater of C and 0.75. Military actions use the greater of C and 0.75 when the target has an active verified advisory relationship with that sponsor, otherwise C. This makes practical assistance possible across ideology without removing the political advantage of a friendly government.

An entrenched aligned sponsor can receive 2.5 times the political gain of a weak ideological outsider from the same anchor. The outsider can improve this situation through opposition support or propaganda. It can also use material assistance while building political support. It never needs a hidden permission flag to win.

## Repeated-action returns

For each sponsor-target pair, count successful completions from the same positive action family within the preceding 60 days. The first completion uses a saturation factor S of 1.00, the second 0.75, and later completions 0.50. Upgrading a propaganda decision or choosing a different subtype within that family does not reset the count. Cancelled actions grant no gain and do not count as successful completions.

Rolling windows include completions on the current day and exclude entries exactly 60 days old for saturation or exactly 30 days old for rival losses. This boundary is shared by tooltips and calculations.

The positive gain is:

`G = floor(4 × anchor × compatibility × saturation) / 4`

Apply this once at completion. The target's existing Influence is not multiplied. Keep positive scores capped at 100 once takeover is committed. Any overshoot is recorded for diagnostics but is not exportable to another target.

An optional incident-specific adjustment is listed in its incident definition and cannot introduce an undocumented multiplier. Most incidents affect popularity, eligibility, or project delivery directly, leaving the standard gain formula intact.

## Action capacity and cost disclosure

A sponsor can run one political campaign and one material campaign per target. Interference occupies the political slot. Across all targets the sponsor can run at most three active campaigns. Completed campaigns free their slot before a new one can begin. Selection dialogs and expanded rankings do not occupy slots.

The action card shows duration, main output, ideology or institution being supported, and current compatibility estimate. Its tooltip explains that the final political state may change the calculated gain before completion. Resource debit uses the confirmed cost quote, not a value calculated when the board was opened.

A campaign with a material delivery cannot award Influence until its required assets or funded work are delivered. If a building cannot be placed, the corresponding gain is withheld. If an equipment transfer cannot debit the donor and credit the target consistently, the action does not complete.
