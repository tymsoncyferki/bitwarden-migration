import pandas as pd


class Data:

    def __init__(self, file_path, file_type):
        self.df = pd.read_csv(file_path)
        assert file_type in ['Bitwarden', 'Chrome']
        self.file_type = file_type

    def verify(self):
        if self.file_type == 'Bitwarden':
            return all(self.df.columns == ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                           'login_uri', 'login_username', 'login_password', 'login_totp'])
        if self.file_type == 'Chrome':
            return all(self.df.columns == ['name', 'url', 'username', 'password', 'note'])

    def aggregate(self):
        if self.file_type == 'Chrome':
            bitwarden_df = pd.DataFrame(columns=['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                                 'login_uri', 'login_username', 'login_password', 'login_totp',
                                                 'additional'])
            bitwarden_df[['name', 'login_username']] = self.df[['name', 'username']]  # todo: add more columns
            # todo: set type to login

        self.df['login_uri'].fillna(value='', inplace=True)
        # todo: cannot aggregate on notes
        finaldata = self.df.groupby(
            ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt', 'login_username',
             'login_password', 'login_totp'], dropna=False)['login_uri'].apply(', '.join).reset_index()