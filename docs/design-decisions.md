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


### Decision

We have decided to implement an automatic saving. We want to follow our minimalistic approach and also the full version control would introduce significant implementation effort/complexity - in comparison to a rather marginal benefit - in other words the resources required in comparison to its value is not worth it.







# 02: Fixing heavy lag when using marker & eraser feature on the workspace

### Meta

Status
: Work in progress - **Decided** - Obsolete  

Updated
: 14-Feb-2025  

### Problem statement  

The marking and erasing feature on the workspace canvas is experiencing significant lagingg during use. Since the workspace is supposed to provide and intuitive and fluid experience, we must decide on a solution that improves performance while ensuring that the workspace remains fluid and responsive without compromising any other essential functionalities.

### Regarded options  

| Criterion | Dedicated Drawing Worker (drawing-worker.js) | Reduce Canvas Size |
| --- | --- | --- | --- |
| **Performance** | ✔️ Yes, offloads rendering work from the main thread | ✔️ Yes, less pixels need to be rendered |
| **Data Persistence** | ❌ Drawing layer is separate from the main HTML and not stored in the database | ✔️ No impact on how data persistence |
| **User Experience** | ✔️ Smooth drawing & erasing experience | ❌ Users feels restricted due to smaller workspace |
| **Implementation Complexity** | ❌ Requires additional worker script & logic to sync with workspace | ✔️ Simple adjustment in CSS & JS |

### Decision  

We have decided to implement a dedicated drawing worker (drawing-worker.js). The main reason for this decision is that reducing the workspace canvas size would negatively impact user experience, making the workspace feel restrictive. 



