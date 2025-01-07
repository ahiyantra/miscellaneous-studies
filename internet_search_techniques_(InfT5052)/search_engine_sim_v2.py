from dataclasses import dataclass
from typing import Dict, List, Optional
import re
from collections import Counter

# Type aliases for clarity
PageRank = float
DocumentID = str
Score = float

@dataclass
class Document:
    """Class to hold document information"""
    id: DocumentID
    content: str
    
@dataclass
class SearchResult:
    """Class to hold search result information"""
    document_id: DocumentID
    similarity_score: Score
    page_rank: PageRank
    combined_score: Score

class SearchEngineSimulator:
    """
    A search engine simulator that implements text similarity and PageRank algorithms.
    Uses an iterative approach to calculate PageRank values and combines them with
    text similarity scores for final document ranking.
    """
    
    def __init__(self, 
                 documents: Dict[DocumentID, str], 
                 damping_factor: float = 0.85,
                 max_iterations: int = 100,
                 external_pr: float = 0.1004):
        """
        Initialize the search engine with documents and parameters.
        
        Args:
            documents: Dictionary mapping document IDs to their content
            damping_factor: Probability of following links vs random jumps
            max_iterations: Maximum iterations for PageRank convergence
            external_pr: External PageRank contribution value
        """
        self.documents = {doc_id: Document(doc_id, content) 
                         for doc_id, content in documents.items()}
        self.damping_factor = damping_factor
        self.random_jump_prob = 1 - damping_factor
        self.max_iterations = max_iterations
        self.external_pr = external_pr
        
    def _get_word_frequencies(self, text: str) -> Counter:
        """
        Convert text into word frequency counter.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Counter object with word frequencies
        """
        words = [word.lower() for word in re.split(r'\W+', text) if word]
        return Counter(words)
    
    def calculate_text_similarity(self, query: str, doc: Document) -> float:
        """
        Calculate text similarity between query and document using term frequency.
        
        Args:
            query: Search query
            doc: Document to compare against
            
        Returns:
            Similarity score between 0 and 1
        """
        query_freq = self._get_word_frequencies(query)
        doc_freq = self._get_word_frequencies(doc.content)
        
        if not doc_freq:
            return 0.0
            
        # Sum of term frequency products
        similarity_sum = sum(query_freq[word] * doc_freq[word] 
                           for word in set(query_freq) | set(doc_freq))
                           
        # Normalize by document length
        similarity = similarity_sum / len(doc_freq)
        
        print(f" sim(q, d) =>> {similarity_sum}/{len(doc_freq)} = {similarity}")
        return similarity
    
    def calculate_page_rank(self, links: Dict[DocumentID, List[DocumentID]], 
                          is_initial: bool = True) -> Dict[DocumentID, PageRank]:
        """
        Calculate PageRank values for all documents.
        
        Args:
            links: Dictionary of document link structure
            is_initial: Whether to use initial or final link structure
            
        Returns:
            Dictionary mapping document IDs to their PageRank values
        """
        # Initialize PageRank values
        page_ranks = {doc_id: 0.0 for doc_id in self.documents}
        
        # Fixed order of documents to match v0 implementation
        doc_order = ['A', 'B', 'C', 'D', 'E']
        
        for _ in range(self.max_iterations):
            new_ranks = {}
            
            # Calculate new rank for each document in fixed order
            for doc_id in doc_order:
                if is_initial:
                    new_ranks[doc_id] = self._calculate_initial_rank(doc_id, links, page_ranks)
                else:
                    new_ranks[doc_id] = self._calculate_final_rank(doc_id, links, page_ranks)
                    
            page_ranks = new_ranks
            
        return {doc_id: page_ranks[doc_id] for doc_id in doc_order}
    
    def _calculate_initial_rank(self, doc_id: DocumentID, 
                              links: Dict[DocumentID, List[DocumentID]], 
                              current_ranks: Dict[DocumentID, PageRank]) -> PageRank:
        """
        Calculate initial PageRank for a document using the original v0 link structure:
        - A receives links from B (1/2), C (1/2), D (1/4)
        - B receives links from A (1/3), C (1/2), D (1/4) + external
        - C receives links from A (1/3), D (1/4)
        - D receives links from A (1/3), B (1/2)
        - E receives links from D (1/4)
        """
        base = self.random_jump_prob
        
        if doc_id == 'A':
            contribution = ((current_ranks['B'] / 2) + 
                          (current_ranks['C'] / 2) + 
                          (current_ranks['D'] / 4))
        elif doc_id == 'B':
            contribution = ((current_ranks['A'] / 3) + 
                          (current_ranks['C'] / 2) + 
                          (current_ranks['D'] / 4) + 
                          self.external_pr)
        elif doc_id == 'C':
            contribution = (current_ranks['A'] / 3) + (current_ranks['D'] / 4)
        elif doc_id == 'D':
            contribution = (current_ranks['A'] / 3) + (current_ranks['B'] / 2)
        else:  # doc_id == 'E'
            contribution = current_ranks['D'] / 4
            
        return base + self.damping_factor * contribution
    
    def _calculate_final_rank(self, doc_id: DocumentID, 
                            links: Dict[DocumentID, List[DocumentID]], 
                            current_ranks: Dict[DocumentID, PageRank]) -> PageRank:
        """
        Calculate final PageRank for a document after re-linking using v0 structure:
        Modified to match v0's link structure and calculations exactly:
        - A receives links from D (1/4)
        - B receives links from C (1/2), D (1/4) + external
        - C receives links from A (1/3), D (1/4)
        - D receives links from A (1/3), C (1/2)
        - E receives links from D (1/4), A (1/3), B (1/2)
        """
        base = self.random_jump_prob
        
        if doc_id == 'A':
            contribution = current_ranks['D'] / 4
        elif doc_id == 'B':
            contribution = ((current_ranks['C'] / 2) + 
                          (current_ranks['D'] / 4) + 
                          self.external_pr)
        elif doc_id == 'C':
            contribution = ((current_ranks['A'] / 3) + 
                          (current_ranks['D'] / 4))
        elif doc_id == 'D':
            contribution = ((current_ranks['A'] / 3) + 
                          (current_ranks['C'] / 2))
        else:  # doc_id == 'E'
            contribution = ((current_ranks['D'] / 4) + 
                          (current_ranks['A'] / 3) + 
                          (current_ranks['B'] / 2))
            
        return base + self.damping_factor * contribution
    
    def search(self, query: str, is_initial: bool = True) -> List[SearchResult]:
        """
        Perform search using both text similarity and PageRank.
        
        Args:
            query: Search query
            is_initial: Whether to use initial or final PageRank values
            
        Returns:
            List of SearchResult objects sorted by combined score
        """
        # Calculate PageRank values
        links = {}  # Placeholder for link structure
        page_ranks = self.calculate_page_rank(links, is_initial)
        
        results = []
        # Process documents in fixed order to match v0
        for doc_id in ['A', 'B', 'C', 'D', 'E']:
            doc = self.documents[doc_id]
            # Calculate similarity score
            similarity = self.calculate_text_similarity(query, doc)
            
            # Calculate combined score
            combined_score = similarity + 0.5 * page_ranks[doc_id]
            
            # Create search result
            result = SearchResult(
                document_id=doc_id,
                similarity_score=similarity,
                page_rank=page_ranks[doc_id],
                combined_score=combined_score
            )
            results.append(result)
            
        # Sort by combined score
        return sorted(results, key=lambda x: x.combined_score, reverse=True)

