# GitHub Pages Setup Instructions

## Automatic Setup via API (Failed)

The GitHub CLI in the Cloud Agent environment does not have sufficient permissions to enable Pages:

```bash
$ gh api -X POST repos/ahalvors/weighhere/pages -f build_type=workflow
# Result: HTTP 403 "Resource not accessible by integration"
```

## Manual Setup Required

**To enable GitHub Pages for this repository:**

1. Navigate to the repository settings page:
   - Go to https://github.com/ahalvors/weighhere
   - Click the **"Settings"** tab (in the repository navigation bar)

2. In the left sidebar, scroll down to the **"Code and automation"** section

3. Click **"Pages"**

4. Under **"Build and deployment"**:
   - **Source**: Select **"GitHub Actions"** from the dropdown
   - (The default "Deploy from a branch" will NOT work with the existing `.github/workflows/pages.yml` workflow)

5. Click **"Save"** (if a save button appears)

6. The page should show:
   - "Your site is ready to be published at `https://ahalvors.github.io/weighhere/`"
   - The `.github/workflows/pages.yml` workflow will run automatically on the next push to `main` (or can be manually triggered)

## Verification

Once enabled, you can verify:
- The Pages workflow runs successfully: https://github.com/ahalvors/weighhere/actions
- The site is live at: https://ahalvors.github.io/weighhere/

## Notes

- The `.github/workflows/pages.yml` file already exists and is configured correctly
- No changes to the workflow file are needed
- After initial setup, all future pushes to `main` will auto-deploy
