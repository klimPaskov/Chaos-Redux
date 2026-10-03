# Event 26 CXT registration boundary

Disposition: implemented, with native runtime validation pending.
Acceptance basis: the user's replacement AGENTS.md requires tag-scoped daily hooks to register carriers and mark pending work, with later package application controlled by player debug decisions.

`common/on_actions/026_black_friday_cxt_on_actions.txt` registers `chaosx_cxt_extension_event026_black_friday` through `black_friday_register_cxt_test_content`.
When daily registration discovers the carrier, it sets `chaosx_test_country_registered_sync_pending` rather than invoking the complete registered-content synchronizer.
Initial setup and **Apply Registered Systems** retain the authoritative application path in `common/scripted_effects/chaosx_test_country_effects.txt`.
The Event 26 initializer remains idempotent and does not launch the sale.

## Reference evidence

The live `hoi4.reference_context` decision request and targeted `hoi4.reference_search`/`hoi4.reference_read` routes returned both required source kinds.
The installed `common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, establishes decision refresh and target scopes.
The offline `Decision modding - Hearts of Iron 4 Wiki.md`, lines 284–336, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, establishes manual custom payment and its display/AI contract.
The installed `common/on_actions/_documentation.md`, lines 7–19, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`, lists `on_daily_TAG`.
The offline `On actions - Hearts of Iron 4 Wiki.md`, lines 91–132, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`, establishes that tag-specific daily effects run only for that existing country, and supplies the installed-style ENG startup precedent.
The repository application contract is `docs/testing/chaosx_test_country.md`, lines 87–105.
The context bundle omitted Localisation, so no localisation-reference coverage is claimed by this hook-only change.

## Validation and remaining work

The source call graph confirms daily registration cannot reach `chaosx_test_country_sync_registered_content` from this package hook.
The initial/manual consumer still dispatches the same carrier's `_apply` effect.
This closes the Event 26 periodic package-application mismatch, with live CXT delivery and broader Event 26 acceptance still unverified.
No art, payment, AI score, event lifecycle, or catalog status changed in this tranche.
