import numpy as np
from hmmlearn import hmm

def create_isolated_model(start_prob, trans_mat, emission_mat):
    model = hmm.MultinomialHMM(n_components=len(start_prob))
    model.startprob_ = np.array(start_prob)
    model.transmat_ = np.array(trans_mat)
    model.emissionprob_ = np.array(emission_mat)
    return model

# 'EV' Modeli Parametreleri [cite: 12-16, 18]
model_ev = create_isolated_model(
    [1.0, 0.0], 
    [[0.6, 0.4], [0.2, 0.8]], 
    [[0.7, 0.3], [0.1, 0.9]]
)

# 'OKUL' Modeli (Temsili Deðerler) [cite: 23]
model_okul = create_isolated_model(
    [1.0, 0.0],
    [[0.7, 0.3], [0.1, 0.9]],
    [[0.4, 0.6], [0.8, 0.2]]
)

# Test Verisi: [High, Low, Low] -> index [0, 1, 1] [cite: 33]
test_data = np.array([[0, 1, 1]]).T
score_ev = model_ev.score(test_data)
score_okul = model_okul.score(test_data)

print(f"EV Modeli Log-Likelihood: {score_ev}")
print(f"OKUL Modeli Log-Likelihood: {score_okul}")
print(f"Sonuç: {'EV' if score_ev > score_okul else 'OKUL'}")
