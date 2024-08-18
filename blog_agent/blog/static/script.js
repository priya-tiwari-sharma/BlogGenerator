const csrfToken = document.getElementById('csrf_token').value; // Fetch from hidden field

const generateForm = document.getElementById('generate-form');
const generatedTitleElement = document.getElementById('generated-title');
const generatedContentDiv = document.getElementById('generated-content');
const generateContentBtn = document.getElementById('generate-content-btn');
const generateImageDiv = document.getElementById('generate-image');
const generateImageBtn = document.getElementById('generate-image-btn');


// generate title
generateForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(generateForm);
    const areaOfWork = formData.get('area_of_work');
    const keywords = formData.get('keywords');
    console.log("data----------------")
    const response = await fetch('/generate_title/', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (data.success) {
      
        
        generatedTitleElement.innerText = data.generated_title; // Update content on success
    } else {
        
        generatedTitleElement.innerText = '<p>Error generating content.</p>';
    }
});
//  generate content
generateContentBtn.addEventListener('click', async () => {
    const generatedTitle = generatedTitleElement.innerText;

    if (!generatedTitle) {
        alert('Please generate a title first!');
        return;
    }

    const areaOfWork = document.querySelector('[name="area_of_work"]').value; 
    const keywords = document.querySelector('[name="keywords"]').value;

    const data = {
        'area_of_work': areaOfWork,
        'keywords': keywords,
        'generated_title': generatedTitle
    };
    console.log(data)
    const response = await fetch('/generate_content/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrfToken } // Include CSRF token manually
    });

    const contentData = await response.json();

    if (contentData.success) {
        generatedContentDiv.innerHTML = contentData.content.replace(/\n/g, '<br>');
    } else {
        generatedContentDiv.innerHTML = '<p>Error generating content.</p>';
    }
});

// generate image

const keywords = document.querySelector('[name="keywords"]').value;
generateImageBtn.addEventListener('click', async () => {
  const generatedTitle = generatedTitleElement.innerText;

  if (!generatedTitle) {
    alert('Please generate a title first!');
    return;
  }

const response = await fetch('/generate_image/', {
    method: 'POST',
    body: JSON.stringify({ 'generatedTitle': generatedTitle ,'keywords':keywords}),
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrfToken } // Include CSRF token manually
  });

  const imageData = await response.json();

  if (imageData.success) {
    const imageUrl = imageData.content;
    document.getElementById('generated-image').src = imageUrl;
    // // Create an image element
    // const image = document.createElement('img');
    // image.setAttribute('src', imageUrl);
    // image.setAttribute('alt', 'Generated Image')
    // console.log(image)
    // generateImageDiv.appendChild(image);
  } else {
    alert('Error generating image!');
  }
});

// copy button
const copyContentBtn = document.getElementById('copy-content-btn');

copyContentBtn.addEventListener('click', async () => {
const contentToCopy = generatedContentDiv.innerHTML.replace(/\n/g, '<br>');
navigator.clipboard.writeText(contentToCopy) 
    .then(() => {
    alert('Content copied to clipboard!');
    })
    .catch(() => {
    alert('Failed to copy content!');
    });
});
// $.ajaxSetup({
//   beforeSend: function(xhr) {
//     xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
//   }
// });