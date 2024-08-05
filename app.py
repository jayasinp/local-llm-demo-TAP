#import gradio as gr
#from transformers import pipeline

# GPT 2 model -> absolute garbage
# Load a pre-trained language model
#model = pipeline('text-generation', model='gpt2')

#def generate_text(prompt):
    # Generate text with the model
    #result = model(prompt, max_length=50, num_return_sequences=1)
    #return result[0]['generated_text']

# Create a Gradio interface
#iface = gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Local LLM Interface Demo")

# Launch the interface
#iface.launch()

################################################################################
#GPT Neo 125M -> still garbage
#import gradio as gr
#from transformers import pipeline

# Load a pre-trained GPT-Neo model
#model = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

#def generate_text(prompt):
    # Generate text with the model
    #result = model(prompt, max_length=50, num_return_sequences=1)
    #return result[0]['generated_text']

# Create a Gradio interface
#iface = gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Local LLM Interface with GPT-Neo")

# Launch the interface
#iface.launch()
###############################################################################

# T5 for summarization
import gradio as gr
from transformers import pipeline

# Load a pre-trained T5 model for summarization
summarizer = pipeline('summarization', model='t5-small')

def summarize_text(prompt):
    # Generate summary with the model
    result = summarizer(prompt, max_length=50, min_length=25, do_sample=False)
    return result[0]['summary_text']

# Create a Gradio interface
iface = gr.Interface(fn=summarize_text, inputs="text", outputs="text", title="Summarization Interface")

# Launch the interface
iface.launch()



