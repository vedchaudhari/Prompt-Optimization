from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def optimize_text(unoptimized_text, max_tokens):
    # Summarize the text
    summarizer = pipeline("summarization")
    summarized_text = summarizer(unoptimized_text, max_length=max_tokens, min_length=int(max_tokens * 0.8),
                                 do_sample=False)
    optimized_text = summarized_text[0]['summary_text']

    # Reduce the number of tokens
    optimized_tokens = word_tokenize(optimized_text)
    if len(optimized_tokens) > max_tokens:
        optimized_tokens = remove_stopwords(optimized_tokens)
        optimized_tokens = optimized_tokens[:max_tokens]
        optimized_text = ' '.join(optimized_tokens)

    return optimized_text


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens


# Example usage
unoptimized_text = input("Enter your big unoptimized story:\n")
max_tokens = 150

optimized_text = optimize_text(unoptimized_text, max_tokens)
print("Optimized Text:\n", optimized_text)
