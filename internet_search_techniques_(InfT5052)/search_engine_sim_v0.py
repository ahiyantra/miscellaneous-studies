import re

# Constants
DAMPING_FACTOR = 0.85  # Standard damping factor used in PageRank
K = 1 - DAMPING_FACTOR  # Probability of random jump

# Sample documents
DOCS = [
    "This is DSV homepage. DSV is a joint department between SU and KTH. We have many good students here.",
    "Hi! This is Eriks homepage at DSV, a joint department owned by SU and KTH. I don't play football, but I have a link to Nikos at DSV.",
    "This is studentexpedition at DSV. We have nothing about football, sorry. But we have a link to Eriks page instead",
    "Hi! This is Nikos' homepage at DSV. I like DSV, but even more I like football. I, Nikos, am a big fan of football, I play football all the time. And I also have a Nikos' link to Eriks page.",
    "This is AIK website. We all play football here. We think football rocks. And we have no links to anybody else, we think we are the best anyway."
]

def text_similarity(query, document):
    """
    Calculate text similarity between query and document
    Similar to the original JavaScript implementation
    """
    # Convert text to lowercase and split into words
    doc_words = re.split(r'\W+', document.lower()) if document else []
    query_words = re.split(r'\W+', query.lower())
    
    # Create frequency dictionaries
    doc_freq = {}
    query_freq = {}
    
    # Count word frequencies
    for word in doc_words:
        if word:
            doc_freq[word] = doc_freq.get(word, 0) + 1
            
    for word in query_words:
        if word:
            query_freq[word] = query_freq.get(word, 0) + 1
    
    # Get all unique words
    all_words = set(doc_freq.keys()) | set(query_freq.keys())
    
    # Calculate similarity sum
    sum_val = 0
    N = len(doc_freq)  # Total number of unique words in document
    
    for word in all_words:
        q = query_freq.get(word, 0)
        d = doc_freq.get(word, 0)
        sum_val += q * d
    
    # Calculate final similarity
    sim = sum_val / N if N > 0 else 0
    print(f" sim(q, d) =>> {sum_val}/{N}  = {sim}")
    return sim

def page_rank_initial():
    """
    Calculate initial PageRank values for the documents
    """
    PR_EXTERNAL = 0.1004
    PR_A = PR_B = PR_C = PR_D = PR_E = 0
    
    # Perform iterations to update PageRank values
    for _ in range(100):
        new_PR_A = K + DAMPING_FACTOR * ((PR_B / 2) + (PR_C / 2) + (PR_D / 4))
        new_PR_B = K + DAMPING_FACTOR * ((PR_A / 3) + (PR_C / 2) + (PR_D / 4) + PR_EXTERNAL)
        new_PR_C = K + DAMPING_FACTOR * ((PR_A / 3) + (PR_D / 4))
        new_PR_D = K + DAMPING_FACTOR * ((PR_A / 3) + (PR_B / 2))
        new_PR_E = K + DAMPING_FACTOR * (PR_D / 4)
        
        # Update values for next iteration
        PR_A, PR_B, PR_C, PR_D, PR_E = new_PR_A, new_PR_B, new_PR_C, new_PR_D, new_PR_E
    
    return [PR_A, PR_B, PR_C, PR_D, PR_E]

def page_rank_final():
    """
    Calculate final PageRank values after re-linking
    """
    PR_EXTERNAL = 0.1004
    PR_A = PR_B = PR_C = PR_D = PR_E = 0
    
    # Perform iterations to update PageRank values
    for _ in range(100):
        new_PR_A = K + DAMPING_FACTOR * (PR_D / 4)
        new_PR_B = K + DAMPING_FACTOR * ((PR_C / 2) + (PR_D / 4) + PR_EXTERNAL)
        new_PR_C = K + DAMPING_FACTOR * ((PR_A / 3) + (PR_B / 2) + (PR_D / 4))
        new_PR_D = K + DAMPING_FACTOR * ((PR_A / 3) + (PR_C / 2))
        new_PR_E = K + DAMPING_FACTOR * ((PR_D / 4) + (PR_A / 3) + (PR_B / 2))
        
        # Update values for next iteration
        PR_A, PR_B, PR_C, PR_D, PR_E = new_PR_A, new_PR_B, new_PR_C, new_PR_D, new_PR_E
    
    return [PR_A, PR_B, PR_C, PR_D, PR_E]

