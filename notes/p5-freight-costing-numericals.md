# Freight Costing Numericals — Sea, Air, Road
Every worked example in the *Maritime and logistics costing* PPT 📘 and the *Air security and cost* PDF 📘, solved step by step in exam layout. Section E adds **practice problems** in the same style (marked *practice*, not from the zip) so you can drill the methods. Theory: [Maritime & Logistics Costing](ch04-maritime-logistics-costing.md) and [Air Freight Pricing & Security](ch05-air-freight-pricing-security.md).

## Formula sheet ⭐⭐⭐
| What | Formula |
|---|---|
| Distance rate | Freight = rate per mile/km × distance |
| Weight rate | Freight = rate per unit weight × weight |
| DIM weight (inches → lb) | L × W × H (in) ÷ 139 (domestic) or ÷ 166 (international) |
| Air volumetric weight (cm → kg) | L × W × H (cm) ÷ 6,000 = kg ⇔ m³ × 166.67 (≈167) |
| Volume (cm → m³) | L × W × H (cm) ÷ 1,000,000 |
| Volumetric weight (given factor) | Volume (m³) × conversion factor (kg/m³) |
| Ocean W/M | 1 m³ = 1,000 kg (1 revenue ton = greater of tonnes or m³) |
| Chargeable weight | The **higher** of actual weight and volumetric weight (air: round **up** to next 0.5 kg) |
| LTL density | Weight (lb) ÷ (L × W × H in ft) = lb/ft³ |
| Total freight | Base freight + surcharges + additional costs |
| CAF (as %) | CAF % × (base + BAF) |
| Air carrier liability (Montreal) | 22 SDR × kg × SDR rate |

---

## A. Freight rate method examples (PPT) 📘

**Q1. Per-mile rate: the rate is $2 per mile and the distance is 500 miles. Find the freight.**
Freight rate = rate per mile × total distance = 2 × 500 = **$1,000**.

**Q2. Weight-based rate: the rate is $0.50 per pound and the shipment weighs 2,000 pounds. Find the freight.**
Freight rate = rate per unit weight × total weight = 0.50 × 2,000 = **$1,000**.

**Q3. Dimensional weight: a package measures 24 in × 18 in × 12 in; DIM factor 139. Find the dimensional weight.**
DIM weight = L × W × H ÷ DIM factor = 24 × 18 × 12 ÷ 139 = 5,184 ÷ 139 = **37.3 lb** (the PPT shows 37.2 lb). Freight is charged on this DIM weight unless the **actual weight is greater**, in which case actual weight is the chargeable weight. (With the international factor 166: 5,184 ÷ 166 = 31.2 lb.)

**Q4. Flat rate: a flat rate of $1,200 is agreed between two cities. What is the freight?**
Freight = flat rate = **$1,200**, regardless of weight or distance.

**Q5. Zone-based pricing: shipping from Zone 1 to Zone 5 has a predefined rate of $50 for a package size. What is the freight?**
Freight = rate for zone pair = **$50**.

**Q6. Freight class (LTL density): a shipment weighs 500 lb and measures 4 ft × 4 ft × 4 ft. Find the density.**
Density = weight ÷ (L × W × H) = 500 ÷ (4 × 4 × 4) = 500 ÷ 64 = **7.81 lb per cubic foot**. The NMFC freight class (50–500) is then read from a density table — 7.81 lb/ft³ falls in the 6–8 lb/ft³ band, which is **class 175** on the standard 13-band NMFC density scale (8–10 lb/ft³ would be class 125). Lower density → higher class → higher rate.

---

## B. Ocean freight calculation examples (PPT) 📘

**Q7. Volumetric weight: total cargo volume is 30 m³ and the carrier's conversion factor is 200 kg/m³. Find the volumetric weight.**
Volumetric weight = volume × conversion factor = 30 m³ × 200 kg/m³ = **6,000 kg**. The chargeable weight is the greater of this and the actual weight.

**Q8. Base freight: cargo volume is 125 m³ and the carrier's base rate is $50 per cubic metre or ton. Find the base freight.**
Base freight = 125 × $50 = **$6,250**. (Ocean conversion: 1 m³ = 1,000 kg = 1 ton, so the rate applies per m³ or per tonne, whichever gives more revenue tons.)

