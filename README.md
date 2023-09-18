# Poppy_s - Diagnostic Robotics Backend App Assignment

## Introducing "Poppy's" - A SciFi Intro[^1]

**Golden Circle** (by **Kingsman, Taylor & Statesman, Lee-Curie LLC**) [incorporation pending] are proud to present:

By Appoinment to Her Imperial Majesty The Empress of the Star Empire of Manticore
Manufacturers and Developers of Advanced Medical Technologies (Golden Circle)
**Poppy's!  "Saving Lives - Legalize! - One Verified Prescription at a Time!"**

Kingsman, Taylor & Statesman, Lee-Curie LLC is a wholly owned subsidiery of **Stacey Hauptman & Blackbird Ventures Inc.**
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
            python3 -m pip install -U --editable .[dev]
        ```

    2. then run the dev server:

        ```bash
            # use '--help' to see all the Command Line Options!
            poppy_s_dev_server --help
        ```

    3. then navigate to the `/docs` route of the server address given in the Console.
    4. setup at least one Doctor (use the `/api/v1/doctor/` route in the Swagger UI) 
    5. and One Patient (use the `/api/v1/patient/` route in the Swagger UI).
    6. Now you can add Prescriptions!!

## Notes

### External Copyrights

[^1]: All Names from the "Honor Harrington" Book Series by David Weber and from the "Kingsman: The Golden Circle"(2017) Movie that are/may be trade marked or copyright protected in any way:
    1. Belong to their respective owners,
    2. Are being used under the [Fair Use Clauses of U.S. Copyright Law and Israeli Copyright Law](https://en.wikipedia.org/wiki/Fair_use):
       1. In HOMAGE (See [Homage - Wordnik](https://www.wordnik.com/words/homage) definition 3 and [Homage - Mirriam-Webster](https://www.merriam-webster.com/dictionary/homage) definition 2b)
       2. and in [PARODY](https://en.wikipedia.org/wiki/Parody).