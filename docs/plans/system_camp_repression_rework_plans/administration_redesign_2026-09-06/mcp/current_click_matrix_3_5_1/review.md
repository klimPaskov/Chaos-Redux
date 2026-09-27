# Current GUI scenario review

This is a review of declared layout scenarios over the real current Chaos Redux source using installed MCP 3.5.1.
It does not establish a campaign state, native click execution, tooltip popup behavior, payment, or delayed engine receipts.
Original full images and MCP metadata remain unchanged; the archive manifest maps each original artifact to its saved file.
The derived click crops are viewing aids; cyan debug labels may extend beyond the cropped panel.

| Case | Reviewed images | Observation |
| --- | --- | --- |
| 01 | Native crop and full click overlay | Active shortage panel fits its window; both shortage actions have separate hit rectangles; labels are legible. |
| 02 | Native crop and full click overlay | Administration panel and three selectors fit; country actions have no active hit rectangles under the declared fixture. |
| 03 | Native crop and cropped click overlay | Only the economic-priority selector is visually hovered; its hit rectangle matches its face; no tooltip popup is modeled. |
| 04 | Native crop and cropped click overlay | Shortage view remains legible; the fixture labels the second action “Projects Deferred” while its hit rectangle is active. This records the rendered fixture and is not an availability acceptance claim. |
| 05 | Native crop and cropped click overlay | Explicit paused/locked fixture suppresses the second shortage action's hit rectangle while retaining its legible label; the spending action stays active. |
| 06 | Native crop and cropped click overlay | Active shortage layout at 125% scale fits the window and both action faces have separate hit rectangles. |
| 07 | Native crop and cropped click overlay | Administration at 125% scale keeps legible headings, aligned selectors and contained country-action faces; their active availability is not established by this fixture. |
| 08 | Native crop and cropped click overlay | The 125% priority hover affects only that selector; no label overflow or active-region overlap is visible. |
| 09 | Native crop and cropped click overlay | The 125% shortage view matches the declared fixture; both controls are active despite the second label saying “Projects Deferred”, as in case 04. No campaign availability is inferred. |
| 10 | Native crop and cropped click overlay | The explicit 125% paused fixture removes the second action's hit region and leaves the spending action active; all labels fit. |
| 11 | Native crop and cropped click overlay | The 1920×1080, 100% active-shortage view is contained and legible with distinct spending and pause hit regions. |
| 12 | Native crop and cropped click overlay | The 1920×1080, 100% Administration view has aligned selectors and unobstructed country-action faces; the fixture does not establish their active availability. |
| 13 | Native crop and cropped click overlay | Priority hover at 1920×1080, 100% affects one selector and preserves its face/hit alignment. |
| 14 | Native crop and cropped click overlay | Legacy shortage fixture at 1920×1080, 100% has the same declared label/active-region ambiguity as cases 04 and 09; there is no overflow or region intersection. |
| 15 | Native crop and cropped click overlay | Explicit paused state at 1920×1080, 100% preserves the label and removes its hit region; the spending action remains active. |
| 16 | Native crop and cropped click overlay | Long-name/large-number Locations view fits, with six visible bottom-scroll rows and four distinct action faces. The requested Change Purpose hover renders disabled (`scripted_enabled_false`), and the bottom actions have no active hit regions; this case does not prove active-action hover or availability. |
| 17 | Native crop and cropped click overlay | Empty Labor Assignments view displays one clear empty-state message; only tabs, close and the filter have active regions. |
| 18 | Native crop and cropped click overlay | Empty-state filter hover is visible on that filter alone and its hit rectangle matches the face; the empty view contains no stale selected-site controls. |
| 19 | Native crop and cropped click overlay | Empty-custody panel keeps all zero values and lock labels legible; only the navigation, filter and single roster row have active regions. |
| 20 | Native crop and cropped click overlay | Requested hover on the explicitly locked-empty work control remains disabled. The native crop, cropped click overlay and normalized control geometry are identical to case 19; this is disabled-state evidence, not active-hover coverage. |
| 21 | Native crop and cropped click overlay | Closed-site message and four locked action faces are legible and have no active action regions. The legacy fixture retains 100% support and a capacity value, so its declared numbers are not accepted as an engine-consistent closed-site state. |
| 22 | Native crop and cropped click overlay | Long-name/large-number Locations view fits at 125%, including six bottom-scroll rows and four distinct action faces. Change Purpose remains disabled rather than hovered, with the same missing selected-state binding as case 16. |
| 23 | Native crop and cropped click overlay | At 125%, the empty-filter message is legible and the selected-site area remains empty; navigation and filter bounds align. |
| 24 | Native crop and cropped click overlay | At 125%, only the filter face is hovered; no stale roster/action regions appear in the empty view. |
| 25 | Native crop and cropped click overlay | At 125%, empty-custody values and four action labels fit their panel; navigation/filter/roster have separate active regions and contextual actions remain disabled. |
| 26 | Exact image and geometry equivalence to reviewed case 25 | Native crop, click crop and normalized control geometry match case 25 exactly. The requested locked-empty hover remains disabled and adds no active-hover proof. |
| 27 | Native crop and cropped click overlay | Closed-site layout at 125% keeps all lock labels and the status line inside the panel. Its legacy declared support/capacity values retain the semantic limit described for case 21. |
| 28 | Native crop and cropped click overlay | At 1920×1080, the native crop and normalized control geometry exactly match case 16; the click overlay was reviewed separately. The requested purpose hover still renders disabled. |
| 29 | Native crop/geometry equality to case 17; separate click-overlay review | The 1920×1080 empty view preserves the exact native crop and control geometry of case 17; its overlay contains only the expected navigation and filter regions. |
| 30 | Native crop/geometry equality to case 18; separate click-overlay review | The 1920×1080 filter-hover view preserves the exact native crop and geometry of case 18; the requested filter state is actually `hover`. |
| 31 | Native crop/geometry equality to case 19; separate click-overlay review | The 1920×1080 empty-custody view preserves case 19's exact native crop and control geometry. Contextual action faces remain legible and disabled. |
| 32 | Exact image and geometry equivalence to reviewed case 31 | Native crop, click crop and normalized geometry match case 31 exactly; requested hover on the locked-empty control remains disabled. |
| 33 | Native crop/geometry equality to case 21; separate click-overlay review | The 1920×1080 closed-site view matches case 21's native crop and control geometry; action faces have no active hit regions and retain the same declared-data caveat. |
| 34 | Native crop and cropped click overlay | The role picker fits at 1280×720. Only the requested option is hovered; its active rectangle is separate from the other choices and Back. No tooltip popup or click execution is proved. |
| 35 | Native crop and cropped click overlay | Locked picker at 1280×720 keeps the unavailable label legible. All three choice controls have no active hit region in this fixture; Back and navigation remain active. This does not prove availability of the other choices. |
| 36 | Native crop and cropped click overlay | Declared active picker at 1280×720 renders three separate active choice rectangles and Back with normal faces; none overlaps another control. |
| 37 | Native crop and cropped click overlay | At 125%, the role-picker title, explanatory text and option labels fit; only the declared target has a hover face and all active regions remain distinct. |
| 38 | Native crop and cropped click overlay | Locked picker at 125% fits with no option hit regions; Back/navigation remain active. As in case 35, this fixture does not establish availability of the other choices. |
| 39 | Native crop and cropped click overlay | Active picker at 125% has three separate active choices and Back, with normal faces and legible explanatory text. |
| 40 | Native crop/geometry equality to case 34; separate click-overlay review | At 1920×1080, the hover view has the same native crop and normalized geometry as case 34; only the requested option is hovered. |
| 41 | Native crop/geometry equality to case 35; separate click-overlay review | The 1920×1080 locked picker matches case 35; choices have no active regions, while navigation and Back remain active. |
| 42 | Native crop/geometry equality to case 36; separate click-overlay review | The 1920×1080 active picker matches case 36, with three distinct choice regions and Back. |
| 43 | Native crop and cropped click overlay | Records at 1280×720 has aligned cause/amount columns, two legible history entries and a contained authority/footer section; only navigation and close are active. Numbers remain declared test inputs. |
| 44 | Native crop and cropped click overlay | Records at 125% preserves column separation, readable entries and a contained footer, with no content hit regions outside navigation. No campaign or historical measurement is inferred from the supplied numeric values. |
| 45 | Native crop/geometry equality to case 43; separate click-overlay review | Records at 1920×1080 exactly matches case 43's native crop and normalized control geometry; the overlay preserves navigation-only active regions. |

The accompanying geometry audit checks active-control intersections, window containment, clipping, visible text overflow, failed validator checks, and exact artifact hashes.
It also compares every declared visibility expectation and requested element state with the resulting scene, keeping requested-but-disabled hover cases as coverage gaps.
Hidden-element warnings and intentional button/label layering are retained in the original validation artifacts rather than presented as visible defects.

## Selected-action fixture boundary

Case 16 forces `camp_admin_site_role` visible but supplies no `values.camp_selected_state_id` or `controls` map.
Its current source route is `camp_admin_site_role_click_enabled` at `common/scripted_guis/camp_repression_ledger_scripted_gui.txt:114`, which calls `camp_admin_has_selected_operating_site`.
At follow-up source inspection, that trigger requires the selected-state variable, an operational site, and matching responsible-country identity at `common/scripted_triggers/camp_administration_ui_triggers.txt:64–69` (SHA-256 `e19226a4e58339e48fbe71aeba45e157b475f3d8139036926c634182f645d293`).
The returned disabled state is consistent with this incomplete declared fixture; a forced visible face is not evidence that the action is available.
No missing campaign facts were invented to make the hover case pass.
