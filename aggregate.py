import pandas as pd


class Data:

    def __init__(self, file_path, file_type):
        self.input_df = pd.read_csv(file_path)
        assert file_type in ['Bitwarden', 'Chrome']
        self.file_type = file_type
        self.output_df = None
        self.rows_removed = None

    def verify(self):
        if self.file_type == 'Bitwarden':
            assert len(self.input_df.columns) == 11
            assert all(self.input_df.columns == ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                                 'login_uri', 'login_username', 'login_password', 'login_totp'])
        if self.file_type == 'Chrome':
            assert len(self.input_df.columns) == 5
            assert all(self.input_df.columns == ['name', 'url', 'username', 'password', 'note'])

    def aggregate(self):
        bitwarden_df = pd.DataFrame(columns=['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                                             'login_uri', 'login_username', 'login_password', 'login_totp'])
        if self.file_type == 'Bitwarden':
            bitwarden_df = self.input_df
        elif self.file_type == 'Chrome':
            bitwarden_df[['name', 'notes', 'login_uri', 'login_username', 'login_password']] = self.input_df[
                ['name', 'note', 'url', 'username', 'password']]
            bitwarden_df['type'] = 'login'
        size = len(bitwarden_df)

        bitwarden_df['login_uri'].fillna(value='', inplace=True)
        bitwarden_df['notes'].fillna(value='', inplace=True)
        finaldata = bitwarden_df.groupby(
            ['folder', 'favorite', 'type', 'name', 'fields', 'reprompt', 'login_username', 'login_password',
             'login_totp'], dropna=False).agg({'login_uri': ', '.join, 'notes': ' '.join}).reset_index()
        finaldata['notes'] = finaldata['notes'].str.strip()
        self.rows_removed = size - len(finaldata)
        finaldata = finaldata[['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt',
                               'login_uri', 'login_username', 'login_password', 'login_totp']]
        print(finaldata.columns.values)
        self.output_df = finaldata.copy()
