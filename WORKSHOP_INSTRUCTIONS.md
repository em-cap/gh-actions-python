# 🚀 GitHub Actions Workshop - Simple Build & Deploy

## Workshop Overview (1 Hour)

This workshop teaches you to create a CI/CD pipeline that:
1. **Tests** your Python code
2. **Builds** a Python package 
3. **Deploys** documentation to GitHub Pages

## 📋 Prerequisites

- GitHub account
- Basic Python knowledge
- Understanding of git/GitHub

## 🎯 Learning Objectives

By the end of this workshop, you'll know how to:
- Create GitHub Actions workflows
- Set up automated testing
- Build Python packages
- Deploy static sites to GitHub Pages
- Use job dependencies and conditions

## 🛠️ Workshop Steps

### Step 1: Fork & Enable Actions (5 min)

1. Fork this repository to your GitHub account
2. Go to the **Actions** tab in your fork
3. Click "I understand my workflows, go ahead and enable them"

### Step 2: Enable GitHub Pages & Workflow Permissions (5 min)

1. Go to **Settings** → **Pages**
2. Under "Source", select **GitHub Actions**
3. Save the settings
4. Go to **Settings** → **Actions** → **General**
5. Scroll down to "Workflow permissions"
6. Select **"Read and write permissions"**
7. Check **"Allow GitHub Actions to create and approve pull requests"**
8. Click **Save**

### Step 3: Understand the Workflow (15 min)

Open `.github/workflows/build.yml` and examine:

```yaml
# Three stages that run in sequence:
jobs:
  test:      # Stage 1: Run tests
  build:     # Stage 2: Build package (needs test to pass)
  deploy:    # Stage 3: Deploy docs (needs both test & build)
```

**Key Concepts:**
- **Jobs**: Independent units of work
- **Steps**: Individual commands within a job
- **Dependencies**: `needs:` controls job order
- **Conditions**: `if:` controls when jobs run

### Step 4: Trigger Your First Build (10 min)

1. Make a small change to `README.md`
2. Commit and push to the `main` branch
3. Go to **Actions** tab to watch the workflow run
4. See all three stages execute in order

### Step 5: View Your Deployed Site (5 min)

1. After the workflow completes, go to **Settings** → **Pages**
2. Click the live site URL
3. Your documentation is now live with test results!

### Step 6: Experiment with Changes (15 min)

Try these modifications to see how the pipeline responds:

#### Break the Tests:
```python
# In calculator.py, change line 13 to:
return a + b + 1  # This will break the test!
```
- Push the change
- Watch the workflow fail at the test stage
- Note that build and deploy stages don't run

#### Fix and Add a Feature:
```python
# Add a new method to Calculator class:
def percentage(self, value, percent):
    """Calculate percentage of a value."""
    return (value * percent) / 100
```

#### Add a Test:
```python
# Add to test_calculator.py:
def test_percentage(self):
    """Test percentage calculation."""
    assert self.calc.percentage(100, 50) == 50
    assert self.calc.percentage(200, 25) == 50
```

### Step 7: Customize the Workflow (5 min)

Try these modifications:

#### Add a different Python version:
```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'  # Change from 3.12
```

#### Add a build step that shows package contents:
```yaml
- name: Show package contents
  run: |
    cd dist
    tar -tzf *.tar.gz | head -10
```

## 🎉 Congratulations!

You've successfully created a CI/CD pipeline that:
- ✅ Automatically tests your code
- ✅ Builds Python packages
- ✅ Deploys documentation to GitHub Pages
- ✅ Only deploys when tests pass
- ✅ Provides visual feedback on build status

## 🚀 Next Steps

Want to go further? Try:
- Adding code quality checks (linting)
- Testing multiple Python versions
- Publishing packages to PyPI
- Adding deployment environments
- Using secrets for API keys

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python packaging guide](https://packaging.python.org/)
- [GitHub Pages documentation](https://docs.github.com/en/pages)

## 💡 Workshop Tips

1. **Watch the Actions tab** - It shows real-time progress
2. **Read the logs** - Click on failed steps to see error details
3. **Use the artifact downloads** - Download built packages
4. **Check the live site** - Your docs update automatically
5. **Experiment safely** - GitHub Actions are free for public repos

---

**Happy automating! 🤖**