# Military Madness: Stacking and Lifecycle

## One record per package

A package keeps the occurrence it came from, its recipient identity, its stage, its start, its expiry, and every individual rolled statistic and magnitude.

The country has one combined Military Madness national spirit. That spirit presents the contributions of all active packages. Separate hidden carriers may be needed for compatible effect types, but they must not create a visible spirit for every roll or package.

There is no gameplay cap on simultaneous packages. The game must not discard an older package, merge away its expiry, or truncate the stored rolls because a display page is full.

Within a package, identical statistics remain separate draw records. Across packages, identical statistics remain separate timed contributions. The combined presentation can group them by statistic without losing either record.

## A worked overlap

On day 0, a country receives +200% land defense for 365 days.

On day 100, it receives a new package containing +300% land defense and two other independently drawn effects.

From day 100 until day 365, the two defense contributions total +500% where the supported calculation is additive and no technical bound is reached.

On day 365, the first package expires. The country keeps the second package's +300% defense and its other two effects.

On day 465, the second package expires. Nothing from either package remains.

A later package has no authority to renew the first package. Closing and reopening the country screen has no authority to change either date.

## Duplicate reductions

Suppose two rolls request reductions of 60% and 55% in the same consumption statistic. Their raw combined request is a 115% reduction.

That raw value must not be sent blindly into a calculation that requires a positive consumption amount. Both records remain intact, while the applied contribution stops at that calculation's certified limit.

When the 60% package expires, the remaining 55% contribution becomes the requested active reduction. The result is rebuilt from the surviving records. It is not recovered by subtracting 60 from a previously clamped number.

This distinction prevents permanent residue, sign reversal, negative costs, and early loss of surviving bonuses.

## Composition with other systems

Military Madness owns its own contributions. It does not overwrite national ideas, advisers, doctrines, technologies, difficulty modifiers, terrain rules, or another event's statistics.

Where safety depends on the total from several systems, the supported composition must be established before admission. A country can gain another reduction after Event 087 fires, so checking safety only at the instant of the roll is insufficient.

A self-referencing dynamic modifier that reads a partially evaluated total is not a safety guarantee. The production adapter must handle the engine's update ordering and distinguish its own contribution from external contributions without circular feedback.

Where a correct composition route cannot be proved, that binding remains blocked. A small hardcoded replacement pool is not an acceptable substitute for resolving the coverage gap.

## Expiry

Every package expires 365 elapsed game days after its recorded activation. This is a days-based duration, not nine months or an approximate calendar year.

Packages sharing an expiry can be processed together, but each package is removed independently. Cleanup is idempotent. A repeated expiry callback cannot remove surviving contributions.

The latest date in a country's active packages must never become the expiry date of its whole spirit. The spirit persists only while it has active contributions. Its visible summary identifies the next change in the active package set.

Disabling the random event or an evolution does not suspend cleanup. Ordinary settings prevent future firings. They do not make previously granted packages permanent.

## Military state at expiry

Expiry changes the temporary statistic through its supported native behavior. It does not delete divisions, destroy equipment, subtract earned experience, revoke acquired commanders, or reverse production completed during the package.

A capacity modifier can leave the country above its normal recruitment or deployment capacity after expiry. Native over-cap behavior applies. Military Madness does not invent a punitive disbandment action.

A maximum-organization change follows the verified native handling of current and maximum organization. Adding and removing the carrier cannot be used as an event-owned healing loop.

A consumption reduction ending can make an existing operation expensive. That is part of the strategic risk of the fixed deadline.

## Identity and political change

A change of ideology, ruling party, leader, subject status, or cosmetic tag does not create a new recipient. Its active packages remain.

A government in exile retains a package while it remains a valid country carrier. Its timer keeps running even when its forces or territory cannot use the result.

Annexation does not transfer packages to the annexer. An annexed identity cannot leave applied modifiers behind on another country.

A later release of the same tag is a new country lifetime. It does not recover an expired package, reset a timer, or collect an undelivered reward from before its destruction.

When a civil war creates a new country, automatic copying of ideas or variables must not duplicate Event 087 packages. The continuing original country keeps its valid records. The new country joins the next worldwide firing.

Cosmetic changes are therefore preserved, while a genuinely new country lifetime does not inherit a lottery ticket.

## Save and reload

Saved records preserve exact results and deadlines. Reloading does not draw again. Rebuilding a displayed total is permitted only from those same saved records.

Random outcomes are produced by synchronized gameplay randomness. Cosmetic sorting, opening the ledger, tooltips, and notification preferences do not consume that randomness.

In multiplayer, every peer uses the same compiled pool revision and the same synchronized occurrence. Separate players receiving a report are not separate worldwide firings.

The pool revision is part of provenance. Updating a pool does not change the meaning of a saved numeric entry or remap an old entry to whatever now occupies the same position.

## Compatibility changes

Compatible catalog additions affect future draws. Existing packages retain their recorded binding and interpretation.

A removed system or changed engine binding cannot be silently converted into a different reward during load. Migration must preserve the original meaning or report the precise unsupported save transition. There is no replacement draw.

When a temporary dependency becomes genuinely unavailable during a campaign, its adapter must define whether application is suspended or the save transition is unsupported. Suspension never pauses the package timer or replaces the roll.

## Legacy Event 087

The inspected existing event uses `chaosx.nr87.1`, grants a fixed entrenchment idea through a report option, and uses a nine-month duration. The new specification replaces that reward path.

The existing entry identity should remain stable unless a reviewed migration explicitly changes every reference. A padded filename is not evidence for changing the namespace to `chaosx.nr087`.

An old save's fixed entrenchment instance must not be mistaken for a new random package. The preservation policy is to let a genuinely identifiable legacy instance retain its existing remaining duration without granting a new reward, extending it, or copying it into the new package ledger.

Exact legacy timer visibility and civil-war copying still require installed-source verification. An unsupported old-save migration must be disclosed rather than repaired by guessed dates.

## Distribution failures

Pool validity and required bindings are checked before a worldwide occurrence commits. A missing required pool is a real blocker. The event must not deliver a complete package to one country and a silently reduced package to another because compilation was incomplete.

A country that ceases to exist before its queued delivery is skipped as no longer valid. That does not authorize compensating another country or changing the frozen tier.

Repeated delivery of the same occurrence to the same country lifetime is ignored. A genuinely new firing creates a genuinely new package, even if it occurs on the same day.
