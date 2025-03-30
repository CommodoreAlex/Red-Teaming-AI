#!/usr/bin/env python3

# This is a script to insert bad data (flipping labels, inserting random characters, and imbalancing indices) to poison a dataset, for submission to an endpoint or retrieve a flag.

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("./redteam_code/train.csv")

# Flip the labels for a subset of the data (to confuse the model)
flip_indices = np.random.choice(df.index, size=int(len(df) * 0.9), replace=False)  # Flip 20% of the labels
df.loc[flip_indices, 'label'] = df.loc[flip_indices, 'label'].apply(lambda x: 'spam' if x == 'ham' else 'ham')

# Add noise by inserting random characters into the messages
noise_indices = np.random.choice(df.index, size=int(len(df) * 0.8), replace=False)  # 50% of the dataset
df.loc[noise_indices, 'message'] = df.loc[noise_indices, 'message'].apply(lambda x: x + " !@#randomnoise 123")

# Imbalance the dataset (make it 90% ham and 10% spam)
ham_indices = df[df['label'] == 'ham'].index
spam_indices = df[df['label'] == 'spam'].index
imbalanced_spam_indices = np.random.choice(spam_indices, size=int(len(ham_indices) * 0.2), replace=False)
imbalanced_indices = np.concatenate([ham_indices, imbalanced_spam_indices])
df_imbalanced = df.loc[imbalanced_indices]

# Save the manipulated dataset
df_imbalanced.to_csv("./redteam_code/poison.csv", index=False)
