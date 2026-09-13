# Event 38 probability scenario manifest

## Use

These scenarios define the minimum named cases for the mandatory read-only baseline and post-patch comparison. The implementation agent may add scenarios when a weighted surface has distinct campaign states that are not represented here.

No scenario authorizes source changes by the probability auditor. Exact normalized probability requires the complete candidate pool and declared external factors.

## Route and focus scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P001` | opening focus AI | Malta at war, supply critical, Jerusalem held | survival and supply outrank political and relic content | exact or score-only depending on full focus pool |
| `E38-P002` | opening focus AI | Malta at war, supply secure, enemy weak | campaign preparation can outrank defensive focus, but logistics remains viable | comparison and sensitivity |
| `E38-P003` | government route | high Authority, low Cohesion, one dominant order | centralization preferred over confederation | score ordering |
| `E38-P004` | government route | moderate Authority, high Cohesion, four strong orders | confederation preferred and centralization remains possible only when valid | score ordering |
| `E38-P005` | Hospitaller route | high casualties, disease or famine active, weak industry | Hospitaller and Lazarite paths outrank Templar aggression | sweep over casualty and humanitarian pressure |
| `E38-P006` | Templar route | strong army, stable supply, low enemy strength, no active humanitarian crisis | Templar and siege paths rise without starving logistics | sweep over force ratio |
| `E38-P007` | Holy See route | Rome controlled and safe, valid Pope, high Legitimacy | Papal route becomes competitive | exact candidate comparison |
| `E38-P008` | Holy See route | Rome controlled but threatened, weak Malta | survival and defence outrank transformation | score ordering |
| `E38-P009` | Kingdom of God route | strong Holy See, large realm, high Legitimacy | route is rare but viable | bounded or sampled evidence |
| `E38-P010` | Eleventh Crusade route | Malta survives after expedition loss | survival, evacuation, transport, and feasible landing content dominates | focus and decision score ordering |

## Campaign and decision scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P011` | regional campaign target | Jerusalem corridor incomplete | connected Holy Land targets outrank distant North Africa | target score evaluation |
| `E38-P012` | regional campaign target | naval superiority, land fronts stalled, Cyprus valid | Cyprus and Aegean targets rise | sensitivity sweep |
| `E38-P013` | regional campaign target | no convoy margin and hostile navy | overseas targets approach zero | exact invalidation or strong penalty proof |
| `E38-P014` | campaign action | active severe supply deficit | depot, port, convoy, and repair actions outrank new offensive | decision score ordering |
| `E38-P015` | settlement choice | high resistance, weak administration, valid principality | charter or local restoration outranks direct integration | option or decision evaluation |
| `E38-P016` | settlement choice | compact strategic state, high compliance, strong Authority | direct commandery or integration becomes competitive | sensitivity sweep |
| `E38-P017` | council response | high Cohesion and affordable demand | accept or negotiate outranks refusal | option pool exact evaluation |
| `E38-P018` | council response | low Authority and unaffordable territorial demand | negotiation or refusal remains viable, acceptance does not bankrupt actor | bounded evaluation |
| `E38-P019` | demand selection | stable council with several active orders | no single demand family dominates and immediate repeat is prevented | complete random pool evaluation |
| `E38-P020` | demand selection | low Cohesion and dominant Templar order | stronger operational or land demand becomes more likely | sweep by Cohesion and influence |

## Evolution and relic scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P021` | Evolution I MTTH | 200 Chaos, successful Malta, orders active | paced around accepted band and not instant | timing evaluation |
| `E38-P022` | Evolution I MTTH | 200 Chaos, Malta near defeat | delayed without becoming permanently starved | sweep over survival state |
| `E38-P023` | Evolution II MTTH | 400 Chaos, stable conquests and high occupation burden | acceleration relative to weak or empty territorial proof | timing comparison |
| `E38-P024` | Evolution III MTTH | 600 Chaos, high Legitimacy and foreign support | viable within accepted band | timing evaluation |
| `E38-P025` | disabled evolution | qualifying world state but evolution disabled | zero activation and zero recorded-state side effects | exact gate proof |
| `E38-P026` | relic expedition target | secure Jerusalem route and known claim | secure target outranks inaccessible or invalid locations | target evaluation |
| `E38-P027` | relic result pool | high security and examination capacity | credible or disputed results rise, fraud remains possible | complete pool evaluation |
| `E38-P028` | relic result pool | foreign competition and poor security | theft, fraud, loss, or failure rise | sensitivity sweep |

