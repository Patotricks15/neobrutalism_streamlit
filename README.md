# Streamlit Neobrutalism Components

## Overview

This project is a demonstration of how to build a Streamlit application using a neobrutalism design aesthetic. The goal is to showcase various built-in Streamlit components—such as text input, text area, slider, date input, and more—with a bold, high-contrast style characterized by strong black borders and pronounced drop shadows.

## Project Structure

~~~
my_streamlit_app/
├── app.py
├── streamlit.toml
└── css/
    ├── general.css
    └── components.css
~~~

- **app.py:** The main application file that assembles the various components into the Streamlit app.
- **streamlit.toml:** A configuration file to set the app theme, including the primary color.
- **css/general.css:** Contains global styles for the body, containers, and titles.
- **css/components.css:** Contains component-specific overrides to apply the neobrutalism style.

## Objective

The primary objective of this project is to illustrate how custom CSS can be used to re-style Streamlit components to achieve a unique neobrutalism aesthetic. This includes:

- **Custom Styling:** Applying external CSS to modify borders, shadows, and focus effects.
- **Component Customization:** Demonstrating how to target and style specific components (e.g., text inputs, number inputs, select boxes) with a consistent design language.
- **Maintainability:** Organizing CSS into separate files for a cleaner project structure and easier future modifications.
- **Theme Integration:** Configuring the primary theme color in `streamlit.toml` to further integrate the custom style with the native Streamlit theming.

## Usage

1. **Install Streamlit:**  
   Ensure that you have Python and Streamlit installed.

   ```bash
   pip install streamlit

2. **Run the Application:**
    In your project directory, run the following command:

    ```bash
   pip install streamlit

3. **Experience the Design:**
    The app will launch in your browser, showcasing a range of neobrutalism-styled components.