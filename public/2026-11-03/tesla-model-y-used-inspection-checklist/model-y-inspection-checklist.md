# Used Tesla Model Y — Pre-Purchase Inspection Checklist

**Prepared:** 2026-11-03
**Scope:** 2020–2025 Model Y (legacy body 2020–2024, "Juniper" refresh 2025+)
**How to use:** Print the PDF in `artifacts/model-y-inspection-checklist.pdf`. Work top to bottom. Anything in **RED FLAGS** ends the inspection — walk away, don't negotiate.

---

## Before you drive out to see the car (15 minutes)

Do this remotely and you eliminate 60% of bad cars without leaving the house.

- [ ] **VIN in hand** (17 digits, from the listing photo of the windshield or door jamb — not just the listing text)
- [ ] **Free NHTSA recall check by VIN** → https://www.nhtsa.gov/recalls — every open recall should be zero. Recalls are free to fix, so open ones mean the owner ignored the car.
- [ ] **Title check** — Carfax or AutoCheck. Look for: salvage, rebuilt, flood, lemon/manufacturer buyback, "structural damage," rental/fleet history, and **accidents with airbag deployment**
- [ ] **Registration state** — a car titled in the Rust Belt vs. the Southwest matters. Chicago cars need a harder underbody look (see §5).
- [ ] **Photos of the tire sidewalls** (all four, with DOT date codes) — if you can't read a date code, assume old tires
- [ ] **Ask the seller, in writing (text is fine):**
  - Has the high-voltage battery or drive unit ever been replaced or repaired?
  - Any accidents, paintwork, or body repair?
  - Is FSD / Enhanced Autopilot currently active on the car? (Not "was" — *is*.)
  - Do you have both key cards and the original charging equipment?
  - How many miles on the current tires, and are they the original set?
  - Reason for selling, and how long have you owned it?
- [ ] **Ask for a screenshot of the Tesla app → Service → Battery & Range** if they'll send one. It costs them 30 seconds and tells you more than any listing.

---

## 1. Paperwork, title, and transfer (do this before money moves)

- [ ] **Title in seller's name** — matches the driver's license, no third-party "I'm selling it for my cousin"
- [ ] **Title brand is clean** — no salvage, rebuilt, flood, lemon, or "prior taxi/rental" notation
- [ ] **Lien released** — if there's a lender, you need a lien release letter in hand *before* payment, or you do the deal at the lender
- [ ] **Odometer matches** the title, the car's screen, and the app
- [ ] **Bill of sale** states VIN, price, mileage, date, and that the seller warrants the title is free of liens
- [ ] **Both key cards** — plus confirm a phone key can be added. A missing key card is ~$40–80 and a hassle.
- [ ] **Charging equipment present:**
  - [ ] Mobile Connector (the bag with the Gen 2 / Gen 3 connector)
  - [ ] Both adapter pigtails — **NEMA 5-15** (standard wall) and **NEMA 14-50** (dryer/range outlet). The 14-50 is ~$45 to replace and most people lose it.
  - [ ] Wall Connector, if the listing included one
- [ ] **FSD / software entitlements confirmed in the car's own menu** — see §3. This is worth thousands and dealers routinely strip it.
- [ ] **Warranty position confirmed:**
  - Basic vehicle: 4 yr / 50,000 mi, **transfers to you**
  - Battery & drive unit: **8 yr / 120,000 mi** (Long Range, Performance, and RWD Long Range) or **8 yr / 100,000 mi** (Standard Range RWD), with **70% minimum capacity retention**, and it **transfers to subsequent owners**
  - Sellers/dealers sometimes claim coverage that's already expired. Verify by date and miles yourself.

---

## 2. High-voltage battery and charging — the single most expensive thing on the car

**This section decides the deal.** A pack replacement outside warranty dwarfs every other negotiation point.

### 2a. Run the in-car Battery Health Test (best evidence available)

Requires software **2025.8.4 or newer**. Takes 15–20 minutes. The car must be parked, plugged into AC power, and it will charge to 100% and discharge to measure real capacity.

- [ ] Path: **Controls → Service → Battery Health** (some builds: Service Mode → Battery)
- [ ] If the test isn't available or won't run: **Controls → Software → press and hold the "Model Y" badge for ~3 seconds → type `service`** to enter Service Mode and read the battery/diagnostics screens directly
- [ ] Record the **capacity retention %** here: `______%`

**How to read the result:**

| Retention | Verdict |
|---|---|
| **≥ 92%** | Strong. Normal for a low-mileage or gently used car. |
| **88–91%** | Typical for 40–70k miles. Fine — use it for negotiation, not rejection. |
| **85–87%** | Below average for the miles. Deduct money, and only proceed if the battery warranty still has meaningful time left. |
| **< 85%** | Serious. You're buying a car with a depreciating, expensive, non-warrantied-in-a-few-years consumable. Negotiate hard or walk. |

