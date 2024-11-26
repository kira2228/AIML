import pandas as pd
import itertools
states = ['sleeping','eating','coughing']
hidden_states = ['healthy', 'sick']
pi = [0.5,0.5]
a_df = pd.DataFrame({
    'healthy' :[0.7,0.3],
    'sick' :[0.4,0.6]
},index=hidden_states)
b_df=pd.DataFrame({
    'sleeping':[0.2,0.4],
    'eating':[0.6,0.1],
    'coughing':[0.2,0.5]
},index=hidden_states)
def simple_HMM(observed_seq):
    total_prob=0
    all_hidden_sequences=list(itertools.product(hidden_states,repeat=len(observed_seq)))
    for hidden_seq in all_hidden_sequences:
        prob = pi[hidden_states.index(hidden_seq[0])]*b_df[observed_seq[0]][hidden_seq[0]]
        for t in range(1, len(observed_seq)):
            prob *= a_df[hidden_seq[t-1]][hidden_seq[t]]*b_df[observed_seq[t]][hidden_seq[t]]
        total_prob += prob
    return total_prob
def simple_viterbi(observed_seq):
    best_prob = 0
    best_path = None
    all_hidden_sequences = list(itertools.product(hidden_states,repeat=len(observed_seq)))
    for hidden_seq in all_hidden_sequences:
        prob = pi[hidden_states.index(hidden_seq[0])]*b_df[observed_seq[0]][hidden_seq[0]]
        for t in range(1, len(observed_seq)):
            prob *= a_df[hidden_seq[t-1]][hidden_seq[t]]*b_df[observed_seq[t]][hidden_seq[t]]
        if prob > best_prob:
            best_prob = prob
            best_path = hidden_seq
    return best_prob,best_path
observed_seq = ['coughing','coughing','coughing']
print("HMM Total probability",simple_HMM(observed_seq))
print("Viterbi best path",simple_viterbi(observed_seq))
