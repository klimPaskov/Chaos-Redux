# Event 021 reference evidence

The live reference context, search and read routes were used for event and decision surfaces, with targeted reads supplementing the initial omitted sections.
Installed documentation is the primary syntax authority, with the offline wiki read in parallel.
No Paradox Wiki web request was made.
Full-file source checks are recorded separately and do not certify native argument semantics or live behavior.

## Installed game sources

Paths in this table are under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

| Source | Relevant lines read | SHA-256 revision |
| --- | --- | --- |
| `documentation/effects_documentation.md` | 1835-1843 opinion modifiers, 2244-2268 timed ideas, 2278-2292 array append, 4279-4295 array iteration, 5053-5077 news, 6496-6504 regular targets, 7691-7711 controller effects | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `documentation/triggers_documentation.md` | 2110-2135 variable comparison, 4941-4950 terrain, 5672-5685 array membership | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `documentation/script_concept_documentation.md` | 216-222 shared constants and their support boundary | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `common/script_constants/documentation.md` | 2-26 schema must be first and scoped fixed-point access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `common/decisions/_documentation.md` | 1-46 visibility and availability scopes and timing | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| `common/scripted_guis/_documentation.md` | 24-57 parent context and named click-effect binding | `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838` |
| `common/on_actions/_documentation.md` | 68-70 state-control callback declaration | `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4` |

The final validation documentation compilation reported revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
It is a compiled command-documentation revision, distinct from the individual file hashes above.
Its explicit country-scope news check left native argument blocks unchecked, so the variable, array and news sections were retrieved and reviewed directly.

Vanilla precedents inspected include `interface/decisions.gfx:1233-1234` and `2899-2900` for the two canonical decision icon references, `common/ideas/army_spirits.txt` for entrenchment and movement modifiers, and `common/opinion_modifiers/00_opinion_modifiers.txt` for monthly opinion decay.
The existing Event 021 category, mission, sponsor and date-wrapper patterns remain the integration precedent.
The console fixture syntax was checked in the installed console documentation at the `add_equipment`, `cp`, `eval_effect`, `event`, `manpower` and `xp` sections.
State-scope controller tests use the documented `set_state_controller_to`, not the country-scope `set_state_controller` command.

## Offline wiki sources

Paths in this table are under the repository's `paradox_wiki/` folder.

| Source | Relevant lines read | SHA-256 revision |
| --- | --- | --- |
| `Event modding - Hearts of Iron 4 Wiki.md` | 159-179 proportional option weights and modifier structure | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| `AI modding - Hearts of Iron 4 Wiki.md` | 31-37 option normalization and weight modifiers | `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818` |
| `Decision modding - Hearts of Iron 4 Wiki.md` | 308-332 custom cost text and tooltip variants, 441-464 hidden payment example | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `Effects - Hearts of Iron 4 Wiki.md` | 1241 opinion direction, 1980 timed idea duration | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `Triggers - Hearts of Iron 4 Wiki.md` | 651 country-only terrain query | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `On actions - Hearts of Iron 4 Wiki.md` | 450 new controller, old controller and changed-state scopes | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| `Data structures - Hearts of Iron 4 Wiki.md` | 263-278 event target types, 302-326 regular target lifetime, 1216 array-loop scope and mutation limits | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `Scopes - Hearts of Iron 4 Wiki.md` | 27-34 target limitations, 246-274 country, state, variable and event-target scopes | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `Localisation - Hearts of Iron 4 Wiki.md` | 195-214 sign-prefix and percentage formatting | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `Scripted GUI modding - Hearts of Iron 4 Wiki.md` | 38-72 independent container binding, 169-210 visibility and named click effects | `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30` |

The generic scripted GUI rules are also documented by the installed binding example and the already-linked Event Log source.
The shared hook edits change data selection rather than layout, and their missing matched visual evidence remains an open gate.
