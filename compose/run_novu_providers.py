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
    await tab.async_set_title("Novu Dependencies")

    # Navigate to the project directory
    session = tab.current_session

    paneHorizontal = session

    depPanel1 = paneHorizontal
    await depPanel1.async_send_text(f"cd {PROJECT_PATH}\n")
    await depPanel1.async_send_text(f"pnpm --filter @novu/providers build\n")
    
    depPanel2 = await depPanel1.async_split_pane(vertical=True)
    await depPanel2.async_send_text(f"cd {PROJECT_PATH}\n")
    await depPanel2.async_send_text(f"pnpm --filter @novu/stateless build\n")

    depPanel3 = await depPanel2.async_split_pane(vertical=True)
    await depPanel3.async_send_text(f"cd {PROJECT_PATH}/packages/shared\n")
    await depPanel3.async_send_text(f"pnpm --filter @novu/ee-api build\n")

    # depPanel4 = await depPanel3.async_split_pane(vertical=True)
    # await depPanel4.async_send_text("ngrok http http://localhost:3000\n")

iterm2.run_until_complete(main)
