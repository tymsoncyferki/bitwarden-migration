# bitwarden-migration

Small desktop application that helps with the migration of passwords to Bitwarden.

# Problem

While exporting passwords from chrome new record in csv is created for each website URI (e.g. for Google it can
be "https://accounts.google.com/", "https://accounts.google.com/ServiceLogin"
and "https://accounts.google.com/ServiceLoginAuth"). Because of that we keep 300 records of passwords instead of 150.

# Solution

But Bitwarden can keep multiple URIs connected to the particular login and password. And that is what my app does - it
aggregates the data and convert it to the bitwarden format. The app is open-source, user-friendly and works 100%
offline, so it is completely safe.

# Development

Planning to add more browser formats

# App

After opening the app you can see the main (and only) menu:

![Photo1](https://github.com/tymsoncyferki/bitwarden-migration/blob/main/readme_files/bit1.png)

Usage:
1. Choose import format e.g. Bitwarden or Chrome
2. Upload your csv file (app checks if it is in correct format)
3. Run the algorithm by clicking "process"
4. Save the cleaned file to your local machine.
5. The file is ready to be imported to Bitwarden!

![Photo1](https://github.com/tymsoncyferki/bitwarden-migration/blob/main/readme_files/bit2.png)
