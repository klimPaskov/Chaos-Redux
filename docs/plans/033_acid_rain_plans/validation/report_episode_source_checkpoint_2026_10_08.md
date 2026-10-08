# Event 033 report episode source checkpoint

Disposition: confirmed source defect, implementation unresolved.
The user's stored-fact and bounded-registry contract and accepted Part 9 require one severe impact report per country and episode, independent of other report classes.
This checkpoint does not accept a replacement ledger or a migration assumption.

The live `hoi4.source_lookup` returned the complete, unshadowed `acid_rain_send_severe_impact_report` definition at `common/scripted_effects/033_acid_rain_effects.txt:3379-3406`, workspace revision `3b390fb7f959e7370db5174396f1cfb22d7e6f9aa8d86bd46f5eeaf3473cd4fc`.
It compares the latest severe or superstorm report ID with the current episode using `less_than`.
After episode 3 reports, the first positive impact for an overlapping episode 2 cannot report, even if episode 2 has never reported to that country.
Separate monotonically increasing IDs for the two classes do not resolve out-of-order overlap within either class.
The current comments explicitly describe this suppression; it is not merely a localisation defect.

Installed `triggers_documentation.md:5672-5685`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, permits `is_in_array` in any scope and accepts a numeric element.
Offline `Data structures - Hearts of Iron 4 Wiki.md:1147`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents value equality membership, including variable inputs.
Installed `effects_documentation.md:2943-2967`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, requires country scope for `country_event` and documents delayed event dispatch.
These exact sections were read through `hoi4.reference_read`, not inferred from the context bundle.
The event context bundle omitted Data structures, Effects, Triggers, Scopes, On actions, Localisation and on-action documentation; the targeted reads above establish only their named report/array rules, not full system-reference coverage.

The repair must separately prove generation identity, bounded receipt storage, out-of-order first delivery, duplicate suppression, control-transfer ownership and reload behavior.
Old maximum-only IDs do not reveal every previously delivered episode, so migration cannot manufacture a complete history from them.
Real damage and protection facts and report navigation also remain part of the F7 implementation, while F6 opening source is held fixed for its independent comparison.