**Q9. Canada → US example: an importer ships 50 packages; total weight 5,000 kg; volume 20 m³; base rate $4 per kg; conversion factor 200 kg/m³. Calculate the freight cost.** ⭐⭐⭐
- Step 1: Volumetric weight = 20 m³ × 200 kg/m³ = **4,000 kg**.
- Step 2: Chargeable weight = max(actual 5,000 kg, volumetric 4,000 kg) = **5,000 kg** (actual is higher).
- Step 3: Freight = 5,000 kg × $4/kg = **$20,000** (no surcharges or additional costs assumed).

**Q10. Step-by-step FCL example: a 40-ft container of garments from Shanghai to Los Angeles, March 2025. Build the total estimated freight.** ⭐⭐⭐
| Cost component | Working | Amount (USD) |
|---|---|---|
| Base ocean freight (Shanghai–LA) | given | 2,100 |
| BAF | given | 180 |
| CAF | 5% × (base + BAF) = 5% × (2,100 + 180) = 5% × 2,280 | 114 |
| THC at origin (Shanghai) | given | 145 |
| THC at destination (LA) | given | 190 |
| Documentation / B/L fee | given | 75 |
| ISPS security charge | given | 12 |
| PSS (seasonal) | given | 150 |
| **Total estimated freight** | 2,100 + 180 + 114 + 145 + 190 + 75 + 12 + 150 | **$2,966** |
Not included: customs duties, inland haulage, demurrage, warehousing. Note that surcharges and handling add **$866, i.e. 41%** on top of the base rate, and the base rate is only **71%** of the total.

**Q11. Comparing two routes: Case 1 — India → UAE (short haul), FCL 20' ceramic tiles Mumbai → Jebel Ali, base $500, total $820. Case 2 — Vietnam → Germany (long haul with transhipment), FCL 40' electronics, base $2,900, transhipment (Singapore) $220, green surcharge $90, total $3,860. Analyse.** ⭐⭐
- Case 1: non-base charges = 820 − 500 = **$320** (64% on top of base; base = 61% of total).
- Case 2: listed extras = 220 + 90 = $310 → base + extras = $3,210; other charges (BAF, THCs, docs, etc.) = 3,860 − 3,210 = **$650**. Total extras = 3,860 − 2,900 = $960 (33% on top of base; base = 75% of total).
- Lesson (PPT): **transit time, routing (transhipment) and port fees** can change the bottom line dramatically; on short routes fixed port/handling costs dominate, on long routes base freight dominates. Per-TEU, Case 2 costs $1,930/TEU vs $820/TEU for Case 1.

**Q12. Air vs sea rule of thumb: a shipment is 0.4 m³ and weighs 80 kg. Which mode is likely cheaper and why?**
Below **0.5 m³ and 100 kg** air may be competitive, because **sea freight has a minimum chargeable volume of 1 m³** — this shipment pays for 1 m³ by sea, while by air it pays for max(80, 0.4 × 167 = 66.8) = **80 kg**. Above 0.5 m³ and 100 kg, sea is generally cheaper (but up to 43 days from China).

---

## C. Air freight volumetric examples 📘

**Q13. PPT example: 1 m³ of goods weighs 100 kg. What is the chargeable weight by air? What if it weighs 500 kg?**
Volumetric weight = 1,000,000 cm³ ÷ 6,000 = 166.67 → **167 kg**. Actual 100 kg < 167 kg → chargeable **167 kg**. If the 1 m³ weighs 500 kg → actual weight is higher → chargeable **500 kg**.

**Q14. Air security & cost PDF example: a piece weighs 150 kg and measures 120 cm × 80 cm × 50 cm. Find the volumetric weight and chargeable weight.** ⭐⭐⭐
- Volume = 1.2 m × 0.80 m × 0.50 m = **0.48 m³**.
- Volumetric weight = 0.48 × 167 = 80.16 ≈ **80 kg**; or 120 × 80 × 50 ÷ 6,000 = 480,000 ÷ 6,000 = **80 kg**.
- Chargeable weight = max(150, 80) = **150 kg** — the actual weight exceeds the volume equivalent.
- Freight = 150 kg × agreed tariff rate per kg for that weight break (origin → destination), plus surcharges (fuel, war risk) and the origin/destination charges listed in the PDF.

