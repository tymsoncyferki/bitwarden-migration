import pandas as pd


class Data:

    def __init__(self, file_path, file_type):
        self.df = pd.read_csv(file_path)
        assert file_type in ['Bitwarden', 'Chrome']
        self.file_type = file_type

    def verify(self):
        if self.file_type == 'Bitwarden':
            assert len(self.df.columns) == 11
            assert all(self.df.columns == ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                           'login_uri', 'login_username', 'login_password', 'login_totp'])
        if self.file_type == 'Chrome':
            assert len(self.df.columns) == 5
            assert all(self.df.columns == ['name', 'url', 'username', 'password', 'note'])

    def aggregate(self):
        bitwarden_df = pd.DataFrame(columns=['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                             'login_uri', 'login_username', 'login_password', 'login_totp',
                                             'additional'])
        if self.file_type == 'Bitwarden':
            bitwarden_df = self.df
        elif self.file_type == 'Chrome':
            bitwarden_df[['name', 'notes', 'login_uri', 'login_username', 'login_password']] = self.df[
                ['name', 'note', 'url', 'username', 'password']]
            bitwarden_df['type'] = 'login'

        bitwarden_df['login_uri'].fillna(value='', inplace=True)
        finaldata = bitwarden_df.groupby(
            ['folder', 'favorite', 'type', 'name', 'fields', 'reprompt', 'login_username', 'login_password',
             'login_totp'], dropna=False).agg({'login_uri': ', '.join, 'notes': ' '.join}).reset_index()
        finaldata['notes'] = finaldata['notes'].str.strip()
