# GitHub Actions Setup - Visual Guide

## Option 1: Automated Setup (Recommended)

### Using PowerShell (Windows)
```powershell
# Navigate to workspace
cd C:\workspace

# Run setup script
.\setup-actions.ps1

# Follow prompts to:
# 1. Authenticate with GitHub (if needed)
# 2. Create GitHub token
# 3. Add token as secret
# Done! ✅
```

### Using Bash (Mac/Linux)
```bash
# Navigate to workspace
cd /path/to/workspace

# Run setup script
bash setup-actions.sh

# Follow prompts
# Done! ✅
```

---

## Option 2: Manual Setup (Web UI)

### Step 1️⃣: Go to Repository Settings

```
URL: https://github.com/Warrafeeq/agent-system-2026/settings
```

**Visual Guide:**
```
1. Open browser
2. Go to: https://github.com/Warrafeeq/agent-system-2026
3. Click "Settings" tab (top right)
4. You should see:
   ├─ General (selected)
   ├─ Collaborators
   ├─ Environments
   ├─ Secrets and variables
   ├─ Actions
   ├─ Security & analysis
   └─ ... more options
```

---

### Step 2️⃣: Navigate to Actions

```
In left sidebar under "Code and automation":
├─ Actions
   ├─ General        ← You are here
   ├─ Runners
   ├─ Caches
   └─ ...
```

**Click: "Actions" → "General"**

---

### Step 3️⃣: Enable All Actions

You should see this section:

```
┌─────────────────────────────────────────┐
│ ACTIONS PERMISSIONS                     │
├─────────────────────────────────────────┤
│                                         │
│ ☐ Disable all actions                   │
│                                         │
│ ⦿ Allow all actions and reusable       │  ← SELECT THIS
│   workflows                             │
│                                         │
│ ☐ Allow actions created by GitHub      │
│                                         │
│ ☐ Allow specified actions and reusable │
│   workflows                             │
│                                         │
└─────────────────────────────────────────┘
```

**Action**: Click the radio button for "Allow all actions and reusable workflows"

---

### Step 4️⃣: Save Changes

```
Scroll to bottom of page
↓
Click green "Save" button
↓
You should see: "Settings saved" confirmation
```

---

### Step 5️⃣: Add GitHub Token Secret

Go to: `https://github.com/Warrafeeq/agent-system-2026/settings/secrets/actions`

**Visual Guide:**
```
1. Click "New repository secret"

2. Fill in:
   Name:  GITHUB_TOKEN
   Value: (paste your token here)

3. Click "Add secret"

4. You should see GITHUB_TOKEN listed with ✅
```

**To create the token:**
```
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Name: "Agent-System-2026"
4. Select scopes:
   ☑ repo (full control of repositories)
   ☑ workflow (GitHub Actions workflows)
5. Generate
6. Copy token (you won't see it again!)
```

---

### Step 6️⃣: Verify Workflows are Enabled

Go to: `https://github.com/Warrafeeq/agent-system-2026/actions`

You should see:

```
┌──────────────────────────────────────┐
│ WORKFLOWS                            │
├──────────────────────────────────────┤
│                                      │
│ ✅ Daily Repository Scan & Analysis  │
│    (workflow file detected)           │
│                                      │
│ ✅ Daily Project Generator           │
│    (workflow file detected)           │
│                                      │
└──────────────────────────────────────┘
```

Both should show green checkmarks ✅

---

## Step 7️⃣: Test First Run (Optional)

```
1. Go to Actions tab
2. Click "Daily Repository Scan & Analysis"
3. Click "Run workflow" button
4. Select branch: main
5. Click "Run workflow"
6. Watch execution in real-time ✅
```

---

## ✅ Success Checklist

- [ ] Settings → Actions → General enabled
- [ ] GITHUB_TOKEN secret added
- [ ] Both workflows visible in Actions tab
- [ ] Both workflows show green checkmarks
- [ ] (Optional) Test run completed successfully

---

## 🚀 Ready!

Your system will now:
- Run automatically tomorrow at 9 AM UTC
- Create reports and projects daily
- Learn and improve continuously
- Scan all your repositories
- Provide recommendations

**Timeline:**
```
Today (now)     - Setup complete
Tomorrow 9 AM   - First scan runs ✅
Tomorrow 10 AM  - Projects generated ✅
Next 30 days    - Daily automation
```

---

## 📞 Troubleshooting

### Workflows Don't Show

**Solution:**
1. Go to `.github/workflows/` folder
2. Verify both YAML files are there
3. Workflows must be pushed to main branch
4. Try: git push origin main

### "Allow all actions" button not visible

**Solution:**
1. Repository owner must have correct permissions
2. May need to enable in organization settings first
3. Try: Settings → Actions → General (scroll down)

### Token Secret Not Added

**Solution:**
1. Create new token: https://github.com/settings/tokens
2. Must have `repo` and `workflow` scopes
3. Add to: Settings → Secrets and variables → Actions
4. Name exactly: `GITHUB_TOKEN`

### Workflows Not Running

**Solution:**
1. Verify Actions is enabled
2. Verify workflows are in `.github/workflows/`
3. Verify they're on main branch
4. Try manual trigger first
5. Check workflow syntax

---

## 📖 Quick Links

| Action | Link |
|--------|------|
| Repository | https://github.com/Warrafeeq/agent-system-2026 |
| Settings | https://github.com/Warrafeeq/agent-system-2026/settings |
| Actions | https://github.com/Warrafeeq/agent-system-2026/actions |
| Actions Settings | https://github.com/Warrafeeq/agent-system-2026/settings/actions |
| Secrets | https://github.com/Warrafeeq/agent-system-2026/settings/secrets/actions |
| GitHub CLI | https://cli.github.com/ |
| Create Token | https://github.com/settings/tokens |

---

## 🎯 Next Steps

**Choose one:**

### ✅ Quick Setup (Automated)
```
Run: .\setup-actions.ps1
Follow prompts
Done! ✅
```

### ✅ Manual Setup (Web UI)
```
Follow steps above
Done! ✅
```

Either way, your agent will be live tomorrow! 🚀
