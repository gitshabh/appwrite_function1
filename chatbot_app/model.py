import tensorflow as tf

from transformers import TFAutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = TFAutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

def getResponse(prompt) :
    # Encode user input
    user_input = prompt
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='tf')

    chat_history_ids = None

    # Append new user input tokens to the chat history
    if chat_history_ids is not None:
        bot_input_ids = tf.concat([chat_history_ids, new_user_input_ids], axis=-1)
    else:
        bot_input_ids = new_user_input_ids

    # Generate a response while limiting the total chat history to 1000 tokens
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Pretty print the last output tokens from the bot
    return "DialoGPT: {}".format(tokenizer.decode(chat_history_ids[0, bot_input_ids.shape[-1]:].numpy(), skip_special_tokens=True))




