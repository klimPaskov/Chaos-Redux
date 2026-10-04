# Generic activation AI cap score ordering

Disposition: source order corrected; matched MCP score and eligibility evidence remains partial.

The `generic_activate_detention_network` `ai_will_do` block starts at zero, adds wartime authoritarian or fascist willingness, then applies condemnation and losing-war factors.
Before this edit, its zero factor for an exceeded AI site cap appeared before those `add` modifiers, so a wartime over-cap actor could regain positive raw willingness.
The current decision places that zero factor last; separate `target_root_trigger` and `available` gates still require the AI site-cap predicate.
This is a source-order correction, not a new activation route, budget, or cost.

The exact pre-order decision source is archived at `generic_activation_weight_order_before_2026-09-27.txt`, SHA-256 `6d201ec4c075a3c321195e56322024845239d006a069edc59f6f195ee2d58601`.
The current `common/decisions/camp_repression_generic_decisions.txt` SHA-256 is `fe36f6e1081c3f01c6bc7de548d2050aa6697860a827a060610bb9e476eec7e1`.
A 34-group restricted source suite checks that the zero-cap factor follows both wartime additions and the other multipliers; it does not execute HOI4's AI selector.
Offline `Decision modding - Hearts of Iron 4 Wiki.md` lines 357–374, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, states that `add` and `factor` modifiers in an MTTH-style decision weight apply in source order.

The mandatory baseline `hoi4.probability_inspect` and evaluate ran before the edit at raw source SHA `6d201ec4c075a3c321195e56322024845239d006a069edc59f6f195ee2d58601`.
The four-scenario set `generic_activate_detention_network_cap_order_probe_v1` has hash `cb2c92c90307eb5578e1ebbcb1f2f4a1d9b75dea8004c14f7b710287348cefa0` and pairs neutral/fascist wartime AFG actors under or over a two-site cap, with exact quoted resources and the same synthetic `FROM=state:430` target.
The over-cap fixtures deliberately carry a stale `camp_ai_can_expand` flag while setting count three against cap two; they are invalid-state probes, not plausible live-controller examples.
The baseline [evaluation JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1d123cc6cef7d05ee704a6e87991f7748e530fea51343f7aebc7e3d0ef77fa7/d00e0dca62399573e001823924319f688d2f548c883ff56c8c27fde27d023180/probability-79996600479edc14819864e2.json) returned `PROBABILITY_ANALYZED_PARTIAL`, zero eligible, two excluded, two unresolved candidate rows and 51 unresolved items at MCP source revision `767d92041fd43d74e339c7148db6c4ae4da4c9ff64d0db39f4fd9eb15c31c0c9`.

The after [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc32708cbe32c5d2d66e4ac87f02ec2d9e048e574ced0c0deca48056cdfe725f/0e5b6db034592e50e7cbb516ebdc6304d530e1fb70a8213bfc6d38d379d29c00/probability-inspect-dc092dc65cfe.json) has source hash `dc092dc65cfede8523c8960f09f8bd5090bccdbe052aa55300e15b8c2767261c` and revision `7a2108ca092736e04d4f2a964d4f37b47542d1de594359c23ec7cf65eb177f1c`.
The [matched comparison JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bcfafb656a5d49c666ef77bd5842d599b3dd1149412bbd43b1be5b0c26b93be/dc1e1ae12c2c4af3f11d2f7ab492d10aadeae7ad2e89aa95082dc35f43791534/probability-6c7a7b739d3fc97d164a4bdf.json) used the same scenarios and candidate, returning `PROBABILITY_ANALYZED_PARTIAL`, zero eligible, two excluded, two unresolved and 51 unresolved items at revision `493968981c12a60ee093d33bdbff47df766f9eef30ac598de1f60883a518509a`.
Its [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/fafa615c81ca610bab20fa12b2edc08cd57dee0ac4ff0e62cabf79f3803094b8/probability-probability-6c7a7b739d3fc97d164a4bdf-comparison.svg) and [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5896e3ae2e4de4b4a8c83f6a96ba2df8d92b99bd11ace527f9e69fb8416e1112/f5df54a77c883686447e7ab739f8b19f405a7196e8dd7021e86a3b9e05790ce4/probability-probability-6c7a7b739d3fc97d164a4bdf-unresolved.svg) views did not resolve a numeric raw-score delta; the comparison reported zero modeled changes.
The adapter does not bind the typed cap helper, active-site count and target state sufficiently to establish route-valid AI eligibility or exact click probability.
