---
title: Design Decisions
nav_order: 4
---


{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>



{: .no_toc }
# Design decisions






All of the decisions listed below were taken in agreement between the two group members:
https://github.com/oezcanemre and https://github.com/schulz115


# 01: Saving procedure - automatic vs manual saving

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










# 03: Theme Selection for Workspaces – Admin-Controlled vs. User-Defined

### Meta  

Status
: Work in progress - **Decided** - Obsolete  
Updated: 14-Feb-2025  

### Problem statement  

We need to determine how the workspace theme (background theme) should be set. There are two main options: Either admin-controlled themes wher admin sets a single theme for all collaboratiors or 2. User-defined themes where each user selects their theme in the settings, which applies only to their view..

### Regarded options  

| Criterion | Admin-Controlled Theme | User-Defined Theme |
| --- | --- | --- |
| **User Freedom** | ❌ Users cant personalize their workspace experience | ✔️ Each user can select a theme on their own |
| **Administrative Control** | ✔️ Aligns with our decision to give admins high authority over workspace settings | ❌ Reduces admin influence over the workspace environment |
| **Implementation Complexity** | ✔️ Straightforward, the theme is globally set | ❌ Requires additional logic to apply different themes per user |


### Decision  

We have decided on the admin to control the theme. This decision aligns with our minimalistic approach and putting big focus on the adming role and less on the end user role by granting admins full authority over workspace management. It also maintains a unified experience for collaboration. 









# 04: Adding Collaborators – Admin-Assigned vs. Invitation-Based  

### Meta  

Status
: Work in progress - **Decided** - Obsolete  
Updated
: 14-Feb-2025  

### Problem statement  

We must decide how users should be added as collaborators to a workspace. This impacts the control admins have and how users experience being added to a workspace.  

The two options are:  
1. Admin-Assigned – The admin directly adds users as collaborators, without requiring their consent.  
2. Invitation-Based – The admin generates an invite link that users must accep* before joining the workspace.  


### Regarded options  

| Criterion | Admin-Assigned | Invitation-Based |
| --- | --- | --- |
| **Efficiency** | ✔️ Convenient and instant access, no extra steps required | ❌ Requires users to manually accept the invitation |
| **User Autonomy** | ❌ Users have no control over being added | ✔️ Users can choose themselves whether they want to join |
| **Administrative Control** | ✔️ Aligns with the decision to grant admins full control over workspaces | ❌ Admins depend on users accepting invitations |

### Decision  

We have decided to allow admins to directly add collaborators to workspaces. This reinforces the admin's authority, and takes load off of the "simple" user aligning with our previous design choice, admin-controlled themes. It ensures fast and efficient onboarding, preventing workspaces from being stalled due to unaccepted invitations.  

Our goal is to prioritize ease of use and reduce unnecessary steps. The admin-first approach remains our guiding principle.






