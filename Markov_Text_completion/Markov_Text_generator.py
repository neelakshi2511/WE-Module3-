import random

def generate(text: str, start_words: list[str], chain_length: int, num_generated: int) -> str:
  """
  Generates text using a Markov chain with a specified chain length.

  Args:
      text: The text content to use for generating new text.
      start_words: A list of words to start the generation with,
                   must have the same length as chain_length.
      chain_length: The length of the Markov chain (number of previous words to consider).
      num_generated: The desired length of the generated text.

  Returns:
      A string containing the generated text.
  """

  words = text.split()

  # Create a dictionary to store transitions for single words
  transitions = {}
  for i in range(len(words) - 1):
    prev_word = words[i]
    next_word = words[i + 1]
    transitions.setdefault(prev_word, []).append(next_word)

  # Generate the text
  output_text = start_words.copy()  # Start with the given starting words
  for _ in range(num_generated - chain_length):
    prev_word = output_text[-1]  # Consider only the last word as context
    next_word = random.choice(transitions.get(prev_word, []))  # Handle unseen words gracefully
    output_text.append(next_word)

  return ' '.join(output_text)