## Principality scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P029` | charter AI | Malta overextended and Evolution II active | principality creation becomes likely in valid large region | decision evaluation |
| `E38-P030` | principality obligation | loyal subject under threat | relief and reduced levy can outrank coercion | decision score ordering |
| `E38-P031` | principality obligation | defiant strong subject, Malta strong | arbitration and enforcement are viable, immediate war is not automatic | option evaluation |
| `E38-P032` | succession | high local legitimacy and accepted heir | stable candidate dominates | complete candidate pool |
| `E38-P033` | succession | rival orders and foreign patron active | disputed candidates remain meaningful | sensitivity sweep |
| `E38-P034` | integration | high compliance, long loyalty, connected region | integration becomes viable after proof | exact gate plus score |
| `E38-P035` | independence | rebellious subject and weak Malta | autonomy or independence rises | score ordering |

## Hidden route scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P036` | Teutonic negotiation | all exact flags, viable Malta, Holy Realm, qualifying Germany | route candidate exists | exact gate proof |
| `E38-P037` | Teutonic negotiation | one required flag absent | route probability and availability are zero | exact invalidation |
| `E38-P038` | Teutonic assent | balanced relations and common enemies | acceptance is viable for all members | option evaluation |
| `E38-P039` | Teutonic assent | Germany losing badly and Malta weak | refusal or delay rises | sensitivity sweep |
| `E38-P040` | Atlantis AI choice | complete eligible pool, AI Germany | Atlantis exactly 90 percent and refusal 10 percent | exact normalized probability |
| `E38-P041` | Atlantis human choice | complete eligible pool, human Germany | no forced AI weight controls player choice | source and UI proof |
| `E38-P042` | Atlantis gate | alliance duration under two years or Germany not strongest | route probability and availability are zero | exact invalidation |
| `E38-P043` | Atlantis regional program | active war with Malta and Holy Realm, supply limited | nearby required programs outrank distant overseas campaigns | target evaluation |

## Holy World and manual scenario scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P044` | believer alignment | Papal-friendly Catholic government, high relations, low exposure | believer alignment high but not automatic without route proof | score evaluation |
| `E38-P045` | believer alignment | hostile secular major with threatened territory | nonbeliever alignment strongly preferred | score evaluation |
| `E38-P046` | believer alignment | dependent small subject under Papal protection | believer alignment high | sensitivity sweep |
| `E38-P047` | Holy World activation | 1000 Chaos, branch enabled, valid Pope, continent proof complete | activation candidate valid | exact gate proof |
| `E38-P048` | Holy World activation | same state but branch disabled | activation is zero without disabling parent event | exact invalidation |
| `E38-P049` | Holy World activation | 1000 Chaos but continent proof transient or incomplete | activation is zero | exact invalidation |
| `E38-P050` | terminal regional target | Europe secured, North Africa exposed, supply available | adjacent region opens before distant Pacific war | target ordering |
| `E38-P051` | terminal regional target | selected front lacks supply and another front is ready | ready front outranks stalled front | target sweep |
| `E38-P052` | manual Low side assignment | Low intensity | modest believer minority and several strong opposition centres | complete setup pool or sampled world evaluation |
| `E38-P053` | manual Medium side assignment | Medium intensity | stronger Mediterranean believer bloc with viable opposition | same evidence class as baseline |
| `E38-P054` | manual High side assignment | High intensity | several believer regions without opposition collapse | same evidence class as baseline |
| `E38-P055` | manual Maximum side assignment | Maximum intensity | believer advantage without automatic Papal victory | simulation with declared world pool |

## Unit and production scenarios

| Scenario ID | Surface | State | Required ordering or constraint | Expected evidence |
| --- | --- | --- | --- | --- |
| `E38-P056` | unit recruitment | low equipment and active siege war | affordable line forces and engineers outrank unavailable elite units | decision and template scoring |
| `E38-P057` | unit recruitment | high industry, high Legitimacy, Blessed cap available | one Blessed formation is viable without starving line reinforcement | score and cap proof |
| `E38-P058` | unit production | fuel shortage | fuel-heavy advanced carriers lose priority | research and production score sweep |
| `E38-P059` | unit production | fortified enemy and sufficient siege stock | siege equipment priority rises | production score evaluation |
| `E38-P060` | Atlantean Supreme replacement | twenty initial units lost, industry and technology inadequate | replacement unavailable or prohibitively low priority | exact gate and score proof |

## Comparison rule

Every source patch that affects a scenario above must carry the baseline scenario ID into its handoff. The final probability auditor must compare the same state, pool, external factors, and desired relationship. A changed candidate pool must be declared and can invalidate direct comparison.
