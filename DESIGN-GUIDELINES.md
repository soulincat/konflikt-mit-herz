# Soulful Academy — Editorial Design Guidelines

Design system for the landing experience: **editorial calm + human warmth + institutional confidence.**  
This is manifesto UI, not app UI.

---

## System philosophy (TL;DR)

- **Buttons invite, they don’t shout.**
- **Text leads, UI supports.**
- **Whitespace is a first-class component.**
- **CTAs feel like “continue reading,” not “convert now.”**

---

## 1. Design language

**Overall:** Low visual noise, generous negative space, soft color temperature, serif-led typography. Buttons that ask, not command.

**Key traits:**

- Low visual noise
- Generous negative space
- Soft color temperature
- Serif-led typography (rare in tech UI)
- Buttons that invite, not command

**Scope:** These guidelines apply to **editorial and landing pages** (e.g. hero, manifesto, long-form sections). Functional or dashboard-style pages should use a quieter, stricter sibling system — do not apply this system blindly to dense UI.

---

## 2. Design tokens

Codify these in CSS (e.g. `:root` or a shared block). Use them everywhere so implementation and this doc stay in sync.

### Spacing

| Token        | Value   | Use |
|-------------|---------|-----|
| `--space-xl` | 160px   | Section vertical padding (large) |
| `--space-lg` | 120px   | Section vertical padding (default) |
| `--space-md` | 64px    | Between major blocks (e.g. after hero quote) |
| `--space-sm` | 32px    | Between related elements |

**Rule:** Vertical spacing > horizontal spacing. Sections breathe; no visible dividers — separation by whitespace only.

### Color

| Token            | Role | Notes |
|------------------|------|--------|
| `--bg-primary`   | Warm neutral background | Tinted off-white / cream (e.g. `#F4EFE9`, `#E6D6C7`) |
| `--bg-secondary`  | Cooler neutral | Where a secondary surface is needed |
| `--text-primary` | Primary text | Soft dark — dark brown/charcoal, never pure black (e.g. `#4A2E32`, `#3A2623`) |
| `--text-secondary` | Attribution, metadata, subtext | Lower contrast (e.g. `#7B5E57`, `#8F5A5E`) |
| `--accent`       | CTAs, subtle emphasis | Desaturated pastel |
| `--focus-ring`   | Focus outline | Custom neutral (not browser blue) |

**Philosophy:** Nothing is pure. Backgrounds are tinted neutrals; text is soft dark; accent is desaturated pastel. All contrast must still pass **WCAG AA**.

---

## 3. Layout and grid

- **Grid:** 12-column (e.g. `grid-template-columns: repeat(12, 1fr)`). Max width of grid container ~1200px where appropriate.
- **Content width:** Primary text/content spans **5–6 columns**. Optional art or signature lives in adjacent columns, not overlapping text.
- **Alignment:** Left-aligned primary text blocks. Optical centering where needed (e.g. hero slightly left-weighted), not strict center. No center-aligned paragraphs; only headlines may be centered in rare cases.
- **Line length:** Cap body at **60–70 characters** (e.g. `max-width: 65ch`).

This creates a reading posture (like a book/letter) and reduces “hero shoutiness.”

---

## 4. Typography and font pairing

- **Primary serif (Lora):** Meaning — headlines, section titles, hero quote, body when editorial tone is desired.
- **Secondary sans (Lato):** Action and structure — UI labels, metadata, buttons, captions.

Contrast is intentional: serif = meaning; sans = action & structure.

---

## 5. TextBlock component

The soul of the system. Use by **role**, not just size.

### Variants

| Variant | Use | Font | Size | Line height | Weight | Max width | Alignment | Notes |
|---------|-----|------|------|-------------|--------|-----------|-----------|--------|
| **HeroQuote** | Manifesto statements | Serif (Lora) | 48–56px | 1.25–1.3 | 400 | 60–70ch | Left | Margin bottom 64–80px. Letter-spacing default or slightly negative (never wide). |
| **SectionTitle** | Chapter titles (e.g. “Careers”) | Serif (Lora) | 56–64px | 1.15–1.2 | 400 | — | Left | Treated as chapter title, not page title. Paired with optional subtext. |
| **Body** | Long-form copy | Serif or Lato | 16–18px | 1.6–1.75 | 400 | 65ch | Left, rag-right | No justified alignment. Used sparingly; whitespace does the work. |
| **Meta / Attribution** | Name, role, captions | Sans (Lato) or mono | 13–14px | — | 400 | — | Left | Letter-spacing +4–6%. Muted color (`--text-secondary`). Always visually separated from main text. |

**Suggested class names:** `.text-block--hero`, `.text-block--section-title`, `.text-block--body`, `.text-block--meta`.

