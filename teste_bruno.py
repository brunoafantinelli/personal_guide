import pandas as pd

path = 'G:/.shortcut-targets-by-id/12HqQ7QBUhWovpFcR6cL8QKGhBWAnBVth/gh_dw_tables/'

candidate_custom_fields = pd.read_csv(path + 'candidate_custom_fields.csv', sep = ";")

candidate_custom_fields_list = ['Mindsight - Raciocinio', 'Mindsight - Social', 'Mindsight - Fit Cultural', '[Comercial] Participação em grupo de jovens']

candidate_custom_fields = candidate_custom_fields[
        candidate_custom_fields['custom_field'].isin(candidate_custom_fields_list)]

candidate_custom_fields = candidate_custom_fields.drop_duplicates(['candidate_id', 'custom_field'])

candidate_custom_fields = candidate_custom_fields[['candidate_id', 'custom_field', 'display_value']]

candidate_custom_fields = candidate_custom_fields.pivot_table(
                            index='candidate_id',
                            columns='custom_field',
                            values='display_value',
                            aggfunc=lambda x: ' '.join(str(v) for v in x))

candidate_custom_fields = candidate_custom_fields.reset_index(drop = False)

candidate_custom_fields.to_csv('C:/Users/bruno.fantinelli/Desktop/candidate_custom_fields_REPORT.csv', index=False)

#teste_end
