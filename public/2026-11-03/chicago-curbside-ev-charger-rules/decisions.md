# Decisions

## D1 — Check whether the law changed before answering from memory
**Decision:** Search for a current Chicago curbside program rather than answering from general knowledge that "cities don't allow private curb chargers."
**Why:** General knowledge on this was six months stale. A curbside pilot ordinance was introduced in May 2026 and *passed* in July 2026. Answering from memory would have missed the single most relevant fact in the response.

## D2 — Verify the ordinance status at the City Clerk, not at a summary site
**Decision:** Go to chicityclerkelms.chicago.gov for the legislative record after councilmatic showed only "Introduced" and "Referred."
**Why:** Councilmatic's history was incomplete — it showed the May introduction but not the July passage. The Clerk record showed `Status 90-Final / Sub Status Passed / Final Action Date 7/15/2026`. A secondary source would have had me tell the user the pilot doesn't exist yet. That would have been flatly wrong.

## D3 — Read the ordinance text visually rather than trusting the title
**Decision:** Download the enrolled PDF, discover it was a scanned image with no text layer, render at 140 dpi, and read it with vision.
**Why:** The title — "establishing Electric Vehicle Curbside Charging Pilot Program" — reads like it might create a resident-application pathway. Only the definition ("owned by the City of Chicago and operated for public use") settles that it doesn't. The title alone would have produced the wrong answer. This is the crux of the whole response and it was worth the extra calls.

## D4 — Lead with the extension-cord violation
**Decision:** Dedicate a full section to why running a cord to the curb doesn't work, with the specific code section.
**Why:** It's the workaround essentially every Chicago renter or rowhouse owner attempts, and it's the one thing that could get them fined or sued. Giving them the actual code citation is what makes the advice stick — "it's not allowed" is ignorable; "§ 14X-7-705.3 prohibits cords for anything but portable appliances, and a car isn't one" is not.

## D5 — Include the right-to-charge law even though it wasn't asked
**Decision:** Cover the Illinois EV Charging Act protections for renters and condo owners.
**Why:** The user's actual problem is "I want to charge at home and I may not control the parking." The curb is the wrong solution to that problem, and the right-to-charge statute is the right one. Answering only the literal question would have been technically correct and practically useless.

## D6 — Flag the federal 30C credit as probably dead
**Decision:** Present the 30C credit as "verify, likely expired" rather than repeating Chicago.gov's still-live link.
**Why:** Chicago's page hasn't been updated for the 2025 tax legislation that terminated the credit for property placed in service after June 30, 2026. Repeating it as available would set the user up to budget around money they won't get. Better to flag the conflict than to pick the more convenient answer.
