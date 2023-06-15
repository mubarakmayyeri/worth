import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'csv_file', 'encoded_dataset.csv')


def make_df(domain: str, age: int, designation: str, cs_bg: str, experience: str, degree: str, avg_time: int, holidays: str,
            week_back: int, graduate: str, skills: list):

        column_names = ['age', 'avg_time', 'week_back', 'flutter', 'angular', 'python',
                    'express', 'firebase', 'aws', 'sql', 'javascript', 'jwt', 'node',
                    'html', 'hasura', 'communication', 'git', 'jest',
                    'react', 'graphql', 'mongodb', 'cnn', 'dart', 'vim',
                    'django', 'mui', 'typescript', 'next', 'redux', 'api', 'bootstrap', 'tailwind',
                    'docker', 'degree_encoded', 'domain_cybersecurity',
                    'domain_data_science', 'domain_devops', 'domain_frontend_react',
                    'game_developemnt', 'domain_golang', 'domain_machine_learning',
                    'domain_mean', 'domain_mern', 'domain_mob_dev_kotlin',
                    'domain_mobile_development_using_flutter', 'domain_mob_dev_swift',
                    'domain_webdev_nodejs', 'domain_webdev_django',
                    'domain_webdev_django_angular', 'domain_webdev_django_react', 'cs_bg',
                    'experience_1', 'experience_2', 'holidays', 'graduated',
                    'designation_encoded']

        data = [np.nan] * len(column_names)
        data[0] = age
        data[1] = avg_time
        data[2] = week_back
        data[50] = cs_bg
        data[53] = holidays
        data[54] = graduate
        data[55] = designation

        df = pd.DataFrame([data], columns=column_names)
        print(df)

        return df