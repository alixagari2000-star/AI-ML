import gradio as gr
import base64
import io
from PIL import Image
import json
import os
import asyncio
from google import genai
#import google.generativeai as genai

from google.genai import types

# Function to convert PIL Image to bytes
def pil_to_bytes(img, format="PNG"):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()

# Function to load image as base64
async def load_image_base64(img):
    if isinstance(img, str):
        # If image is a URL or file path, load it
        raise ValueError("URL loading not implemented in this version")
    else:
        # If image is already a PIL Image
        return pil_to_bytes(img)

# Main function to generate edited image using Gemini
async def generate_image_gemini(prompt, image, api_key, temperature=0.4):
    SAFETY_SETTINGS = {
        types.HarmCategory.HARM_CATEGORY_HARASSMENT: types.HarmBlockThreshold.BLOCK_NONE,
        types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: types.HarmBlockThreshold.BLOCK_NONE,
        types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: types.HarmBlockThreshold.BLOCK_NONE,
        types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: types.HarmBlockThreshold.BLOCK_NONE,
    }
    
    try:
        # Initialize Gemini client with API key
        client = genai.Client(api_key="AIzaSyAxAUAOJzMhTOY1M5Sb3Hgrma5_XzMvEyM")
        
        # Convert PIL image to bytes
        image_bytes = await load_image_base64(image)
        
        contents = []

        # Add the image to the contents
        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type="image/png",
                    )
                ],
            )
        )
        
        # Add the prompt to the contents
        edit_prompt = f"Edit this image: {prompt}"
        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=edit_prompt),
                ],
            )
        )

        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=temperature,
                safety_settings=[
                    types.SafetySetting(
                        category=category, threshold=threshold
                    ) for category, threshold in SAFETY_SETTINGS.items()
                ],
                response_modalities=['Text', 'Image']
            )
        )
        
        edited_images = []
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_bytes = part.inline_data.data
                edited_images.append(image_bytes)
                
        # Convert the first returned image bytes to PIL image
        if edited_images:
            result_image = Image.open(io.BytesIO(edited_images[0]))
            return result_image
        else:
            return None
            
    except Exception as e:
        print(f"Google GenAI client failed with error: {e}")
        return None

# Function to process the image edit
def process_image_edit(image, prompt, api_key, image_history, temperature):
    if not image or not prompt or not api_key:
        return None, image_history, "Please provide an image, prompt, and API key"
    
    # Store current image in history if not empty
    if image is not None and image_history is None:
        image_history = []
    if image is not None:
        image_history.append(image)
    
    # Run the async function to edit the image
    try:
        edited_image = asyncio.run(generate_image_gemini(prompt, image, api_key, temperature))
        if edited_image:
            return edited_image, image_history, "Image edited successfully"
        else:
            return image, image_history, "Failed to edit image. Please try again."
    except Exception as e:
        return image, image_history, f"Error: {str(e)}"

# Function to undo the last edit
def undo_edit(image_history):
    if image_history and len(image_history) > 1:
        # Remove current image
        image_history.pop()
        # Return the previous image
        return image_history[-1], image_history, "Reverted to previous image"
    else:
        return None, [], "No previous version available"

# Function to set output image as input for continuous editing
def continue_editing(output_image):
    if output_image is not None:
        return output_image, "Ready to continue editing the current image"
    else:
        return None, "No edited image available to continue editing"

# Create Gradio UI
def create_ui():
    with gr.Blocks(title="Gemini Image Editor") as app:
        gr.Markdown("# Gemini Image Editor")
        gr.Markdown("Upload an image, enter a description of the edit you want, and let Gemini do the rest!")
        
        # Store image history in state
        image_history = gr.State([])
        
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(type="pil", label="Upload Image")
                prompt = gr.Textbox(label="Edit Description", placeholder="Describe the edit you want...")
                api_key = gr.Textbox(label="Gemini API Key", placeholder="Enter your Gemini API key", type="password")
                
                # Replace hidden settings with accordion
                with gr.Accordion("Advanced Settings", open=False):
                    temperature = gr.Slider(
                        minimum=0.0, 
                        maximum=2.0, 
                        value=1, 
                        step=0.05, 
                        label="Temperature", 
                        info="Controls randomness in generation (0 = deterministic, 1 = creative, 2 = extreme)"
                    )
                
                with gr.Row():
                    edit_btn = gr.Button("Edit Image")
                    undo_btn = gr.Button("Undo Last Edit")
                    continue_btn = gr.Button("Continue Editing")
                
            with gr.Column():
                output_image = gr.Image(type="pil", label="Edited Image")
                status = gr.Textbox(label="Status", interactive=False)
        
        # Set up event handlers
        edit_btn.click(
            fn=process_image_edit,
            inputs=[input_image, prompt, api_key, image_history, temperature],
            outputs=[output_image, image_history, status]
        )
        
        undo_btn.click(
            fn=undo_edit,
            inputs=[image_history],
            outputs=[output_image, image_history, status]
        )
        
        # Add handler for continue editing button
        continue_btn.click(
            fn=continue_editing,
            inputs=[output_image],
            outputs=[input_image, status]
        )
    
    return app

# Launch the app
if __name__ == "__main__":
    app = create_ui()
    app.launch()