**Sanity checks that don't need Service Mode:**
- [ ] Charge to 100%, note the **rated range** shown. Compare to the original EPA figure for that exact trim/year. Expect **10–15% loss** on a 4–5 year old car; more than 18% is a problem.
- [ ] Tap the range display to switch from **"Rated"** to **"Ideal"** vs **percentage** — know which one you're reading before you judge it
- [ ] Check **Energy → Consumption** for lifetime efficiency (Wh/mi). ~250–280 Wh/mi is normal; 350+ means hard driving or a lot of fast charging in cold weather

### 2b. Supercharging test (do this if there's a Supercharger nearby)

- [ ] Navigate to a **V3 Supercharger** so the car preconditions the pack
- [ ] Plug in and watch the peak. A healthy Long Range should pull **~200–250 kW** at low state of charge in good weather
- [ ] **Peak below ~120 kW on a V3 with a warm pack and <20% SOC = red flag.** Could be a throttled pack, a failing charge port, or a car with heavy DC-fast-charge history.

### 2c. AC / home charging

- [ ] Charge port door opens and closes smoothly by touch and by app
- [ ] **Charge port pins are clean and unbent** — look inside with a light. Bent or burned pins are a known wear item and a port assembly is real money.
- [ ] Level 2 charging actually initiates and holds (don't just trust that it "worked at home")
- [ ] **CCS adapter** present, if the car is old enough that one was bought separately — and whether the car is **CCS-enabled** (retrofit was required on early cars)
- [ ] Mobile Connector charges the car when plugged into a normal outlet

### 2d. 12V battery

- [ ] Ask when the **12V battery** was replaced. 2020–2021 cars had **lead-acid** units that fail at ~3–4 years and strand the car; later cars moved to lithium-ion.
- [ ] Any "12V battery needs service" or low-voltage warning in the alert list = address before purchase

---

## 3. Software, computers, and driver aids

- [ ] **Controls → Software → Additional Vehicle Information** — record:
  - [ ] **Autopilot computer:** HW3 or HW4 (`________`) — HW4 is the newer, more capable hardware and matters for resale and future FSD features
  - [ ] **Software version** (`________`) — confirm the car is on a current build, not stuck on an old branch
  - [ ] **Free Supercharging** status, if any is listed
- [ ] **FSD / Enhanced Autopilot status** — confirm in the Autopilot menu that the *upgrade is actually present on the car*. If a dealer is selling it, get "FSD is active on this VIN" in writing on the bill of sale.
- [ ] **Screen:** no bubbles, delamination, dead pixels, or discoloration at the edges. Drag your finger across **every** corner of the touchscreen — dead zones are common and expensive.
- [ ] **All cameras render** — open the camera view and confirm front, rear, and both repeaters show a clean image. A blank or foggy camera is a hardware fault.
- [ ] **No persistent alert list** — Controls → Service → Alerts / the warning bell icon. Screenshot anything that appears.
- [ ] Sentry mode, dashcam recording, and the USB drive in the glovebox all function
- [ ] Bluetooth phone pairing, wireless charging pad, and all four USB-C ports work
- [ ] Navigation loads maps and traffic (confirms the connectivity/LTE module is alive)

---

## 4. Body, paint, glass, and water intrusion

- [ ] **Panel gaps are even** — frunk to fenders, doors to rockers, liftgate to quarters. Wide or uneven gaps on a used car often mean prior body repair, not factory sloppiness.
- [ ] **Paint depth / color match** between adjacent panels, especially in daylight at an angle. Look at the doors, quarters, and bumper covers.
- [ ] **Paint chips on the front bumper, hood leading edge, and behind the rear wheels** — Tesla paint is thin; heavy chipping is normal wear, but it's a negotiating point
- [ ] **Glass roof:** no chips, cracks, or delamination. Check the entire span — these are expensive and insurance-claim territory.
- [ ] **Windshield:** chips and cracks, and *whether the car has been recalibrated* after a replacement (camera calibration matters for Autopilot)
- [ ] **Water intrusion** — the classic Model Y leaks:
  - [ ] Lift the rear cargo floor and check for **dampness or rust** around the well
  - [ ] Check the **liftgate seal** and look for water trails inside the hatch
  - [ ] **Taillight housings** — condensation inside the lens
  - [ ] **Frunk** — water pooling under the liner
  - [ ] Sniff for **musty/mildew** smell in the cabin with the HVAC on recirculate
- [ ] **Undercarriage** — get on the ground with a light (or ask for it on a lift):
  - [ ] Battery pack tray: no dents, gouges, scrapes through the shield, or signs of impact. **A physically damaged pack can void coverage — this is a hard walk-away.**
  - [ ] Subframe and suspension mounts: rust scale, especially on a Chicago/salt-belt car
  - [ ] Brake lines and coolant lines: no corrosion or weeping

---

## 5. Suspension, steering, tires, brakes

Model Y is a ~4,400 lb car. Suspension and tires wear faster than people expect.

- [ ] **Front upper control arms** — the known creak. Turn the wheel slowly at a standstill and listen for **creaking/popping** from the front strut towers. Also listen over speed bumps at low speed.
- [ ] **Suspension knuckles** — 2020–2022 cars had a recall for front/rear knuckle fracture. Confirm it was done (VIN check on NHTSA) and listen for clunks over bumps.
- [ ] **Lateral link fasteners** — 2020–2021 recall; loose front suspension links. Any clunk or vague steering = investigate.
- [ ] **Half shafts / CV boots** — look behind the front wheels for torn boots and grease sling; click on full-lock turns
- [ ] **Tires — this is where money hides:**
  - [ ] Read all four **DOT date codes**. Over 6 years old = replace regardless of tread.
  - [ ] Measure tread depth at **outer, center, and inner** on each tire. Model Y wears the **inner shoulder** of the rears; a tire that looks fine at the outer edge can be corded inside.
  - [ ] Confirm all four are a **matched set**. Mismatched brands/sizes on an AWD EV stresses the drive units.
  - [ ] Sidewall damage, bubbles, or curb rash on the wheels
  - [ ] A full set of quality tires is a real cost — factor it in
- [ ] **Brakes:** regenerative braking means the pads are often near-new while the **rotors are pitted or rusted** from disuse — very common in salt-belt cars
  - [ ] Rotor faces: pitting, deep scoring, or a heavy rust lip
  - [ ] **Caliper slide pins** free, not seized
  - [ ] Brake fluid not dark; ask about the 2-year fluid service
- [ ] **Steering:** no play, no pulling, no vibration; check the steering wheel fastener recall on 2022–2023 cars
- [ ] **Drive unit noise:** a faint whine under acceleration is normal. **Clunking, grinding, or a rattle on lift-off** is not.

---

## 6. Interior and HVAC

- [ ] **Heat pump / HVAC — test both extremes.** This is the most expensive non-battery failure on early cars.
  - [ ] Set **LO** and max fan: air must go genuinely cold within a minute; listen for the compressor
  - [ ] Set **HI** and max fan: air must go genuinely hot
  - [ ] Run **defrost** and confirm it clears
  - [ ] Any error, weak output, or a compressor that cycles loudly = likely a heat pump/octovalve issue. On 2020–2021 cars this was a recurring failure with four-figure repair quotes. **Get it diagnosed before you buy, not after.**
- [ ] **Seats:** all power adjustments, heat (all zones), and cooling if equipped. Check the driver's **outer bolster** for collapse and tears.
- [ ] White interior: check for **blue jean dye transfer** on the driver's seat and door card
- [ ] **Seat belts:** all five latch and retract. 2019–2021 cars had a second-row retractor fastener recall.
- [ ] Second-row seat backs: fold and unfold, listen for rattles; 2022–2023 cars had a seat-back bolt recall
- [ ] **Trim and rattles:** drive over broken pavement and listen. Rear parcel shelf, door cards, and the B-pillar are the usual suspects.
- [ ] Sun visors, glovebox, center console, all cupholders, and the cargo cover work
- [ ] No smoke or pet odor, no stains in the cargo area
- [ ] Check the **tire repair kit / no spare** situation — Model Y has no spare; confirm the kit is present

---

## 7. The test drive — do it in this order

Do not let the seller "warm it up" first. **A cold start tells you things a warm car hides.**

1. **Cold start, before driving**
   - [ ] Listen at the front for coolant pump or fan noise that doesn't settle
   - [ ] Screenshot the alert list
   - [ ] Confirm no warnings on the cluster

2. **Low speed, parking lot (5 mph)**
   - [ ] Creaking from the front suspension while turning
   - [ ] Any lurching or unintended acceleration — 2020–2021 cars drew complaints here; you want to feel nothing unusual
   - [ ] Brakes grab smoothly, no grinding

3. **Surface streets**
   - [ ] Steering tracks straight on a flat road, hands light on the wheel
   - [ ] No vibration at 25–45 mph
   - [ ] Regen braking engages and feels consistent

4. **Highway (this is the important one)**
   - [ ] Accelerate hard from 40–70 mph: strong, smooth, no hesitation, no shudder
   - [ ] **Engage Autopilot/TACC and watch for phantom braking** — the #1 owner complaint on this model, worst on 2020–2021. If the car brakes hard for no visible reason, note it. Software can fix some of this; hardware can't.
   - [ ] Lane keep holds the center without sawing
   - [ ] No wind noise from the roof glass or door seals (a whistle means a bad seal)
   - [ ] Over expansion joints: no clunks, no rattles from the suspension

5. **Braking hard, safely, once**
   - [ ] Straight stop, no pull, no pulsation through the pedal (pulsation = warped/worn rotors)

6. **After the drive**
   - [ ] Put your hand near each wheel — one wheel much hotter than the others means a dragging brake
   - [ ] Re-check the alert list — warnings that only appear when warm still count
   - [ ] Smell for coolant (sweet) or burning
   - [ ] Re-check battery % consumed vs. miles driven for a rough efficiency sanity check

---

## 8. Year-by-year watch list

NHTSA recall campaign counts for Model Y, pulled from the NHTSA API on 2026-11-03. Recalls are free to fix — the count tells you how much attention the car needed, and whether the owner kept up.

| Model year | Recall campaigns | What to focus on |
|---|---|---|
| **2020** | **24** | First-year build. Front upper control arm bolts, suspension knuckle fracture, lateral link fasteners, seat belt fasteners, brake caliper bolts. Heat pump failures. Lead-acid 12V. Panel gaps and paint. **Weakest year — price it that way.** |
| **2021** | **23** | Same suspension/seat-belt campaign exposure, plus heat pump and 12V. Camera cable terminal issue affecting AEB. |
| **2022** | **20** | Knuckle recall still applies. Second-row seat back bolts, steering wheel fastener. Better build consistency than 2020–21. |
| **2023** | **17** | Lateral link fastener recall, pyrotechnic battery disconnect, forward camera misalignment. HW4 arrives this era — verify which computer the car has. |
| **2024** | **5** | Big drop in campaigns and complaints — the value pick. Watch for the **AP4 computer failure** that blacks out cameras and driver aids; ask if it's been replaced. |
| **2025** | **3** | Refresh ("Juniper") era. Fewest problems but still depreciating fast off new. Confirm the certification-label recall was addressed. |

**Verify the individual car, not the year:** run the VIN at https://www.nhtsa.gov/recalls and insist every open recall is closed before you pay.

---

## 9. Red flags — walk away, don't negotiate

- [ ] **Battery pack physical damage** (dents, gouges, shield scrapes) — coverage risk, huge cost
- [ ] **Battery capacity under 85% with the 8-year warranty nearly expired**
- [ ] **Salvage / rebuilt / flood title**, or a title that isn't in the seller's name
- [ ] **Deployed-airbag accident history** or evidence of structural repair
- [ ] **FSD advertised but not active in the car** — that's bait
- [ ] **Heat pump not producing heat or cold** and the seller won't let you get it diagnosed
- [ ] **Persistent alerts** the seller dismisses as "just a glitch"
- [ ] **Cannot run the battery health test and won't allow Service Mode**
- [ ] **Peak Supercharging drastically low** on a warm pack at a V3
- [ ] **Seller refuses a pre-purchase inspection** by an independent EV shop
- [ ] **Odometer or title discrepancy** of any kind
- [ ] **"Deposit now, I'll hold it"** pressure with no paperwork

---

## 10. Negotiation levers — what each finding is worth

| Finding | Leverage |
|---|---|
| Battery retention 85–88% | Push for a discount; cite the test number directly |
| Tires at 4/32" or mismatched | Full set is a real cost — ask for it off the price |
| Pitted/rusty rotors, seized pins | Brake job, ask for it |
| Heat pump weak | Do not buy "as is" — require repair or a large credit |
| Open recalls | Free to fix, but use it: "you haven't kept up on the car" |
| Missing Mobile Connector / 14-50 adapter | Small, but real |
| Missing key card | Small |
| Accident history with paintwork | Real money off, always |
| 2020–2021 model year | Price against the 2024, which has 1/5 the recall exposure |

---

## 11. Deal-day sequence

1. Remote screen → shortlist the car
2. VIN recall check + title check → confirm clean
3. In-person inspection → this checklist
4. Battery health test → record the number
5. Supercharger test if possible
6. Independent PPI at an EV shop if anything is unclear
7. Agree price **in writing** with findings itemized
8. Payment + signed bill of sale + title + lien release + both keys + charging gear
9. **Transfer the Tesla account to your email before you leave the driveway** — this is the step people forget. The previous owner must remove the car from their account, or you can't add it to yours.
10. Add the car to your insurance and confirm coverage on the VIN that day

---

*Companion files: `summary.md`, `sources.json`, printable `artifacts/model-y-inspection-checklist.pdf`*
