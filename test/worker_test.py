import iterm2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PROJECT_PATH

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Create a new tab
    window = app.current_terminal_window
    if window is None:
        print("No current terminal window found. Creating a new one.")
        window = await app.async_create_window()
    tab = await window.async_create_tab()
    await tab.async_set_title("Novu Worker")

    # Navigate to the project directory
    session = tab.current_session

    await session.async_send_text(f"cd {PROJECT_PATH}\n")
    await session.async_send_text("pnpm --filter @novu/worker start:test\n")

iterm2.run_until_complete(main)
