import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
import pickle
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'csv_file', 'encoded_dataset.csv')
scaler_path = os.path.join(base_dir, 'scaler.pkl')

with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)



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

        data = [0] * len(column_names)
        data[0] = int(age)
        data[1] = int(avg_time)
        data[2] = int(week_back)
        data[33] = int(degree)
        data[50] = int(cs_bg)
        data[53] = int(holidays)
        data[54] = int(graduate)
        data[55] = int(designation)

        df = pd.DataFrame([data], columns=column_names)

        df = encode_domain(df, domain)

        df = encode_experience(df, experience)

        df = encode_skills(df, skills)

        sc_data = scale_data(df)

        return sc_data

def encode_domain(df, domain):
    for col in df.columns:
        if domain == col:
            df[col] = 1

    return df

def encode_experience(df, experience):
    if experience == "it":
        df['experience_1'] = 1
    elif experience == "nit":
        df['experience_2'] = 1

    return df

def encode_skills(df, skills):
    for skill in skills:
        if skill in df.columns:
            df[skill] = 1

    return df

def scale_data(df):
    scaled_data = scaler.transform(df)

    return scaled_data