**Rhythm:** Headline → pause → body → pause → action. CTA is never glued to text; always separated by space.

---

## 6. Button component

Polite buttons: they invite, they don’t shout.

### Variants

- **Primary**
- **Secondary**
- **IconOnly**
- **Ghost** (very limited use)

### Base anatomy

- **Structure:** `[ Label Text ]`
- **Height:** 44–48px (desktop)
- **Min width:** Content-based (never fixed)
- **Padding:** Horizontal 20–24px, vertical 12–14px
- **Border radius:** 999px (pill). Never sharp, never variable.

### Typography (all label buttons)

- Font: UI sans — Lato (not serif)
- Size: 14–15px
- Weight: 400–500
- Letter-spacing: +2% to +4%
- Text transform: none (no all caps)

### Colors by variant

| Variant   | Background | Text | Border |
|-----------|------------|------|--------|
| Primary   | Soft pastel (tinted neutral) | Dark neutral | None |
| Secondary | Transparent | Dark neutral | Optional 1px soft neutral |
| IconOnly  | Slightly stronger than label button | — | — |

### States

| State   | Behavior |
|---------|----------|
| Hover   | Background darkens ~4–6%. Transition 250–300ms ease-out. No scale, no shadow. |
| Active  | Background darkens slightly more. No press animation. |
| Focus   | 2px outline, custom neutral focus color (`--focus-ring`), offset 2px. Not default browser blue. |
| Disabled| Opacity 0.4–0.5. Cursor default. |

---

## 7. CTAGroup component

Not a single button — a **narrative unit**. Two components acting as one.

### Structure

```
[ Label Button ]  [ → Icon Button ]
```

### Layout

- Horizontal alignment
- Gap between label and icon button: **8–12px**
- On mobile: **always left-aligned** (never centered)
- Vertical spacing **above** CTAGroup: **48–64px** — positioned after a pause, never glued to text

### Behavior

- Hovering either button subtly highlights **both**
- Arrow suggests continuation, not urgency
- Clicking either triggers the **same action**

### Icon button (right part)

- Size: **44×44px**
- Icon: Simple arrow, **1.5–2px stroke**
- Background: Slightly darker than label button
- Border radius: **12–16px** (NOT pill)

---

## 8. Spacing and grouping (system-wide)

- **Stacking:** Never stack more than: **TextBlock → CTAGroup → Next section** in one chunk.
- **No dividers.** Separation by whitespace only.
- **No cards** unless absolutely necessary.
- **One emotional focal point per viewport.**

---

## 9. Control panel and utility UI

- Style to match “low visual noise”: softer background (tinted neutral), subtle border or shadow.
- Use Button component variants (pill, soft pastel); no harsh borders.
- **Accessibility/settings toggle:** Low-contrast, bottom-left, “socially quiet.” **Persistent and global** — always available.

---

## 10. Interaction design

- **Transitions:** ease-out, duration **250–300ms**. No bouncy easing, no sharp hovers.
- **Hover:** No scale, no shadow. Subtle shade shift only.
- **Cursor:** Minimal changes; avoid pointer overload.
- Apply consistently to links, buttons, and any interactive section.

This UI never rushes the user.

---

## 11. Accessibility

- **Contrast:** All text/UI must pass **WCAG AA** even when the palette looks soft.
- **Focus:** Custom focus styles (2px outline, neutral, 2px offset). Never rely on default browser focus only.
- **Accessibility Mode toggle:** Persistent and global (e.g. panel or settings); visible but quiet.

---

## 12. Mobile

- **Layout:** Single column; content full-width within safe padding.
- **Vertical spacing:** Large — use `--space-lg` or `--space-xl` between sections.
- **CTAGroup:** Left-aligned; pushed down with 48–64px spacing above.
- **Control panel:** Collapse or move to a drawer so main content keeps the same editorial rhythm.

Mobile is not “shrunk desktop” — it’s single column with massive vertical spacing and CTA pushed down.

---

## Quick reference — token summary

```css
/* Spacing */
--space-xl: 160px;
--space-lg: 120px;
--space-md: 64px;
--space-sm: 32px;

/* Color (example values — tune to Artsy theme) */
--bg-primary: #F4EFE9;      /* or #E6D6C7 */
--bg-secondary: #E3D6C8;     /* cooler neutral */
--text-primary: #4A2E32;    /* soft dark */
--text-secondary: #7B5E57;  /* muted */
--accent: /* desaturated pastel */;
--focus-ring: /* custom neutral, WCAG AA */;
```

---

*Document version: 1.0. Lock this guide first; implement the landing page (and any sibling pages) against it.*
