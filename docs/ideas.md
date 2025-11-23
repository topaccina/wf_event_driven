# Step 0 — Event-Driven Prefect Workflow (Foundation)

## 🎯 Goal
Build the simplest possible **event-driven Prefect workflow** using two independent flows:

- **Flow A**  
  - Manually triggered from Prefect Cloud UI  
  - Generates a random number  
  - Publishes a custom Prefect event  
  - Runs independently of your laptop

- **Flow B**  
  - Automatically triggered by the event emitted from Flow A  
  - Runs on a cloud worker (not on your laptop)  
  - Writes a log that is visible in the Prefect Cloud UI

This step proves the core architecture:  
✔ The project runs entirely in the cloud  
✔ Flows are independent  
✔ Prefect events trigger downstream workflows  
✔ A cloud worker executes the flows even when the laptop is turned off

---

## 🧩 Why This Step Matters
This is the foundation for a larger, fun project about generating **Italian culture “pills”** and sending them to a friend.

Before adding PDFs, Notion pages, S3 files, or newsletters, we first validate that:

- Flow orchestration is working  
- Event-driven triggers are working  
- Cloud execution works without local machines  
- Code is stored in a remote repo or storage location accessible to Prefect Workers

Once this step is stable, we can expand the system safely.

---

## 📦 Requirements for Step 0
To ensure the flows run without your laptop:

1. **Code stored in the cloud**  
   - GitHub repository (recommended)  
   - Or Prefect Storage block  
   - Or container registry

2. **Prefect Cloud account** (free)

3. **Cloud-hosted Prefect Worker**  
   - Heroku Eco plan (works)  
   - Or Render / Railway / Fly.io (free alternatives)

This worker polls Prefect Cloud and executes the flows 24/7.

---

## 🚀 What Success Looks Like
After Step 0:

- You open Prefect Cloud UI  
- Click **Run** on Flow A  
- Flow A runs on a cloud worker  
- It emits an event (e.g., `italy.random.number.generated`)  
- Prefect Cloud automatically starts Flow B  
- Flow B logs something like:

