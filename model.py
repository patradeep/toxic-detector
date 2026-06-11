from functools import lru_cache

from transformers import pipeline
import re


@lru_cache(maxsize=1)
def get_classifier():
    return pipeline("text-classification", model="unitary/toxic-bert")

# Custom bad words (Indian context)
bad_words = ["pagal", "chutiya", "boka", "faltu", "idiot", "stupid","nudes","nude","sex","sexy","ass","bitch","dick","pussy","slut","whore","dumb","fool","sucker","loser","jerk","bastard","douchebag","motherfucker","crap","damn"]

def clean_text(text):
    text = text.lower()
    text = text.replace("1", "i").replace("0", "o")
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def has_bad_word(text):
    return any(word in text for word in bad_words)

def predict(text):
    cleaned = clean_text(text)

    classifier = get_classifier()
    result = classifier(cleaned)[0]
    label = result['label']
    score = result['score']
    
    # Convert label to toxicity score
    toxicity_score = score if label == "toxic" else 1 - score

    # Boost score if custom bad word found
    if has_bad_word(cleaned):
        toxicity_score = min(1.0, toxicity_score + 0.2)

    return {
        "input": text,
        "cleaned": cleaned,
        "toxicity_score": round(toxicity_score, 3),
        "is_toxic": toxicity_score > 0.5
    }