# 📑 Project Brief – CORAH Web Application

## 1. Client Overview

**CORAH (Centre of Rural and Aging Health)** is a non-profit organization dedicated to improving the quality of life for seniors in rural communities. CORAH provides health services, education, and community engagement opportunities, with a strong emphasis on accessibility, inclusivity, and usability for older adults.

---

## 2. Project Purpose

The goal of this project is to design and implement a **modern, highly accessible web application** that allows seniors to discover, register for, and participate in CORAH events. The platform must also empower administrators to efficiently manage events, participants, and promotional materials, while ensuring a **centralized hub** for both digital and print-based outreach.

---

## 3. Key Objectives

1. **Accessibility First**

   * WCAG 2.1 AA compliance for usability by seniors (large fonts, high contrast, screen reader friendly, simple navigation).
   * Clear, uncluttered interfaces to reduce cognitive load.

2. **Event Management**

   * Easy creation and management of events (date, time, location, description).
   * Public-facing event listings with filtering/search by category and location.
   * One-click event registration for seniors (minimal form fields).

3. **User Registration & Profiles**

   * Seniors can register for events with simple, guided steps.
   * Optional profile system for repeat participants (saving contact info, preferred events).
   * Confirmation and reminder emails/SMS for registered events.

4. **Admin Functions**

   * Admin dashboard for managing events, users, and registrations.
   * Tools to export attendance lists and reporting features.
   * Role-based access (admin, staff).

5. **Integrated Print/Marketing Features**

   * Automated generation of printable **event posters and flyers** from the same event data (no need for separate publishing software).
   * Branded templates with CORAH’s logo and identity.
   * Export to PDF for printing and local distribution.

---

## 4. Target Audience

* **Primary Users:** Senior citizens (60+) in rural communities, often with varying levels of digital literacy and accessibility needs.
* **Secondary Users:** CORAH staff and administrators managing events, communications, and outreach.

---

## 5. Functional Requirements

### Public-Facing Website

* Event calendar and listing view.
* Event details page (accessible typography, large buttons, “Register” CTA).
* Registration form (minimum steps, mobile-friendly).
* Accessibility features: resizable text, color contrast switcher, screen reader compatibility.

### Admin Portal

* Login for staff.
* CRUD functionality for events and user data.
* Export reports (attendance, participation trends).
* Auto-generate flyers/posters from event data.

### Print Integration

* Template-driven flyer/poster design system.
* Support for A4, letter, and half-sheet formats.
* Export to print-ready PDF with event details auto-populated.

---

## 6. Technical Requirements (Initial Considerations)

* **Frontend:** Responsive HTML5/CSS3 with ARIA roles; scalable for future frameworks (e.g., React, Vue).
* **Backend:** Secure CMS or custom admin panel; user authentication and role management.
* **Database:** Event, user, and registration data stored relationally.
* **Print Functionality:** PDF export engine integrated with event data.
* **Hosting:** Cloud-based (e.g., Netlify, GitHub Pages for static; or institutional hosting with database for dynamic).

---

## 7. Success Criteria

* Website is **fully accessible** and senior-friendly.
* Event creation, registration, and flyer generation functions work seamlessly.
* Admins reduce time spent on manual event promotion and data management by at least **50%**.
* Positive user feedback from seniors during pilot testing (≥ 80% satisfaction).

---

## 8. Deliverables

* **Wireframes & Mockups** (high-fidelity, accessibility-focused).
* **Responsive Website** (front-end, tested on multiple devices).
* **Admin Dashboard** (event and user management).
* **Poster/Flyer Generator** (templates, export functionality).
* **Documentation & Training Materials** (admin guide, accessibility testing checklist).

---

## 9. Constraints & Considerations

* Accessibility is **non-negotiable**; design decisions must prioritize usability for seniors.
* Content should be **readable at Grade 8 literacy level or lower**.
* Rural communities may have limited internet speeds — site must be lightweight and performant.
* Budget-conscious solution: use **open-source or free tools** where possible.

---

## 10. Next Steps

1. **Discovery Phase** – User research (interviews with seniors and CORAH staff).
2. **Design Phase** – Wireframes → mockups → accessible design system.
3. **Prototype Phase** – Interactive prototypes and usability testing with seniors.
4. **Development Phase** – Front-end, back-end, and admin portal build.
5. **Testing Phase** – Accessibility, usability, and cross-device QA.
6. **Launch & Training** – Deployment, staff training, feedback cycle.