def main():
    QUERY = "DSV football"
    
    # 1. Text similarity
    print("1. Text similarity")
    text_sim = text_similarity(QUERY, " ".join(DOCS))
    print(f"Text similarity is {text_sim:.5f}")
    print("------------")
    
    # 2. Initial Page Rank
    print("2. Page rank")
    PR_A, PR_B, PR_C, PR_D, PR_E = page_rank_initial()
    print(f"PR(A) = {PR_A:.5f}, PR(B) = {PR_B:.5f}, PR(C) = {PR_C:.5f}, PR(D) = {PR_D:.5f}, PR(E) = {PR_E:.5f}")
    avg = (PR_A + PR_B + PR_C + PR_D + PR_E) / 5
    print(f"AVG = {avg:.5f}")
    print("------------")
    
    # 3. Combining Text Similarity with Page Rank
    print("3. Combining Text Similarity with Page Rank")
    
    # Calculate individual similarities
    sim_q_A = text_similarity(QUERY, DOCS[0])
    sim_q_B = text_similarity(QUERY, DOCS[1])
    sim_q_C = text_similarity(QUERY, DOCS[2])
    sim_q_D = text_similarity(QUERY, DOCS[3])
    sim_q_E = text_similarity(QUERY, DOCS[4])
    
    # Calculate SIM1 scores
    SIM1_A = sim_q_A + 0.5 * PR_A
    SIM1_B = sim_q_B + 0.5 * PR_B
    SIM1_C = sim_q_C + 0.5 * PR_C
    SIM1_D = sim_q_D + 0.5 * PR_D
    SIM1_E = sim_q_E + 0.5 * PR_E
    
    # Create and sort results
    results = [
        {'document': 'A', 'SIM1': SIM1_A},
        {'document': 'B', 'SIM1': SIM1_B},
        {'document': 'C', 'SIM1': SIM1_C},
        {'document': 'D', 'SIM1': SIM1_D},
        {'document': 'E', 'SIM1': SIM1_E}
    ]
    results.sort(key=lambda x: x['SIM1'], reverse=True)
    
    # Print ordered documents
    print("Ordered Documents based on SIM1:")
    for item in results:
        print(f"Document {item['document']}: SIM1 = {item['SIM1']:.5f}")
    
    # 4. Re-linking the Documents
    print("------------")
    print("4. Re-linking the Documents")
    new_PR_A, new_PR_B, new_PR_C, new_PR_D, new_PR_E = page_rank_final()
    
    print("New page ranking")
    print(f"PR(A) = {new_PR_A:.5f}, PR(B) = {new_PR_B:.5f}, PR(C) = {new_PR_C:.5f}, PR(D) = {new_PR_D:.5f}, PR(E) = {new_PR_E:.5f}")
    
    # Calculate new SIM2 scores
    SIM2_A = sim_q_A + 0.5 * new_PR_A
    SIM2_B = sim_q_B + 0.5 * new_PR_B
    SIM2_C = sim_q_C + 0.5 * new_PR_C
    SIM2_D = sim_q_D + 0.5 * new_PR_D
    SIM2_E = sim_q_E + 0.5 * new_PR_E
    
    # Create and sort new results
    results2 = [
        {'document': 'A', 'SIM': SIM2_A},
        {'document': 'B', 'SIM': SIM2_B},
        {'document': 'C', 'SIM': SIM2_C},
        {'document': 'D', 'SIM': SIM2_D},
        {'document': 'E', 'SIM': SIM2_E}
    ]
    results2.sort(key=lambda x: x['SIM'], reverse=True)
    
    # Print ordered documents
    print("Ordered Documents based on SIM2:")
    for item in results2:
        print(f"Document {item['document']}: SIM2 = {item['SIM']:.5f}")

if __name__ == "__main__":
    main()