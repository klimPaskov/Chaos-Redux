# Event 020 Dedicated Response Category Correction

This correction supersedes every earlier Event 020 instruction that forbids a dedicated Black Plague decision category.

Event 020 uses two coordinated decision surfaces:

- `black_plague_response_category` is the dedicated national cure and strategic-management category. It owns medical-reserve production, the 0–100 countermeasure programme, research policy, knowledge sharing or hoarding, international medical cooperation, and post-crisis recovery programmes.
- `chaosx_disease_containment_category` remains the shared disease-containment category. It owns state-selected quarantine, hospitals, cordons, treatment, rat clearance, food-store sealing, sewer and burrow clearance, flea control, transport purges, demolition, anti-rat operations, and terminal state missions.

Both categories may be visible at the same time. The dedicated category is independent of the disease currently selected on the shared board, so another active disease does not displace Black Plague cure management. The shared category retains its existing selected-disease and selected-state gates.

The dedicated category reuses the existing Event 020 countermeasure variables, effects, costs, AI logic, and cleanup rules. It must not duplicate progress, create an alias decision that pays twice, instantly cure a state, or bypass the normal state machine. Its standard category description shows country deaths, worldwide deaths, cure status and progress, Medical Reserve, Response Capacity, and international coordination. No new scripted GUI is required.

The category picture is a final 114×101 decision-category image depicting plague doctors or protected medical workers treating a patient in a period field ward. It contains no text or simulated interface elements and is registered as `GFX_decision_cat_picture_black_plague_response`.