**Q15. Air carrier liability (PDF): the Montreal Convention limits liability to 22 SDR/kg, and 1 SDR = US$1.43493. What is the limit per kg in US$?**
22 × 1.43493 = **US$31.57 per kg** (US$31.56846). For the 150 kg piece in Q14 the carrier's maximum liability = 150 × 31.56846 = **US$4,735.27**, which may be far below the cargo's value — hence **cargo insurance** on a small percentage of declared value, ideally door-to-door. (Note: from 28 Dec 2019 the Montreal limit was revised to 22 SDR; it is revised every five years and rose to 26 SDR from Dec 2024.)

---

## D. Container capacity checks (Containerization PPT data) 📘

**Q16. How many cartons of 60 cm × 40 cm × 40 cm can theoretically fit in a 20-ft container (internal 5.9 m × 2.35 m × 2.4 m)?**
Carton volume = 0.6 × 0.4 × 0.4 = 0.096 m³. By dimensions: 5.9 ÷ 0.6 = 9 (9.83), 2.35 ÷ 0.4 = 5 (5.875), 2.4 ÷ 0.4 = 6 → 9 × 5 × 6 = **270 cartons** (25.9 m³). Rotating (length 0.4 along 5.9 m: 14; width 0.6 across 2.35: 3; height 6) = 14 × 3 × 6 = 252. Best simple layout = **270**. By volume alone 33.2 ÷ 0.096 = 345, so stowage factor ≈ 78%. Check payload too: if a carton weighs 120 kg, 270 × 120 = 32,400 kg > 28,180 kg → **weight-limited** to 234 cartons. *(practice built on PPT container data)*

---

## E. Practice problems (not from the zip — same methods) 

**Q17. Air: 3 cartons, each 60 × 50 × 40 cm and 18 kg. Rate $4.20/kg; fuel surcharge $0.80/kg on chargeable weight. Find the charge.**
Volumetric per carton = 60 × 50 × 40 ÷ 6,000 = 120,000 ÷ 6,000 = 20 kg → total 60 kg. Actual = 3 × 18 = 54 kg. Chargeable = **60 kg**. Freight = 60 × 4.20 = $252; FSC = 60 × 0.80 = $48; **total $300**.

**Q18. Ocean LCL (W/M): a shipment of 12 m³ weighing 4,500 kg; rate $60 per revenue ton. Find freight. What if it were 6 m³ weighing 8,000 kg?**
Revenue tons = max(12 m³, 4.5 t) = 12 → freight = 12 × 60 = **$720** (volume-based). Second case: max(6, 8) = 8 RT → 8 × 60 = **$480** (weight-based).

**Q19. Cylinder pricing rule (Air security PDF): a drum 40 cm in diameter and 120 cm long weighing 25 kg. Find the chargeable weight.**
Unusual shapes are charged on the **box they fit in**, not the true volume: 40 × 40 × 120 = 192,000 cm³ ÷ 6,000 = **32 kg** > 25 kg → chargeable **32 kg**. (True cylinder volume would give only 25.1 kg — the rectilinear rule costs the shipper 7 kg more.)

**Q20. Rounding rule: a consignment's volumetric weight is 80.16 kg and actual weight 78 kg. What is the chargeable weight?**
Chargeable weight is always **rounded up to the next half kilogram** → 80.16 → **80.5 kg**.

**Q21. Road FTL vs LTL: LTL rate ₹2,000 per pallet; FTL (33 pallets) ₹45,000. At how many pallets does FTL become cheaper?**
Break-even = 45,000 ÷ 2,000 = 22.5 → from **23 pallets** FTL is cheaper (and avoids hub handling and trans-shipment).

**Q22. Inches DIM for the Vibrant Video speaker carton (30 × 18 × 18 in, 28 lb) — domestic factor 139.**
30 × 18 × 18 = 9,720 in³ ÷ 139 = **69.9 lb** DIM vs 28 lb actual → parcel carriers would bill ≈ 70 lb: bulky, light goods are priced on space, which is why the KPI case uses LTL/TL rather than parcel service.
