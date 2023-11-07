# bitwarden-migration

Small desktop application that helps with the migration of passwords to Bitwarden.

# Problem

While exporting passwords from chrome new record in csv is created for each website URI (e.g. for Google it can
be "https://accounts.google.com/", "https://accounts.google.com/ServiceLogin"
and "https://accounts.google.com/ServiceLoginAuth"). Because of that we keep 300 records of passwords instead of 150.

# Solution

But Bitwarden can keep multiple URIs connected to the particular login and password. And that is what my app does - it
aggregates the data and convert it to the bitwarden format. The app is transparent and user-friendly and works 100%
offline, so it is completely safe.

# Development

Planning to add more browser formats

# App
