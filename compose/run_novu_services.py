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
    await tab.async_set_title("Novu Services")

    # Navigate to the project directory
    session = tab.current_session

    # Split into 3 panes and run commands
    pane1 = session
    pane2 = await pane1.async_split_pane(vertical=True)
    pane3 = await pane2.async_split_pane(vertical=True)

    # Run the commands in each pane
    await pane1.async_send_text(f"cd {PROJECT_PATH}\n")
    await pane1.async_send_text("pnpm start:api:dev\n")
    
    await pane2.async_send_text(f"cd {PROJECT_PATH}\n")
    await pane2.async_send_text("pnpm start:worker\n")
    
    await pane3.async_send_text(f"cd {PROJECT_PATH}\n")
    await pane3.async_send_text("pnpm start:dashboard\n")

iterm2.run_until_complete(main)
