# Poppy_s - Diagnostic Robotics Backend App Assignment

## Introducing "Poppy's" - A SciFi Intro

**Golden Circle** (by **Kingsman, Taylor & Statesman, LeCurie LLC**) [incorporation pending] are proud to present:

By Appoinment to Her Imperial Majesty The Emperess of the Star Empire of Manticore
Manufacturers and Developers of Advanced Medical Technologies (Golden Circle)
**Poppy's!  "Saving Lives - Legalize! - One Verified Prescription at a Time!"**

Kingsman, Taylor & Statesman, LeCurie LLC is a wholly owned subsidiery of **Stacey Hauptman & Blackbird Ventures Inc.**
of Landing City, Manticore, the Star Empire of Manticore;
a joint venture of the **Hauptman Cartel** and **Grayson (Blackbird) SkyDomes Inc**.

## Installation

- clone the repo
- cd into the directory
- run:
  
    ```bash
        python3 -m venv ./.venv
        . ./.venv/bin/activate
        python3 -m pip install -U -r ./requirements/basic.txt
        python3 -m pip install -U -r ./requirements/requirements.txt
    ```

- to be able to run the notebooks install the dev extra

    ```bash
        python3 -m pip install -U -r ./requirements/dev.txt
    ```

- to build a wheel run:

    ```bash
        python3 -m build
    ```

- to install locally while developing:
    1. run:

        ```bash
            python3 -m pip install -U --editable .
        ```

    2. then run the dev server:

        ```bash
            poppy_s_dev_server
        ```