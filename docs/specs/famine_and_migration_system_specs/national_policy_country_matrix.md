# National policy country initialization matrix

This matrix records which tags exist through state ownership at the vanilla 1936 and 1939 bookmarks and which starting policy profile the current Chaos Redux initialization assigns. The bookmark country-selection entries are a curated list of playable selections; they are not the country-existence inventory used here.

## Country tag inventory

The base-game bookmark files are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/bookmarks/the_gathering_storm.txt` (`1936.1.1.12`) and `.../common/bookmarks/blitzkrieg.txt` (`1939.8.14.12`). I parsed all 1,081 vanilla `history/states/*.txt` files with a Clausewitz-aware block parser, taking each state’s base `history.owner` and applying its dated `owner` entries through the respective bookmark date. The mod has no `history/states` directory; its `map/buildings.txt` is a buildings override and does not replace state ownership. All 91 tags in the union resolve to a vanilla country-tag definition.

| Tag | 1936 owner | 1939 owner | Starting profile |
| --- | --- | --- | --- |
| `AFA` | yes | no | [DEFAULT](#profile-default) |
| `AFG` | yes | yes | [DEFAULT](#profile-default) |
| `ALB` | yes | no | [DEFAULT](#profile-default) |
| `ARG` | yes | yes | [DEFAULT](#profile-default) |
| `AST` | yes | yes | [DEFAULT](#profile-default) |
| `AUS` | yes | no | [DEFAULT](#profile-default) |
| `BEL` | yes | yes | [DEFAULT](#profile-default) |
| `BHU` | yes | yes | [DEFAULT](#profile-default) |
| `BOL` | yes | yes | [DEFAULT](#profile-default) |
| `BRA` | yes | yes | [DEFAULT](#profile-default) |
| `BRM` | yes | yes | [DEFAULT](#profile-default) |
| `BUL` | yes | yes | [DEFAULT](#profile-default) |
| `CAN` | yes | yes | [DEFAULT](#profile-default) |
| `CHI` | yes | yes | [DEFAULT](#profile-default) |
| `CHL` | yes | yes | [DEFAULT](#profile-default) |
| `COL` | yes | yes | [DEFAULT](#profile-default) |
| `COS` | yes | yes | [DEFAULT](#profile-default) |
| `CUB` | yes | yes | [DEFAULT](#profile-default) |
| `CZE` | yes | no | [DEFAULT](#profile-default) |
| `DEN` | yes | yes | [DEFAULT](#profile-default) |
| `DOM` | yes | yes | [DEFAULT](#profile-default) |
| `ECU` | yes | yes | [DEFAULT](#profile-default) |
| `ELS` | yes | yes | [DEFAULT](#profile-default) |
| `ENG` | yes | yes | [DEFAULT](#profile-default) |
| `EST` | yes | yes | [DEFAULT](#profile-default) |
| `ETH` | yes | no | [DEFAULT](#profile-default) |
| `FIN` | yes | yes | [DEFAULT](#profile-default) |
| `FRA` | yes | yes | [DEFAULT](#profile-default) |
| `GER` | yes | yes | [GER](#profile-ger) |
| `GRE` | yes | yes | [DEFAULT](#profile-default) |
| `GUA` | yes | yes | [DEFAULT](#profile-default) |
| `GXC` | yes | yes | [DEFAULT](#profile-default) |
| `HAI` | yes | yes | [DEFAULT](#profile-default) |
| `HOL` | yes | yes | [DEFAULT](#profile-default) |
| `HON` | yes | yes | [DEFAULT](#profile-default) |
| `HUN` | yes | yes | [DEFAULT](#profile-default) |
| `ICE` | yes | yes | [DEFAULT](#profile-default) |
| `INS` | yes | yes | [DEFAULT](#profile-default) |
| `IRE` | yes | yes | [DEFAULT](#profile-default) |
| `IRQ` | yes | yes | [DEFAULT](#profile-default) |
| `ITA` | yes | yes | [ITA](#profile-ita) |
| `JAP` | yes | yes | [JAP](#profile-jap) |
| `JOR` | yes | yes | [DEFAULT](#profile-default) |
| `KUW` | yes | yes | [DEFAULT](#profile-default) |
| `LAT` | yes | yes | [DEFAULT](#profile-default) |
| `LEB` | yes | yes | [DEFAULT](#profile-default) |
| `LIB` | yes | yes | [DEFAULT](#profile-default) |
| `LIT` | yes | yes | [DEFAULT](#profile-default) |
| `LUX` | yes | yes | [DEFAULT](#profile-default) |
| `MAL` | yes | yes | [DEFAULT](#profile-default) |
| `MAN` | yes | yes | [DEFAULT](#profile-default) |
| `MEN` | yes | yes | [DEFAULT](#profile-default) |
| `MEX` | yes | yes | [DEFAULT](#profile-default) |
| `MON` | yes | yes | [DEFAULT](#profile-default) |
| `NEP` | yes | yes | [DEFAULT](#profile-default) |
| `NIC` | yes | yes | [DEFAULT](#profile-default) |
| `NOR` | yes | yes | [DEFAULT](#profile-default) |
| `NZL` | yes | yes | [DEFAULT](#profile-default) |
| `OMA` | yes | yes | [DEFAULT](#profile-default) |
| `PAL` | yes | yes | [DEFAULT](#profile-default) |
| `PAN` | yes | yes | [DEFAULT](#profile-default) |
| `PAR` | yes | yes | [DEFAULT](#profile-default) |
| `PER` | yes | yes | [DEFAULT](#profile-default) |
| `PHI` | yes | yes | [DEFAULT](#profile-default) |
| `POL` | yes | yes | [DEFAULT](#profile-default) |
| `POR` | yes | yes | [DEFAULT](#profile-default) |
| `PRC` | yes | yes | [DEFAULT](#profile-default) |
| `PRU` | yes | yes | [DEFAULT](#profile-default) |
| `RAJ` | yes | yes | [DEFAULT](#profile-default) |
| `ROM` | yes | yes | [DEFAULT](#profile-default) |
| `SAF` | yes | yes | [DEFAULT](#profile-default) |
| `SAU` | yes | yes | [DEFAULT](#profile-default) |
| `SHX` | yes | no | [DEFAULT](#profile-default) |
| `SIA` | yes | yes | [DEFAULT](#profile-default) |
| `SIK` | yes | yes | [DEFAULT](#profile-default) |
| `SLO` | no | yes | [DEFAULT](#profile-default) |
| `SOV` | yes | yes | [SOV](#profile-sov) |
| `SPR` | yes | yes | [DEFAULT](#profile-default) |
| `SWE` | yes | yes | [DEFAULT](#profile-default) |
| `SWI` | yes | yes | [DEFAULT](#profile-default) |
| `SYR` | yes | yes | [DEFAULT](#profile-default) |
| `TAN` | yes | yes | [DEFAULT](#profile-default) |
| `TIB` | yes | yes | [DEFAULT](#profile-default) |
| `TUR` | yes | yes | [DEFAULT](#profile-default) |
| `URG` | yes | yes | [DEFAULT](#profile-default) |
| `USA` | yes | yes | [DEFAULT](#profile-default) |
| `VEN` | yes | yes | [DEFAULT](#profile-default) |
| `XSM` | yes | yes | [DEFAULT](#profile-default) |
| `YEM` | yes | yes | [DEFAULT](#profile-default) |
| `YUG` | yes | yes | [DEFAULT](#profile-default) |
| `YUN` | yes | yes | [DEFAULT](#profile-default) |

There are 90 state-owning tags on 1 January 1936 and 85 on 14 August 1939. The tags that cease to own a state by the 1939 bookmark are `AFA`, `ALB`, `AUS`, `CZE`, `ETH`, and `SHX`; `SLO` first owns states by 1939. The state-history ownership changes explaining those tag differences are:

| Tag movement | State ids and 1939 owner |
| --- | --- |
| `AFA` disappears | `908` → ITA |
| `ALB` disappears | `44`, `805`, `934` → ITA |
| `AUS` disappears | `4`, `152`, `153`, `848`, `975`, `976` → GER |
| `CZE` disappears | `9`, `69`, `74`, `75`, `972` → GER; `664`, `73` → HUN; `72` → POL; `70`, `71` → SLO |
| `ETH` disappears | `271`, `835`–`843` → ITA |
| `SHX` disappears | `615`, `621`, `746` → PRC |
| `SLO` appears | `70`, `71` transferred from CZE |

These are date-specific map outcomes, not invented countries. The procedure deliberately derives the list from state owners rather than treating tags absent from the bookmark’s selectable-country list as nonexistent.

## Audit coverage and file surfaces

| Country-package surface | Coverage |
| --- | --- |
| Actual starting tags and tag definitions | Covered from dated state owners; all tags resolve to vanilla definitions. |
| Native policy categories, ideas, defaults, eligibility, and reconciliation | Covered in `common/idea_tags/national_policy_categories.txt`, `common/ideas/national_policy_laws.txt`, `common/scripted_effects/national_policy_effects.txt`, and `common/scripted_triggers/national_policy_triggers.txt`. |
| Setup, release, civil-war, puppet, and state-control lifecycle | Covered in `common/on_actions/human_system_boundaries_on_actions.txt`; CXT registration separately in `common/on_actions/national_policy_cxt_on_actions.txt` and `common/ideas/national_policy_cxt_extension_ideas.txt`. |
| Country-tag alias interaction | Read `common/country_tag_aliases/tag_aliases.txt`; exact profile conditions do not infer Japan’s laws from overlord status. |
| Map/state ownership | Parsed base-game `history/states/*.txt`; confirmed the mod has no `history/states` override folder. No map edit was needed. |
| Leaders, portraits, flags, parties, focus trees, ordinary decisions, military/equipment setup, and country balance | Outside this bounded policy-initialization audit; no such surface was changed by the policy feature review here. |

## Starting policy profiles

Every listed country meets the current source eligibility conditions at setup: the civilian laws are gated by `uses_normal_civilian_systems` and `NOT = { is_special_chaos_country = yes }`; the warfare laws are gated by `cbrn_action_actor_is_valid`, which currently checks that the country exists. The default profile is the code path for every listed tag without a named override. Nuclear law is a prospective game-policy setting and makes no historical claim.

| Profile | Reception | Departure | Chemical use | Biological use | Nuclear use | Basis, interpretation, and confidence |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="profile-default"></a>`DEFAULT` | Controlled Admission | Free Departure | Retaliation | Retaliation | None | Explicit user rule. High confidence for code assignment; this is a broad game default, not a claim that each country had these exact laws. |
| <a id="profile-ger"></a>`GER` | Controlled Admission | Departure Permit | Retaliation | Retaliation | None | Explicit user override. USHMM documents emigration encouraged until 1941 alongside targeted barriers, and the Évian conference shows controlled admission rather than universally open refuge; the permit level is a game abstraction, not a blanket exit-ban claim. Medium historical fit; high assignment confidence. |
| <a id="profile-sov"></a>`SOV` | Controlled Admission | Departure Permit | Retaliation | Retaliation | None | Explicit user override. The Soviet internal-passport system supports a controlled-movement abstraction, not a claim of a total external-departure ban. Medium historical fit; high assignment confidence. |
| <a id="profile-ita"></a>`ITA` | Controlled Admission | Free Departure | Unrestricted | Retaliation | None | Explicit user rule for chemical use in both bookmarks; the 1939 application is an inference authorized by the user. ICRC documents Italian chemical warfare in Ethiopia during 1935–36. This maps recorded use to an unrestricted law as a game abstraction; it does not equate treaty membership with possession or claim all methods were unrestricted. Medium historical fit; high assignment confidence. |
| <a id="profile-jap"></a>`JAP` | Controlled Admission | Free Departure | Unrestricted | Unrestricted | Unrestricted | Explicit user override for all three warfare laws in both bookmarks. This is a prospective design choice, not a historical claim. High assignment confidence. |

**Historical source notes:** [UN Treaty Collection, 1925 Geneva Protocol](https://treaties.un.org/pages/showdetails.aspx?objid=0800000280167ca8); [OPCW, History](https://www.opcw.org/about-us/history); [ICRC, Italian chemical warfare in Ethiopia](https://international-review.icrc.org/articles/force-versus-law-international-committee-red-cross-and-chemical-warfare-italo-ethiopian); [USHMM, German Jewish refugees, 1933–1939](https://encyclopedia.ushmm.org/content/en/article/german-jewish-refugees-1933-1939); [USHMM, The Évian Conference](https://encyclopedia.ushmm.org/content/en/article/the-evian-conference); [US State Department, Argentina’s 1938 selective immigration rule](https://history.state.gov/historicaldocuments/frus1938v01/d762); [Turkey’s 1934 Settlement Law](https://www.refworld.org/legal/legislation/natlegbod/1934/55668). Mexico’s selective Spanish asylum and the Dominican Republic’s conditional 100,000-person offer (not a realized 1938 capacity; agreement in 1940) are additional reasons to avoid treating the `DEFAULT` reception label as a universal historical description. The user supplied these research leads and the profile decisions; they were not independently re-researched for this audit.

`MAN` (Manchukuo) and `MEN` (Mengjiang) map to `DEFAULT`; the Japan profile is an exact `tag = JAP` condition and is not inherited through overlord status. No Japanese nuclear authorization is copied to them. All other tags also retain `DEFAULT` unless explicitly named above.

## Initialization and lifecycle audit

| Surface | Source behavior | Audit result |
| --- | --- | --- |
| Five law groups | `common/ideas/national_policy_laws.txt` defines reception, departure, chemical, biological, and nuclear categories. Each group has the intended default law; every selectable law allows civil-war survival. | Coverage matches all five specified groups. |
| Startup initialization | `common/on_actions/human_system_boundaries_on_actions.txt` runs one `on_startup` pass from GER scope over `every_country`, calling `national_policy_apply_starting_profile`. That initializes defaults, applies the exact GER/SOV/JAP/ITA overrides, reconciles compatibility variables, and marks the profile applied. | One-time all-country setup; no new recurring world-country scan. MCP reference for `on_startup` says it runs after country selection with no default country scope, so explicit GER scope is material. |
| `on_add` write path | Each law’s `on_add` publishes its corresponding policy value. Startup sets `national_policy_initializing`; the reconciler then writes the same law-derived values and combined compatibility views. | The initialization path performs idempotent same-value publication through `on_add` and reconciliation. The initializing flag suppresses the ordinary change response. No conflicting policy write found. |
| Civil war | `allowed_civil_war = { always = yes }` is set on each of the five families. `on_government_change` calls initializer/reconcile, which preserves any law already present and only supplies missing groups. | Current laws are source-configured to survive both civil-war sides; this callback does not reapply the campaign-start profile to a successor. Engine-side inheritance remains unobserved. |
| Newly released or liberated country | `on_release_as_free`, `on_release_as_puppet`, and `on_liberate` call `national_policy_initialize_released_country`, which removes all five families, clears the applied-profile receipt, and runs the normal default/profile initializer. | No copied retaliation rights survive this explicit release boundary; the new tag receives a default law set, plus a special profile only if its exact tag is GER, SOV, JAP, or ITA. |
| Generic puppet and ownership changes | `on_puppet` and `on_state_control_changed` call the non-destructive initializer; existing laws remain. | Does not overwrite a current policy. Release callbacks are the reset path for new independent tags. |
| CXT | `national_policy_cxt_extension` is a modifier-free hidden-idea registration token. Startup registers its setup effect through GER; `on_daily_CXT` repeats registration and marks sync pending only when newly registered. The player-triggered CXT extension initializes defaults; unrestricted warfare is a separate explicit fixture action. | Test-country path is separate from the bookmark matrix. It does not create a daily grant hook or alter other countries. |
| Human-system civilian eligibility and cleanup | Civilian law visibility/availability uses the normal-civilian trigger and excludes special Chaos countries. Existing human-boundary callbacks invoke nonhuman cleanup on release, puppet, government, and state-control transitions. | **Historical finding, resolved by the accepted adapter:** the initial audit found that the Holy Realm is a humanitarian-valid special country excluded from ordinary civilian laws, while its Event 003 actions depended on policy variables that reconciliation cleared. The accepted narrow adapter preserves its existing action eligibility and maps those requests to native laws without adding it to the shared law UI. The initial finding and its source context are retained below; corrected source tests now cover the exception. |
| Holy Realm adapter after correction | The exact Event 003 refuge actions use the explicit special-country adapter; the Holy Realm remains excluded from the shared civilian-law UI. | The corrected maintained law suite covers all three actual Event 003 helpers, both callback orders, all 21 valid reception/departure request pairs, atomic rejection of unsupported or excluded requests, and no scripted payment. This is current source-fixture evidence; native callback execution remains unobserved. |
| Tag aliases | `common/country_tag_aliases/tag_aliases.txt` defines succession/civil-war aliases for SOV and ITA, among other countries. | They do not automatically copy a starting profile. Civil-war successors should preserve laws via `allowed_civil_war`; independent releases take the reset/default path. No JAP/MAN/MEN alias-based exception was found. |

## Validation and limits

The connected reference workflow succeeded for the installed `add_ideas` documentation and offline wiki sections on idea implementation, `on_startup`, and civil-war idea survival. The wiki confirms that `on_add` does not run when an idea is granted by history/bookmark setup, and that `allowed_civil_war` defaults to false; the current policy laws avoid those pitfalls by adding laws in the startup effect and explicitly enabling civil-war retention. Source lookup returned the current `national_policy_apply_starting_profile` definition at `common/scripted_effects/national_policy_effects.txt:222–244` (workspace revision `a14aa631fc1169e5677f1fa8b39ec07bc33eb70fb196b0e7bf37f8382a4636a2`).

The initial `.tmp/national_policy_panels/laws_test_results.json` snapshot records 18 named profile cases and 132 ordered law transitions, including release reset, civil-war preservation, generic special/nonhuman civilian exclusion, CXT, and Japan’s profile. Its initial suite did not cover the Holy Realm exception. The corrected maintained `.tools/tests/test_national_policy_laws.py` suite now covers that adapter in both callback orders and all 21 valid request pairs; it remains a source fixture, not native callback execution. A read-only audit of all 19 `ai_will_do` law blocks found no definite weighting defect; the source-derived scores are conditional AI scores, not selection probabilities. `hoi4.probability_inspect` reported no weighted-surface adapter for law ideas, so no MCP score trace or simulation was available. No live game was run. The targeted map lookup completed against a 1,081-state map catalog but did not provide date-specific ownership evidence; the country/date inventory above comes from the direct state-history parser.

The initial audit found a material Holy Realm policy-adapter gap. The later accepted source change supplies the Event 003 adapter, and the corrected law fixture covers all three actual actions, both callback orders, and all 21 valid request pairs; there is no remaining Holy Realm source defect in this matrix. Native callback order is still not engine-observed. Historical confidence is intentionally limited to the named researched contexts; the default profile remains an explicit game rule rather than a country-by-country historical conclusion. No gameplay source was changed by the original read-only audit.
