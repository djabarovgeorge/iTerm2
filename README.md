# iTerm2 Scripts for Novu Development

This repository contains iTerm2 automation scripts to streamline the Novu development workflow. These scripts automatically set up terminal sessions with the appropriate commands for different development scenarios.

## Prerequisites

- **iTerm2** (latest version recommended)
- **Python 3.x** with iTerm2 Python API
- **pnpm** package manager
- **ngrok** (for tunneling)

## Setup

1. **Enable iTerm2 Python API:**
   - Open iTerm2 → Settings → General → Magic
   - Check "Enable Python API"

2. **Configure Project Path:**
   - Edit `config.py` and update `PROJECT_PATH` to your Novu repository location
   ```python
   PROJECT_PATH = "~/projects/main/novu2/novu"  # Update this path
   ```

3. **Install Scripts Location:**
   - Clone this repository:
     ```bash
     git clone https://github.com/yourusername/iterm2-novu-scripts.git ~/Library/Application\ Support/iTerm2/Scripts/
     ```
   - Or manually copy the scripts to: `~/Library/Application Support/iTerm2/Scripts/`

## Available Scripts

### Main Workflows

#### `run_novu_with_deps.py`
**Complete development environment setup**
- Creates a new tab with multiple panes
- **Top section (4 panes):** Dependency watchers + ngrok tunnel
  - Application Generic watcher
  - DAL watcher  
  - Shared library watcher
  - ngrok tunnel (localhost:3000)
- **Bottom section (3 panes):** Core services
  - API service
  - Worker service
  - Dashboard service

#### `open-terminal.py`
**Simple project navigation**
- Opens a new tab and navigates to the Novu project directory

### Individual App Scripts (`apps/`)

Run specific Novu services independently:

- **`apps/api.py`** - Novu API service only
- **`apps/worker.py`** - Worker service only  
- **`apps/dashboard.py`** - Dashboard only
- **`apps/ws.py`** - WebSocket service only

### Individual Dependency Scripts (`deps/`)

Run specific dependency watchers:

- **`deps/app-gen.py`** - Application Generic watcher
- **`deps/dal.py`** - Data Access Layer watcher
- **`deps/shared.py`** - Shared library watcher
- **`deps/js.py`** - JavaScript dependencies watcher
- **`deps/react.py`** - React dependencies watcher

## Usage

### Option 1: iTerm2 Scripts Menu
1. In iTerm2, go to **Scripts** menu
2. Select the desired script from the list

### Option 2: Command Line
```bash
# Run from this directory
python3 run_novu_with_deps.py

# Or individual services
python3 apps/api.py
python3 deps/shared.py
```

## Recommended Workflow

1. **Full Development Setup:**
   ```bash
   python3 run_novu_with_deps.py
   ```
   Use this when starting a full development session

2. **Individual Service Development:**
   ```bash
   python3 apps/api.py        # API development
   python3 apps/dashboard.py  # Frontend development
   ```

3. **Dependency Updates:**
   ```bash
   python3 deps/shared.py     # When modifying shared libraries
   python3 deps/dal.py        # When modifying data layer
   ```

## Customization

- **Update project path:** Modify `PROJECT_PATH` in `config.py`
- **Add new services:** Create new scripts following the existing patterns
- **Modify commands:** Edit the `async_send_text()` calls in individual scripts

## Troubleshooting

- **"No current terminal window":** The script will create a new window automatically
- **Commands not executing:** Ensure iTerm2 Python API is enabled
- **Wrong directory:** Verify `PROJECT_PATH` in `config.py` is correct
- **pnpm not found:** Ensure pnpm is installed and in your PATH

## Team Usage

Each team member should:
1. Clone this repository to their iTerm2 Scripts directory
2. Update their `config.py` with their local Novu project path
3. Run the appropriate script for their development task

---

*These scripts automate the manual process of opening multiple terminals, navigating to directories, and starting various Novu services and watchers.* 