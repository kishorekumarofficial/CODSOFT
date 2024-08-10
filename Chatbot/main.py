import re
import long_responses as lr


def calculate_match_score(input_message, target_words, exact_match=False, mandatory_words=None):
    if mandatory_words is None:
        mandatory_words = []
        
    word_match_count = sum(1 for word in input_message if word in target_words)
    mandatory_words_present = all(word in input_message for word in mandatory_words)

    match_percentage = word_match_count / len(target_words) if target_words else 0

    return int(match_percentage * 100) if mandatory_words_present or exact_match else 0


def evaluate_all_messages(user_input):
    response_scores = {}

    def add_response(possible_response, keywords, exact_match=False, mandatory_words=None):
        if mandatory_words is None:
            mandatory_words = []
            
        response_scores[possible_response] = calculate_match_score(user_input, keywords, exact_match, mandatory_words)

    # Predefined responses ---------------------------------------------------------------------------------------------
    add_response('Greetings!', ['hello', 'hi', 'hey'], exact_match=True)
    add_response('Goodbye!', ['bye', 'goodbye'], exact_match=True)
    add_response('I\'m well, how about you?', ['how', 'are', 'you', 'doing'], mandatory_words=['how'])
    add_response('You\'re welcome!', ['thank', 'thanks'], exact_match=True)

    # Extended responses
    add_response(lr.R_ADVICE, ['give', 'advice'], mandatory_words=['advice'])
    add_response(lr.R_EATING, ['what', 'you', 'eat'], mandatory_words=['you', 'eat'])

    optimal_response = max(response_scores, key=response_scores.get)
    
    return lr.unknown() if response_scores[optimal_response] < 1 else optimal_response


def generate_reply(user_text):
    processed_input = re.split(r'\s+|[,;?!.-]\s*', user_text.lower())
    best_response = evaluate_all_messages(processed_input)
    return best_response


# Chatbot loop for testing
if __name__ == "__main__":
    while True:
        print('Bot: ' + generate_reply(input('You: ')))