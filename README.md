# AR Box Game

This is a simple web-based Augmented Reality (AR) game where you can tap a virtual box that appears in your real-world environment. The game is built as a Progressive Web App (PWA) and includes a feature to invite friends using the Facebook SDK.

## Features

-   **AR Gameplay:** Uses A-Frame and AR.js to display a virtual box on a hiro marker.
-   **Simple Game Mechanics:** Tap the box to score points and make it move to a new location.
-   **PWA:** Includes a manifest file and a service worker for a PWA experience.
-   **Facebook Integration:** Allows users to invite their friends to play the game.

## Components

-   **Frontend:** A single `index.html` file containing the game logic, AR scene, and Facebook integration.
-   **Backend:** A simple Python Flask server (`app.py`) that serves the frontend files.

## Dependencies

To run this project, you will need the following dependencies installed:

-   **Python 3:** With the `Flask` library.
-   **A modern web browser** with support for WebRTC and WebGL.
-   **A physical hiro marker** to display the AR content. You can find one by searching for "hiro marker" online.

## How to Run

1.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up Facebook App ID:**
    -   Open the `templates/index.html` file.
    -   Search for `_YOUR_APP_ID_` and replace it with your real Facebook App ID. You will need to create a Facebook App on the [Facebook for Developers](https://developers.facebook.com/) website.

3.  **Run the Flask server:**
    ```bash
    python app.py
    ```

4.  **Open the game:**
    -   Open your web browser and navigate to `http://localhost:8080`.
    -   Allow the browser to access your camera.
    -   Point your camera at a hiro marker to see the game.
