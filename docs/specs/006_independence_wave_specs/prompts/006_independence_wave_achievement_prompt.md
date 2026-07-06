# 006 Independence Wave, Achievement Prompt

Implement the achievement suite from the canonical super-events and achievements file. Create tracking flags or variables, unlock checks, disqualifiers, localisation keys, icon references, docs, and validation for every achievement.

Achievements must respect Event 6 origin. A tag that appears through another event system must not unlock Event 6 origin achievements unless it has the Event 6 origin flag. Host survival achievements must confirm the former host was not fully deleted by Event 6 logic. Scenario achievements must account for release-all setup choices and any debug or manual control exclusions used by the project.

Every achievement icon needs an icon direction, completed art, and grey or not eligible variants if the achievement framework uses them. Do not implement hard achievements as automatic unlocks. Report blocked icons or missing tracking separately.