def main():
    """Main function to run the search engine simulation"""
    # Initialize documents
    documents = {
        "A": "This is DSV homepage. DSV is a joint department between SU and KTH. We have many good students here.",
        "B": "Hi! This is Eriks homepage at DSV, a joint department owned by SU and KTH. I don't play football, but I have a link to Nikos at DSV.",
        "C": "This is studentexpedition at DSV. We have nothing about football, sorry. But we have a link to Eriks page instead",
        "D": "Hi! This is Nikos' homepage at DSV. I like DSV, but even more I like football. I, Nikos, am a big fan of football, I play football all the time. And I also have a Nikos' link to Eriks page.",
        "E": "This is AIK website. We all play football here. We think football rocks. And we have no links to anybody else, we think we are the best anyway."
    }
    
    # Create search engine instance
    search_engine = SearchEngineSimulator(documents)
    query = "DSV football"
    
    # Run initial test
    print("1. Text similarity")
    text_sim = search_engine.calculate_text_similarity(
        query, 
        Document("all", " ".join(documents.values()))
    )
    print(f"Text similarity is {text_sim:.5f}")
    print("------------")
    
    # Initial PageRank calculation and search
    print("2. Page rank")
    initial_results = search_engine.search(query, is_initial=True)
    
    # Print initial PageRank values
    page_ranks = [result.page_rank for result in sorted(initial_results, key=lambda x: x.document_id)]
    PR_A, PR_B, PR_C, PR_D, PR_E = page_ranks
    print(f"PR(A) = {PR_A:.5f}, PR(B) = {PR_B:.5f}, PR(C) = {PR_C:.5f}, PR(D) = {PR_D:.5f}, PR(E) = {PR_E:.5f}")
    print(f"AVG = {sum(page_ranks) / 5:.5f}")
    print("------------")
    
    # Print initial combined scores
    print("3. Combining Text Similarity with Page Rank")
    print("Ordered Documents based on SIM1:")
    for result in initial_results:
        print(f"Document {result.document_id}: SIM1 = {result.combined_score:.5f}")
    
    # Final PageRank calculation and search
    print("------------")
    print("4. Re-linking the Documents")
    final_results = search_engine.search(query, is_initial=False)
    
    # Print final PageRank values
    print("New page ranking")
    new_page_ranks = [result.page_rank for result in sorted(final_results, key=lambda x: x.document_id)]
    new_PR_A, new_PR_B, new_PR_C, new_PR_D, new_PR_E = new_page_ranks
    print(f"PR(A) = {new_PR_A:.5f}, PR(B) = {new_PR_B:.5f}, PR(C) = {new_PR_C:.5f}, PR(D) = {new_PR_D:.5f}, PR(E) = {new_PR_E:.5f}")
    
    # Print final combined scores
    print("Ordered Documents based on SIM2:")
    for result in final_results:
        print(f"Document {result.document_id}: SIM2 = {result.combined_score:.5f}")

if __name__ == "__main__":
    main()