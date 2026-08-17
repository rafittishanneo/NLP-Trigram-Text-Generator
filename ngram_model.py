import nltk
import re
import math
import collections
import random
from nltk.corpus import gutenberg

nltk.download('gutenberg', quiet=True)
raw_text = gutenberg.raw('shakespeare-caesar.txt')
print(f"Raw text length: {len(raw_text)}")


#step 1--------------------------------------------
def preprocess_text(text: str) -> list[str]:
    # Lowercase
    text = text.lower()
    # Remove punctuation, keep letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # Tokenize and strip empty strings
    tokens = [word.strip() for word in text.split() if word.strip()]
    return tokens

tokens = preprocess_text(raw_text)
vocab = list(set(tokens))  # Unique words for V
vocab_size = len(vocab)
print(f"Vocabulary size: {vocab_size}")
print(f"Total tokens: {len(tokens)}")
print("Sample:", tokens[:10])  # e.g., ['friends', 'romans', 'countrymen']



#step 2---------------------------------------------
def preprocess_text(text: str) -> list[str]:
    # Lowercase
    text = text.lower()
    # Remove punctuation, keep letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # Tokenize and strip empty strings
    tokens = [word.strip() for word in text.split() if word.strip()]
    return tokens

tokens = preprocess_text(raw_text)
vocab = list(set(tokens))  # Unique words for V
vocab_size = len(vocab)
print(f"Vocabulary size: {vocab_size}")
print(f"Total tokens: {len(tokens)}")
print("Sample:", tokens[:10])  # e.g., ['friends', 'romans', 'countrymen']




#step 3----------------------------------------------
import collections

def build_trigram_model(tokens: list[str]) -> dict:
    trigram_counts = collections.defaultdict(lambda: collections.Counter())
    # NO padding - raw tokens only as per assignment
    for i in range(len(tokens) - 2):
        context = (tokens[i], tokens[i+1])
        next_word = tokens[i+2]
        trigram_counts[context][next_word] += 1
    return dict(trigram_counts)

# Now call it (this will work)
trigram_counts = build_trigram_model(tokens)
print(f"Trigram contexts: {len(trigram_counts)}")  
print("Sample:", dict(list(trigram_counts.items())[:2]))




#step 4---------------------------------------------
def laplace_smoothing(trigram_counts: dict, vocab_size: int) -> dict:
    smoothed_probs = {}
    for context, counter in trigram_counts.items():
        total_context = sum(counter.values())
        smoothed_probs[context] = {}
        for next_word, count in counter.items():
            prob = (count + 1) / (total_context + vocab_size)
            smoothed_probs[context][next_word] = prob
    return smoothed_probs

smoothed_probs = laplace_smoothing(trigram_counts, 3014)
print(f"Smoothed contexts: {len(smoothed_probs)}")
print("Sample probs:")
sample_context = next(iter(smoothed_probs))
print(f"{sample_context}: {dict(list(smoothed_probs[sample_context].items())[:3])}")




#step 5--------------------------------------------------
def generate_text(seed: list[str], smoothed_probs: dict, vocab: list[str], num_words: int = 30) -> str:
    story = seed[:]
    while len(story) < num_words:
        context = tuple(story[-2:])
        if context in smoothed_probs and smoothed_probs[context]:
            # Greedy: pick highest probability next word
            next_word = max(smoothed_probs[context], key=smoothed_probs[context].get)
        else:
            # Unseen context: random vocab word
            next_word = random.choice(vocab)
        story.append(next_word)
    return ' '.join(story)

seed = ['the', 'king']
story = generate_text(seed, smoothed_probs, vocab)
print(f"Seed: {' '.join(seed)}")
print(f"Generated ({len(story.split())} words): {story}")




#Step 6-------------------------------------------------------
import math

