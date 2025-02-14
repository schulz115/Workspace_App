---
title: Design Decisions
nav_order: 4
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

---
title: Design Decisions
nav_order: 4
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---



All the following decisions were taken in agreement between the two group members:
https://github.com/oezcanemre and https://github.com/schulz115


01: Saving procedure - automatic vs manual saving

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 14-Feb-2025

### Problem statement


We must decide on whether to implement automatic saving or manual saving (implying a version control feature) for workspaces that are being edited. 


### Regarded options


| Criterion | Automatic Saving | Manual Saving |
| --- | --- | --- |
| **User Convenience** | ✔️ No need to remember to save | ❌ Requires user action to save |
| **Data Loss Prevention** | ✔️ Ensures no work is lost | ❌ Risk of losing unsaved changes |
| **Version Control** | ❌ No built-in version tracking | ✔️ Users can decide when to save |
| **Implementation Complexity** | ✔️ Easy to implement | ❌ Requires complex version control implementation |
 |


Criterion	Automatic Saving	Manual Saving
Usability	✔️ Highly practical and immediate for users	❌ Requires explicit actions by users
Version Control	❌ Lacks version control; cannot easily retrieve past states	✔️ Can implement version control for retrieving previous states
Implementation Effort	✔️ Minimal implementation required	❌ High complexity and significant development effort required


### Decision

We have decided to implement an automatic saving. We want to follow our minimalistic approach and also the full version control would introduce significant implementation effort/complexity - in comparison to a rather marginal benefit - in other words the resources required in comparison to its value is not worth it.



















01: Saving procedure - automatic vs manual saving

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 14-Feb-2025

### Problem statement


We must decide on whether to implement automatic saving or manual saving (implying a version control feature) for workspaces that are being edited. 


### Regarded options


| Criterion | Automatic Saving | Manual Saving |
| --- | --- | --- |
| **User Convenience** | ✔️ No need to remember to save | ❌ Requires user action to save |
| **Data Loss Prevention** | ✔️ Ensures no work is lost | ❌ Risk of losing unsaved changes |
| **Version Control** | ❌ No built-in version tracking | ✔️ Users can decide when to save |
| **Implementation Complexity** | ✔️ Easy to implement | ❌ Requires complex version control implementation |
 |


Criterion	Automatic Saving	Manual Saving
Usability	✔️ Highly practical and immediate for users	❌ Requires explicit actions by users
Version Control	❌ Lacks version control; cannot easily retrieve past states	✔️ Can implement version control for retrieving previous states
Implementation Effort	✔️ Minimal implementation required	❌ High complexity and significant development effort required


### Decision

We have decided to implement an automatic saving. We want to follow our minimalistic approach and also the full version control would introduce significant implementation effort/complexity - in comparison to a rather marginal benefit - in other words the resources required in comparison to its value is not worth it.




































---

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
