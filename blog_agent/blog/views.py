import base64
import os
from django.shortcuts import render
import json
import requests
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
from .forms import GenerateForm
from django.http import HttpResponse, JsonResponse
from django.conf import settings 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def BlogPage(request):
    if request.method == 'GET':
        form = GenerateForm()
    return render(request, 'BlogApp.html', {'form': form})


def GenerateTitles(request):
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            area_of_work = form.cleaned_data['area_of_work']
            keywords = form.cleaned_data['keywords']

            prompt = f"""You are a content writer. Generate a single blog title about {keywords} tailored for an 
            IT company's blog. The purpose of these blogs is to provide in-depth knowledge on the topic specifically targeted at technical persons like developers. 
            Each title should reflect a specific aspect or subtopic of {area_of_work} that would be of interest to developers, 
            offering insights, tips, or tutorials to enhance their understanding and skills."""

            response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2048 
            )
            generated_title = response.choices[0].text.strip()
            generated_title = generated_title.replace('"', '')
            return JsonResponse({'success': True, 'generated_title': generated_title})
    else:
        form = GenerateForm()

    return render(request, 'BlogApp.html', {'form': form})


def GenerateContent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        area_of_work = data['area_of_work']
        keywords = data['keywords']
        generated_title = data['generated_title'] 
        blog_content = f"""Write a detailed blog post based on the title **{generated_title}** 
                The purpose of this blog is to provide technical persons like developers with comprehensive knowledge and practical guidance on the crucial aspect
                of data preprocessing in the context of {keywords}. The blog should delve into various best practices, optimization strategies, 
                and expert tips aimed at helping developers enhance their skills in handling data preprocessing tasks effectively for AI projects.
                Ensure the content is informative, engaging, and tailored to meet the needs of 
                developers seeking to improve their proficiency in this essential area of {area_of_work} development. The blog should contain around 500 words."""

        blog_response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=blog_content,
        max_tokens=2048 
        )
        generated_blog = blog_response.choices[0].text.strip()
        print(generated_blog)
        return JsonResponse({'success': True, 'content': generated_blog})

    

def GenerateImage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keywords = data['keywords']
        generated_title = data['generatedTitle'] 
        image_prompt = f"""Create an engaging and informative image to complement the blog titled 
                        {generated_title} The image should visually convey the essence of data preprocessing in {keywords}, showcasing key concepts, techniques, or tools discussed in the blog. 
                        Consider using graphical representations such as flowcharts, diagrams, or illustrations to illustrate the data preprocessing pipeline, common preprocessing tasks,
                        and optimization strategies. Incorporate visual elements that resonate with developers and enhance their understanding of the topic, ensuring the image is clear,
                        concise, and visually appealing. Strive to make the image informative, eye-catching, and aligned with the content of the blog to enrich the reader's experience and reinforce key concepts effectively."""

        response = client.images.generate(
                    model="dall-e-3",
                    prompt=image_prompt,
                    size="1024x1024",
                    quality="hd",
                    n=1,
                    )
        generated_image = response.data[0].url
        # generated_image = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sqZmRoUCvVPG4XjsLLBnpLmv/user-j43yEsk3jxgJPiR6MJDt0IJ6/img-oUW2THzt3q4B6tzuvgbpBQld.png?st=2024-04-25T14%3A11%3A23Z&se=2024-04-25T16%3A11%3A23Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-04-24T19%3A15%3A53Z&ske=2024-04-25T19%3A15%3A53Z&sks=b&skv=2021-08-06&sig=/K9ZMNnEIa9wHu6yZxbuTMKo80F%2Bq5yWMpa4cUWxh/Y%3D"
        print(generated_image)
        response = requests.get(generated_image, stream=True)
        generated_title_name = generated_title.replace(" ","_")
        file_name = os.path.join(settings.MEDIA_ROOT, generated_title_name)
        file_name = file_name + ".png"
        with open(file_name, "wb") as f:
            f.write(response.content)
        generated_title_img = generated_title_name+'.png'
        return JsonResponse({'success': True, 'content': generated_title_img})

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        keywords = request.data.get('keywords')
        title = request.data.get('title')



        if not (keywords and title):
            return Response({'error': 'Missing keywords or title parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # ChatGPT API request for titles (adjust parameters as needed)
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        params = {
            "model": "text-davinci-003",  # Adjust model as needed
            "prompt": f"Generate three creative titles related to the keywords: {keywords}",
            "max_tokens": 100,
            "n": 3,
            "stop": None,
            "temperature": 0.7,  # Adjust for creative vs. factual content
        }
        response = requests.post(url, headers=headers, json=params)

        if response.status_code == 200:
            data = json.loads(response.text)
            titles = [choice['text'].strip() for choice in data['choices']]

            # Use the chosen title (or any from the list) for content generation
            chosen_title = title or titles[0]  # Adjust based on user preference

            # LangChain content generation (adjust parameters as needed)
            content = model.generate_text(
                prompt=f"Write some engaging content related to the title: {chosen_title}",
                temperature=0.7,  # Adjust for style and factuality
                max_length=500,  # Adjust for content length
            )

            return Response({'titles': titles, 'content': content})
        else:
            return Response({'error': 'Error generating titles'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