def compute_perplexity(test_tokens: list[str], smoothed_probs: dict, vocab_size: int) -> float:
    # Pad test sentence for trigrams
    padded_test = ['<s>', '<s>'] + test_tokens  # But use real probs
    N = len(test_tokens) - 2  # Trigrams in test
    if N <= 0:
        return float('inf')
    
    log_prob_sum = 0.0
    for i in range(2, len(padded_test)):
        context = tuple(padded_test[i-2:i])  # ('<s>', '<s>'), ('<s>', 'the'), etc.
        word = padded_test[i]
        
        if context in smoothed_probs and word in smoothed_probs[context]:
            prob = smoothed_probs[context][word]
        else:
            # Unseen: uniform Laplace 1/V
            prob = 1.0 / vocab_size
        prob = max(prob, 1e-10)  # Avoid log(0)
        log_prob_sum += math.log(prob)
    
    perplexity = math.exp(-log_prob_sum / N)
    return perplexity

# Test on assignment example
test_sentence = "the king is dead"
test_tokens = preprocess_text(test_sentence)
ppl = compute_perplexity(test_tokens, smoothed_probs, 3014)
print(f"Test sentence: {test_sentence}")
print(f"Perplexity: {ppl:.2f}")






#step 7--------------------------------------------------------
import nltk
import re
import math
import collections
import random
from nltk.corpus import gutenberg

nltk.download('gutenberg', quiet=True)
raw_text = gutenberg.raw('shakespeare-caesar.txt')

# ===== ALL 5 REQUIRED FUNCTIONS =====

def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = [word.strip() for word in text.split() if word.strip()]
    return tokens

def build_trigram_model(tokens: list[str]) -> dict:
    trigram_counts = collections.defaultdict(lambda: collections.Counter())
    for i in range(len(tokens) - 2):
        context = (tokens[i], tokens[i+1])
        next_word = tokens[i+2]
        trigram_counts[context][next_word] += 1
    return dict(trigram_counts)

def laplace_smoothing(trigram_counts: dict, vocab_size: int) -> dict:
    smoothed_probs = {}
    for context, counter in trigram_counts.items():
        total_context = sum(counter.values())
        smoothed_probs[context] = {}
        for next_word, count in counter.items():
            prob = (count + 1) / (total_context + vocab_size)
            smoothed_probs[context][next_word] = prob
    return smoothed_probs

def generate_text(seed: list[str], smoothed_probs: dict, vocab: list[str], num_words: int = 30) -> str:
    story = seed[:]
    while len(story) < num_words:
        context = tuple(story[-2:])
        if context in smoothed_probs and smoothed_probs[context]:
            next_word = max(smoothed_probs[context], key=smoothed_probs[context].get)
        else:
            next_word = random.choice(vocab)
        story.append(next_word)
    return ' '.join(story)

def compute_perplexity(test_tokens: list[str], smoothed_probs: dict, vocab_size: int) -> float:
    N = len(test_tokens) - 2
    if N <= 0:
        return float('inf')
    log_prob_sum = 0.0
    for i in range(2, len(test_tokens)):
        context = (test_tokens[i-2], test_tokens[i-1])
        word = test_tokens[i]
        if context in smoothed_probs and word in smoothed_probs[context]:
            prob = smoothed_probs[context][word]
        else:
            prob = 1.0 / vocab_size
        prob = max(prob, 1e-10)
        log_prob_sum += math.log(prob)
    perplexity = math.exp(-log_prob_sum / N)
    return perplexity

# ===== MAIN EXECUTION =====
tokens = preprocess_text(raw_text)
vocab = list(set(tokens))
vocab_size = len(vocab)
trigram_counts = build_trigram_model(tokens)
smoothed_probs = laplace_smoothing(trigram_counts, vocab_size)

print("Preprocessing")
print(f"Vocabulary size: {vocab_size}")
print(f"Total tokens: {len(tokens)}")

print("\nText Generation - Laplace Smoothing")
seed = ['the', 'king']
story = generate_text(seed, smoothed_probs, vocab)
print(f"Seed: {' '.join(seed)}")
print(f"Generated: {story}")

print("\nPerplexity")
test_tokens = preprocess_text("the king is dead")
ppl = compute_perplexity(test_tokens, smoothed_probs, vocab_size)
print(f"Test sentence: the king is dead")
print(f"Perplexity: {ppl:.2f}")
