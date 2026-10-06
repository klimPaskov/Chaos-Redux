# Event 021 regional responses

All helpers run in country scope and use `event021_regional_response` from `common/script_constants/021_random_civil_war_regional_constants.txt`.
They use the existing crisis category and bounded review, with no additional periodic hook.

`event021_contain_regional_exposure` lowers an existing exposure stage once, clamping at Observed.
Monitoring and mediation call it, and their existing timed recent flags prevent advancement while the response lasts.
Only the due branch of `event021_review_current_country` calls `event021_advance_regional_exposure`.
Unanswered live exposure advances one stage, with Mobilizing adding eight pressure points.
The nearby-conflict flag raises pressure and target weight while exposure is active and lasts another 180 days after cleanup.
Humanitarian pressure requires a source losing territory and no active civilian relief.

`event021_begin_campaign_adaptation` requires an enabled Evolution II and a live territorial war.
Its decision pays 15 army experience and 200 rifles first.
The helper sets a once-per-crisis flag and a pending report flag, then fires `chaosx.nr21_adaptation.1` once.
The three option helpers consume that pending flag and apply one 90-day idea.
Supply escorts exchange attack for lower supply use and recovery, defensive preparation exchanges movement for defense and entrenchment, and columns exchange defense for movement and planning.
Defense requires mountain or urban terrain in country scope, matching the installed `has_terrain` documentation.
The action changes neither country identity nor Event 006 package content.

`event021_mass_mobilization` follows adaptation only at Totalen Chaos or World Collapse.
The decision spends 1,500 rifles and 100 support equipment.
Its 60-day idea raises attack and organization by 10% and recruitable population by two percentage points, costing eight stability points and five percent consumer goods requirements.
Counting those two temporary sacrifices together with both equipment payments gives four cost types, with no extra command-power debit.
It leaves a memory that adds 12 to the government's eventual recurrence score.
An opposition side also writes this memory to its source government, so armed groups on either side affect that country's aftermath.
New crisis provenance clears the memory, while ordinary cleanup leaves it for recurrence evaluation.
Successor preparation copies the predecessor's memory before annexation, so changing the surviving government does not erase the aftermath.

`event021_expose_foreign_intervention` requires the government's exact live opposition-sponsor pointer.
Its decision spends 25 political power and 50 support equipment for investigators.
It ends the sponsor's paired commitment through the existing clearing helper, clears the government's intervention condition, and applies a negative opinion modifier from the sponsor toward the government.
Delivered equipment is retained, and the original intervention loss is not refunded.
There is no new random withdrawal roll or report.

One response slot opens after an existing primary order has been taken.
A live sponsor response takes priority, followed by campaign adaptation, high-chaos mobilization and communications.
The phase keeps at most six selectable actions, including the capital commitment card.
All new decisions show their complete resource cost and reuse existing decision and idea sprites.

`event021_cleanup_campaign_adaptation` removes the four temporary ideas and the adaptation, report, mobilization and sponsor-response flags.
It is called by crisis action reset, decision cleanup and annexation teardown.

Example: after reviewing command loyalty, an Evolution II government with enough resources selects Adapt the Campaign, pays once, and chooses guarded supply routes.
The report cannot grant a second specialization after its pending flag is consumed.

Future extension: use verified controlled rail routes to distinguish specialized rail warfare from the present general supply plan, if that creates a worthwhile tactical choice.
No additional action or country package is queued by this note.

## Popup budget

`event021_emit_multifront_news_once` records the crisis id in a durable global array before sending world news.
Successor governments therefore cannot repeat the same announcement.
Scenario-origin wars use the aggregate scenario presentation and skip per-target multifront news.
Their exposed neighbours see the normal category without per-target border popups.
Successful scenario openings record their crisis ids separately, preserving this rule even when an Event 006 or ordinary claimant inherits the government role.
Neighbour presentation records the source crisis id in the neighbour's own durable array before sending its report.
Exposure cleanup does not clear those identities, so a later front in the same war cannot repeat the border report.
The normal government chain has at most six presentations: opening, multifront news, optional strange incident, chosen adaptation, settlement and final verdict.
Sponsor counterplay adds no report.
